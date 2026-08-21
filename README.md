# IBM Apptio Process Catalog

A collaborative, data-driven catalog of the business processes supported and enabled by
**IBM Apptio Targetprocess, Costing, Planning, and Cloudability**, framed by **TBM**, **SPM**
(including hybrid planning, not just agile), and **FinOps** — structured to produce L0–L2
BPML/BPMN diagrams and tool-configuration backlogs.

## What's here

| Path | What it is | Edit it? |
|---|---|---|
| `data/` | **Single source of truth** — L0 areas, the L1/L2 catalog, E2E flow steps, tool config checklists, frameworks | ✅ **Yes — edit here** |
| `docs/` | Generated Markdown documentation (overview, full catalog, config reference) | ❌ Generated |
| `diagrams/mermaid/` | Generated Mermaid diagrams (GitHub renders these inline) | ❌ Generated |
| `diagrams/bpmn/generated/` | Generated BPMN 2.0 XML, one per L1 process | ❌ Generated |
| `diagrams/bpmn/custom/` | **Hand-refined BPMN models** (incl. the reviewed cross-tool E2E model) | ✅ Yes — CI never touches |
| `diagrams/drawio/` | draw.io sources (open at [diagrams.net](https://app.diagrams.net) or the VS Code extension) | ✅ Yes — CI never touches |
| `site/` | Interactive dashboard (`index.html`) + BPMN viewer/editor (`viewer.html`), published via GitHub Pages | ❌ Generated (templates in `site/templates/`) |
| `dist/` | Generated Excel workbook of the catalog | ❌ Generated |
| `assets/diagrams/` | SVG snapshots (optional, via `scripts/export_svgs.py`) | ❌ Generated |
| `scripts/` | The generator (`generate.py`) and helpers | ✅ Yes |

## How to update things

- **Change process content** (names, descriptions, config objects, personas, delivery model,
  add/remove L2s): edit `data/catalog.yaml` (or `data/l0.yaml`, `data/flows.yaml`,
  `data/tool-config.yaml`) in a branch and open a PR. On merge, CI regenerates the docs,
  Mermaid, BPMN, dashboard, and xlsx so everything stays consistent.
- **Refine a diagram's layout/semantics beyond what generation gives you**: open the `.bpmn`
  in the **[viewer/editor](site/viewer.html)** (on the Pages site) or at [bpmn.io](https://demo.bpmn.io) /
  Camunda Modeler, edit visually, download, and commit it to `diagrams/bpmn/custom/` via PR.
  Custom models are listed first in the viewer and are never overwritten.
- **Freeform drawing**: add or edit `.drawio` files in `diagrams/drawio/` with
  [diagrams.net](https://app.diagrams.net) (File → Open from → Device, or the GitHub integration)
  or the draw.io VS Code extension.
- **Regenerate locally**: `pip install -r scripts/requirements.txt && python scripts/generate.py`

## The dashboard

The GitHub Pages site serves the interactive dashboard (L0 map, filterable L0–L2 explorer with
hybrid/agile/traditional delivery-model filters, E2E flow visualizer, BPML diagrams with
SVG/.bpmn export, insights charts) at `/site/` and the BPMN editor at `/site/viewer.html`.

## Levels

**L0** = process area (10) · **L1** = process (53) · **L2** = sub-process/activity (143).
Each L2 carries BPMN lanes (personas), trigger/cadence, inputs/outputs, tool configuration
objects, framework mapping (TBM / FinOps / SPM / SAFe), delivery-model applicability
(Any / Agile / Hybrid / Traditional), and source evidence.

See [`docs/overview.md`](docs/overview.md) for the L0 map and the six cross-tool E2E flows
("targets down, rates back, actuals in, TCO up"), and [`CONTRIBUTING.md`](CONTRIBUTING.md)
for the workflow.
