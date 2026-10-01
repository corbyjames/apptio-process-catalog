#!/usr/bin/env python3
"""Build a customer instance of the catalog: base + overlay -> site, docs.

Usage: python3 scripts/build_customer.py <customer-dir>

<customer-dir>/customer.json      the overlay (see docs/customer-overlay.md)
<customer-dir>/assessment/*.json  assessment rounds (latest by filename is baked into the site)
<customer-dir>/review/*.json      optional exported review state (status/verdict/owner/comments)
Outputs under <customer-dir>/:
  site/index.html                 the customer's site (same template as the base)
  site/index.artifact.html        body-only copy for publishing as a Claude artifact
  docs/overview.md                what the overlay does, scope, profile, fiscal calendar, assessment summary
  data/catalog.json               the merged catalog this build used

Overlay semantics: every durable reference is a permanent element ID (P-nnnn, G-nnn).
  profile     {decision_key: [option ids]} - initial profile the site opens with (viewer can still change it)
  overrides   {eid: {field: value}}        - replaces fields on base records (L2 by P-id, L1 by G-id)
  additions   [ {parent: G-id, ...record} ]- customer-specific L2s; eids must be P-9000+ and ids in the parent's numbering
  suppress    [eid]                        - removed from this instance (L2 or whole L1)
  labels      {term: replacement}          - whole-word vocabulary substitutions applied to all record text
  scope       {name, summary, groups:[G-id], eids:[P-id]} - the engagement focus surfaced on the hub and badged on records
"""
import copy, glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import bpmn

MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
TEXT_FIELDS = ["name","description","personas","inputs","outputs","config","cadence","outcome","evidence","tool"]

def load(p): return json.load(open(p, encoding="utf-8"))

def build(cdir):
    cdir = os.path.abspath(cdir)
    C = load(os.path.join(cdir, "customer.json"))
    CAT = load(os.path.join(ROOT, "data/catalog.json"))
    if C.get("base") and C["base"] != CAT["version"]:
        print(f"note: overlay pinned to base {C['base']}, building against {CAT['version']}")

    L1 = {g["eid"]: g for l0 in CAT["l0s"] for g in l0["l1s"]}
    L2 = {p["eid"]: p for g in L1.values() for p in g["l2s"]}

    # ---- suppress ----
    sup = set(C.get("suppress", []))
    for l0 in CAT["l0s"]:
        l0["l1s"] = [g for g in l0["l1s"] if g["eid"] not in sup]
        for g in l0["l1s"]: g["l2s"] = [p for p in g["l2s"] if p["eid"] not in sup]
    keep_l2 = {p["eid"] for l0 in CAT["l0s"] for g in l0["l1s"] for p in g["l2s"]}
    id2eid = {p["id"]: p["eid"] for p in L2.values()}
    for f in CAT["flows"]:
        for s in f["steps"]: s["l2"] = [x for x in s["l2"] if id2eid.get(x) in keep_l2]
    for d in CAT.get("decisions", []):
        d["affects"] = [x for x in d["affects"] if id2eid.get(x) in keep_l2]

    # ---- additions: customer groups first (G-9xx under an existing L0), then processes ----
    for add in [a for a in C.get("additions", []) if "group" in a]:
        gd = add["group"]; l0 = next(x for x in CAT["l0s"] if x["id"] == gd["parent_l0"])
        assert gd["eid"].startswith("G-9"), "customer groups use G-900+"
        g = {"id": gd["id"], "name": gd["name"], "original_name": gd["name"], "merged_from": [], "l2s": [], "eid": gd["eid"], "l0": l0["id"], "customer_addition": True}
        l0["l1s"].append(g); L1[g["eid"]] = g
    for add in [a for a in C.get("additions", []) if "group" not in a]:
        g = L1.get(add["parent"]);  assert g, f"unknown parent {add['parent']}"
        rec = copy.deepcopy(add); rec.pop("parent", None)
        assert rec["eid"].startswith("P-9"), "customer additions use P-9000+"
        base_l2 = g["l2s"][0] if g["l2s"] else {}
        for k in ["legacy_id","delivery_model","budgeting_method"]: rec.setdefault(k, None)
        rec.setdefault("persona_list", [x.strip() for x in rec.get("personas","").split(",") if x.strip()])
        rec.setdefault("cadence_bucket", "Event-driven"); rec.setdefault("products", [rec.get("tool","Costing")]); rec.setdefault("primary_product", rec["products"][0])
        rec.setdefault("frameworks", []); rec.setdefault("framework_tags", []); rec.setdefault("framework", ""); rec.setdefault("evidence", "Customer-specific addition")
        rec.setdefault("outcome", ""); rec.setdefault("completeness", 9); rec.setdefault("completeness_of", 9); rec.setdefault("flows", [])
        rec["customer_addition"] = True; rec["l0"] = g.get("l0") or next(l0["id"] for l0 in CAT["l0s"] if g in l0["l1s"]); rec["l1"] = g["id"]
        g["l2s"].append(rec); L2[rec["eid"]] = rec

    # ---- overrides ----
    for eid, patch in C.get("overrides", {}).items():
        tgt = L2.get(eid) or L1.get(eid); assert tgt, f"unknown eid {eid}"
        for k, v in patch.items(): tgt[k] = v
        tgt.setdefault("customer_overrides", []); tgt["customer_overrides"] = sorted(set(tgt["customer_overrides"]) | set(patch))
        if "personas" in patch and "persona_list" not in patch: tgt["persona_list"] = [x.strip() for x in patch["personas"].split(",") if x.strip()]

    # ---- labels (vocabulary) ----
    labels = C.get("labels", {})
    if labels:
        pat = re.compile(r"\b(" + "|".join(re.escape(k) for k in sorted(labels, key=len, reverse=True)) + r")\b")
        def lab(s): return pat.sub(lambda m: m.group(1) if labels[m.group(1)] in s else labels[m.group(1)], s)
        for p in L2.values():
            for f in TEXT_FIELDS:
                if isinstance(p.get(f), str): p[f] = lab(p[f])
            p["persona_list"] = [lab(x) for x in p.get("persona_list", [])]
            for v in p.get("variants", []):
                for f in TEXT_FIELDS:
                    if isinstance(v.get(f), str): v[f] = lab(v[f])
        for g in L1.values(): g["name"] = lab(g["name"])
        for f in CAT["flows"]:
            f["summary"] = lab(f["summary"]); f["lanes"] = [lab(x) for x in f["lanes"]]
            for s in f["steps"]: s["task"] = lab(s["task"]); s["lane"] = lab(s["lane"]); s["note"] = lab(s.get("note","")) if s.get("note") else s.get("note")

    # ---- scope ----
    scope = C.get("scope")
    if scope:
        scope.setdefault("eids", [])
        # groups listed without explicit eids contribute all their L2s
        listed = set(scope["eids"])
        for gid in scope.get("groups", []):
            g = L1.get(gid) or next((x for x in L1.values() if x["id"]==gid), None); assert g, f"unknown scope group {gid}"
            if not any(p["eid"] in listed for p in g["l2s"]):
                listed |= {p["eid"] for p in g["l2s"]}
        scope["eids"] = sorted(listed)
        scope["groups"] = [ (L1[g]["eid"] if g in L1 else next(x["eid"] for x in L1.values() if x["id"]==g)) for g in scope.get("groups", []) ]

    # ---- assessment (latest round file) ----
    rounds = sorted(f for f in glob.glob(os.path.join(cdir, "assessment", "*.json")) if os.path.basename(f) != "mapping.json")
    A = load(rounds[-1]) if rounds else None
    if A:
        A.setdefault("levels", DEFAULT_LEVELS)
        A.setdefault("bands", DEFAULT_BANDS)
        A.setdefault("scores", {})
        A["scores"] = {k: v for k, v in A["scores"].items() if k in L2 or k in L1}
        # group-level targets expand to every process in the group that has no explicit target
        for gid, t in (A.get("targets") or {}).items():
            g = L1.get(gid) or next((x for x in L1.values() if x["id"]==gid), None)
            if not g: continue
            for p in g["l2s"]:
                if scope and p["eid"] not in set(scope["eids"]): continue
                A["scores"].setdefault(p["eid"], {}); A["scores"][p["eid"]].setdefault("target", t)

    mp = os.path.join(cdir, "assessment", "mapping.json")
    if A and os.path.exists(mp): A["questionnaire"] = load(mp)

    # ---- review state (exported from the site, committed to the repo) ----
    R = None
    rv = sorted(glob.glob(os.path.join(cdir, "review", "*.json")))
    if rv: R = load(rv[-1])

    # ---- models ----
    DEC = {d["key"]: d for d in CAT.get("decisions", [])}; bpmn.DECISIONS = DEC
    for l0 in CAT["l0s"]:
        l0["bpmn"] = bpmn.l0_to_flow(l0)
        for g in l0["l1s"]:
            g["bpmn"] = bpmn.l1_to_flow(l0, g)
            byid = {p["id"]: p for p in g["l2s"]}
            for s in g["bpmn"]["steps"]:
                if s["n"] in byid: byid[s["n"]]["lane"] = s["lane"]; byid[s["n"]]["bpmn_type"] = s["type"]
    for f in CAT["flows"]: f["kind"] = None

    # ---- payload ----
    cust = {k: C[k] for k in ["id","name","title","short","fy_start","currency","profile","scope","base"] if k in C}
    cust["labels"] = labels
    CAT["customer"] = cust
    if A: CAT["assessment"] = A
    if R: CAT["review_seed"] = R
    CAT["changelog"] = [{"version": CAT["version"], "date": C.get("built", ""), "items": [
        f"{C['name']} instance built on base v{CAT['version']}: {len(C.get('overrides',{}))} overrides, {len(C.get('additions',[]))} additions, {len(sup)} suppressed, {len(labels)} vocabulary substitutions; "
        f"engagement scope “{scope['name']}” ({len(scope['eids'])} processes)" + (f"; assessment round {A['round']} ({len(A['scores'])} scored)" if A else "") + "."]}] + CAT["changelog"]

    tpl = open(os.path.join(ROOT, "site/templates/app.html"), encoding="utf-8").read()
    tpl = tpl.replace("<title>Apptio Process Catalog</title>", f"<title>{C['title']}</title>")
    payload = json.dumps(CAT, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = tpl.replace("__DATA__", payload)
    os.makedirs(os.path.join(cdir, "site"), exist_ok=True); os.makedirs(os.path.join(cdir, "docs"), exist_ok=True); os.makedirs(os.path.join(cdir, "data"), exist_ok=True)
    open(os.path.join(cdir, "site/index.html"), "w", encoding="utf-8").write(page)
    head = page[page.index("<head>")+6: page.index("</head>")]; head = re.sub(r"<meta [^>]*>\s*", "", head)
    body = page[page.index("<body>")+6: page.rindex("</body>")]
    open(os.path.join(cdir, "site/index.artifact.html"), "w", encoding="utf-8").write(head.strip()+"\n"+body)
    json.dump(CAT, open(os.path.join(cdir, "data/catalog.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # ---- docs/overview.md ----
    fy = int(C.get("fy_start", 1))
    def cal(fm): return MONTHS[(fy - 1 + fm - 1) % 12]
    out = [f"# {C['title']} — instance overview", "",
           f"Built from base catalog v{CAT['version']} with overlay `customer.json`. Fiscal year starts {MONTHS[fy-1]} (FM1 = {cal(1)}, FM12 = {cal(12)}). Currency {C.get('currency','')}.", "",
           "## Engagement scope", "", f"**{scope['name']}** — {scope.get('summary','')}", ""]
    for gid in scope["groups"]:
        g = L1[gid]; ins = [p for p in g["l2s"] if p["eid"] in set(scope["eids"])]
        out.append(f"- **{g['id']} {g['name']}** — " + ", ".join(f"{p['id']} {p['name']}" for p in ins))
    out += ["", "## Decision profile (initial)", ""]
    for k, opts in C.get("profile", {}).items():
        d = DEC.get(k);
        if d: out.append(f"- **{d['id']} {d['name']}**: " + ", ".join(next((o['name'] for o in d['options'] if o['id']==oid), oid) for oid in opts))
    if C.get("profile_notes"): out += ["", C["profile_notes"]]
    out += ["", "## Overrides", ""]
    for eid, patch in C.get("overrides", {}).items():
        t = L2.get(eid) or L1.get(eid)
        if t: out.append(f"- **{t['id']} {t['name']}** ({eid}): " + "; ".join(f"{k} → {str(v)[:160]}" for k, v in patch.items()))
    if labels: out += ["", "## Vocabulary", "", ", ".join(f"{k} → {v}" for k, v in labels.items())]
    out += ["", "## Operating calendar (fiscal → calendar months)", "", "| FM | Month |", "|---|---|"] + [f"| {m} | {cal(m)} |" for m in range(1,13)]
    if A:
        out += ["", f"## Assessment round {A['round']} — target profile {A.get('target_profile','')}", "", "| Level | Name | Meaning |", "|---|---|---|"] + [f"| {L['n']} | {L['name']} | {L['desc']} |" for L in A["levels"]] + [""]
        scored = [(L2[e], s) for e, s in A["scores"].items() if e in L2 and s.get("level") is not None]
        out.append(f"{len(scored)} of {len(scope['eids'])} in-scope processes scored." if scope else f"{len(scored)} processes scored.")
        if scored:
            out += ["", "| Process | Level | Target | Method | Confidence | Gap |", "|---|---|---|---|---|---|"] + [f"| {p['id']} {p['name']} | {s.get('level')} | {s.get('target','')} | {s.get('method','')} | {s.get('confidence','')} | {s.get('gap','')} |" for p, s in scored]
    open(os.path.join(cdir, "docs/overview.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")

    # ---- docs/assessment-report.md: the assessment deliverable, generated from the round ----
    if A:
        def lvl(n): return next((L["name"] for L in A["levels"] if L["n"] == n), str(n))
        def band(m):
            if m is None: return "—"
            b = next((b for b in A["bands"] if m > b[0] and m <= b[1]), A["bands"][0]); return b[2]
        rep = [f"# {C['name']} — maturity assessment, round {A['round']}", "",
               f"Target profile: {A.get('target_profile','')}. Base catalog v{CAT['version']}. Scale per process: " + " · ".join(f"{L['n']} {L['name']}" for L in A["levels"]) + ". Roll-up bands: " + " / ".join(b[2] for b in A["bands"]) + ".", ""]
        if A.get("notes"): rep += [A["notes"], ""]
        units = A.get("units") or [""]
        def rec_for(eid, u): return A["scores"].get(eid if (not u or u == units[0]) else f"{eid}@{u}")
        rep += ["## Scope summary", "", "| Group | Processes | Scored | Mean level | Band | Target |", "|---|---|---|---|---|---|"]
        gaps = []
        for gid in (scope["groups"] if scope else list(L1)):
            g = L1[gid]; ps = [p for p in g["l2s"] if not scope or p["eid"] in set(scope["eids"])]
            lv = [rec_for(p["eid"], units[0])["level"] for p in ps if rec_for(p["eid"], units[0]) and rec_for(p["eid"], units[0]).get("level") is not None]
            tg = [rec_for(p["eid"], units[0])["target"] for p in ps if rec_for(p["eid"], units[0]) and rec_for(p["eid"], units[0]).get("target") is not None]
            m = sum(lv)/len(lv) if lv else None; t = sum(tg)/len(tg) if tg else None
            rep.append(f"| {g['id']} {g['name']} | {len(ps)} | {len(lv)} | {m:.1f} | {band(m)} | {t:.1f} |" if m is not None else f"| {g['id']} {g['name']} | {len(ps)} | 0 | — | — | {t:.1f} |" if t is not None else f"| {g['id']} {g['name']} | {len(ps)} | 0 | — | — | — |")
            for p in ps:
                r = rec_for(p["eid"], units[0])
                if r and r.get("level") is not None and r.get("target") is not None and r["level"] < r["target"]: gaps.append((p, r))
        rep += ["", "## Gaps to target (flow order)", ""]
        order = {}; i = 0
        for f in CAT["flows"]:
            for st in f["steps"]:
                for pid in st["l2"]:
                    if pid not in order: order[pid] = i; i += 1
        gaps.sort(key=lambda x: order.get(x[0]["id"], 9999))
        if gaps:
            rep += ["| # | Process | Level → target | Gap | Evidence | Basis |", "|---|---|---|---|---|---|"] + [f"| {n+1} | {p['id']} {p['name']} | {r['level']} {lvl(r['level'])} → {r['target']} | {r.get('gap','')} | {r.get('evidence','')} | {r.get('method','')} {r.get('confidence','')} |" for n, (p, r) in enumerate(gaps)]
        else: rep.append("No scored process is below its target yet.")
        rep += ["", "## Scored processes", "", "| Process | Unit | Level | Target | Lens | Method | Confidence | Evidence | Gap |", "|---|---|---|---|---|---|---|---|---|"]
        for k, r in sorted(A["scores"].items()):
            if r.get("level") is None: continue
            eid, _, u = k.partition("@"); p = L2.get(eid)
            if not p: continue
            rep.append(f"| {p['id']} {p['name']} | {u or units[0]} | {r['level']} {lvl(r['level'])} | {r.get('target','')} | {r.get('lens','')} | {r.get('method','')} | {r.get('confidence','')} | {r.get('evidence','')} | {r.get('gap','')} |")
        rep += ["", "## Method", "", "Scores are collected three ways and converge on one level per process: consultant-led workshop scoring on the site (evidence and gap note per record), the yes/no self-assessment questionnaire whose answers map to processes and produce provisional scores, and tool evidence checked against the costing and work-management tools. Capability and dimension × lens views are derived from process scores through `assessment/mapping.json`. This report is regenerated from the committed round; the site's *Export assessment* button produces the file to commit."]
        open(os.path.join(cdir, "docs/assessment-report.md"), "w", encoding="utf-8").write("\n".join(rep) + "\n")
    print(f"built {C['id']}: base v{CAT['version']} · scope {len(scope['eids']) if scope else 0} L2 · overrides {len(C.get('overrides',{}))} · assessment {A['round'] if A else 'none'} → {os.path.relpath(cdir, ROOT)}/site/index.html")

DEFAULT_LEVELS = [
 {"n":1,"name":"Ad Hoc","desc":"Unpredictable and reactive: it happens (if at all) person-by-person, undocumented, without metrics."},
 {"n":2,"name":"Emerging","desc":"Developing: documented in places, an owner and cadence exist in pockets, data improving but inconsistent across the organization."},
 {"n":3,"name":"Repeatable","desc":"Recurs with the same accuracy every time: defined owner, inputs/outputs and cadence; the required capabilities are configured in the tool of record and data flows on cadence."},
 {"n":4,"name":"Proactive","desc":"Managed: outputs are used in decisions, metrics and variances are tracked and acted on, exceptions are anticipated."},
 {"n":5,"name":"Optimized","desc":"Planned, governed, integrated and automated where the tooling allows; continuously improved and benchmarked."},
]
# roll-up bands on the mean level (SPM Maturity Assessment v0.6 RESULTS sheet)
DEFAULT_BANDS = [[0,1.0,"Ad hoc"],[1.0,2.0,"Emerging"],[2.0,3.0,"Defined"],[3.0,4.0,"Managed"],[4.0,5.01,"Optimizing"]]

if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "customers", "example"))
