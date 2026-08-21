# 03 Agile Program & Delivery Management — L1/L2 Diagrams

Generated — edit `data/catalog.yaml`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N03_1[["03.1 PI Planning"]]
  S --> N03_1
  N03_2[["03.2 Team Delivery"]]
  N03_1 --> N03_2
  N03_3[["03.3 Release & Hybrid Project Management"]]
  N03_2 --> N03_3
  N03_4[["03.4 Value Stream Management"]]
  N03_3 --> N03_4
  N03_4 --> E(((end)))
```

## 03.1 PI Planning (L2)

```mermaid
flowchart LR
  S((start))
  N03_1_1["03.1.1 Assess & prepare PI readiness<br/><i>RTE/PI Coordinator · Agile</i>"]
  S --> N03_1_1
  N03_1_2["03.1.2 Run PI planning event<br/><i>ART (all roles) · Agile</i>"]
  N03_1_1 --> N03_1_2
  N03_1_3["03.1.3 Commit & publish PI objectives<br/><i>ART · Agile</i>"]
  N03_1_2 --> N03_1_3
  N03_1_4["03.1.4 Track PI execution & system demo<br/><i>RTE · Agile</i>"]
  N03_1_3 --> N03_1_4
  N03_1_4 --> E(((end)))
```

## 03.2 Team Delivery (L2)

```mermaid
flowchart LR
  S((start))
  N03_2_1["03.2.1 Plan & execute iterations<br/><i>Agile teams · Agile</i>"]
  S --> N03_2_1
  N03_2_2["03.2.2 Track flow & progress<br/><i>Teams · Agile</i>"]
  N03_2_1 --> N03_2_2
  N03_2_3["03.2.3 Manage impediments & dependencies<br/><i>Teams · Any</i>"]
  N03_2_2 --> N03_2_3
  N03_2_4["03.2.4 Sync with dev tools<br/><i>Teams · Agile</i>"]
  N03_2_3 --> N03_2_4
  N03_2_4 --> E(((end)))
```

## 03.3 Release & Hybrid Project Management (L2)

```mermaid
flowchart LR
  S((start))
  N03_3_1["03.3.1 Plan releases & enable release packages<br/><i>Release/Program Mgmt · Any</i>"]
  S --> N03_3_1
  N03_3_2["03.3.2 Manage hybrid & waterfall projects<br/><i>Project Managers · Hybrid</i>"]
  N03_3_1 --> N03_3_2
  N03_3_3["03.3.3 Govern stage-gates & milestones for traditional initiatives<br/><i>PMO · Traditional</i>"]
  N03_3_2 --> N03_3_3
  N03_3_3 --> E(((end)))
```

## 03.4 Value Stream Management (L2)

```mermaid
flowchart LR
  S((start))
  N03_4_1["03.4.1 Identify & map value streams<br/><i>Portfolio Mgmt · Agile</i>"]
  S --> N03_4_1
  N03_4_2["03.4.2 Measure & improve flow<br/><i>VS owners · Agile</i>"]
  N03_4_1 --> N03_4_2
  N03_4_2 --> E(((end)))
```
