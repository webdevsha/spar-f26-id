# spar-f26-id

**Technical spine of the SPAR Fall 2026 *Indonesia* lane** — the data and deployment
infrastructure behind the lane's AI-and-labour-market work.

This repository is not a document. It is the *machine* that turns the team's spreadsheet edits into a
versioned, auditable, and (where consented) public evidence base. The analysis and narrative live in
the shared deck and the Google Sheets tracker; this repo keeps that work **reproducible, diffable,
and shippable** without anyone hand-coding a webpage or re-exporting a CSV.

**Last full sync of this file: 26 November 2026.** If a file below is missing from this README, the
README is wrong — fix it in the same commit as the file.

---

## Contents

- [The deliverables (as tracked)](#the-deliverables-as-tracked)
- [Start here (five files, in this order)](#start-here-five-files-in-this-order)
- [What this repo is for](#what-this-repo-is-for)
- [File index — everything we actually work on](#file-index--everything-we-actually-work-on)
- [Layout](#layout)
- [The pipeline](#the-pipeline)
- [The sheets](#the-sheets)
- [Sync visibility — who changed what](#sync-visibility--who-changed-what)
- [Running it](#running-it)
- [Live URLs (tested 24 Nov 2026)](#live-urls-tested-24-nov-2026)
- [Secrets (never in this repo)](#secrets-never-in-this-repo)
- [Shafira's task progress (SPAR Fall 2026)](#shafiras-task-progress-spar-fall-2026)
- [Open items and blockers](#open-items-and-blockers)
- [BoxCompute collection (24 Nov 2026)](#boxcompute-collection-24-nov-2026)
- [Non-negotiables](#non-negotiables)

---

## The deliverables (as tracked)

What the lane hands in, mirroring the team tracker so the repo and the spreadsheet never disagree. Live tracker: **[IND team progress](https://docs.google.com/spreadsheets/d/1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ/edit)** — tab `Sheet1` is the team view, the `Shafira's tasks` tab is her own work with due dates.

> **What has actually been built, and when:** [the work log](#work-log--everything-built-2428-november-2026)
> at the end of this file — one row per artefact, with the PR or the audit note that carries it.

### A. Measures and signals — reviewed

| Work | What it covers | Progress | Owner | Evidence |
|---|---|---|---|---|
| **M1** Workforce exposure | Finance and insurance clerical employment, formality and wages compared between the February 2024 and 2026 surveys | 100% · Reviewed | Akbar | [Microdata Findings.pptx](https://docs.google.com/presentation/d/1U_DRtEJL68KPnKRWEmoQlf_P_SJ0tlLcd/edit) |
| **M2** Bank AI deployment | AI use reviewed at five banks; the evidence identifies tasks and usage | 100% · Reviewed | Akbar | [Bank AI deployment and worker support in Indonesia](https://docs.google.com/document/d/1-UkVM7HjWyYFfgmjwPodZ0Y2HKVegzm_Te0UaLdkiNU/edit) |
| **M3** Recruitment and skills | Job-posting ads reviewed for changes in roles and skill requirements | 100% · Reviewed | Akbar | [Job-ads report](https://spar-f26-id.pages.dev/build/spar-id-postings) |
| **M4** Worker adjustment | Employment outcomes for recent finance clerical job leavers; national JKP claims reviewed separately | 100% · Reviewed | Akbar | [Bank AI deployment and worker support in Indonesia](https://docs.google.com/document/d/1-UkVM7HjWyYFfgmjwPodZ0Y2HKVegzm_Te0UaLdkiNU/edit) |
| **M5** Worker support capacity | JKP eligibility, training routes and access barriers | 100% · Reviewed | Akbar | [Bank AI deployment and worker support in Indonesia](https://docs.google.com/document/d/1-UkVM7HjWyYFfgmjwPodZ0Y2HKVegzm_Te0UaLdkiNU/edit) |
| **M6** Fiscal and consumption signals | Gross labour income tax receipts across banks, finance and all sectors | 100% · Reviewed | Akbar | [Microdata Findings.pptx](https://docs.google.com/presentation/d/1U_DRtEJL68KPnKRWEmoQlf_P_SJ0tlLcd/edit) |

### B. Team deliverables

| Work | What it covers | Progress | Status | Owner | Where |
|---|---|---|---|---|---|
| **Final report** | Midterm draft continued; six findings, scenarios and policy responses integrated | 50% | In progress | Akbar, Natraj, Shafira | [Midterm Report](https://docs.google.com/document/d/1WXY8YiPSC7rmgUNhc0jxFc4YbWYDNnxLGVLz_2qRa9Y/edit) |
| **Scenario model** | Clerical exposure under three scenarios and two baselines | 50% | In progress | Akbar, Natraj | [SPAR model](https://docs.google.com/spreadsheets/d/1JpJG9wxsRIKf7dGl6RrMyvsaxcaBPO5CCsbde_7vkU0/edit) |
| **Ecosystem and policy map** | Actors, instruments and worker support routes | 75% | Ready for review | Shafira, Rachel | [Live map](https://spar-f26-id.pages.dev/build/spar-id-ecosystem-map) |
| **Data inventory** | Indonesian sources and data holders; coverage gaps reconciled with the shared inventory | 50% | In progress | Napat, Akbar, Shafira | [Core file](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit) |
| **Decision calendar** | Six Indonesian decision windows, with dates and owners | 50% | In progress | Shafira, Rachel | [Decision calendar](https://github.com/webdevsha/spar-f26-id/blob/main/docs/ID-DECISION-CALENDAR.md) |
| **Policy readiness review** | Policy documents scored against six readiness questions | 50% | In progress | Shafira | [Readiness tab](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=597313565) |
| **Signal watchlist** | Signals shortlisted with a shared log of observations | 50% | In progress | Shafira, Ian | [Signals tab](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=838965401) |
| **Indonesia trigger cards** | Draft cards linking signals to possible responses | 50% | In progress | Akbar | [Triggers tab](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=778752423) |
| **Job-postings dashboard** | Archived ads compared for AI mentions, occupational exposure and entry level | 80% | In progress | Shafira | [Job-ads report](https://spar-f26-id.pages.dev/build/spar-id-postings) |
| **Bank interviews** | Interviewee candidates identified; access awaited | 25% | Scoping | Akbar | [Interviewee sheet](https://docs.google.com/document/d/1ZNwb0TbpdryC1jyS0qPzPOPQuQ4RiFuv8Dp9sbAXVhg/edit) |
| **Final presentation** | Three-slide Indonesia research map and narration | 100% | Complete | Akbar | — |
| **Indonesia op-ed** | Full and short versions written, awaiting review | 75% | Ready for review | Akbar | [Indonesia Op-Ed](https://docs.google.com/document/d/1eXJW4GZe-R_eVI9u7nmh4m9DZk68Qs8yDY1EfADxQ4U/edit) |

### C. Shafira's own work (with due dates)

Mirrors the `Shafira's tasks` tab — her work only, so the shared sheet stays untouched.

| Work | Progress | Status | Due |
|---|---|---|---|
| Data list (with Napat) | 90% | Ready to check | 14 Nov 2026 — overdue |
| Checking the sources | 100% | Done | 24 Nov 2026 — done |
| Reading the job portal | 100% | Done | 22 Nov 2026 — overdue |
| Job-ads dashboard | 80% | In progress | Ongoing |
| Indonesian data, full history | 40% | In progress | 29 Nov 2026 |
| Licence note for the paid data (with Akbar) | 20% | In progress | 14 Nov 2026 — overdue |
| Country report — Part 3 | 70% | Draft ready to read | 22 Nov 2026 — overdue |
| Country report — Part 4 (with Ian) | 70% | Draft ready to read | 22 Nov 2026 — overdue |
| Country report — Part 5 (with Natraj) | 25% | In progress | 29 Nov 2026 |
| Report section 5 — Indonesia chapter | 15% | In progress | 2 Dec 2026 |
| Report section 8 — limits (with Napat) | 60% | Draft ready to read | 2 Dec 2026 |
| Policy readiness review | 50% | In progress | 26 Oct 2026 — overdue |
| Signal watchlist (with Ian) | 90% | Ready to check | Ongoing |
| Indonesia indicator table — S1–S10 (`SIGNALS_ID`, with Ian) | 90% | Ready to check | Ongoing |
| Decision calendar (with Rachel) | 80% | Ready to check | 22 Nov 2026 — overdue |
| Ecosystem and policy map (with Rachel) | 75% | Ready to check | 22 Nov 2026 — overdue |
| Atlas page (our public page) | 45% | In progress | Jan 2027 |
| Overview and scenarios page | 85% | Built, not yet online | 24 Nov 2026 — done |
| More job ads (target 10,000) | 15% | Scoping | After 29 Nov 2026 |
| One interview about data gaps | 20% | Scoping | 27 Nov 2026 |
| Freeze the shared sheet | 25% | Blocked | 29 Nov 2026 |

*The tracker is the source. This section is a mirror — update it when the tracker moves.*

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

## File index — everything we actually work on

**Status key:** `live` = published and reachable · `repo` = tracked here · `local` = built but not
deployed · `blocked` = waiting on infrastructure · `superseded` = kept for provenance only.

### A. Analysis, evidence and writing (`docs/`)

| File | What it is | Owner | Status |
|---|---|---|---|
| [ID-PENDING-24NOV.md](docs/ID-PENDING-24NOV.md) | The open/closed task ledger, with what "done" looks like per item | Shafira (ID lane) | repo |
| [ID-SIGNAL-SOURCE-MATRIX.md](docs/ID-SIGNAL-SOURCE-MATRIX.md) | Source matrix v2 — the 22-row verified source line, 5 status corrections, 2 attribution traps, 3 denominator traps | Shafira + CRO | repo |
| [ID-PART3-DRAFT.md](docs/ID-PART3-DRAFT.md) | Country Report Part 3 draft, 678 words, every figure traced; unverified figures left bracketed | Shafira | repo |
| [ID-PART4-DRAFT.md](docs/ID-PART4-DRAFT.md) | Country Report Part 4 v1 — who can act and the policies in place, reframed to the AI shock question: each instrument carries its verdict, three flags for Ian, word count stated honestly | Shafira + Ian | repo |
| [ID-PART8-LIMITS-DRAFT.md](docs/ID-PART8-LIMITS-DRAFT.md) | Report section 8 — limits, stated on the record | Shafira + Napat | repo |
| [ID-POLICY-SITE-PROPOSAL.md](docs/ID-POLICY-SITE-PROPOSAL.md) | **The design proposal** — ten patterns from the Windfall scenarios site that work for a policy reader, what we must not copy, the seven-route product, the two evidenceable scenario axes, the evidence grammar, the build plan and the five gates | CRO for Shafira | repo |
| [ID-CALL-RUNSHEET-26NOV.md](docs/ID-CALL-RUNSHEET-26NOV.md) | One-page run sheet for the SPAR call: six do-now items, six raise-on-call items, the numbers to have at hand, the two decisions needed | CRO for Shafira | repo |
| [ID-READINESS-WORKSHEET.md](docs/ID-READINESS-WORKSHEET.md) | 3 policy documents × 6 readiness questions, pre-loaded with the evidence each question answers from | Shafira | repo (untracked) |
| [ID-HANDOFF-HANNACHAN.md](docs/ID-HANDOFF-HANNACHAN.md) | Continuity handoff: truth map, boundaries, blockers, order of work | CRO | repo (untracked) |
| [ID-SIGNALS-PERPLEXITY-PACK.md](docs/ID-SIGNALS-PERPLEXITY-PACK.md) | The verification brief sent to Perplexity (blocks A–E, rules, output contract) | CRO | repo |
| [PROMPTS-PERPLEXITY-BOXCOMPUTE.md](docs/PROMPTS-PERPLEXITY-BOXCOMPUTE.md) | Copy-paste prompt set: Perplexity verification (P1, P2) and the first BoxCompute collection brief (B1–B3) | CRO | repo |
| [PROMPTS-BOXCOMPUTE-V2.md](docs/PROMPTS-BOXCOMPUTE-V2.md) | **Current** collection brief — archive-first, three record kinds, 34-field schema, comparability gate (supersedes B1–B3) | CRO | repo |
| [SCRAPING-WITH-BOXCOMPUTE.md](docs/SCRAPING-WITH-BOXCOMPUTE.md) | Plain-English guide to scraping with BoxCompute, using this Indonesia run as the worked example | CRO | repo |
| [SHEET-WRITE-2026-11-24.md](docs/SHEET-WRITE-2026-11-24.md) | Audit + revert instructions for every shared-sheet write, 24–26 Nov (Core file `signals` O–T, skeleton `SIGNALS` H–K, `SIGNALS_ID` E–J + highlighting, `IND team progress` G, `SIGNALS` J) | CRO | repo |
| [MODEL-INDONESIA.md](docs/MODEL-INDONESIA.md) | How the scenario model maps onto Indonesia: what the data identifies, what must be calibrated | CRO + Natraj | repo |
| [back-up-research.md](docs/back-up-research.md) | Evidence notes behind the six measures M1–M6, with sources per indicator | CRO | repo |
| [apps-script-trigger.gs](docs/apps-script-trigger.gs) | Apps Script `onChange` hook → `repository_dispatch`, so a sheet edit reaches the repo in seconds | CTO | repo |

### B. Signal register and registers data (`data/`)

| File | What it is | Owner | Status |
|---|---|---|---|
| [id-signals.csv](data/id-signals.csv) | Mirror of the register's `signals` tab — **currently stale**: repo holds 9 rows, the sheet holds 22 | sync job | repo (stale) |
| [id-policy-inventory.csv](data/id-policy-inventory.csv) | Policy inventory: 3 documents (OJK AI guide, JKP, Pasker ID) | team | repo |
| [id-readiness.csv](data/id-readiness.csv) | Readiness scoring join — all `q1`–`q6` still `tbc` | Shafira | repo (open) |
| [id-who-can-act.csv](data/id-who-can-act.csv) | The who-can-act map: 6 organisations with proposed doors | Shafira + Rachel | repo |
| [id-instruments.csv](data/id-instruments.csv) | Instrument map — **DEMO row only**, needs real rows | team | repo (open) |
| [id-triggers.csv](data/id-triggers.csv) | Trigger card(s) — one row so far | Akbar | repo |
| [sheets.json](data/sheets.json) | Tab name → output CSV map used by the sync | CTO | repo |
| [SYNC-LOG.md](data/SYNC-LOG.md) | Append-only record of every sync run: editors, `+added / −removed`, changed `id`s | sync job | repo |
| [PERSONAL-DATA-STOP.md](data/PERSONAL-DATA-STOP.md) | The no-personal-data rule and what it means row by row | CRO | repo |
| [ecosystem-id-map.json](data/ecosystem-id-map.json), [ecosystem-id-domains.json](data/ecosystem-id-domains.json) | The Indonesia ecosystem & policy map (actors, instruments, support routes) that renders as a public page. **`views.policy.nodes` is now generated** from the register by [build/sync_map_from_register.py](build/sync_map_from_register.py) (22 nodes: 8 hand-written kept, 8 added, 6 levers); bands, edges, marks and `responsibility` stay hand-curated | Shafira + Rachel | repo |
| [ecosystem-ph-v0.json](data/ecosystem-ph-v0.json) | Philippines ecosystem stub — kept in this repo for parity; PH lane owns the content | BG | repo |
| [model-id-demo.json](data/model-id-demo.json) | Inputs for the interactive model demo | CRO + Natraj | repo |
| `seed/*.tsv` | Original seed rows used to create the sheet tabs | CTO | superseded |

### C. The postings dataset (`data/id-postings/`)

| File | What it is | Owner | Status |
|---|---|---|---|
| [postings-2024.csv](data/id-postings/postings-2024.csv) (1.4 MB) · [postings-2025.csv](data/id-postings/postings-2025.csv) (1.8 MB) · [postings-2026.csv](data/id-postings/postings-2026.csv) (0.4 MB) | 2,618 archived Indonesian finance/BPO postings, 2024-02 → 2026-10, one row per posting, 37 columns | Shafira | repo |
| [README.md](README.md) | Schema, provenance, ethics, coverage limits for the dataset | Shafira + CRO | repo |
| [summary.json](data/id-postings/summary.json) | Counts used by the report builder (sectors, months, AI tiers, provinces) | build | repo |
| [verification.json](data/id-postings/verification.json) | Per-row re-fetch results (411 of 2,618 checked) | build | repo |
| [karirhub-id-postings-sample.csv](data/id-postings/karirhub-id-postings-sample.csv) | The original 331-row sample from the first successful scrape | CRO | repo |
| [perplexity-id-data.md](data/id-postings/perplexity-id-data.md) | The verification run: 22 rows, 5 priority figures, request routes, contradictions | Shafira (run) | repo |

### D. Kemnaker's own portal counts (`data/kemnaker/` and `build/`)

These are the **portal's own advertised totals** — the weights any posting sample must be calibrated
to. All four are public CSV downloads from `paskerid.kemnaker.go.id/documents/`, no gate.

| File | What it is | Status |
|---|---|---|
| [data/kemnaker/Lowongan_Kerja_Menurut_Kategori_Lapangan_Usaha_Tahun_2022-2024.csv](data/kemnaker/Lowongan_Kerja_Menurut_Kategori_Lapangan_Usaha_Tahun_2022-2024.csv) | Postings and advertised slots by industry (KBLI 1-digit), 2022–24. Finance & insurance: **1,195 → 797 → 726** | repo |
| [data/kemnaker/Lowongan_Kerja_di_Karirhub_Menurut_Golongan_Pokok_Jabatan_Tahun_2022-2024.csv](data/kemnaker/Lowongan_Kerja_di_Karirhub_Menurut_Golongan_Pokok_Jabatan_Tahun_2022-2024.csv) | The same by occupation group (KBJI). Clerical (group 4): 1,751 → 3,341 → 2,034 | repo |
| [build/sector.csv](build/sector.csv) | Byte-identical copy of the industry file — **duplicate, should move to `data/kemnaker/`** | repo (duplicate) |
| [build/occ.csv](build/occ.csv) | Duplicate of the occupation file | repo (duplicate) |
| [build/emp.csv](build/emp.csv) | **Postings by experience requirement, 2022–24.** `0-1 tahun`: 1,833 → 1,807 → **2**. See the flag below — do not plot this as a trend without checking with Kemnaker | repo |
| [build/prov.csv](build/prov.csv) | Employers posting by province: national 2,483 → 2,730 → 2,644; DKI Jakarta 389 → 492 → 576 | repo |

> **Flag on [emp.csv](build/emp.csv).** The portal's own `0-1 tahun` (entry-level) postings fall from 1,807 in 2023 to
> **2** in 2024, while `tidak ada informasi` (not stated) absorbs 5,126. A collapse that extreme is far
> more likely a change in how the portal captured the field than a collapse in entry-level hiring — our
> own ad sample shows entry-level wording in roughly one in ten finance/BPO ads. **Treat it as a
> data-capture question for Kemnaker, not as a finding.** It is a strong candidate for the one
> interview question the plan asks for.

### E. Pages and reports (`build/`, deployed via `dist/`)

| File | What it is | Live URL | Status |
|---|---|---|---|
| [build/spar-id-postings.html](build/spar-id-postings.html) | Individual-postings report: method, refusals, coverage, AI-skill table, filterable posting table | [`/build/spar-id-postings`](https://spar-f26-id.pages.dev/build/spar-id-postings) | **live** |
| [build/spar-id-ecosystem-map.html](build/spar-id-ecosystem-map.html) | Ecosystem, policy and bridge maps (~210 KB, SVG-driven) | [`/build/spar-id-ecosystem-map`](https://spar-f26-id.pages.dev/build/spar-id-ecosystem-map) | **live** |
| [build/spar-id-overview.html](build/spar-id-overview.html) | Overview + 7 highlights + 4 policy scenarios + portal counts + exposure scores | — | **local** (deploy blocked) |
| [build/spar-id-model-demo.html](build/spar-id-model-demo.html) | Interactive scenario-model demo (current-data vs with-more-data) | see `dist/build/` | repo |
| [build/spar-signal-feasibility.html](build/spar-signal-feasibility.html) | The S5 vacancy feasibility test write-up | see `dist/build/` | repo |
| [build/model_section.html](build/model_section.html) | Partial markup embedded into the dashboard build | — | repo |
| [build/proposal-wireframe.html](build/proposal-wireframe.html) | The one-page light-theme wireframe for the proposed report site — hero, four findings tiered, the 2×2 with its undrawn quadrant, the outlook strip and the compare strip. Uses only figures already verified in the register; unsigned scenario bands print `bracket pending` | — | repo (not deployed) |
| [build/eco_theme.css](build/eco_theme.css) | Shared light-theme tokens for the map and overview pages | — | repo |
| [build/spar-id-eco.svg](build/spar-id-eco.svg), [spar-id-bridge.svg](build/spar-id-bridge.svg), [spar-id-policy.svg](build/spar-id-policy.svg), [spar-id-ecosystem-map.svg](build/spar-id-ecosystem-map.svg) | The SVG sources behind the ecosystem page | — | repo |
| [dist/index.html](dist/index.html), `dist/build/*` | Generated output — **never hand-edit**; what Cloudflare Pages serves | [spar-f26-id.pages.dev](https://spar-f26-id.pages.dev) (dashboard is gated, HTTP 401) | generated |

### F. Build scripts

| Script | What it does |
|---|---|
| [build/build_dashboard.py](build/build_dashboard.py) | `data/*.csv` → [dist/index.html](dist/index.html) (the gated dashboard) |
| [build/build_overview.py](build/build_overview.py) | `data/id-postings/postings-*.csv` + `data/kemnaker/*.csv` → [build/spar-id-overview.html](build/spar-id-overview.html) (stdlib only) |
| [build/build_ecosystem_map.py](build/build_ecosystem_map.py) | `data/ecosystem-id-*.json` → [build/spar-id-ecosystem-map.html](build/spar-id-ecosystem-map.html) + SVGs |
| [build/build_postings_report.py](build/build_postings_report.py) | `postings-*.csv` + [summary.json](data/id-postings/summary.json) → [build/spar-id-postings.html](build/spar-id-postings.html) |
| [build/prep_postings.py](build/prep_postings.py) | Raw scrape → normalised, year-sharded CSVs (calls `ai_classify`) |
| [build/ai_classify.py](build/ai_classify.py) | The AI/data/digital-basic requirement classifier |
| [build/verify_postings.py](build/verify_postings.py) | Re-fetches a sample of rows and writes [verification.json](data/id-postings/verification.json) |
| [build/sync_sheets.py](build/sync_sheets.py) | GSheets → `data/*.csv` (the hourly job; **needs creds**) |
| [build/check_parity.py](build/check_parity.py) | Read-only diff: does the sheet still agree with `data/*.csv`, row for row? |
| [build/sync_map_from_register.py](build/sync_map_from_register.py) | `--check` (default) prints the drift between the register and the ecosystem map; `--write` rebuilds the map's **policy nodes** from `id-policy-inventory.csv` + `id-instruments.csv`. Keeps hand-written node detail; never touches bands, edges, marks or the responsibility map |
| [build/seed_sheet.py](build/seed_sheet.py) | One-off seeding of the six tabs from `data/seed/` |
| [deploy.sh](deploy.sh) | Build + `wrangler pages deploy` |
| [tools/scrape_karirhub.py](tools/scrape_karirhub.py) | Standalone, robots-aware scraper that writes the team schema |
| [functions/_middleware.js](functions/_middleware.js) | Access gate: dashboard gated, `/build/*` public |

### G. Task and continuity notes

| File | What it is |
|---|---|
| [SPAR_Fall2026_Shafira_Tasks.md](SPAR_Fall2026_Shafira_Tasks.md) | Shafira's task card extracted from the six-week plan deck (roles, deliverables, dates) |
| [build/CTO-HANDOFF.md](build/CTO-HANDOFF.md) | CRO → CTO handoff: open items, decisions left open |
| [.github/workflows/sync.yml](.github/workflows/sync.yml) | Hourly sheet → repo sync (+ Apps Script dispatch) |
| [.github/workflows/deploy.yml](.github/workflows/deploy.yml) | Build + Cloudflare Pages deploy (runs only on push to `main`) |

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

## The pipeline

```text
GSheets (team edits) ──sync──▶ repo /data/*.csv ──build──▶ dist/index.html ──▶ Cloudflare Pages (gated dashboard)
Google Drive         ──walk──▶ spar-f26-drive-index.md ──▶ repo (audit trail)
build/*.html         ──copy──▶ dist/build/*            ──▶ Cloudflare Pages (PUBLIC reports)
postings-*.csv + kemnaker/*.csv ──build_overview──▶ build/spar-id-overview.html
```

| Layer | Where | Who edits |
|---|---|---|
| Source of truth | Google Drive — folder `1WW-Af6uO5_k9MQeHpnbIqjqvyeHo0-el` | the team |
| Tracker (India team progress) | Sheet [1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ](https://docs.google.com/spreadsheets/d/1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ/edit) | the team |
| Register / skeleton / trackers | see "The sheets" below | the team |
| Audit trail | this repo, `data/*.csv` | the sync job |
| Team view | Cloudflare Pages (dashboard) | nobody — read-only, **gated** |
| Public view | Cloudflare Pages `/build/*` | nobody — read-only, **public** |

**Nothing writes back to Google Drive or Google Sheets.** This is a one-way mirror.

## The sheets

[data/sheets.json](data/sheets.json) maps a **tab name** to an output CSV; the Sheets API is used by tab name, so the
"CSV export only returns the first tab" gotcha does not apply.

| Sheet | ID | Tab(s) | What is in it |
|---|---|---|---|
| Core file — the register | [1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit) | `signals` (gid `838965401`), `triggers`, `Indonesia policy inventory`, `readiness`, `who-can-act`, `instruments` | 22 Indonesia signal rows; each policy document; the six readiness questions |
| SPAR signals skeleton (team) | [1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo](https://docs.google.com/spreadsheets/d/1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo/edit) | `README`, `SIGNALS`, `SIGNALS_ID`, `(dani notes)`, `LOG` | S1–S10 signal definitions in three layers; **`SIGNALS_ID` = the Indonesia indicator table** (indicator · source · policy · verdict · capability · details); the observation log. `README` carries the policy legend, the layer definitions and the float-up key |
| IND team progress | [1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ](https://docs.google.com/spreadsheets/d/1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ/edit) | `Sheet1` | Every Indonesia deliverable with progress, status, PIC |

### Direct links — every tab, clickable

The sheets are navigable: cells carry cross-tab links, so a policy name jumps to its row in the register
and a signal code jumps to its definition. Use these links directly, or click through from the cells.

| Sheet | Tab | Link |
|---|---|---|
| Core file | `signals` (22 rows, the register) | [gid=838965401](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=838965401) |
| Core file | `Indonesia policy inventory` (16 rows) | [gid=562214644](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=562214644) |
| Core file | `instruments` (6 levers) | [gid=2122536552](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=2122536552) |
| Core file | `who-can-act` (6 bodies) | [gid=2093456593](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=2093456593) |
| Core file | `triggers` | [gid=778752423](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=778752423) |
| Core file | `readiness` | [gid=597313565](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=597313565) |
| Skeleton | `SIGNALS_ID` (the indicator table) | [gid=265881413](https://docs.google.com/spreadsheets/d/1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo/edit#gid=265881413) |
| Skeleton | `SIGNALS` (signal definitions) | [gid=514284320](https://docs.google.com/spreadsheets/d/1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo/edit#gid=514284320) |
| Skeleton | `README` (legend + keys) | [gid=179910438](https://docs.google.com/spreadsheets/d/1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo/edit#gid=179910438) |
| Tracker | `Shafira's tasks` | [IND team progress](https://docs.google.com/spreadsheets/d/1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ/edit) |

**Cross-tab link graph (written 26 Nov, 134 cells — only where a cell was plain text, so no existing
hyperlink was overwritten):**

| From | Cell | Goes to |
|---|---|---|
| Core `signals` | `ian_signal` · `holder` | the `SIGNALS` row · the `who-can-act` row |
| Core `who-can-act` | `proposed_door` · `relevant_data_or_programme` | the `instruments` lever · the `policy inventory` row |
| Core `instruments` | `evidence` | the `who-can-act` row named in the cell |
| Core `Indonesia policy inventory` | `owner_agency` · `short_name` | the `who-can-act` row · the `readiness` row |
| Core `triggers` | `agency` · `action` | the `who-can-act` row · the lever it describes |
| Core `readiness` | `document` | the `policy inventory` row |
| Skeleton `SIGNALS` / `SIGNALS_ID` | `#` | each other's row for that signal |
| Skeleton `SIGNALS_ID` | `Indonesia's policy` | **each instrument name links to its own register row** (`textFormatRuns`, 18 cells / 55 links, wording unchanged) |
| Skeleton `README` | legend `P1`–`P10` names | the `policy inventory` row |

**Columns added 24–26 Nov (previously empty — revert ranges in [docs/SHEET-WRITE-2026-11-24.md](docs/SHEET-WRITE-2026-11-24.md)):**

| Sheet → tab | New columns | Contents |
|---|---|---|
| Core file → `signals` | `O`–`T` | `link` · `source_verbatim` · `confidence` · `data_status` · `not_verified` · `source_checked` |
| Skeleton → `SIGNALS` | `H`–`K` | Indonesian evidence · public source · status · gap/route |
| IND team progress → `Sheet1` | `G` | `Comments` — one line per task, plain language |
| Skeleton → `SIGNALS_ID` | `E`–`J` | `Indonesia's indicator` (name only, linked to the register row) · `Source` (compiled per shared indicator) · `Indonesia's policy` · `Verdict` · `Capability` · `Details` (the old single review column, split three ways on 26 Nov) |
| Skeleton → `SIGNALS` | `J` | `Relevant Policies` — the same instruments as `SIGNALS_ID`, one row per signal |
| Core file → `Indonesia policy inventory` | rows 5–17 | **3 → 16 rows.** The 7 other instruments the indicator table names (`UU 27/2026`, `PP 35/2021`, `PP 6/2025`, `Stranas KA`, `Kartu Prakerja`, `PP 44/2015`, `PP 46/2015`), the 5 the ecosystem map knew and the register did not (`RP3I 2026-2030`, the 50,000-worker programme, `PEKA`, `Sakernas × SIAPkerja`, the ILO–OJK–Kemenko collaboration) and `POJK 11/PADK 1` |
| Core file → `instruments` | rows 2–7 | **DEMO placeholder → 6 real levers**, one per actor's door in Part 4, each citing the `who-can-act` row or trigger card it rests on |

**Edit rules (all tabs):** header row is row 1 · `id` is the upsert and join key, never rename or
reorder · no merged cells, no blank spacer rows · one document per row · dates `YYYY-MM-DD` ·
`link` = the public source, not a Drive link · public sources only, no personal data · never rename a
header without telling CTO. Demo rows are marked `verified_by=DEMO`.

**Data is additive (Sha, 28 Nov 2026).** New data goes into the tab, row or column that already needs
it — never by replacing or removing what is there. Existing values and headers stay unless Sha says
otherwise in the session that is doing the work. Where a correction cannot be avoided, the superseded
reading stays and the new one is added beside it with its own period and vintage, so both can be cited.
This is why `app/data.js` now carries the August-round labour series *and* `LABOUR_ALT` for the
February and November readings instead of overwriting one with the other.

## Sync visibility — who changed what

Every sync run appends to [data/SYNC-LOG.md](data/SYNC-LOG.md) (newest first): timestamp, source, editor when known, and
per tab the `+added / −removed` counts with the changed `id`s. The dashboard renders the newest
entries in its **Recent changes** panel, and the commit message carries the editor.

| Trigger | Latency | Cost |
|---|---|---|
| Hourly cron (`17 * * * *`) | up to 60 min | negligible |
| Apps Script `onChange` → `repository_dispatch` | seconds | none (fires only on real edits) |

**Honest limit:** the service account reads cell *values*, not authorship. "Who edited" is only
knowable via the Apps Script trigger. Scheduled runs log the editor as unknown — expected, not a bug.

> **Currently failing.** `sync-sheets` fails on every hourly run: step *Sync tabs to CSV* succeeds,
> step *Commit if changed* fails. Consequence: the repo no longer mirrors the sheets (9 signal rows
> against the tab's 22), so the dashboard reads stale data and the 29 Nov sheet freeze cannot proceed.
> Owner: CTO / `@misshanna_bot`.

## Running it

```bash
python3 build/build_dashboard.py          # data/*.csv -> dist/index.html (+ dist/build/* reports)
python3 build/build_overview.py           # postings-*.csv + kemnaker/*.csv -> build/spar-id-overview.html
python3 build/build_ecosystem_map.py      # data/ecosystem-id-*.json -> map page + SVGs
python3 build/build_postings_report.py    # postings-*.csv -> build/spar-id-postings.html
python3 build/check_parity.py             # read-only: does the sheet still match data/*.csv?
python3 build/sync_sheets.py              # GSheets -> data/*.csv (needs creds)
./deploy.sh                               # build + wrangler pages deploy
```

## Live URLs (tested 24 Nov 2026)

| URL | Status |
|---|---|
| [https://spar-f26-id.pages.dev/](https://spar-f26-id.pages.dev) | 401 — gated dashboard (expected) |
| [https://spar-f26-id.pages.dev/build/spar-id-postings](https://spar-f26-id.pages.dev/build/spar-id-postings) | 200 — public |
| [https://spar-f26-id.pages.dev/build/spar-id-ecosystem-map](https://spar-f26-id.pages.dev/build/spar-id-ecosystem-map) | 200 — public |

> **Deploy is broken.** Cloudflare Pages fails authentication (error code 10000) — last successful
> deploy 22 Oct, failure first seen 5 Nov. Newly built pages therefore stay **local only**. Owner:
> CTO / `@misshanna_bot` (regenerate the CF API token with no expiry, update the repo secret).

## Secrets (never in this repo)

| Secret | Where | What |
|---|---|---|
| `SITE_PASSWORD` | Cloudflare Pages project secret | access-gate password (dashboard only; `/build/*` is public) |
| `SHEET_ID` | GitHub repo secret | the Google Sheet's ID |
| `GOOGLE_SERVICE_ACCOUNT` | GitHub repo secret | read-only service-account JSON |
| `SYNC_PAT` | GitHub repo secret | PAT used by the sync job to push past the Main-rule code-scanning gate |
| `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID` | GitHub repo secrets | Pages deploy — **currently rejected (code 10000)** |

```bash
wrangler pages secret put SITE_PASSWORD --project-name spar-f26-id
```

---

## Shafira's task progress (SPAR Fall 2026)

> Tallied **2026-11-28** from the `SIGNALS_ID` indicator table, the Core file (9 tabs: 22 signals,
> 16 policy instruments, 6 levers, 6 bodies), the generated ecosystem map (22 policy nodes), the
> Perplexity verification run, Kemnaker's own portal counts, `IND team progress` and repo state.
> Supersedes the 2026-11-26 tally.

```
Data spine        ███████████████████████░   97%  22 signals + 16 policies + 6 levers; id-shock-data 48 evidence rows (ID-12 x33, ID-17 x5, run-1 x10)
Data list (lead)  ███████████████████████░   95%  public source + verbatim + H/M/L on all rows; sources compiled per shared indicator; duplicates cleared
Part 3 (signals)  ███████████████████░░░░░   80%  country report v0.4 drafted end to end on the sourced base - shocks, ads, backtest, asks; needs Shafira's read
Part 4 (policy)   ████████████████████░░░░   85%  v1 written and reframed; its data is in the register; waiting on Ian's read + the word trim
Shared sheet/repo ██████████████████████░░   93%  register, model, app and postings tabs agree; sync job still failing, so the freeze is not safe
Section 5 (SPAR)  ██░░░░░░░░░░░░░░░░░░░░░░   10%  2,500w Indonesia chapter; report v0.4 is the raw material
Section 8 (Limits)██████████████░░░░░░░░░░   60%  draft ready to read with Napat
Interview (BPS)   █████░░░░░░░░░░░░░░░░░░░   20%  question reframed as a data-availability enquiry
Atlas site        ████████████████░░░░░░░░   65%  postings evidence added, light theme, 8-bank panel, net flows; deploy still not done
```

**Backfilled from the Hermes logs — Thu 26 and Fri 27 Nov.** Work that happened in the sessions but did
not leave a commit, recorded here so the progress bar is not flattering itself:

| When | What she did | Where it lives now |
|---|---|---|
| **Thu 26, 09:24–10:07** | Directed the `SIGNALS_ID` build point by point: the six own indicators pulled out of the tab, the new column, the no-redundancy rule ("if yes, must show details that makes it cited"), indicator **names only**, verdict first in the review, duplicates removed, one compiled source per shared indicator, acronyms in place of `P7`/`P8` | skeleton `SIGNALS_ID` |
| **Thu 26, ~11:00** | Restructured the Core `signals` tab with `signal_code`, `indicator_no`, `data_layer`, `next_step`, `origin_code` — the columns the 26 Nov merge had to respect | Core file `signals`, now 23 columns (re-verified 28 Nov) |
| **Fri 27, 18:46–18:54** | Set the **ground layer** going — the official files (Kemnaker Satudata PHK, OJK banking statistics, BPS, BPJS JKP) — and prototyped an `id-shock-data` tab, 29 columns, with the first real platform counts. **Jobstreet publishes a total (68,114 postings); most Indonesian boards are JS-only and publish nothing** | tab was closed on her instruction; the schema and the counts survive in the kit below |
| **Fri 27, 18:58–19:08** | Built the **BoxCompute kit** so the collection can run without her narrating it: a 92-line self-contained prompt, the ID+PH indicator spine as CSV, Akbar's six measures as PDF, a column dictionary and a 37 KB source registry | [`docs/boxcompute-kit/`](docs/boxcompute-kit/) |
| **Fri 27, 18:59–19:03** | Read the team's `SPAR indicator table — ID + PH (draft 26 Nov 2026)` (25 indicators per country) and Akbar's six measures, and set the crosswalk **S1–S10 × M1–M6** before writing anything | kit + the indicator table |
| **Fri 27, 19:33–19:34** | The 22-row merge into `signals` overwrote her `M1:W1` headers. It was reported immediately rather than papered over; the header row is now clean and 23 columns wide — I re-verified it on 28 Nov | Core file `signals` |
| **Fri 27, 18:30 Jakarta** | Indonesia team call with Akbar and Natraj (calendar) | — |

Two honest footnotes. **The `id-shock-data` tab she closed leaves the ground-layer collection designed but
not running** — the kit is its executable form, so the next step is a BoxCompute run, not more design. And
**None of the Friday work was in the repo until now**: the kit sat in `~/.hermes/projects/productivity/`
and the sheet was deleted, which is exactly the gap that makes a progress bar lie.

**Moved on 26 Nov — the indicator table, and the register made navigable:**

- **S1–S10 each mapped to an Indonesia indicator**, every row linked to the exact register row it came
  from (S3 and S4 correctly show none, because no indicator exists for them yet).
- **Source compiled per shared indicator.** Where one indicator serves several signals, its `Source`
  cell now carries the union of what backs it (e.g. M1 → `ILO · BPS`), so the same indicator reads
  identically wherever it appears.
- **Policy mapped and de-coded.** Every instrument is named in full with its acronym — `UU 27/2026`,
  `POJK 11/POJK.03/2022 and PADK OJK 1/2026`, `JKP (PP 37/2021)`, `Stranas KA 2020-2045`, `Kartu Prakerja` — and hyperlinked to
  its official source. Full titles, status and links live once in the tab's `README`, not on every row.
- **The long review cell is now three columns: `Verdict` · `Capability` · `Details`.** The full reading
  sits on the first row of each signal; the other rows of that signal carry the verdict and the
  capability line plus a one-line pointer, so no paragraph is repeated 2–5 times.
- **Reframed to the team's own question.** Each `Details` line now closes on what the signal *cannot*
  tell us about an AI economic shock — e.g. S5: *"a fall in banking vacancies caused by AI would look
  identical to a fall caused by a change in the rules."*
- **Float-up highlighting on the rows that should be raised, not just read.** Rose `#FCE8E6` = the
  shock would be invisible (S1, S3, S4); amber `#FFF2CC` = the number exists but cannot be read as an
  AI shock on its own (S5–S10); plain = S2 only. The key sits on the tab's `README`.
- **Duplicates and dead weight removed:** the indicator column was checked for repeats, the stray
  leftover row was cleared, layer definitions and the policy legend were moved out of the repeated
  cells into the tab's `README`, and one broken pointer (S8 had lost the row it pointed at) was rebuilt.
- **The sheets are now navigable.** 134 cross-tab links: a policy name jumps to its register row, a
  signal code to its definition, an actor to its lever, a lever back to the actor. `SIGNALS_ID`'s policy
  column links **each instrument name separately** to its own row in the register.
- **Part 4 in the register, so the map can read it.** `Indonesia policy inventory` 3 → **16 rows**;
  `instruments` DEMO → **6 real levers**; new generator
  [build/sync_map_from_register.py](build/sync_map_from_register.py) keeps the map's policy nodes in
  step with the register (9 → **22 nodes**), which is why the map page now shows `UU 27/2026`,
  `PP 6/2025`, `POJK 11`, `Stranas KA`, `RP3I` and the six levers.

**Moved on 28 Nov — the product, and the reference base:**

- **Studied the Windfall scenarios site** (`scenarios-2030.windfalltrust.org`) and wrote the proposal:
  ten patterns that work for a policy reader, what we must not copy, seven routes (five already built),
  two scenario axes our own evidence can support, and the evidence grammar — see
  [docs/ID-POLICY-SITE-PROPOSAL.md](docs/ID-POLICY-SITE-PROPOSAL.md).
- **A wireframe that shows it** — [build/proposal-wireframe.html](build/proposal-wireframe.html), light
  theme, using only figures already verified in the register; unsigned scenario bands print
  `bracket pending` rather than an invented midpoint.
- **The reference base indexed** — [docs/REFERENCE-LIBRARY.md](docs/REFERENCE-LIBRARY.md) cites the
  twelve third-party documents we rely on instead of redistributing them; eight of the twelve are
  voluntary corporate disclosures, which is itself one of the study's findings.
- **Work log added** — [the 24–28 Nov log](#work-log--everything-built-2428-november-2026) records every
  artefact with the PR or audit entry that carries it.
- **The model was backtested against the series that claims to measure it.** National JKP claims carry an
  8.8% noise floor inside two months; Extreme's ~100 claims a year is 0.11% of that. To shift the annual
  number 1% needs 1,090 layoffs in one year — 1.8× the model's entire five-year Extreme total. The model
  survives; the instrument does not. See [MODEL-BACKTEST](docs/MODEL-BACKTEST.md).
- **Attrition turned out to be the biggest lever, not adoption.** All-leavers attrition (6.11%) gives 602
  Extreme layoffs and Rp 9.0 bn; voluntary-only (4.38%) gives 7,718 and Rp 115.3 bn — a 12.8× swing with
  2030 headcount unchanged. Published as a sensitivity, not a new default: [MODEL-ATTRITION-SENSITIVITY](docs/MODEL-ATTRITION-SENSITIVITY.md).
- **The model sheet was brought to v0.3b** (and renamed): 8-bank panel with reported hires, leavers and
  turnover; `Feed_Panel` gained total and voluntary turnover columns; panel 218,129 and 2030 headcount
  216,951 / 210,346 / 191,884 — reproduced by `app/model.js` in node with zero delta.
- **The register went to 38 evidence rows** (`id-shock-data`, 31 columns): 27 new p6 rows of bank-level
  hires, leavers and turnover, appended after a schema and duplicate check.
- **The team table's stale ID-12 was refreshed** to the Dec-2025 panel, with the BNI contradiction and the
  turnover split appended to its notes rather than replacing what was there.
- **The six readiness question texts now exist** — reconstructed from the worksheet's own A–F evidence
  blocks, written into `readiness!M1:N8` with the "grades documents, never a government" caution, and
  labelled a proposal for Akbar to confirm.
- **Everything the next BoxCompute run needs is in one kit**: [`docs/boxcompute-kit/`](docs/boxcompute-kit/),
  now including the register export, plus the six collection targets in
  [DATA-FEED-GAPS-28NOV](docs/DATA-FEED-GAPS-28NOV.md) and the shareable summary in
  [TEAM-SHARE-28NOV](docs/TEAM-SHARE-28NOV.md).
- **The 1.03m-advertisement corpus is in, analysed and reconciled.** Banking exposure **0.582** (20,088 ads,
  94.3% in G2-G4), the crawl validated against a same-month census within **0.57 pt**, and only **Dealls**
  reconciles against our own `id-postings` (ratio **0.84**, median month **0.97**, monthly spread
  **0.30-1.67**) - which sets the noise floor for any postings claim. Two new tabs (`postings-monthly`,
  `postings-exposure`) plus `postings-recon`; Glints and Kalibrr are truncated and must never be trended.
- **The country report is drafted as v0.4** - eight-bank panel, measured exposure, the backtest verdict, the
  attrition sensitivity, the four asks: `docs/COUNTRY-REPORT-v0.4.md` (HTML rendered alongside).
- **The app and atlas were refined and moved to a light theme**: a postings section with the monthly panel
  and exposure by category, the corrected panel KPI (218,129 across eight banks, not 151,340 across five),
  and a postings section in the atlas that gives S5 its supply side.

**Pull requests:** [#35](https://github.com/webdevsha/spar-f26-id/pull/35) the first progress tally ·
[#36](https://github.com/webdevsha/spar-f26-id/pull/36) Part 4 v1 + the register and map work ·
[#37](https://github.com/webdevsha/spar-f26-id/pull/37) the tab links and the link graph ·
[#38](https://github.com/webdevsha/spar-f26-id/pull/38) the proposal, the wireframe and the work log —
**all four merged**. [#39](https://github.com/webdevsha/spar-f26-id/pull/39) carries the one-pager, the
scenario export and the reference-library index, and **cannot merge yet**: the `main` ruleset requires
CodeQL to be clean at error severity, and alert
[#4](https://github.com/webdevsha/spar-f26-id/security/code-scanning/4)
(`py/clear-text-storage-sensitive-data`, `build/build_overview.py:607`) is open on `main`. That alert sits
on the base branch, so it holds every pull request until it is fixed or dismissed. Part 4 itself:
[docs/ID-PART4-DRAFT.md](docs/ID-PART4-DRAFT.md) (the section has no Google Doc; the repo draft is its
only home).

**Evidence behind the bars:** `id-shock-data` — **38 evidence rows** (31 columns) · `SIGNALS_ID` — 18 indicator rows across S1–S10, verdict + capability on
every row, 10 full readings, 9 of 10 signals flagged for float-up · Core file `signals` — 22 rows ·
`triggers` 1 · `who-can-act` 6 · policy inventory **16** · readiness 3 (all `tbc`) · instruments **6 real
levers** (the DEMO placeholder is gone) ·
postings 2,618 rows (2024→Oct 2026) · Kemnaker portal counts 2022–24 in `data/kemnaker/` ·
[docs/ID-SIGNAL-SOURCE-MATRIX.md](docs/ID-SIGNAL-SOURCE-MATRIX.md),
[docs/ID-PART3-DRAFT.md](docs/ID-PART3-DRAFT.md), [docs/ID-READINESS-WORKSHEET.md](docs/ID-READINESS-WORKSHEET.md), [docs/ID-PENDING-24NOV.md](docs/ID-PENDING-24NOV.md),
[docs/SHEET-WRITE-2026-11-24.md](docs/SHEET-WRITE-2026-11-24.md) (revert ranges for every sheet write, 24–26 Nov).

**Open question on the table:** **M6 has no row** in `SIGNALS_ID` — coverage is M1 ×6, M2 ×5, M3 ×2,
M4 ×6, M5 ×5, plus rows still without an indicator. Either a signal carries M6, or it should be marked
unused so the register's six-measure structure does not look one short.

**Next due:** Fri 27 Nov (one interview about data gaps) → Sun 29 Nov (sheet frozen into the repo —
blocked by the sync failure) → Wed 2 Dec (§5 + §8 to Rachel). SPAR submission 14 Dec; Demo Day 19 Dec.

## Open items and blockers

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Hourly sheet → repo sync failing at its commit step | CTO / `@misshanna_bot` | The 29 Nov freeze; every `data/*.csv` consumer |
| 2 | Cloudflare Pages deploy auth failure (code 10000) | CTO / `@misshanna_bot` | Every new page going live |
| 3 | Readiness scoring — 3 documents × 6 questions | Shafira | Needs the six question texts (not recorded anywhere; the tab holds only `q1`–`q6`) |
| 4 | Regulator-facing requests: 15 routes surfaced to BPJS, OJK, Kemnaker, BPS, DPR Commission IX, plus a scope question on platform data obtained via web archives | **@clo before anything is sent** | Nothing sent to date |
| 5 | [data/id-signals.csv](data/id-signals.csv) etc. mirror stale vs the sheets | sync job (#1) | Dashboard accuracy |

## BoxCompute collection (24 Nov 2026)

**Why BoxCompute.** The lane's posting evidence currently rests on one government portal plus a
sampled archive (2,618 rows). The v2 brief ([docs/PROMPTS-BOXCOMPUTE-V2.md](docs/PROMPTS-BOXCOMPUTE-V2.md)) moves to an
**archive-first** design across 13 platforms, **Indonesia only** (the Philippines lane was dropped on 24 Nov as this study covers Indonesia), because that is both the ToS-clean route to volume and
the only route that reaches a platform's own published scale.

**Target (v2 brief, Step 1).** Per platform: `distinct posting URLs` by year, plus a coverage probe —
*counts first, no fetching until the counts exist*. Q1, honestly asked: **how much is actually
archived?** Until that is answered, any collection number is a guess.

**Collection runs in a BoxCompute sandbox, driven by the CLI** (`bxc sandbox exec`), not through the
web chat: the chat surface is not exposed by the CLI, SDK or REST API, and a scripted sandbox puts
results in the repo as artefacts instead of chat prose.

Artefacts produced by the run are committed under [`data/boxcompute/`](data/boxcompute/):

| File | What |
|---|---|
| [census.json](data/boxcompute/census.json) | per platform: CDX page probe, distinct URLs per year, the scoped CDX target, and whether the host was capped |
| [patterns.json](data/boxcompute/patterns.json) | per host: distinct URLs → **posting-like** URLs, the rate, and the URL shapes behind both — the derivation of the posting filters from evidence rather than guesswork |
| [url_shapes/](data/boxcompute/url_shapes) | sampled distinct URLs, one file per host (e.g. [kitalulus.com.txt](data/boxcompute/url_shapes/kitalulus.com.txt)) |
| [census.log](data/boxcompute/census.log) | full request log, including every backoff |
| [harvest.log](data/boxcompute/harvest.log) | Stage 2 `job_card` harvest progress, bucket by bucket |

**Method, and its limits.** Wayback CDX only: `collapsed=urlkey`, `statuscode:200`, one request every
3 s, backoff on 429/503/504, and a User-Agent that identifies the crawler as an academic study.
Three cautions are part of the result, not footnotes:

- **Distinct URLs ≠ postings ≠ hires.** A URL can be one ad or one search page; CDX volume is a
  property of the crawl, not of hiring. No figure from this run may be read as a level of demand.
- **CDX page counts are a volume probe only.** An assumed page size would be an invented figure, so
  the raw page count is reported and nothing is extrapolated from it.
- **Some hosts are too large for a single CDX response.** Piercing `jobstreet.co.id` and
  `linkedin.com` needs monthly pagination; where a host is skipped or throttled the table says so.

**Census complete (24 Nov, 10 Indonesian platforms).** The census produced a number that must
**not** be quoted as-is, and finding that out is the run's first real result.

Raw distinct-URL counts are dominated by non-postings: on KitaLulus, 16,172 of 183,982 distinct URLs
are `/_next/image` paths; on Dealls, tens of thousands are city × category *search permutations*.
Posting patterns were therefore **derived from the data** — see
[patterns.json](data/boxcompute/patterns.json) — and applied as a filter:

| Platform | 2024 | 2025 | 2026 (to 30 Nov) | Distinct URLs | Posting-like | Rate |
|---|---:|---:|---:|---:|---:|---:|
| Glints ⚠️ *capped* | 100,000 | 100,000 | 33,876 | 233,876 | 136,451 | 58.3% † |
| KitaLulus | 49,881 | 72,729 | 61,372 | 183,982 | 71,076 | 38.6% |
| Dealls | 17,946 | 26,471 | 31,928 | 76,345 | 67,647 | 88.6% |
| Kalibrr | 28,039 | 12,423 | 2,518 | 42,980 | 29,455 | 68.5% |
| JobStreet ID ⚠️ *capped* | 20,000 | 0 | 0 | 20,000 | 18,327 | 91.6% † |
| LinkedIn Jobs ⚠️ *capped* | 0 | 0 | 20,000 | 20,000 | 20,000 | 100.0% † |
| Karirhub (ours) | 5,772 | 7,266 | 270 | 13,308 | 12,390 | 93.1% |
| Karir.com | 4,118 | 2,197 | 1,006 | 7,321 | 52 | 0.7% † |
| Pintarnya | 0 | 0 | 0 | 0 | 0 | — |
| Bossjob | 0 | 0 | 0 | 0 | 0 | — |
| **Total (10 of 10 ID)** | | | | **597,812** | **355,398** | 59.4% |

Three cautions are part of the result, not footnotes:

- **The total is a floor, not a total.** Three hosts stopped at a per-request cap — Glints at exactly
  100,000 for two consecutive years, JobStreet ID and LinkedIn at 20,000 — so those rows are minimums.
- **† The filter errs both ways.** It over-counts where a URL is a search permutation, and
  under-counts where the real pattern was not anticipated: Karir.com's pattern is
  `/opportunities/<num>` (4,658 URLs), so its rate reads wrongly near-zero. JobStreet ID and LinkedIn
  each returned a zero year whose neighbours are full — a failed query, not a year without vacancies —
  so those cells are unusable. Posting-like is a **per-platform sanity signal, never a cross-platform
  ranking.**
- **Distinct URLs ≠ postings ≠ hires.** A URL can be one ad or one search page; CDX volume is a
  property of the crawl, not of hiring. 2026 is a partial year and is not comparable on its own.

**Stage 2 (`job_card` harvest) is running**, chained into Stage 3 (`full_page`). Stratified 25 URLs per
platform-month, extracted via schema.org `JobPosting` where the page carries it, falling back to
OpenGraph. Every row carries `posted_basis` (`jsonld` | `capture_proxy`) so a crawl date can never be
read as a posting date, and rows without a title or employer go to a rejected file rather than being
emitted blank. Progress in [harvest.log](data/boxcompute/harvest.log).

**Access is not the constraint.** From the sandbox: Wayback CDX **200**, Common Crawl index **200**,
Karirhub live **200**, Pasker ID **200**. By contrast Algolia (`algolia.kemnaker.go.id`, the
`L3WWP72HSI` shard) is **unreachable from both the sandbox and the agent network**, and Glints /
LinkedIn / JobStreet direct requests return **403/403/308**. The archive-first design is therefore
not a preference — it is the only route that works and the only one that respects the platforms.

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

## Work log — everything built, 24–28 November 2026

One row per artefact. Every row is a file in this repo, a PR, or an entry in
[docs/SHEET-WRITE-2026-11-24.md](docs/SHEET-WRITE-2026-11-24.md) — nothing here is a claim without an artefact.

### 24 November — the ground work

| What | Where it landed |
|---|---|
| **First shared-sheet writes**: signal layer + evidence columns in the Core file (`signals` O–T), the skeleton (`SIGNALS` H–K), and `IND team progress` G | Core file + skeleton · audit and revert ranges in [SHEET-WRITE](docs/SHEET-WRITE-2026-11-24.md) |
| **README header made true and readable by policymakers** — claims narrowed to what the data carries | PR [#33](https://github.com/webdevsha/spar-f26-id/pull/33) |
| **Live intake made always-on** — sandbox collector publishing to the Worker | PR [#34](https://github.com/webdevsha/spar-f26-id/pull/34) |
| **Source verification**: 22-row source matrix (5 status corrections, 2 attribution traps, 3 denominator traps), the Perplexity verification pack, and the BoxCompute collection briefs | [ID-SIGNAL-SOURCE-MATRIX](docs/ID-SIGNAL-SOURCE-MATRIX.md) · [ID-SIGNALS-PERPLEXITY-PACK](docs/ID-SIGNALS-PERPLEXITY-PACK.md) · [PROMPTS-BOXCOMPUTE-V2](docs/PROMPTS-BOXCOMPUTE-V2.md) |
| **Kemnaker's own portal counts, 2022–24** — the only free vacancy series that needs no scrape | [data/kemnaker/](data/kemnaker/) |
| **Postings at scale**: Karirhub 13,308 and Dealls 44,417 distinct URLs proven collectable; 2,618 rows in the team schema (2024 → Oct 2026) | [data/id-postings/](data/id-postings/) · [build/spar-id-postings.html](build/spar-id-postings.html) |

### 26 November — the indicator table, and the register made navigable

| What | Where it landed |
|---|---|
| **`SIGNALS_ID` built**: S1–S10 each mapped to an Indonesia indicator, the name linked to the exact register row it came from, the source compiled once per shared indicator so the same indicator reads identically everywhere | Skeleton `SIGNALS_ID` · [SHEET-WRITE](docs/SHEET-WRITE-2026-11-24.md) |
| **Policy de-coded**: every instrument named in full with its acronym (`UU 27/2026`, `POJK 11/POJK.03/2022 and PADK OJK 1/2026`, `JKP (PP 37/2021)`, `Stranas KA 2020-2045`), hyperlinked, with titles and status in the tab's own `README` | Skeleton `README` + `SIGNALS_ID` G |
| **The one long review column split three ways** — *Verdict · Capability · Details*; full reading on the first row of each signal, one-line pointer on the rest; the broken S8 pointer rebuilt; duplicates and dead weight cleared | Skeleton `SIGNALS_ID` H–J |
| **Every reading reframed to the team's question** — each Details line closes on what the row cannot tell us about an AI economic shock | Skeleton `SIGNALS_ID` H–J |
| **Float-up highlighting**: rose = the shock would be invisible (S1, S3, S4); amber = the number exists but cannot be read as an AI shock alone (S5–S10); plain = S2 — with the key stated once on the tab `README` | Skeleton `SIGNALS_ID` A–M + `README` |
| **Task progress re-tallied** from the indicator table | PR [#35](https://github.com/webdevsha/spar-f26-id/pull/35) |
| **Part 4 v1 written** — who can act and the policies in place, reframed to the shock question, three flags for Ian, word count stated honestly against the 600-word target | [ID-PART4-DRAFT](docs/ID-PART4-DRAFT.md) · PR [#36](https://github.com/webdevsha/spar-f26-id/pull/36) |
| **Part 4's data into the register**: `Indonesia policy inventory` 3 → **16 rows**; `instruments` DEMO placeholder → **6 real levers**, one per actor's door, each citing the row it rests on | Core file · PR [#36](https://github.com/webdevsha/spar-f26-id/pull/36) |
| **Cross-tab navigation**: 134 hyperlinks so a policy name opens its register row, a signal code its definition, an actor its lever and a lever back to the actor; `SIGNALS_ID` column G re-linked **per instrument** (18 cells / 55 spans, wording untouched) | Three sheets · PRs [#36](https://github.com/webdevsha/spar-f26-id/pull/36), [#37](https://github.com/webdevsha/spar-f26-id/pull/37) |
| **The register now generates the map**: `build/sync_map_from_register.py` (`--check` = drift report) rebuilt the map's policy nodes 9 → **22** — 8 hand-written nodes kept with their detail, 8 added, 6 lever nodes replacing the stale placeholder; bands, edges, marks and the responsibility map untouched | PR [#36](https://github.com/webdevsha/spar-f26-id/pull/36) |
| **README given the tab directory**: every tab's deep link, plus the cross-tab link graph | PR [#37](https://github.com/webdevsha/spar-f26-id/pull/37) |
| **Call run sheet** for the 22:00 SPAR call — six do-now items, six raise-on-call items, the numbers at hand, the two decisions needed | [ID-CALL-RUNSHEET-26NOV](docs/ID-CALL-RUNSHEET-26NOV.md) |

### 28 November — the product proposal

| What | Where it landed |
|---|---|
| **Studied `scenarios-2030.windfalltrust.org`** (home, a scenario page, compare, methodology) and distilled ten communication patterns that work for a policy reader — the load-bearing ones: a quadrant deliberately left empty *with its reason*, a scenario range always printed next to a real number, and gaps drawn as dotted segments rather than footnoted | [ID-POLICY-SITE-PROPOSAL](docs/ID-POLICY-SITE-PROPOSAL.md) §1 |
| **Refused what we cannot honestly copy**: signed workshop ranges, monthly official series, status-quo policy | §2 |
| **Proposed one product, seven routes** — five of which already have a built artefact in this repo; the genuinely new page is `/compare` | §3 |
| **Scenario axes our evidence can carry**: pace of AI deployment in banking (S1–S3) × strength of the adjustment buffer (S8, S10, readiness) — four worlds, one deliberately undrawn, three variants that each break one assumption | §4 |
| **Evidence grammar per number**: real / team-reported / gap / demo, with H–M–L confidence and a checked-on date; unsigned bands print `bracket pending`, never a midpoint | §5 |
| **Wireframe** — one light-theme page showing the hero, the four tiered findings, the 2×2 with its hatched "not covered" quadrant, the outlook strip and the compare strip | [build/proposal-wireframe.html](build/proposal-wireframe.html) |
| **Five gates named**, each a question for a person rather than for the drafting lane | §8 |
| **This work log**, the file-index corrections and the PR status fixes | PR [#38](https://github.com/webdevsha/spar-f26-id/pull/38) |

### Still open, stated plainly

| Item | State |
|---|---|
| `sync-sheets` hourly job | **failing** — the repo CSVs were mirrored by hand; the 29 Nov freeze depends on this |
| Cloudflare deploy of the overview and the new pages | not deployed; `dist/` is generated output and deploy needs an explicit go-ahead |
| `Read Me_Methods` tab in the team indicator workbook | **empty** — the methodology page has nothing to render from |
| Every indicator threshold | `Deferred` — the compare page cannot draw a line it does not have |
| Readiness questions `q1`–`q6` | not recorded anywhere, so the buffer axis is half-blind |
| `M6` in the measure register | has no row in `SIGNALS_ID` |
| Scenario bands | unsigned — they belong to the team, not to the drafting lane |
| Last three items to verify with Ian, Napat and Akbar | needs the SPAR call |
