# 03 Agile Program & Delivery Management — L1/L2 diagrams

Generated from `data/catalog.json`. BPMN versions: see `../bpmn/generated/`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N03_1[["03.1 Plan quarterly (SAFe PI cadence)"]]
  S --> N03_1
  N03_2[["03.2 Deliver at team level"]]
  N03_1 --> N03_2
  N03_3[["03.3 Manage releases & hybrid projects"]]
  N03_2 --> N03_3
  N03_4[["03.4 Manage value streams"]]
  N03_3 --> N03_4
  N03_4 --> E(((end)))
```

## 03.1 Plan quarterly (SAFe PI cadence) (L2)

```mermaid
flowchart LR
  S((start))
  N03_1_1["03.1.1 Assess & prepare quarterly planning readiness<br/><i>RTE/Program · Agile</i>"]
  S --> N03_1_1
  N03_1_2["03.1.2 Run quarterly planning event<br/><i>Agile Teams · Agile</i>"]
  N03_1_1 --> N03_1_2
  N03_1_3["03.1.3 Commit & publish PI objectives<br/><i>Agile Teams · Agile</i>"]
  N03_1_2 --> N03_1_3
  N03_1_4["03.1.4 Baseline commitments & track PI execution<br/><i>RTE/Program · Agile</i>"]
  N03_1_3 --> N03_1_4
  N03_1_5["03.1.5 Manage PI risks (ROAM) & confidence vote<br/><i>RTE/Program · Agile</i>"]
  N03_1_4 --> N03_1_5
  N03_1_6["03.1.6 Run system demo & Inspect and Adapt<br/><i>RTE/Program · Agile</i>"]
  N03_1_5 --> N03_1_6
  N03_1_6 --> E(((end)))
```

## 03.2 Deliver at team level (L2)

```mermaid
flowchart LR
  S((start))
  N03_2_1["03.2.1 Plan & execute iterations<br/><i>Agile Teams · Agile</i>"]
  S --> N03_2_1
  N03_2_2["03.2.2 Track flow & progress<br/><i>Agile Teams · Agile</i>"]
  N03_2_1 --> N03_2_2
  N03_2_3["03.2.3 Manage impediments & dependencies<br/><i>Agile Teams · Any</i>"]
  N03_2_2 --> N03_2_3
  N03_2_4["03.2.4 Sync with dev tools<br/><i>Agile Teams · Agile</i>"]
  N03_2_3 --> N03_2_4
  N03_2_4 --> E(((end)))
```

## 03.3 Manage releases & hybrid projects (L2)

```mermaid
flowchart LR
  S((start))
  N03_3_1["03.3.1 Plan releases & enable release packages<br/><i>RTE/Program · Any</i>"]
  S --> N03_3_1
  N03_3_2["03.3.2 Manage hybrid & waterfall projects<br/><i>RTE/Program · Hybrid</i>"]
  N03_3_1 --> N03_3_2
  N03_3_3["03.3.3 Govern stage-gates & milestones for traditional initiatives<br/><i>RTE/Program · Traditional</i>"]
  N03_3_2 --> N03_3_3
  N03_3_3 --> E(((end)))
```

## 03.4 Manage value streams (L2)

```mermaid
flowchart LR
  S((start))
  N03_4_1["03.4.1 Identify & map value streams<br/><i>RTE/Program · Agile</i>"]
  S --> N03_4_1
  N03_4_2["03.4.2 Measure & improve flow<br/><i>RTE/Program · Agile</i>"]
  N03_4_1 --> N03_4_2
  N03_4_2 --> E(((end)))
```
