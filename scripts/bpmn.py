# -*- coding: utf-8 -*-
"""BPMN 2.0 model builder, layout engine, SVG renderer and XML (with DI) writer.

The same "flow" shape drives everything: {id, name, title, summary, lanes:[...],
steps:[{n, type, lane, task, note, l2:[...], href}]}. Cross-tool flows come straight
from catalog.json; L1 groups and L0 areas are turned into that shape by
`l1_to_flow` / `l0_to_flow` (lane = persona-derived BPMN lane, one task per L2 or one
collapsed sub-process per L1).

The layout is a faithful port of the in-page JavaScript renderer in
site/templates/app.js so the static SVG snapshots and the live site agree.
"""
import re, html

BP = dict(laneHead=150, colW=208, nodeW=162, taskH=74, laneBase=122, slotH=96, padX=28, evR=18, gwR=24)
esc = lambda s: html.escape(str("" if s is None else s), quote=True)

# ------------------------------------------------------------------ lane + type inference
LANE_KEYS = {
  "C-Suite/Strategy": ["c-suite","cio","cfo","vp strategy","strategy","leadership","sponsor"],
  "Portfolio Management": ["portfolio","lpm","value stream","vs owner","epic owner","lace","hiring manager"],
  "Finance": ["finance","fp&a","accounting","budget owner","cost-category","procurement"],
  "Requesters/Business": ["requester","service desk","business owner","business"],
  "PMO": ["pmo","project manager","gate"],
  "RTE/Program": ["rte","pi coordinator","program","release","ste","transformation","scrum master"],
  "Agile Teams": ["team","art","stakeholder","business owner"],
  "Product Management": ["product owner","product"],
  "Dev tools (Jira/ADO)": ["jira","ado","git","platform admin"],
  "Resource Management": ["resource","capacity","managers","team members"],
  "HR/Approvers": ["hr","approver"],
  "Finance (IT Planning)": ["finance","system (adm)","system"],
  "IT Finance": ["it finance","finance","tbm analyst","tbm office","accounting","system","restricted"],
  "Budget Owners": ["budget owner","service/app owner","vendor mgmt","infrastructure","resource mgmt","pmo","hr"],
  "FP&A": ["fp&a","cost-category"],
  "CIO": ["cio","cfo","leadership","portfolio"],
  "TBM Office/IT Finance": ["tbm","it finance","finance","accounting","vendor"],
  "Costing Admin": ["costing admin","system","automated"],
  "App/Service Owners": ["app owner","service owner","app/service","ea","bu"],
  "ERP-GL": [],
  "FinOps Practitioner": ["finops","practitioner","admin","sustainability","all personas"],
  "Engineering": ["eng","platform","architect"],
  "Cloud vendors": [],
  "TBM Office": ["tbm","analyst","it finance","enterprise finance"],
  "BU Owners": ["bu owner","business"],
  "CIO/CFO": ["cio","cfo","app/platform owners","finops focals"],
  "Service Owners": ["service owner","app owner"],
  "Platform Admins": ["admin","consultant","atp product owner","planning admin","finops admin"],
  "FinOps Team": ["finops"],
  "SPM Governance": ["spm","lace","transformation","governance","security","rte"],
  "Integration Team": ["integration","architecture","data governance"],
}
PRODUCT_LANE_HINT = {"Costing": ["TBM","Costing"], "Planning": ["IT Finance","Finance"], "Cloudability": ["FinOps"], "Targetprocess": ["Portfolio","Platform"]}

def lane_for(l0_lanes, l2):
    """Pick the BPMN lane of an L2 inside its L0's default lanes: first persona in the
    source string that matches a lane wins; fall back to a product hint, then lane 1."""
    personas = [p.strip().lower() for p in re.split(r"[,;/]| and ", l2.get("personas","")) if p.strip()]
    for p in personas:
        for lane in l0_lanes:
            keys = LANE_KEYS.get(lane, [lane.lower()])
            if any(k in p for k in keys): return lane
    for hint in PRODUCT_LANE_HINT.get(l2.get("primary_product",""), []):
        for lane in l0_lanes:
            if hint.lower() in lane.lower(): return lane
    return l0_lanes[0]

_SEND = re.compile(r"^(send|publish|feed|share|distribute|sync)\b", re.I)
_SERVICE = re.compile(r"^(generate|compute|calculate|ingest|load|refresh|run allocations|allocate costs|allocate team|allocate consumption|operate the adm|operate data)", re.I)
_USER = re.compile(r"^(approve|submit|enter|record|score|review|rank|build|create|write|capture|raise|select|narrate|commit|prioritize|triage|decide|vote|scope|rank|set &|define)\b", re.I)

def step_type_for(l2):
    name, personas = l2["name"], l2.get("personas","").lower()
    if re.search(r"\bsystem\b(?!\s*architect)", personas) or "automated" in personas or _SERVICE.search(name): return "Service task"
    if _SEND.search(name): return "Send task (ADM)" if re.search(r"adm|data highway|feed", l2.get("config","").lower()) else "Send task"
    if _USER.search(name): return "User task"
    return "Task"

def l1_to_flow(l0, l1):
    lanes = [x.rstrip(".") for x in l0["lanes"]]
    steps = []
    for l2 in l1["l2s"]:
        steps.append({"n": l2["id"], "type": step_type_for(l2), "lane": lane_for(lanes, l2), "task": l2["name"],
                      "note": l2.get("outcome") and ("Outcome: " + l2["outcome"]) or "", "l2": [l2["id"]]})
    used = [ln for ln in lanes if any(s["lane"]==ln for s in steps)]
    return {"id": "G"+l1["id"].replace(".","_"), "kind": "l1", "name": l1["id"]+" "+l1["name"], "title": l1["name"],
            "summary": f"Process group {l1['id']} in L0-{l0['id']} {l0['name']}: {len(steps)} L2 processes laid out in the order of the catalog, in the BPMN lane of the persona that performs each one.",
            "lanes": used or lanes[:1], "steps": steps}

def l0_to_flow(l0):
    lanes = [x.rstrip(".") for x in l0["lanes"]]
    steps = []
    for l1 in l0["l1s"]:
        f = l1_to_flow(l0, l1)
        # dominant lane of the group
        cnt = {}
        for s in f["steps"]: cnt[s["lane"]] = cnt.get(s["lane"],0)+1
        lane = max(lanes, key=lambda ln: (cnt.get(ln,0), -lanes.index(ln)))
        steps.append({"n": l1["id"], "type": "Sub-process", "lane": lane, "task": l1["name"],
                      "note": f"{len(l1['l2s'])} processes: " + ", ".join(x["id"] for x in l1["l2s"]),
                      "l2": [l1["l2s"][0]["id"]], "href": f"#/l0/{l0['id']}/{l1['id']}"})
    used = [ln for ln in lanes if any(s["lane"]==ln for s in steps)]
    return {"id": "A"+l0["id"], "kind": "l0", "name": "L0-"+l0["id"]+" "+l0["name"], "title": l0["name"],
            "summary": l0["description"], "lanes": used or lanes[:1], "steps": steps}

# ------------------------------------------------------------------ layout (port of app.js)
def kind_of(t):
    t = (t or "").lower()
    if t.startswith("start"): return "startTimer" if "timer" in t else "start"
    if t.startswith("end"): return "end"
    if "gateway" in t: return "gwPar" if "parallel" in t else "gwXor"
    if t.startswith("user"): return "user"
    if t.startswith("service"): return "service"
    if t.startswith("send"): return "send"
    if t.startswith("sub"): return "sub"
    return "task"

def layout(f):
    lanes = list(f["lanes"]); lane_ix = {l:i for i,l in enumerate(lanes)}
    nodes, edges, byN = [], [], {}
    col = -1; group = None; prev = None; slot_use = {}
    is_branch = lambda n: re.match(r"^[a-z]?\d+[a-z]$", n or "") is not None
    base_of = lambda n: n[:-1]
    def place(node):
        k = (node["lane"], node["col"]); node["slot"] = slot_use.get(k,0); slot_use[k] = node["slot"]+1
    steps = list(f["steps"])
    if not re.match(r"^start", steps[0]["type"], re.I):
        steps.insert(0, {"n":"","type":"Start event","lane":steps[0]["lane"],"task":"","l2":[],"implicit":True})
    if not re.match(r"^end", steps[-1]["type"], re.I):
        steps.append({"n":"","type":"End event","lane":steps[-1]["lane"],"task":"","l2":[],"implicit":True})
    for s in steps:
        kind = kind_of(s["type"])
        node = {"id": ("n_"+kind+"_implicit") if s.get("implicit") else ("n_"+re.sub(r"[^\w]","_",s["n"])),
                "n": s["n"], "kind": kind, "label": s["task"], "lane": lane_ix.get(s["lane"],0), "l2": s.get("l2",[]),
                "note": s.get("note","") or "", "type": s["type"], "href": s.get("href")}
        branch = is_branch(s["n"]) and base_of(s["n"]) in byN
        if branch:
            if not group or group["base"] != base_of(s["n"]):
                group = {"base": base_of(s["n"]), "members": []}; col += 1
            node["col"] = col; group["members"].append(node)
        else:
            col += 1; node["col"] = col
            if group and group["members"]:
                for m in group["members"]: edges.append({"from": m["id"], "to": node["id"]})
                group = None
            elif prev:
                e = {"from": prev["id"], "to": node["id"]}
                if prev["kind"].startswith("gw"): e["label"] = prev.get("yesLabel","Yes")
                edges.append(e)
        place(node); nodes.append(node)
        if s["n"]: byN[s["n"]] = node
        prev = node
        if branch:
            gw = byN[base_of(s["n"])]; labels = gw.get("branchLabels", [])
            i = len(group["members"])-1
            edges.append({"from": gw["id"], "to": node["id"], "label": labels[i] if i < len(labels) else ""})
        if kind.startswith("gw"):
            m = re.findall(r"(?:^|;\s*)(Yes|No)\s*:\s*([^;]+)", node["note"], re.I)
            node["branchLabels"] = [x[0] for x in m]; node["yesLabel"] = "Yes"
            endM = re.search(r"No:\s*end event\s*'([^']+)'", node["note"], re.I)
            if endM:
                en = {"id": node["id"]+"_no", "n":"", "kind":"end", "label": endM.group(1), "lane": node["lane"], "col": node["col"], "l2": [], "note":"", "type":"End event", "extra":True}
                place(en); nodes.append(en); edges.append({"from": node["id"], "to": en["id"], "label":"No"})
            loopM = re.search(r"loop to\s+([\w.]+)", node["note"], re.I)
            if loopM and loopM.group(1) in byN:
                edges.append({"from": node["id"], "to": byN[loopM.group(1)]["id"], "label":"No", "loop":True})
    lane_slots = [max([1]+[n["slot"]+1 for n in nodes if n["lane"]==li]) for li in range(len(lanes))]
    lane_h = [BP["laneBase"]+(s-1)*BP["slotH"] for s in lane_slots]
    lane_y = []; y = 0
    for h in lane_h: lane_y.append(y); y += h
    H = y; W = BP["laneHead"]+(col+1)*BP["colW"]+BP["padX"]
    for n in nodes:
        n["cx"] = BP["laneHead"]+BP["padX"]+n["col"]*BP["colW"]+BP["nodeW"]/2
        n["cy"] = lane_y[n["lane"]]+BP["laneBase"]/2+n["slot"]*BP["slotH"]
        if n["kind"] in ("start","startTimer","end"): n["w"]=n["h"]=BP["evR"]*2
        elif n["kind"].startswith("gw"): n["w"]=n["h"]=BP["gwR"]*2
        else: n["w"]=BP["nodeW"]; n["h"]=BP["taskH"]
        n["x"]=n["cx"]-n["w"]/2; n["y"]=n["cy"]-n["h"]/2
    by_id = {n["id"]:n for n in nodes}
    for e in edges:
        a, b = by_id[e["from"]], by_id[e["to"]]
        if e.get("loop"):
            yb = max(a["y"]+a["h"], b["y"]+b["h"])+18
            pts = [(a["cx"],a["y"]+a["h"]),(a["cx"],yb),(b["cx"],yb),(b["cx"],b["y"]+b["h"])]
        elif b["col"]==a["col"]: pts = [(a["cx"],a["y"]+a["h"]),(a["cx"],b["y"])]
        elif abs(a["cy"]-b["cy"])<1: pts = [(a["x"]+a["w"],a["cy"]),(b["x"],b["cy"])]
        else:
            mx = a["x"]+a["w"]+(b["x"]-(a["x"]+a["w"]))/2
            pts = [(a["x"]+a["w"],a["cy"]),(mx,a["cy"]),(mx,b["cy"]),(b["x"],b["cy"])]
        e["pts"] = pts
    return {"lanes":lanes,"laneY":lane_y,"laneH":lane_h,"nodes":nodes,"edges":edges,"W":W,"H":H}

def wrap(s, max_chars, max_lines):
    words = str(s).split(); lines=[]; cur=""
    for w in words:
        if len((cur+" "+w).strip())>max_chars and cur: lines.append(cur); cur=w
        else: cur=(cur+" "+w).strip()
    if cur: lines.append(cur)
    if len(lines)>max_lines:
        lines = lines[:max_lines]; lines[-1] = lines[-1][:-2]+"…"
    return lines

# ------------------------------------------------------------------ SVG (standalone, theme-aware)
LANE_PAL = ["#5B6E1F","#3A6EA5","#8C5A2B","#2A8C8C","#5E5A72"]
SVG_STYLE = """<style>
svg{font-family:"IBM Plex Sans",-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:#1E2422}
.lane0{fill:#FFFFFF}.lane1{fill:#EBEDE8}.ground{fill:#F3F4F1}.gw{fill:#FAF0DC}.env{fill:#FFFFFF}
@media (prefers-color-scheme: dark){svg{color:#E8EAE6}.lane0{fill:#202423}.lane1{fill:#2A2F2D}.ground{fill:#181B1A}.gw{fill:#3A2F17}.env{fill:#202423}}
</style>"""

def icon(kind, x, y):
    c = 'stroke="currentColor" fill="none" stroke-width="1.4"'
    if kind=="user": return f'<g transform="translate({x},{y})" {c}><circle cx="6" cy="4" r="3"/><path d="M0 13c0-4 12-4 12 0"/></g>'
    if kind=="service": return f'<g transform="translate({x},{y})" {c}><circle cx="6" cy="6" r="2.2"/><circle cx="6" cy="6" r="5.2" stroke-dasharray="2 1.6"/></g>'
    if kind=="send": return f'<g transform="translate({x},{y})"><rect width="13" height="9" rx="1" fill="currentColor"/><path d="M0.5 1l6 4.5 6-4.5" class="env" stroke="#fff" stroke-width="1.2" fill="none"/></g>'
    return ""

def svg(f, title=None, link_base=None):
    L = layout(f)
    out = []
    for i, name in enumerate(L["lanes"]):
        y, h = L["laneY"][i], L["laneH"][i]; lines = wrap(name, 18, 3)
        tsp = "".join(f'<tspan x="{BP["laneHead"]/2+3}" dy="{14 if k else 0}">{esc(t)}</tspan>' for k,t in enumerate(lines))
        empty = "" if any(n["lane"]==i for n in L["nodes"]) else f'<text x="{BP["laneHead"]+BP["padX"]}" y="{y+h/2+4}" font-size="11" font-style="italic" fill="currentColor" fill-opacity=".55">Receiving system — no catalog step modeled in this lane</text>'
        out.append(f'<g><rect x="0" y="{y}" width="{L["W"]}" height="{h}" class="lane{i%2}" stroke="currentColor" stroke-opacity=".35"/><rect x="0" y="{y}" width="6" height="{h}" fill="{LANE_PAL[i%len(LANE_PAL)]}"/><text x="{BP["laneHead"]/2+3}" y="{y+h/2-(len(lines)-1)*7}" text-anchor="middle" font-size="12" font-weight="600" fill="currentColor">{tsp}</text><line x1="{BP["laneHead"]}" y1="{y}" x2="{BP["laneHead"]}" y2="{y+h}" stroke="currentColor" stroke-opacity=".35"/>{empty}</g>')
    for e in L["edges"]:
        d = "M"+"L".join(f"{p[0]:.0f} {p[1]:.0f}" for p in e["pts"]); lab=""
        if e.get("label"):
            pts=e["pts"]; anchor="start"
            if e.get("loop"): lx=(pts[1][0]+pts[2][0])/2; ly=pts[1][1]-4; anchor="middle"
            elif len(pts)==2 and pts[0][0]==pts[1][0]: lx=pts[0][0]+7; ly=(pts[0][1]+pts[1][1])/2+4
            elif len(pts)==2: lx=(pts[0][0]+pts[1][0])/2; ly=pts[0][1]-6; anchor="middle"
            else: lx=pts[2][0]+6; ly=pts[2][1]-6
            lab=f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="10" font-weight="600" fill="currentColor" text-anchor="{anchor}">{esc(e["label"])}</text>'
        out.append(f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>{lab}')
    for n in L["nodes"]:
        t = f'<title>{esc((n["n"]+" · " if n["n"] else "")+n["label"]+(" ("+n["type"]+")" if n["type"] else ""))}{esc(" — "+n["note"]) if n["note"] else ""}</title>'
        cx, cy = n["cx"], n["cy"]
        if n["kind"] in ("start","startTimer","end"):
            body = f'<circle cx="{cx}" cy="{cy}" r="{BP["evR"]}" class="ground" stroke="currentColor" stroke-width="{3 if n["kind"]=="end" else 1.5}"/>'
            if n["kind"]=="startTimer": body += f'<circle cx="{cx}" cy="{cy}" r="11" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M{cx} {cy-7}v7h5" fill="none" stroke="currentColor" stroke-width="1.4"/>'
            lines = wrap(n["label"],22,2)
            body += f'<text x="{cx}" y="{cy+BP["evR"]+13}" text-anchor="middle" font-size="10.5" fill="currentColor">'+"".join(f'<tspan x="{cx}" dy="{12 if k else 0}">{esc(l)}</tspan>' for k,l in enumerate(lines))+'</text>'
        elif n["kind"].startswith("gw"):
            r = BP["gwR"]
            body = f'<path d="M{cx} {cy-r}L{cx+r} {cy}L{cx} {cy+r}L{cx-r} {cy}Z" class="gw" stroke="currentColor" stroke-width="1.5"/>'
            body += (f'<path d="M{cx} {cy-10}v20M{cx-10} {cy}h20" stroke="currentColor" stroke-width="2.2"/>' if n["kind"]=="gwPar" else f'<path d="M{cx-7} {cy-7}l14 14M{cx+7} {cy-7}l-14 14" stroke="currentColor" stroke-width="2.2"/>')
            lines = wrap(n["label"],24,2)
            body += f'<text x="{cx}" y="{cy-r-8-(len(lines)-1)*12}" text-anchor="middle" font-size="10.5" font-weight="600" fill="currentColor">'+"".join(f'<tspan x="{cx}" dy="{12 if k else 0}">{esc(l)}</tspan>' for k,l in enumerate(lines))+'</text>'
            body += f'<text x="{cx+r+4}" y="{cy+r+2}" font-size="9.5" fill="currentColor" fill-opacity=".6" font-family="monospace">{esc(n["n"])}</text>'
        else:
            lines = wrap(n["label"],26,3); x,y,w,h = n["x"],n["y"],n["w"],n["h"]
            body = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="ground" stroke="currentColor" stroke-width="{2.2 if n["kind"]=="sub" else 1.5}"/>'
            if n["kind"]=="send": body += f'<rect x="{x+3}" y="{y+3}" width="{w}" height="{h}" rx="8" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity=".5"/>'
            if n["kind"]=="sub": body += f'<rect x="{cx-6}" y="{y+h-14}" width="12" height="12" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M{cx-3} {y+h-8}h6M{cx} {y+h-11}v6" stroke="currentColor" stroke-width="1.2"/>'
            body += icon(n["kind"], x+8, y+7)
            body += f'<text x="{x+w-7}" y="{y+13}" text-anchor="end" font-size="9.5" fill="currentColor" fill-opacity=".6" font-family="monospace">{esc(n["n"])}{" · ADM" if "ADM" in n["type"] else ""}</text>'
            ty = y+18+(h-18)/2+4-(len(lines)-1)*6.5
            body += f'<text x="{cx}" y="{ty}" text-anchor="middle" font-size="10.5" fill="currentColor">'+"".join(f'<tspan x="{cx}" dy="{13 if k else 0}">{esc(l)}</tspan>' for k,l in enumerate(lines))+'</text>'
        g = f'<g class="bn">{t}{body}</g>'
        href = n.get("href") or (n["l2"] and link_base and (link_base % n["l2"][0]))
        out.append(f'<a href="{esc(href)}">{g}</a>' if href else g)
    aria = f'BPMN swimlane diagram of {f["name"]}: {len(L["lanes"])} lanes, {len(f["steps"])} steps'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {L["W"]} {L["H"]}" width="{L["W"]}" height="{L["H"]}" role="img" aria-label="{esc(aria)}">'
            f'<title>{esc(title or f["name"])}</title>{SVG_STYLE}<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="currentColor"/></marker></defs>'
            + "".join(out) + "</svg>")

# ------------------------------------------------------------------ BPMN 2.0 XML with DI
TAG = {"start":"startEvent","startTimer":"startEvent","end":"endEvent","gwXor":"exclusiveGateway","gwPar":"parallelGateway","user":"userTask","service":"serviceTask","send":"sendTask","task":"task","sub":"subProcess"}

def xml(f, version="0.6.0"):
    L = layout(f); x = esc
    fid = re.sub(r"[^\w]","_",f["id"]); pid, ppid = "Process_"+fid, "Participant_"+fid
    inc, out = {}, {}
    for i,e in enumerate(L["edges"]):
        e["id"] = "Flow_"+str(i); out.setdefault(e["from"],[]).append(e["id"]); inc.setdefault(e["to"],[]).append(e["id"])
    lanes = "\n".join(f'      <bpmn:lane id="Lane_{fid}_{i}" name="{x(name)}">\n' + "\n".join(f'        <bpmn:flowNodeRef>{n["id"]}</bpmn:flowNodeRef>' for n in L["nodes"] if n["lane"]==i) + '\n      </bpmn:lane>' for i,name in enumerate(L["lanes"]))
    nodes = []
    for n in L["nodes"]:
        doc = (f"Catalog: {', '.join(n['l2'])}. " if n["l2"] else "") + (n["note"] or "")
        inner = (f"\n      <bpmn:documentation>{x(doc)}</bpmn:documentation>" if doc else "")
        inner += "".join(f"\n      <bpmn:incoming>{i}</bpmn:incoming>" for i in inc.get(n["id"],[]))
        inner += "".join(f"\n      <bpmn:outgoing>{o}</bpmn:outgoing>" for o in out.get(n["id"],[]))
        if n["kind"]=="startTimer": inner += "\n      <bpmn:timerEventDefinition />"
        tag = TAG[n["kind"]]
        sub_attr = ' triggeredByEvent="false"' if n["kind"]=="sub" else ""
        nodes.append(f'    <bpmn:{tag} id="{n["id"]}" name="{x(n["label"])}"{sub_attr}>{inner}\n    </bpmn:{tag}>')
    flows = "\n".join(f'    <bpmn:sequenceFlow id="{e["id"]}" sourceRef="{e["from"]}" targetRef="{e["to"]}"' + (f' name="{x(e["label"])}"' if e.get("label") else "") + " />" for e in L["edges"])
    exp = lambda n: ' isExpanded="false"' if n["kind"]=="sub" else ""
    shapes = [f'      <bpmndi:BPMNShape id="{ppid}_di" bpmnElement="{ppid}" isHorizontal="true"><dc:Bounds x="0" y="0" width="{L["W"]}" height="{L["H"]}" /></bpmndi:BPMNShape>']
    shapes += [f'      <bpmndi:BPMNShape id="Lane_{fid}_{i}_di" bpmnElement="Lane_{fid}_{i}" isHorizontal="true"><dc:Bounds x="30" y="{L["laneY"][i]}" width="{L["W"]-30}" height="{L["laneH"][i]}" /></bpmndi:BPMNShape>' for i in range(len(L["lanes"]))]
    shapes += [f'      <bpmndi:BPMNShape id="{n["id"]}_di" bpmnElement="{n["id"]}"{exp(n)}><dc:Bounds x="{n["x"]:.0f}" y="{n["y"]:.0f}" width="{n["w"]}" height="{n["h"]}" /></bpmndi:BPMNShape>' for n in L["nodes"]]
    shapes += [f'      <bpmndi:BPMNEdge id="{e["id"]}_di" bpmnElement="{e["id"]}">' + "".join(f'<di:waypoint x="{p[0]:.0f}" y="{p[1]:.0f}" />' for p in e["pts"]) + '</bpmndi:BPMNEdge>' for e in L["edges"]]
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_{fid}" targetNamespace="urn:apptio:process-catalog" exporter="Apptio Process Catalog" exporterVersion="{version}">
  <bpmn:collaboration id="Collaboration_{fid}">
    <bpmn:participant id="{ppid}" name="{x(f["name"]+" — "+f["title"])}" processRef="{pid}" />
  </bpmn:collaboration>
  <bpmn:process id="{pid}" name="{x(f["title"])}" isExecutable="false">
    <bpmn:documentation>{x(f.get("summary",""))}</bpmn:documentation>
    <bpmn:laneSet id="LaneSet_{fid}">
{lanes}
    </bpmn:laneSet>
{chr(10).join(nodes)}
{flows}
  </bpmn:process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_{fid}">
    <bpmndi:BPMNPlane id="BPMNPlane_{fid}" bpmnElement="Collaboration_{fid}">
{chr(10).join(shapes)}
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</bpmn:definitions>
'''
