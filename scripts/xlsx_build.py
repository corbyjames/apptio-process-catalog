# -*- coding: utf-8 -*-
"""Excel workbook generator — called by generate.py."""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build(ROOT, L0, ALL, FLOWS_RAW, FRAMEWORKS, CFG_RAW, l1s_of, CALENDAR=None):
    FLOWS = [(f["flow"], f["name"], f["step"], f["type"], f["lane"], f["task"], f.get("notes") or "") for f in FLOWS_RAW]
    CFG_T = [(c["tool"], c["domain"], c["objects"], c.get("notes") or "") for c in CFG_RAW]
    FONT = "Arial"
    HDR_FILL = PatternFill("solid", fgColor="1F3864")
    HDR_FONT = Font(name=FONT, bold=True, color="FFFFFF", size=10)
    BASE = Font(name=FONT, size=10)
    BOLD = Font(name=FONT, size=10, bold=True)
    THIN = Border(*[Side(style="thin", color="BFBFBF")]*4)
    WRAP = Alignment(wrap_text=True, vertical="top")
    L0_FILLS = {"01":"DEEBF7","02":"DEEBF7","03":"DEEBF7","04":"E2EFDA","05":"FFF2CC","06":"FCE4D6","07":"E4DFEC","08":"FCE4D6","09":"D9D9D9","10":"EDEDED"}

    wb = Workbook()

    def header(ws, cols, widths):
        for i,(c,w) in enumerate(zip(cols,widths),1):
            cell = ws.cell(1,i,c); cell.font = HDR_FONT; cell.fill = HDR_FILL; cell.alignment = WRAP; cell.border = THIN
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}1"

    # ---- Sheet 1: Read Me ----
    ws = wb.active; ws.title = "Read Me"
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 4; ws.column_dimensions["B"].width = 120
    rows = [
    ("IBM Apptio Process Catalog - Targetprocess, Costing, Planning, Cloudability", True),
    ("Built 2026-08-18 from TBM Council / FinOps Foundation / SPM framework research, IBM product documentation research, and local demo, RFP and assessment material (incl. the cross-tool E2E BPMN).", False),
    ("", False),
    ("Purpose: a single catalog of the business processes the four IBM Apptio products support and enable, structured to generate L0-L2 BPML/BPMN diagrams and to drive tool configuration.", False),
    ("", False),
    ("How the levels work", True),
    ("L0 = process area (value-chain level). L1 = process. L2 = sub-process/activity - the unit you turn into BPMN tasks or sub-processes.", False),
    ("IDs: L0 'NN', L1 'NN.N', L2 'NN.N.N'. Stable IDs - reference them from diagrams and configuration backlogs.", False),
    ("Delivery Model column: 'Any' = methodology-agnostic; 'Agile' = SAFe/agile-specific (PI planning, Kanban, story points); 'Traditional' = waterfall/stage-gate specific; 'Hybrid' = explicitly about running agile and traditional side by side in one governed model (hybrid portfolio views, dual funding, role- and team-based capacity, multi-approach capitalization).", False),
    ("", False),
    ("How to build BPML diagrams from this workbook", True),
    ("1. L0 diagram: use the 'L0 Map' sheet - one node per L0 area; the arrows are the cross-tool feeds listed on 'E2E Flow Steps'.", False),
    ("2. L1 diagrams: for one L0, lay its L1 processes as sub-processes; lanes come from the 'Personas / Lanes' column.", False),
    ("3. L2/BPMN: each L2 row gives the task set; 'Trigger / Cadence' = start events, 'Key Inputs/Outputs' = data objects, 'Personas' = lanes, cross-tool feeds = message flows. The 'E2E Flow Steps' sheet is already BPMN-ready (element types, lanes, gateways) and mirrors a real reviewed BPMN model.", False),
    ("4. Tool configuration: the 'Configuration Objects' column per L2 plus the 'Tool Config Reference' sheet form the configuration backlog per product.", False),
    ("", False),
    ("Sheets", True),
    ("L0 Map - the ten process areas with tool coverage and framework framing.", False),
    ("Process Catalog L0-L2 - the full catalog (~140 L2 activities).", False),
    ("E2E Flow Steps - BPMN-ready step tables for the six cross-tool flows (UC1-UC4 + cloud-to-TBM + investment loop).", False),
    ("Tool Config Reference - configuration-object checklists per product.", False),
    ("Framework Reference - TBM, FinOps, SPM, SAFe structures and maturity scales used as the catalog's framing.", False),
    ("Sources - research and local source material.", False),
    ("", False),
    ("Known gap: Box-hosted RFP documents (Danske Bank, Florida Blue/GuideWell, AER, Honda transcripts, Amex) were cloud-only placeholders during this build and are not yet folded in. The Desjardins RFP solution deck and local demo/assessment corpus are included.", False),
    ]
    for i,(t,b) in enumerate(rows,2):
        c = ws.cell(i,2,t); c.font = Font(name=FONT, size=14 if i==2 else 10, bold=b); c.alignment = Alignment(wrap_text=True, vertical="top")

    # ---- Sheet 2: L0 Map ----
    ws = wb.create_sheet("L0 Map")
    cols = ["L0 ID","L0 Process Area","Description","Primary Tool","Supporting Tools","Framework Framing","Default BPMN Lanes","# L1","# L2"]
    header(ws, cols, [7,30,60,16,20,50,40,7,7])
    for i,(k,v) in enumerate(sorted(L0.items()),2):
        n_l1 = len({r["l1id"] for r in ALL if r["l0id"]==k}); n_l2 = len([r for r in ALL if r["l0id"]==k])
        vals = [k, v["name"], v["desc"], v["primary"], v.get("supporting",""), v["frameworks"], v["lanes"], n_l1, n_l2]
        for j,val in enumerate(vals,1):
            c = ws.cell(i,j,val); c.font = BASE; c.alignment = WRAP; c.border = THIN
            c.fill = PatternFill("solid", fgColor=L0_FILLS[k])
        ws.cell(i,2).font = BOLD

    # ---- Sheet 3: Process Catalog ----
    ws = wb.create_sheet("Process Catalog L0-L2")
    cols = ["L0 ID","L0 Area","L1 ID","L1 Process","L2 ID","L2 Sub-process / Activity","Description","Delivery Model","Primary Tool","Supporting Tools / Systems","Personas / Lanes","Trigger / Cadence","Key Inputs","Key Outputs","Configuration Objects (tool setup)","Framework Mapping","Source / Evidence"]
    header(ws, cols, [6,22,7,26,8,32,45,11,14,16,26,16,26,26,50,34,30])
    r_i = 2
    for r in ALL:
        vals = [r["l0id"], r["l0"], r["l1id"], r["l1"], r["l2id"], r["l2"], r["desc"], r["delivery"], r["tool"], r["support"], r["personas"], r["cadence"], r["inputs"], r["outputs"], r["config"], r["fw"], r["src"]]
        for j,val in enumerate(vals,1):
            c = ws.cell(r_i,j,val); c.font = BASE; c.alignment = WRAP; c.border = THIN
        ws.cell(r_i,1).fill = PatternFill("solid", fgColor=L0_FILLS[r["l0id"]])
        ws.cell(r_i,6).font = BOLD
        r_i += 1

    # ---- Sheet 4: E2E Flow Steps ----
    ws = wb.create_sheet("E2E Flow Steps")
    cols = ["Flow","Flow Name","Step","BPMN Element Type","Lane","Task / Event Name","Notes"]
    header(ws, cols, [7,34,6,16,30,55,45])
    fills = {"UC3":"DEEBF7","UC2":"E2EFDA","UC1":"FFF2CC","UC4":"FCE4D6","CLD":"E4DFEC","INV":"D9D9D9"}
    for i,row in enumerate(FLOWS,2):
        for j,val in enumerate(row,1):
            c = ws.cell(i,j,val); c.font = BASE; c.alignment = WRAP; c.border = THIN
        ws.cell(i,1).fill = PatternFill("solid", fgColor=fills[row[0]])

    # ---- Sheet 5: Tool Config Reference ----
    ws = wb.create_sheet("Tool Config Reference")
    cols = ["Tool","Config Domain","Configuration Objects","Notes"]
    header(ws, cols, [16,28,70,45])
    CFG = CFG_T
    for i,row in enumerate(CFG,2):
        for j,val in enumerate(row,1):
            c = ws.cell(i,j,val); c.font = BASE; c.alignment = WRAP; c.border = THIN
        ws.cell(i,1).font = BOLD

    # ---- Sheet 6: Framework Reference ----
    ws = wb.create_sheet("Framework Reference")
    cols = ["Framework","Structure / Layers","Disciplines / Capabilities","Maturity & Personas"]
    header(ws, cols, [12,55,70,55])
    for i,(k,v) in enumerate(FRAMEWORKS.items(),2):
        for j,val in enumerate([k, v["layers"], v["disciplines"], v["maturity"]],1):
            c = ws.cell(i,j,val); c.font = BASE; c.alignment = WRAP; c.border = THIN
        ws.cell(i,1).font = BOLD
    # ATUM taxonomy quick reference below
    r0 = len(FRAMEWORKS)+3
    ws.cell(r0,1,"TBM Taxonomy v4 quick reference (ATUM)").font = BOLD
    atum = [
    ("Cost Pools (OpEx)","Internal Labor; External Labor; Outside Services (Consulting, MSP, CSP); Hardware; Software; Facilities & Power; Telecom; Other; Internal Services (+ CapEx pool variants)"),
    ("IT / Resource Towers","Data Center; Compute; Storage; Network; Platform; Output; End User; Application; Delivery; Security & Compliance; IT Management (each with sub-towers)"),
    ("Solutions (6 types)","Delivery; Infrastructure; Platform; Workplace; Business; Shared & Corporate"),
    ("Consumers","Business Units; Business Architecture (capabilities, processes, product lines); Customers & Partners"),
    ]
    for i,(a,b) in enumerate(atum, r0+1):
        ws.cell(i,1,a).font = BOLD; ws.cell(i,1).border = THIN; ws.cell(i,1).alignment = WRAP
        ws.cell(i,2,b).font = BASE; ws.cell(i,2).border = THIN; ws.cell(i,2).alignment = WRAP

    # ---- Sheet 7: Sources ----
    ws = wb.create_sheet("Sources")
    cols = ["Type","Source","What it contributed"]
    header(ws, cols, [18,60,70])
    SRC = [
    ("Local - BPMN","apptio-e2e-flow.bpmn + apptio-e2e-demo-script (MetLife E2E demo)","Anchor artifact: 3 lanes, 4 use cases (UC1-UC4), 20+ tasks/gateways - basis of L0-09 and E2E Flow Steps sheet"),
    ("Local - demo","PI Planning Demo Script","PI readiness assessment + 4-phase preparation process (03.1)"),
    ("Local - demo","LFM - Demo Talking Points","Labor financial management lifecycle: scoring > headcount > targets > allocations > leadership reporting"),
    ("Local - deck","TBMC25 Integration of Apptio Product Suite (IBM Client Zero)","Suite integration map, sync cadences, ATUM product catalog, CIO monthly ops dashboard (08.4), TBM>EBM"),
    ("Local - deck","ApptioOne Overview CFD","Costing/Planning capability depth, IIP, Billing/Benchmarking/EBM, virtuous cycle"),
    ("Local - deck","Apptio TargetProcess WFM (BofA); SPM & EAP CFDs; Solution Overview (Desjardins RFP); SPM Framework; Customer PowerUp","SPM structural model, WFM use cases, demand/capacity activity lists, closed-loop processes, capability maps"),
    ("Local - assessment","SPM Maturity Assessment (+ Metlife instance); TBM Practice Assessment (+ Metlife); FinOps Assessment (Metlife)","Maturity dimensions & scales framing L0/L1 areas and 10.6.4"),
    ("Local - data","Targetprocess Customer Briefs; SPM Personas","Buying personas, real use-case mixes"),
    ("Web - framework","tbmcouncil.org (framework, taxonomy v4); finops.org (framework, FOCUS); Gartner SPM definition; SAFe LPM","Framework layers, capabilities, maturity models"),
    ("Web - product","IBM Docs (Costing Standard, TBM Studio, Datalink, Planning, Targetprocess, Cloudability incl. Savings Automation & Workload Planning); apptio.com product pages; IBM service descriptions","Product modules, configuration objects, edition differences"),
    ("Gap","Box RFPs (Danske Bank, Florida Blue/GuideWell, AER, Honda transcripts, Amex WFM responses)","Not yet ingested - Box cloud placeholders; fold in when available offline"),
    ]
    for i,row in enumerate(SRC,2):
        for j,val in enumerate(row,1):
            c = ws.cell(i,j,val); c.font = BASE; c.alignment = WRAP; c.border = THIN

    if CALENDAR:
        ws = wb.create_sheet("Operating Calendar")
        cols = ["Stream","Process","Cadence"] + ["FM%d"%i for i in range(1,13)] + ["Description","Catalog refs"]
        header(ws, cols, [22,34,15]+[5]*12+[60,22])
        ri = 2
        for st in CALENDAR["streams"]:
            for en in st["entries"]:
                vals = [st["name"], en["name"], en["cadence"]] + [("X" if m in en["fm"] else "") for m in range(1,13)] + [en["desc"], ", ".join(en.get("refs",[]))]
                for j,val in enumerate(vals,1):
                    c = ws.cell(ri,j,val); c.font = BASE; c.alignment = WRAP; c.border = THIN
                ri += 1
    wb.save(os.path.join(ROOT,"dist","Apptio_Process_Catalog_L0-L2.xlsx"))

