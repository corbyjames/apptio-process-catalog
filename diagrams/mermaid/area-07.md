# 07 Cloud Financial Management (FinOps) — L1/L2 Diagrams

Generated — edit `data/catalog.yaml`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N07_1[["07.1 Cloud Cost Data Foundation"]]
  S --> N07_1
  N07_2[["07.2 Cloud Allocation & Tagging Governance"]]
  N07_1 --> N07_2
  N07_3[["07.3 Cloud Reporting & Unit Economics"]]
  N07_2 --> N07_3
  N07_4[["07.4 Anomaly Management"]]
  N07_3 --> N07_4
  N07_5[["07.5 Usage & Rate Optimization"]]
  N07_4 --> N07_5
  N07_6[["07.6 Cloud Planning & Forecasting"]]
  N07_5 --> N07_6
  N07_7[["07.7 Cloud Sustainability"]]
  N07_6 --> N07_7
  N07_7 --> E(((end)))
```

## 07.1 Cloud Cost Data Foundation (L2)

```mermaid
flowchart LR
  S((start))
  N07_1_1["07.1.1 Connect cloud billing accounts<br/><i>FinOps Practitioner · Any</i>"]
  S --> N07_1_1
  N07_1_2["07.1.2 Ingest custom & FOCUS data<br/><i>FinOps Practitioner · Any</i>"]
  N07_1_1 --> N07_1_2
  N07_1_3["07.1.3 Onboard container cost data<br/><i>Platform Eng · Any</i>"]
  N07_1_2 --> N07_1_3
  N07_1_4["07.1.4 Validate & reprocess data<br/><i>FinOps Practitioner · Any</i>"]
  N07_1_3 --> N07_1_4
  N07_1_4 --> E(((end)))
```

## 07.2 Cloud Allocation & Tagging Governance (L2)

```mermaid
flowchart LR
  S((start))
  N07_2_1["07.2.1 Design business mappings & views<br/><i>FinOps Practitioner · Any</i>"]
  S --> N07_2_1
  N07_2_2["07.2.2 Govern tagging<br/><i>FinOps · Any</i>"]
  N07_2_1 --> N07_2_2
  N07_2_3["07.2.3 Allocate shared costs<br/><i>FinOps Practitioner · Any</i>"]
  N07_2_2 --> N07_2_3
  N07_2_4["07.2.4 Map cloud spend to TBM taxonomy<br/><i>FinOps · Any</i>"]
  N07_2_3 --> N07_2_4
  N07_2_4 --> E(((end)))
```

## 07.3 Cloud Reporting & Unit Economics (L2)

```mermaid
flowchart LR
  S((start))
  N07_3_1["07.3.1 Operate dashboards & scheduled reports<br/><i>FinOps · Any</i>"]
  S --> N07_3_1
  N07_3_2["07.3.2 Benchmark efficiency<br/><i>FinOps · Any</i>"]
  N07_3_1 --> N07_3_2
  N07_3_3["07.3.3 Track unit economics<br/><i>FinOps · Any</i>"]
  N07_3_2 --> N07_3_3
  N07_3_3 --> E(((end)))
```

## 07.4 Anomaly Management (L2)

```mermaid
flowchart LR
  S((start))
  N07_4_1["07.4.1 Configure anomaly detection<br/><i>FinOps Practitioner · Any</i>"]
  S --> N07_4_1
  N07_4_2["07.4.2 Triage, route & resolve anomalies<br/><i>FinOps · Any</i>"]
  N07_4_1 --> N07_4_2
  N07_4_2 --> E(((end)))
```

## 07.5 Usage & Rate Optimization (L2)

```mermaid
flowchart LR
  S((start))
  N07_5_1["07.5.1 Run the rightsizing cadence<br/><i>FinOps · Any</i>"]
  S --> N07_5_1
  N07_5_2["07.5.2 Eliminate waste & govern pre-deployment<br/><i>FinOps · Any</i>"]
  N07_5_1 --> N07_5_2
  N07_5_3["07.5.3 Manage commitments (assisted)<br/><i>FinOps · Any</i>"]
  N07_5_2 --> N07_5_3
  N07_5_4["07.5.4 Automate commitments (Savings Automation)<br/><i>FinOps admin (RateOptimizationFullAccess) · Any</i>"]
  N07_5_3 --> N07_5_4
  N07_5_4 --> E(((end)))
```

## 07.6 Cloud Planning & Forecasting (L2)

```mermaid
flowchart LR
  S((start))
  N07_6_1["07.6.1 Manage cloud budgets<br/><i>FinOps · Any</i>"]
  S --> N07_6_1
  N07_6_2["07.6.2 Forecast cloud spend<br/><i>FinOps · Any</i>"]
  N07_6_1 --> N07_6_2
  N07_6_3["07.6.3 Plan migrations & new workloads<br/><i>Cloud architects · Any</i>"]
  N07_6_2 --> N07_6_3
  N07_6_3 --> E(((end)))
```

## 07.7 Cloud Sustainability (L2)

```mermaid
flowchart LR
  S((start))
  N07_7_1["07.7.1 Report & act on sustainability<br/><i>FinOps · Any</i>"]
  S --> N07_7_1
  N07_7_1 --> E(((end)))
```
