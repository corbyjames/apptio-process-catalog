# 04 Workforce & Resource Management — L1/L2 Diagrams

Generated — edit `data/catalog.yaml`.

## L1 process chain

```mermaid
flowchart LR
  S((start))
  N04_1[["04.1 Workforce Baseline & Team Structure"]]
  S --> N04_1
  N04_2[["04.2 Capacity Planning"]]
  N04_1 --> N04_2
  N04_3[["04.3 Resource Allocation & Utilization"]]
  N04_2 --> N04_3
  N04_4[["04.4 Position Management"]]
  N04_3 --> N04_4
  N04_5[["04.5 Time Tracking & Approval"]]
  N04_4 --> N04_5
  N04_5 --> E(((end)))
```

## 04.1 Workforce Baseline & Team Structure (L2)

```mermaid
flowchart LR
  S((start))
  N04_1_1["04.1.1 Load & maintain people roster<br/><i>Resource Mgmt · Any</i>"]
  S --> N04_1_1
  N04_1_2["04.1.2 Create & assign teams, ARTs & trains<br/><i>Resource Mgmt · Any</i>"]
  N04_1_1 --> N04_1_2
  N04_1_3["04.1.3 Maintain job profiles & financial mappings<br/><i>Finance · Any</i>"]
  N04_1_2 --> N04_1_3
  N04_1_3 --> E(((end)))
```

## 04.2 Capacity Planning (L2)

```mermaid
flowchart LR
  S((start))
  N04_2_1["04.2.1 Map & forecast capacity<br/><i>Resource Mgmt · Any</i>"]
  S --> N04_2_1
  N04_2_2["04.2.2 Balance demand vs capacity<br/><i>Portfolio Mgmt · Any</i>"]
  N04_2_1 --> N04_2_2
  N04_2_3["04.2.3 Run workforce scenarios<br/><i>Resource Mgmt · Any</i>"]
  N04_2_2 --> N04_2_3
  N04_2_3 --> E(((end)))
```

## 04.3 Resource Allocation & Utilization (L2)

```mermaid
flowchart LR
  S((start))
  N04_3_1["04.3.1 Allocate people & teams to work<br/><i>Portfolio Mgmt · Any</i>"]
  S --> N04_3_1
  N04_3_2["04.3.2 Track utilization & productivity<br/><i>Resource Mgmt · Any</i>"]
  N04_3_1 --> N04_3_2
  N04_3_3["04.3.3 Match skills & close gaps<br/><i>Resource Mgmt · Any</i>"]
  N04_3_2 --> N04_3_3
  N04_3_4["04.3.4 Assign individuals & roles to project work (hybrid resourcing)<br/><i>Resource Mgmt · Hybrid</i>"]
  N04_3_3 --> N04_3_4
  N04_3_4 --> E(((end)))
```

## 04.4 Position Management (L2)

```mermaid
flowchart LR
  S((start))
  N04_4_1["04.4.1 Create position requests<br/><i>Portfolio/Hiring managers · Any</i>"]
  S --> N04_4_1
  N04_4_2["04.4.2 Approve positions (multi-level workflow)<br/><i>HR · Any</i>"]
  N04_4_1 --> N04_4_2
  N04_4_3["04.4.3 Sync approved positions to Planning & auto-update on fill<br/><i>System (ADM) · Any</i>"]
  N04_4_2 --> N04_4_3
  N04_4_3 --> E(((end)))
```

## 04.5 Time Tracking & Approval (L2)

```mermaid
flowchart LR
  S((start))
  N04_5_1["04.5.1 Record time against work<br/><i>Team members · Any</i>"]
  S --> N04_5_1
  N04_5_2["04.5.2 Approve timesheets<br/><i>Managers · Any</i>"]
  N04_5_1 --> N04_5_2
  N04_5_3["04.5.3 Feed time/effort to finance processes<br/><i>Finance · Any</i>"]
  N04_5_2 --> N04_5_3
  N04_5_3 --> E(((end)))
```
