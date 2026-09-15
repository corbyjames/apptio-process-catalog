# 10 Platform Configuration, Data & Administration — L1/L2 diagrams

Generated from `data/catalog.json`. BPMN versions: see `../bpmn/generated/`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N10_1[["10.1 Configure Targetprocess"]]
  S --> N10_1
  N10_2[["10.2 Configure Costing"]]
  N10_1 --> N10_2
  N10_3[["10.3 Configure Planning"]]
  N10_2 --> N10_3
  N10_4[["10.4 Configure Cloudability"]]
  N10_3 --> N10_4
  N10_5[["10.5 Operate cross-product data & integrations"]]
  N10_4 --> N10_5
  N10_6[["10.6 Run the practices & grow maturity"]]
  N10_5 --> N10_6
  N10_7[["10.7 Run AI-assisted planning & delivery intelligence"]]
  N10_6 --> N10_7
  N10_7 --> E(((end)))
```

## 10.1 Configure Targetprocess (L2)

```mermaid
flowchart LR
  S((start))
  N10_1_1["10.1.1 Design org, portfolio & team structure<br/><i>Platform Admins · Any</i>"]
  S --> N10_1_1
  N10_1_2["10.1.2 Configure processes, workflows & fields<br/><i>Platform Admins · Any</i>"]
  N10_1_1 --> N10_1_2
  N10_1_3["10.1.3 Install & tailor Solution Library packages<br/><i>Platform Admins · Any</i>"]
  N10_1_2 --> N10_1_3
  N10_1_4["10.1.4 Build views, dashboards & automation<br/><i>Platform Admins · Any</i>"]
  N10_1_3 --> N10_1_4
  N10_1_5["10.1.5 Manage integrations & environments<br/><i>Platform Admins · Any</i>"]
  N10_1_4 --> N10_1_5
  N10_1_5 --> E(((end)))
```

## 10.2 Configure Costing (L2)

```mermaid
flowchart LR
  S((start))
  N10_2_1["10.2.1 Implement the cost model<br/><i>Platform Admins · Any</i>"]
  S --> N10_2_1
  N10_2_2["10.2.2 Operate data pipelines (Datalink)<br/><i>Platform Admins · Any</i>"]
  N10_2_1 --> N10_2_2
  N10_2_2 --> E(((end)))
```

## 10.3 Configure Planning (L2)

```mermaid
flowchart LR
  S((start))
  N10_3_1["10.3.1 Configure planning structures<br/><i>Platform Admins · Any</i>"]
  S --> N10_3_1
  N10_3_2["10.3.2 Configure workflow & integrations<br/><i>Platform Admins · Any</i>"]
  N10_3_1 --> N10_3_2
  N10_3_2 --> E(((end)))
```

## 10.4 Configure Cloudability (L2)

```mermaid
flowchart LR
  S((start))
  N10_4_1["10.4.1 Configure cloud data, mappings & views<br/><i>Platform Admins · Any</i>"]
  S --> N10_4_1
  N10_4_2["10.4.2 Configure budgets, alerts, optimization & governance<br/><i>Platform Admins · Any</i>"]
  N10_4_1 --> N10_4_2
  N10_4_2 --> E(((end)))
```

## 10.5 Operate cross-product data & integrations (L2)

```mermaid
flowchart LR
  S((start))
  N10_5_1["10.5.1 Operate the ADM data highway<br/><i>Integration Team · Any</i>"]
  S --> N10_5_1
  N10_5_2["10.5.2 Govern master data & taxonomy<br/><i>TBM Office · Any</i>"]
  N10_5_1 --> N10_5_2
  N10_5_2 --> E(((end)))
```

## 10.6 Run the practices & grow maturity (L2)

```mermaid
flowchart LR
  S((start))
  N10_6_1["10.6.1 Run the TBM office<br/><i>TBM Office · Any</i>"]
  S --> N10_6_1
  N10_6_2["10.6.2 Run the FinOps practice<br/><i>FinOps Team · Any</i>"]
  N10_6_1 --> N10_6_2
  N10_6_3["10.6.3 Run SPM governance & transformation<br/><i>SPM Governance · Any</i>"]
  N10_6_2 --> N10_6_3
  N10_6_4["10.6.4 Assess maturity & set roadmap<br/><i>TBM Office · Any</i>"]
  N10_6_3 --> N10_6_4
  N10_6_4 --> E(((end)))
```

## 10.7 Run AI-assisted planning & delivery intelligence (L2)

```mermaid
flowchart LR
  S((start))
  N10_7_1["10.7.1 Deploy the planning copilot & delivery intelligence<br/><i>SPM Governance · Agile</i>"]
  S --> N10_7_1
  N10_7_2["10.7.2 Govern agent autonomy & trust<br/><i>SPM Governance · Any</i>"]
  N10_7_1 --> N10_7_2
  N10_7_3["10.7.3 Ground agents in enterprise context & ecosystem<br/><i>Platform Admins · Any</i>"]
  N10_7_2 --> N10_7_3
  N10_7_3 --> E(((end)))
```
