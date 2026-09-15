#!/usr/bin/env python3
"""One-off: merge the v0.5 prototype catalog (JSON) with the enrichments that only
existed in the old data/catalog.yaml (PI Planning / EVD agent requirements, 2026-08-28).
Writes data/catalog.json (v0.6.0). Kept for provenance; not part of the regular build."""
import json, yaml, re, copy, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cat = json.load(open(sys.argv[1]))
rows = yaml.safe_load(open(os.path.join(ROOT, "data/catalog.yaml")))
rl2 = {r["l2id"]: r for r in rows}
jl2 = {l2["id"]: l2 for l0 in cat["l0s"] for l1 in l0["l1s"] for l2 in l1["l2s"]}
l1s = {l1["id"]: l1 for l0 in cat["l0s"] for l1 in l0["l1s"]}

# 1. rows where the YAML is a superset (EVD enrichments) -> take desc/config/src, union evidence
EVD = ["01.1.2","01.2.1","02.1.2","02.2.1","02.3.2","02.3.3","03.1.1","03.1.4","05.7.2"]
for k in EVD:
    r, j = rl2[k], jl2[k]
    for a, b in (("desc","description"),("config","config")):
        if len(r[a].strip()) > len(j[b].strip()): j[b] = r[a].strip()
    if r["src"].strip() != j["evidence"].strip():
        j["evidence"] = r["src"].strip()
    j["personas"] = r["personas"] if len(r["personas"]) > len(j["personas"]) else j["personas"]

# 2. 03.1 rename (repo decision 2026-08-28): Quarterly Planning (SAFe PI cadence)
g = l1s["03.1"]
g["name"] = "Plan quarterly (SAFe PI cadence)"
g["original_name"] = "Quarterly Planning (SAFe PI cadence)"
g["aliases"] = ["PI Planning"]
jl2["03.1.1"]["name"] = "Assess & prepare quarterly planning readiness"
jl2["03.1.2"]["name"] = "Run quarterly planning event"
jl2["03.1.4"]["name"] = "Baseline commitments & track PI execution"

def persona_list(s):
    s = s.lower(); out = []
    rules = [("Executive leadership", ["c-suite","cio","cfo","vp ","leadership","business owner","sponsor"]),
             ("Portfolio management", ["portfolio","lpm","value stream","vs owner","epic owner"]),
             ("PMO & project managers", ["pmo","project manager","release","gate"]),
             ("Product management", ["product"]),
             ("Agile teams & RTEs", ["rte","team","scrum","art","ste"]),
             ("Resource management", ["resource","capacity","hiring"]),
             ("HR & approvers", ["hr","approver"]),
             ("IT Finance & FP&A", ["finance","fp&a","accounting","it finance"]),
             ("Budget & cost-category owners", ["budget owner","cost-category"]),
             ("TBM Office & analysts", ["tbm","costing admin","analyst"]),
             ("FinOps practitioners", ["finops","cloud eng","cloud architect"]),
             ("Engineering", ["engineering","platform eng","infrastructure","architecture"]),
             ("Vendor management & procurement", ["vendor","procurement"]),
             ("Business, app & service owners", ["app owner","service owner","bu owner","business"]),
             ("Platform admins & integration", ["admin","integration","platform","system","transformation","governance","security"]),
             ("Requesters", ["requester"])]
    for name, kws in rules:
        if any(k in s for k in kws) and name not in out: out.append(name)
    return out or ["Platform admins & integration"]

def bucket(c):
    c = c.lower()
    if "continuous" in c or "daily" in c or "on change" in c or "on demand" in c: return "Continuous"
    if "weekly" in c: return "Weekly"
    if "monthly" in c: return "Monthly"
    if "quarter" in c: return "Quarterly"
    if "annual" in c or "cycle" in c or "per pi" in c and False: return "Annual / per cycle"
    return "Event-driven"

def fw_tags(fw):
    t = []
    for k in ("TBM","SPM","SAFe","FinOps","ITFM"):
        if re.search(r"\b"+k+r"\b", fw, re.I): t.append(k)
    return t

def products(tool, support):
    s = tool + " " + (support or ""); out = []
    for p, kws in (("Targetprocess",["targetprocess","atp"]),("Costing",["costing"]),("Planning",["planning"]),("Cloudability",["cloudability"])):
        if any(k in s.lower() for k in kws): out.append(p)
    if "all four" in s.lower(): out = ["Targetprocess","Costing","Planning","Cloudability"]
    return out

def to_l2(r, eid):
    fws = [x.strip() for x in r["fw"].split("|") if x.strip()]
    tool = r["tool"] + (f" (+ {r['support']})" if r.get("support") else "")
    prods = products(r["tool"], r.get("support"))
    return {"id": r["l2id"], "legacy_id": None, "name": r["l2"], "description": r["desc"].strip(),
            "delivery_model": r["delivery"], "tool": tool, "personas": r["personas"], "cadence": r["cadence"],
            "inputs": r["inputs"], "outputs": r["outputs"], "config": r["config"].strip(), "framework": r["fw"],
            "evidence": r["src"].strip(), "eid": eid, "persona_list": persona_list(r["personas"]),
            "cadence_bucket": bucket(r["cadence"]), "products": prods,
            "primary_product": ("All four" if r["tool"]=="All four" else prods[0] if prods else "All four"),
            "budgeting_method": None, "outcome": r["outputs"][0].lower()+r["outputs"][1:] if r["outputs"] else "",
            "frameworks": fws, "framework_tags": fw_tags(r["fw"]), "completeness": 9, "completeness_of": 9, "flows": []}

# 3. new L2s in 03.1
g["l2s"].append(to_l2(rl2["03.1.5"], "P-0145"))
g["l2s"].append(to_l2(rl2["03.1.6"], "P-0146"))
# 4. new L1 10.7 (AI-assisted planning & delivery intelligence)
l0_10 = [l0 for l0 in cat["l0s"] if l0["id"]=="10"][0]
l0_10["l1s"].append({"id":"10.7","name":"Run AI-assisted planning & delivery intelligence",
    "original_name":"AI-Assisted Planning & Delivery Intelligence","merged_from":[],
    "l2s":[to_l2(rl2["10.7.1"],"P-0147"), to_l2(rl2["10.7.2"],"P-0148"), to_l2(rl2["10.7.3"],"P-0149")],
    "eid":"G-107"})
l0_10["lanes"] = [x.rstrip(".") for x in l0_10["lanes"]]
for l0 in cat["l0s"]: l0["lanes"] = [x.rstrip(".") for x in l0["lanes"]]

cat["version"] = "0.6.0"; cat["built"] = "2026-09-15"
cat["changelog"].insert(0, {"version":"0.6.0","date":"2026-09-15","items":[
    "Repository build: data/catalog.json is now the single source of truth; the GitHub Pages site, docs, Mermaid, BPMN XML, SVG snapshots and Excel master are all regenerated from it by scripts/generate.py.",
    "BPMN 2.0 swimlane diagrams for every process area (9), every process group (45) and every cross-tool flow (7), both in the site and as importable .bpmn files with SVG snapshots.",
    "Folded in the PI Planning / Enterprise Value Delivery agent requirements that only lived in the old YAML catalog: 03.1 renamed to quarterly planning on the SAFe PI cadence, two new L2s (03.1.5 ROAM & confidence vote, 03.1.6 System demo & Inspect and Adapt), enriched 01.1.2, 01.2.1, 02.1.2, 02.2.1, 02.3.2, 02.3.3, 03.1.1, 03.1.4, 05.7.2, and a new group 10.7 AI-assisted planning & delivery intelligence (10.7.1-10.7.3).",
    "Structure is now 9 L0 · 45 L1 · 149 L2 · 7 flows."]})
cat["changelog"].insert(1, {"version":"0.5.0","date":"2026-09-15","items":[
    "BPMN 2.0 swimlane diagram on every flow page, generated from the step table, with BPMN XML export."]})
json.dump(cat, open(os.path.join(ROOT,"data/catalog.json"),"w"), indent=1, ensure_ascii=False)
n2 = sum(len(l1["l2s"]) for l0 in cat["l0s"] for l1 in l0["l1s"]); n1 = sum(len(l0["l1s"]) for l0 in cat["l0s"])
print("wrote data/catalog.json", cat["version"], len(cat["l0s"]), n1, n2, len(cat["flows"]))
