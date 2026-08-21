# 08 Consumption, Chargeback & Value Management — L1/L2 Diagrams

Generated — edit `data/catalog.yaml`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N08_1[["08.1 Showback & Bill of IT"]]
  S --> N08_1
  N08_2[["08.2 Demand Shaping & BU Engagement"]]
  N08_1 --> N08_2
  N08_3[["08.3 Enterprise Business Management (EBM)"]]
  N08_2 --> N08_3
  N08_4[["08.4 Executive Value Operating Rhythm"]]
  N08_3 --> N08_4
  N08_4 --> E(((end)))
```

## 08.1 Showback & Bill of IT (L2)

```mermaid
flowchart LR
  S((start))
  N08_1_1["08.1.1 Allocate consumption to business units<br/><i>TBM Analyst · Any</i>"]
  S --> N08_1_1
  N08_1_2["08.1.2 Publish showback / Bill of IT<br/><i>TBM Office · Any</i>"]
  N08_1_1 --> N08_1_2
  N08_1_3["08.1.3 Price services & run chargeback<br/><i>IT Finance · Any</i>"]
  N08_1_2 --> N08_1_3
  N08_1_3 --> E(((end)))
```

## 08.2 Demand Shaping & BU Engagement (L2)

```mermaid
flowchart LR
  S((start))
  N08_2_1["08.2.1 Review costs with BU owners<br/><i>TBM Office · Any</i>"]
  S --> N08_2_1
  N08_2_1 --> E(((end)))
```

## 08.3 Enterprise Business Management (EBM) (L2)

```mermaid
flowchart LR
  S((start))
  N08_3_1["08.3.1 Extend costing beyond IT<br/><i>Enterprise Finance · Any</i>"]
  S --> N08_3_1
  N08_3_1 --> E(((end)))
```

## 08.4 Executive Value Operating Rhythm (L2)

```mermaid
flowchart LR
  S((start))
  N08_4_1["08.4.1 Run the CIO monthly operations review<br/><i>CIO · Any</i>"]
  S --> N08_4_1
  N08_4_1 --> E(((end)))
```
