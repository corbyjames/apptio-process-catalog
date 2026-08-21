# Tool Configuration Reference

Generated from `data/tool-config.yaml`.


## Targetprocess

**Structure & access**: Portfolios (Projects); Teams & hierarchy; ART / Solution Train (Groups); team-project assignment; user types; roles & per-process/per-state permissions; RBAC/entitlements *(Mirror operating model; Client Zero pattern: Team > ART > Solution Train with involvement %)*

**Entities & workflows**: Process per portfolio; entity states & sub-states; terminology renames (Release > Planning Interval); custom fields; calculated fields; Metrics engine rollups *(Entity hierarchy: Portfolio Epic > Epic > Feature > Story/Bug (+ Requests))*

**Workforce objects**: People (typed: internal/external/contingent, on/offshore, billable); Position Request + multi-level approval workflow; Involvements %; Job Profiles (rate & CapEx/OpEx mapping); skills; locations; vacations *(The three ingredients of the labor model live here)*

**Solutions Library**: SAFe 6.0; PI Planning; OKR; KPI; Demand & Capacity Mgmt (Work Allocation, Demand, Availability); Budgeting; Scenario Planning; Time Tracking + Timesheet Approval; Vacation Tracking; WFM & Optimization; Service Desk; Risk/Incident/Hybrid PM; DevOps *(Install then tailor; environment promotion Sandbox > Pre-Prod > Prod)*

**Views & automation**: Boards/lists/timelines; dashboards & information radiators; view sharing per role; automation rules (JS, webhooks); validation rules *(Role-based views per SPM journey map)*

**Integrations**: Jira & Azure DevOps native bi-directional connectors; ServiceNow; email; SSO/SAML; REST API v1/v2; Workday roster feed (+ team-mapping metadata); ADM feeds to Planning/Costing *(Sync cadences per source (daily/weekly/monthly/manual))*


## Costing

**Project & model**: Costing Standard project; Foundation / Applications & Services / Business Units modules; Cost Source, Labor, Fixed Asset Ledger, Other Cost Pools, IT Resource Towers objects *(TBM Studio: Data Studio / Model Studio / Report Studio)*

**Master & reference data**: Cost Source Master Data (+Profile, Validity); Labor, Vendors, Fixed Asset, Projects master data; Cost Pool Reference List (ATUM); account mapping lookup tables; cost center hierarchy *(Key fields: Cost Pool/Sub-Pool, Is Depr, Fixed/Variable, Discretionary)*

**Allocations**: Allocation strategies (even, %, weighted, consumption); drivers (servers, headcount, tickets, transactions, story points); labor allocation options (estimates, time, agile stories, hybrid); ATP CM Rate Transform; fixed-capacity team rules; cross-charge & Build/Run cost types *(Mature allocations over time; absorption analysis for over/under allocation)*

**Data pipeline**: Datalink app + on-prem Agent (Boomi); connectors (REST, SAP, ServiceNow, Salesforce...); ULS; schedules & monitoring; Data Studio transforms & quality checks *(Implementation tiers automate 5-15 sources)*

**Reporting**: IT Financial Reports; Applications Overview / App TCO; Business Units collection; Services & Workforce NX reports; Benchmarking; Billing (Bill of IT); Apptio BI self-service + subscriptions *(CT Leadership Review pattern for exec reporting)*


## Planning

**Plan structure**: Plans & folders; plan states New/Open/Final; snapshots & version compare; multi-year; multi-currency; working calendars; fiscal periods *(Budget of record + forecast versions strategy)*

**Planning domains**: Worksheets/line items & cost categories; labor planning (positions, comp adjustments, headcount targets, allocation rules); asset planning (depreciation methods, delegation); contract planning (amortization, renewals & escalations, delegation); Integrated Investment Planning (investment tags, Build/Run, rate cards, cross-charge) *(GL-to-IT category mappings translate finance categories into IT terms)*

**Governance & integration**: Approval workflows (submit/review/approve/return); cost object permissions; Restricted Access (sensitive comp); Intelligent Forecasting; Costing & Cloudability integrations; IBM Planning Analytics bi-directional connector; REST APIs (plans, variance, status, spend)


## Cloudability

**Data & allocation**: Vendor Credentials (AWS/Azure/GCP/OCI); FOCUS Ingress + manifest; IBM FinOps Agent (containers); Business Mappings & Business Metrics; Tags/Labels + Tag Explorer; Account Groups; Views; Cost Sharing & Telemetry rules; ATUM dimensions *(FOCUS 1.0/1.1 supported; native connectors preferred for CSP data)*

**Planning & optimization**: Budgets on Views; Intelligent Forecasting (driver dims); Workload Planning (Workloads, Resources, Recommendations, Preferences); Rightsizing Preferences & ROI; Commitment Overview/Portfolio/Recommendations; Savings Automation guardrails (per-account/region, active-management toggles, RateOptimizationFullAccess)

**Operate & govern**: Anomaly alert rules (scope, thresholds, recipients, email/PagerDuty, Jira/ServiceNow ticketing); Dashboards/Reports/Scorecards; AI Services Dashboard; Cost Governance policies (tag enforcement, pre-deployment estimation - preview); user/role admin *(Turbonomic action automation in Premium)*


## Cross-product

**ADM / data highway**: Feed catalog: targets down (Planning>ATP); positions up (ATP>Planning, daily/weekly); rates back (Costing>ATP); workforce & work data in (ATP>Costing, monthly); cloud cost (Cloudability>Costing); investment loop (ATP<->Costing/Planning); roster sources (daily/monthly/manual) *(Monitor cadences & errors; this is the integration fabric of every E2E flow)*
