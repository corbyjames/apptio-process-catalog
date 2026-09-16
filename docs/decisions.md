# Design decisions register · v0.7.0

Generated from `data/catalog.json` (`decisions[]`, `variants[]`, `applies_when`, flow-step `when`) — **edit the JSON, not this file.** 11 decisions · 36 options · 69 variants on 21 processes · 14 conditional processes.

A *decision* is a choice a customer makes once (usually in discovery) that ripples through several processes and flows — for example whether labor cost is derived from story points or from timesheets. Each decision lists its options with fit, prerequisites and trade-offs, and the processes it shapes. A process that is done differently under each option carries a **variant** per option (fields on the variant override the base record; everything else is common). A process that only exists under some options carries an **applies-when** condition, as do flow steps. On the site, `#/decisions` is also the customer-profile picker: choosing options renders the whole catalog for that customer.


## D-01 Labor effort signal

**How is labor effort captured and attached to work so it can be costed, capitalized and rolled into App TCO?**

Drives which Targetprocess entities carry effort, what crosses the ADM feed to Costing, how team cost is spread over work and towers, and what the auditors see behind the CapEx file. Most customers mix approaches by team kind (e.g. story points for product teams, fixed capacity for ops queues), so this decision is normally made per team type.

Domain: Labor costing & capitalization · pick one or more · default: **Cost per story point** · flows: UC1 · related: D-02 Labor rate exposure, D-07 Capacity planning basis

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Cost per story point** (default) `story-points` | Monthly team cost divided by story points completed gives a cost per point; cost lands on epics, features and applications in proportion to the points delivered against them. Effort is never typed in - it comes from the backlog. | Agile teams with a visible, well-groomed backlog in Targetprocess or a synced Jira/ADO. The Apptio reference pattern ('deprecates time writing'). | Involvements % (04.1.2), job profiles with CapEx/OpEx split (04.1.3), protected rates (06.4.1), completed-work feed to Costing (UC1), a capitalization policy signed off with Finance/audit. | Points are only comparable within a team - always normalize per team, never enterprise-wide. Un-estimated or carried-over work distorts the month. Needs backlog hygiene and a documented policy for auditors. | E2E BPMN g_vis/t_work; e2e script UC1 |
| **Cost per completed work item** `story-count` | Same mechanism as story points but every completed story/work item weighs the same. Team cost divided by items done. | Kanban / no-estimates teams, support and enhancement teams whose items are of similar size. | As story points, minus estimation discipline. | A one-line fix and a two-week story cost the same; acceptable only where item sizes are homogeneous. | Costing labor allocation options (06.4.5 config) |
| **Timesheets (hours x rate)** `timesheet` | People log hours against work items or projects in the Time entity; managers approve weekly; approved hours x rate is the labor cost attached to work and the basis for CapEx. | Traditional and hybrid delivery, professional-services and contractor billing, regulated environments that require hours as the capitalization evidence, or where Finance already runs a timesheet regime. | Time Tracking solution + Timesheet approval workflow (04.5.1-04.5.2), rate source (job-profile or blended rate), timesheet compliance reporting. | Highest burden and the classic accuracy decay (end-of-week estimates, 'other' buckets). Needs chasing and compliance metrics. Strongest audit trail. | TP Time Tracking; 2026.03 Timesheet with Approval Workflow solution sheet |
| **Planned work-effort units (allocation-based)** `work-effort-unit` | Work Allocations (% or man-days per person/team per period) are treated as the effort signal; no hours are recorded. Cost = allocation x rate, trued up periodically against actual completion. | Hybrid organizations that plan resourcing carefully but will not run timesheets; project-based funding where the plan is the contract. | Demand & Capacity solution with Work Allocations (04.3.1 / 04.3.4), a true-up rule (quarterly or at project close), blended rates (UC2). | Planned is not actual - variance hides until true-up. Weaker capitalization evidence than hours; usually paired with a sign-off step. | LFM demo (requested man-days); WFM deck |
| **Fixed capacity (team to tower/app)** `fixed-capacity` | No work-level attribution at all: the team's monthly cost is allocated to applications or IT towers by a standing rule (team->tower mapping, % splits). | Run/operations teams without a visible backlog (ServiceNow queues, infrastructure ops, service desk), platform teams charged as shared services. | Team->IT tower / application mapping (04.1.3), allocation strategy in Model Studio (06.1.2). | No run-vs-change split from data; capitalization only via a fixed % if policy allows. Simplest to operate. | E2E BPMN t_tower; e2e script (ServiceNow example) |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 04.1.3 | Maintain job profiles & financial mappings | affected (no variant text yet) |
| 04.5.1 | Capture effort against work | 5 variants: Cost per story point, Cost per completed work item, Timesheets (hours x rate), Planned work-effort units (allocation-based), Fixed capacity (team to tower/app) |
| 04.5.2 | Approve timesheets | 1 variants: Timesheets (hours x rate) |
| 04.5.3 | Feed time/effort to finance processes | 5 variants: Cost per story point, Cost per completed work item, Timesheets (hours x rate), Planned work-effort units (allocation-based), Fixed capacity (team to tower/app) |
| 06.4.3 | Ingest workforce & completed work data | 5 variants: Cost per story point, Cost per completed work item, Timesheets (hours x rate), Planned work-effort units (allocation-based), Fixed capacity (team to tower/app) |
| 06.4.5 | Allocate team costs to work or towers | 5 variants: Cost per story point, Cost per completed work item, Timesheets (hours x rate), Planned work-effort units (allocation-based), Fixed capacity (team to tower/app) |
| 06.4.6 | Generate audit-ready capitalization actuals | 4 variants: Cost per story point, Timesheets (hours x rate), Planned work-effort units (allocation-based), Fixed capacity (team to tower/app) |

Flow steps: UC1 step 17 (gateway); UC1 step 17a (only when Cost per story point / Cost per completed work item / Timesheets (hours x rate) / Planned work-effort units (allocation-based)); UC1 step 17b (only when Fixed capacity (team to tower/app))

## D-02 Labor rate exposure

**Which labor rate is allowed to leave Costing and be used in Targetprocess to cost work?**

Individual compensation is sensitive; the level at which rates are blended sets who can see what, how accurate costed allocations are, and whether a true-up is needed between the rate used in the portfolio and actuals in Costing.

Domain: Labor costing & capitalization · pick one · default: **Blended team / ART rate** · flows: UC2 · related: D-01 Labor effort signal

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Blended team / ART rate** (default) `blended-team` | Costing computes one blended rate per team, ART or solution train from protected individual rates and publishes only that. Portfolio costs work at the team rate. | Most enterprises; the Apptio reference pattern. | Team structure with involvements (04.1.2), ATP CM Rate Transform (06.4.1), ADM rate feed (06.4.2). | Costed allocations drift from actuals when team mix changes - define a true-up (monthly or quarterly). | E2E BPMN t_rates/t_send4; e2e script UC2 |
| **Job-profile rate (role x location)** `role-location` | Standard rate card per job profile (role x location, optionally employment type) published to Targetprocess; individuals inherit their profile's rate. | Organizations with a mature rate card, project-based estimating, PS/contractor mixes, or where teams are too fluid to blend. | Job Profile entities with rate linkage (04.1.3), rate card governance (annual refresh). | More granular than a team rate and still non-identifying, but a rate card needs owning and refreshing. | E2E BPMN t_data; Planning labor rate cards (05.7.2) |
| **Individual (actual) rates** `individual` | Actual loaded cost per person leaves Costing and is used to cost allocations and time. | Small IT organizations, PS firms, or where Finance already exposes comp to project accounting. | Restricted-access roles in Targetprocess, HR/works-council approval, field-level permissions. | Most accurate, but exposes compensation in a delivery tool; usually blocked by HR/privacy. Not the default. | 06.4.1 rate-exposure design decision |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 04.1.3 | Maintain job profiles & financial mappings | 2 variants: Blended team / ART rate, Job-profile rate (role x location) |
| 06.4.1 | Maintain protected rates & compute blended rates | 3 variants: Blended team / ART rate, Job-profile rate (role x location), Individual (actual) rates |
| 06.4.2 | Publish blended rates to Targetprocess | 3 variants: Blended team / ART rate, Job-profile rate (role x location), Individual (actual) rates |
| 04.3.1 | Allocate people & teams to work | affected (no variant text yet) |
| 02.4.3 | Track portfolio budget vs actuals | affected (no variant text yet) |

## D-03 Budget build method

**How is the IT budget built for a given decision unit and cycle?**

Sets whether 05.1 or 05.8 is the path for a cost center, tower, service or application, how the baseline is seeded, and whether the ZBB flow runs. Selectable per decision unit and per cycle - a rotation is the normal pattern.

Domain: IT financial planning · pick one or more · default: **Driver-based** · flows: ZBB · related: D-04 Portfolio funding model

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Incremental** `incremental` | Prior-year budget or actuals seeded as the baseline, adjusted line by line for known changes. | Stable run units between ZBB rotations; low-effort cycles. | Prior plan / actuals import (05.1.1). | Carries last year's inefficiencies forward; weakest challenge of the run base. | Planning docs (Adjust Baseline Values) |
| **Driver-based** (default) `driver-based` | Lines are built from drivers (headcount, contracts, assets, volumes) with rates; the baseline is regenerated from drivers rather than copied. | The default for most units; pairs with rolling forecasting (05.2). | Driver data (positions, contracts, asset register), driver-based line items in Planning. | Needs clean driver feeds; still anchored on current activity levels. | Planning docs; Apptio rolling-forecast method |
| **Zero-based - rotational** `zbb-rotational` | A subset of decision units is rebuilt from a zero base each cycle (each unit every 2-3 years); the rest run driver-based. Decision packages at Minimum / Current / Enhanced tiers, ranked to a cut-line. | Organizations that want the challenge of ZBB without the annual burden. The catalog's primary ZBB variant. | Group 05.8, cost-category owners, TBM fact base (06.x), rotation calendar (10.6.1). | Two budgeting paths in one cycle; needs the merge step 05.8.5. | Gartner; McKinsey; Apptio ZBB blog |
| **Zero-based - all units annually** `zbb-full` | Classic ZBB: every decision unit justified from zero every year. | Turnaround / cost-out programs with executive mandate. | As rotational, at full scale; FP&A facilitation capacity. | The historical failure mode (burden, sandbagging); rarely sustained beyond 2-3 cycles. | Pyhrr; Kraft Heinz / federal cases |
| **Zero-based mindset (continuous)** `zbx` | No annual ZBB event; cost-category owners run a continuous zero-based review inside the monthly rhythm (05.8.6 as an operating cadence). | Organizations past their first ZBB cycles that want to keep the discipline without the event. | Monthly variance with package-level thresholds (05.3.2 / 06.2.2), owner community. | Depends on culture and incentives; without the event the challenge can fade. | Accenture ZBx; FinOps Budgeting (Run maturity) |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 05.1.1 | Establish plan structure & baseline | 4 variants: Incremental, Driver-based, Zero-based - rotational, Zero-based - all units annually |
| 05.1.3 | Enter bottom-up budgets | 4 variants: Incremental, Driver-based, Zero-based - rotational, Zero-based - all units annually |
| 05.1.4 | Review, iterate & approve budget | affected (no variant text yet) |
| 05.1.5 | Finalize budget of record | affected (no variant text yet) |
| 05.8.1 | Scope the ZBB cycle & select decision units | 3 variants: Zero-based - rotational, Zero-based - all units annually, Zero-based mindset (continuous) |
| 05.8.2 | Build the cost-driver fact base & activity inventory | only when Budget build method: Zero-based - rotational / Zero-based - all units annually / Zero-based mindset (continuous) |
| 05.8.3 | Build decision packages at tiered service levels | only when Budget build method: Zero-based - rotational / Zero-based - all units annually |
| 05.8.4 | Rank packages & set the funding cut-line | only when Budget build method: Zero-based - rotational / Zero-based - all units annually |
| 05.8.5 | Approve zero-based budget & release freed spend to the investment envelope | only when Budget build method: Zero-based - rotational / Zero-based - all units annually |
| 05.8.6 | Monitor package commitments & sustain the zero-based mindset | 2 variants: Zero-based - rotational, Zero-based mindset (continuous) |
| 07.6.1 | Manage cloud budgets | affected (no variant text yet) |

Flow steps: ZBB step z0 (only when Zero-based - rotational / Zero-based - all units annually); ZBB step z1 (only when Zero-based - rotational / Zero-based - all units annually); ZBB step z4 (only when Zero-based - rotational / Zero-based - all units annually); ZBB step z5 (only when Zero-based - rotational / Zero-based - all units annually); ZBB step z6 (only when Zero-based - rotational / Zero-based - all units annually); ZBB step z7 (only when Zero-based - rotational / Zero-based - all units annually); ZBB step z8 (only when Zero-based - rotational / Zero-based - all units annually); ZBB step z9 (only when Zero-based - rotational / Zero-based - all units annually)

## D-04 Portfolio funding model

**Is change work funded per project, per value stream/product, or both during a transition?**

Decides the shape of the Budgeting solution in Targetprocess, whether budgets attach to Projects or to Portfolios/ARTs, what the investment loop with Planning carries, and how top-down targets are applied.

Domain: Demand & portfolio investment · pick one · default: **Hybrid (both, side by side)** · flows: INV, UC3 · related: D-05 Investment approval governance, D-03 Budget build method

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Project-based funding** `project-based` | Money is approved per project/initiative with a business case and a defined scope; actuals are tracked per project. | Traditional and regulated PMOs, capital-project cultures, organizations early on the SPM journey. | Project entities with budgets, stage-gate governance (D-05), investment tags in Planning (05.7.1). | Re-planning is slow; funding follows projects rather than capacity; encourages large batches. | EAP CFD (annual -> continuous); TP Budgeting |
| **Value-stream / product funding (Lean Budgets)** `value-stream` | Capacity is funded per value stream, ART or product with guardrails; epics are approved inside the envelope, not funded individually. | SAFe / LPM organizations, product operating models. | Value streams as Portfolios/Groups (03.4.1), Lean Budget guardrails (02.4.1), participatory budgeting forums. | Finance must accept capacity-based accounting; capitalization moves to the labor model (D-01). | SAFe Lean Budgets; TP Budgeting solution |
| **Hybrid (both, side by side)** (default) `hybrid` | Project-based and value-stream funding coexist - typically during a multi-year transition or where some domains stay project-shaped. | Most large enterprises today. | Common categorization (BAU vs change, CapEx/OpEx) across both (02.3.4), Hybrid Portfolio Management solution. | Two governance paths to keep consistent; reporting must reconcile both. | WFM deck (hybrid programs); Customer PowerUp |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 02.4.1 | Define funding model | 3 variants: Project-based funding, Value-stream / product funding (Lean Budgets), Hybrid (both, side by side) |
| 02.4.2 | Receive & apply top-down targets | affected (no variant text yet) |
| 02.2.3 | Approve & fund investments | affected (no variant text yet) |
| 05.7.1 | Define investments & cost treatment | affected (no variant text yet) |
| 05.7.2 | Plan investment labor & cross-charge | affected (no variant text yet) |
| 05.7.3 | Operate the investment loop with ATP | affected (no variant text yet) |

## D-05 Investment approval governance

**How does an investment get approved - phase gates, lean portfolio flow, or both?**

Shapes entity workflows and per-state permissions in Targetprocess, which forums decide, and whether Portfolio Kanban states or gate reviews are the control points.

Domain: Demand & portfolio investment · pick one · default: **Hybrid** · flows: INV · related: D-04 Portfolio funding model, D-06 Prioritization method

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Stage-gate** `stage-gate` | Initiatives pass formal gates (concept, business case, design, build, deploy) with documented approvals and criteria at each. | Traditional PMOs, regulated change, capital projects. | Entity states as gates with role permissions, milestone entities, gate evidence fields (03.3.3). | Predictable control, slow flow; encourages big up-front business cases. | Traditional PM solution; stage-gate research |
| **Lean portfolio flow (Portfolio Kanban)** `lean-lpm` | Epics move Funnel > Reviewing > Analyzing > Backlog > Implementing with WIP limits; approval is the move to Backlog within the value-stream guardrails. | SAFe / LPM organizations with value-stream funding. | Portfolio Epic workflow, WSJF or scoring (D-06), Lean Budgets (D-04). | Needs trust in guardrails; auditors may want an explicit approval artifact. | SAFe LPM; TP entity workflows (02.1.3) |
| **Hybrid** (default) `hybrid` | Gates for large/regulated initiatives, lean flow for value-stream work - one governed portfolio view over both. | Enterprises running agile and traditional delivery together. | Hybrid Portfolio Management solution, common categorization (02.3.4). | Clear rules needed for which path an item takes. | WFM deck; Customer PowerUp (hybrid) |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 02.1.3 | Progress demand through Portfolio Kanban | only when Investment approval governance: Lean portfolio flow (Portfolio Kanban) / Hybrid |
| 02.2.3 | Approve & fund investments | 3 variants: Stage-gate, Lean portfolio flow (Portfolio Kanban), Hybrid |
| 03.3.3 | Govern stage-gates & milestones for traditional initiatives | only when Investment approval governance: Stage-gate / Hybrid |

## D-06 Prioritization method

**How is the portfolio backlog ranked?**

Determines which custom and calculated fields exist on epics, what the ranking views show and how ZBB packages are ranked when 05.8 runs.

Domain: Demand & portfolio investment · pick one · default: **WSJF** · related: D-05 Investment approval governance

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **WSJF** (default) `wsjf` | Cost of delay (business value + time criticality + risk reduction/opportunity enablement) divided by job size, as a calculated field. | SAFe organizations; fast, relative ranking. | Numeric custom fields BV/TC/RR-OE/size, calculated field or metric, prioritized list views (02.2.2). | Relative, gameable, weak for compliance/mandatory work. | SAFe WSJF; TP calculated fields |
| **Weighted objective scoring** `weighted-scoring` | Configurable criteria (strategic alignment, value, risk, cost, compliance) with weights; a score per item; often per portfolio. | Hybrid and traditional portfolios; organizations that must show a defensible model to a board. | Scoring custom fields, Portfolio Epic Score report, objective-scoring configuration. | Weights need governance; can become a spreadsheet exercise. | WFM deck prioritization; TP Portfolio Epic Score |
| **Manual / forum ranking** `manual` | A governance forum ranks items by hand (drag-order or rank field) informed by business cases. | Small portfolios, early maturity. | Rank/order field, prioritized list views. | Opaque; depends on who is in the room. | SPM maturity model (Foundational) |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 02.2.2 | Prioritize the portfolio backlog | 3 variants: WSJF, Weighted objective scoring, Manual / forum ranking |
| 05.8.4 | Rank packages & set the funding cut-line | affected (no variant text yet) |

## D-07 Capacity planning basis

**Is capacity planned and allocated per team, per role/named individual, or both?**

Decides whether Work Allocations attach to teams or people, how demand is expressed (team % vs role man-days) and which capacity views and reports are configured.

Domain: Workforce & resource management · pick one · default: **Both (one capacity model)** · flows: UC3 · related: D-01 Labor effort signal

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Team-based** `team-based` | Long-lived teams are the unit of capacity; work is allocated to teams and ARTs by % or PI capacity. | Agile at scale; value-stream funding. | Team entities with involvements (04.1.2), team allocation views. | Named-resource requests (specialists) have no home. | E2E BPMN t_alloc; SAFe capacity |
| **Role / individual-based** `role-individual` | Demand is expressed as roles and man-days; named individuals are assigned to projects with availability checks. | Project-based PMOs, PS organizations, shared specialist pools. | Role-based demand requests, Work Allocations at person level, availability / vacation integration (04.3.4). | Heavier to maintain; utilization chasing. | LFM demo (requested man-days) |
| **Both (one capacity model)** (default) `both` | Team-based for agile work and role/individual-based for project work in the same capacity model. | Hybrid organizations - the common case. | Both configurations plus a rule for which work type uses which. | Double-counting risk where a person is both in a team and on a project - involvements must sum to 100%. | WFM deck; 04.2.1 / 04.3.4 |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 04.2.1 | Map & forecast capacity | 3 variants: Team-based, Role / individual-based, Both (one capacity model) |
| 04.2.2 | Balance demand vs capacity | affected (no variant text yet) |
| 04.3.1 | Allocate people & teams to work | 3 variants: Team-based, Role / individual-based, Both (one capacity model) |
| 04.3.4 | Assign individuals & roles to project work (hybrid resourcing) | only when Capacity planning basis: Role / individual-based / Both (one capacity model) |
| 05.7.2 | Plan investment labor & cross-charge | affected (no variant text yet) |

## D-08 Demand intake channel

**Where do ideas and requests enter - the Targetprocess Service Desk, a ServiceNow front end, or email/forms?**

Sets which portal is configured, whether an integration is needed, and where triage happens.

Domain: Demand & portfolio investment · pick one or more · default: **Targetprocess Service Desk portal**

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Targetprocess Service Desk portal** (default) `tp-service-desk` | Requesters use the built-in portal; Request entities and request types with voting. | Organizations standardizing on Targetprocess for intake. | Service Desk portal, Request entity + types, automation rules for routing (02.1.1-02.1.2). | Another portal for business users if ServiceNow already exists. | TP guide Service Desk |
| **ServiceNow ideation / demand front end** `servicenow` | Ideas are raised in ServiceNow; an integration creates Requests/epics in Targetprocess for qualification. | ServiceNow-centric enterprises. | ServiceNow integration (10.1.5), field mapping, status sync. | Two systems of record for the early lifecycle; sync rules matter. | WFM deck (ServiceNow ideation front-end) |
| **Email / forms** `email-forms` | Requests arrive by email or a form and are created by automation or a triage team. | Small volumes, interim state. | Email integration, automation rules. | Low structure; manual triage. | TP email integration |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 02.1.1 | Capture ideas & requests | 3 variants: Targetprocess Service Desk portal, ServiceNow ideation / demand front end, Email / forms |
| 02.1.2 | Triage, categorize & qualify demand | affected (no variant text yet) |
| 10.1.5 | Manage integrations & environments | affected (no variant text yet) |

## D-09 Cloud commitment management mode

**Are reserved-instance / savings-plan / CUD commitments managed by hand, assisted by recommendations, or automated?**

Decides whether 07.5.3 or 07.5.4 is the operating process, what guardrails and roles are configured, and how Finance approves commitments.

Domain: Cloud financial management · pick one · default: **Assisted (recommendations + approval)**

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Manual (vendor consoles)** `manual` | Commitments are bought in the cloud vendor consoles on a periodic review; Cloudability reports coverage. | Small cloud spend; early FinOps maturity (Crawl). | Commitment Overview reports. | Under-coverage and expiry misses are common. | FinOps Framework Rate Optimization (Crawl) |
| **Assisted (recommendations + approval)** (default) `assisted` | Cloudability generates purchase/exchange recommendations; FinOps and Finance approve and execute. | Most organizations (Walk). | Commitment Recommendations, approval forum, procurement alignment (07.5.3). | Human latency; coverage typically 70-85%. | IBM Docs commitments |
| **Automated (Savings Automation)** `automated` | Commitment portfolio managed on autopilot within per-account / per-region guardrails; savings-share billing. | Large, steady AWS/Azure estates (Run). | RateOptimizationFullAccess role, guardrail configuration (07.5.4 / 10.4.2), Finance sign-off on savings-share. | Governance shifts to guardrails; commercial model to accept. | IBM Docs Savings Automation |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 07.5.3 | Manage commitments (assisted) | only when Cloud commitment management mode: Assisted (recommendations + approval) |
| 07.5.4 | Automate commitments (Savings Automation) | only when Cloud commitment management mode: Automated (Savings Automation) |
| 10.4.2 | Configure budgets, alerts, optimization & governance | affected (no variant text yet) |

## D-10 IT cost recovery model

**Does IT show costs back, charge them back at allocated cost, or charge priced services with over/under recovery?**

Sets whether the Billing product is needed, whether a price list and O/U recovery process exist, and how BU conversations are framed.

Domain: Consumption & chargeback · pick one · default: **Showback** · flows: UC4, CLD

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Showback** (default) `showback` | BUs receive a Bill of IT for information; no journal entries. | First years of TBM; where BU budgets do not carry IT cost. | BU allocation (08.1.1), Bill of IT reports (08.1.2). | Influences behavior less than real charges. | TBM assessment (showback at service level) |
| **Chargeback at allocated cost** `chargeback-cost` | Allocated cost is journaled to BU cost centers each period; full recovery by construction. | Organizations with BU P&L accountability. | Billing product or GL journal export, agreed drivers, dispute process. | Charges fluctuate with allocation changes; BUs contest drivers. | Apptio Billing |
| **Chargeback at service prices** `chargeback-priced` | Services are priced (unit rates from 06.3.4); BUs are charged consumption x price; IT manages over/under recovery. | Mature TBM with a service catalog; shared-service models. | Service unit costs, pricing strategy and what-if modeling, O/U recovery management (08.1.3). | Pricing governance and recovery variance to manage; strongest demand shaping. | Apptio Billing (pricing, O/U recovery) |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 07.2.3 | Allocate shared costs | affected (no variant text yet) |
| 08.1.1 | Allocate consumption to business units | affected (no variant text yet) |
| 08.1.2 | Publish showback / Bill of IT | 3 variants: Showback, Chargeback at allocated cost, Chargeback at service prices |
| 08.1.3 | Price services & run chargeback | only when IT cost recovery model: Chargeback at service prices |
| 08.2.1 | Review costs with BU owners | affected (no variant text yet) |

## D-11 Team tool of record

**Do teams work in Targetprocess natively, or in Jira / Azure DevOps synced into Targetprocess as the aggregation layer?**

Decides which connectors exist, where iteration planning happens and what completed-work data is available for the labor model.

Domain: Agile program & delivery · pick one or more · default: **Jira / ADO synced** · flows: UC1 · related: D-01 Labor effort signal

| Option | What it is | Fits | Prerequisites | Trade-offs | Evidence |
|---|---|---|---|---|---|
| **Targetprocess native** `native` | Teams plan iterations and execute stories in Targetprocess boards. | Greenfield or consolidating tool estates. | Team boards, story/bug/task workflows (03.2.1). | Migration of team habits and history. | TP entity model |
| **Jira / ADO synced** (default) `synced` | Teams stay in Jira or Azure DevOps; native bi-directional connectors keep Targetprocess as the aggregation layer for portfolio and finance. | Most enterprises with established engineering tooling. | Native connectors, area/iteration path mapping, hierarchy rules (03.2.4). | Mapping governance; do not import story-level detail into cost systems. | TP integrations; e2e script anti-pattern |

**Processes shaped**

| L2 | Process | How |
|---|---|---|
| 03.2.1 | Plan & execute iterations | 2 variants: Targetprocess native, Jira / ADO synced |
| 03.2.4 | Sync with dev tools | only when Team tool of record: Jira / ADO synced |
| 02.3.4 | Maintain one governed hybrid portfolio view | affected (no variant text yet) |