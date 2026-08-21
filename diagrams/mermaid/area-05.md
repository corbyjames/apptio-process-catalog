# 05 IT Financial Planning & Budgeting — L1/L2 Diagrams

Generated — edit `data/catalog.yaml`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N05_1[["05.1 Annual IT Budgeting"]]
  S --> N05_1
  N05_2[["05.2 Rolling & Periodic Forecasting"]]
  N05_1 --> N05_2
  N05_3[["05.3 Variance Analysis & Reforecasting"]]
  N05_2 --> N05_3
  N05_4[["05.4 Workforce & Labor Cost Planning"]]
  N05_3 --> N05_4
  N05_5[["05.5 Vendor & Contract Planning"]]
  N05_4 --> N05_5
  N05_6[["05.6 Capital & Asset Planning"]]
  N05_5 --> N05_6
  N05_7[["05.7 Project & Investment Financial Planning"]]
  N05_6 --> N05_7
  N05_7 --> E(((end)))
```

## 05.1 Annual IT Budgeting (L2)

```mermaid
flowchart LR
  S((start))
  N05_1_1["05.1.1 Establish plan structure & baseline<br/><i>IT Finance · Any</i>"]
  S --> N05_1_1
  N05_1_2["05.1.2 Set & distribute top-down targets<br/><i>CIO · Any</i>"]
  N05_1_1 --> N05_1_2
  N05_1_3["05.1.3 Enter bottom-up budgets<br/><i>Budget owners · Any</i>"]
  N05_1_2 --> N05_1_3
  N05_1_4["05.1.4 Review, iterate & approve budget<br/><i>IT Finance · Any</i>"]
  N05_1_3 --> N05_1_4
  N05_1_5["05.1.5 Finalize budget of record<br/><i>IT Finance · Any</i>"]
  N05_1_4 --> N05_1_5
  N05_1_5 --> E(((end)))
```

## 05.2 Rolling & Periodic Forecasting (L2)

```mermaid
flowchart LR
  S((start))
  N05_2_1["05.2.1 Create forecast seeded with actuals<br/><i>IT Finance · Any</i>"]
  S --> N05_2_1
  N05_2_2["05.2.2 Update forecasts (driver & AI-assisted)<br/><i>IT Finance · Any</i>"]
  N05_2_1 --> N05_2_2
  N05_2_3["05.2.3 Model what-if scenarios<br/><i>IT Finance · Any</i>"]
  N05_2_2 --> N05_2_3
  N05_2_4["05.2.4 Submit & sign off forecast<br/><i>Budget owners · Any</i>"]
  N05_2_3 --> N05_2_4
  N05_2_4 --> E(((end)))
```

## 05.3 Variance Analysis & Reforecasting (L2)

```mermaid
flowchart LR
  S((start))
  N05_3_1["05.3.1 Load & reconcile actuals to plan<br/><i>IT Finance · Any</i>"]
  S --> N05_3_1
  N05_3_2["05.3.2 Analyze variances with thresholds<br/><i>IT Finance · Any</i>"]
  N05_3_1 --> N05_3_2
  N05_3_3["05.3.3 Narrate variance & reforecast<br/><i>Budget owners · Any</i>"]
  N05_3_2 --> N05_3_3
  N05_3_3 --> E(((end)))
```

## 05.4 Workforce & Labor Cost Planning (L2)

```mermaid
flowchart LR
  S((start))
  N05_4_1["05.4.1 Plan positions & FTEs<br/><i>Budget owners · Any</i>"]
  S --> N05_4_1
  N05_4_2["05.4.2 Plan compensation & adjustments<br/><i>IT Finance (restricted) · Any</i>"]
  N05_4_1 --> N05_4_2
  N05_4_3["05.4.3 Allocate planned labor<br/><i>IT Finance · Any</i>"]
  N05_4_2 --> N05_4_3
  N05_4_3 --> E(((end)))
```

## 05.5 Vendor & Contract Planning (L2)

```mermaid
flowchart LR
  S((start))
  N05_5_1["05.5.1 Maintain contract line items<br/><i>IT Finance · Any</i>"]
  S --> N05_5_1
  N05_5_2["05.5.2 Plan renewals & escalations<br/><i>Vendor Mgmt · Any</i>"]
  N05_5_1 --> N05_5_2
  N05_5_3["05.5.3 Delegate contract costs<br/><i>IT Finance · Any</i>"]
  N05_5_2 --> N05_5_3
  N05_5_3 --> E(((end)))
```

## 05.6 Capital & Asset Planning (L2)

```mermaid
flowchart LR
  S((start))
  N05_6_1["05.6.1 Plan asset purchases & lifecycle<br/><i>Budget owners · Any</i>"]
  S --> N05_6_1
  N05_6_2["05.6.2 Generate depreciation schedules<br/><i>IT Finance · Any</i>"]
  N05_6_1 --> N05_6_2
  N05_6_2 --> E(((end)))
```

## 05.7 Project & Investment Financial Planning (L2)

```mermaid
flowchart LR
  S((start))
  N05_7_1["05.7.1 Define investments & cost treatment<br/><i>PMO · Any</i>"]
  S --> N05_7_1
  N05_7_2["05.7.2 Plan investment labor & cross-charge<br/><i>PMO · Any</i>"]
  N05_7_1 --> N05_7_2
  N05_7_3["05.7.3 Operate the investment loop with ATP<br/><i>IT Finance · Any</i>"]
  N05_7_2 --> N05_7_3
  N05_7_3 --> E(((end)))
```
