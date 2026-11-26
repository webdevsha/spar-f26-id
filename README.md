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
| [ID-PART3-DRAFT.md](docs/ID-PART3-DRAFT.md) | Country Report Part 3 draft, 678 words, every figure traced; unverified figures left bracketed | Shafira | repo (untracked) |
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
| [ecosystem-id-map.json](data/ecosystem-id-map.json), [ecosystem-id-domains.json](data/ecosystem-id-domains.json) | The Indonesia ecosystem & policy map (actors, instruments, support routes) that renders as a public page | Shafira + Rachel | repo |
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

**Columns added 24–26 Nov (previously empty — revert ranges in [docs/SHEET-WRITE-2026-11-24.md](docs/SHEET-WRITE-2026-11-24.md)):**

| Sheet → tab | New columns | Contents |
|---|---|---|
| Core file → `signals` | `O`–`T` | `link` · `source_verbatim` · `confidence` · `data_status` · `not_verified` · `source_checked` |
| Skeleton → `SIGNALS` | `H`–`K` | Indonesian evidence · public source · status · gap/route |
| IND team progress → `Sheet1` | `G` | `Comments` — one line per task, plain language |
| Skeleton → `SIGNALS_ID` | `E`–`J` | `Indonesia's indicator` (name only, linked to the register row) · `Source` (compiled per shared indicator) · `Indonesia's policy` · `Verdict` · `Capability` · `Details` (the old single review column, split three ways on 26 Nov) |
| Skeleton → `SIGNALS` | `J` | `Relevant Policies` — the same instruments as `SIGNALS_ID`, one row per signal |

**Edit rules (all tabs):** header row is row 1 · `id` is the upsert and join key, never rename or
reorder · no merged cells, no blank spacer rows · one document per row · dates `YYYY-MM-DD` ·
`link` = the public source, not a Drive link · public sources only, no personal data · never rename a
header without telling CTO. Demo rows are marked `verified_by=DEMO`.

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

> Tallied **2026-11-26** from the `SIGNALS_ID` indicator table in the SPAR signals skeleton, the Core
> file `signals` tab (22 rows), the Perplexity verification run, Kemnaker's own portal counts,
> `IND team progress` and repo state. Supersedes the 2026-11-24 tally.

```
Data spine        ███████████████████████░  94%  22 signal rows; the S1–S10 indicator table now carries a source, a policy and a verdict per row
Data list (lead)  ███████████████████████░  95%  public source + verbatim + H/M/L on all rows; sources compiled per shared indicator; duplicate rows cleared
Part 3 (signals)  ██████████████░░░░░░░░░░  70%  678-word draft written from the sourced base; needs Shafira's read-through, not a rewrite
Part 4 (policy)   ██████░░░░░░░░░░░░░░░░░░  25%  who-can-act map + request routes ready; 600w with Ian pending (assembly, not discovery)
Shared sheet/repo ██████████████████░░░░░░  85%  indicator table now mirrors the review in three columns; hourly sync still failing, so the 29 Nov freeze is blocked
Section 5 (SPAR)  ██░░░░░░░░░░░░░░░░░░░░░░  10%  2,500w Indonesia chapter; data underpinning ready
Section 8 (Limits)█░░░░░░░░░░░░░░░░░░░░░░░   5%  not started (with Napat, Wed 2 Dec)
Interview (BPS)   ████░░░░░░░░░░░░░░░░░░░░  20%  question reframed as a data-availability enquiry; candidate question found (see the emp.csv flag)
Atlas site        ██████████░░░░░░░░░░░░░░  45%  ecosystem map + postings report live; overview/scenarios page built, deploy blocked
```

**Moved on 26 Nov — the Indonesia indicator table (`SIGNALS_ID`):**

- **S1–S10 each mapped to an Indonesia indicator**, every row linked to the exact register row it came
  from (S3 and S4 correctly show none, because no indicator exists for them yet).
- **Source compiled per shared indicator.** Where one indicator serves several signals, its `Source`
  cell now carries the union of what backs it (e.g. M1 → `ILO · BPS`), so the same indicator reads
  identically wherever it appears.
- **Policy mapped and de-coded.** Every instrument is named in full with its acronym — `UU 27/2026`,
  `POJK 38/SEOJK 21`, `JKP (PP 37/2021)`, `Stranas KA 2020-2045`, `Kartu Prakerja` — and hyperlinked to
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

**Evidence behind the bars:** `SIGNALS_ID` — 18 indicator rows across S1–S10, verdict + capability on
every row, 10 full readings, 9 of 10 signals flagged for float-up · Core file `signals` — 22 rows ·
`triggers` 1 · `who-can-act` 6 · policy inventory 3 · readiness 3 (all `tbc`) · instruments 1 (DEMO) ·
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
