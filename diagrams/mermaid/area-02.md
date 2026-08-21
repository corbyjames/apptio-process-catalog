# 02 Demand & Portfolio Investment Management — L1/L2 Diagrams

Generated — edit `data/catalog.yaml`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N02_1[["02.1 Demand Intake & Qualification"]]
  S --> N02_1
  N02_2[["02.2 Prioritization & Investment Decision"]]
  N02_1 --> N02_2
  N02_3[["02.3 Portfolio Planning & Roadmapping"]]
  N02_2 --> N02_3
  N02_4[["02.4 Portfolio Funding & Budget Tracking"]]
  N02_3 --> N02_4
  N02_5[["02.5 Value & Benefits Realization"]]
  N02_4 --> N02_5
  N02_5 --> E(((end)))
```

## 02.1 Demand Intake & Qualification (L2)

```mermaid
flowchart LR
  S((start))
  N02_1_1["02.1.1 Capture ideas & requests<br/><i>Requesters (any) · Any</i>"]
  S --> N02_1_1
  N02_1_2["02.1.2 Triage, categorize & qualify demand<br/><i>PMO · Any</i>"]
  N02_1_1 --> N02_1_2
  N02_1_3["02.1.3 Progress demand through Portfolio Kanban<br/><i>Portfolio Mgmt · Agile</i>"]
  N02_1_2 --> N02_1_3
  N02_1_3 --> E(((end)))
```

## 02.2 Prioritization & Investment Decision (L2)

```mermaid
flowchart LR
  S((start))
  N02_2_1["02.2.1 Build lean business case / epic hypothesis<br/><i>Epic owners · Any</i>"]
  S --> N02_2_1
  N02_2_2["02.2.2 Prioritize by value (WSJF / scoring)<br/><i>Portfolio Mgmt · Agile</i>"]
  N02_2_1 --> N02_2_2
  N02_2_3["02.2.3 Approve & fund investments<br/><i>Portfolio Mgmt · Hybrid</i>"]
  N02_2_2 --> N02_2_3
  N02_2_3 --> E(((end)))
```

## 02.3 Portfolio Planning & Roadmapping (L2)

```mermaid
flowchart LR
  S((start))
  N02_3_1["02.3.1 Build & maintain roadmaps<br/><i>Portfolio Mgmt · Any</i>"]
  S --> N02_3_1
  N02_3_2["02.3.2 Model scenarios & trade-offs<br/><i>Portfolio Mgmt · Any</i>"]
  N02_3_1 --> N02_3_2
  N02_3_3["02.3.3 Manage cross-initiative dependencies & risks<br/><i>Portfolio Mgmt · Any</i>"]
  N02_3_2 --> N02_3_3
  N02_3_4["02.3.4 Maintain one governed hybrid portfolio view<br/><i>Portfolio Mgmt · Hybrid</i>"]
  N02_3_3 --> N02_3_4
  N02_3_4 --> E(((end)))
```

## 02.4 Portfolio Funding & Budget Tracking (L2)

```mermaid
flowchart LR
  S((start))
  N02_4_1["02.4.1 Define funding model<br/><i>Finance · Hybrid</i>"]
  S --> N02_4_1
  N02_4_2["02.4.2 Receive & apply top-down targets<br/><i>Portfolio Mgmt · Any</i>"]
  N02_4_1 --> N02_4_2
  N02_4_3["02.4.3 Track portfolio budget vs actuals<br/><i>Portfolio Mgmt · Any</i>"]
  N02_4_2 --> N02_4_3
  N02_4_3 --> E(((end)))
```

## 02.5 Value & Benefits Realization (L2)

```mermaid
flowchart LR
  S((start))
  N02_5_1["02.5.1 Define expected outcomes & value metrics<br/><i>Epic owners · Any</i>"]
  S --> N02_5_1
  N02_5_2["02.5.2 Track realized value & feed decisions<br/><i>Portfolio Mgmt · Any</i>"]
  N02_5_1 --> N02_5_2
  N02_5_2 --> E(((end)))
```
