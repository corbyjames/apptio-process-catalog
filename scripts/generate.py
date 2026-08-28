#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate all derived artifacts from data/*.yaml.

Outputs (all overwritten on every run — edit data/, not these):
  docs/*.md                     catalog documentation (GitHub-rendered, incl. Mermaid)
  diagrams/mermaid/*.md         L0 landscape + per-area L1/L2 Mermaid diagrams
  diagrams/bpmn/generated/*.bpmn  BPMN 2.0 XML per L1 process (open in bpmn.io / Camunda)
  site/index.html               interactive dashboard (GitHub Pages)
  site/viewer.html              bpmn-js viewer/editor for the .bpmn files
  site/bpmn-manifest.json       file list for the viewer
  dist/Apptio_Process_Catalog_L0-L2.xlsx

Hand-edited diagram homes that this script NEVER touches:
  diagrams/bpmn/custom/         refined BPMN models (viewer lists them first)
  diagrams/drawio/              draw.io sources
"""
import json, os, sys, html, re
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(name):
    with open(os.path.join(ROOT, "data", name)) as f: return yaml.safe_load(f)

L0 = load("l0.yaml"); ROWS = load("catalog.yaml"); FLOWS = load("flows.yaml")
FRAMEWORKS = load("frameworks.yaml"); CFG = load("tool-config.yaml"); LINKS = load("l0-links.yaml")
CALENDAR = load("calendar.yaml")
for r in ROWS: r["l0id"] = r["l1id"].split(".")[0]; r["l0"] = L0[r["l0id"]]["name"]
FAM = lambda t: ("Targetprocess" if t=="Targetprocess" else "Costing" if t.startswith("Costing") else
                 "Planning" if t.startswith("Planning") else "Cloudability" if t.startswith("Cloudability") else "Cross-tool")
for r in ROWS: r["family"] = FAM(r["tool"])
def l1s_of(l0id):
    out, seen = [], set()
    for r in ROWS:
        if r["l0id"]==l0id and r["l1id"] not in seen: seen.add(r["l1id"]); out.append((r["l1id"], r["l1"]))
    return out
def lane_of(r):
    p = re.split(r"[,|]", r["personas"])[0].strip()
    return re.sub(r"\s*\(automated\)","", re.sub(r"^Lanes:\s*","",p)) or "Process owner"
def ensure(d): os.makedirs(os.path.join(ROOT,d), exist_ok=True)
for d in ("docs","diagrams/mermaid","diagrams/bpmn/generated","site","dist"): ensure(d)
W = lambda p, s: open(os.path.join(ROOT,p),"w").write(s)
mmid = lambda s: "N"+re.sub(r"[^A-Za-z0-9]","_",s)

# ---------------- docs ----------------
def gen_docs():
    out = ["# IBM Apptio Process Catalog — Overview (L0 Map)\n",
    "Generated from `data/` — **edit the YAML, not this file.**\n",
    "| L0 | Area | Primary tool | Framing |\n|---|---|---|---|"]
    for k,v in sorted(L0.items()):
        out.append(f"| {k} | **{v['name']}** | {v['primary']} | {v['frameworks']} |")
    out.append("\n## L0 landscape\n")
    out.append(mermaid_l0())
    out.append("\n## Cross-tool E2E flows\n")
    out.append('The story: **"Targets down. Rates back. Actuals in. TCO up."** Full step tables in `data/flows.yaml`; the reviewed master model is `diagrams/bpmn/custom/apptio-e2e-flow.bpmn`.\n')
    cur=None
    for f in FLOWS:
        if f["flow"]!=cur:
            cur=f["flow"]; out.append(f"\n### {f['flow']} — {f['name']}\n")
            out.append("| Step | Type | Lane | Task / Event | Notes |\n|---|---|---|---|---|")
        out.append(f"| {f['step']} | {f['type']} | {f['lane']} | {f['task']} | {f.get('notes') or ''} |")
    out.append("\n## Hybrid planning vs agile-only\n")
    out.append("Every L2 carries a Delivery Model tag: Any (methodology-agnostic), Agile (PI planning, Portfolio Kanban, WSJF, story-point capitalization), Traditional (stage-gate/milestone governance), or Hybrid (both governed side by side: 02.3.4 hybrid portfolio view, 02.4.1/02.2.3 dual funding, 04.2.1/04.3.4 team- and role-based capacity, 06.4.5 multi-approach capitalization).\n")
    W("docs/overview.md","\n".join(out))

    out = ["# Full Catalog — L0-L2\n","Generated from `data/catalog.yaml` — **edit the YAML, not this file.**\n"]
    for k,v in sorted(L0.items()):
        out.append(f"\n## L0-{k} {v['name']}\n")
        out.append(f"*{v['desc']}* Primary: **{v['primary']}**. Lanes: {v['lanes']}.\n")
        out.append(f"Diagrams: [Mermaid](../diagrams/mermaid/area-{k}.md)\n")
        last=None
        for r in [r for r in ROWS if r["l0id"]==k]:
            if r["l1id"]!=last:
                last=r["l1id"]
                out.append(f"\n### {r['l1id']} {r['l1']}\n")
                out.append(f"BPMN: [`diagrams/bpmn/generated/{r['l1id']}.bpmn`](../diagrams/bpmn/generated/{r['l1id']}.bpmn)\n")
            out.append(f"**{r['l2id']} {r['l2']}** — {r['desc']}")
            out.append(f"- Delivery model: {r['delivery']} | Tool: {r['tool']}" + (f" (+ {r['support']})" if r['support'] else "") + f" | Personas: {r['personas']} | Cadence: {r['cadence']}")
            out.append(f"- Inputs: {r['inputs']} → Outputs: {r['outputs']}")
            out.append(f"- Config: {r['config']}")
            out.append(f"- Framework: {r['fw']} | Evidence: {r['src']}\n")
    W("docs/catalog-L0-L2.md","\n".join(out))

    out = ["# Tool Configuration Reference\n","Generated from `data/tool-config.yaml`.\n"]
    cur=None
    for c in CFG:
        if c["tool"]!=cur: cur=c["tool"]; out.append(f"\n## {c['tool']}\n")
        out.append(f"**{c['domain']}**: {c['objects']}" + (f" *({c['notes']})*" if c.get("notes") else "") + "\n")
    W("docs/tool-config-reference.md","\n".join(out))

    out = ["# Annual Operating Calendar\n","Generated from `data/calendar.yaml` (months are fiscal months, FM1 = fiscal year start). The dashboard's Operating Calendar tab renders this with a fiscal-year selector.\n"]
    for st in CALENDAR["streams"]:
        out.append(f"\n## {st['name']}\n")
        out.append("| Process | Cadence | Fiscal months | Catalog refs |\n|---|---|---|---|")
        for en in st["entries"]:
            months = ", ".join(f"FM{m}" for m in en["fm"]) if len(en["fm"])<12 else "All year"
            out.append(f"| {en['name']} | {en['cadence']} | {months} | {', '.join(en.get('refs',[]))} |")
        for en in st["entries"]:
            out.append(f"\n**{en['name']}** — {en['desc']}")
    W("docs/operating-calendar.md","\n".join(out))

# ---------------- mermaid ----------------
def mermaid_l0():
    g = ["```mermaid","flowchart LR"]
    groups = [("SPM","Targetprocess — SPM",["01","02","03","04"]),("ITFM","Planning & Costing — ITFM/TBM",["05","06","08"]),("FINOPS","Cloudability — FinOps",["07"]),("ENABLE","Integration & Enablement",["09","10"])]
    for gid,label,ids in groups:
        g.append(f'  subgraph {gid}["{label}"]')
        for i in ids: g.append(f'    A{i}["{i} {L0[i]["name"]}"]')
        g.append("  end")
    for l in LINKS: g.append(f'  A{l["frm"]} -- "{l["label"]}" --> A{l["to"]}')
    g.append("```")
    return "\n".join(g)

def gen_mermaid():
    W("diagrams/mermaid/l0-landscape.md", "# L0 Process Landscape\n\nGenerated — edit `data/l0.yaml` / `data/l0-links.yaml`.\n\n" + mermaid_l0() + "\n")
    for k,v in sorted(L0.items()):
        out = [f"# {k} {v['name']} — L1/L2 Diagrams\n", "Generated — edit `data/catalog.yaml`.\n", "## L1 process chain\n","```mermaid","flowchart LR","  S((start))"]
        chain = l1s_of(k)
        prev="S"
        for lid,lname in chain:
            nid=mmid(lid); out.append(f'  {nid}[["{lid} {lname}"]]'); out.append(f"  {prev} --> {nid}"); prev=nid
        out.append(f"  {prev} --> E(((end)))"); out.append("```")
        for lid,lname in chain:
            out.append(f"\n## {lid} {lname} (L2)\n")
            out.append("```mermaid"); out.append("flowchart LR"); out.append("  S((start))")
            prev="S"
            for r in [r for r in ROWS if r["l1id"]==lid]:
                nid=mmid(r["l2id"])
                out.append(f'  {nid}["{r["l2id"]} {r["l2"]}<br/><i>{lane_of(r)} · {r["delivery"]}</i>"]')
                out.append(f"  {prev} --> {nid}"); prev=nid
            out.append(f"  {prev} --> E(((end)))"); out.append("```")
        W(f"diagrams/mermaid/area-{k}.md","\n".join(out)+"\n")

# ---------------- BPMN ----------------
def bpmn_for_l1(l1id):
    rs = [r for r in ROWS if r["l1id"]==l1id]
    lanes=[]
    for r in rs:
        ln=lane_of(r)
        if ln not in lanes: lanes.append(ln)
    laneH, headW, stepW, gap, padT = 110, 160, 190, 40, 14
    Wd = headW + len(rs)*(stepW+gap)+120; Hd = len(lanes)*laneH+padT*2
    pos=[]
    for i,r in enumerate(rs):
        pos.append((headW+34+i*(stepW+gap), padT+lanes.index(lane_of(r))*laneH+(laneH-8)/2-29, stepW, 58, r))
    x = lambda s: html.escape(str(s), quote=True)
    idify = lambda s: re.sub(r"[^A-Za-z0-9]","_",s)
    nid = lambda r: "Task_"+idify(r["l2id"])
    pid = "Process_"+idify(l1id); l1name = rs[0]["l1"]
    lanesXml=""
    for i,ln in enumerate(lanes):
        refs = ("<bpmn:flowNodeRef>StartEvent_1</bpmn:flowNodeRef>" if i==0 else "")
        refs += "".join(f"<bpmn:flowNodeRef>{nid(r)}</bpmn:flowNodeRef>" for r in rs if lane_of(r)==ln)
        if lane_of(rs[-1])==ln: refs += "<bpmn:flowNodeRef>EndEvent_1</bpmn:flowNodeRef>"
        lanesXml += f'<bpmn:lane id="Lane_{i+1}" name="{x(ln)}">{refs}</bpmn:lane>'
    nodes = '<bpmn:startEvent id="StartEvent_1" name="Start"><bpmn:outgoing>Flow_0</bpmn:outgoing></bpmn:startEvent>'
    for i,r in enumerate(rs):
        nodes += f'<bpmn:task id="{nid(r)}" name="{x(r["l2id"]+" "+r["l2"])}"><bpmn:incoming>Flow_{i}</bpmn:incoming><bpmn:outgoing>Flow_{i+1}</bpmn:outgoing></bpmn:task>'
    nodes += f'<bpmn:endEvent id="EndEvent_1" name="End"><bpmn:incoming>Flow_{len(rs)}</bpmn:incoming></bpmn:endEvent>'
    flows = f'<bpmn:sequenceFlow id="Flow_0" sourceRef="StartEvent_1" targetRef="{nid(rs[0])}"/>'
    for i,r in enumerate(rs):
        tgt = nid(rs[i+1]) if i<len(rs)-1 else "EndEvent_1"
        flows += f'<bpmn:sequenceFlow id="Flow_{i+1}" sourceRef="{nid(r)}" targetRef="{tgt}"/>'
    shapes = f'<bpmndi:BPMNShape id="Participant_1_di" bpmnElement="Participant_1" isHorizontal="true"><dc:Bounds x="0" y="0" width="{Wd}" height="{Hd}"/></bpmndi:BPMNShape>'
    for i,ln in enumerate(lanes):
        shapes += f'<bpmndi:BPMNShape id="Lane_{i+1}_di" bpmnElement="Lane_{i+1}" isHorizontal="true"><dc:Bounds x="30" y="{padT+i*laneH}" width="{Wd-30}" height="{laneH}"/></bpmndi:BPMNShape>'
    sy = pos[0][1]+29; ey = pos[-1][1]+29; last = pos[-1]
    shapes += f'<bpmndi:BPMNShape id="StartEvent_1_di" bpmnElement="StartEvent_1"><dc:Bounds x="{headW-5}" y="{sy-13}" width="26" height="26"/></bpmndi:BPMNShape>'
    for q in pos:
        shapes += f'<bpmndi:BPMNShape id="{nid(q[4])}_di" bpmnElement="{nid(q[4])}"><dc:Bounds x="{q[0]}" y="{q[1]}" width="{q[2]}" height="{q[3]}"/></bpmndi:BPMNShape>'
    shapes += f'<bpmndi:BPMNShape id="EndEvent_1_di" bpmnElement="EndEvent_1"><dc:Bounds x="{last[0]+last[2]+17}" y="{ey-13}" width="26" height="26"/></bpmndi:BPMNShape>'
    def wp(x1,y1,x2,y2):
        return f'<di:waypoint x="{x1}" y="{y1}"/><di:waypoint x="{(x1+x2)/2}" y="{y1}"/><di:waypoint x="{(x1+x2)/2}" y="{y2}"/><di:waypoint x="{x2}" y="{y2}"/>'
    edges = f'<bpmndi:BPMNEdge id="Flow_0_di" bpmnElement="Flow_0">{wp(headW+21,sy,pos[0][0],sy)}</bpmndi:BPMNEdge>'
    for i,q in enumerate(pos):
        tx = pos[i+1][0] if i<len(pos)-1 else last[0]+last[2]+17
        ty = pos[i+1][1]+29 if i<len(pos)-1 else ey
        edges += f'<bpmndi:BPMNEdge id="Flow_{i+1}_di" bpmnElement="Flow_{i+1}">{wp(q[0]+q[2], q[1]+29, tx, ty)}</bpmndi:BPMNEdge>'
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Defs_{idify(l1id)}" targetNamespace="http://apptio-process-catalog">
<bpmn:collaboration id="Collab_1"><bpmn:participant id="Participant_1" name="{x(l1id+" "+l1name)}" processRef="{pid}"/></bpmn:collaboration>
<bpmn:process id="{pid}" name="{x(l1name)}" isExecutable="false"><bpmn:laneSet id="LaneSet_1">{lanesXml}</bpmn:laneSet>{nodes}{flows}</bpmn:process>
<bpmndi:BPMNDiagram id="Diagram_1"><bpmndi:BPMNPlane id="Plane_1" bpmnElement="Collab_1">{shapes}{edges}</bpmndi:BPMNPlane></bpmndi:BPMNDiagram>
</bpmn:definitions>'''

def gen_bpmn():
    seen=set()
    for r in ROWS:
        if r["l1id"] in seen: continue
        seen.add(r["l1id"])
        W(f"diagrams/bpmn/generated/{r['l1id']}.bpmn", bpmn_for_l1(r["l1id"]))
    # viewer manifest: custom first
    custom = sorted(f for f in os.listdir(os.path.join(ROOT,"diagrams/bpmn/custom")) if f.endswith(".bpmn"))
    gen = sorted(f for f in os.listdir(os.path.join(ROOT,"diagrams/bpmn/generated")) if f.endswith(".bpmn"))
    man = [{"path":f"../diagrams/bpmn/custom/{f}","label":f"custom / {f}"} for f in custom] + \
          [{"path":f"../diagrams/bpmn/generated/{f}","label":f"generated / {f}"} for f in gen]
    W("site/bpmn-manifest.json", json.dumps(man, indent=1))

# ---------------- site ----------------
def gen_site():
    head = open(os.path.join(ROOT,"site/templates/template_head.html")).read()
    js = open(os.path.join(ROOT,"site/templates/template_js.html")).read()
    data = {"l0":[dict(id=k, name=v["name"], desc=v["desc"], primary=v["primary"], supporting=v.get("supporting",""), frameworks=v["frameworks"], lanes=v["lanes"]) for k,v in sorted(L0.items())],
            "rows":ROWS, "flows":FLOWS, "frameworks":FRAMEWORKS, "calendar":CALENDAR}
    payload = json.dumps(data, ensure_ascii=False).replace("</","<\\/")
    W("site/index.html", head + js.replace("__DATA__", payload))

# ---------------- xlsx ----------------
def gen_xlsx():
    sys.path.insert(0, os.path.join(ROOT,"scripts"))
    from xlsx_build import build
    build(ROOT, L0, ROWS, FLOWS, FRAMEWORKS, CFG, l1s_of, CALENDAR)

if __name__ == "__main__":
    gen_docs(); gen_mermaid(); gen_bpmn(); gen_site(); gen_xlsx()
    print("generated: docs/, diagrams/mermaid/, diagrams/bpmn/generated/, site/, dist/")
