# Full Catalog — L0-L2

Generated from `data/catalog.yaml` — **edit the YAML, not this file.**


## L0-01 Strategy & Goal Management

*Define enterprise strategy and cascade it as measurable objectives so every portfolio, program and team has line of sight from work to strategic intent.* Primary: **Targetprocess**. Lanes: C-Suite/Strategy; Portfolio Management; Finance.

Diagrams: [Mermaid](../diagrams/mermaid/area-01.md)


### 01.1 Strategic Planning & Alignment

BPMN: [`diagrams/bpmn/generated/01.1.bpmn`](../diagrams/bpmn/generated/01.1.bpmn)

**01.1.1 Define strategic themes & business objectives** — Capture enterprise strategy as strategic themes/objectives that will govern portfolio investment.
- Delivery model: Any | Tool: Targetprocess | Personas: C-Suite, VP Strategy, Portfolio Mgmt | Cadence: Annual + quarterly refresh
- Inputs: Corporate strategy, market context → Outputs: Strategic themes, objective hierarchy
- Config: Objective entity (OKR solution), Group/portfolio hierarchy, roadmap views
- Framework: SPM: Strategic Planning | SAFe: Strategic Themes | Evidence: SPM CFD; WFM deck; IBM Docs OKR solution

**01.1.2 Cascade strategy to portfolios & value streams** — Link objectives to portfolios, value streams and ARTs so investment and work align top-down (line of sight).
- Delivery model: Any | Tool: Targetprocess | Personas: Portfolio Mgmt, Value Stream owners | Cadence: Annual + on change
- Inputs: Strategic themes → Outputs: Objective-portfolio linkage, funded value streams
- Config: Portfolio/ART (Group) structure, relations objectives->portfolio epics, OKR cascade (Ultimate>Strategic>Tactical)
- Framework: SPM: Strategic Planning | SAFe: LPM | Evidence: TBMC25 Client Zero OKR cascade; EAP CFD 5-step strategic planning

**01.1.3 Monitor strategy execution & re-plan dynamically** — Track progress of strategy in real time via dashboards and re-plan objectives and allocations as conditions change.
- Delivery model: Any | Tool: Targetprocess (+ Costing) | Personas: C-Suite, Portfolio Mgmt | Cadence: Quarterly + continuous
- Inputs: OKR progress, delivery rollups, financials → Outputs: Strategy course corrections
- Config: Corporate Strategy Dashboard, OKR hierarchy views, dashboards fed to leadership reporting (CT Leadership Review)
- Framework: SPM: Strategic Planning | SAFe: Measure & Grow | Evidence: LFM demo (Value Realization tab); EAP CFD step 4-5


### 01.2 OKR Management

BPMN: [`diagrams/bpmn/generated/01.2.bpmn`](../diagrams/bpmn/generated/01.2.bpmn)

**01.2.1 Set & cascade OKRs** — Define objectives and measurable key results at enterprise/portfolio/ART/team levels (3-level or SAFe model) per period.
- Delivery model: Any | Tool: Targetprocess | Personas: All levels; facilitated by Strategy/PMO | Cadence: Quarterly/annual
- Inputs: Strategic themes → Outputs: OKR tree with owners & periods
- Config: OKR solution: Objective & Key Result entities, period assignment, weighted scoring
- Framework: SPM: Strategic Planning | SAFe: OKRs | Evidence: IBM Docs/TP guide OKR solution; Client Zero cascade

**01.2.2 Link work & investments to OKRs** — Relate portfolio epics, features and budgets to objectives so funding and delivery inherit strategic alignment.
- Delivery model: Any | Tool: Targetprocess | Personas: Portfolio Mgmt, Product | Cadence: Continuous
- Inputs: OKR tree, portfolio backlog → Outputs: Work-to-objective traceability
- Config: Relations work items->Objectives, KPI-linked key results, alignment views
- Framework: SPM: Strategic Planning | Evidence: WFM deck (align resources to OKRs); LFM demo

**01.2.3 Score, review & refresh OKRs** — Measure key results (KPI-driven), run quarterly reviews, score and reset objectives.
- Delivery model: Any | Tool: Targetprocess | Personas: C-Suite, Portfolio Mgmt, Teams | Cadence: Quarterly
- Inputs: KR measurements, delivery data → Outputs: OKR scores, refreshed OKRs
- Config: KPI solution measurements, calculated fields, OKR dashboards & review views
- Framework: SPM: Strategic Planning | SAFe: Measure & Grow | Evidence: TP guide OKR; SPM maturity model (Strategic Planning lens)


## L0-02 Demand & Portfolio Investment Management

*Capture all demand into one funnel, qualify and prioritize it against strategy and capacity, fund the winning investments, and manage the portfolio roadmap and its value realization.* Primary: **Targetprocess**. Lanes: Requesters/Business; Portfolio Management; PMO; Finance.

Diagrams: [Mermaid](../diagrams/mermaid/area-02.md)


### 02.1 Demand Intake & Qualification

BPMN: [`diagrams/bpmn/generated/02.1.bpmn`](../diagrams/bpmn/generated/02.1.bpmn)

**02.1.1 Capture ideas & requests** — Collect demand from all channels - Service Desk portal, email, ServiceNow ideation - into Request/idea entities.
- Delivery model: Any | Tool: Targetprocess (+ ServiceNow) | Personas: Requesters (any), Service Desk users | Cadence: Continuous
- Inputs: Ideas, requests, mandates → Outputs: Logged demand records
- Config: Service Desk portal, Request entity + request types, email integration, voting; ServiceNow intake integration
- Framework: SPM: Demand Intake | FinOps n/a | Evidence: TP guide Service Desk; WFM deck (ServiceNow ideation front-end)

**02.1.2 Triage, categorize & qualify demand** — Route, categorize (work item taxonomy, BAU vs change, CapEx/OpEx) and qualify requests against strategy before they enter the portfolio funnel.
- Delivery model: Any | Tool: Targetprocess | Personas: PMO, Portfolio Mgmt | Cadence: Weekly cadence
- Inputs: Demand records → Outputs: Qualified demand in funnel
- Config: Request workflow states, triage boards, automation rules (routing/auto-reply/linked entities), work-intake taxonomy (categories, CapEx/OpEx, non-labor categories)
- Framework: SPM: Demand Intake | Evidence: SPM journey map (work-intake model taxonomy); TP guide

**02.1.3 Progress demand through Portfolio Kanban** — Move epics Funnel-Reviewing-Analyzing-Backlog-Implementing-Done with WIP limits and visible decision states.
- Delivery model: Agile | Tool: Targetprocess | Personas: Portfolio Mgmt, LPM function | Cadence: Continuous
- Inputs: Qualified demand → Outputs: Decided/scheduled portfolio backlog
- Config: Portfolio Epic workflow states, Kanban board views, WIP limits, per-state permissions
- Framework: SAFe: Portfolio Kanban | SPM: Demand Intake | Evidence: SAFe LPM; TP entity workflows


### 02.2 Prioritization & Investment Decision

BPMN: [`diagrams/bpmn/generated/02.2.bpmn`](../diagrams/bpmn/generated/02.2.bpmn)

**02.2.1 Build lean business case / epic hypothesis** — Estimate outcomes, effort and MVP for candidate investments; capture hypothesis and benefit model.
- Delivery model: Any | Tool: Targetprocess | Personas: Epic owners, Portfolio Mgmt, Finance | Cadence: Per candidate epic
- Inputs: Qualified epics → Outputs: Lean business cases with estimates
- Config: Budgeting solution templates (epic hypothesis, lean business case), rich-text/custom fields, Portfolio Epic Score report
- Framework: SAFe: Epic/LPM | SPM: Demand Intake | Evidence: TP Budgeting solution; LFM demo (epic scoring)

**02.2.2 Prioritize by value (WSJF / scoring)** — Rank the portfolio backlog by WSJF or configurable value scoring against strategy. Hybrid alternative: manual or objective-scoring prioritization for non-agile work.
- Delivery model: Agile | Tool: Targetprocess | Personas: Portfolio Mgmt, Business owners | Cadence: Per planning cadence
- Inputs: Business cases, capacity signal → Outputs: Ranked backlog
- Config: Numeric custom fields (BV, TC, RR/OE, size), calculated field/metric for WSJF, prioritized list views, objective-scoring
- Framework: SAFe: WSJF | SPM: Demand Intake | Evidence: TP calculated fields; WFM deck prioritization

**02.2.3 Approve & fund investments** — Make funding decisions - stage-gate approval or lean value-stream funding - and record approved budget against the investment. Supports both stage-gate (phase approvals via entity states) and lean value-stream funding.
- Delivery model: Hybrid | Tool: Targetprocess (+ Costing, Planning) | Personas: Portfolio Mgmt, Finance, PMO | Cadence: Quarterly/participatory budgeting
- Inputs: Ranked backlog, budget envelope → Outputs: Funded investments/epics
- Config: Entity states + per-state role permissions (gates), automation rules for approvals, Budgeting solution (fund Portfolios/Work/People/Products), A1 approved-investment-budget feed
- Framework: SAFe: Lean Budgets & Guardrails | TBM: Investment in Innovation | Evidence: TP Budgeting; ApptioOne CFD IIP bi-directional loop


### 02.3 Portfolio Planning & Roadmapping

BPMN: [`diagrams/bpmn/generated/02.3.bpmn`](../diagrams/bpmn/generated/02.3.bpmn)

**02.3.1 Build & maintain roadmaps** — Publish time-based portfolio/product/program roadmaps against releases and PIs at multiple levels.
- Delivery model: Any | Tool: Targetprocess | Personas: Portfolio Mgmt, Product | Cadence: Quarterly + continuous
- Inputs: Funded epics, PI calendar → Outputs: Multi-level roadmaps
- Config: Timeline/Roadmap views on Portfolio Epics/Epics/Features vs Releases/PIs, multi-level roadmaps
- Framework: SPM: Portfolio Mgmt | Evidence: TP view modes; Solution Overview deck

**02.3.2 Model scenarios & trade-offs** — Evaluate alternative portfolio mixes (scope, timing, capacity, budget) and promote the chosen scenario to the plan of record.
- Delivery model: Any | Tool: Targetprocess (+ Planning) | Personas: Portfolio Mgmt, Finance | Cadence: Planning cycles + ad hoc
- Inputs: Backlog, capacity, targets → Outputs: Selected scenario/baseline
- Config: Scenario Planning solution (plan variants, promote scenario to baseline), demand vs capacity data, budget dashboards
- Framework: SPM: Portfolio Mgmt | SAFe: Participatory Budgeting | Evidence: Customer PowerUp (scenario planning, baselines); TP solutions

**02.3.3 Manage cross-initiative dependencies & risks** — Identify, visualize and resolve dependencies and portfolio-level risks across initiatives and trains.
- Delivery model: Any | Tool: Targetprocess | Personas: Portfolio Mgmt, RTEs | Cadence: Continuous
- Inputs: Roadmaps, PI plans → Outputs: Dependency/risk register & resolutions
- Config: Dependency/Impediment entities, relations, ART Planning Board, Risk Management solution
- Framework: SAFe: Program risks/ROAM | SPM: Portfolio Mgmt | Evidence: TP entities; PI Planning solution

**02.3.4 Maintain one governed hybrid portfolio view** — View and manage all work across hybrid programs - agile (epics/features from teams' tools) and waterfall projects - in a single governed environment with common categorization (BAU vs Change, CapEx/OpEx).
- Delivery model: Hybrid | Tool: Targetprocess (+ Jira/ADO) | Personas: Portfolio Mgmt, PMO | Cadence: Continuous
- Inputs: Agile work (synced), project plans → Outputs: Unified hybrid portfolio views & status
- Config: Hybrid portfolio views (agile + waterfall side by side), Hybrid Project Management solution, common work categorization fields, Jira/ADO sync for agile initiatives
- Framework: SPM: Hybrid Portfolio Mgmt (HPM solution area) | Evidence: WFM deck (View all work across Hybrid Programs); Customer PowerUp (hybrid planning)


### 02.4 Portfolio Funding & Budget Tracking

BPMN: [`diagrams/bpmn/generated/02.4.bpmn`](../diagrams/bpmn/generated/02.4.bpmn)

**02.4.1 Define funding model** — Choose and configure project-based, product/value-stream (continuous) or hybrid funding with planning periods. Hybrid organizations typically run project-based and product-based funding side by side during transition.
- Delivery model: Hybrid | Tool: Targetprocess (+ Planning) | Personas: Finance, Portfolio Mgmt, PMO | Cadence: Annual (model), evolving
- Inputs: Operating model decisions → Outputs: Configured funding structure
- Config: Budgeting solution (annual or custom periods, value-stream funding), portfolio structure, budget guardrails by horizon/capacity/initiative
- Framework: SAFe: Lean Budgets | SPM: Financial Mgmt | Evidence: EAP CFD (annual->continuous); TP Budgeting

**02.4.2 Receive & apply top-down targets** — Consume target spend/budget artifacts from IT Planning and apply them as portfolio budget targets (UC3 receive side).
- Delivery model: Any | Tool: Targetprocess (+ Planning) | Personas: Portfolio Mgmt, Finance | Cadence: Per planning cycle
- Inputs: Portfolio spend targets (ADM from Planning) → Outputs: Top-down budget/target artifacts in ATP
- Config: Budget Targets report, target budget entities, ADM/data highway feed
- Framework: SPM: Financial Mgmt | TBM: Plan & Govern | Evidence: E2E BPMN UC3; LFM demo (Target Budget from planning solution)

**02.4.3 Track portfolio budget vs actuals** — Compare proposed/funded budgets against costed work and actuals; adjust funding in-year.
- Delivery model: Any | Tool: Targetprocess (+ Costing) | Personas: Portfolio Mgmt, Finance | Cadence: Monthly
- Inputs: Costed allocations, actuals, budgets → Outputs: Variance signals, funding adjustments
- Config: Budget vs actuals dashboards, money custom fields, blended-rate costed work allocations, Budgeting view (Proposed Labor vs Target)
- Framework: SPM: Financial Mgmt | Evidence: LFM demo; WFM deck Finance Manager activities


### 02.5 Value & Benefits Realization

BPMN: [`diagrams/bpmn/generated/02.5.bpmn`](../diagrams/bpmn/generated/02.5.bpmn)

**02.5.1 Define expected outcomes & value metrics** — Set benefit hypotheses, KPIs and leading indicators for each funded investment.
- Delivery model: Any | Tool: Targetprocess | Personas: Epic owners, Finance, Strategy | Cadence: At funding
- Inputs: Business cases → Outputs: Outcome metrics per investment
- Config: KPI solution, key results on epics, money/number custom fields
- Framework: SPM: Value Realization | TBM: Delivering Value | Evidence: SPM maturity model; TP KPI solution

**02.5.2 Track realized value & feed decisions** — Measure delivered outcomes vs hypothesis after release and feed results into ongoing funding and portfolio reviews.
- Delivery model: Any | Tool: Targetprocess (+ Costing) | Personas: Portfolio Mgmt, Finance | Cadence: Quarterly
- Inputs: KPI measurements, cost actuals → Outputs: Value realization reports, kill/persevere/pivot decisions
- Config: KPI measurements, dashboards, Value Realization tab in leadership reporting, ROI/margin analysis
- Framework: SPM: Value Realization | TBM: four value conversations | Evidence: WFM closed loop (Analyze & Act); LFM demo


## L0-03 Agile Program & Delivery Management

*Plan and execute work on a PI and iteration cadence across ARTs, solution trains and teams, including hybrid/waterfall delivery, release management and value stream flow.* Primary: **Targetprocess**. Lanes: RTE/Program; Agile Teams; Product Management; Dev tools (Jira/ADO).

Diagrams: [Mermaid](../diagrams/mermaid/area-03.md)


### 03.1 PI Planning

BPMN: [`diagrams/bpmn/generated/03.1.bpmn`](../diagrams/bpmn/generated/03.1.bpmn)

**03.1.1 Assess & prepare PI readiness** — Run readiness checks (PI/ART entities, objectives, features, team objectives) and execute the 4-phase preparation plan.
- Delivery model: Agile | Tool: Targetprocess | Personas: RTE/PI Coordinator, Product Owners, System Architect, Scrum Masters | Cadence: Per PI (8-12 wks)
- Inputs: Portfolio backlog, ART/team structure → Outputs: READY verdict, prepared backlog & objectives
- Config: PI & ART entities with dates, ART/Program PI Objectives, Team PI Objectives, features assigned to PI release, capacity fields (velocity = people x 8 rule; 80/20 allocation), PI Planning solution Pre-Plan views
- Framework: SAFe: PI Planning | Evidence: PI Planning Demo Script (readiness + 20-day plan); PI Planning solution 1.0.0

**03.1.2 Run PI planning event** — Facilitate big-room planning: teams plan features/stories into iterations, map dependencies, ROAM risks.
- Delivery model: Agile | Tool: Targetprocess | Personas: ART (all roles), Business Owners | Cadence: Per PI
- Inputs: Prepared backlog, capacity → Outputs: Draft team plans, dependency board
- Config: PI Planning Board, ART Planning Board (dependencies), Team Iteration assignment, WSJF-ordered features, risk entities
- Framework: SAFe: PI Planning | Evidence: PI Planning solution; EAP CFD program mgmt 4-step

**03.1.3 Commit & publish PI objectives** — Finalize team/ART PI objectives with business value, confidence vote, and publish the program board.
- Delivery model: Agile | Tool: Targetprocess | Personas: ART, Business Owners | Cadence: Per PI
- Inputs: Draft plans → Outputs: Committed PI objectives & program board
- Config: Team PI Objectives (Committed/Stretch, confidence %, BV points), PI Dashboard, Program Board
- Framework: SAFe: PI Planning | Evidence: PI Planning Demo Script

**03.1.4 Track PI execution & system demo** — Monitor feature progress, dependencies and risks through the PI; run system demos and inspect & adapt.
- Delivery model: Agile | Tool: Targetprocess (+ Jira/ADO) | Personas: RTE, teams, stakeholders | Cadence: Iteration cadence
- Inputs: Committed plan, delivery data → Outputs: Progress/flow reporting, I&A actions
- Config: PI Dashboard, dependency & risk boards, progress rollup metrics, burndown/CFD reports
- Framework: SAFe: PI execution | Evidence: TP reports; PI Planning solution Coordinate & Deliver views


### 03.2 Team Delivery

BPMN: [`diagrams/bpmn/generated/03.2.bpmn`](../diagrams/bpmn/generated/03.2.bpmn)

**03.2.1 Plan & execute iterations** — Teams plan sprints/iterations and execute stories, bugs and tasks through their workflow.
- Delivery model: Agile | Tool: Targetprocess (+ Jira/ADO) | Personas: Agile teams, Scrum Masters | Cadence: Per iteration
- Inputs: Team backlog, capacity → Outputs: Working increments, updated states
- Config: Team Iteration entities, Scrum/Kanban team boards, story/bug/task workflows, estimation fields
- Framework: SAFe/Scrum/Kanban | Evidence: TP entity model

**03.2.2 Track flow & progress** — Measure velocity, cycle/lead time, cumulative flow and rollups to features/epics/releases.
- Delivery model: Agile | Tool: Targetprocess | Personas: Teams, RTE, PMO | Cadence: Continuous
- Inputs: Work item events → Outputs: Flow metrics, forecasts
- Config: Velocity/burn/CFD/cycle-time reports, Metrics engine rollups, Forecast reports
- Framework: SAFe: Metrics | VSM flow metrics | Evidence: TP reports; Solution Overview

**03.2.3 Manage impediments & dependencies** — Raise, track and resolve team-level impediments and cross-team dependencies.
- Delivery model: Any | Tool: Targetprocess | Personas: Teams, Scrum Masters, RTE | Cadence: Continuous
- Inputs: Delivery events → Outputs: Resolved blockers
- Config: Impediment/Dependency entities, boards, automation rule notifications
- Framework: SAFe | Evidence: TP entities

**03.2.4 Sync with dev tools** — Keep team-of-record tools (Jira, Azure DevOps, Git) bi-directionally synced so ATP is the aggregation layer, not a duplicate.
- Delivery model: Agile | Tool: Targetprocess (+ Jira, ADO, Git) | Personas: Teams, Platform Admin | Cadence: Continuous (auto)
- Inputs: Issues, commits, PRs → Outputs: Unified hierarchy over team tools
- Config: Native Jira/ADO bi-directional connectors (issue-level, area/iteration path), Git/GitHub/GitLab via automation rules/webhooks
- Framework: EAP: aggregation layer | Evidence: TP integrations; anti-pattern: no story-level Jira import to cost systems (e2e script)


### 03.3 Release & Hybrid Project Management

BPMN: [`diagrams/bpmn/generated/03.3.bpmn`](../diagrams/bpmn/generated/03.3.bpmn)

**03.3.1 Plan releases & enable release packages** — Plan release scope/timing and manage release package enablement across trains.
- Delivery model: Any | Tool: Targetprocess | Personas: Release/Program Mgmt | Cadence: Per release
- Inputs: Roadmap, PI plans → Outputs: Release plans
- Config: Release/Planning Interval entities, Release Package Enablement solution
- Framework: SAFe: Release on demand | Evidence: TP solutions

**03.3.2 Manage hybrid & waterfall projects** — Run traditional/hybrid projects (phases, milestones, Gantt) side-by-side with agile work in one governed portfolio.
- Delivery model: Hybrid | Tool: Targetprocess | Personas: Project Managers, PMO | Cadence: Per project
- Inputs: Project charters → Outputs: Project plans & status
- Config: Traditional/Hybrid Project Management solutions, timeline views, milestones, hybrid portfolio views
- Framework: SPM: hybrid portfolio | Evidence: Customer PowerUp (hybrid); WFM deck

**03.3.3 Govern stage-gates & milestones for traditional initiatives** — Run phase-gate governance for waterfall/traditional initiatives: gate reviews as controlled state transitions, milestone tracking, and gate-approval evidence.
- Delivery model: Traditional | Tool: Targetprocess | Personas: PMO, Gate approvers, Project Managers | Cadence: Per phase gate
- Inputs: Project plans, gate criteria → Outputs: Gate decisions, milestone status
- Config: Entity states as gates with per-state role permissions, milestone entities, timeline/Gantt views, automation rules for gate notifications, Traditional Project Management solution
- Framework: Stage-gate governance | SPM: Portfolio Mgmt | Evidence: SPM/TP research (stage-gate vs lean funding); Traditional PM solution


### 03.4 Value Stream Management

BPMN: [`diagrams/bpmn/generated/03.4.bpmn`](../diagrams/bpmn/generated/03.4.bpmn)

**03.4.1 Identify & map value streams** — Define operational/development value streams and organize portfolios, ARTs and funding around them.
- Delivery model: Agile | Tool: Targetprocess | Personas: Portfolio Mgmt, LACE/Transformation | Cadence: Initial + periodic
- Inputs: Org & product context → Outputs: Value stream model in tool structure
- Config: ART/Group structure as value streams, value stream workshops (journey map), portfolio mapping
- Framework: SAFe: VSM | SPM | Evidence: SPM journey map (VSM pilot, workshops)

**03.4.2 Measure & improve flow** — Track value stream KPIs and flow metrics; run improvement actions.
- Delivery model: Agile | Tool: Targetprocess | Personas: VS owners, RTEs | Cadence: Quarterly
- Inputs: Flow data → Outputs: VS KPI dashboards, improvement backlog
- Config: Value stream KPIs (SAFe 6.0 solution), KPI solution, flow dashboards
- Framework: SAFe: VSM/flow | Evidence: Customer PowerUp (SAFe 6.0, value stream KPIs)


## L0-04 Workforce & Resource Management

*Maintain the workforce baseline (people, teams, involvements, job profiles), plan capacity against demand, allocate resources to work, govern position requests, and track time.* Primary: **Targetprocess**. Lanes: Resource Management; Portfolio Management; HR/Approvers; Finance (IT Planning).

Diagrams: [Mermaid](../diagrams/mermaid/area-04.md)


### 04.1 Workforce Baseline & Team Structure

BPMN: [`diagrams/bpmn/generated/04.1.bpmn`](../diagrams/bpmn/generated/04.1.bpmn)

**04.1.1 Load & maintain people roster** — Establish the workforce baseline (employees, contractors, vendor service, consulting) from HR sources with per-source sync cadences.
- Delivery model: Any | Tool: Targetprocess (+ Workday/HCM) | Personas: Resource Mgmt, HR, Platform Admin | Cadence: Daily-monthly by source
- Inputs: HCM/roster feeds (Workday, Fieldglass) → Outputs: Current people baseline with attributes
- Config: People/Users entities, employee type (internal/external/contingent, on/offshore, billable), locations, skills; sync cadence per source (Client Zero: employees+contractors daily, consulting monthly, other manual)
- Framework: SPM: WFM (baseline) | TBM: labor cost pools | Evidence: TBMC25 Load & Maintain People; WFM deck

**04.1.2 Create & assign teams, ARTs & trains** — Build the team-of-teams structure and assign people to teams with involvement percentages.
- Delivery model: Any | Tool: Targetprocess | Personas: Resource Mgmt, RTEs | Cadence: On change
- Inputs: People baseline, org design → Outputs: Team>ART>Solution Train structure with involvements
- Config: Team entities & hierarchy, ART/Solution Train, Involvements (% allocation, e.g. 50/75/100), team-project assignment
- Framework: SPM: WFM | SAFe: ART | Evidence: TBMC25 Create & Assign Teams; e2e script (involvements)

**04.1.3 Maintain job profiles & financial mappings** — Keep job profiles (role x location) mapped to rates and CapEx/OpEx splits, and teams mapped to IT towers - the three ingredients of the labor model.
- Delivery model: Any | Tool: Targetprocess (+ Costing) | Personas: Finance, Resource Mgmt | Cadence: Quarterly + on change
- Inputs: HR role data, finance rules → Outputs: Job profiles with rate & CapEx/OpEx mapping; team-tower mapping
- Config: Job Profile entities, CapEx/OpEx split mapping per profile, team->IT Tower mapping (fixed capacity rule), rate linkage (rates held in Costing)
- Framework: TBM: labor costing | SPM: WFM | Evidence: E2E BPMN t_data; e2e script UC1 three ingredients


### 04.2 Capacity Planning

BPMN: [`diagrams/bpmn/generated/04.2.bpmn`](../diagrams/bpmn/generated/04.2.bpmn)

**04.2.1 Map & forecast capacity** — Model capacity by function, role, location, level, skills, BU and domain across the planning horizon, integrating vacation/holiday schedules. Agile contexts plan capacity team-based; hybrid/traditional contexts plan role- and individual-based - model both.
- Delivery model: Any | Tool: Targetprocess | Personas: Resource Mgmt, Capacity planners | Cadence: Monthly/quarterly
- Inputs: Roster, involvements, calendars → Outputs: Capacity model & forward view
- Config: Capacity dashboards, availability (total/reserved/available), Vacation Tracking solution feeding availability, regional calendars
- Framework: SPM: WFM capacity | Evidence: SPM Framework WFM use cases; WFM deck capacity activities

**04.2.2 Balance demand vs capacity** — Compare bottom-up demand rollups against available capacity and targets; resolve over/under allocation (e.g. 'three months out, demand exceeds FTE').
- Delivery model: Any | Tool: Targetprocess (+ Planning) | Personas: Portfolio Mgmt, Resource Mgmt, Finance | Cadence: Monthly + planning cycles
- Inputs: Work allocations/demand, capacity model, target spend → Outputs: Rebalanced allocations, hiring signals
- Config: Demand & Capacity Mgmt solution (Work Allocation entity %/hours/man-days, auto-generated Demand per period, load reports, demand processing screens), capacity/FTE reports vs targets
- Framework: SPM: WFM | SAFe: capacity | Evidence: E2E BPMN t_cmp; TP Demand & Capacity solution

**04.2.3 Run workforce scenarios** — Model alternative workforce/demand scenarios (mix, location, hiring) and promote decisions into plans.
- Delivery model: Any | Tool: Targetprocess (+ Planning) | Personas: Resource Mgmt, Finance | Cadence: Planning cycles
- Inputs: Capacity model, targets → Outputs: Chosen workforce scenario
- Config: Scenario planning (workforce scenarios, labor availabilities generation), HC scenario views
- Framework: SPM: WFM scenarios | Evidence: Customer PowerUp; WFM deck


### 04.3 Resource Allocation & Utilization

BPMN: [`diagrams/bpmn/generated/04.3.bpmn`](../diagrams/bpmn/generated/04.3.bpmn)

**04.3.1 Allocate people & teams to work** — Assign users, teams, ARTs and solution trains to portfolio work at any hierarchy level (bottom-up demand).
- Delivery model: Any | Tool: Targetprocess | Personas: Portfolio Mgmt, Resource Mgmt | Cadence: Continuous
- Inputs: Funded work, capacity → Outputs: Work allocations (bottom-up demand)
- Config: Work Allocation entities, allocation timelines, team-to-work assignment at any level
- Framework: SPM: WFM | SAFe | Evidence: E2E BPMN t_alloc; LFM demo work allocations

**04.3.2 Track utilization & productivity** — Compare planned vs actual utilization; monitor bottlenecks and efficiency by role/location/team.
- Delivery model: Any | Tool: Targetprocess (+ Costing) | Personas: Resource Mgmt | Cadence: Monthly
- Inputs: Allocations, time/work data → Outputs: Utilization & efficiency reports
- Config: Resource Management Dashboard, Team Load report, Efficiency tab (completed items & effort MoM)
- Framework: SPM: WFM metrics | Evidence: LFM demo deep-dives

**04.3.3 Match skills & close gaps** — Compare work demand to skills supply; identify hiring/upskilling needs.
- Delivery model: Any | Tool: Targetprocess | Personas: Resource Mgmt, HR | Cadence: Quarterly
- Inputs: Skills data, demand → Outputs: Gap analysis, hiring/upskill plan
- Config: Skills fields, capacity by skill views, gap reports
- Framework: SPM: WFM | Evidence: SPM Framework WFM use case 5

**04.3.4 Assign individuals & roles to project work (hybrid resourcing)** — For traditional/hybrid work, assign named individuals or roles to projects with requested man-days - alongside team-based allocation used for agile work - so one capacity model covers both.
- Delivery model: Hybrid | Tool: Targetprocess (+ Planning) | Personas: Resource Mgmt, Project Managers | Cadence: Per project + continuous
- Inputs: Project demand (roles, man-days), roster → Outputs: Individual/role assignments in the same capacity model
- Config: Work Allocations (person-level man-days/hours), role-based demand requests, New Requested Demand workflow, availability integration
- Framework: SPM: WFM | Hybrid resourcing | Evidence: LFM demo (requested man-days from individuals/teams); WFM deck


### 04.4 Position Management

BPMN: [`diagrams/bpmn/generated/04.4.bpmn`](../diagrams/bpmn/generated/04.4.bpmn)

**04.4.1 Create position requests** — Raise governed requests for new positions (role, location, hours, type, department link to the finance budget line).
- Delivery model: Any | Tool: Targetprocess | Personas: Portfolio/Hiring managers | Cadence: On demand
- Inputs: Capacity gaps, budget line → Outputs: Position request records
- Config: Position Request entity (role, location, hours, employment type, department link)
- Framework: SPM: WFM | ITFM: headcount | Evidence: E2E BPMN t_pos; e2e script UC3

**04.4.2 Approve positions (multi-level workflow)** — Route position requests through HR > Department > Final approval with notifications, dependencies and escalations; reject or approve.
- Delivery model: Any | Tool: Targetprocess | Personas: HR, Dept approvers, Final approver | Cadence: Per request
- Inputs: Position requests → Outputs: Approved/rejected positions
- Config: Multi-level approval workflow (entity states + per-state permissions), automation rules (notifications, escalations), XOR outcome
- Framework: Governance | Evidence: E2E BPMN t_appr/g_appr

**04.4.3 Sync approved positions to Planning & auto-update on fill** — Send only approved positions across the data highway to IT Planning for budgeting; when filled in ATP the Planning record updates automatically.
- Delivery model: Any | Tool: Targetprocess (+ Planning) | Personas: System (ADM), Finance | Cadence: Daily/weekly sync
- Inputs: Approved positions; fill events → Outputs: Budgeted open+filled positions, auto-updated
- Config: ADM/data highway position feed, open vs filled normalization in Planning, auto-update linkage
- Framework: ITFM: headcount planning | Evidence: E2E BPMN t_send2/t_norm; e2e script round-trip


### 04.5 Time Tracking & Approval

BPMN: [`diagrams/bpmn/generated/04.5.bpmn`](../diagrams/bpmn/generated/04.5.bpmn)

**04.5.1 Record time against work** — Log task-level time or use work allocations as the effort signal; capture estimate vs actual vs remaining, billable flags. Timesheets matter most for traditional/hybrid delivery; pure agile teams can rely on work allocations and completed-work signals instead.
- Delivery model: Any | Tool: Targetprocess | Personas: Team members | Cadence: Daily/weekly
- Inputs: Work items → Outputs: Time entries / effort data
- Config: Time entity, Time Tracking solution, timesheet views, billable/non-billable fields; alternative: work allocations instead of timesheets
- Framework: SPM: Financial Mgmt | capitalization input | Evidence: TP Time Tracking; Timesheet solution sheet; LFM demo

**04.5.2 Approve timesheets** — Managers review and approve weekly timesheets under governance rules.
- Delivery model: Any | Tool: Targetprocess | Personas: Managers | Cadence: Weekly
- Inputs: Time entries → Outputs: Approved time
- Config: Timesheet approval workflow (solution component), notifications
- Framework: Governance | Evidence: 2026.03 Timesheet with Approval Workflow solution sheet; Solution Overview (time recording)

**04.5.3 Feed time/effort to finance processes** — Deliver approved time or allocation-based effort to capitalization, costing and billing processes (or deprecate time writing via the UC1 model).
- Delivery model: Any | Tool: Targetprocess (+ Costing) | Personas: Finance | Cadence: Monthly
- Inputs: Approved time / completed work → Outputs: Effort data for costing & CapEx
- Config: Time reports/exports, ADM feed to Costing, story-point/completed-work alternative (deprecates time writing)
- Framework: TBM: labor allocation options | Evidence: E2E script UC1 payoff; Costing labor allocation options


## L0-05 IT Financial Planning & Budgeting

*Build the annual IT budget and rolling forecasts on the TBM taxonomy - labor, contracts, assets and investments - manage variance, and publish targets that drive portfolio behavior.* Primary: **Planning**. Lanes: IT Finance; Budget Owners; FP&A; CIO.

Diagrams: [Mermaid](../diagrams/mermaid/area-05.md)


### 05.1 Annual IT Budgeting

BPMN: [`diagrams/bpmn/generated/05.1.bpmn`](../diagrams/bpmn/generated/05.1.bpmn)

**05.1.1 Establish plan structure & baseline** — Create the plan, fiscal calendar and hierarchy; seed baseline from prior plan or actuals.
- Delivery model: Any | Tool: Planning (+ Costing) | Personas: IT Finance | Cadence: Annual
- Inputs: Prior plan, actuals, reference data → Outputs: Open plan with baseline
- Config: Plan creation, plan folders, working calendar, Adjust Baseline Values, actuals import, cost center/account hierarchies
- Framework: ITFM: budgeting | TBM: Plan & Govern | Evidence: IBM Docs Planning; planning research

**05.1.2 Set & distribute top-down targets** — Set target spend and headcount envelopes by department/cost center/ART and distribute to budget owners.
- Delivery model: Any | Tool: Planning (+ Targetprocess) | Personas: CIO, IT Finance, FP&A | Cadence: Annual
- Inputs: Corporate targets → Outputs: Distributed targets
- Config: Set Targets, Labor Headcount Targets, cost object permissions; target feed to ATP (UC3)
- Framework: ITFM | SPM: Financial Mgmt | Evidence: Planning docs; E2E BPMN t_wfp/t_send1

**05.1.3 Enter bottom-up budgets** — Budget owners build OpEx/CapEx line items and transactions per cost center in resource-based views.
- Delivery model: Any | Tool: Planning | Personas: Budget owners | Cadence: Annual (cycle)
- Inputs: Targets, driver data → Outputs: Submitted budgets
- Config: Worksheets/line items, cost categorization, multi-currency, transaction-level entry
- Framework: ITFM | Evidence: Planning docs

**05.1.4 Review, iterate & approve budget** — Run submit/review/approve/return cycles until targets and bottom-up plans reconcile.
- Delivery model: Any | Tool: Planning | Personas: IT Finance, leadership, budget owners | Cadence: Annual (cycle)
- Inputs: Submitted budgets → Outputs: Approved budget
- Config: Approval workflow (submit/review/approve/return), plan states New>Open>Final, conversational insights
- Framework: ITFM governance | Evidence: Planning docs

**05.1.5 Finalize budget of record** — Lock the approved plan as budget of record with a snapshot for variance baselines.
- Delivery model: Any | Tool: Planning | Personas: IT Finance | Cadence: Annual
- Inputs: Approved budget → Outputs: Budget of record + snapshot
- Config: Plan state Final, snapshots/version compare
- Framework: ITFM | Evidence: Planning docs


### 05.2 Rolling & Periodic Forecasting

BPMN: [`diagrams/bpmn/generated/05.2.bpmn`](../diagrams/bpmn/generated/05.2.bpmn)

**05.2.1 Create forecast seeded with actuals** — Open a forecast version seeded with YTD actuals plus remaining plan.
- Delivery model: Any | Tool: Planning (+ Costing) | Personas: IT Finance | Cadence: Monthly/quarterly
- Inputs: Actuals (Costing/GL), plan → Outputs: Forecast version
- Config: Actuals import, Costing integration, snapshots, multi-year plans
- Framework: ITFM: rolling forecast | Evidence: Planning docs; Apptio 5-step rolling forecast

**05.2.2 Update forecasts (driver & AI-assisted)** — Focus on largest controllable variance drivers; use Intelligent Forecasting and contract auto-extension to update lines.
- Delivery model: Any | Tool: Planning | Personas: IT Finance, budget owners | Cadence: Monthly
- Inputs: Historical data, drivers → Outputs: Updated forecast
- Config: Intelligent Forecasting (multi-model AI), contract auto-extension, driver-based lines
- Framework: ITFM | FinOps: Forecasting (intersect) | Evidence: Planning release notes; rolling-forecast method

**05.2.3 Model what-if scenarios** — Compare versions/plans and model scenario impacts; sync enterprise scenarios with corporate FP&A.
- Delivery model: Any | Tool: Planning (+ Planning Analytics) | Personas: IT Finance, FP&A | Cadence: Ad hoc
- Inputs: Forecast, scenario drivers → Outputs: Scenario comparisons
- Config: Compare Versions/Plans, what-if modeling, IBM Planning Analytics bi-directional connector
- Framework: ITFM | Evidence: Planning docs; McGraw Hill pattern

**05.2.4 Submit & sign off forecast** — Budget owners submit forecasts for review and sign-off on cadence.
- Delivery model: Any | Tool: Planning | Personas: Budget owners, IT Finance | Cadence: Monthly/quarterly
- Inputs: Updated forecasts → Outputs: Approved forecast of record
- Config: Approval workflow, plan status tracking
- Framework: ITFM governance | Evidence: Planning docs


### 05.3 Variance Analysis & Reforecasting

BPMN: [`diagrams/bpmn/generated/05.3.bpmn`](../diagrams/bpmn/generated/05.3.bpmn)

**05.3.1 Load & reconcile actuals to plan** — Bring closed actuals from Costing/GL into the plan and reconcile mappings (plan-to-actuals).
- Delivery model: Any | Tool: Planning (+ Costing) | Personas: IT Finance | Cadence: Monthly close
- Inputs: Closed actuals → Outputs: Reconciled plan-vs-actuals dataset
- Config: Costing/Cost Transparency integration, actuals import, GL-to-IT category mappings
- Framework: ITFM | TBM | Evidence: Planning docs

**05.3.2 Analyze variances with thresholds** — Analyze budget-vs-actuals and plan-vs-plan variance by cost pool/tower/CC with materiality thresholds.
- Delivery model: Any | Tool: Planning (+ Costing) | Personas: IT Finance, budget owners | Cadence: Monthly
- Inputs: Reconciled data → Outputs: Material variance list
- Config: Variance analysis, Plan vs Plan variance with thresholds, variance REST APIs, exports
- Framework: ITFM | TBM: Cost Pool variance monthly | Evidence: Planning docs; TBM assessment (reporting)

**05.3.3 Narrate variance & reforecast** — Capture commentary and corrective actions on material variances, then reforecast remaining periods (<1% variance ambition).
- Delivery model: Any | Tool: Planning | Personas: Budget owners, IT Finance | Cadence: Monthly
- Inputs: Variance list → Outputs: Commentary, updated forecast
- Config: Comments, change-history audit, forecast update workflow
- Framework: ITFM | Evidence: Planning docs; ApptioOne virtuous cycle (Control)


### 05.4 Workforce & Labor Cost Planning

BPMN: [`diagrams/bpmn/generated/05.4.bpmn`](../diagrams/bpmn/generated/05.4.bpmn)

**05.4.1 Plan positions & FTEs** — Plan filled and open positions by cost center with hire/term dating; normalize positions received from ATP.
- Delivery model: Any | Tool: Planning (+ Targetprocess) | Personas: Budget owners, HR, IT Finance | Cadence: Annual + continuous
- Inputs: Roster, approved position requests → Outputs: Position-level labor plan (open + filled)
- Config: Labor planning module, headcount targets, working calendar, position normalization from ATP feed (UC3)
- Framework: ITFM: headcount | SPM: WFM | Evidence: Planning docs; E2E BPMN t_norm

**05.4.2 Plan compensation & adjustments** — Model base compensation, merit/bonus/burden and monthly variable adjustments under restricted access.
- Delivery model: Any | Tool: Planning | Personas: IT Finance (restricted) | Cadence: Annual + on change
- Inputs: Comp data → Outputs: Labor cost plan
- Config: Compensation adjustments, variable workforce adjustments, field-level Restricted Access (sensitive salary)
- Framework: ITFM | Evidence: Planning docs

**05.4.3 Allocate planned labor** — Apply labor allocation rules so planned labor lands on cost centers, projects and TBM categories like actuals will.
- Delivery model: Any | Tool: Planning (+ Costing) | Personas: IT Finance, PMO | Cadence: Per plan cycle
- Inputs: Labor plan → Outputs: Allocated labor plan
- Config: Labor allocation rules, project labor activity (role-based), plan-side cost model
- Framework: ITFM | TBM taxonomy | Evidence: Planning docs


### 05.5 Vendor & Contract Planning

BPMN: [`diagrams/bpmn/generated/05.5.bpmn`](../diagrams/bpmn/generated/05.5.bpmn)

**05.5.1 Maintain contract line items** — Load and maintain contracts with terms, amortization approach and VAT.
- Delivery model: Any | Tool: Planning | Personas: IT Finance, Vendor Mgmt | Cadence: Continuous
- Inputs: Contract register → Outputs: Contract plan lines
- Config: Contract planning, amortization approaches, VAT handling
- Framework: ITFM: committed spend | Evidence: Planning docs

**05.5.2 Plan renewals & escalations** — Time renewals into the forecast with per-renewal compounding escalations; align forecast cadence to renewal periods.
- Delivery model: Any | Tool: Planning | Personas: Vendor Mgmt | Cadence: Per renewal cycle
- Inputs: Contract terms → Outputs: Renewal-aware forecast
- Config: Contract extensions/renewals with compounding % adjustments, renewal comments, auto-extension
- Framework: ITFM | Evidence: Planning docs; rolling-forecast step 2

**05.5.3 Delegate contract costs** — Delegate contract costs to the consuming budget owners' plans.
- Delivery model: Any | Tool: Planning | Personas: IT Finance | Cadence: Per plan cycle
- Inputs: Contract lines → Outputs: Delegated cost ownership
- Config: Contract cost delegation
- Framework: ITFM accountability | Evidence: Planning docs


### 05.6 Capital & Asset Planning

BPMN: [`diagrams/bpmn/generated/05.6.bpmn`](../diagrams/bpmn/generated/05.6.bpmn)

**05.6.1 Plan asset purchases & lifecycle** — Plan CapEx purchases, in-service dates and refresh; identify fully depreciated assets.
- Delivery model: Any | Tool: Planning (+ Costing) | Personas: Budget owners, Infrastructure | Cadence: Annual + quarterly
- Inputs: Asset register, refresh needs → Outputs: Asset purchase plan
- Config: Asset planning module, Fixed Asset Ledger linkage, refresh planning
- Framework: ITFM: CapEx | Evidence: Planning docs; ApptioOne CFD asset lifecycle

**05.6.2 Generate depreciation schedules** — Configure depreciation methods so planned CapEx flows into future-period OpEx correctly.
- Delivery model: Any | Tool: Planning | Personas: IT Finance | Cadence: Per plan cycle
- Inputs: Asset plan → Outputs: Depreciation schedule in plan
- Config: Depreciation methods configuration, Delegate Asset Costs
- Framework: ITFM | Evidence: Planning docs


### 05.7 Project & Investment Financial Planning

BPMN: [`diagrams/bpmn/generated/05.7.bpmn`](../diagrams/bpmn/generated/05.7.bpmn)

**05.7.1 Define investments & cost treatment** — Set up investments/projects with CapEx/OpEx (build vs run) treatment and permissions; tag budget lines to investments.
- Delivery model: Any | Tool: Planning (+ Costing) | Personas: PMO, IT Finance | Cadence: Per investment
- Inputs: Funded investments (from ATP) → Outputs: Investment financial structures
- Config: Integrated Investment Planning: investment tags on budget lines, Project Cost Type (build/run), Project Total & Charges KPIs, project permissions
- Framework: TBM: run/grow/transform | SPM: Financial Mgmt | Evidence: ApptioOne CFD IIP

**05.7.2 Plan investment labor & cross-charge** — Plan labor effort (hours/days/FTE) by role or named resource with rate cards; configure internal cross-charge to avoid double counting.
- Delivery model: Any | Tool: Planning (+ Targetprocess) | Personas: PMO, Resource Mgmt, IT Finance | Cadence: Per plan cycle
- Inputs: Labor demand from portfolio → Outputs: Investment labor plan
- Config: Labor resource planning (rates x effort), flexible rate cards, configurable cross-charge, demand vs capacity balancing
- Framework: ITFM | SPM: WFM | Evidence: ApptioOne CFD IIP

**05.7.3 Operate the investment loop with ATP** — Exchange approved budgets and budget-change requests with Targetprocess; receive planned allocations and actual effort back.
- Delivery model: Any | Tool: Planning (+ Targetprocess, Costing) | Personas: IT Finance, Portfolio Mgmt | Cadence: Continuous
- Inputs: Investments, allocations, actual effort (ATP) → Outputs: Approved budgets & changes (to ATP)
- Config: Bi-directional A1<->ATP integration (A1->ATP: approved investment budget, budget changes; ATP->A1: investments, planned labor allocations, actual labor effort, change requests)
- Framework: SPM+TBM integration | Evidence: ApptioOne CFD; Desjardins architecture


## L0-06 Cost Transparency & TBM Operations

*Run the monthly TBM engine: ingest actuals, allocate costs through cost pools and towers to applications, services and business units, cost labor defensibly, and analyze TCO.* Primary: **Costing**. Lanes: TBM Office/IT Finance; Costing Admin; App/Service Owners; ERP-GL.

Diagrams: [Mermaid](../diagrams/mermaid/area-06.md)


### 06.1 Monthly Cost Allocation & Close

BPMN: [`diagrams/bpmn/generated/06.1.bpmn`](../diagrams/bpmn/generated/06.1.bpmn)

**06.1.1 Load month-end actuals** — Ingest GL, payroll, fixed assets, vendor invoices and cloud bills for the closed period.
- Delivery model: Any | Tool: Costing (+ Cloudability, ERP/GL) | Personas: Costing Admin, TBM Analyst | Cadence: Monthly close
- Inputs: GL extract, subledgers, cloud bills → Outputs: Loaded period data
- Config: Datalink connectors & schedules, Cost Source master data tables, ULS uploads
- Framework: TBM: Data | Cost Transparency | Evidence: IBM Docs Costing; TBM assessment (Data)

**06.1.2 Refresh mappings & run allocations** — Update account/cost-center mappings and run the allocation model for the period through pools, towers, apps and BUs.
- Delivery model: Any | Tool: Costing | Personas: TBM Analyst | Cadence: Monthly
- Inputs: Loaded data, mapping tables → Outputs: Allocated cost model for period
- Config: Account mapping lookup tables, Cost Pool Reference List (ATUM), Model Studio allocation strategies (even/percent/weighted/consumption), allocation drivers
- Framework: TBM: taxonomy & model | Evidence: IBM Docs; ATUM

**06.1.3 Validate & reconcile to GL** — Validate allocations, analyze absorption (over/under allocation) and prove traceability back to the GL.
- Delivery model: Any | Tool: Costing | Personas: TBM Analyst, IT Finance | Cadence: Monthly
- Inputs: Allocated model → Outputs: Validated, reconciled model
- Config: Model validation, absorption analysis, GL traceability drill-through
- Framework: TBM: defensibility | Evidence: IBM community absorption analysis; LFM 'allocations = defensibility'

**06.1.4 Publish monthly TBM reporting** — Release the monthly IT financial reports and executive dashboards.
- Delivery model: Any | Tool: Costing | Personas: TBM Office, CIO org | Cadence: Monthly
- Inputs: Validated model → Outputs: Published dashboards/reports
- Config: IT Financial Reports, Apptio BI, report subscriptions, CT Leadership Review
- Framework: TBM: Reporting & Metrics | Evidence: IBM Docs; LFM demo


### 06.2 Cost Analysis & Variance (Actuals)

BPMN: [`diagrams/bpmn/generated/06.2.bpmn`](../diagrams/bpmn/generated/06.2.bpmn)

**06.2.1 Analyze spend by cost pool & tower** — Slice actuals by cost pool/sub-pool, tower/sub-tower, OpEx/CapEx, fixed/variable, discretionary for insight and unit costs.
- Delivery model: Any | Tool: Costing | Personas: TBM Analyst, IT Finance | Cadence: Monthly
- Inputs: Allocated model → Outputs: Spend insights, unit costs
- Config: Cost pool & tower reports, Cost Source fields (Is Depr, Fixed Variable, Discretionary), tower unit costs
- Framework: TBM: Cost for Performance | Evidence: IBM Docs; TBM taxonomy

**06.2.2 Track budget vs actuals in the model** — Compare actuals against budget/forecast at cost pool level monthly, baselined to original budget and reforecasts.
- Delivery model: Any | Tool: Costing (+ Planning) | Personas: IT Finance | Cadence: Monthly
- Inputs: Budget (Planning), actuals → Outputs: Variance reporting
- Config: Budget dataset integration, variance reports, common data bus with Planning
- Framework: TBM: Reporting & Metrics | Evidence: TBM assessment; ApptioOne CFD


### 06.3 Application & Service TCO

BPMN: [`diagrams/bpmn/generated/06.3.bpmn`](../diagrams/bpmn/generated/06.3.bpmn)

**06.3.1 Maintain application & service inventory** — Keep the app/service catalog and metadata current (functional groupings, owners, strategic alignment), aligned to ATUM service taxonomy.
- Delivery model: Any | Tool: Costing (+ CMDB/APM) | Personas: App/Service owners, TBM Office | Cadence: Continuous
- Inputs: CMDB/APM data, catalog → Outputs: Governed app/service master data
- Config: Applications & Services module master data, service catalog, ATUM Service Taxonomy (Service Type>Category>Service>Offering)
- Framework: TBM: taxonomy Solutions layer | Evidence: IBM Docs; TBMC25 ATUM product catalog

**06.3.2 Allocate costs to applications & services** — Flow tower, labor and vendor costs to apps/services using consumption drivers (servers, storage, tickets, effort).
- Delivery model: Any | Tool: Costing | Personas: TBM Analyst | Cadence: Monthly
- Inputs: Tower costs, drivers → Outputs: App/service costs (fully burdened)
- Config: Tower->application allocation strategies, drivers (server counts, tickets, time/story points)
- Framework: TBM: Cost Transparency | Evidence: IBM Docs; ATUM model

**06.3.3 Report & act on App TCO** — Publish Application TCO with run vs change attribution; drive rationalization (duplicates, long tail) and addressable-spend decisions.
- Delivery model: Any | Tool: Costing (+ Targetprocess) | Personas: App owners, TBM Office, EA | Cadence: Monthly/quarterly
- Inputs: App costs, delivery data → Outputs: TCO reports, rationalization actions
- Config: Applications Overview / App TCO reports, run vs change attribution from work data (UC4), addressable vs committed spend, AppRat analysis
- Framework: TBM: Delivering Value | Evidence: E2E BPMN t_tco/t_run; ApptioOne Plus

**06.3.4 Compute service unit costs** — Calculate unit costs/unit economics for services to support pricing and benchmarking.
- Delivery model: Any | Tool: Costing | Personas: TBM Analyst | Cadence: Monthly/quarterly
- Inputs: Service costs, volumes → Outputs: Service unit costs
- Config: Service costing model, consumption metrics, Services NX Reports
- Framework: TBM: unit cost | FinOps: Unit Economics (intersect) | Evidence: IBM Docs; TBM assessment


### 06.4 Labor Costing & Capitalization

BPMN: [`diagrams/bpmn/generated/06.4.bpmn`](../diagrams/bpmn/generated/06.4.bpmn)

**06.4.1 Maintain protected rates & compute blended rates** — Keep individual rates protected inside Costing; compute blended team/ART/solution-train rates.
- Delivery model: Any | Tool: Costing | Personas: IT Finance, TBM Analyst | Cadence: Monthly/quarterly
- Inputs: HR comp data, org structure → Outputs: Blended rates by team/ART
- Config: ATP CM Rate Transform, protected rate tables, blending logic; rate-level exposure design decision (blended vs individual)
- Framework: TBM: labor | privacy | Evidence: E2E BPMN t_rates; e2e script UC2

**06.4.2 Publish blended rates to Targetprocess** — Send blended rates to ATP on cadence so portfolio can cost work without exposing compensation.
- Delivery model: Any | Tool: Costing (+ Targetprocess) | Personas: System (ADM) | Cadence: Regular cadence
- Inputs: Blended rates → Outputs: Rates available in ATP
- Config: ADM rate feed, rate cadence config; true-up pattern for blended-vs-actual reconciliation (design decision)
- Framework: Integration | Evidence: E2E BPMN t_send4; e2e script

**06.4.3 Ingest workforce & completed work data** — Receive involvements, job profiles, CapEx/OpEx mappings, tower mappings and completed work from ATP.
- Delivery model: Any | Tool: Costing (+ Targetprocess) | Personas: System (ADM), TBM Analyst | Cadence: Monthly
- Inputs: ATP workforce & work data → Outputs: Labor model inputs
- Config: ADM feed ATP->TBM Studio, involvement/profile/mapping datasets
- Framework: Integration | Evidence: E2E BPMN t_send3

**06.4.4 Compute monthly team cost & blended CapEx %** — Combine involvements, profiles and protected rates into monthly cost and a blended CapEx percentage per team.
- Delivery model: Any | Tool: Costing | Personas: TBM Analyst (automated) | Cadence: Monthly
- Inputs: Labor model inputs → Outputs: Team cost & CapEx % per team
- Config: TBM Studio computation, job profile CapEx/OpEx splits, involvement math
- Framework: TBM: labor capitalization | Evidence: E2E BPMN t_calc; e2e script UC1

**06.4.5 Allocate team costs to work or towers** — Allocate visible-backlog team costs to completed work (story points, weightage); allocate no-backlog teams (e.g. ServiceNow ops) to apps/towers by fixed capacity. Capitalization approaches span agile and traditional: Story Points, Story Count, Timesheet, or Project/Work Effort Unit.
- Delivery model: Hybrid | Tool: Costing (+ ServiceNow) | Personas: TBM Analyst | Cadence: Monthly
- Inputs: Team costs, completed work / capacity rules → Outputs: Work-attached & tower-attached labor costs
- Config: Story-point/weightage allocation, fixed-capacity rules (team->app/tower), one normalized model for both team kinds
- Framework: TBM: allocation principles | Evidence: E2E BPMN g_vis/t_work/t_tower; e2e script UC1

**06.4.6 Generate audit-ready capitalization actuals** — Produce the monthly SAP-ready file of actuals split CapEx/OpEx by user - accurate enough to deprecate time writing; validate fixed-bid/PS work against invoices.
- Delivery model: Any | Tool: Costing (+ SAP/ERP) | Personas: IT Finance, Accounting | Cadence: Monthly
- Inputs: Allocated labor costs → Outputs: SAP-ready CapEx/OpEx actuals file
- Config: SAP-ready extract format, audit documentation, contractor/PS normalization
- Framework: Compliance: software capitalization | Evidence: E2E BPMN t_sap; e2e script UC1 payoff


### 06.5 Vendor & Asset Cost Management

BPMN: [`diagrams/bpmn/generated/06.5.bpmn`](../diagrams/bpmn/generated/06.5.bpmn)

**06.5.1 Consolidate & analyze vendor spend** — Unify vendor spend across towers/apps/BUs; find duplicate services, consolidation and renewal opportunities, underspent contracts.
- Delivery model: Any | Tool: Costing | Personas: Vendor Mgmt, IT Finance | Cadence: Monthly/quarterly
- Inputs: AP/vendor invoices, contracts → Outputs: Vendor insights & actions
- Config: Vendors master data, vendor insights reports, contract/PO feeds
- Framework: TBM: vendor spend | Evidence: ApptioOne CFD; CIO Vendor Report

**06.5.2 Track assets & depreciation** — Maintain the fixed asset ledger and depreciation/amortization flows in the cost model.
- Delivery model: Any | Tool: Costing | Personas: IT Finance | Cadence: Monthly
- Inputs: Fixed asset schedule → Outputs: Asset cost & depreciation in model
- Config: Fixed Asset Ledger, Is Depr flag, depreciation flows
- Framework: ITFM/TBM | Evidence: IBM Docs


### 06.6 Benchmarking

BPMN: [`diagrams/bpmn/generated/06.6.bpmn`](../diagrams/bpmn/generated/06.6.bpmn)

**06.6.1 Prepare taxonomy-aligned benchmark data** — Ensure cost data aligns to ATUM/TBM taxonomy so peer comparison is valid.
- Delivery model: Any | Tool: Costing | Personas: TBM Office | Cadence: Annual/quarterly
- Inputs: Allocated model → Outputs: Benchmark-ready dataset
- Config: ATUM mappings, benchmarking data prep
- Framework: TBM: Benchmarking | Evidence: Apptio Benchmarking

**06.6.2 Compare vs peers & set targets** — Benchmark cost pools/towers against peer groups; identify variance drivers and set improvement targets (spend archetypes).
- Delivery model: Any | Tool: Costing | Personas: TBM Office, CIO | Cadence: Annual + refresh
- Inputs: Benchmark data, peer groups → Outputs: Benchmark insights & targets
- Config: Benchmarking Essentials/Standard, custom peer groups, box plots, IT Benchmarking Review, Spend Archetypes
- Framework: TBM: Benchmarking | FinOps: KPIs & Benchmarking | Evidence: IBM Docs; Benchmarking product


### 06.7 Investment Mix Analysis

BPMN: [`diagrams/bpmn/generated/06.7.bpmn`](../diagrams/bpmn/generated/06.7.bpmn)

**06.7.1 Classify & report run/grow/transform** — Classify spend run/grow/transform (build vs run) and report innovation-vs-run mix to steer investment conversations.
- Delivery model: Any | Tool: Costing (+ Planning, Targetprocess) | Personas: TBM Office, CIO, CFO | Cadence: Quarterly
- Inputs: Classified spend, project attributes → Outputs: Investment mix reporting
- Config: Run/grow/transform classification fields, Project Cost Type (build/run), Run-vs-Grow reports
- Framework: TBM: Investment in Innovation | Evidence: ApptioOne CFD; CIO dashboard App & Run-vs-Grow reports


## L0-07 Cloud Financial Management (FinOps)

*Operate the FinOps lifecycle - ingest and allocate multi-cloud and container spend, report it, respond to anomalies, optimize usage and rates, and plan cloud budgets and migrations.* Primary: **Cloudability**. Lanes: FinOps Practitioner; Engineering; Finance; Cloud vendors.

Diagrams: [Mermaid](../diagrams/mermaid/area-07.md)


### 07.1 Cloud Cost Data Foundation

BPMN: [`diagrams/bpmn/generated/07.1.bpmn`](../diagrams/bpmn/generated/07.1.bpmn)

**07.1.1 Connect cloud billing accounts** — Onboard AWS/Azure/GCP/OCI billing exports under vendor credentials.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps Practitioner, Cloud Eng | Cadence: Once + on change
- Inputs: Payer accounts, billing exports → Outputs: Normalized multi-cloud cost data
- Config: Vendor Credentials (AWS payer+CUR, Azure export, GCP BigQuery, OCI), amortization/cost-basis settings
- Framework: FinOps: Understand > Data Ingestion | Evidence: IBM Docs Cloudability

**07.1.2 Ingest custom & FOCUS data** — Bring non-native spend (SaaS, other platforms) in via FOCUS-compliant ingress.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps Practitioner | Cadence: On change
- Inputs: FOCUS 1.0/1.1 datasets → Outputs: Unified spend incl. non-cloud
- Config: FOCUS Ingress (S3/Blob/GCS + manifest), FOCUS validator
- Framework: FinOps: Data Ingestion | FOCUS | Evidence: IBM Docs FOCUS ingress

**07.1.3 Onboard container cost data** — Install cluster agents and configure shared-cluster allocation for Kubernetes/OpenShift to namespace/label level.
- Delivery model: Any | Tool: Cloudability | Personas: Platform Eng, FinOps | Cadence: Per cluster
- Inputs: Cluster metrics → Outputs: Container cost allocation
- Config: IBM FinOps Agent (Helm), cluster credentials, shared cluster cost allocation rules
- Framework: FinOps: Allocation (containers) | Evidence: IBM Docs container agent

**07.1.4 Validate & reprocess data** — Reconcile ingested cost vs invoices; reprocess history after mapping changes.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps Practitioner | Cadence: Monthly + on change
- Inputs: Ingested data → Outputs: Validated dataset
- Config: TrueCost Explorer reconciliation, Data Reprocess
- Framework: FinOps: Data Ingestion | Evidence: IBM Docs


### 07.2 Cloud Allocation & Tagging Governance

BPMN: [`diagrams/bpmn/generated/07.2.bpmn`](../diagrams/bpmn/generated/07.2.bpmn)

**07.2.1 Design business mappings & views** — Build rule-based business dimensions (cost center, app, product, environment) and scope views/account groups per audience.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps Practitioner | Cadence: Initial + on change
- Inputs: Org structures, tag data → Outputs: Allocation dimensions & scoped views
- Config: Business Mappings (match/value expressions), Business Metrics, Account Groups, Views
- Framework: FinOps: Allocation | Evidence: IBM Docs Business Mappings

**07.2.2 Govern tagging** — Define the tagging standard, monitor coverage, remediate untagged spend, enforce mandatory tags in CI/CD.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps, Engineering | Cadence: Continuous
- Inputs: Tag standard → Outputs: Tag hygiene & coverage
- Config: Tags & Labels config, Tag Explorer, untagged-cost reports, Governance mandatory tag enforcement (Terraform/GitHub preview)
- Framework: FinOps: Allocation | TBM: Data (tagging) | Evidence: IBM Docs; TBM assessment tagging

**07.2.3 Allocate shared costs** — Split shared platform costs to consumers via cost sharing and telemetry rules for showback/chargeback.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps Practitioner | Cadence: Monthly
- Inputs: Shared cost pools, telemetry → Outputs: Fully allocated cloud cost
- Config: Cost Sharing & Telemetry rules, CSV rule import/export
- Framework: FinOps: Allocation, Invoicing & Chargeback | Evidence: Cloudability cost sharing

**07.2.4 Map cloud spend to TBM taxonomy** — Apply ATUM dimensions and share cloud cost/capacity data into Costing for hybrid TCO.
- Delivery model: Any | Tool: Cloudability (+ Costing) | Personas: FinOps, TBM Office | Cadence: Monthly
- Inputs: Allocated cloud cost → Outputs: TBM-aligned cloud spend in cost model
- Config: ATUM Tower/Sub-Tower/Service dimensions, Cloudability->Costing data share
- Framework: FinOps: Intersecting (ITFM/TBM) | Evidence: IBM Docs ATUM dimensions; TBMC25 flow


### 07.3 Cloud Reporting & Unit Economics

BPMN: [`diagrams/bpmn/generated/07.3.bpmn`](../diagrams/bpmn/generated/07.3.bpmn)

**07.3.1 Operate dashboards & scheduled reports** — Maintain persona dashboards and scheduled reports for engineering, finance and leadership; include AI/GenAI spend.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps, all personas | Cadence: Continuous/monthly
- Inputs: Allocated cost data → Outputs: Self-service visibility
- Config: Dashboards & widgets, Reports (scheduled email), TrueCost Explorer, AI Services Dashboard, Views
- Framework: FinOps: Reporting & Analytics | Evidence: IBM Docs

**07.3.2 Benchmark efficiency** — Score teams/BUs against internal and peer benchmarks.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps, Leadership | Cadence: Monthly/quarterly
- Inputs: Cost & usage data → Outputs: Scorecards
- Config: Scorecards (peer & internal)
- Framework: FinOps: KPIs & Benchmarking | Evidence: IBM Docs

**07.3.3 Track unit economics** — Define and monitor cost-per-business-unit-of-value metrics (cost per customer/transaction).
- Delivery model: Any | Tool: Cloudability | Personas: FinOps, Product, Finance | Cadence: Monthly
- Inputs: Cost + business telemetry → Outputs: Unit cost trends
- Config: Business Metrics (<=5/account), telemetry joins, dashboards
- Framework: FinOps: Unit Economics | Evidence: IBM Docs Business Metrics


### 07.4 Anomaly Management

BPMN: [`diagrams/bpmn/generated/07.4.bpmn`](../diagrams/bpmn/generated/07.4.bpmn)

**07.4.1 Configure anomaly detection** — Set alert scopes, thresholds, recipients and channels for ML-based unusual-spend detection.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps Practitioner | Cadence: Initial + tuning
- Inputs: Views, thresholds → Outputs: Active anomaly alerting
- Config: Anomaly alerts (view scope, Total Cost/Unusual Spend thresholds, filters, email/PagerDuty)
- Framework: FinOps: Anomaly Management | Evidence: IBM Docs anomaly

**07.4.2 Triage, route & resolve anomalies** — Investigate anomalies, route to owning engineers via ticketing, track resolution and tune rules.
- Delivery model: Any | Tool: Cloudability (+ Jira/ServiceNow) | Personas: FinOps, Engineering | Cadence: Per event + weekly review
- Inputs: Anomaly alerts → Outputs: Resolved anomalies, tuned rules
- Config: Anomaly drill-down, TrueCost Explorer, bi-directional Jira/ServiceNow ticketing, alert history
- Framework: FinOps: Anomaly Management | Operate phase | Evidence: IBM Docs 2025 features


### 07.5 Usage & Rate Optimization

BPMN: [`diagrams/bpmn/generated/07.5.bpmn`](../diagrams/bpmn/generated/07.5.bpmn)

**07.5.1 Run the rightsizing cadence** — Review utilization-based recommendations, dispatch to owners, execute (or automate via Turbonomic in Premium) and measure realized savings.
- Delivery model: Any | Tool: Cloudability (+ Turbonomic, Jira) | Personas: FinOps, Engineering | Cadence: Weekly/monthly
- Inputs: Utilization data → Outputs: Actioned rightsizing, ROI
- Config: Rightsizing recommendations & Preferences (lookback, aggressiveness), Rightsizing ROI, Turbonomic action automation (Premium)
- Framework: FinOps: Usage Optimization | Evidence: IBM Docs; Premium announcement

**07.5.2 Eliminate waste & govern pre-deployment** — Find idle/unused resources; enforce cost policy and estimation before deployment in CI/CD.
- Delivery model: Any | Tool: Cloudability (+ Terraform/GitHub) | Personas: FinOps, Engineering | Cadence: Continuous
- Inputs: Utilization, IaC plans → Outputs: Waste removal, policy compliance
- Config: Utilization/idle reports, Cost Governance policies, pre-deployment cost estimation (preview)
- Framework: FinOps: Usage Optimization, Governance | Evidence: IBM Docs Governance preview

**07.5.3 Manage commitments (assisted)** — Assess RI/SP/CUD coverage, generate and approve purchase/exchange recommendations, track amortization.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps, Finance, Procurement | Cadence: Monthly/quarterly
- Inputs: Usage patterns → Outputs: Commitment purchases & coverage
- Config: Commitment Overview / Portfolio / Recommendations
- Framework: FinOps: Rate Optimization | Evidence: IBM Docs commitments

**07.5.4 Automate commitments (Savings Automation)** — Run commitment management on autopilot within guardrails (per-account/per-region), monitoring coverage (>90%) and savings-share billing.
- Delivery model: Any | Tool: Cloudability Savings Automation | Personas: FinOps admin (RateOptimizationFullAccess) | Cadence: Continuous (autopilot)
- Inputs: Payer spend, guardrails → Outputs: Automated RI/SP portfolio & savings
- Config: Guardrails (ingestion account selection, active-management toggles, advanced config), savings assessment, coverage monitoring
- Framework: FinOps: Rate Optimization (Run maturity) | Evidence: IBM Docs Savings Automation


### 07.6 Cloud Planning & Forecasting

BPMN: [`diagrams/bpmn/generated/07.6.bpmn`](../diagrams/bpmn/generated/07.6.bpmn)

**07.6.1 Manage cloud budgets** — Set budgets on views/BUs, monitor burn and alert on breach.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps, Finance, Eng leads | Cadence: Monthly
- Inputs: Forecasts, targets → Outputs: Budgets with alerts
- Config: Budgets on Views, breach alerts
- Framework: FinOps: Budgeting | Evidence: IBM Docs

**07.6.2 Forecast cloud spend** — Produce rolling AI-backed forecasts with driver dimensions; analyze variance.
- Delivery model: Any | Tool: Cloudability (+ Planning) | Personas: FinOps, Finance | Cadence: Monthly
- Inputs: Historical usage → Outputs: Rolling forecast & variance
- Config: Intelligent/Enhanced Forecasting (best-fit model, <=3 driver dims), dashboards
- Framework: FinOps: Forecasting | Evidence: IBM Docs 2025

**07.6.3 Plan migrations & new workloads** — Model future/migration workloads cross-cloud (vendor, region, lease type, commitment) and export cost estimates.
- Delivery model: Any | Tool: Cloudability | Personas: Cloud architects, FinOps | Cadence: Per initiative
- Inputs: Workload requirements → Outputs: Cross-cloud plan & estimates
- Config: Workload Planning: Workloads, Resources (VM/DB/storage/LB, bulk JSON/XLSX), Recommendations, Preferences
- Framework: FinOps: Planning & Estimating | Evidence: IBM Docs Workload Planning


### 07.7 Cloud Sustainability

BPMN: [`diagrams/bpmn/generated/07.7.bpmn`](../diagrams/bpmn/generated/07.7.bpmn)

**07.7.1 Report & act on sustainability** — Track carbon/GPU sustainability metrics and include them in optimization decisions.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps, Sustainability | Cadence: Monthly/quarterly
- Inputs: Usage & carbon metrics → Outputs: Sustainability reporting
- Config: Sustainability metrics (incl. Azure/OCI GPU), dashboards, scorecards
- Framework: FinOps: Sustainability | Evidence: IBM Docs 2025 (verify metric names)


## L0-08 Consumption, Chargeback & Value Management

*Turn transparency into accountability: showback and Bill of IT to business units, price services, shape demand, benchmark against peers, and run the executive value operating rhythm.* Primary: **Costing (Billing)**. Lanes: TBM Office; BU Owners; CIO/CFO; Service Owners.

Diagrams: [Mermaid](../diagrams/mermaid/area-08.md)


### 08.1 Showback & Bill of IT

BPMN: [`diagrams/bpmn/generated/08.1.bpmn`](../diagrams/bpmn/generated/08.1.bpmn)

**08.1.1 Allocate consumption to business units** — Allocate app/service (and cloud) costs to business units on consumption drivers for defensible showback.
- Delivery model: Any | Tool: Costing (+ Cloudability) | Personas: TBM Analyst | Cadence: Monthly
- Inputs: App/service costs, consumption drivers → Outputs: BU consumption costs
- Config: Business Units module, drivers (headcount, users, transactions, volume), Cloudability cost sharing results
- Framework: TBM: Cost Transparency>consumers | FinOps: Invoicing & Chargeback | Evidence: IBM Docs; ApptioOne Plus

**08.1.2 Publish showback / Bill of IT** — Deliver periodic Bill of IT statements per BU with traceability to sources.
- Delivery model: Any | Tool: Costing (Billing) | Personas: TBM Office, BU Owners | Cadence: Monthly
- Inputs: BU consumption costs → Outputs: Bill of IT statements
- Config: Billing product (Bill of IT reports), Business Units Report Collection, scheduled distribution
- Framework: TBM: Delivering Value | Evidence: Apptio Billing; TBM assessment (showback at service level)

**08.1.3 Price services & run chargeback** — Set strategic service prices, model what-if allocation changes, execute chargeback and manage over/under recovery.
- Delivery model: Any | Tool: Costing (Billing) | Personas: IT Finance, TBM Office | Cadence: Quarterly + annual pricing
- Inputs: Unit costs, pricing strategy → Outputs: Chargeback invoices, recovery position
- Config: Billing pricing, what-if scenario modeling, O/U recovery management
- Framework: TBM: Shaping Demand | FinOps: Invoicing & Chargeback | Evidence: Apptio Billing


### 08.2 Demand Shaping & BU Engagement

BPMN: [`diagrams/bpmn/generated/08.2.bpmn`](../diagrams/bpmn/generated/08.2.bpmn)

**08.2.1 Review costs with BU owners** — Run consumption conversations with business partners using cost driver insight to shape demand.
- Delivery model: Any | Tool: Costing (+ Cloudability) | Personas: TBM Office, BU Owners | Cadence: Monthly/quarterly
- Inputs: Bill of IT, drivers → Outputs: Demand decisions, behavior change
- Config: BU reports, cost driver drill-downs, per-employee spend views
- Framework: TBM: Shaping Demand, four value conversations | Evidence: TBM assessment (Engagement, Taxonomy)


### 08.3 Enterprise Business Management (EBM)

BPMN: [`diagrams/bpmn/generated/08.3.bpmn`](../diagrams/bpmn/generated/08.3.bpmn)

**08.3.1 Extend costing beyond IT** — Model total spend (tech + non-tech) to TCO of business processes, products and services; align digital KPIs to enterprise workflows.
- Delivery model: Any | Tool: Costing (EBM) | Personas: Enterprise Finance, TBM Office | Cadence: Quarterly+
- Inputs: Enterprise cost data → Outputs: Business process/product TCO
- Config: EBM Costing & Billing, EIW alignment, digital KPIs (unit cost, flow velocity, volumes)
- Framework: TBM->EBM evolution | Evidence: TBMC25 EBM section; ApptioOne CFD EBM


### 08.4 Executive Value Operating Rhythm

BPMN: [`diagrams/bpmn/generated/08.4.bpmn`](../diagrams/bpmn/generated/08.4.bpmn)

**08.4.1 Run the CIO monthly operations review** — Operate the monthly executive dashboard cycle: financial attainment, vendor, app run-vs-grow, cloud consumption and workforce analytics - actuals from Costing/ATP, plans from Planning.
- Delivery model: Any | Tool: All four (+ PowerBI) | Personas: CIO, TBM Office, FinOps focals, App/Platform owners | Cadence: Monthly
- Inputs: All product outputs → Outputs: Executive decisions & actions
- Config: CIO Monthly Operations Dashboard: IT Financial Attainment (CT + Planning), IT Vendor Report, App & Run-vs-Grow (APM+CT), Cloud Consumption (Cloudability), Workforce Analytics
- Framework: TBM: Reporting | SPM: Value Realization | Evidence: TBMC25 Client Zero dashboard


## L0-09 Cross-Tool End-to-End Flows

*The integrated 'data highway' processes that span two or more products: targets down, rates back, actuals in, TCO up - plus cloud-to-TBM and the investment loop.* Primary: **All four**. Lanes: IT Planning (Finance); Targetprocess/ATP; Costing/TBM Studio; Cloudability; ERP (SAP).

Diagrams: [Mermaid](../diagrams/mermaid/area-09.md)


### 09.1 UC3 - Portfolio Target Spend (targets down)

BPMN: [`diagrams/bpmn/generated/09.1.bpmn`](../diagrams/bpmn/generated/09.1.bpmn)

**09.1.1 Flow: Planning -> Targetprocess targets & positions** — Finance builds workforce plans and top-down target spend in Planning; targets ride ADM to ATP as budget artifacts; portfolio allocates teams to work, compares bottom-up demand to targets; position requests round-trip through approval back into the plan.
- Delivery model: Any | Tool: Planning + Targetprocess | Personas: Lanes: IT Planning (Finance) | ATP (Portfolio & Workforce) | Cadence: Planning cycle + daily/weekly sync
- Inputs: Corporate targets, roster → Outputs: Targets in ATP; budgeted open+filled positions; demand-vs-target reports
- Config: Steps: create workforce plan & targets > send targets (ADM) > create budget artifacts > position request > multi-level approval > send approved positions > normalize & budget > allocate teams to work > compare demand vs targets. See E2E Flows sheet for BPMN detail.
- Framework: SPM: Financial Mgmt + WFM | ITFM | Evidence: E2E BPMN UC3; e2e demo script


### 09.2 UC2 - Work Allocation Rates (rates back)

BPMN: [`diagrams/bpmn/generated/09.2.bpmn`](../diagrams/bpmn/generated/09.2.bpmn)

**09.2.1 Flow: Costing -> Targetprocess blended rates** — Costing maintains protected individual rates, computes blended team/ART rates and publishes them to ATP so work allocations can be costed without exposing compensation.
- Delivery model: Any | Tool: Costing + Targetprocess | Personas: Lanes: Costing (TBM Studio) | ATP | Cadence: Regular cadence
- Inputs: Protected rates, org structure → Outputs: Costed work allocations feeding budget cycle
- Config: Steps: maintain protected rates > compute blended rates > send to ATP (ADM) > cost work allocations. Design decisions: rate exposure level; blended-vs-actual true-up.
- Framework: TBM: labor | SPM: Financial Mgmt | Evidence: E2E BPMN UC2; e2e demo script


### 09.3 UC1 - Labor Capitalization (actuals in)

BPMN: [`diagrams/bpmn/generated/09.3.bpmn`](../diagrams/bpmn/generated/09.3.bpmn)

**09.3.1 Flow: Targetprocess -> Costing -> SAP actuals** — ATP sends involvements, job profiles, mappings and completed work to Costing; TBM Studio computes monthly team cost and blended CapEx %, allocates to work (story points) or towers (fixed capacity), and generates the SAP-ready CapEx/OpEx actuals file that deprecates time writing.
- Delivery model: Any | Tool: Targetprocess + Costing (+ SAP, ServiceNow) | Personas: Lanes: ATP | Costing | ERP | Cadence: Monthly
- Inputs: Workforce & completed work data → Outputs: SAP-ready CapEx/OpEx actuals by user
- Config: Steps: maintain involvements/profiles/mappings > send to TBM Studio (ADM) > compute team cost & CapEx % > visible-work? story-point allocation : fixed-capacity allocation > generate SAP file. Three ingredients: job profiles, involvements, protected rates.
- Framework: TBM: capitalization | Compliance | Evidence: E2E BPMN UC1; e2e demo script


### 09.4 UC4 - Cost Actuals to App TCO (TCO up)

BPMN: [`diagrams/bpmn/generated/09.4.bpmn`](../diagrams/bpmn/generated/09.4.bpmn)

**09.4.1 Flow: actuals roll up to Application TCO** — All cost actuals roll up to Application TCO; because labor arrives attached to work, run vs change attribution is driven by real delivery data.
- Delivery model: Any | Tool: Costing (+ Targetprocess) | Personas: Lanes: Costing | consumers of TCO | Cadence: Monthly
- Inputs: Allocated actuals incl. labor-on-work → Outputs: App TCO with run/change attribution
- Config: Steps: roll actuals to App TCO > attribute run vs change in TCO view. Anti-pattern: story-level Jira import into cost model.
- Framework: TBM: Delivering Value | Evidence: E2E BPMN UC4; e2e demo script


### 09.5 Cloud-to-TBM Flow

BPMN: [`diagrams/bpmn/generated/09.5.bpmn`](../diagrams/bpmn/generated/09.5.bpmn)

**09.5.1 Flow: Cloudability -> Costing hybrid TCO** — Cloud cost and capacity data flows from Cloudability into the Costing model (ATUM-aligned) so App TCO and BU consumption include cloud.
- Delivery model: Any | Tool: Cloudability + Costing | Personas: Lanes: Cloudability | Costing | Cadence: Monthly
- Inputs: Allocated cloud spend → Outputs: Hybrid App TCO, cloud in Bill of IT
- Config: ATUM dimensions in Cloudability, Cloudability->Costing data share, cloud cost pool mapping
- Framework: FinOps x TBM intersect | Evidence: TBMC25 suite map; Cloudability ATUM dims


### 09.6 Investment Loop

BPMN: [`diagrams/bpmn/generated/09.6.bpmn`](../diagrams/bpmn/generated/09.6.bpmn)

**09.6.1 Flow: ATP <-> Costing/Planning investment round-trip** — Investments, planned allocations and actual effort flow from ATP to Costing/Planning; approved budgets and budget changes flow back - continuous portfolio-finance reconciliation.
- Delivery model: Hybrid | Tool: Targetprocess + Costing/Planning | Personas: Lanes: ATP | Costing/Planning | Cadence: Continuous
- Inputs: Investments, allocations, effort; budgets → Outputs: Reconciled investment funding
- Config: IIP bi-directional integration (A1->ATP approved budgets/changes; ATP->A1 investments, planned allocations, actual effort, change requests); Desjardins flow labels (Budgets, Labor Data, Objectives, Guidance down; Progress, Actuals, Key Results up)
- Framework: SPM: Financial Mgmt | TBM: Plan & Govern | Evidence: ApptioOne CFD IIP; Desjardins architecture


## L0-10 Platform Configuration, Data & Administration

*The enabling processes: configure each product, operate the data pipelines and integrations, and run the TBM/FinOps/SPM practices that govern adoption and maturity.* Primary: **All four**. Lanes: Platform Admins; TBM Office; FinOps Team; SPM Governance; Integration Team.

Diagrams: [Mermaid](../diagrams/mermaid/area-10.md)


### 10.1 Targetprocess Configuration

BPMN: [`diagrams/bpmn/generated/10.1.bpmn`](../diagrams/bpmn/generated/10.1.bpmn)

**10.1.1 Design org, portfolio & team structure** — Configure portfolios/projects, teams, ARTs/groups and access model to mirror the operating model.
- Delivery model: Any | Tool: Targetprocess | Personas: ATP Admin, ATP Product Owner | Cadence: Implementation + evolution
- Inputs: Operating model → Outputs: Configured structure
- Config: Portfolios (Projects), Teams, ART/Groups, team-project assignment, user types, roles & per-process permissions, RBAC
- Framework: SPM journey: Initiate/Discover | Evidence: SPM journey map; TP guide

**10.1.2 Configure processes, workflows & fields** — Set entity workflows/states, terminology, custom & calculated fields and metrics per entity type.
- Delivery model: Any | Tool: Targetprocess | Personas: ATP Admin | Cadence: Implementation + change
- Inputs: Process design → Outputs: Configured processes
- Config: Process editor, entity states & per-state permissions, terminology renames, custom fields, calculated fields, Metrics engine
- Framework: Enabling | Evidence: TP guide

**10.1.3 Install & tailor Solution Library packages** — Deploy packaged solutions (SAFe, OKR, PI Planning, Demand & Capacity, Budgeting, Time Tracking, Scenario Planning, WFM) and tailor them.
- Delivery model: Any | Tool: Targetprocess | Personas: ATP Admin, consultants | Cadence: Per capability rollout
- Inputs: Capability roadmap → Outputs: Installed, tailored solutions
- Config: Solutions Library, solution components, extensions, versioning/upgradability
- Framework: Enabling | Evidence: TP Solutions Library; solution sheets

**10.1.4 Build views, dashboards & automation** — Create role-based views/boards/timelines, dashboards and automation/validation rules.
- Delivery model: Any | Tool: Targetprocess | Personas: ATP Admin | Cadence: Continuous
- Inputs: Audience needs → Outputs: Role-based UX & automations
- Config: Board/list/timeline views, view sharing, dashboards, automation rules (JS logic, webhooks), validation rules
- Framework: Enabling | Evidence: TP guide; Customer PowerUp

**10.1.5 Manage integrations & environments** — Configure Jira/ADO/ServiceNow/email/SSO integrations and promote configuration Sandbox > Pre-Prod > Prod.
- Delivery model: Any | Tool: Targetprocess (+ Jira, ADO, ServiceNow) | Personas: ATP Admin, Integration team | Cadence: Per integration + release
- Inputs: Integration requirements → Outputs: Working integrations, promoted config
- Config: Native connectors, REST API/webhooks, SSO/SAML, environment promotion (incl. validation & automation rules)
- Framework: Enabling | Evidence: Customer PowerUp (env promotion); TP integrations


### 10.2 Costing Configuration

BPMN: [`diagrams/bpmn/generated/10.2.bpmn`](../diagrams/bpmn/generated/10.2.bpmn)

**10.2.1 Implement the cost model** — Create the Costing project, configure master data, map GL to cost pools, build allocation strategies and reports.
- Delivery model: Any | Tool: Costing | Personas: Costing Admin, TBM consultants | Cadence: Implementation (10-12 wks) + evolution
- Inputs: GL, org & asset data → Outputs: Working TBM model
- Config: Costing Standard project, Cost Source/Labor/Fixed Asset/Vendors/Projects master data, Cost Pool Reference List, account mapping tables, Model Studio strategies, Report Studio/Apptio BI
- Framework: TBM Foundations | Evidence: IBM Docs; onboarding packages

**10.2.2 Operate data pipelines (Datalink)** — Onboard sources via Datalink connectors/agent, schedule loads, monitor and troubleshoot; validate data quality.
- Delivery model: Any | Tool: Costing (+ All sources) | Personas: Costing Admin, Integration team | Cadence: Continuous
- Inputs: Source systems → Outputs: Reliable automated feeds (5-15 sources)
- Config: Datalink app + Agent (Boomi), connectors (REST, SAP, ServiceNow...), ULS, schedules, Data Studio transforms & quality checks
- Framework: TBM: Automation dimension | Evidence: IBM Docs Datalink; TBM assessment


### 10.3 Planning Configuration

BPMN: [`diagrams/bpmn/generated/10.3.bpmn`](../diagrams/bpmn/generated/10.3.bpmn)

**10.3.1 Configure planning structures** — Set reference data/hierarchies, line items, GL-to-IT mappings, calendars, currencies, permissions and restricted fields.
- Delivery model: Any | Tool: Planning | Personas: Planning Admin | Cadence: Implementation (~4 wks) + evolution
- Inputs: Finance structures → Outputs: Configured planning environment
- Config: Reference data/schemas/custom lists, line-item config, working calendar, multi-currency, cost object permissions, Restricted Access dims
- Framework: Enabling | Evidence: Planning docs

**10.3.2 Configure workflow & integrations** — Set approval workflows, plan lifecycle, and integrations (Costing actuals, Cloudability, Planning Analytics, APIs).
- Delivery model: Any | Tool: Planning (+ Costing, Cloudability) | Personas: Planning Admin | Cadence: Implementation + change
- Inputs: Governance design → Outputs: Working workflow & feeds
- Config: Approval workflow config, plan states, Costing/Cloudability/Planning Analytics connectors, REST APIs
- Framework: Enabling | Evidence: Planning docs


### 10.4 Cloudability Configuration

BPMN: [`diagrams/bpmn/generated/10.4.bpmn`](../diagrams/bpmn/generated/10.4.bpmn)

**10.4.1 Configure FinOps tooling** — Set credentials, mappings/metrics, views, budgets, anomaly rules, rightsizing preferences, guardrails, container agents and governance policies.
- Delivery model: Any | Tool: Cloudability | Personas: FinOps Admin | Cadence: Implementation + tuning
- Inputs: Cloud estate, org model → Outputs: Configured FinOps platform
- Config: 13-item checklist: vendor credentials, Business Mappings/Metrics, tags/account groups/views, cost sharing rules, dashboards/reports/scorecards, budgets & forecast settings, anomaly rules, rightsizing prefs, commitment/SA guardrails, container agents, governance policies, workload planning prefs, users/roles + ATUM dims
- Framework: FinOps: Manage the Practice | Evidence: Cloudability research checklist


### 10.5 Cross-Product Data & Integration Operations

BPMN: [`diagrams/bpmn/generated/10.5.bpmn`](../diagrams/bpmn/generated/10.5.bpmn)

**10.5.1 Operate the ADM data highway** — Run and monitor the cross-product feeds (targets, positions, rates, workforce/work data, cloud cost, investment loop) at their cadences.
- Delivery model: Any | Tool: All four (+ ADM/Datalink) | Personas: Integration team, Platform admins | Cadence: Daily-monthly by feed
- Inputs: Product data → Outputs: Reliable cross-tool flows
- Config: ADM/data highway feeds & cadences (positions daily/weekly, rates regular, work data monthly, roster daily-monthly by source), monitoring & error handling
- Framework: Enabling all L0-09 flows | Evidence: E2E BPMN; TBMC25 sync cadences

**10.5.2 Govern master data & taxonomy** — Own shared reference data: ATUM taxonomy versions, service/product catalog, cost centers, tags, naming conventions and cross-reference tables.
- Delivery model: Any | Tool: All four | Personas: TBM Office, Data governance | Cadence: Quarterly + on change
- Inputs: Source-of-truth systems → Outputs: Consistent shared taxonomy
- Config: ATUM taxonomy layers, service catalog as product catalog, tag dictionaries, cross-reference tables, referential integrity checks
- Framework: TBM: Data & Taxonomy dimensions | Evidence: TBM assessment; TBMC25 ATUM catalog


### 10.6 Practice Operations & Maturity

BPMN: [`diagrams/bpmn/generated/10.6.bpmn`](../diagrams/bpmn/generated/10.6.bpmn)

**10.6.1 Run the TBM office** — Operate TBM governance: roles (sponsor, practice lead, analyst, admin, change manager), stakeholder engagement, program roadmap.
- Delivery model: Any | Tool: Costing (practice) | Personas: TBM Office | Cadence: Continuous
- Inputs: Executive sponsorship → Outputs: Sustained TBM practice
- Config: TBM office roles, governance forums, OCM & training, procurement/vendor alignment
- Framework: TBM Foundations & Engagement | Evidence: TBM Council; TBM assessment

**10.6.2 Run the FinOps practice** — Operate the FinOps team: policies, education, persona enablement, intersecting disciplines (Security, ITAM, ITSM, Procurement).
- Delivery model: Any | Tool: Cloudability (practice) | Personas: FinOps team | Cadence: Continuous
- Inputs: Cloud operating model → Outputs: Sustained FinOps practice
- Config: FinOps roles/personas, governance policies, training, Crawl/Walk/Run capability plans
- Framework: FinOps: Manage the FinOps Practice | Evidence: FinOps Framework; FinOps assessment

**10.6.3 Run SPM governance & transformation** — Operate SPM governance and the maturity journey (Initiate>Discover>Accelerate>Scale & Evolve); assess maturity and transition to customer governance.
- Delivery model: Any | Tool: Targetprocess (practice) | Personas: SPM governance, LACE, Transformation office | Cadence: Quarterly + phases
- Inputs: Maturity assessments → Outputs: Advancing SPM maturity
- Config: SPM maturity model (6 domains x lenses, Foundational>Scaled), journey map tracks, governance cadences, domain owners
- Framework: SPM maturity model | Evidence: SPM Maturity Assessment; SPM journey map

**10.6.4 Assess maturity & set roadmap** — Run periodic TBM / FinOps / SPM maturity assessments, score against target state and prioritize the capability roadmap.
- Delivery model: Any | Tool: All four | Personas: TBM Office, FinOps, SPM governance | Cadence: Annual/semi-annual
- Inputs: Assessment instruments → Outputs: Scores, gaps, roadmap
- Config: TBM 6-dimension assessment (0-5), FinOps 4-domain Crawl/Walk/Run, SPM 6-domain x lens assessment (1-5), roadmap planning
- Framework: All three frameworks | Evidence: TBM/FinOps/SPM assessment instruments (Metlife examples)
