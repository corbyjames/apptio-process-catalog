# 06 Cost Transparency & TBM Operations — L1/L2 diagrams

Generated from `data/catalog.json`. BPMN versions: see `../bpmn/generated/`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N06_1[["06.1 Run the monthly allocation & close"]]
  S --> N06_1
  N06_2[["06.2 Analyze cost, variance & investment mix"]]
  N06_1 --> N06_2
  N06_3[["06.3 Compute application & service TCO"]]
  N06_2 --> N06_3
  N06_4[["06.4 Cost labor & capitalize"]]
  N06_3 --> N06_4
  N06_5[["06.5 Manage vendor & asset cost"]]
  N06_4 --> N06_5
  N06_6[["06.6 Benchmark against peers"]]
  N06_5 --> N06_6
  N06_6 --> E(((end)))
```

## 06.1 Run the monthly allocation & close (L2)

```mermaid
flowchart LR
  S((start))
  N06_1_1["06.1.1 Load month-end actuals<br/><i>Costing Admin · Any</i>"]
  S --> N06_1_1
  N06_1_2["06.1.2 Refresh mappings & run allocations<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_1_1 --> N06_1_2
  N06_1_3["06.1.3 Validate & reconcile to GL<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_1_2 --> N06_1_3
  N06_1_4["06.1.4 Publish monthly TBM reporting<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_1_3 --> N06_1_4
  N06_1_4 --> E(((end)))
```

## 06.2 Analyze cost, variance & investment mix (L2)

```mermaid
flowchart LR
  S((start))
  N06_2_1["06.2.1 Analyze spend by cost pool & tower<br/><i>TBM Office/IT Finance · Any</i>"]
  S --> N06_2_1
  N06_2_2["06.2.2 Track budget vs actuals in the model<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_2_1 --> N06_2_2
  N06_2_3["06.2.3 Classify & report run/grow/transform<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_2_2 --> N06_2_3
  N06_2_3 --> E(((end)))
```

## 06.3 Compute application & service TCO (L2)

```mermaid
flowchart LR
  S((start))
  N06_3_1["06.3.1 Maintain application & service inventory<br/><i>App/Service Owners · Any</i>"]
  S --> N06_3_1
  N06_3_2["06.3.2 Allocate costs to applications & services<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_3_1 --> N06_3_2
  N06_3_3["06.3.3 Report & act on App TCO<br/><i>App/Service Owners · Any</i>"]
  N06_3_2 --> N06_3_3
  N06_3_4["06.3.4 Compute service unit costs<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_3_3 --> N06_3_4
  N06_3_4 --> E(((end)))
```

## 06.4 Cost labor & capitalize (L2)

```mermaid
flowchart LR
  S((start))
  N06_4_1["06.4.1 Maintain protected rates & compute blended rates<br/><i>TBM Office/IT Finance · Any</i>"]
  S --> N06_4_1
  N06_4_2["06.4.2 Publish blended rates to Targetprocess<br/><i>Costing Admin · Any</i>"]
  N06_4_1 --> N06_4_2
  N06_4_3["06.4.3 Ingest workforce & completed work data<br/><i>Costing Admin · Any</i>"]
  N06_4_2 --> N06_4_3
  N06_4_4["06.4.4 Compute monthly team cost & blended CapEx %<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_4_3 --> N06_4_4
  N06_4_5["06.4.5 Allocate team costs to work or towers<br/><i>TBM Office/IT Finance · Hybrid</i>"]
  N06_4_4 --> N06_4_5
  N06_4_6["06.4.6 Generate audit-ready capitalization actuals<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_4_5 --> N06_4_6
  N06_4_6 --> E(((end)))
```

## 06.5 Manage vendor & asset cost (L2)

```mermaid
flowchart LR
  S((start))
  N06_5_1["06.5.1 Consolidate & analyze vendor spend<br/><i>TBM Office/IT Finance · Any</i>"]
  S --> N06_5_1
  N06_5_2["06.5.2 Track assets & depreciation<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_5_1 --> N06_5_2
  N06_5_2 --> E(((end)))
```

## 06.6 Benchmark against peers (L2)

```mermaid
flowchart LR
  S((start))
  N06_6_1["06.6.1 Prepare taxonomy-aligned benchmark data<br/><i>TBM Office/IT Finance · Any</i>"]
  S --> N06_6_1
  N06_6_2["06.6.2 Compare vs peers & set targets<br/><i>TBM Office/IT Finance · Any</i>"]
  N06_6_1 --> N06_6_2
  N06_6_2 --> E(((end)))
```
