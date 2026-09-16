#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off migration to v0.7.0: add the design-decision register, L2 variants,
L2 applicability and flow-step conditions to data/catalog.json.

Kept for provenance (like merge_v05.py). Re-running is idempotent: it replaces the
`decisions` block and every `variants` / `applies_when` / `when` it owns.

Concepts (see README "Design decisions and variants"):
  decisions[]            catalog-level register of the choices a customer makes once
                         (e.g. how labor effort is captured). Each has options.
  l2.variants[]          the same L2 done a different way under one option of one
                         decision. Fields given on the variant override the base L2;
                         everything else is inherited. The base L2 stays method-neutral.
  l2.applies_when        {decision_key: [option_ids]} - the whole L2 only exists under
                         those options (e.g. 04.5.2 Approve timesheets).
  flow.steps[].when      {decision_key: [option_ids]} - the step is on the path only
                         under those options; a gateway step may name `decision` so the
                         diamond is labeled from the register.
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "catalog.json")
CAT = json.load(open(P, encoding="utf-8"))
L2 = {l2["id"]: l2 for l0 in CAT["l0s"] for l1 in l0["l1s"] for l2 in l1["l2s"]}
FLOW = {f["id"]: f for f in CAT["flows"]}

# ----------------------------------------------------------------------------- register
DECISIONS = [
 {"id":"D-01","key":"labor-effort-signal","name":"Labor effort signal","domain":"Labor costing & capitalization",
  "question":"How is labor effort captured and attached to work so it can be costed, capitalized and rolled into App TCO?",
  "why":"Drives which Targetprocess entities carry effort, what crosses the ADM feed to Costing, how team cost is spread over work and towers, and what the auditors see behind the CapEx file. Most customers mix approaches by team kind (e.g. story points for product teams, fixed capacity for ops queues), so this decision is normally made per team type.",
  "multi":True,"default":"story-points",
  "options":[
   {"id":"story-points","name":"Cost per story point","summary":"Monthly team cost divided by story points completed gives a cost per point; cost lands on epics, features and applications in proportion to the points delivered against them. Effort is never typed in - it comes from the backlog.",
    "fit":"Agile teams with a visible, well-groomed backlog in Targetprocess or a synced Jira/ADO. The Apptio reference pattern ('deprecates time writing').",
    "prereqs":"Involvements % (04.1.2), job profiles with CapEx/OpEx split (04.1.3), protected rates (06.4.1), completed-work feed to Costing (UC1), a capitalization policy signed off with Finance/audit.",
    "tradeoffs":"Points are only comparable within a team - always normalize per team, never enterprise-wide. Un-estimated or carried-over work distorts the month. Needs backlog hygiene and a documented policy for auditors.",
    "evidence":"E2E BPMN g_vis/t_work; e2e script UC1"},
   {"id":"story-count","name":"Cost per completed work item","summary":"Same mechanism as story points but every completed story/work item weighs the same. Team cost divided by items done.",
    "fit":"Kanban / no-estimates teams, support and enhancement teams whose items are of similar size.",
    "prereqs":"As story points, minus estimation discipline.",
    "tradeoffs":"A one-line fix and a two-week story cost the same; acceptable only where item sizes are homogeneous.",
    "evidence":"Costing labor allocation options (06.4.5 config)"},
   {"id":"timesheet","name":"Timesheets (hours x rate)","summary":"People log hours against work items or projects in the Time entity; managers approve weekly; approved hours x rate is the labor cost attached to work and the basis for CapEx.",
    "fit":"Traditional and hybrid delivery, professional-services and contractor billing, regulated environments that require hours as the capitalization evidence, or where Finance already runs a timesheet regime.",
    "prereqs":"Time Tracking solution + Timesheet approval workflow (04.5.1-04.5.2), rate source (job-profile or blended rate), timesheet compliance reporting.",
    "tradeoffs":"Highest burden and the classic accuracy decay (end-of-week estimates, 'other' buckets). Needs chasing and compliance metrics. Strongest audit trail.",
    "evidence":"TP Time Tracking; 2026.03 Timesheet with Approval Workflow solution sheet"},
   {"id":"work-effort-unit","name":"Planned work-effort units (allocation-based)","summary":"Work Allocations (% or man-days per person/team per period) are treated as the effort signal; no hours are recorded. Cost = allocation x rate, trued up periodically against actual completion.",
    "fit":"Hybrid organizations that plan resourcing carefully but will not run timesheets; project-based funding where the plan is the contract.",
    "prereqs":"Demand & Capacity solution with Work Allocations (04.3.1 / 04.3.4), a true-up rule (quarterly or at project close), blended rates (UC2).",
    "tradeoffs":"Planned is not actual - variance hides until true-up. Weaker capitalization evidence than hours; usually paired with a sign-off step.",
    "evidence":"LFM demo (requested man-days); WFM deck"},
   {"id":"fixed-capacity","name":"Fixed capacity (team to tower/app)","summary":"No work-level attribution at all: the team's monthly cost is allocated to applications or IT towers by a standing rule (team->tower mapping, % splits).",
    "fit":"Run/operations teams without a visible backlog (ServiceNow queues, infrastructure ops, service desk), platform teams charged as shared services.",
    "prereqs":"Team->IT tower / application mapping (04.1.3), allocation strategy in Model Studio (06.1.2).",
    "tradeoffs":"No run-vs-change split from data; capitalization only via a fixed % if policy allows. Simplest to operate.",
    "evidence":"E2E BPMN t_tower; e2e script (ServiceNow example)"}],
  "affects":["04.1.3","04.5.1","04.5.2","04.5.3","06.4.3","06.4.5","06.4.6"],"flows":["UC1"],"related":["rate-exposure","capacity-basis"]},

 {"id":"D-02","key":"rate-exposure","name":"Labor rate exposure","domain":"Labor costing & capitalization",
  "question":"Which labor rate is allowed to leave Costing and be used in Targetprocess to cost work?",
  "why":"Individual compensation is sensitive; the level at which rates are blended sets who can see what, how accurate costed allocations are, and whether a true-up is needed between the rate used in the portfolio and actuals in Costing.",
  "multi":False,"default":"blended-team",
  "options":[
   {"id":"blended-team","name":"Blended team / ART rate","summary":"Costing computes one blended rate per team, ART or solution train from protected individual rates and publishes only that. Portfolio costs work at the team rate.",
    "fit":"Most enterprises; the Apptio reference pattern.","prereqs":"Team structure with involvements (04.1.2), ATP CM Rate Transform (06.4.1), ADM rate feed (06.4.2).",
    "tradeoffs":"Costed allocations drift from actuals when team mix changes - define a true-up (monthly or quarterly).","evidence":"E2E BPMN t_rates/t_send4; e2e script UC2"},
   {"id":"role-location","name":"Job-profile rate (role x location)","summary":"Standard rate card per job profile (role x location, optionally employment type) published to Targetprocess; individuals inherit their profile's rate.",
    "fit":"Organizations with a mature rate card, project-based estimating, PS/contractor mixes, or where teams are too fluid to blend.","prereqs":"Job Profile entities with rate linkage (04.1.3), rate card governance (annual refresh).",
    "tradeoffs":"More granular than a team rate and still non-identifying, but a rate card needs owning and refreshing.","evidence":"E2E BPMN t_data; Planning labor rate cards (05.7.2)"},
   {"id":"individual","name":"Individual (actual) rates","summary":"Actual loaded cost per person leaves Costing and is used to cost allocations and time.",
    "fit":"Small IT organizations, PS firms, or where Finance already exposes comp to project accounting.","prereqs":"Restricted-access roles in Targetprocess, HR/works-council approval, field-level permissions.",
    "tradeoffs":"Most accurate, but exposes compensation in a delivery tool; usually blocked by HR/privacy. Not the default.","evidence":"06.4.1 rate-exposure design decision"}],
  "affects":["04.1.3","06.4.1","06.4.2","04.3.1","02.4.3"],"flows":["UC2"],"related":["labor-effort-signal"]},

 {"id":"D-03","key":"budget-build-method","name":"Budget build method","domain":"IT financial planning",
  "question":"How is the IT budget built for a given decision unit and cycle?",
  "why":"Sets whether 05.1 or 05.8 is the path for a cost center, tower, service or application, how the baseline is seeded, and whether the ZBB flow runs. Selectable per decision unit and per cycle - a rotation is the normal pattern.",
  "multi":True,"default":"driver-based",
  "options":[
   {"id":"incremental","name":"Incremental","summary":"Prior-year budget or actuals seeded as the baseline, adjusted line by line for known changes.","fit":"Stable run units between ZBB rotations; low-effort cycles.","prereqs":"Prior plan / actuals import (05.1.1).","tradeoffs":"Carries last year's inefficiencies forward; weakest challenge of the run base.","evidence":"Planning docs (Adjust Baseline Values)"},
   {"id":"driver-based","name":"Driver-based","summary":"Lines are built from drivers (headcount, contracts, assets, volumes) with rates; the baseline is regenerated from drivers rather than copied.","fit":"The default for most units; pairs with rolling forecasting (05.2).","prereqs":"Driver data (positions, contracts, asset register), driver-based line items in Planning.","tradeoffs":"Needs clean driver feeds; still anchored on current activity levels.","evidence":"Planning docs; Apptio rolling-forecast method"},
   {"id":"zbb-rotational","name":"Zero-based - rotational","summary":"A subset of decision units is rebuilt from a zero base each cycle (each unit every 2-3 years); the rest run driver-based. Decision packages at Minimum / Current / Enhanced tiers, ranked to a cut-line.","fit":"Organizations that want the challenge of ZBB without the annual burden. The catalog's primary ZBB variant.","prereqs":"Group 05.8, cost-category owners, TBM fact base (06.x), rotation calendar (10.6.1).","tradeoffs":"Two budgeting paths in one cycle; needs the merge step 05.8.5.","evidence":"Gartner; McKinsey; Apptio ZBB blog"},
   {"id":"zbb-full","name":"Zero-based - all units annually","summary":"Classic ZBB: every decision unit justified from zero every year.","fit":"Turnaround / cost-out programs with executive mandate.","prereqs":"As rotational, at full scale; FP&A facilitation capacity.","tradeoffs":"The historical failure mode (burden, sandbagging); rarely sustained beyond 2-3 cycles.","evidence":"Pyhrr; Kraft Heinz / federal cases"},
   {"id":"zbx","name":"Zero-based mindset (continuous)","summary":"No annual ZBB event; cost-category owners run a continuous zero-based review inside the monthly rhythm (05.8.6 as an operating cadence).","fit":"Organizations past their first ZBB cycles that want to keep the discipline without the event.","prereqs":"Monthly variance with package-level thresholds (05.3.2 / 06.2.2), owner community.","tradeoffs":"Depends on culture and incentives; without the event the challenge can fade.","evidence":"Accenture ZBx; FinOps Budgeting (Run maturity)"}],
  "affects":["05.1.1","05.1.3","05.1.4","05.1.5","05.8.1","05.8.2","05.8.3","05.8.4","05.8.5","05.8.6","07.6.1"],"flows":["ZBB"],"related":["funding-model"]},

 {"id":"D-04","key":"funding-model","name":"Portfolio funding model","domain":"Demand & portfolio investment",
  "question":"Is change work funded per project, per value stream/product, or both during a transition?",
  "why":"Decides the shape of the Budgeting solution in Targetprocess, whether budgets attach to Projects or to Portfolios/ARTs, what the investment loop with Planning carries, and how top-down targets are applied.",
  "multi":False,"default":"hybrid",
  "options":[
   {"id":"project-based","name":"Project-based funding","summary":"Money is approved per project/initiative with a business case and a defined scope; actuals are tracked per project.","fit":"Traditional and regulated PMOs, capital-project cultures, organizations early on the SPM journey.","prereqs":"Project entities with budgets, stage-gate governance (D-05), investment tags in Planning (05.7.1).","tradeoffs":"Re-planning is slow; funding follows projects rather than capacity; encourages large batches.","evidence":"EAP CFD (annual -> continuous); TP Budgeting"},
   {"id":"value-stream","name":"Value-stream / product funding (Lean Budgets)","summary":"Capacity is funded per value stream, ART or product with guardrails; epics are approved inside the envelope, not funded individually.","fit":"SAFe / LPM organizations, product operating models.","prereqs":"Value streams as Portfolios/Groups (03.4.1), Lean Budget guardrails (02.4.1), participatory budgeting forums.","tradeoffs":"Finance must accept capacity-based accounting; capitalization moves to the labor model (D-01).","evidence":"SAFe Lean Budgets; TP Budgeting solution"},
   {"id":"hybrid","name":"Hybrid (both, side by side)","summary":"Project-based and value-stream funding coexist - typically during a multi-year transition or where some domains stay project-shaped.","fit":"Most large enterprises today.","prereqs":"Common categorization (BAU vs change, CapEx/OpEx) across both (02.3.4), Hybrid Portfolio Management solution.","tradeoffs":"Two governance paths to keep consistent; reporting must reconcile both.","evidence":"WFM deck (hybrid programs); Customer PowerUp"}],
  "affects":["02.4.1","02.4.2","02.2.3","05.7.1","05.7.2","05.7.3"],"flows":["INV","UC3"],"related":["investment-governance","budget-build-method"]},

 {"id":"D-05","key":"investment-governance","name":"Investment approval governance","domain":"Demand & portfolio investment",
  "question":"How does an investment get approved - phase gates, lean portfolio flow, or both?",
  "why":"Shapes entity workflows and per-state permissions in Targetprocess, which forums decide, and whether Portfolio Kanban states or gate reviews are the control points.",
  "multi":False,"default":"hybrid",
  "options":[
   {"id":"stage-gate","name":"Stage-gate","summary":"Initiatives pass formal gates (concept, business case, design, build, deploy) with documented approvals and criteria at each.","fit":"Traditional PMOs, regulated change, capital projects.","prereqs":"Entity states as gates with role permissions, milestone entities, gate evidence fields (03.3.3).","tradeoffs":"Predictable control, slow flow; encourages big up-front business cases.","evidence":"Traditional PM solution; stage-gate research"},
   {"id":"lean-lpm","name":"Lean portfolio flow (Portfolio Kanban)","summary":"Epics move Funnel > Reviewing > Analyzing > Backlog > Implementing with WIP limits; approval is the move to Backlog within the value-stream guardrails.","fit":"SAFe / LPM organizations with value-stream funding.","prereqs":"Portfolio Epic workflow, WSJF or scoring (D-06), Lean Budgets (D-04).","tradeoffs":"Needs trust in guardrails; auditors may want an explicit approval artifact.","evidence":"SAFe LPM; TP entity workflows (02.1.3)"},
   {"id":"hybrid","name":"Hybrid","summary":"Gates for large/regulated initiatives, lean flow for value-stream work - one governed portfolio view over both.","fit":"Enterprises running agile and traditional delivery together.","prereqs":"Hybrid Portfolio Management solution, common categorization (02.3.4).","tradeoffs":"Clear rules needed for which path an item takes.","evidence":"WFM deck; Customer PowerUp (hybrid)"}],
  "affects":["02.1.3","02.2.3","03.3.3"],"flows":["INV"],"related":["funding-model","prioritization-method"]},

 {"id":"D-06","key":"prioritization-method","name":"Prioritization method","domain":"Demand & portfolio investment",
  "question":"How is the portfolio backlog ranked?",
  "why":"Determines which custom and calculated fields exist on epics, what the ranking views show and how ZBB packages are ranked when 05.8 runs.",
  "multi":False,"default":"wsjf",
  "options":[
   {"id":"wsjf","name":"WSJF","summary":"Cost of delay (business value + time criticality + risk reduction/opportunity enablement) divided by job size, as a calculated field.","fit":"SAFe organizations; fast, relative ranking.","prereqs":"Numeric custom fields BV/TC/RR-OE/size, calculated field or metric, prioritized list views (02.2.2).","tradeoffs":"Relative, gameable, weak for compliance/mandatory work.","evidence":"SAFe WSJF; TP calculated fields"},
   {"id":"weighted-scoring","name":"Weighted objective scoring","summary":"Configurable criteria (strategic alignment, value, risk, cost, compliance) with weights; a score per item; often per portfolio.","fit":"Hybrid and traditional portfolios; organizations that must show a defensible model to a board.","prereqs":"Scoring custom fields, Portfolio Epic Score report, objective-scoring configuration.","tradeoffs":"Weights need governance; can become a spreadsheet exercise.","evidence":"WFM deck prioritization; TP Portfolio Epic Score"},
   {"id":"manual","name":"Manual / forum ranking","summary":"A governance forum ranks items by hand (drag-order or rank field) informed by business cases.","fit":"Small portfolios, early maturity.","prereqs":"Rank/order field, prioritized list views.","tradeoffs":"Opaque; depends on who is in the room.","evidence":"SPM maturity model (Foundational)"}],
  "affects":["02.2.2","05.8.4"],"flows":[],"related":["investment-governance"]},

 {"id":"D-07","key":"capacity-basis","name":"Capacity planning basis","domain":"Workforce & resource management",
  "question":"Is capacity planned and allocated per team, per role/named individual, or both?",
  "why":"Decides whether Work Allocations attach to teams or people, how demand is expressed (team % vs role man-days) and which capacity views and reports are configured.",
  "multi":False,"default":"both",
  "options":[
   {"id":"team-based","name":"Team-based","summary":"Long-lived teams are the unit of capacity; work is allocated to teams and ARTs by % or PI capacity.","fit":"Agile at scale; value-stream funding.","prereqs":"Team entities with involvements (04.1.2), team allocation views.","tradeoffs":"Named-resource requests (specialists) have no home.","evidence":"E2E BPMN t_alloc; SAFe capacity"},
   {"id":"role-individual","name":"Role / individual-based","summary":"Demand is expressed as roles and man-days; named individuals are assigned to projects with availability checks.","fit":"Project-based PMOs, PS organizations, shared specialist pools.","prereqs":"Role-based demand requests, Work Allocations at person level, availability / vacation integration (04.3.4).","tradeoffs":"Heavier to maintain; utilization chasing.","evidence":"LFM demo (requested man-days)"},
   {"id":"both","name":"Both (one capacity model)","summary":"Team-based for agile work and role/individual-based for project work in the same capacity model.","fit":"Hybrid organizations - the common case.","prereqs":"Both configurations plus a rule for which work type uses which.","tradeoffs":"Double-counting risk where a person is both in a team and on a project - involvements must sum to 100%.","evidence":"WFM deck; 04.2.1 / 04.3.4"}],
  "affects":["04.2.1","04.2.2","04.3.1","04.3.4","05.7.2"],"flows":["UC3"],"related":["labor-effort-signal"]},

 {"id":"D-08","key":"demand-intake-channel","name":"Demand intake channel","domain":"Demand & portfolio investment",
  "question":"Where do ideas and requests enter - the Targetprocess Service Desk, a ServiceNow front end, or email/forms?",
  "why":"Sets which portal is configured, whether an integration is needed, and where triage happens.",
  "multi":True,"default":"tp-service-desk",
  "options":[
   {"id":"tp-service-desk","name":"Targetprocess Service Desk portal","summary":"Requesters use the built-in portal; Request entities and request types with voting.","fit":"Organizations standardizing on Targetprocess for intake.","prereqs":"Service Desk portal, Request entity + types, automation rules for routing (02.1.1-02.1.2).","tradeoffs":"Another portal for business users if ServiceNow already exists.","evidence":"TP guide Service Desk"},
   {"id":"servicenow","name":"ServiceNow ideation / demand front end","summary":"Ideas are raised in ServiceNow; an integration creates Requests/epics in Targetprocess for qualification.","fit":"ServiceNow-centric enterprises.","prereqs":"ServiceNow integration (10.1.5), field mapping, status sync.","tradeoffs":"Two systems of record for the early lifecycle; sync rules matter.","evidence":"WFM deck (ServiceNow ideation front-end)"},
   {"id":"email-forms","name":"Email / forms","summary":"Requests arrive by email or a form and are created by automation or a triage team.","fit":"Small volumes, interim state.","prereqs":"Email integration, automation rules.","tradeoffs":"Low structure; manual triage.","evidence":"TP email integration"}],
  "affects":["02.1.1","02.1.2","10.1.5"],"flows":[],"related":[]},

 {"id":"D-09","key":"cloud-commitment-mode","name":"Cloud commitment management mode","domain":"Cloud financial management",
  "question":"Are reserved-instance / savings-plan / CUD commitments managed by hand, assisted by recommendations, or automated?",
  "why":"Decides whether 07.5.3 or 07.5.4 is the operating process, what guardrails and roles are configured, and how Finance approves commitments.",
  "multi":False,"default":"assisted",
  "options":[
   {"id":"manual","name":"Manual (vendor consoles)","summary":"Commitments are bought in the cloud vendor consoles on a periodic review; Cloudability reports coverage.","fit":"Small cloud spend; early FinOps maturity (Crawl).","prereqs":"Commitment Overview reports.","tradeoffs":"Under-coverage and expiry misses are common.","evidence":"FinOps Framework Rate Optimization (Crawl)"},
   {"id":"assisted","name":"Assisted (recommendations + approval)","summary":"Cloudability generates purchase/exchange recommendations; FinOps and Finance approve and execute.","fit":"Most organizations (Walk).","prereqs":"Commitment Recommendations, approval forum, procurement alignment (07.5.3).","tradeoffs":"Human latency; coverage typically 70-85%.","evidence":"IBM Docs commitments"},
   {"id":"automated","name":"Automated (Savings Automation)","summary":"Commitment portfolio managed on autopilot within per-account / per-region guardrails; savings-share billing.","fit":"Large, steady AWS/Azure estates (Run).","prereqs":"RateOptimizationFullAccess role, guardrail configuration (07.5.4 / 10.4.2), Finance sign-off on savings-share.","tradeoffs":"Governance shifts to guardrails; commercial model to accept.","evidence":"IBM Docs Savings Automation"}],
  "affects":["07.5.3","07.5.4","10.4.2"],"flows":[],"related":[]},

 {"id":"D-10","key":"cost-recovery-model","name":"IT cost recovery model","domain":"Consumption & chargeback",
  "question":"Does IT show costs back, charge them back at allocated cost, or charge priced services with over/under recovery?",
  "why":"Sets whether the Billing product is needed, whether a price list and O/U recovery process exist, and how BU conversations are framed.",
  "multi":False,"default":"showback",
  "options":[
   {"id":"showback","name":"Showback","summary":"BUs receive a Bill of IT for information; no journal entries.","fit":"First years of TBM; where BU budgets do not carry IT cost.","prereqs":"BU allocation (08.1.1), Bill of IT reports (08.1.2).","tradeoffs":"Influences behavior less than real charges.","evidence":"TBM assessment (showback at service level)"},
   {"id":"chargeback-cost","name":"Chargeback at allocated cost","summary":"Allocated cost is journaled to BU cost centers each period; full recovery by construction.","fit":"Organizations with BU P&L accountability.","prereqs":"Billing product or GL journal export, agreed drivers, dispute process.","tradeoffs":"Charges fluctuate with allocation changes; BUs contest drivers.","evidence":"Apptio Billing"},
   {"id":"chargeback-priced","name":"Chargeback at service prices","summary":"Services are priced (unit rates from 06.3.4); BUs are charged consumption x price; IT manages over/under recovery.","fit":"Mature TBM with a service catalog; shared-service models.","prereqs":"Service unit costs, pricing strategy and what-if modeling, O/U recovery management (08.1.3).","tradeoffs":"Pricing governance and recovery variance to manage; strongest demand shaping.","evidence":"Apptio Billing (pricing, O/U recovery)"}],
  "affects":["07.2.3","08.1.1","08.1.2","08.1.3","08.2.1"],"flows":["UC4","CLD"],"related":[]},

 {"id":"D-11","key":"team-of-record","name":"Team tool of record","domain":"Agile program & delivery",
  "question":"Do teams work in Targetprocess natively, or in Jira / Azure DevOps synced into Targetprocess as the aggregation layer?",
  "why":"Decides which connectors exist, where iteration planning happens and what completed-work data is available for the labor model.",
  "multi":True,"default":"synced",
  "options":[
   {"id":"native","name":"Targetprocess native","summary":"Teams plan iterations and execute stories in Targetprocess boards.","fit":"Greenfield or consolidating tool estates.","prereqs":"Team boards, story/bug/task workflows (03.2.1).","tradeoffs":"Migration of team habits and history.","evidence":"TP entity model"},
   {"id":"synced","name":"Jira / ADO synced","summary":"Teams stay in Jira or Azure DevOps; native bi-directional connectors keep Targetprocess as the aggregation layer for portfolio and finance.","fit":"Most enterprises with established engineering tooling.","prereqs":"Native connectors, area/iteration path mapping, hierarchy rules (03.2.4).","tradeoffs":"Mapping governance; do not import story-level detail into cost systems.","evidence":"TP integrations; e2e script anti-pattern"}],
  "affects":["03.2.1","03.2.4","02.3.4"],"flows":["UC1"],"related":["labor-effort-signal"]},
]

# ----------------------------------------------------------------------------- L2 variants
# {l2_id: [ {decision, option, <overrides>} ]}
V = {
 "04.5.1": [
  {"decision":"labor-effort-signal","option":"story-points","name":"Use completed work as the effort signal","description":"No time is recorded. The completed stories/features on the team backlog are the effort signal; involvements and rates supply the cost. Estimate vs remaining stays on the work item for planning only.","config":"No Time entity for these teams; backlog hygiene rules (every story estimated, closed in-period); Jira/ADO sync of story points","inputs":"Completed work items with story points","outputs":"Completed-work data per team per month","bpmn_type":"Service task"},
  {"decision":"labor-effort-signal","option":"story-count","name":"Use completed items as the effort signal","description":"As story points, but the count of completed work items is the signal - no estimation required.","config":"No Time entity; closed-item rules per period","inputs":"Completed work items","outputs":"Item counts per team per month","bpmn_type":"Service task"},
  {"decision":"labor-effort-signal","option":"timesheet","name":"Record hours on timesheets","description":"Team members log hours against work items or projects daily/weekly in the Time entity; billable flags and estimate vs actual vs remaining are captured for each entry.","config":"Time entity, Time Tracking solution, timesheet views, billable/non-billable fields, reminders/compliance report","inputs":"Work items, projects, calendar","outputs":"Time entries pending approval"},
  {"decision":"labor-effort-signal","option":"work-effort-unit","name":"Maintain work allocations as the effort record","description":"Planned Work Allocations (% or man-days per person/team per period) stand in for recorded effort; owners confirm or adjust them at period end instead of logging hours.","config":"Work Allocation entities (%, hours, man-days), period-end confirmation view, true-up rule","inputs":"Work allocations, availability","outputs":"Confirmed allocation-based effort per period"},
  {"decision":"labor-effort-signal","option":"fixed-capacity","name":"No effort capture (fixed capacity)","description":"Nothing is recorded at work level; the team's cost is attributed by a standing team->tower/app rule downstream (06.4.5).","config":"None in Targetprocess beyond team membership","inputs":"Team roster","outputs":"—","bpmn_type":"Task"}],
 "04.5.2": [
  {"decision":"labor-effort-signal","option":"timesheet","description":"Managers review and approve weekly timesheets under governance rules; unapproved time is chased before the month closes."}],
 "04.5.3": [
  {"decision":"labor-effort-signal","option":"story-points","name":"Feed completed work to Costing","description":"Send completed work (story points by epic/feature/app) with involvements and job profiles to Costing over ADM; time writing is deprecated for these teams.","config":"ADM feed ATP->TBM Studio: completed-work dataset (points, weightage) + workforce data","inputs":"Completed work, involvements, profiles","outputs":"Work-attached effort data for costing & CapEx","bpmn_type":"Send task (ADM)"},
  {"decision":"labor-effort-signal","option":"story-count","name":"Feed completed item counts to Costing","description":"Send completed-item counts by epic/feature/app with workforce data to Costing over ADM.","config":"ADM feed ATP->TBM Studio: completed-work dataset (counts) + workforce data","inputs":"Completed items, involvements, profiles","outputs":"Work-attached effort data for costing & CapEx","bpmn_type":"Send task (ADM)"},
  {"decision":"labor-effort-signal","option":"timesheet","name":"Feed approved hours to Costing","description":"Export approved hours by person x work item/project x period to Costing (and to billing where hours are invoiced).","config":"Time reports/exports, ADM feed of approved Time entries, billing extract","inputs":"Approved time","outputs":"Hours-based effort data for costing, CapEx & billing","bpmn_type":"Send task (ADM)"},
  {"decision":"labor-effort-signal","option":"work-effort-unit","name":"Feed confirmed allocations to Costing","description":"Send confirmed Work Allocations (planned effort, trued up) by person/team x work x period to Costing.","config":"ADM feed of Work Allocation records per period; true-up flag","inputs":"Confirmed allocations","outputs":"Allocation-based effort data for costing & CapEx","bpmn_type":"Send task (ADM)"},
  {"decision":"labor-effort-signal","option":"fixed-capacity","name":"Feed team roster & tower mapping to Costing","description":"Only the team roster, involvements and team->tower/app mapping cross; there is no work-level effort record.","config":"ADM feed of teams, involvements and tower mapping","inputs":"Roster, mappings","outputs":"Capacity-rule inputs for costing","bpmn_type":"Send task (ADM)"}],
 "06.4.3": [
  {"decision":"labor-effort-signal","option":"story-points","description":"Receive involvements, job profiles, CapEx/OpEx and tower mappings plus completed work with story points per epic/feature/app from Targetprocess."},
  {"decision":"labor-effort-signal","option":"story-count","description":"Receive involvements, job profiles, CapEx/OpEx and tower mappings plus completed-item counts per epic/feature/app from Targetprocess."},
  {"decision":"labor-effort-signal","option":"timesheet","description":"Receive involvements, job profiles and mappings plus approved hours by person x work item/project x period from Targetprocess (or the timesheet system of record).","config":"ADM feed ATP->TBM Studio; approved-hours dataset; contractor/PS hours normalization"},
  {"decision":"labor-effort-signal","option":"work-effort-unit","description":"Receive involvements, job profiles and mappings plus confirmed Work Allocations per period from Targetprocess.","config":"ADM feed ATP->TBM Studio; allocation dataset with true-up flag"},
  {"decision":"labor-effort-signal","option":"fixed-capacity","description":"Receive the team roster, involvements and team->tower/app mapping only.","config":"ADM feed ATP->TBM Studio; team/tower mapping dataset"}],
 "06.4.5": [
  {"decision":"labor-effort-signal","option":"story-points","name":"Allocate team cost by story points","description":"Divide each team's monthly cost by the story points it completed to get a cost per point; allocate cost to epics, features and applications in proportion to points delivered (optionally weighted by item type). Points are normalized per team only.","config":"Story-point/weightage allocation strategy in TBM Studio, per-team normalization, weightage table by work-item type, carry-over rule","inputs":"Team costs, completed work with points","outputs":"Work-attached labor cost (per epic/feature/app)","evidence":"E2E BPMN g_vis/t_work; e2e script UC1"},
  {"decision":"labor-effort-signal","option":"story-count","name":"Allocate team cost by completed items","description":"Divide each team's monthly cost by completed work items and allocate evenly per item to the epics/features/apps they belong to.","config":"Item-count allocation strategy, per-team normalization","inputs":"Team costs, completed item counts","outputs":"Work-attached labor cost (per epic/feature/app)"},
  {"decision":"labor-effort-signal","option":"timesheet","name":"Allocate labor cost by approved hours","description":"Approved hours x rate (blended, job-profile or individual per D-02) attach labor cost directly to the work items/projects and applications the hours were logged against; unlogged hours are absorbed by a policy rule.","config":"Hours-based allocation strategy (hours x rate), unlogged-hours absorption rule, billable/non-billable handling","inputs":"Approved hours, rates","outputs":"Work-attached labor cost (per project/app)","evidence":"TP Time Tracking; Costing labor allocation options"},
  {"decision":"labor-effort-signal","option":"work-effort-unit","name":"Allocate labor cost by confirmed allocations","description":"Confirmed Work Allocation % or man-days x rate attach labor cost to the work and applications planned, with a periodic true-up against completion.","config":"Allocation-based strategy (allocation x rate), true-up adjustment period","inputs":"Confirmed allocations, rates","outputs":"Work-attached labor cost (planned, trued up)"},
  {"decision":"labor-effort-signal","option":"fixed-capacity","name":"Allocate team cost to towers/apps by fixed capacity","description":"Allocate the team's cost to IT towers and applications by the standing team->tower/app mapping (percent splits); no work-level attribution.","config":"Fixed-capacity rules (team->app/tower), percent allocation strategy in Model Studio","inputs":"Team costs, capacity rules","outputs":"Tower-/app-attached labor cost","evidence":"E2E BPMN t_tower; e2e script (ServiceNow)"}],
 "06.4.6": [
  {"decision":"labor-effort-signal","option":"story-points","description":"Produce the monthly SAP-ready file of actuals split CapEx/OpEx by user from the work-attached costs and job-profile CapEx %; document the story-point policy so the file stands up to audit without timesheets."},
  {"decision":"labor-effort-signal","option":"timesheet","description":"Produce the monthly SAP-ready file of actuals split CapEx/OpEx by user from approved hours x rate; hours are the audit evidence, so retain approved timesheets with the extract.","config":"SAP-ready extract format, approved-hours retention, contractor/PS normalization against invoices"},
  {"decision":"labor-effort-signal","option":"work-effort-unit","description":"Produce the monthly SAP-ready file from confirmed allocations x rate; add the period-end confirmation as the audit evidence and post true-up adjustments when they occur."},
  {"decision":"labor-effort-signal","option":"fixed-capacity","description":"Capitalization for fixed-capacity teams is by policy percentage (or none); the extract carries the OpEx tower allocation."}],
 "04.1.3": [
  {"decision":"rate-exposure","option":"blended-team","description":"Keep job profiles (role x location) mapped to CapEx/OpEx splits and teams mapped to IT towers; rates stay in Costing and only blended team rates come back (UC2)."},
  {"decision":"rate-exposure","option":"role-location","description":"Keep job profiles (role x location) with a rate-card rate attached, CapEx/OpEx splits and team->tower mappings; the rate card is the published rate source.","config":"Job Profile entities with rate field (rate card), CapEx/OpEx split per profile, team->IT Tower mapping, annual rate-card refresh"}],
 "06.4.1": [
  {"decision":"rate-exposure","option":"blended-team","description":"Keep individual rates protected inside Costing; compute one blended rate per team/ART/solution train from involvements and loaded cost."},
  {"decision":"rate-exposure","option":"role-location","name":"Maintain protected rates & the job-profile rate card","description":"Keep individual rates protected; derive and govern a standard rate per job profile (role x location) as the rate card that is published.","config":"Protected rate tables, job-profile rate derivation, rate-card version control","outputs":"Job-profile rate card"},
  {"decision":"rate-exposure","option":"individual","name":"Maintain individual rates for publication","description":"Individual loaded rates are maintained and permitted to leave Costing under restricted access.","config":"Rate tables, HR/privacy approval record, restricted-access role mapping","outputs":"Individual rates (restricted)"}],
 "06.4.2": [
  {"decision":"rate-exposure","option":"blended-team","description":"Send blended team/ART rates to Targetprocess on cadence; define the true-up pattern for blended-vs-actual reconciliation."},
  {"decision":"rate-exposure","option":"role-location","description":"Send the job-profile rate card to Targetprocess on cadence (typically annual + on change); profiles inherit rates.","config":"ADM rate-card feed, job-profile key mapping, refresh cadence","outputs":"Rate card available in ATP"},
  {"decision":"rate-exposure","option":"individual","description":"Send individual rates to Targetprocess under field-level restricted access.","config":"ADM rate feed with restricted-access target fields","outputs":"Individual rates in ATP (restricted)"}],
 "05.1.1": [
  {"decision":"budget-build-method","option":"incremental","description":"Create the plan, fiscal calendar and hierarchy; seed the baseline from the prior plan or actuals and adjust by line.","config":"Plan creation, plan folders, working calendar, Adjust Baseline Values (prior plan/actuals), cost center/account hierarchies"},
  {"decision":"budget-build-method","option":"driver-based","description":"Create the plan, fiscal calendar and hierarchy; regenerate the baseline from drivers (positions, contracts, assets, volumes) rather than copying prior-year values.","config":"Plan creation, working calendar, driver-based line items, driver data imports (positions from ATP, contracts, asset register)"},
  {"decision":"budget-build-method","option":"zbb-rotational","description":"Create the plan and calendar; seed in-scope decision units at zero or driver-only (05.8) and the rest from drivers.","config":"Plan creation, ZBB plan/folder per cycle, Adjust Baseline Values = zero/driver-only for in-scope units, 'ZBB Rotation Year' attribute"},
  {"decision":"budget-build-method","option":"zbb-full","description":"Create the plan and calendar; seed every decision unit at zero or driver-only.","config":"Plan creation, Adjust Baseline Values = zero/driver-only for all units"}],
 "05.1.3": [
  {"decision":"budget-build-method","option":"incremental","description":"Budget owners adjust seeded OpEx/CapEx line items per cost center against the prior-year baseline, with justification for changes."},
  {"decision":"budget-build-method","option":"driver-based","description":"Budget owners build OpEx/CapEx lines from drivers and rates per cost center in resource-based views (labor from positions, contracts from the register, assets from the refresh plan)."},
  {"decision":"budget-build-method","option":"zbb-rotational","description":"For in-scope units budget owners build decision packages at tiered service levels (05.8.3) instead of line-item entry; other units enter driver-based lines here."},
  {"decision":"budget-build-method","option":"zbb-full","description":"All units build decision packages at tiered service levels (05.8.3); line-item entry is replaced."}],
 "05.8.1": [
  {"decision":"budget-build-method","option":"zbb-rotational","description":"Select this cycle's rotation slice of decision units (each every 2-3 years, plus units under cost pressure or misaligned with strategy); define the zero base; name cost-category owners paired with budget owners; publish calendar and training."},
  {"decision":"budget-build-method","option":"zbb-full","description":"All decision units are in scope; define the zero base per unit; name cost-category owners paired with budget owners; publish calendar and training. Plan FP&A facilitation capacity for full scale."},
  {"decision":"budget-build-method","option":"zbx","description":"No cycle scoping: maintain the standing decision-unit register and owner matrix; the zero-based challenge runs continuously in 05.8.6."}],
 "05.8.6": [
  {"decision":"budget-build-method","option":"zbb-rotational","description":"Cost-category owners review actuals against package commitments monthly, track savings realization, block silent re-allocation of freed spend, and feed learnings into the next rotation slice."},
  {"decision":"budget-build-method","option":"zbx","name":"Run the continuous zero-based review","description":"Cost-category owners run a standing zero-based review of their categories inside the monthly rhythm - challenging run spend, re-basing where drivers change - without an annual ZBB event.","cadence":"Monthly (standing)","config":"Package-level variance thresholds, category review agenda in the CIO monthly ops review (08.2.3), savings tracker"}],
 "02.4.1": [
  {"decision":"funding-model","option":"project-based","name":"Define project-based funding","description":"Budgets are approved and tracked per project/initiative with annual planning periods; investment tags carry the project into Planning.","config":"Budgeting solution (project budgets, annual periods), project entities, investment tags (05.7.1)"},
  {"decision":"funding-model","option":"value-stream","name":"Define value-stream funding","description":"Fund value streams/ARTs as capacity envelopes with guardrails by horizon and initiative size; epics are approved inside envelopes. Where IT Finance runs ZBB (05.8) the envelope is the change budget that receives freed run spend.","config":"Budgeting solution (value-stream funding, custom periods), Portfolio/Group structure as value streams, Lean Budget guardrails"},
  {"decision":"funding-model","option":"hybrid","description":"Run project-based and value-stream funding side by side during transition, with common categorization (BAU vs change, CapEx/OpEx) so both reconcile to Planning."}],
 "02.2.3": [
  {"decision":"investment-governance","option":"stage-gate","name":"Approve investments at phase gates","description":"Approve initiatives at defined gates (entity states) with per-state role permissions and gate evidence; record the approved budget on the project and feed it to Planning (A1 approved-investment-budget).","config":"Entity states as gates + per-state role permissions, gate checklists/evidence fields, automation rules for gate notifications, A1 approved-investment-budget feed"},
  {"decision":"investment-governance","option":"lean-lpm","name":"Fund epics within value-stream envelopes","description":"Approval is the move of a Portfolio Epic into Backlog/Implementing within the value stream's guardrails, decided at the participatory budgeting / LPM forum; no per-epic funding record beyond the envelope.","config":"Portfolio Epic workflow states, Lean Budget guardrails, Budgeting solution (fund Portfolios/People), LPM forum cadence"},
  {"decision":"investment-governance","option":"hybrid","description":"Gate approval for large or regulated initiatives; lean envelope approval for value-stream work; one approved-investment feed to Planning covers both."}],
 "02.2.2": [
  {"decision":"prioritization-method","option":"wsjf","name":"Prioritize by WSJF","description":"Rank the portfolio backlog by weighted shortest job first: (business value + time criticality + risk reduction/opportunity enablement) / job size, recalculated each planning cadence.","config":"Numeric custom fields (BV, TC, RR/OE, size), calculated field/metric for WSJF, prioritized list views"},
  {"decision":"prioritization-method","option":"weighted-scoring","name":"Prioritize by weighted objective scoring","description":"Score candidates against weighted criteria (strategic alignment, value, risk, cost, compliance) and rank by score, with weights governed per portfolio.","config":"Scoring custom fields per criterion, weighted score calculated field, Portfolio Epic Score report, objective-scoring configuration"},
  {"decision":"prioritization-method","option":"manual","name":"Rank manually in the governance forum","description":"The portfolio forum orders candidates by hand informed by business cases; the rank is recorded on the epic.","config":"Rank/order field, prioritized list views, forum minutes as comments"}],
 "04.2.1": [
  {"decision":"capacity-basis","option":"team-based","description":"Model capacity per team/ART across the horizon (people x involvement x calendar); vacations reduce team availability."},
  {"decision":"capacity-basis","option":"role-individual","description":"Model capacity per role, location, level and skill and per named individual across the horizon, integrating vacation/holiday schedules."},
  {"decision":"capacity-basis","option":"both","description":"Model team capacity for agile work and role/individual capacity for project work in one model; involvements must sum to 100% per person."}],
 "04.3.1": [
  {"decision":"capacity-basis","option":"team-based","description":"Assign teams, ARTs and solution trains to portfolio work at any hierarchy level (bottom-up demand as team %)."},
  {"decision":"capacity-basis","option":"role-individual","description":"Assign named individuals and roles to projects with requested man-days/hours (see 04.3.4)."},
  {"decision":"capacity-basis","option":"both","description":"Assign teams to agile work and individuals/roles to project work in the same Work Allocation model."}],
 "02.1.1": [
  {"decision":"demand-intake-channel","option":"tp-service-desk","description":"Collect demand through the Targetprocess Service Desk portal into Request entities with request types and voting.","config":"Service Desk portal, Request entity + request types, voting, automation rules"},
  {"decision":"demand-intake-channel","option":"servicenow","description":"Collect ideas in ServiceNow; the integration creates Request/idea records in Targetprocess for qualification and keeps status in sync.","config":"ServiceNow intake integration (10.1.5), field/status mapping, Request entity"},
  {"decision":"demand-intake-channel","option":"email-forms","description":"Collect demand by email or form; automation rules create Request records for triage.","config":"Email integration, form/webhook automation rules, Request entity"}],
 "03.2.1": [
  {"decision":"team-of-record","option":"native","description":"Teams plan sprints/iterations and execute stories, bugs and tasks on Targetprocess boards."},
  {"decision":"team-of-record","option":"synced","description":"Teams plan and execute in Jira/ADO; iterations, states and estimates sync into Targetprocess Team Iterations so the portfolio sees progress without duplicate entry.","config":"Jira/ADO connectors (03.2.4), Team Iteration mapping, state/estimate mapping"}],
 "08.1.2": [
  {"decision":"cost-recovery-model","option":"showback","description":"Deliver periodic Bill of IT statements per BU for information, with traceability to sources; no accounting entries."},
  {"decision":"cost-recovery-model","option":"chargeback-cost","description":"Deliver Bill of IT statements and post the allocated cost as journal entries to BU cost centers each period.","config":"Billing product (Bill of IT), GL journal export, dispute/adjustment process"},
  {"decision":"cost-recovery-model","option":"chargeback-priced","description":"Deliver invoices at service prices (consumption x rate) per BU with a variance view against allocated cost.","config":"Billing product (priced invoices), price list, recovery variance report"}],
}

# whole-L2 applicability
APPLIES = {
 "04.5.2": {"labor-effort-signal":["timesheet"]},
 "05.8.1": {"budget-build-method":["zbb-rotational","zbb-full","zbx"]},
 "05.8.2": {"budget-build-method":["zbb-rotational","zbb-full","zbx"]},
 "05.8.3": {"budget-build-method":["zbb-rotational","zbb-full"]},
 "05.8.4": {"budget-build-method":["zbb-rotational","zbb-full"]},
 "05.8.5": {"budget-build-method":["zbb-rotational","zbb-full"]},
 "05.8.6": {"budget-build-method":["zbb-rotational","zbb-full","zbx"]},
 "03.3.3": {"investment-governance":["stage-gate","hybrid"]},
 "02.1.3": {"investment-governance":["lean-lpm","hybrid"]},
 "04.3.4": {"capacity-basis":["role-individual","both"]},
 "07.5.3": {"cloud-commitment-mode":["assisted"]},
 "07.5.4": {"cloud-commitment-mode":["automated"]},
 "08.1.3": {"cost-recovery-model":["chargeback-priced"]},
 "03.2.4": {"team-of-record":["synced"]},
}

# flow-step conditions: (flow, step n) -> when / decision
WHEN = {
 ("UC1","17"):  {"decision":"labor-effort-signal"},
 ("UC1","17a"): {"when":{"labor-effort-signal":["story-points","story-count","timesheet","work-effort-unit"]}},
 ("UC1","17b"): {"when":{"labor-effort-signal":["fixed-capacity"]}},
 ("ZBB","z0"):  {"when":{"budget-build-method":["zbb-rotational","zbb-full"]}},
 ("ZBB","z1"):  {"when":{"budget-build-method":["zbb-rotational","zbb-full"]}},
 ("ZBB","z4"):  {"when":{"budget-build-method":["zbb-rotational","zbb-full"]}},
 ("ZBB","z5"):  {"when":{"budget-build-method":["zbb-rotational","zbb-full"]}},
 ("ZBB","z6"):  {"when":{"budget-build-method":["zbb-rotational","zbb-full"]}},
 ("ZBB","z7"):  {"when":{"budget-build-method":["zbb-rotational","zbb-full"]}},
 ("ZBB","z8"):  {"when":{"budget-build-method":["zbb-rotational","zbb-full"]}},
 ("ZBB","z9"):  {"when":{"budget-build-method":["zbb-rotational","zbb-full"]}},
}

# base-text edits: strip "alternative:" prose that the variants now carry
BASE = {
 "04.5.1": {"name":"Capture effort against work","description":"Establish the effort record for each team according to the labor effort signal chosen (D-01): recorded hours, completed work from the backlog, confirmed work allocations, or nothing for fixed-capacity teams.","config":"Depends on D-01: Time entity + Time Tracking solution (timesheets) or backlog/allocation data (no timesheets)"},
 "06.4.5": {"name":"Allocate team costs to work or towers","description":"Attach each team's monthly cost to work (epics/features/applications) or to towers/apps, using the labor effort signal chosen for that team kind (D-01): story points, item counts, approved hours, confirmed allocations, or fixed capacity.","config":"One normalized labor model in TBM Studio with an allocation strategy per team kind (see variants)"},
 "02.2.2": {"name":"Prioritize the portfolio backlog","description":"Rank the portfolio backlog against strategy using the prioritization method chosen (D-06): WSJF, weighted objective scoring or manual forum ranking."},
 "04.5.3": {"description":"Deliver the effort record chosen in D-01 (approved hours, completed work, confirmed allocations or roster only) to capitalization, costing and billing over the ADM feed."},
}

# ----------------------------------------------------------------------------- apply
def validate():
    keys = {d["key"] for d in DECISIONS}
    assert len(keys) == len(DECISIONS), "duplicate decision keys"
    D = {d["key"]: d for d in DECISIONS}
    for d in DECISIONS:
        opts = {o["id"] for o in d["options"]}
        assert d["default"] in opts, d["key"]
        for a in d["affects"]: assert a in L2, f"{d['key']} affects unknown {a}"
        for f in d["flows"]: assert f in FLOW, f
        for r in d["related"]: assert r in keys, r
    for l2id, vs in V.items():
        assert l2id in L2, l2id
        for v in vs:
            assert v["decision"] in D, v; assert v["option"] in {o["id"] for o in D[v["decision"]]["options"]}, v
            assert l2id in D[v["decision"]]["affects"], f"{l2id} has variant for {v['decision']} but is not in its affects"
    for l2id, w in APPLIES.items():
        assert l2id in L2, l2id
        for k, opts in w.items():
            assert k in D and set(opts) <= {o["id"] for o in D[k]["options"]}, (l2id, w)
            assert l2id in D[k]["affects"], f"{l2id} applies_when {k} but not in affects"
    for (fid, n), w in WHEN.items():
        assert fid in FLOW and any(s["n"] == n for s in FLOW[fid]["steps"]), (fid, n)
    for l2id in BASE: assert l2id in L2, l2id

def apply():
    validate()
    CAT["decisions"] = DECISIONS
    for l2 in L2.values():
        l2.pop("variants", None); l2.pop("applies_when", None)
    for l2id, edits in BASE.items(): L2[l2id].update(edits)
    for l2id, vs in V.items(): L2[l2id]["variants"] = vs
    for l2id, w in APPLIES.items(): L2[l2id]["applies_when"] = w
    for f in CAT["flows"]:
        for s in f["steps"]: s.pop("when", None); s.pop("decision", None)
    for (fid, n), w in WHEN.items():
        for s in FLOW[fid]["steps"]:
            if s["n"] == n: s.update(w)
    # derived: decisions each L2 touches (variants, applies_when, or listed in affects)
    for d in DECISIONS:
        for a in d["affects"]: L2[a].setdefault("decisions", [])
    for l2 in L2.values():
        ds = set()
        for d in DECISIONS:
            if l2["id"] in d["affects"]: ds.add(d["key"])
        for v in l2.get("variants", []): ds.add(v["decision"])
        for k in l2.get("applies_when", {}): ds.add(k)
        if ds: l2["decisions"] = [d["key"] for d in DECISIONS if d["key"] in ds]
        else: l2.pop("decisions", None)
    if CAT["version"] != "0.7.0":
        CAT["version"] = "0.7.0"; CAT["built"] = "2026-09-15"
        CAT["changelog"].insert(0, {"version":"0.7.0","date":"2026-09-15","items":[
          "Design-decision register added (decisions[]): 11 choices a customer makes once - labor effort signal (story points / item count / timesheets / work-effort units / fixed capacity), labor rate exposure, budget build method, portfolio funding model, investment governance, prioritization method, capacity basis, demand intake channel, cloud commitment mode, IT cost recovery model and team tool of record - each with options, fit, prerequisites, trade-offs and the L2s and flows it affects.",
          "L2 variants: the same process done a different way under an option of a decision (variants[] on 21 L2s, e.g. 06.4.5 has one variant per labor effort signal). Variant fields override the base record; the base stays method-neutral.",
          "L2 applicability (applies_when) marks processes that only exist under certain options, e.g. 04.5.2 Approve timesheets, 05.8.x under ZBB, 07.5.4 under Savings Automation.",
          "Flow-step conditions (when / decision) on UC1 steps 17-17b and ZBB z0-z9 so gateways are labeled from the register and the profile view dims steps that are off-path.",
          "Site: Decisions page (#/decisions) doubles as a customer-profile picker; records show approach tabs; register gains a Decision facet and an 'Approaches' column; flow pages show step conditions. Docs and the Excel master gain Decisions and Variants outputs.",
          "Base text of 04.5.1, 04.5.3, 06.4.5 and 02.2.2 rewritten method-neutral; the 'alternative' prose moved into variants. budgeting_method tags are retained and now documented by decision D-03.",
        ]})
    json.dump(CAT, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(P, "a", encoding="utf-8").write("\n")
    nv = sum(len(v) for v in V.values())
    print(f"v{CAT['version']}: {len(DECISIONS)} decisions, {nv} variants on {len(V)} L2s, {len(APPLIES)} applies_when, {len(WHEN)} flow-step conditions")

if __name__ == "__main__":
    apply()
