# 01 Strategy & Goal Management — L1/L2 diagrams

Generated from `data/catalog.json`. BPMN versions: see `../bpmn/generated/`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N01_1[["01.1 Set strategic direction & alignment"]]
  S --> N01_1
  N01_2[["01.2 Manage OKRs"]]
  N01_1 --> N01_2
  N01_2 --> E(((end)))
```

## 01.1 Set strategic direction & alignment (L2)

```mermaid
flowchart LR
  S((start))
  N01_1_1["01.1.1 Define strategic themes & business objectives<br/><i>C-Suite/Strategy · Any</i>"]
  S --> N01_1_1
  N01_1_2["01.1.2 Cascade strategy to portfolios & value streams<br/><i>Portfolio Management · Any</i>"]
  N01_1_1 --> N01_1_2
  N01_1_3["01.1.3 Monitor strategy execution & re-plan dynamically<br/><i>C-Suite/Strategy · Any</i>"]
  N01_1_2 --> N01_1_3
  N01_1_3 --> E(((end)))
```

## 01.2 Manage OKRs (L2)

```mermaid
flowchart LR
  S((start))
  N01_2_1["01.2.1 Set & cascade OKRs<br/><i>C-Suite/Strategy · Any</i>"]
  S --> N01_2_1
  N01_2_2["01.2.2 Link work & investments to OKRs<br/><i>Portfolio Management · Any</i>"]
  N01_2_1 --> N01_2_2
  N01_2_3["01.2.3 Score, review & refresh OKRs<br/><i>C-Suite/Strategy · Any</i>"]
  N01_2_2 --> N01_2_3
  N01_2_3 --> E(((end)))
```
