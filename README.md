# IBM Apptio Process Catalog

A data-driven catalog of the business processes supported and enabled by **IBM Apptio
Targetprocess, Costing, Planning and Cloudability**, framed by **TBM**, **SPM** (hybrid planning,
not just agile) and **FinOps** — with a **BPMN 2.0 swimlane diagram for every process area,
every process group and every cross-tool flow**, and a configuration backlog per product.

**Live site:** https://corbyjames.github.io/apptio-process-catalog/ (GitHub Pages, deployed on every push to `main`).

Current structure (v0.6.0): **9 L0 areas · 45 L1 groups · 149 L2 processes · 7 cross-tool flows · 61 BPMN diagrams.**

## What's here

| Path | What it is | Edit it? |
|---|---|---|
| `data/catalog.json` | **Single source of truth** — areas, groups, processes (with permanent element IDs), flows with BPMN-ready step tables, glossary, changelog | ✅ **Yes — edit here** |
| `data/calendar.yaml`, `data/tool-config.yaml`, `data/frameworks.yaml`, `data/l0-links.yaml` | Operating calendar, per-product config checklists, framework framing, L0 landscape feeds | ✅ Yes |
| `site/` | The catalog site: hub / area pages / register / flow pages / diagrams index / glossary / changelog / print view, plus `viewer.html` (bpmn-js editor) | ❌ Generated from `site/templates/app.html` |
| `diagrams/bpmn/generated/` | BPMN 2.0 XML with diagram interchange: `L0-NN.bpmn` (areas), `NN.N.bpmn` (groups), `flow-XXX.bpmn` (flows) | ❌ Generated |
| `assets/diagrams/` | SVG snapshot of each diagram (theme-aware, embeddable) | ❌ Generated |
| `diagrams/bpmn/custom/` | **Hand-refined BPMN models** (incl. the reviewed cross-tool E2E model) — CI never touches | ✅ Yes |
| `diagrams/drawio/` | draw.io sources | ✅ Yes |
| `diagrams/mermaid/` | Mermaid diagrams (GitHub renders inline) | ❌ Generated |
| `docs/` | Markdown: overview, full catalog, diagram index, tool-config reference, operating calendar; `docs/sources/` holds source material | ❌ Generated (except `sources/`) |
| `dist/Apptio_Process_Catalog_L0-L2.xlsx` | Excel master (all sheets regenerated) | ❌ Generated |
| `scripts/` | `generate.py` (the build), `bpmn.py` (layout, SVG, XML), `xlsx_build.py`, `merge_v05.py` (provenance of the v0.6 merge) | ✅ Yes |

## How the diagrams are built

Everything is derived from `data/catalog.json` by `scripts/bpmn.py`; the same layout engine runs in
Python (for the `.bpmn` and `.svg` files) and in the site's JavaScript (for the live, theme-aware,
clickable version), so they agree.

- **Cross-tool flows** (`flow-UC3.bpmn` …): straight from the step tables — lane = system or role,
  element type = the BPMN type named on the step, gateway branches parsed from the note
  (`No: end event '…'`, `loop to z4`, suffix steps `17a`/`17b`).
- **Process groups** (`05.8.bpmn` …): one task per L2 in catalog order; lane = the first persona in
  the L2's *Who* text that matches one of the area's default lanes; task type inferred from persona
  (`System`/`automated` → service task) and verb (send/publish → send task, approve/submit/enter →
  user task).
- **Process areas** (`L0-05.bpmn` …): one collapsed sub-process per group, in the lane where most of
  its processes sit.

Each diagram on the site has *Download .bpmn / .svg*, *open in editor* and *Copy BPMN XML*. The XML
imports into Camunda Modeler, bpmn.io, Signavio, Visio and Draw.io.

## How to update things

- **Change process content** (names, descriptions, config objects, personas, delivery model, add or
  remove L2s): edit `data/catalog.json` in a branch and open a PR. Keep positional IDs stable and
  give new L2s the next free element ID (`P-0150`, …). On merge, CI regenerates the site, docs,
  Mermaid, BPMN, SVGs and xlsx and deploys Pages.
- **Change a lane or task type on a group diagram**: adjust the L2's `personas` text (the first
  persona decides the lane) or the keyword tables at the top of `scripts/bpmn.py`.
- **Refine a diagram beyond what generation gives**: open it in the site's
  [viewer/editor](site/viewer.html), edit, download, and commit it to `diagrams/bpmn/custom/`.
  Custom models are listed first in the viewer and are never overwritten.
- **Regenerate locally**: `pip install -r scripts/requirements.txt && python scripts/generate.py`

## Review layer

Statuses per process, verdicts per group and comments anchored to element IDs are kept in the
browser (`localStorage`) on the Pages site. The claude.ai review prototype shares them across
reviewers; this repository build does not.

## Levels

**L0** = process area · **L1** = process group · **L2** = process/activity (the unit that becomes a
BPMN task). Each L2 carries a permanent element ID, BPMN lane and task type, delivery model
(Any / Agile / Traditional / Hybrid), budgeting method where relevant, personas, cadence,
inputs/outputs, configuration objects, framework mapping (TBM / FinOps / SPM / SAFe / ITFM), the
cross-tool flows it belongs to, and source evidence.

See [`docs/overview.md`](docs/overview.md) for the L0 map and the seven cross-tool flows
("targets down, rates back, actuals in, TCO up" + cloud-to-TBM, the investment loop and the ZBB
re-base), [`docs/diagrams.md`](docs/diagrams.md) for the diagram index, and
[`CONTRIBUTING.md`](CONTRIBUTING.md) for the workflow.
