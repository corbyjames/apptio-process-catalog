#!/usr/bin/env python3
"""Build a publishable extract of the catalog site for a subset of processes.

Usage: python3 scripts/extract_site.py [extract-key]

An extract keeps the full site (records with Business/SME lens, BPMN diagrams,
register, decisions + profile picker, glossary, changelog, browser-local review)
but only for the groups, flows and decisions listed in EXTRACTS below.
Outputs:
  dist/extracts/<key>.html            standalone page (open in a browser)
  dist/extracts/<key>.artifact.html   same page without the html/head/body
                                      skeleton, for publishing as a Claude artifact
"""
import copy, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import bpmn

EXTRACTS = {
    "labor-demand-capacity": {
        "title": "Labor Rates, Demand & Capacity Management",
        "lede": "How demand is captured and prioritized, how workforce capacity is planned and allocated against it, "
                "how effort is captured, and how labor rates are protected, blended and published so that team cost "
                "and capitalization follow from the same data. An extract of the Apptio Process Catalog.",
        # L1 groups to keep; a group may be narrowed to specific L2s
        "groups": {"02.1": None, "02.2": None, "04.1": ["04.1.3"], "04.2": None, "04.3": None,
                   "04.4": None, "04.5": None, "06.4": None},
        "l0_order": ["02", "04", "06"],
        "band_title": "Demand → Capacity → Labor cost",
        "band_sub": "Shape demand → plan &amp; allocate capacity, capture effort → rate, cost and capitalize the work",
        "flows": ["UC3", "INV", "UC2", "UC1"],
    },
}

def build(key):
    spec = EXTRACTS[key]
    CAT = json.load(open(os.path.join(ROOT, "data/catalog.json"), encoding="utf-8"))
    full_l2 = sum(len(g["l2s"]) for l0 in CAT["l0s"] for g in l0["l1s"])

    # ---- filter hierarchy ----
    keep_l2 = set()
    l0s = []
    for l0 in CAT["l0s"]:
        if l0["id"] not in spec["l0_order"]: continue
        l0 = copy.deepcopy(l0); l1s = []
        for g in l0["l1s"]:
            if g["id"] not in spec["groups"]: continue
            only = spec["groups"][g["id"]]
            if only: g["l2s"] = [p for p in g["l2s"] if p["id"] in only]
            g["extract_narrowed"] = bool(only)
            for p in g["l2s"]: keep_l2.add(p["id"])
            l1s.append(g)
        l0["l1s"] = l1s; l0s.append(l0)
    l0s.sort(key=lambda l: spec["l0_order"].index(l["id"]))

    # ---- flows ----
    flows = [copy.deepcopy(f) for f in CAT["flows"] if f["id"] in spec["flows"]]
    flows.sort(key=lambda f: spec["flows"].index(f["id"]))
    keep_flows = {f["id"] for f in flows}
    for f in flows:
        f["upstream"] = [u for u in f["upstream"] if u in keep_flows]
        f["downstream"] = [u for u in f["downstream"] if u in keep_flows]

    # ---- decisions: any that shape a kept L2 or condition a kept flow step ----
    used_keys = set()
    for f in flows:
        for s in f["steps"]:
            for k in (s.get("when") or {}): used_keys.add(k)
            if s.get("decision"): used_keys.add(s["decision"])
    decisions = []
    for d in CAT.get("decisions", []):
        aff = [a for a in d["affects"] if a in keep_l2]
        if aff or d["key"] in used_keys:
            d = copy.deepcopy(d); d["affects"] = aff
            d["flows"] = [x for x in d.get("flows", []) if x in keep_flows]
            d["related"] = [x for x in d.get("related", [])]
            decisions.append(d)
    keep_keys = {d["key"] for d in decisions}
    for d in decisions: d["related"] = [x for x in d["related"] if x in keep_keys]

    # ---- per-record references ----
    for l0 in l0s:
        for g in l0["l1s"]:
            for p in g["l2s"]:
                p["flows"] = [x for x in p["flows"] if x in keep_flows]
                if p.get("decisions"): p["decisions"] = [k for k in p["decisions"] if k in keep_keys]
                if p.get("variants"): p["variants"] = [v for v in p["variants"] if v["decision"] in keep_keys]
                if p.get("applies_when"): p["applies_when"] = {k: v for k, v in p["applies_when"].items() if k in keep_keys}

    # ---- BPMN models (same generator as the main site) ----
    DEC = {d["key"]: d for d in decisions}
    bpmn.DECISIONS = DEC
    for l0 in l0s:
        l0["bpmn"] = bpmn.l0_to_flow(l0)
        for g in l0["l1s"]:
            g["bpmn"] = bpmn.l1_to_flow(l0, g)
            byid = {p["id"]: p for p in g["l2s"]}
            for s in g["bpmn"]["steps"]:
                if s["n"] in byid: byid[s["n"]]["lane"] = s["lane"]; byid[s["n"]]["bpmn_type"] = s["type"]
    for f in flows: f["kind"] = None

    n_l2 = len(keep_l2)
    narrowed = [g["id"] for l0 in l0s for g in l0["l1s"] if g.get("extract_narrowed")]
    changelog = [{"version": CAT["version"], "date": CAT["built"][:10] if CAT.get("built") else "",
                  "items": [f"Extract “{spec['title']}”: {n_l2} of the catalog’s {full_l2} processes "
                            f"({', '.join(spec['groups'])}), {len(flows)} of {len(CAT['flows'])} flows and "
                            f"{len(decisions)} of {len(CAT.get('decisions', []))} design decisions. "
                            + (f"Group {', '.join(narrowed)} is narrowed to the processes relevant here. " if narrowed else "")
                            + "Records, diagrams and decisions are identical to the full catalog at this version."]}] + CAT["changelog"]
    data = {"version": CAT["version"], "built": CAT.get("built"), "extract": {"key": key, "title": spec["title"], "lede": spec["lede"],
            "band_title": spec["band_title"], "band_sub": spec["band_sub"], "total_l2": full_l2, "narrowed": narrowed},
            "l0s": l0s, "flows": flows, "glossary": CAT["glossary"], "changelog": changelog, "decisions": decisions}

    # ---- template edits ----
    tpl = open(os.path.join(ROOT, "site/templates/app.html"), encoding="utf-8").read()
    def sub1(old, new, flags=0):
        nonlocal tpl
        n = len(re.findall(old, tpl, flags)); assert n == 1, (old, n)
        tpl = re.sub(old, lambda m: new, tpl, flags=flags)

    sub1(r"<title>Apptio Process Catalog</title>", f"<title>{spec['title']}</title>")
    sub1(r"\(CUST\?CUST\.title:'Apptio Process Catalog'\); return; \}", "(CUST?CUST.title:DATA.extract.title); return; }")
    sub1(r"document\.title = title \+ ' · '\+\(CUST\?CUST\.title:'Apptio Process Catalog'\);", "document.title = title + ' · '+(CUST?CUST.title:DATA.extract.title);")
    sub1(r"let crumbs = `<a href=\"#/\">\$\{CUST\?esc\(CUST\.short\|\|CUST\.name\):'Catalog'\}</a>`;", "let crumbs = `<a href=\"#/\">${CUST?esc(CUST.short||CUST.name):'Extract'}</a>`;")
    # downloads and the bpmn-js editor are not available inside an artifact: keep Copy XML only
    sub1(r'<div class="dl"><span style="color:var\(--ink3\)">Download:</span><a href="\$\{files.bpmn\}" download>\$\{files.base\}.bpmn</a><a href="\$\{files.svg\}" download>\$\{files.base\}.svg</a><a href="viewer.html#\$\{encodeURIComponent\(files.bpmn\)\}">open in editor</a>',
         '<div class="dl"><span style="color:var(--ink3)">${files.base}</span>')
    sub1(r'with \.bpmn and \.svg downloads and a <a href="viewer.html">bpmn-js editor</a>\.', 'each with copyable BPMN 2.0 XML.')
    # review stays browser-local in an extract (no shared db), and the diagram index has no files to download
    sub1(r"db = await window\.claude\.use\('db'\);", "db = null; // extract: review marks stay in this browser")
    sub1(r'<div class="dl"><a href="\$\{files\.bpmn\}" download>\.bpmn</a><a href="\$\{files\.svg\}" download>\.svg</a><a href="viewer\.html#\$\{encodeURIComponent\(files\.bpmn\)\}">editor</a></div>',
         '<div class="dl"><span style="color:var(--ink3)">${files.base}</span><a href="${href}">open</a></div>')
    # the extract's own hub
    start = tpl.index("function hubHTML(){"); end = tpl.index("\nfunction l0HTML(")
    hub = r'''function hubHTML(){
  const X = DATA.extract;
  const tile = (l0) => { const l2s=l0.l1s.flatMap(g=>g.l2s), c=counts(l2s); return `<a class="tile" data-p="${l0.product}" data-l0="${l0.id}" href="#/l0/${l0.id}"><span class="n">L0-${l0.id}</span><span class="t">${esc(l0.name)}</span><span class="sub">${l0.l1s.map(g=>g.id).join(' · ')}<br>${l2s.length} processes · ${c.confirmed} confirmed</span><span class="bar2">${barHTML(l0)}</span></a>`; };
  const total = ALL_L2.length, c = counts(ALL_L2);
  const note = `<div class="notice">An extract of the Apptio Process Catalog v${DATA.version}: ${total} of its ${X.total_l2} processes, ${FLOWS.length} cross-tool flows and ${DECISIONS.length} design decisions, unchanged from the full catalog.${X.narrowed.length?` Group ${X.narrowed.join(', ')} is narrowed to the processes relevant here.`:''} Every process keeps its permanent ID (P-0001…) so comments can be carried back to the master.</div>`;
  return `<div class="pagehead"><div><p class="eyebrow">IBM Apptio · Targetprocess · Costing · Planning · <a href="#/changelog" title="What changed in this release">v${DATA.version}</a></p><h1>${esc(X.title)}</h1><p class="lede">${esc(X.lede)}</p></div>
  <div class="statlist"><div class="stat"><b>${total}</b><span>L2 processes</span></div><div class="stat"><b>${c.confirmed}</b><span>confirmed</span></div><div class="stat"><b>${FLOWS.length}</b><span>E2E flows</span></div><div class="stat"><b>${DECISIONS.length}</b><span>design decisions</span></div></div></div>
  ${note}
  <div class="landscape">
    <section class="band core extract"><div class="bhead"><h2>${X.band_title}</h2><span>${X.band_sub}</span></div><div class="tiles">${L0S.map(l=>tile(l)).join('')}</div></section>
    <section class="band"><div class="bhead"><h2>Flows across the chain</h2><span>"Targets down. Rates back. Actuals in." — plus the investment loop</span></div><div class="flows-band">${FLOWS.map(f=>`<a class="flowcard" href="#/flow/${f.id}"><span class="fid">${f.id}</span><span><span class="ft">${esc(f.name)}</span><span class="fs">${esc(f.title)} · ${f.steps.length} steps</span><span class="fp">${f.products.map(p=>`<i style="background:${PCOLOR[p]}" title="${p}"></i>`).join('')}</span></span></a>`).join('')}</div></section>
  </div>
  <div class="hubgrid">
    <section class="panel"><h2>Other ways in</h2><dl class="kv">
      <dt><a href="#/decisions">Decisions</a></dt><dd>The ${DECISIONS.length} design decisions that shape these processes — how labor effort is captured, which rate leaves Costing, the capacity basis, how demand arrives and how work is funded and governed. Choose options to render the extract as one customer's profile.</dd>
      <dt><a href="#/register">Register</a></dt><dd>One sortable, filterable table of all ${total} processes — slice by product, persona, cadence, flow, framework, decision or review status.</dd>
      <dt><a href="#/diagrams">Diagrams</a></dt><dd>BPMN 2.0 swimlane diagrams — ${L0S.length} areas, ${Object.keys(L1).length} groups and ${FLOWS.length} flows — each with copyable BPMN 2.0 XML.</dd>
      <dt><a href="#/glossary">Glossary</a></dt><dd>Every acronym in the catalog, in plain language.</dd>
      <dt><a href="#/changelog">Changelog</a></dt><dd>What this extract contains, and what changed in the catalog since v0.2.</dd>
      <dt><a href="#/print">Everything on one page</a></dt><dd>All ${total} processes expanded with their diagrams, in reading order.</dd>
    </dl></section>
    <section class="panel"><h2>Legend</h2><div class="legend" style="margin-bottom:10px">${Object.entries(PCOLOR).map(([p,c])=>`<span><i style="background:${c}"></i>${p}</span>`).join('')}</div><div class="legend">${Object.entries(STATUS).map(([k,n])=>`<span class="status" data-s="${k}">${n}</span>`).join('')}</div><p style="font-size:12.5px;color:var(--ink2);margin:12px 0 0">Tile stripe = primary product. Bar = review status of the processes in the area. Review marks are kept in this browser only.</p></section>
  </div>`;
}
'''
    tpl = tpl[:start] + hub + tpl[end:]
    # three tiles, not six, in the chain band
    sub1(r"\.band\.core \.tiles\{grid-template-columns:repeat\(6,minmax\(0,1fr\)\)\}",
         ".band.core .tiles{grid-template-columns:repeat(6,minmax(0,1fr))}\n.band.core.extract .tiles{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}")

    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = tpl.replace("__DATA__", payload)
    os.makedirs(os.path.join(ROOT, "dist/extracts"), exist_ok=True)
    open(os.path.join(ROOT, f"dist/extracts/{key}.html"), "w", encoding="utf-8").write(page)

    # artifact body: the host supplies doctype/html/head/body
    head = page[page.index("<head>") + 6: page.index("</head>")]
    head = re.sub(r"<meta [^>]*>\s*", "", head)
    body = page[page.index("<body>") + 6: page.rindex("</body>")]
    open(os.path.join(ROOT, f"dist/extracts/{key}.artifact.html"), "w", encoding="utf-8").write(head.strip() + "\n" + body)
    print(f"extract {key}: {len(l0s)} L0 · {sum(len(l.get('l1s')) for l in l0s)} L1 · {n_l2} L2 · {len(flows)} flows · {len(decisions)} decisions → dist/extracts/{key}.html")

if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "labor-demand-capacity")
