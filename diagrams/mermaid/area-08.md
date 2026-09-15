# 08 Consumption, Chargeback & Value Management — L1/L2 diagrams

Generated from `data/catalog.json`. BPMN versions: see `../bpmn/generated/`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N08_1[["08.1 Show back & bill for IT"]]
  S --> N08_1
  N08_2[["08.2 Engage the business & steer value"]]
  N08_1 --> N08_2
  N08_2 --> E(((end)))
```

## 08.1 Show back & bill for IT (L2)

```mermaid
flowchart LR
  S((start))
  N08_1_1["08.1.1 Allocate consumption to business units<br/><i>TBM Office · Any</i>"]
  S --> N08_1_1
  N08_1_2["08.1.2 Publish showback / Bill of IT<br/><i>TBM Office · Any</i>"]
  N08_1_1 --> N08_1_2
  N08_1_3["08.1.3 Price services & run chargeback<br/><i>TBM Office · Any</i>"]
  N08_1_2 --> N08_1_3
  N08_1_3 --> E(((end)))
```

## 08.2 Engage the business & steer value (L2)

```mermaid
flowchart LR
  S((start))
  N08_2_1["08.2.1 Review costs with BU owners<br/><i>TBM Office · Any</i>"]
  S --> N08_2_1
  N08_2_2["08.2.2 Extend costing beyond IT<br/><i>TBM Office · Any</i>"]
  N08_2_1 --> N08_2_2
  N08_2_3["08.2.3 Run the CIO monthly operations review<br/><i>CIO/CFO · Any</i>"]
  N08_2_2 --> N08_2_3
  N08_2_3 --> E(((end)))
```
