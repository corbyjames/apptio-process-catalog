# 07 Cloud Financial Management (FinOps) — L1/L2 diagrams

Generated from `data/catalog.json`. BPMN versions: see `../bpmn/generated/`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N07_1[["07.1 Establish the cloud cost data foundation"]]
  S --> N07_1
  N07_2[["07.2 Allocate cloud cost & govern tagging"]]
  N07_1 --> N07_2
  N07_3[["07.3 Report cloud cost, unit economics & sustainability"]]
  N07_2 --> N07_3
  N07_4[["07.4 Manage anomalies"]]
  N07_3 --> N07_4
  N07_5[["07.5 Optimize usage & rates"]]
  N07_4 --> N07_5
  N07_6[["07.6 Plan & forecast cloud spend"]]
  N07_5 --> N07_6
  N07_6 --> E(((end)))
```

## 07.1 Establish the cloud cost data foundation (L2)

```mermaid
flowchart LR
  S((start))
  N07_1_1["07.1.1 Connect cloud billing accounts<br/><i>FinOps Practitioner · Any</i>"]
  S --> N07_1_1
  N07_1_2["07.1.2 Ingest custom & FOCUS data<br/><i>FinOps Practitioner · Any</i>"]
  N07_1_1 --> N07_1_2
  N07_1_3["07.1.3 Onboard container cost data<br/><i>Engineering · Any</i>"]
  N07_1_2 --> N07_1_3
  N07_1_4["07.1.4 Validate & reprocess data<br/><i>FinOps Practitioner · Any</i>"]
  N07_1_3 --> N07_1_4
  N07_1_4 --> E(((end)))
```

## 07.2 Allocate cloud cost & govern tagging (L2)

```mermaid
flowchart LR
  S((start))
  N07_2_1["07.2.1 Design business mappings & views<br/><i>FinOps Practitioner · Any</i>"]
  S --> N07_2_1
  N07_2_2["07.2.2 Govern tagging<br/><i>FinOps Practitioner · Any</i>"]
  N07_2_1 --> N07_2_2
  N07_2_3["07.2.3 Allocate shared costs<br/><i>FinOps Practitioner · Any</i>"]
  N07_2_2 --> N07_2_3
  N07_2_4["07.2.4 Map cloud spend to TBM taxonomy<br/><i>FinOps Practitioner · Any</i>"]
  N07_2_3 --> N07_2_4
  N07_2_4 --> E(((end)))
```

## 07.3 Report cloud cost, unit economics & sustainability (L2)

```mermaid
flowchart LR
  S((start))
  N07_3_1["07.3.1 Operate dashboards & scheduled reports<br/><i>FinOps Practitioner · Any</i>"]
  S --> N07_3_1
  N07_3_2["07.3.2 Benchmark efficiency<br/><i>FinOps Practitioner · Any</i>"]
  N07_3_1 --> N07_3_2
  N07_3_3["07.3.3 Track unit economics<br/><i>FinOps Practitioner · Any</i>"]
  N07_3_2 --> N07_3_3
  N07_3_4["07.3.4 Report & act on sustainability<br/><i>FinOps Practitioner · Any</i>"]
  N07_3_3 --> N07_3_4
  N07_3_4 --> E(((end)))
```

## 07.4 Manage anomalies (L2)

```mermaid
flowchart LR
  S((start))
  N07_4_1["07.4.1 Configure anomaly detection<br/><i>FinOps Practitioner · Any</i>"]
  S --> N07_4_1
  N07_4_2["07.4.2 Triage, route & resolve anomalies<br/><i>FinOps Practitioner · Any</i>"]
  N07_4_1 --> N07_4_2
  N07_4_2 --> E(((end)))
```

## 07.5 Optimize usage & rates (L2)

```mermaid
flowchart LR
  S((start))
  N07_5_1["07.5.1 Run the rightsizing cadence<br/><i>FinOps Practitioner · Any</i>"]
  S --> N07_5_1
  N07_5_2["07.5.2 Eliminate waste & govern pre-deployment<br/><i>FinOps Practitioner · Any</i>"]
  N07_5_1 --> N07_5_2
  N07_5_3["07.5.3 Manage commitments (assisted)<br/><i>FinOps Practitioner · Any</i>"]
  N07_5_2 --> N07_5_3
  N07_5_4["07.5.4 Automate commitments (Savings Automation)<br/><i>FinOps Practitioner · Any</i>"]
  N07_5_3 --> N07_5_4
  N07_5_4 --> E(((end)))
```

## 07.6 Plan & forecast cloud spend (L2)

```mermaid
flowchart LR
  S((start))
  N07_6_1["07.6.1 Manage cloud budgets<br/><i>FinOps Practitioner · Any</i>"]
  S --> N07_6_1
  N07_6_2["07.6.2 Forecast cloud spend<br/><i>FinOps Practitioner · Any</i>"]
  N07_6_1 --> N07_6_2
  N07_6_3["07.6.3 Plan migrations & new workloads<br/><i>Engineering · Any</i>"]
  N07_6_2 --> N07_6_3
  N07_6_3 --> E(((end)))
```
