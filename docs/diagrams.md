# BPMN diagram index · v0.6.0

Generated. One BPMN 2.0 model (with diagram interchange) and one SVG snapshot per process area, process group and cross-tool flow. Open any `.bpmn` in the Pages [viewer/editor](../site/viewer.html), bpmn.io, Camunda Modeler, Signavio, Visio or Draw.io. Hand-refined models belong in `diagrams/bpmn/custom/`.

## How the diagrams are derived

- **Flows** (`flow-*.bpmn`): straight from the step tables in `data/catalog.json` (`flows[].steps`): lane = system/role, type = the BPMN element named in the step, gateway branches parsed from the note (`No: end event '…'`, `loop to z4`, suffix steps `17a`/`17b`).
- **Groups** (`NN.N.bpmn`): one task per L2 in catalog order; lane = the first persona in the L2's *Who* text that matches one of the area's default lanes (fallback: product hint, then lane 1); task type inferred from the persona (`System`/`automated` → service) and the verb (send/publish → send task; approve/submit/enter/… → user task).
- **Areas** (`L0-NN.bpmn`): one collapsed sub-process per group, placed in the lane where most of its L2s sit.

| Diagram | Kind | Lanes | Steps | BPMN | SVG |
|---|---|---|---|---|---|
| UC3 Targets down | flow | IT Planning (Finance); Targetprocess / ATP | 11 | [flow-UC3.bpmn](../diagrams/bpmn/generated/flow-UC3.bpmn) | [flow-UC3.svg](../assets/diagrams/flow-UC3.svg) |
| UC2 Rates back | flow | Costing / TBM Studio; Targetprocess / ATP | 3 | [flow-UC2.bpmn](../diagrams/bpmn/generated/flow-UC2.bpmn) | [flow-UC2.svg](../assets/diagrams/flow-UC2.svg) |
| UC1 Actuals in | flow | Targetprocess / ATP; Costing / TBM Studio; ERP (SAP) | 7 | [flow-UC1.bpmn](../diagrams/bpmn/generated/flow-UC1.bpmn) | [flow-UC1.svg](../assets/diagrams/flow-UC1.svg) |
| UC4 TCO up | flow | Costing / TBM Studio | 3 | [flow-UC4.bpmn](../diagrams/bpmn/generated/flow-UC4.bpmn) | [flow-UC4.svg](../assets/diagrams/flow-UC4.svg) |
| CLD Cloud to TBM | flow | Cloudability; Costing / TBM Studio | 3 | [flow-CLD.bpmn](../diagrams/bpmn/generated/flow-CLD.bpmn) | [flow-CLD.svg](../assets/diagrams/flow-CLD.svg) |
| INV Investment loop | flow | Targetprocess / ATP; Costing / TBM Studio; IT Planning (Finance) | 3 | [flow-INV.bpmn](../diagrams/bpmn/generated/flow-INV.bpmn) | [flow-INV.svg](../assets/diagrams/flow-INV.svg) |
| ZBB ZBB re-base | flow | IT Planning (Finance); Costing / TBM Studio; Budget owners (in Planning); Targetprocess / ATP | 12 | [flow-ZBB.bpmn](../diagrams/bpmn/generated/flow-ZBB.bpmn) | [flow-ZBB.svg](../assets/diagrams/flow-ZBB.svg) |
| L0-01 Strategy & Goal Management | area | C-Suite/Strategy | 2 | [L0-01.bpmn](../diagrams/bpmn/generated/L0-01.bpmn) | [L0-01.svg](../assets/diagrams/L0-01.svg) |
| 01.1 Set strategic direction & alignment | group | C-Suite/Strategy; Portfolio Management | 3 | [01.1.bpmn](../diagrams/bpmn/generated/01.1.bpmn) | [01.1.svg](../assets/diagrams/01.1.svg) |
| 01.2 Manage OKRs | group | C-Suite/Strategy; Portfolio Management | 3 | [01.2.bpmn](../diagrams/bpmn/generated/01.2.bpmn) | [01.2.svg](../assets/diagrams/01.2.svg) |
| L0-02 Demand & Portfolio Investment Management | area | Requesters/Business; Portfolio Management | 5 | [L0-02.bpmn](../diagrams/bpmn/generated/L0-02.bpmn) | [L0-02.svg](../assets/diagrams/L0-02.svg) |
| 02.1 Capture & qualify demand | group | Requesters/Business; Portfolio Management; PMO | 3 | [02.1.bpmn](../diagrams/bpmn/generated/02.1.bpmn) | [02.1.svg](../assets/diagrams/02.1.svg) |
| 02.2 Prioritize & decide investments | group | Portfolio Management | 3 | [02.2.bpmn](../diagrams/bpmn/generated/02.2.bpmn) | [02.2.svg](../assets/diagrams/02.2.svg) |
| 02.3 Plan & roadmap the portfolio | group | Portfolio Management | 4 | [02.3.bpmn](../diagrams/bpmn/generated/02.3.bpmn) | [02.3.svg](../assets/diagrams/02.3.svg) |
| 02.4 Fund the portfolio & track budget | group | Portfolio Management; Finance | 3 | [02.4.bpmn](../diagrams/bpmn/generated/02.4.bpmn) | [02.4.svg](../assets/diagrams/02.4.svg) |
| 02.5 Realize value & benefits | group | Portfolio Management | 2 | [02.5.bpmn](../diagrams/bpmn/generated/02.5.bpmn) | [02.5.svg](../assets/diagrams/02.5.svg) |
| L0-03 Agile Program & Delivery Management | area | RTE/Program; Agile Teams | 4 | [L0-03.bpmn](../diagrams/bpmn/generated/L0-03.bpmn) | [L0-03.svg](../assets/diagrams/L0-03.svg) |
| 03.1 Plan quarterly (SAFe PI cadence) | group | RTE/Program; Agile Teams | 6 | [03.1.bpmn](../diagrams/bpmn/generated/03.1.bpmn) | [03.1.svg](../assets/diagrams/03.1.svg) |
| 03.2 Deliver at team level | group | Agile Teams | 4 | [03.2.bpmn](../diagrams/bpmn/generated/03.2.bpmn) | [03.2.svg](../assets/diagrams/03.2.svg) |
| 03.3 Manage releases & hybrid projects | group | RTE/Program | 3 | [03.3.bpmn](../diagrams/bpmn/generated/03.3.bpmn) | [03.3.svg](../assets/diagrams/03.3.svg) |
| 03.4 Manage value streams | group | RTE/Program | 2 | [03.4.bpmn](../diagrams/bpmn/generated/03.4.bpmn) | [03.4.svg](../assets/diagrams/03.4.svg) |
| L0-04 Workforce & Resource Management | area | Resource Management; Portfolio Management | 5 | [L0-04.bpmn](../diagrams/bpmn/generated/L0-04.bpmn) | [L0-04.svg](../assets/diagrams/L0-04.svg) |
| 04.1 Maintain the workforce baseline | group | Resource Management; Finance (IT Planning) | 3 | [04.1.bpmn](../diagrams/bpmn/generated/04.1.bpmn) | [04.1.svg](../assets/diagrams/04.1.svg) |
| 04.2 Plan capacity | group | Resource Management; Portfolio Management | 3 | [04.2.bpmn](../diagrams/bpmn/generated/04.2.bpmn) | [04.2.svg](../assets/diagrams/04.2.svg) |
| 04.3 Allocate resources & track utilization | group | Resource Management; Portfolio Management | 4 | [04.3.bpmn](../diagrams/bpmn/generated/04.3.bpmn) | [04.3.svg](../assets/diagrams/04.3.svg) |
| 04.4 Manage positions | group | Portfolio Management; HR/Approvers; Finance (IT Planning) | 3 | [04.4.bpmn](../diagrams/bpmn/generated/04.4.bpmn) | [04.4.svg](../assets/diagrams/04.4.svg) |
| 04.5 Track & approve time | group | Resource Management; Finance (IT Planning) | 3 | [04.5.bpmn](../diagrams/bpmn/generated/04.5.bpmn) | [04.5.svg](../assets/diagrams/04.5.svg) |
| L0-05 IT Financial Planning & Budgeting | area | IT Finance; Budget Owners; CIO | 8 | [L0-05.bpmn](../diagrams/bpmn/generated/L0-05.bpmn) | [L0-05.svg](../assets/diagrams/L0-05.svg) |
| 05.1 Build the annual IT budget | group | IT Finance; Budget Owners; CIO | 5 | [05.1.bpmn](../diagrams/bpmn/generated/05.1.bpmn) | [05.1.svg](../assets/diagrams/05.1.svg) |
| 05.2 Forecast on a rolling cadence | group | IT Finance; Budget Owners | 4 | [05.2.bpmn](../diagrams/bpmn/generated/05.2.bpmn) | [05.2.svg](../assets/diagrams/05.2.svg) |
| 05.3 Analyze variance & reforecast | group | IT Finance; Budget Owners | 3 | [05.3.bpmn](../diagrams/bpmn/generated/05.3.bpmn) | [05.3.svg](../assets/diagrams/05.3.svg) |
| 05.4 Plan workforce & labor cost | group | IT Finance; Budget Owners | 3 | [05.4.bpmn](../diagrams/bpmn/generated/05.4.bpmn) | [05.4.svg](../assets/diagrams/05.4.svg) |
| 05.5 Plan vendors & contracts | group | IT Finance; Budget Owners | 3 | [05.5.bpmn](../diagrams/bpmn/generated/05.5.bpmn) | [05.5.svg](../assets/diagrams/05.5.svg) |
| 05.6 Plan capital & assets | group | IT Finance; Budget Owners | 2 | [05.6.bpmn](../diagrams/bpmn/generated/05.6.bpmn) | [05.6.svg](../assets/diagrams/05.6.svg) |
| 05.7 Plan project & investment finances | group | IT Finance; Budget Owners | 3 | [05.7.bpmn](../diagrams/bpmn/generated/05.7.bpmn) | [05.7.svg](../assets/diagrams/05.7.svg) |
| 05.8 Build & review a zero-based budget | group | IT Finance; Budget Owners; FP&A; CIO | 6 | [05.8.bpmn](../diagrams/bpmn/generated/05.8.bpmn) | [05.8.svg](../assets/diagrams/05.8.svg) |
| L0-06 Cost Transparency & TBM Operations | area | TBM Office/IT Finance | 6 | [L0-06.bpmn](../diagrams/bpmn/generated/L0-06.bpmn) | [L0-06.svg](../assets/diagrams/L0-06.svg) |
| 06.1 Run the monthly allocation & close | group | TBM Office/IT Finance; Costing Admin | 4 | [06.1.bpmn](../diagrams/bpmn/generated/06.1.bpmn) | [06.1.svg](../assets/diagrams/06.1.svg) |
| 06.2 Analyze cost, variance & investment mix | group | TBM Office/IT Finance | 3 | [06.2.bpmn](../diagrams/bpmn/generated/06.2.bpmn) | [06.2.svg](../assets/diagrams/06.2.svg) |
| 06.3 Compute application & service TCO | group | TBM Office/IT Finance; App/Service Owners | 4 | [06.3.bpmn](../diagrams/bpmn/generated/06.3.bpmn) | [06.3.svg](../assets/diagrams/06.3.svg) |
| 06.4 Cost labor & capitalize | group | TBM Office/IT Finance; Costing Admin | 6 | [06.4.bpmn](../diagrams/bpmn/generated/06.4.bpmn) | [06.4.svg](../assets/diagrams/06.4.svg) |
| 06.5 Manage vendor & asset cost | group | TBM Office/IT Finance | 2 | [06.5.bpmn](../diagrams/bpmn/generated/06.5.bpmn) | [06.5.svg](../assets/diagrams/06.5.svg) |
| 06.6 Benchmark against peers | group | TBM Office/IT Finance | 2 | [06.6.bpmn](../diagrams/bpmn/generated/06.6.bpmn) | [06.6.svg](../assets/diagrams/06.6.svg) |
| L0-07 Cloud Financial Management (FinOps) | area | FinOps Practitioner | 6 | [L0-07.bpmn](../diagrams/bpmn/generated/L0-07.bpmn) | [L0-07.svg](../assets/diagrams/L0-07.svg) |
| 07.1 Establish the cloud cost data foundation | group | FinOps Practitioner; Engineering | 4 | [07.1.bpmn](../diagrams/bpmn/generated/07.1.bpmn) | [07.1.svg](../assets/diagrams/07.1.svg) |
| 07.2 Allocate cloud cost & govern tagging | group | FinOps Practitioner | 4 | [07.2.bpmn](../diagrams/bpmn/generated/07.2.bpmn) | [07.2.svg](../assets/diagrams/07.2.svg) |
| 07.3 Report cloud cost, unit economics & sustainability | group | FinOps Practitioner | 4 | [07.3.bpmn](../diagrams/bpmn/generated/07.3.bpmn) | [07.3.svg](../assets/diagrams/07.3.svg) |
| 07.4 Manage anomalies | group | FinOps Practitioner | 2 | [07.4.bpmn](../diagrams/bpmn/generated/07.4.bpmn) | [07.4.svg](../assets/diagrams/07.4.svg) |
| 07.5 Optimize usage & rates | group | FinOps Practitioner | 4 | [07.5.bpmn](../diagrams/bpmn/generated/07.5.bpmn) | [07.5.svg](../assets/diagrams/07.5.svg) |
| 07.6 Plan & forecast cloud spend | group | FinOps Practitioner; Engineering | 3 | [07.6.bpmn](../diagrams/bpmn/generated/07.6.bpmn) | [07.6.svg](../assets/diagrams/07.6.svg) |
| L0-08 Consumption, Chargeback & Value Management | area | TBM Office | 2 | [L0-08.bpmn](../diagrams/bpmn/generated/L0-08.bpmn) | [L0-08.svg](../assets/diagrams/L0-08.svg) |
| 08.1 Show back & bill for IT | group | TBM Office | 3 | [08.1.bpmn](../diagrams/bpmn/generated/08.1.bpmn) | [08.1.svg](../assets/diagrams/08.1.svg) |
| 08.2 Engage the business & steer value | group | TBM Office; CIO/CFO | 3 | [08.2.bpmn](../diagrams/bpmn/generated/08.2.bpmn) | [08.2.svg](../assets/diagrams/08.2.svg) |
| L0-10 Platform Configuration, Data & Administration | area | Platform Admins; TBM Office; SPM Governance | 7 | [L0-10.bpmn](../diagrams/bpmn/generated/L0-10.bpmn) | [L0-10.svg](../assets/diagrams/L0-10.svg) |
| 10.1 Configure Targetprocess | group | Platform Admins | 5 | [10.1.bpmn](../diagrams/bpmn/generated/10.1.bpmn) | [10.1.svg](../assets/diagrams/10.1.svg) |
| 10.2 Configure Costing | group | Platform Admins | 2 | [10.2.bpmn](../diagrams/bpmn/generated/10.2.bpmn) | [10.2.svg](../assets/diagrams/10.2.svg) |
| 10.3 Configure Planning | group | Platform Admins | 2 | [10.3.bpmn](../diagrams/bpmn/generated/10.3.bpmn) | [10.3.svg](../assets/diagrams/10.3.svg) |
| 10.4 Configure Cloudability | group | Platform Admins | 2 | [10.4.bpmn](../diagrams/bpmn/generated/10.4.bpmn) | [10.4.svg](../assets/diagrams/10.4.svg) |
| 10.5 Operate cross-product data & integrations | group | TBM Office; Integration Team | 2 | [10.5.bpmn](../diagrams/bpmn/generated/10.5.bpmn) | [10.5.svg](../assets/diagrams/10.5.svg) |
| 10.6 Run the practices & grow maturity | group | TBM Office; FinOps Team; SPM Governance | 4 | [10.6.bpmn](../diagrams/bpmn/generated/10.6.bpmn) | [10.6.svg](../assets/diagrams/10.6.svg) |
| 10.7 Run AI-assisted planning & delivery intelligence | group | Platform Admins; SPM Governance | 3 | [10.7.bpmn](../diagrams/bpmn/generated/10.7.bpmn) | [10.7.svg](../assets/diagrams/10.7.svg) |