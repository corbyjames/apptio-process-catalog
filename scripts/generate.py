#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate every derived artifact from data/.

Source of truth
  data/catalog.json      L0 areas > L1 groups > L2 processes, cross-tool flows, glossary, changelog
  data/calendar.yaml     annual operating calendar (fiscal months, refs to L2 ids)
  data/tool-config.yaml  per-product configuration checklists
  data/frameworks.yaml   TBM / FinOps / SPM / SAFe framing
  data/l0-links.yaml     cross-area feeds drawn on the L0 landscape

Outputs (all overwritten on every run - edit data/, not these)
  docs/*.md                          overview, full catalog, tool-config reference, operating calendar, diagram index
  diagrams/mermaid/*.md              L0 landscape + per-area Mermaid (GitHub renders inline)
  diagrams/bpmn/generated/*.bpmn     BPMN 2.0 XML with DI: L0-NN (9), NN.N (45), flow-XXX (7)
  assets/diagrams/*.svg              SVG snapshot of each of those diagrams
  site/index.html                    the catalog site (templates/app.html + embedded data)
  site/bpmn-manifest.json            file list for site/viewer.html (custom models first)
  dist/Apptio_Process_Catalog_L0-L2.xlsx

Never touched: diagrams/bpmn/custom/, diagrams/drawio/, docs/sources/.
"""
import json, os, sys, re, glob
import yaml
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import bpmn

def rd(name):
    p = os.path.join(ROOT, "data", name)
    with open(p, encoding="utf-8") as f:
        return json.load(f) if name.endswith(".json") else yaml.safe_load(f)
CAT = rd("catalog.json"); CAL = rd("calendar.yaml"); CFG = rd("tool-config.yaml"); FW = rd("frameworks.yaml"); LINKS = rd("l0-links.yaml")
L0S = CAT["l0s"]; FLOWS = CAT["flows"]; VERSION = CAT["version"]
L1S = [l1 for l0 in L0S for l1 in l0["l1s"]]
L2S = [l2 for l1 in L1S for l2 in l1["l2s"]]
L2 = {l2["id"]: l2 for l2 in L2S}
for l0 in L0S:
    for l1 in l0["l1s"]:
        l1["l0"] = l0["id"]
        for l2 in l1["l2s"]: l2["l0"] = l0["id"]; l2["l1"] = l1["id"]

def ensure(d): os.makedirs(os.path.join(ROOT, d), exist_ok=True)
def W(p, s):
    with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f: f.write(s)
def clean(d, pattern):
    for f in glob.glob(os.path.join(ROOT, d, pattern)): os.remove(f)
mmid = lambda s: "N" + re.sub(r"[^A-Za-z0-9]", "_", s)
for d in ("docs", "diagrams/mermaid", "diagrams/bpmn/generated", "diagrams/bpmn/custom", "assets/diagrams", "site", "dist"): ensure(d)

# ---------------- BPMN models (shared by site, files, docs) ----------------
def build_models():
    for l0 in L0S:
        l0["bpmn"] = bpmn.l0_to_flow(l0)
        for l1 in l0["l1s"]:
            l1["bpmn"] = bpmn.l1_to_flow(l0, l1)
            for s in l1["bpmn"]["steps"]: L2[s["n"]]["lane"] = s["lane"]; L2[s["n"]]["bpmn_type"] = s["type"]
    for f in FLOWS: f["kind"] = None
build_models()

def diagram_basename(f):
    if f.get("kind") == "l1": return f["name"].split(" ")[0]
    if f.get("kind") == "l0": return "L0-" + f["name"].split(" ")[0].replace("L0-", "")
    return "flow-" + f["id"]

def all_models():
    for f in FLOWS: yield f
    for l0 in L0S:
        yield l0["bpmn"]
        for l1 in l0["l1s"]: yield l1["bpmn"]

# ---------------- mermaid ----------------
def mermaid_l0():
    g = ["```mermaid", "flowchart LR"]
    groups = [("SPM", "Targetprocess — SPM", ["01", "02", "03", "04"]), ("ITFM", "Planning & Costing — ITFM/TBM", ["05", "06", "08"]),
              ("FINOPS", "Cloudability — FinOps", ["07"]), ("ENABLE", "Platform, data & practices", ["10"])]
    names = {l0["id"]: l0["name"] for l0 in L0S}
    for gid, label, ids in groups:
        g.append(f'  subgraph {gid}["{label}"]')
        for i in ids: g.append(f'    A{i}["{i} {names[i]}"]')
        g.append("  end")
    for l in LINKS:
        frm, to = str(l["frm"]).zfill(2), str(l["to"]).zfill(2)
        if frm in names and to in names: g.append(f'  A{frm} -- "{l["label"]}" --> A{to}')
    g.append("```")
    return "\n".join(g)

def gen_mermaid():
    W("diagrams/mermaid/l0-landscape.md", "# L0 Process Landscape\n\nGenerated — edit `data/catalog.json` / `data/l0-links.yaml`.\n\n" + mermaid_l0() + "\n")
    for l0 in L0S:
        out = [f"# {l0['id']} {l0['name']} — L1/L2 diagrams\n", "Generated from `data/catalog.json`. BPMN versions: see `../bpmn/generated/`.\n", "## L1 process chain\n", "```mermaid", "flowchart LR", "  S((start))"]
        prev = "S"
        for l1 in l0["l1s"]:
            nid = mmid(l1["id"]); out.append(f'  {nid}[["{l1["id"]} {l1["name"]}"]]'); out.append(f"  {prev} --> {nid}"); prev = nid
        out.append(f"  {prev} --> E(((end)))"); out.append("```")
        for l1 in l0["l1s"]:
            out.append(f"\n## {l1['id']} {l1['name']} (L2)\n"); out += ["```mermaid", "flowchart LR", "  S((start))"]; prev = "S"
            for l2 in l1["l2s"]:
                nid = mmid(l2["id"]); out.append(f'  {nid}["{l2["id"]} {l2["name"]}<br/><i>{l2["lane"]} · {l2["delivery_model"]}</i>"]'); out.append(f"  {prev} --> {nid}"); prev = nid
            out.append(f"  {prev} --> E(((end)))"); out.append("```")
        W(f"diagrams/mermaid/area-{l0['id']}.md", "\n".join(out) + "\n")

# ---------------- BPMN files + SVG snapshots ----------------
def gen_bpmn():
    clean("diagrams/bpmn/generated", "*.bpmn"); clean("assets/diagrams", "*.svg")
    n = 0
    for f in all_models():
        base = diagram_basename(f)
        W(f"diagrams/bpmn/generated/{base}.bpmn", bpmn.xml(f, VERSION))
        W(f"assets/diagrams/{base}.svg", bpmn.svg(f, link_base=None)); n += 1
    custom = sorted(x for x in os.listdir(os.path.join(ROOT, "diagrams/bpmn/custom")) if x.endswith(".bpmn"))
    gen = sorted(x for x in os.listdir(os.path.join(ROOT, "diagrams/bpmn/generated")) if x.endswith(".bpmn"))
    order = lambda x: (0 if x.startswith("flow-") else 1 if x.startswith("L0-") else 2, x)
    man = [{"path": f"../diagrams/bpmn/custom/{x}", "label": f"custom / {x}"} for x in custom] + \
          [{"path": f"../diagrams/bpmn/generated/{x}", "label": f"generated / {x}"} for x in sorted(gen, key=order)]
    W("site/bpmn-manifest.json", json.dumps(man, indent=1))
    return n

# ---------------- docs ----------------
def gen_docs():
    n1, n2 = len(L1S), len(L2S)
    out = [f"# IBM Apptio Process Catalog — Overview (L0 map) · v{VERSION}\n",
           f"Generated from `data/catalog.json` — **edit the JSON, not this file.** Structure: {len(L0S)} L0 · {n1} L1 · {n2} L2 · {len(FLOWS)} cross-tool flows. Live site: `site/index.html` (GitHub Pages).\n",
           "| L0 | Area | Primary product | Band | L1 / L2 | Default BPMN lanes |\n|---|---|---|---|---|---|"]
    for l0 in L0S:
        out.append(f"| {l0['id']} | **{l0['name']}** | {l0['primary']} | {l0['band']} | {len(l0['l1s'])} / {sum(len(g['l2s']) for g in l0['l1s'])} | {'; '.join(l0['lanes'])} |")
    out.append("\n## L0 landscape\n"); out.append(mermaid_l0())
    out.append("\n## Area descriptions\n")
    for l0 in L0S: out.append(f"**{l0['id']} — {l0['name']}.** {l0['description']}\n")
    out.append("\n## Cross-tool flows (overlays on the L2 spine)\n")
    out.append('The story: **"Targets down. Rates back. Actuals in. TCO up."** — plus cloud-to-TBM, the investment loop and the zero-based re-base. Each flow has a BPMN diagram in `diagrams/bpmn/generated/flow-<ID>.bpmn` (snapshot in `assets/diagrams/`). The reviewed master model is `diagrams/bpmn/custom/apptio-e2e-flow.bpmn`.\n')
    for f in FLOWS:
        out.append(f"\n### {f['id']} — {f['name']}: {f['title']}\n\n{f['summary']}\n\nCadence: {f['cadence']}. Lanes: {'; '.join(f['lanes'])}. Upstream: {', '.join(f['upstream']) or '—'}. Downstream: {', '.join(f['downstream']) or '—'}.\n")
        out.append(f"![{f['id']}](../assets/diagrams/flow-{f['id']}.svg)\n")
        out.append("| Step | Type | Lane | Task / event | Catalog | Notes |\n|---|---|---|---|---|---|")
        for s in f["steps"]: out.append(f"| {s['n']} | {s['type']} | {s['lane']} | {s['task']} | {', '.join(s['l2'])} | {s.get('note','') or ''} |")
    out.append("\n## Hybrid planning vs agile-only\n")
    out.append("Every L2 carries a Delivery Model tag: Any (methodology-agnostic), Agile (PI planning, Portfolio Kanban, WSJF, story-point capitalization), Traditional (stage-gate/milestone governance), or Hybrid (both governed side by side: 02.3.4 hybrid portfolio view, 02.4.1/02.2.3 dual funding, 04.2.1/04.3.4 team- and role-based capacity, 06.4.5 multi-approach capitalization).\n")
    out.append("\n## Budgeting methods\n")
    out.append("Budgeting-related L2s (02.4, 05.1, 05.8, 07.6) carry a Budgeting-method tag (Incremental, Driver-based, ZBB, Rolling, Lean/participatory, Any). ZBB re-bases the run base; lean/participatory budgeting governs the change envelope; FinOps rolling budgets absorb the variable cloud tail. See flow ZBB and group 05.8.\n")
    out.append("\n## Framework framing\n")
    for k, v in FW.items(): out.append(f"**{k}** — {v.get('layers','')}\n\n- Disciplines/capabilities: {v.get('disciplines','')}\n- Maturity: {v.get('maturity','')}\n")
    W("docs/overview.md", "\n".join(out))

    out = [f"# Full catalog — L0-L2 · v{VERSION}\n", f"Generated from `data/catalog.json` — **edit the JSON, not this file.** {len(L0S)} areas · {n1} groups · {n2} processes. Each group links to its BPMN diagram; every process shows its BPMN lane and task type.\n"]
    for l0 in L0S:
        out.append(f"\n## L0-{l0['id']} {l0['name']}\n\n*{l0['description']}* Primary: **{l0['primary']}**. Band: {l0['band']}. Lanes: {'; '.join(l0['lanes'])}.\n")
        out.append(f"![L0-{l0['id']}](../assets/diagrams/L0-{l0['id']}.svg)\n\nDiagrams: [BPMN](../diagrams/bpmn/generated/L0-{l0['id']}.bpmn) · [Mermaid](../diagrams/mermaid/area-{l0['id']}.md)\n")
        for l1 in l0["l1s"]:
            merged = f" Merged in: {', '.join(m['id']+' '+m['name'] for m in l1['merged_from'])}." if l1.get("merged_from") else ""
            out.append(f"\n### {l1['id']} {l1['name']} `{l1['eid']}`\n\nOriginal name: {l1['original_name']}.{merged} BPMN: [`{l1['id']}.bpmn`](../diagrams/bpmn/generated/{l1['id']}.bpmn) · ![{l1['id']}](../assets/diagrams/{l1['id']}.svg)\n")
            for l2 in l1["l2s"]:
                out.append(f"**{l2['id']} {l2['name']}** `{l2['eid']}`" + (f" (was {l2['legacy_id']})" if l2.get("legacy_id") else "") + f" — {l2['description']}")
                out.append(f"- What you get: {l2['outcome']}")
                out.append(f"- BPMN: lane *{l2['lane']}*, {l2['bpmn_type']} | Delivery model: {l2['delivery_model']}" + (f" | Budgeting method: {l2['budgeting_method']}" if l2.get("budgeting_method") else "") + f" | Product: {l2['tool']} | Who: {', '.join(l2['persona_list'])} ({l2['personas']}) | When: {l2['cadence_bucket']} ({l2['cadence']})")
                out.append(f"- Inputs: {l2['inputs']} → Outputs: {l2['outputs']}")
                out.append(f"- Config: {l2['config']}")
                out.append(f"- Framework: {l2['framework']} | Flows: {', '.join(l2['flows']) or '—'} | Evidence: {l2['evidence']}\n")
    W("docs/catalog-L0-L2.md", "\n".join(out))

    out = ["# Tool configuration reference\n", "Generated from `data/tool-config.yaml` (per-product checklists) plus the per-L2 configuration objects in `data/catalog.json`.\n", "## Per-product checklists\n"]
    cur = None
    for c in CFG:
        if c["tool"] != cur: cur = c["tool"]; out.append(f"\n### {c['tool']}\n")
        out.append(f"**{c['domain']}**: {c['objects']}" + (f" *({c['notes']})*" if c.get("notes") else "") + "\n")
    out.append("\n## Configuration objects by process (from the catalog)\n")
    for prod in ("Targetprocess", "Costing", "Planning", "Cloudability", "All four"):
        rows = [l2 for l2 in L2S if l2["primary_product"] == prod]
        if not rows: continue
        out.append(f"\n### {prod}\n\n| L2 | Process | Configuration objects |\n|---|---|---|")
        for l2 in rows: out.append(f"| {l2['id']} | {l2['name']} | {l2['config']} |")
    W("docs/tool-config-reference.md", "\n".join(out))

    out = ["# Annual operating calendar\n", "Generated from `data/calendar.yaml` (fiscal months, FM1 = fiscal year start).\n"]
    for st in CAL["streams"]:
        out.append(f"\n## {st['name']}\n"); out.append("| Process | Cadence | Fiscal months | Catalog refs |\n|---|---|---|---|")
        for en in st["entries"]:
            months = ", ".join(f"FM{m}" for m in en["fm"]) if len(en["fm"]) < 12 else "All year"
            refs = ", ".join(r for r in en.get("refs", []))
            out.append(f"| {en['name']} | {en['cadence']} | {months} | {refs} |")
        for en in st["entries"]: out.append(f"\n**{en['name']}** — {en['desc']}")
    W("docs/operating-calendar.md", "\n".join(out))

    out = [f"# BPMN diagram index · v{VERSION}\n", "Generated. One BPMN 2.0 model (with diagram interchange) and one SVG snapshot per process area, process group and cross-tool flow. Open any `.bpmn` in the Pages [viewer/editor](../site/viewer.html), bpmn.io, Camunda Modeler, Signavio, Visio or Draw.io. Hand-refined models belong in `diagrams/bpmn/custom/`.\n",
           "## How the diagrams are derived\n",
           "- **Flows** (`flow-*.bpmn`): straight from the step tables in `data/catalog.json` (`flows[].steps`): lane = system/role, type = the BPMN element named in the step, gateway branches parsed from the note (`No: end event '…'`, `loop to z4`, suffix steps `17a`/`17b`).\n- **Groups** (`NN.N.bpmn`): one task per L2 in catalog order; lane = the first persona in the L2's *Who* text that matches one of the area's default lanes (fallback: product hint, then lane 1); task type inferred from the persona (`System`/`automated` → service) and the verb (send/publish → send task; approve/submit/enter/… → user task).\n- **Areas** (`L0-NN.bpmn`): one collapsed sub-process per group, placed in the lane where most of its L2s sit.\n",
           "| Diagram | Kind | Lanes | Steps | BPMN | SVG |\n|---|---|---|---|---|---|"]
    for f in all_models():
        base = diagram_basename(f); kind = "flow" if not f.get("kind") else ("area" if f["kind"] == "l0" else "group")
        out.append(f"| {f['name'] if f.get('kind') else f['id']+' '+f['name']} | {kind} | {'; '.join(f['lanes'])} | {len(f['steps'])} | [{base}.bpmn](../diagrams/bpmn/generated/{base}.bpmn) | [{base}.svg](../assets/diagrams/{base}.svg) |")
    W("docs/diagrams.md", "\n".join(out))

# ---------------- site ----------------
def gen_site():
    tpl = open(os.path.join(ROOT, "site/templates/app.html"), encoding="utf-8").read()
    payload = json.dumps(CAT, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    W("site/index.html", tpl.replace("__DATA__", payload))
    # data copy for anyone who wants to consume the catalog from the Pages site
    W("site/catalog.json", json.dumps(CAT, ensure_ascii=False, indent=1))

# ---------------- xlsx ----------------
def gen_xlsx():
    from xlsx_build import build
    build(ROOT, CAT, L0S, L1S, L2S, FLOWS, FW, CFG, CAL, [(diagram_basename(f), f) for f in all_models()])

if __name__ == "__main__":
    gen_mermaid(); n = gen_bpmn(); gen_docs(); gen_site(); gen_xlsx()
    print(f"generated: v{VERSION} · {len(L0S)} L0 · {len(L1S)} L1 · {len(L2S)} L2 · {len(FLOWS)} flows · {n} BPMN diagrams → docs/, diagrams/, assets/, site/, dist/")
