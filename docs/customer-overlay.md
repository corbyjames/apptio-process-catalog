# Customer instances — overlay build

A customer instance is `base catalog + overlay → site, docs, merged data`, built by `scripts/build_customer.py <customer-dir>`. The overlay lives in the customer's own private repository (template: the `apc-scotiabank` layout — `customer.json`, `assessment/`, `review/`, `.github/workflows/build.yml`), never in this repository. Every durable reference in an overlay is a permanent element ID (`P-nnnn` processes, `G-nnn` groups); positional IDs (`06.4.2`) are display labels that may change between base releases.

## customer.json

| Key | Meaning |
|---|---|
| `id`, `name`, `short`, `title` | identity; `title` is the site title, `short` the breadcrumb root |
| `base` | base catalog version the overlay was written against (the build warns if different) |
| `fy_start`, `currency` | fiscal year start month (1–12) and reporting currency; used in `docs/overview.md` |
| `profile` | `{decision_key: [option ids]}` — the profile the site opens with; viewers can still change it |
| `profile_notes` | free text explaining the profile choices |
| `scope` | `{name, summary, groups:[G-ids], eids:[P-ids]}` — the engagement focus: a band on the hub, an *In scope* badge on records. A group listed without any of its processes in `eids` contributes all of them |
| `overrides` | `{eid: {field: value}}` — replaces fields on a base record (L2 by P-id, L1 by G-id); the record notes which fields are customer overrides |
| `additions` | customer-specific L2s (`eid` P-9000+, `parent` G-id, `id` in the parent's numbering) |
| `suppress` | element IDs removed from this instance (L2 or whole L1); flow steps and decision scopes are trimmed accordingly |
| `labels` | whole-word vocabulary substitutions applied to all record, group and flow text |

## Assessment rounds

`assessment/<round>.json`: `round`, `target_profile`, `levels` (defaults to the 0–5 maturity scale in `build_customer.py`), `targets` (per group, expanded to each in-scope process), `scores` (`{eid: {level, target, evidence, gap, method, confidence}}`). The latest file by name is baked into the site, which shows a scoring panel on every record, maturity chips on tiles and group headings, and an *Export assessment* button that copies and downloads the round as JSON to commit back into the repo.

## Review state

The site's review marks (status, verdict, owner, comments) stay browser-local; an exported copy committed under `review/` is kept with the instance for audit. Shared live review is deliberately out of scope for a Pages-hosted instance.
