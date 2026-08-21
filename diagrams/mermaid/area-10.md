# 10 Platform Configuration, Data & Administration — L1/L2 Diagrams

Generated — edit `data/catalog.yaml`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N10_1[["10.1 Targetprocess Configuration"]]
  S --> N10_1
  N10_2[["10.2 Costing Configuration"]]
  N10_1 --> N10_2
  N10_3[["10.3 Planning Configuration"]]
  N10_2 --> N10_3
  N10_4[["10.4 Cloudability Configuration"]]
  N10_3 --> N10_4
  N10_5[["10.5 Cross-Product Data & Integration Operations"]]
  N10_4 --> N10_5
  N10_6[["10.6 Practice Operations & Maturity"]]
  N10_5 --> N10_6
  N10_6 --> E(((end)))
```

## 10.1 Targetprocess Configuration (L2)

```mermaid
flowchart LR
  S((start))
  N10_1_1["10.1.1 Design org, portfolio & team structure<br/><i>ATP Admin · Any</i>"]
  S --> N10_1_1
  N10_1_2["10.1.2 Configure processes, workflows & fields<br/><i>ATP Admin · Any</i>"]
  N10_1_1 --> N10_1_2
  N10_1_3["10.1.3 Install & tailor Solution Library packages<br/><i>ATP Admin · Any</i>"]
  N10_1_2 --> N10_1_3
  N10_1_4["10.1.4 Build views, dashboards & automation<br/><i>ATP Admin · Any</i>"]
  N10_1_3 --> N10_1_4
  N10_1_5["10.1.5 Manage integrations & environments<br/><i>ATP Admin · Any</i>"]
  N10_1_4 --> N10_1_5
  N10_1_5 --> E(((end)))
```

## 10.2 Costing Configuration (L2)

```mermaid
flowchart LR
  S((start))
  N10_2_1["10.2.1 Implement the cost model<br/><i>Costing Admin · Any</i>"]
  S --> N10_2_1
  N10_2_2["10.2.2 Operate data pipelines (Datalink)<br/><i>Costing Admin · Any</i>"]
  N10_2_1 --> N10_2_2
  N10_2_2 --> E(((end)))
```

## 10.3 Planning Configuration (L2)

```mermaid
flowchart LR
  S((start))
  N10_3_1["10.3.1 Configure planning structures<br/><i>Planning Admin · Any</i>"]
  S --> N10_3_1
  N10_3_2["10.3.2 Configure workflow & integrations<br/><i>Planning Admin · Any</i>"]
  N10_3_1 --> N10_3_2
  N10_3_2 --> E(((end)))
```

## 10.4 Cloudability Configuration (L2)

```mermaid
flowchart LR
  S((start))
  N10_4_1["10.4.1 Configure FinOps tooling<br/><i>FinOps Admin · Any</i>"]
  S --> N10_4_1
  N10_4_1 --> E(((end)))
```

## 10.5 Cross-Product Data & Integration Operations (L2)

```mermaid
flowchart LR
  S((start))
  N10_5_1["10.5.1 Operate the ADM data highway<br/><i>Integration team · Any</i>"]
  S --> N10_5_1
  N10_5_2["10.5.2 Govern master data & taxonomy<br/><i>TBM Office · Any</i>"]
  N10_5_1 --> N10_5_2
  N10_5_2 --> E(((end)))
```

## 10.6 Practice Operations & Maturity (L2)

```mermaid
flowchart LR
  S((start))
  N10_6_1["10.6.1 Run the TBM office<br/><i>TBM Office · Any</i>"]
  S --> N10_6_1
  N10_6_2["10.6.2 Run the FinOps practice<br/><i>FinOps team · Any</i>"]
  N10_6_1 --> N10_6_2
  N10_6_3["10.6.3 Run SPM governance & transformation<br/><i>SPM governance · Any</i>"]
  N10_6_2 --> N10_6_3
  N10_6_4["10.6.4 Assess maturity & set roadmap<br/><i>TBM Office · Any</i>"]
  N10_6_3 --> N10_6_4
  N10_6_4 --> E(((end)))
```
