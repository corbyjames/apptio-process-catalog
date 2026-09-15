# Tool configuration reference

Generated from `data/tool-config.yaml` (per-product checklists) plus the per-L2 configuration objects in `data/catalog.json`.

## Per-product checklists


### Targetprocess

**Structure & access**: Portfolios (Projects); Teams & hierarchy; ART / Solution Train (Groups); team-project assignment; user types; roles & per-process/per-state permissions; RBAC/entitlements *(Mirror operating model; Client Zero pattern: Team > ART > Solution Train with involvement %)*

**Entities & workflows**: Process per portfolio; entity states & sub-states; terminology renames (Release > Planning Interval); custom fields; calculated fields; Metrics engine rollups *(Entity hierarchy: Portfolio Epic > Epic > Feature > Story/Bug (+ Requests))*

**Workforce objects**: People (typed: internal/external/contingent, on/offshore, billable); Position Request + multi-level approval workflow; Involvements %; Job Profiles (rate & CapEx/OpEx mapping); skills; locations; vacations *(The three ingredients of the labor model live here)*

**Solutions Library**: SAFe 6.0; PI Planning; OKR; KPI; Demand & Capacity Mgmt (Work Allocation, Demand, Availability); Budgeting; Scenario Planning; Time Tracking + Timesheet Approval; Vacation Tracking; WFM & Optimization; Service Desk; Risk/Incident/Hybrid PM; DevOps *(Install then tailor; environment promotion Sandbox > Pre-Prod > Prod)*

**Views & automation**: Boards/lists/timelines; dashboards & information radiators; view sharing per role; automation rules (JS, webhooks); validation rules *(Role-based views per SPM journey map)*

**Integrations**: Jira & Azure DevOps native bi-directional connectors; ServiceNow; email; SSO/SAML; REST API v1/v2; Workday roster feed (+ team-mapping metadata); ADM feeds to Planning/Costing *(Sync cadences per source (daily/weekly/monthly/manual))*


### Costing

**Project & model**: Costing Standard project; Foundation / Applications & Services / Business Units modules; Cost Source, Labor, Fixed Asset Ledger, Other Cost Pools, IT Resource Towers objects *(TBM Studio: Data Studio / Model Studio / Report Studio)*

**Master & reference data**: Cost Source Master Data (+Profile, Validity); Labor, Vendors, Fixed Asset, Projects master data; Cost Pool Reference List (ATUM); account mapping lookup tables; cost center hierarchy *(Key fields: Cost Pool/Sub-Pool, Is Depr, Fixed/Variable, Discretionary)*

**Allocations**: Allocation strategies (even, %, weighted, consumption); drivers (servers, headcount, tickets, transactions, story points); labor allocation options (estimates, time, agile stories, hybrid); ATP CM Rate Transform; fixed-capacity team rules; cross-charge & Build/Run cost types *(Mature allocations over time; absorption analysis for over/under allocation)*

**Data pipeline**: Datalink app + on-prem Agent (Boomi); connectors (REST, SAP, ServiceNow, Salesforce...); ULS; schedules & monitoring; Data Studio transforms & quality checks *(Implementation tiers automate 5-15 sources)*

**Reporting**: IT Financial Reports; Applications Overview / App TCO; Business Units collection; Services & Workforce NX reports; Benchmarking; Billing (Bill of IT); Apptio BI self-service + subscriptions *(CT Leadership Review pattern for exec reporting)*


### Planning

**Plan structure**: Plans & folders; plan states New/Open/Final; snapshots & version compare; multi-year; multi-currency; working calendars; fiscal periods *(Budget of record + forecast versions strategy)*

**Planning domains**: Worksheets/line items & cost categories; labor planning (positions, comp adjustments, headcount targets, allocation rules); asset planning (depreciation methods, delegation); contract planning (amortization, renewals & escalations, delegation); Integrated Investment Planning (investment tags, Build/Run, rate cards, cross-charge) *(GL-to-IT category mappings translate finance categories into IT terms)*

**Governance & integration**: Approval workflows (submit/review/approve/return); cost object permissions; Restricted Access (sensitive comp); Intelligent Forecasting; Costing & Cloudability integrations; IBM Planning Analytics bi-directional connector; REST APIs (plans, variance, status, spend)


### Cloudability

**Data & allocation**: Vendor Credentials (AWS/Azure/GCP/OCI); FOCUS Ingress + manifest; IBM FinOps Agent (containers); Business Mappings & Business Metrics; Tags/Labels + Tag Explorer; Account Groups; Views; Cost Sharing & Telemetry rules; ATUM dimensions *(FOCUS 1.0/1.1 supported; native connectors preferred for CSP data)*

**Planning & optimization**: Budgets on Views; Intelligent Forecasting (driver dims); Workload Planning (Workloads, Resources, Recommendations, Preferences); Rightsizing Preferences & ROI; Commitment Overview/Portfolio/Recommendations; Savings Automation guardrails (per-account/region, active-management toggles, RateOptimizationFullAccess)

**Operate & govern**: Anomaly alert rules (scope, thresholds, recipients, email/PagerDuty, Jira/ServiceNow ticketing); Dashboards/Reports/Scorecards; AI Services Dashboard; Cost Governance policies (tag enforcement, pre-deployment estimation - preview); user/role admin *(Turbonomic action automation in Premium)*


### Cross-product

**ADM / data highway**: Feed catalog: targets down (Planning>ATP); positions up (ATP>Planning, daily/weekly); rates back (Costing>ATP); workforce & work data in (ATP>Costing, monthly); cloud cost (Cloudability>Costing); investment loop (ATP<->Costing/Planning); roster sources (daily/monthly/manual) *(Monitor cadences & errors; this is the integration fabric of every E2E flow)*


## Configuration objects by process (from the catalog)


### Targetprocess

| L2 | Process | Configuration objects |
|---|---|---|
| 01.1.1 | Define strategic themes & business objectives | Objective entity (OKR solution), Group/portfolio hierarchy, roadmap views |
| 01.1.2 | Cascade strategy to portfolios & value streams | Portfolio/ART (Group) structure, relations objectives->portfolio epics, OKR cascade (Ultimate>Strategic>Tactical) |
| 01.1.3 | Monitor strategy execution & re-plan dynamically | Corporate Strategy Dashboard, OKR hierarchy views, dashboards fed to leadership reporting (CT Leadership Review) |
| 01.2.1 | Set & cascade OKRs | OKR solution: Objective & Key Result entities, period assignment, weighted scoring; objective-writing standards (outcome- not task-phrased, measurable, sufficient supporting features) |
| 01.2.2 | Link work & investments to OKRs | Relations work items->Objectives, KPI-linked key results, alignment views |
| 01.2.3 | Score, review & refresh OKRs | KPI solution measurements, calculated fields, OKR dashboards & review views |
| 02.1.1 | Capture ideas & requests | Service Desk portal, Request entity + request types, email integration, voting; ServiceNow intake integration |
| 02.1.2 | Triage, categorize & qualify demand | Request workflow states, triage boards, automation rules (routing/auto-reply/linked entities), work-intake taxonomy (categories, CapEx/OpEx, non-labor categories); duplicate/overlap detection across descriptions, outcomes, journeys, capabilities |
| 02.1.3 | Progress demand through Portfolio Kanban | Portfolio Epic workflow states, Kanban board views, WIP limits, per-state permissions |
| 02.2.1 | Build lean business case / epic hypothesis | Budgeting solution templates (epic hypothesis, lean business case), rich-text/custom fields, Portfolio Epic Score report |
| 02.2.2 | Prioritize by value (WSJF / scoring) | Numeric custom fields (BV, TC, RR/OE, size), calculated field/metric for WSJF, prioritized list views, objective-scoring |
| 02.2.3 | Approve & fund investments | Entity states + per-state role permissions (gates), automation rules for approvals, Budgeting solution (fund Portfolios/Work/People/Products), A1 approved-investment-budget feed |
| 02.3.1 | Build & maintain roadmaps | Timeline/Roadmap views on Portfolio Epics/Epics/Features vs Releases/PIs, multi-level roadmaps |
| 02.3.2 | Model scenarios & trade-offs | Scenario Planning solution (plan variants, promote scenario to baseline), demand vs capacity data, budget dashboards |
| 02.3.3 | Manage cross-initiative dependencies & risks | Dependency/Impediment entities, relations, ART Planning Board, Risk Management solution; dependency graph & prioritized heatmap, dependency ownership & aging tracking |
| 02.3.4 | Maintain one governed hybrid portfolio view | Hybrid portfolio views (agile + waterfall side by side), Hybrid Project Management solution, common work categorization fields, Jira/ADO sync for agile initiatives |
| 02.4.1 | Define funding model | Budgeting solution (annual or custom periods, value-stream funding), portfolio structure, budget guardrails by horizon/capacity/initiative |
| 02.4.2 | Receive & apply top-down targets | Budget Targets report, target budget entities, ADM/data highway feed |
| 02.4.3 | Track portfolio budget vs actuals | Budget vs actuals dashboards, money custom fields, blended-rate costed work allocations, Budgeting view (Proposed Labor vs Target) |
| 02.5.1 | Define expected outcomes & value metrics | KPI solution, key results on epics, money/number custom fields |
| 02.5.2 | Track realized value & feed decisions | KPI measurements, dashboards, Value Realization tab in leadership reporting, ROI/margin analysis |
| 03.1.1 | Assess & prepare quarterly planning readiness | PI & ART entities with dates, ART/Program PI Objectives, Team PI Objectives, features assigned to PI release, capacity fields (velocity = people x 8 rule; 80/20 allocation), PI Planning solution Pre-Plan views; readiness scoring & gap-resolution workflow (assign owner, add estimate, split feature, escalate decision), definition-of-ready rules |
| 03.1.2 | Run quarterly planning event | PI Planning Board, ART Planning Board (dependencies), Team Iteration assignment, WSJF-ordered features, risk entities |
| 03.1.3 | Commit & publish PI objectives | Team PI Objectives (Committed/Stretch, confidence %, BV points), PI Dashboard, Program Board |
| 03.1.4 | Baseline commitments & track PI execution | PI Dashboard, dependency & risk boards, progress rollup metrics, burndown/CFD reports; commitment baseline snapshot, planned-vs-actual objective tracking, predictive ART health (flow time/efficiency/load, WIP, dependency aging), RTE/STE daily briefing views |
| 03.1.5 | Manage PI risks (ROAM) & confidence vote | Risk entities with ROAM classification fields, risk boards, owners & due dates, confidence-vote capture, risk aging/escalation automation rules |
| 03.1.6 | Run system demo & Inspect and Adapt | Demo readiness views, PI metrics dashboards (predictability, flow, carryover), retrospective/improvement work items, pattern analysis (recurring dependency failures, chronic overcommitment) |
| 03.2.1 | Plan & execute iterations | Team Iteration entities, Scrum/Kanban team boards, story/bug/task workflows, estimation fields |
| 03.2.2 | Track flow & progress | Velocity/burn/CFD/cycle-time reports, Metrics engine rollups, Forecast reports |
| 03.2.3 | Manage impediments & dependencies | Impediment/Dependency entities, boards, automation rule notifications |
| 03.2.4 | Sync with dev tools | Native Jira/ADO bi-directional connectors (issue-level, area/iteration path), Git/GitHub/GitLab via automation rules/webhooks |
| 03.3.1 | Plan releases & enable release packages | Release/Planning Interval entities, Release Package Enablement solution |
| 03.3.2 | Manage hybrid & waterfall projects | Traditional/Hybrid Project Management solutions, timeline views, milestones, hybrid portfolio views |
| 03.3.3 | Govern stage-gates & milestones for traditional initiatives | Entity states as gates with per-state role permissions, milestone entities, timeline/Gantt views, automation rules for gate notifications, Traditional Project Management solution |
| 03.4.1 | Identify & map value streams | ART/Group structure as value streams, value stream workshops (journey map), portfolio mapping |
| 03.4.2 | Measure & improve flow | Value stream KPIs (SAFe 6.0 solution), KPI solution, flow dashboards |
| 04.1.1 | Load & maintain people roster | People/Users entities, employee type (internal/external/contingent, on/offshore, billable), locations, skills; sync cadence per source (Client Zero: employees+contractors daily, consulting monthly, other manual) |
| 04.1.2 | Create & assign teams, ARTs & trains | Team entities & hierarchy, ART/Solution Train, Involvements (% allocation, e.g. 50/75/100), team-project assignment |
| 04.1.3 | Maintain job profiles & financial mappings | Job Profile entities, CapEx/OpEx split mapping per profile, team->IT Tower mapping (fixed capacity rule), rate linkage (rates held in Costing) |
| 04.2.1 | Map & forecast capacity | Capacity dashboards, availability (total/reserved/available), Vacation Tracking solution feeding availability, regional calendars |
| 04.2.2 | Balance demand vs capacity | Demand & Capacity Mgmt solution (Work Allocation entity %/hours/man-days, auto-generated Demand per period, load reports, demand processing screens), capacity/FTE reports vs targets |
| 04.2.3 | Run workforce scenarios | Scenario planning (workforce scenarios, labor availabilities generation), HC scenario views |
| 04.3.1 | Allocate people & teams to work | Work Allocation entities, allocation timelines, team-to-work assignment at any level |
| 04.3.2 | Track utilization & productivity | Resource Management Dashboard, Team Load report, Efficiency tab (completed items & effort MoM) |
| 04.3.3 | Match skills & close gaps | Skills fields, capacity by skill views, gap reports |
| 04.3.4 | Assign individuals & roles to project work (hybrid resourcing) | Work Allocations (person-level man-days/hours), role-based demand requests, New Requested Demand workflow, availability integration |
| 04.4.1 | Create position requests | Position Request entity (role, location, hours, employment type, department link) |
| 04.4.2 | Approve positions (multi-level workflow) | Multi-level approval workflow (entity states + per-state permissions), automation rules (notifications, escalations), XOR outcome |
| 04.4.3 | Sync approved positions to Planning & auto-update on fill | ADM/data highway position feed, open vs filled normalization in Planning, auto-update linkage |
| 04.5.1 | Record time against work | Time entity, Time Tracking solution, timesheet views, billable/non-billable fields; alternative: work allocations instead of timesheets |
| 04.5.2 | Approve timesheets | Timesheet approval workflow (solution component), notifications |
| 04.5.3 | Feed time/effort to finance processes | Time reports/exports, ADM feed to Costing, story-point/completed-work alternative (deprecates time writing) |
| 10.1.1 | Design org, portfolio & team structure | Portfolios (Projects), Teams, ART/Groups, team-project assignment, user types, roles & per-process permissions, RBAC |
| 10.1.2 | Configure processes, workflows & fields | Process editor, entity states & per-state permissions, terminology renames, custom fields, calculated fields, Metrics engine |
| 10.1.3 | Install & tailor Solution Library packages | Solutions Library, solution components, extensions, versioning/upgradability |
| 10.1.4 | Build views, dashboards & automation | Board/list/timeline views, view sharing, dashboards, automation rules (JS logic, webhooks), validation rules |
| 10.1.5 | Manage integrations & environments | Native connectors, REST API/webhooks, SSO/SAML, environment promotion (incl. validation & automation rules) |
| 10.6.3 | Run SPM governance & transformation | SPM maturity model (6 domains x lenses, Foundational>Scaled), journey map tracks, governance cadences, domain owners |
| 10.7.1 | Deploy the planning copilot & delivery intelligence | MVP capability set: readiness assessment & scoring, resolution recommendations, dependency discovery/visualization, capacity validation, objective drafting/quality, live copilot, real-time impact analysis, risk/ROAM facilitation, commitment baseline & tracking, executive/RTE briefings; Targetprocess + Jira/ADO integration |

### Costing

| L2 | Process | Configuration objects |
|---|---|---|
| 05.8.2 | Build the cost-driver fact base & activity inventory | Cost Source fields (Fixed/Variable, Discretionary, Is Depr), Applications Overview / App TCO & AppRat reports, vendor consolidation reports, Cloudability rightsizing & idle reports, Planning 'Adjust Baseline Values' set to zero or driver-only for in-scope units |
| 06.1.1 | Load month-end actuals | Datalink connectors & schedules, Cost Source master data tables, ULS uploads |
| 06.1.2 | Refresh mappings & run allocations | Account mapping lookup tables, Cost Pool Reference List (ATUM), Model Studio allocation strategies (even/percent/weighted/consumption), allocation drivers |
| 06.1.3 | Validate & reconcile to GL | Model validation, absorption analysis, GL traceability drill-through |
| 06.1.4 | Publish monthly TBM reporting | IT Financial Reports, Apptio BI, report subscriptions, CT Leadership Review |
| 06.2.1 | Analyze spend by cost pool & tower | Cost pool & tower reports, Cost Source fields (Is Depr, Fixed Variable, Discretionary), tower unit costs |
| 06.2.2 | Track budget vs actuals in the model | Budget dataset integration, variance reports, common data bus with Planning |
| 06.2.3 | Classify & report run/grow/transform | Run/grow/transform classification fields, Project Cost Type (build/run), Run-vs-Grow reports |
| 06.3.1 | Maintain application & service inventory | Applications & Services module master data, service catalog, ATUM Service Taxonomy (Service Type>Category>Service>Offering) |
| 06.3.2 | Allocate costs to applications & services | Tower->application allocation strategies, drivers (server counts, tickets, time/story points) |
| 06.3.3 | Report & act on App TCO | Applications Overview / App TCO reports, run vs change attribution from work data (UC4), addressable vs committed spend, AppRat analysis |
| 06.3.4 | Compute service unit costs | Service costing model, consumption metrics, Services NX Reports |
| 06.4.1 | Maintain protected rates & compute blended rates | ATP CM Rate Transform, protected rate tables, blending logic; rate-level exposure design decision (blended vs individual) |
| 06.4.2 | Publish blended rates to Targetprocess | ADM rate feed, rate cadence config; true-up pattern for blended-vs-actual reconciliation (design decision) |
| 06.4.3 | Ingest workforce & completed work data | ADM feed ATP->TBM Studio, involvement/profile/mapping datasets |
| 06.4.4 | Compute monthly team cost & blended CapEx % | TBM Studio computation, job profile CapEx/OpEx splits, involvement math |
| 06.4.5 | Allocate team costs to work or towers | Story-point/weightage allocation, fixed-capacity rules (team->app/tower), one normalized model for both team kinds |
| 06.4.6 | Generate audit-ready capitalization actuals | SAP-ready extract format, audit documentation, contractor/PS normalization |
| 06.5.1 | Consolidate & analyze vendor spend | Vendors master data, vendor insights reports, contract/PO feeds |
| 06.5.2 | Track assets & depreciation | Fixed Asset Ledger, Is Depr flag, depreciation flows |
| 06.6.1 | Prepare taxonomy-aligned benchmark data | ATUM mappings, benchmarking data prep |
| 06.6.2 | Compare vs peers & set targets | Benchmarking Essentials/Standard, custom peer groups, box plots, IT Benchmarking Review, Spend Archetypes |
| 08.1.1 | Allocate consumption to business units | Business Units module, drivers (headcount, users, transactions, volume), Cloudability cost sharing results |
| 08.1.2 | Publish showback / Bill of IT | Billing product (Bill of IT reports), Business Units Report Collection, scheduled distribution |
| 08.1.3 | Price services & run chargeback | Billing pricing, what-if scenario modeling, O/U recovery management |
| 08.2.1 | Review costs with BU owners | BU reports, cost driver drill-downs, per-employee spend views |
| 08.2.2 | Extend costing beyond IT | EBM Costing & Billing, EIW alignment, digital KPIs (unit cost, flow velocity, volumes) |
| 10.2.1 | Implement the cost model | Costing Standard project, Cost Source/Labor/Fixed Asset/Vendors/Projects master data, Cost Pool Reference List, account mapping tables, Model Studio strategies, Report Studio/Apptio BI |
| 10.2.2 | Operate data pipelines (Datalink) | Datalink app + Agent (Boomi), connectors (REST, SAP, ServiceNow...), ULS, schedules, Data Studio transforms & quality checks |
| 10.6.1 | Run the TBM office | TBM office roles, governance forums, OCM & training, procurement/vendor alignment; ZBB: cost-category owner matrix, rotation calendar |

### Planning

| L2 | Process | Configuration objects |
|---|---|---|
| 05.1.1 | Establish plan structure & baseline | Plan creation, plan folders, working calendar, Adjust Baseline Values, actuals import, cost center/account hierarchies |
| 05.1.2 | Set & distribute top-down targets | Set Targets, Labor Headcount Targets, cost object permissions; target feed to ATP (UC3) |
| 05.1.3 | Enter bottom-up budgets | Worksheets/line items, cost categorization, multi-currency, transaction-level entry |
| 05.1.4 | Review, iterate & approve budget | Approval workflow (submit/review/approve/return), plan states New>Open>Final, conversational insights |
| 05.1.5 | Finalize budget of record | Plan state Final, snapshots/version compare |
| 05.2.1 | Create forecast seeded with actuals | Actuals import, Costing integration, snapshots, multi-year plans |
| 05.2.2 | Update forecasts (driver & AI-assisted) | Intelligent Forecasting (multi-model AI), contract auto-extension, driver-based lines |
| 05.2.3 | Model what-if scenarios | Compare Versions/Plans, what-if modeling, IBM Planning Analytics bi-directional connector |
| 05.2.4 | Submit & sign off forecast | Approval workflow, plan status tracking |
| 05.3.1 | Load & reconcile actuals to plan | Costing/Cost Transparency integration, actuals import, GL-to-IT category mappings |
| 05.3.2 | Analyze variances with thresholds | Variance analysis, Plan vs Plan variance with thresholds, variance REST APIs, exports |
| 05.3.3 | Narrate variance & reforecast | Comments, change-history audit, forecast update workflow |
| 05.4.1 | Plan positions & FTEs | Labor planning module, headcount targets, working calendar, position normalization from ATP feed (UC3) |
| 05.4.2 | Plan compensation & adjustments | Compensation adjustments, variable workforce adjustments, field-level Restricted Access (sensitive salary) |
| 05.4.3 | Allocate planned labor | Labor allocation rules, project labor activity (role-based), plan-side cost model |
| 05.5.1 | Maintain contract line items | Contract planning, amortization approaches, VAT handling |
| 05.5.2 | Plan renewals & escalations | Contract extensions/renewals with compounding % adjustments, renewal comments, auto-extension |
| 05.5.3 | Delegate contract costs | Contract cost delegation |
| 05.6.1 | Plan asset purchases & lifecycle | Asset planning module, Fixed Asset Ledger linkage, refresh planning |
| 05.6.2 | Generate depreciation schedules | Depreciation methods configuration, Delegate Asset Costs |
| 05.7.1 | Define investments & cost treatment | Integrated Investment Planning: investment tags on budget lines, Project Cost Type (build/run), Project Total & Charges KPIs, project permissions |
| 05.7.2 | Plan investment labor & cross-charge | Labor resource planning (rates x effort), flexible rate cards, configurable cross-charge, demand vs capacity balancing |
| 05.7.3 | Operate the investment loop with ATP | Bi-directional A1<->ATP integration (A1->ATP: approved investment budget, budget changes; ATP->A1: investments, planned labor allocations, actual labor effort, change requests) |
| 05.8.1 | Scope the ZBB cycle & select decision units | Dedicated ZBB plan/folder per cycle, cost object permissions per decision unit, custom list 'Cost Category Owner', decision-unit hierarchy sourced from Costing towers/services/cost centers, 'ZBB Rotation Year' attribute on cost objects |
| 05.8.3 | Build decision packages at tiered service levels | Worksheets/line items tagged by custom lists 'Decision Package' and 'Service Level Tier' (Minimum/Current/Enhanced), driver-based line items, labor planning positions & comp (05.4), contract lines (05.5), asset lines (05.6), justification/comment fields, package templates |
| 05.8.4 | Rank packages & set the funding cut-line | Scoring custom fields (criticality, alignment, value, risk) on line items/packages, Compare Versions/Plans (one version per cut-line scenario), Set Targets, what-if modeling; Targetprocess objective-scoring for any change packages; unfunded initiatives list |
| 05.8.5 | Approve zero-based budget & release freed spend to the investment envelope | Approval workflow (submit/review/approve/return), plan state Final + snapshot as ZBB baseline, merge of ZBB plan into master plan, target feed to ATP (ADM), Budget Targets report in Targetprocess |
| 05.8.6 | Monitor package commitments & sustain the zero-based mindset | Variance thresholds per package/cost category, budget dataset in Costing (06.2.2), CIO Monthly Ops Dashboard financial-attainment tile (08.2.3), savings-tracking custom fields, snapshot compare vs ZBB baseline |
| 10.3.1 | Configure planning structures | Reference data/schemas/custom lists, line-item config, working calendar, multi-currency, cost object permissions, Restricted Access dims; ZBB custom lists & scoring fields |
| 10.3.2 | Configure workflow & integrations | Approval workflow config, plan states, Costing/Cloudability/Planning Analytics connectors, REST APIs |

### Cloudability

| L2 | Process | Configuration objects |
|---|---|---|
| 07.1.1 | Connect cloud billing accounts | Vendor Credentials (AWS payer+CUR, Azure export, GCP BigQuery, OCI), amortization/cost-basis settings |
| 07.1.2 | Ingest custom & FOCUS data | FOCUS Ingress (S3/Blob/GCS + manifest), FOCUS validator |
| 07.1.3 | Onboard container cost data | IBM FinOps Agent (Helm), cluster credentials, shared cluster cost allocation rules |
| 07.1.4 | Validate & reprocess data | TrueCost Explorer reconciliation, Data Reprocess |
| 07.2.1 | Design business mappings & views | Business Mappings (match/value expressions), Business Metrics, Account Groups, Views |
| 07.2.2 | Govern tagging | Tags & Labels config, Tag Explorer, untagged-cost reports, Governance mandatory tag enforcement (Terraform/GitHub preview) |
| 07.2.3 | Allocate shared costs | Cost Sharing & Telemetry rules, CSV rule import/export |
| 07.2.4 | Map cloud spend to TBM taxonomy | ATUM Tower/Sub-Tower/Service dimensions, Cloudability->Costing data share |
| 07.3.1 | Operate dashboards & scheduled reports | Dashboards & widgets, Reports (scheduled email), TrueCost Explorer, AI Services Dashboard, Views |
| 07.3.2 | Benchmark efficiency | Scorecards (peer & internal) |
| 07.3.3 | Track unit economics | Business Metrics (<=5/account), telemetry joins, dashboards |
| 07.3.4 | Report & act on sustainability | Sustainability metrics (incl. Azure/OCI GPU), dashboards, scorecards |
| 07.4.1 | Configure anomaly detection | Anomaly alerts (view scope, Total Cost/Unusual Spend thresholds, filters, email/PagerDuty) |
| 07.4.2 | Triage, route & resolve anomalies | Anomaly drill-down, TrueCost Explorer, bi-directional Jira/ServiceNow ticketing, alert history |
| 07.5.1 | Run the rightsizing cadence | Rightsizing recommendations & Preferences (lookback, aggressiveness), Rightsizing ROI, Turbonomic action automation (Premium) |
| 07.5.2 | Eliminate waste & govern pre-deployment | Utilization/idle reports, Cost Governance policies, pre-deployment cost estimation (preview) |
| 07.5.3 | Manage commitments (assisted) | Commitment Overview / Portfolio / Recommendations |
| 07.5.4 | Automate commitments (Savings Automation) | Guardrails (ingestion account selection, active-management toggles, advanced config), savings assessment, coverage monitoring |
| 07.6.1 | Manage cloud budgets | Budgets on Views, breach alerts |
| 07.6.2 | Forecast cloud spend | Intelligent/Enhanced Forecasting (best-fit model, <=3 driver dims), dashboards |
| 07.6.3 | Plan migrations & new workloads | Workload Planning: Workloads, Resources (VM/DB/storage/LB, bulk JSON/XLSX), Recommendations, Preferences |
| 10.4.1 | Configure cloud data, mappings & views | Vendor credentials (AWS/Azure/GCP/OCI), Business Mappings/Metrics, tags/account groups/views, cost sharing rules, container agents, users/roles + ATUM dims |
| 10.4.2 | Configure budgets, alerts, optimization & governance | Dashboards/reports/scorecards, budgets & forecast settings, anomaly rules, rightsizing prefs, commitment/SA guardrails, governance policies, workload planning prefs |
| 10.6.2 | Run the FinOps practice | FinOps roles/personas, governance policies, training, Crawl/Walk/Run capability plans |

### All four

| L2 | Process | Configuration objects |
|---|---|---|
| 08.2.3 | Run the CIO monthly operations review | CIO Monthly Operations Dashboard: IT Financial Attainment (CT + Planning), IT Vendor Report, App & Run-vs-Grow (APM+CT), Cloud Consumption (Cloudability), Workforce Analytics |
| 10.5.1 | Operate the ADM data highway | ADM/data highway feeds & cadences (positions daily/weekly, rates regular, work data monthly, roster daily-monthly by source), monitoring & error handling |
| 10.5.2 | Govern master data & taxonomy | ATUM taxonomy layers, service catalog as product catalog, tag dictionaries, cross-reference tables, referential integrity checks |
| 10.6.4 | Assess maturity & set roadmap | TBM 6-dimension assessment (0-5), FinOps 4-domain Crawl/Walk/Run, SPM 6-domain x lens assessment (1-5), roadmap planning |
| 10.7.2 | Govern agent autonomy & trust | Configurable autonomy/approval rules, RBAC & data entitlements, separation of duties, action history & recommendation traceability, data-source attribution, model/prompt governance, sensitive-data protection |
| 10.7.3 | Ground agents in enterprise context & ecosystem | Version-controlled context store (journeys, architectures, policies, conventions), MCP-based extensibility (approved tools, customer agents, role-based tool access, auditable actions), source-of-truth & two-way sync governance, stale/conflicting-data disclosure |