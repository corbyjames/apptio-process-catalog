#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off migration to v0.8.0: the labor rate card build.

Adds three L2s at the head of 06.4 "Cost labor & capitalize" that describe how a
company derives its labor rates — by band/level, role family, location and
employment type, from base pay + benefits (employees) or contract rates
(contractors) already loaded in Apptio Costing, with overhead uplift and a
productive-hours divisor — and publishes the approved rate card into the
protected rate tables that 06.4.1 (now 06.4.4) blends from.

The existing 06.4.1–06.4.6 move to 06.4.4–06.4.9; every reference in the catalog
(flow steps, decision `affects`, variants, prose cross-references) and in
data/calendar.yaml is rewritten, and each moved record keeps its old id in
`legacy_id` (the site shows "was 06.4.1"). Permanent element IDs do not change.

Kept for provenance like merge_v05.py / add_decisions_v07.py. Idempotent: a
catalog that already has P-0150 is left alone.
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "catalog.json")
CAL = os.path.join(ROOT, "data", "calendar.yaml")
CAT = json.load(open(P, encoding="utf-8"))
L2 = {l2["id"]: l2 for l0 in CAT["l0s"] for l1 in l0["l1s"] for l2 in l1["l2s"]}
if any(l2["eid"] == "P-0150" for l2 in L2.values()):
    print("already applied"); sys.exit(0)

G = next(g for l0 in CAT["l0s"] for g in l0["l1s"] if g["id"] == "06.4")
OLD = [l2["id"] for l2 in G["l2s"]]                     # 06.4.1 … 06.4.6
SHIFT = 3
MAP = {o: f"06.4.{int(o.split('.')[-1]) + SHIFT}" for o in OLD}

def rewrite(s):
    return re.sub(r"\b06\.4\.(\d)\b", lambda m: MAP.get(m.group(0), m.group(0)), s)
def walk(x):
    if isinstance(x, str): return rewrite(x)
    if isinstance(x, list): return [walk(v) for v in x]
    if isinstance(x, dict): return {k: walk(v) for k, v in x.items()}
    return x

# ---- renumber everything (ids inside records, flow steps, decisions, prose) ----
for l2 in G["l2s"]:
    l2["legacy_id"] = l2["id"]
CAT = walk(CAT)
G = next(g for l0 in CAT["l0s"] for g in l0["l1s"] if g["id"] == "06.4")
for l2 in G["l2s"]:                     # legacy_id was rewritten too; restore the old positional id
    l2["legacy_id"] = {v: k for k, v in MAP.items()}[l2["id"]]

# ---- the new records ----
def rec(id, eid, name, desc, personas, plist, cadence, bucket, inputs, outputs, config, fw, fws, evidence, outcome, decisions=None, variants=None, flows=None):
    r = {"id": id, "legacy_id": None, "name": name, "description": desc, "delivery_model": "Any", "tool": "Costing",
         "personas": personas, "cadence": cadence, "inputs": inputs, "outputs": outputs, "config": config,
         "framework": fw, "evidence": evidence, "eid": eid, "persona_list": plist, "cadence_bucket": bucket,
         "products": ["Costing"], "primary_product": "Costing", "budgeting_method": None, "outcome": outcome,
         "frameworks": fws, "framework_tags": ["TBM"], "completeness": 9, "completeness_of": 9, "flows": flows or ["UC2"]}
    if decisions: r["decisions"] = decisions
    if variants: r["variants"] = variants
    return r

EV = "Added v0.8 (labor rate card build); TBM Council labor cost guidance; ITFM standard-rate practice"
NEW = [
 rec("06.4.1", "P-0150", "Define the labor rate structure",
     "Decide how the company expresses labor rates before any number is computed: the rate dimensions (band/level or job grade, "
     "role family, location or cost-of-labor region, employment type - employee, contractor, MSP/offshore), the rate types "
     "(standard rate used for planning and costing vs actual loaded rate used for true-up), the productive-hours policy "
     "(available hours net of PTO, holidays, training and admin, by country and employment type), the overhead/indirect uplift "
     "policy, and the governance - rate-card owner, refresh cadence, approval path and which rate is allowed to leave Costing. "
     "Three rates coexist and the structure says which is which: the actual loaded rate per person (monthly, never leaves Costing), "
     "the standard rate per cell that finance issues (derived from the cell's roster average or the band midpoint, fixed for the year), "
     "and the blended team rate (FTE-weighted standard rates of the team's members, or the actual team average inside Costing). "
     "The structure also fixes the thin-cell rule (cells under about five people roll up to the parent band or region), whether "
     "overhead is carried in the rate or left in tower allocation (never both), the productive-hours divisor (contracted hours net of "
     "PTO, holidays, training and admin - typically 1,650-1,800 of 2,080), and the mid-year revision triggers (actual drifts beyond "
     "tolerance, e.g. 5%, for two or three consecutive months, or cell headcount moves more than 10-15%). See docs/labor-rates.md.",
     "IT Finance, HR Compensation, TBM Office", ["IT Finance & FP&A", "HR & approvers", "TBM Office & analysts"],
     "Annually at budget; on job-architecture or org change", "Annual / per cycle",
     "HRIS job architecture (bands/levels, role families) and location model; employment categories; HR policy on standard hours, PTO and holidays by country; finance policy on overhead pools, capitalization and variance tolerance; privacy constraints on rate exposure",
     "Rate structure definition (dimensions x rate types: actual, standard, blended), thin-cell roll-up rule, productive-hours policy, overhead uplift policy, variance tolerance and mid-year revision triggers, rate governance (owner, cadence, approval, versioning)",
     "Costing: Job Profile dimensions (band/level, role family, location, employment type), rate table design, productive-hours reference table; ATP CM Rate Transform design",
     "TBM: labor | ITFM | privacy", ["TBM: labor", "ITFM", "privacy"], EV,
     "an agreed rate structure and policies that every later rate follows",
     decisions=["rate-exposure"],
     variants=[
      {"decision": "rate-exposure", "option": "blended-team", "description": "Structure centres on team membership: rate cells are kept inside Costing and exist only to roll up to one blended rate per team/ART; band and location remain internal attributes."},
      {"decision": "rate-exposure", "option": "role-location", "name": "Define the job-profile rate-card structure", "description": "Structure is the published grid itself: band/level x role family x location (x employment type) is the rate card everyone plans and costs with, so cell granularity is set with thin-cell roll-up rules.", "outputs": "Rate-card grid definition with roll-up rules"},
      {"decision": "rate-exposure", "option": "individual", "description": "Structure is person-level loaded cost; bands and locations are reporting attributes, and the governance work is the access model and HR/privacy approval."}]),
 rec("06.4.2", "P-0151", "Compute fully loaded labor rates",
     "Starting from the labor roster already loaded in Costing - salary plus benefits for employees, contract rates for contractors - "
     "attach each person's band/level, role family, location and employment type; aggregate loaded cost to each cell of the rate "
     "structure; apply the overhead/indirect uplift; and divide by the cell's productive hours to produce a standard loaded rate per "
     "hour (or per point or per FTE-month, depending on the effort signal). Produce the actual rate per cell alongside, compare both "
     "to the prior rate card and external benchmarks, and raise exceptions for outliers and thin cells (small n rolls up to the parent "
     "band or region). The arithmetic per cell: loaded annual cost = base pay + variable pay + employer taxes + benefits (or contract "
     "rate x contracted hours); cell loaded cost = roster mean (or band midpoint x (1 + burden %)); fully loaded = x (1 + overhead "
     "uplift %); standard rate = fully loaded / productive hours. Burden is normally a % by country and employment type from the GL, "
     "not per person. Team blended rate = sum(FTE x cell standard rate) / sum(FTE). Example: base 120,000 + 10% variable = 132,000; "
     "burden 28% = 168,960; overhead 12% = 189,235; 1,720 productive hours = 110/hour. Sources: HRIS (person, band, role, location, "
     "employment type, FTE, cost center, dates), payroll/GL (pay and burden), VMS/procurement (contractor rates), finance (overhead "
     "pools), HR policy (hours, PTO, holidays), timekeeping (divisor validation), salary surveys and TBM Council benchmarks.",
     "TBM Analyst, IT Finance", ["TBM Office & analysts", "IT Finance & FP&A"],
     "Annually at budget; refreshed quarterly or on reorganization", "Annual / per cycle",
     "Costing labor roster with loaded cost per person (salary + benefits from payroll/GL) or contract rate (VMS/SOW), HRIS attributes (band/level, role family, location, employment type, FTE, cost center, hire/term dates), burden % by country and employment type, productive-hours table, overhead uplift policy, prior rate card, salary-survey and TBM Council benchmarks",
     "Draft rate card (standard and actual rate per cell, headcount n, variance vs prior card), exception list",
     "Costing: labor roster dataset, Job Profile attributes, productive-hours table (country x employment type), overhead allocation %, rate computation in TBM Studio / ATP CM Rate Transform, draft rate table",
     "TBM: labor | ITFM", ["TBM: labor", "ITFM"], EV,
     "a defensible loaded rate for every band, role, location and employment type",
     decisions=["labor-effort-signal"],
     variants=[
      {"decision": "labor-effort-signal", "option": "timesheet", "description": "Divisor is productive hours: loaded annual cost / available hours net of PTO, holidays, training and admin gives an hourly standard rate per cell.", "outputs": "Hourly standard and actual rate per cell"},
      {"decision": "labor-effort-signal", "option": "story-points", "description": "Cell rates feed team cost; the unit rate that matters is cost per point, derived monthly in 06.4.7 from team cost and points completed, so this step validates the loaded cost per FTE-month per cell rather than an hourly rate.", "outputs": "Loaded cost per FTE-month per cell"},
      {"decision": "labor-effort-signal", "option": "story-count", "description": "As for story points: validate loaded cost per FTE-month per cell; the per-item rate is derived monthly from team cost.", "outputs": "Loaded cost per FTE-month per cell"},
      {"decision": "labor-effort-signal", "option": "work-effort-unit", "description": "Divisor is planned allocation capacity: loaded cost / planned effort units gives a rate per allocation unit per cell.", "outputs": "Rate per work-effort unit per cell"},
      {"decision": "labor-effort-signal", "option": "fixed-capacity", "description": "No divisor: the cell's loaded cost per FTE-month is the rate, since teams are assigned whole to towers or applications.", "outputs": "Loaded cost per FTE-month per cell"}]),
 rec("06.4.3", "P-0152", "Approve, effective-date & publish the rate card",
     "Review the draft rate card and its exceptions with Finance and HR, resolve or document exceptions, obtain approval, set the "
     "effective date and version, and load the approved rates into Costing's protected rate tables - the source that 06.4.4 blends "
     "from and 06.4.5 publishes to Targetprocess. Archive the prior version for audit, record the change log by cell, and notify "
     "planning and portfolio owners of material rate movements and their budget impact. Both Targetprocess and Costing reference the "
     "card by version, so plans built on one version can be compared with actuals without dispute about which rate applied. Standard "
     "rates are issued annually, just after the merit cycle takes effect and before budget entry; mid-year, only the cells that hit a "
     "revision trigger in 06.4.10 are re-issued, effective-dated, never the whole card.",
     "IT Finance, HR Compensation, TBM Office", ["IT Finance & FP&A", "HR & approvers", "TBM Office & analysts"],
     "Annually, plus mid-year change control", "Annual / per cycle",
     "Draft rate card, exception list, Finance/HR approvals, effective-dating rules",
     "Approved, versioned, effective-dated rate card in Costing protected rate tables; rate change log; notification to planning and portfolio owners",
     "Costing: protected rate tables (versioned, effective-dated), approval record, rate change log; downstream: ATP CM Rate Transform picks up the new version",
     "TBM: labor | ITFM | privacy", ["TBM: labor", "ITFM", "privacy"], EV,
     "one approved rate card of record that every costing and plan uses"),
]
# a variant replaces the base description on the page, so keep the base mechanism and add the approach-specific sentence
for r in NEW:
    for v in r.get("variants", []):
        v["description"] = r["description"] + " Under this approach: " + v["description"][0].lower() + v["description"][1:]
RECON = rec("06.4.10", "P-0153", "Reconcile standard vs actual labor cost & trigger rate revisions",
     "Keep the portfolio view (work valued at standard or blended rates in Targetprocess) and the accounting view (actual loaded cost "
     "in Costing and the GL) deliberately different and reconciled, never forced to agree. Each month after the true-up, check the "
     "reconciliation key team x month - the cost spread across a team's completed work must equal the team's actual cost; anything "
     "that does not tie is an unmapped person, missing involvement or stale team mapping, fixed in 04.1.x before close. Then report, "
     "per team and per rate cell, standard cost of work vs actual team cost for the month and year to date, split into rate variance "
     "(standard vs actual rate) and volume variance (planned vs delivered effort). Standard-cost figures never post to the GL. When a "
     "cell's actual drifts beyond tolerance for two or three consecutive months, or its headcount moves more than 10-15%, raise a "
     "mid-year revision request for that cell to 06.4.3. The variance report is also the documentation auditors see when standard "
     "rates are used for planning while capitalization is at actual.",
     "TBM Analyst, IT Finance, Accounting", ["TBM Office & analysts", "IT Finance & FP&A"],
     "Monthly after close; year-to-date at quarter end", "Monthly",
     "Monthly team cost and allocations (06.4.7-06.4.8), standard cost of completed work from Targetprocess (rate card version x effort), rate card of record, variance tolerance and revision triggers (06.4.1)",
     "Team x month tie-out, rate and volume variance report by team and cell, mid-year revision requests, audit trail of standard-vs-actual treatment",
     "Costing / TBM Studio: variance report (standard vs actual by team and cell), tie-out check, exception list; Targetprocess: rate card version on costed allocations",
     "TBM: labor | ITFM | FinOps: variance", ["TBM: labor", "ITFM", "FinOps: variance"], EV,
     "a monthly proof that the portfolio numbers and the books describe the same labor cost", flows=["UC1", "UC2"])
G["l2s"] = NEW + G["l2s"] + [RECON]

# ---- decisions: the new records are shaped by D-02 and D-01 ----
for d in CAT["decisions"]:
    if d["key"] == "rate-exposure" and "06.4.1" not in d["affects"]: d["affects"] = ["06.4.1", "06.4.3"] + d["affects"]
    if d["key"] == "labor-effort-signal" and "06.4.2" not in d["affects"]: d["affects"] = ["06.4.2"] + d["affects"]

# ---- UC2 gains the rate-card build as its first step ----
uc2 = next(f for f in CAT["flows"] if f["id"] == "UC2")
if not any(s["n"] == "10" for s in uc2["steps"]):
    uc2["steps"].insert(0, {"n": "10", "type": "User task", "lane": "Costing / TBM Studio",
        "task": "Build, approve and load the fully loaded rate card (band x role x location x employment type)",
        "note": "Annual, from the Costing labor roster: salary + benefits or contract rate, overhead uplift, productive hours",
        "l2": ["06.4.1", "06.4.2", "06.4.3"]})
    uc2["summary"] = rewrite(uc2["summary"])

uc1 = next(f for f in CAT["flows"] if f["id"] == "UC1")
if not any(s["n"] == "19" for s in uc1["steps"]):
    uc1["steps"].append({"n": "19", "type": "Task", "lane": "Costing / TBM Studio",
        "task": "Tie out team x month; report rate & volume variance (standard vs actual); raise mid-year rate revisions",
        "note": "Portfolio view at standard, books at actual - reconciled, never forced to agree", "l2": ["06.4.10"]})
    uc1["summary"] += " A monthly tie-out and variance report keeps the standard-rate portfolio view reconciled with the actual-cost accounting view."
uc2["summary"] = "Finance builds the standard rate card from the Costing roster (06.4.1-06.4.3); Costing keeps individual rates protected, computes blended team/ART rates and publishes them to Targetprocess so work allocations can be cost without exposing compensation. Monthly variance against actuals (06.4.10) is the true-up that triggers mid-year re-publication."
for d in CAT["decisions"]:
    if d["key"] == "rate-exposure" and "06.4.10" not in d["affects"]: d["affects"].append("06.4.10")

# ---- version & changelog ----
CAT["version"] = "0.8.0"; CAT["built"] = "2026-10-01"
CAT["changelog"].insert(0, {"version": "0.8.0", "date": "2026-10-01", "items": [
    "Labor rate card build: three new processes at the head of 06.4 - 06.4.1 Define the labor rate structure (P-0150), 06.4.2 Compute fully loaded labor rates (P-0151), 06.4.3 Approve, effective-date & publish the rate card (P-0152). They start from the labor roster already loaded in Costing (salary + benefits, or contract rates) and produce the protected rate tables that blending starts from. Rate dimensions: band/level, role family, location, employment type; components: base pay, benefits/burden, overhead uplift, productive hours.",
    "06.4.1-06.4.6 renumbered to 06.4.4-06.4.9 (P-0091-P-0096 unchanged; each record shows its former id). All cross-references, D-01/D-02 scope, UC1/UC2 steps and the operating calendar updated.",
    "UC2 Rates back gains step 10, the annual rate-card build, ahead of blending.",
    "D-02 Rate exposure now also shapes 06.4.1, 06.4.3 and 06.4.10; D-01 Labor effort signal shapes 06.4.2 (the rate divisor).",
    "06.4.10 Reconcile standard vs actual labor cost & trigger rate revisions (P-0153): the monthly team x month tie-out and rate/volume variance report that keeps the standard-rate portfolio view and the actual-cost accounting view in sync and triggers mid-year cell revisions. UC1 gains step 19.",
    "docs/labor-rates.md: method note on the three kinds of rate, the calculation with a worked example, data sources, refresh cadence vs turnover, and the four reconciliation mechanisms."]})

json.dump(CAT, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---- calendar.yaml: renumber refs and add the annual rate-card refresh ----
cal = open(CAL, encoding="utf-8").read()
cal = rewrite(cal)
marker = "  - name: Labor capitalization actuals to ERP\n"
entry = ('  - name: Annual labor rate card refresh\n    cadence: Annual\n    fm: [8, 9]\n'
         '    desc: Define the rate structure, compute fully loaded rates by band, role, location and employment type from the Costing roster, approve and load the protected rate tables ahead of budget.\n'
         '    refs: ["06.4.1", "06.4.2", "06.4.3"]\n')
recon = ('  - name: Labor rate variance & tie-out\n    cadence: Monthly\n    fm: [1,2,3,4,5,6,7,8,9,10,11,12]\n'
         '    desc: Tie out team x month after the true-up; report standard-vs-actual rate and volume variance; raise mid-year rate revisions by cell.\n'
         '    refs: ["06.4.10"]\n')
m2 = "  - name: Showback / Bill of IT publication\n"
if "Labor rate variance & tie-out" not in cal:
    assert cal.count(m2) == 1; cal = cal.replace(m2, recon + m2)
if "Annual labor rate card refresh" not in cal:
    assert cal.count(marker) == 1; cal = cal.replace(marker, entry + marker)
open(CAL, "w", encoding="utf-8").write(cal)
print("v0.8.0: added 06.4.1-06.4.3, renumbered", MAP)
