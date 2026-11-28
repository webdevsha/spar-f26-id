# spar-f26-id

**Technical spine of the SPAR Fall 2026 *Indonesia* lane** — the data and deployment
infrastructure behind the lane's AI-and-labour-market work.

This repository is not a document. It is the *machine* that turns the team's spreadsheet edits into a
versioned, auditable, and (where consented) public evidence base. The analysis and narrative live in
the shared deck and the Google Sheets tracker; this repo keeps that work **reproducible, diffable,
and shippable** without anyone hand-coding a webpage or re-exporting a CSV.

**Last full sync of this file: 28 November 2026.** If a file below is missing from this README, the
README is wrong — fix it in the same commit as the file.

**Structure (28 Nov 2026):** this page is the index. The long tables — deliverables, the file index,
the sheets, task progress, open items and the work log — were moved verbatim into
[`docs/readme/`](docs/readme/) and are linked from the Contents below. Nothing was deleted, so an
old bookmark still lands on the same words one click deeper.

---

---

## Contents

**The essentials stay on this page. The nitty-gritty is linked, not deleted.**

| Section | What is in it |
|---|---|
| [Start here — five files, in this order](#start-here-five-files-in-this-order) | The shortest path into the work |
| [What this repo is for](#what-this-repo-is-for) | Why this machine exists |
| [Layout](#layout) | Top-level directories at a glance |
| [Deliverables — as tracked](docs/readme/deliverables.md) | M1–M6, the team's deliverable table, and Shafira's own list |
| [File index](docs/readme/file-index.md) | Every path actually edited, and why |
| [The pipeline](docs/readme/pipeline.md) | Spreadsheet edit → committed, deployed artefact |
| [The sheets, and sync visibility](docs/readme/sheets-and-sync.md) | Direct links to every tab; who changed what |
| [Running it](docs/readme/operations.md) | Build, deploy, live URLs, secrets |
| [Task progress](docs/readme/task-progress.md) | The full `Shafira's tasks` mirror with due dates |
| [Open items and blockers](docs/readme/open-items.md) | What is open, stated plainly; BoxCompute collection |
| [Work log](docs/readme/work-log.md) | Everything built, 24–28 November 2026 |
| [Non-negotiables](#non-negotiables) | The four rules that do not bend |

### The site, in one place

`app/` is the public face and deploys to the site root:

| URL | What it is | Access |
|---|---|---|
| https://spar-f26-id.pages.dev/ | Bank AI-shock scenarios (`app/index.html`) — the home page | password |
| https://spar-f26-id.pages.dev/atlas.html | Ecosystem, policy and readiness atlas (`app/atlas.html`) | password |
| https://spar-f26-id.pages.dev/dashboard.html | The generated policy-readiness dashboard (`build/build_dashboard.py`) | password |
| https://spar-f26-id.pages.dev/build/* | Standalone reports | **public** |

---

## Start here (five files, in this order)

| # | File | Why |
|---|---|---|
| 1 | [docs/ID-PENDING-24NOV.md](docs/ID-PENDING-24NOV.md) | What is open, what is closed, and what "done" means for each item |
| 2 | [docs/ID-SIGNAL-SOURCE-MATRIX.md](docs/ID-SIGNAL-SOURCE-MATRIX.md) | The sourced evidence base: 22 Indonesia signals, each with a public source, a verbatim figure, a confidence tag and its stated gap |
| 3 | [data/id-postings/README.md](data/id-postings/README.md) | The hiring-signal dataset: schema, provenance, what refused us, and its limits |
| 4 | [docs/ID-HANDOFF-HANNACHAN.md](docs/ID-HANDOFF-HANNACHAN.md) | Continuity: where the truth lives, the boundaries, the blockers |
| 5 | [build/spar-id-overview.html](build/spar-id-overview.html) | The lane's findings page: overview, highlights, policy scenarios |

---

---

## What this repo is for

The Indonesia lane produces three named end results. This repository serves **all three from a single
source of truth**:

| Workstream | The output it produces | How this repo serves it |
|---|---|---|
| **Research work** | **Country reports** — what is at stake, moves to start now, triggers for when signals move. Backed by the versioned signal register, policy inventory and readiness scoring | GSheets → tracked CSV → a build that renders the evidence base as a filterable dashboard; every edit is a git commit, so the research record is versioned and auditable |
| **Policy advocacy** | **Notes for officials** — the two-page brief an official can read. Point a regulator at a gated URL instead of emailing a slide | The dashboard *is* the advocacy artefact: OJK, Kemnaker, BPJS, PERBANAS can be walked through the same data the brief is drawn from, and every figure traces to source |
| **Public engagement** *(the lane's **Ecosystem & policy map**, published as an annex on AISA's SEA **Observatory**)* | A public, living view of Indonesia's AI-in-labour ecosystem | Cloudflare Pages ships the public reports while the dashboard stays access-gated; the consent gate is a one-line switch, not a rebuild |

The three outputs are **three views of one versioned dataset** — which is why a single repo beats
three spreadsheets and a deck: the country report, the official brief and the public Observatory
cannot drift apart, because they are compiled from the same source.

---

---

## Layout

```text
data/       synced CSVs (tracked, diffable) + sheets.json tab map
  id-postings/  the 2,618-row hiring-signal dataset, its README, verification and summary
  kemnaker/     the portal's own published totals (the weights)
  seed/         original seed rows (superseded)
build/      every build script, every rendered page, and the table sources
docs/       the evidence base: matrices, drafts, prompts, guides, handoffs, sheet-write audit
dist/       generated output — never hand-edit
functions/  _middleware.js — access gate: dashboard gated, /build/* public
tools/      standalone scraper
.github/    sync.yml (hourly) + deploy.yml (build + Pages deploy)
```

---

## Non-negotiables

- **Consent gate.** Anything shown *publicly* needs AISA's consent first. Default private; the
  dashboard stays behind the access gate, and public reports are published only after sign-off.
- **No personal data.** See [data/PERSONAL-DATA-STOP.md](data/PERSONAL-DATA-STOP.md). Aggregates and totals/shares only — never
  raw individual ads — in anything shared beyond the team.
- **Framing.** This grades *documents*, never a government. No ranking, no scoring of institutions.
  Statements are "consistent with AI-driven change", never "caused by AI".
- **Never fabricate.** Unverified figures stay marked `[unverified — confirm]` or "not verified".
- **Light theme only** in any deliverable UI.
- **Not a CMS.** No write-back to Drive or Sheets.

---
