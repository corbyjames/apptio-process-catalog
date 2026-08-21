# 09 Cross-Tool End-to-End Flows — L1/L2 Diagrams

Generated — edit `data/catalog.yaml`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N09_1[["09.1 UC3 - Portfolio Target Spend (targets down)"]]
  S --> N09_1
  N09_2[["09.2 UC2 - Work Allocation Rates (rates back)"]]
  N09_1 --> N09_2
  N09_3[["09.3 UC1 - Labor Capitalization (actuals in)"]]
  N09_2 --> N09_3
  N09_4[["09.4 UC4 - Cost Actuals to App TCO (TCO up)"]]
  N09_3 --> N09_4
  N09_5[["09.5 Cloud-to-TBM Flow"]]
  N09_4 --> N09_5
  N09_6[["09.6 Investment Loop"]]
  N09_5 --> N09_6
  N09_6 --> E(((end)))
```

## 09.1 UC3 - Portfolio Target Spend (targets down) (L2)

```mermaid
flowchart LR
  S((start))
  N09_1_1["09.1.1 Flow: Planning -> Targetprocess targets & positions<br/><i>IT Planning (Finance) · Any</i>"]
  S --> N09_1_1
  N09_1_1 --> E(((end)))
```

## 09.2 UC2 - Work Allocation Rates (rates back) (L2)

```mermaid
flowchart LR
  S((start))
  N09_2_1["09.2.1 Flow: Costing -> Targetprocess blended rates<br/><i>Costing (TBM Studio) · Any</i>"]
  S --> N09_2_1
  N09_2_1 --> E(((end)))
```

## 09.3 UC1 - Labor Capitalization (actuals in) (L2)

```mermaid
flowchart LR
  S((start))
  N09_3_1["09.3.1 Flow: Targetprocess -> Costing -> SAP actuals<br/><i>ATP · Any</i>"]
  S --> N09_3_1
  N09_3_1 --> E(((end)))
```

## 09.4 UC4 - Cost Actuals to App TCO (TCO up) (L2)

```mermaid
flowchart LR
  S((start))
  N09_4_1["09.4.1 Flow: actuals roll up to Application TCO<br/><i>Costing · Any</i>"]
  S --> N09_4_1
  N09_4_1 --> E(((end)))
```

## 09.5 Cloud-to-TBM Flow (L2)

```mermaid
flowchart LR
  S((start))
  N09_5_1["09.5.1 Flow: Cloudability -> Costing hybrid TCO<br/><i>Cloudability · Any</i>"]
  S --> N09_5_1
  N09_5_1 --> E(((end)))
```

## 09.6 Investment Loop (L2)

```mermaid
flowchart LR
  S((start))
  N09_6_1["09.6.1 Flow: ATP <-> Costing/Planning investment round-trip<br/><i>ATP · Hybrid</i>"]
  S --> N09_6_1
  N09_6_1 --> E(((end)))
```
