# 05 IT Financial Planning & Budgeting — L1/L2 diagrams

Generated from `data/catalog.json`. BPMN versions: see `../bpmn/generated/`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N05_1[["05.1 Build the annual IT budget"]]
  S --> N05_1
  N05_2[["05.2 Forecast on a rolling cadence"]]
  N05_1 --> N05_2
  N05_3[["05.3 Analyze variance & reforecast"]]
  N05_2 --> N05_3
  N05_4[["05.4 Plan workforce & labor cost"]]
  N05_3 --> N05_4
  N05_5[["05.5 Plan vendors & contracts"]]
  N05_4 --> N05_5
  N05_6[["05.6 Plan capital & assets"]]
  N05_5 --> N05_6
  N05_7[["05.7 Plan project & investment finances"]]
  N05_6 --> N05_7
  N05_8[["05.8 Build & review a zero-based budget"]]
  N05_7 --> N05_8
  N05_8 --> E(((end)))
```

## 05.1 Build the annual IT budget (L2)

```mermaid
flowchart LR
  S((start))
  N05_1_1["05.1.1 Establish plan structure & baseline<br/><i>IT Finance · Any</i>"]
  S --> N05_1_1
  N05_1_2["05.1.2 Set & distribute top-down targets<br/><i>CIO · Any</i>"]
  N05_1_1 --> N05_1_2
  N05_1_3["05.1.3 Enter bottom-up budgets<br/><i>Budget Owners · Any</i>"]
  N05_1_2 --> N05_1_3
  N05_1_4["05.1.4 Review, iterate & approve budget<br/><i>IT Finance · Any</i>"]
  N05_1_3 --> N05_1_4
  N05_1_5["05.1.5 Finalize budget of record<br/><i>IT Finance · Any</i>"]
  N05_1_4 --> N05_1_5
  N05_1_5 --> E(((end)))
```

## 05.2 Forecast on a rolling cadence (L2)

```mermaid
flowchart LR
  S((start))
  N05_2_1["05.2.1 Create forecast seeded with actuals<br/><i>IT Finance · Any</i>"]
  S --> N05_2_1
  N05_2_2["05.2.2 Update forecasts (driver & AI-assisted)<br/><i>IT Finance · Any</i>"]
  N05_2_1 --> N05_2_2
  N05_2_3["05.2.3 Model what-if scenarios<br/><i>IT Finance · Any</i>"]
  N05_2_2 --> N05_2_3
  N05_2_4["05.2.4 Submit & sign off forecast<br/><i>Budget Owners · Any</i>"]
  N05_2_3 --> N05_2_4
  N05_2_4 --> E(((end)))
```

## 05.3 Analyze variance & reforecast (L2)

```mermaid
flowchart LR
  S((start))
  N05_3_1["05.3.1 Load & reconcile actuals to plan<br/><i>IT Finance · Any</i>"]
  S --> N05_3_1
  N05_3_2["05.3.2 Analyze variances with thresholds<br/><i>IT Finance · Any</i>"]
  N05_3_1 --> N05_3_2
  N05_3_3["05.3.3 Narrate variance & reforecast<br/><i>Budget Owners · Any</i>"]
  N05_3_2 --> N05_3_3
  N05_3_3 --> E(((end)))
```

## 05.4 Plan workforce & labor cost (L2)

```mermaid
flowchart LR
  S((start))
  N05_4_1["05.4.1 Plan positions & FTEs<br/><i>Budget Owners · Any</i>"]
  S --> N05_4_1
  N05_4_2["05.4.2 Plan compensation & adjustments<br/><i>IT Finance · Any</i>"]
  N05_4_1 --> N05_4_2
  N05_4_3["05.4.3 Allocate planned labor<br/><i>IT Finance · Any</i>"]
  N05_4_2 --> N05_4_3
  N05_4_3 --> E(((end)))
```

## 05.5 Plan vendors & contracts (L2)

```mermaid
flowchart LR
  S((start))
  N05_5_1["05.5.1 Maintain contract line items<br/><i>IT Finance · Any</i>"]
  S --> N05_5_1
  N05_5_2["05.5.2 Plan renewals & escalations<br/><i>Budget Owners · Any</i>"]
  N05_5_1 --> N05_5_2
  N05_5_3["05.5.3 Delegate contract costs<br/><i>IT Finance · Any</i>"]
  N05_5_2 --> N05_5_3
  N05_5_3 --> E(((end)))
```

## 05.6 Plan capital & assets (L2)

```mermaid
flowchart LR
  S((start))
  N05_6_1["05.6.1 Plan asset purchases & lifecycle<br/><i>Budget Owners · Any</i>"]
  S --> N05_6_1
  N05_6_2["05.6.2 Generate depreciation schedules<br/><i>IT Finance · Any</i>"]
  N05_6_1 --> N05_6_2
  N05_6_2 --> E(((end)))
```

## 05.7 Plan project & investment finances (L2)

```mermaid
flowchart LR
  S((start))
  N05_7_1["05.7.1 Define investments & cost treatment<br/><i>Budget Owners · Any</i>"]
  S --> N05_7_1
  N05_7_2["05.7.2 Plan investment labor & cross-charge<br/><i>Budget Owners · Any</i>"]
  N05_7_1 --> N05_7_2
  N05_7_3["05.7.3 Operate the investment loop with ATP<br/><i>IT Finance · Any</i>"]
  N05_7_2 --> N05_7_3
  N05_7_3 --> E(((end)))
```

## 05.8 Build & review a zero-based budget (L2)

```mermaid
flowchart LR
  S((start))
  N05_8_1["05.8.1 Scope the ZBB cycle & select decision units<br/><i>CIO · Any</i>"]
  S --> N05_8_1
  N05_8_2["05.8.2 Build the cost-driver fact base & activity inventory<br/><i>IT Finance · Any</i>"]
  N05_8_1 --> N05_8_2
  N05_8_3["05.8.3 Build decision packages at tiered service levels<br/><i>Budget Owners · Any</i>"]
  N05_8_2 --> N05_8_3
  N05_8_4["05.8.4 Rank packages & set the funding cut-line<br/><i>CIO · Any</i>"]
  N05_8_3 --> N05_8_4
  N05_8_5["05.8.5 Approve zero-based budget & release freed spend to the investment envelope<br/><i>CIO · Any</i>"]
  N05_8_4 --> N05_8_5
  N05_8_6["05.8.6 Monitor package commitments & sustain the zero-based mindset<br/><i>FP&A · Any</i>"]
  N05_8_5 --> N05_8_6
  N05_8_6 --> E(((end)))
```
