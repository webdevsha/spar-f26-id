# spar-f26-id

**Technical spine of the SPAR Fall 2026 *Indonesia* lane** — the data and deployment
infrastructure behind the lane's AI-and-labour-market work.

This repository is not a document. It is the *machine* that turns the team's spreadsheet edits into a
versioned, auditable, and (where consented) public evidence base. The analysis and narrative live in
the shared deck and the Google Sheets tracker; this repo keeps that work **reproducible, diffable,
and shippable** without anyone hand-coding a webpage or re-exporting a CSV.

**Last full sync of this file: 24 November 2026.** If a file below is missing from this README, the
README is wrong — fix it in the same commit as the file.

---

## Start here (five files, in this order)

| # | File | Why |
|---|---|---|
| 1 | `docs/ID-PENDING-24NOV.md` | What is open, what is closed, and what "done" means for each item |
| 2 | `docs/ID-SIGNAL-SOURCE-MATRIX.md` | The sourced evidence base: 22 Indonesia signals, each with a public source, a verbatim figure, a confidence tag and its stated gap |
| 3 | `data/id-postings/README.md` | The hiring-signal dataset: schema, provenance, what refused us, and its limits |
| 4 | `docs/ID-HANDOFF-HANNACHAN.md` | Continuity: where the truth lives, the boundaries, the blockers |
| 5 | `build/spar-id-overview.html` | The lane's findings page: overview, highlights, policy scenarios |

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
| `ID-PENDING-24NOV.md` | The open/closed task ledger, with what "done" looks like per item | Shafira (ID lane) | repo |
| `ID-SIGNAL-SOURCE-MATRIX.md` | Source matrix v2 — the 22-row verified source line, 5 status corrections, 2 attribution traps, 3 denominator traps | Shafira + CRO | repo |
| `ID-PART3-DRAFT.md` | Country Report Part 3 draft, 678 words, every figure traced; unverified figures left bracketed | Shafira | repo (untracked) |
| `ID-READINESS-WORKSHEET.md` | 3 policy documents × 6 readiness questions, pre-loaded with the evidence each question answers from | Shafira | repo (untracked) |
| `ID-HANDOFF-HANNACHAN.md` | Continuity handoff: truth map, boundaries, blockers, order of work | CRO | repo (untracked) |
| `ID-SIGNALS-PERPLEXITY-PACK.md` | The verification brief sent to Perplexity (blocks A–E, rules, output contract) | CRO | repo |
| `PROMPTS-PERPLEXITY-BOXCOMPUTE.md` | Copy-paste prompt set: Perplexity verification (P1, P2) and the first BoxCompute collection brief (B1–B3) | CRO | repo |
| `PROMPTS-BOXCOMPUTE-V2.md` | **Current** collection brief — archive-first, three record kinds, 34-field schema, comparability gate (supersedes B1–B3) | CRO | repo |
| `SCRAPING-WITH-BOXCOMPUTE.md` | Plain-English guide to scraping with BoxCompute, using this Indonesia run as the worked example | CRO | repo |
| `SHEET-WRITE-2026-11-24.md` | Audit + revert instructions for the three shared-sheet writes made on 24 Nov | CRO | repo |
| `MODEL-INDONESIA.md` | How the scenario model maps onto Indonesia: what the data identifies, what must be calibrated | CRO + Natraj | repo |
| `back-up-research.md` | Evidence notes behind the six measures M1–M6, with sources per indicator | CRO | repo |
| `apps-script-trigger.gs` | Apps Script `onChange` hook → `repository_dispatch`, so a sheet edit reaches the repo in seconds | CTO | repo |

### B. Signal register and registers data (`data/`)

| File | What it is | Owner | Status |
|---|---|---|---|
| `id-signals.csv` | Mirror of the register's `signals` tab — **currently stale**: repo holds 9 rows, the sheet holds 22 | sync job | repo (stale) |
| `id-policy-inventory.csv` | Policy inventory: 3 documents (OJK AI guide, JKP, Pasker ID) | team | repo |
| `id-readiness.csv` | Readiness scoring join — all `q1`–`q6` still `tbc` | Shafira | repo (open) |
| `id-who-can-act.csv` | The who-can-act map: 6 organisations with proposed doors | Shafira + Rachel | repo |
| `id-instruments.csv` | Instrument map — **DEMO row only**, needs real rows | team | repo (open) |
| `id-triggers.csv` | Trigger card(s) — one row so far | Akbar | repo |
| `sheets.json` | Tab name → output CSV map used by the sync | CTO | repo |
| `SYNC-LOG.md` | Append-only record of every sync run: editors, `+added / −removed`, changed `id`s | sync job | repo |
| `PERSONAL-DATA-STOP.md` | The no-personal-data rule and what it means row by row | CRO | repo |
| `ecosystem-id-map.json`, `ecosystem-id-domains.json` | The Indonesia ecosystem & policy map (actors, instruments, support routes) that renders as a public page | Shafira + Rachel | repo |
| `ecosystem-ph-v0.json` | Philippines ecosystem stub — kept in this repo for parity; PH lane owns the content | BG | repo |
| `model-id-demo.json` | Inputs for the interactive model demo | CRO + Natraj | repo |
| `seed/*.tsv` | Original seed rows used to create the sheet tabs | CTO | superseded |

### C. The postings dataset (`data/id-postings/`)

| File | What it is | Owner | Status |
|---|---|---|---|
| `postings-2024.csv` (1.4 MB) · `postings-2025.csv` (1.8 MB) · `postings-2026.csv` (0.4 MB) | 2,618 archived Indonesian finance/BPO postings, 2024-02 → 2026-10, one row per posting, 37 columns | Shafira | repo |
| `README.md` | Schema, provenance, ethics, coverage limits for the dataset | Shafira + CRO | repo |
| `summary.json` | Counts used by the report builder (sectors, months, AI tiers, provinces) | build | repo |
| `verification.json` | Per-row re-fetch results (411 of 2,618 checked) | build | repo |
| `karirhub-id-postings-sample.csv` | The original 331-row sample from the first successful scrape | CRO | repo |
| `perplexity-id-data.md` | The verification run: 22 rows, 5 priority figures, request routes, contradictions | Shafira (run) | repo |

### D. Kemnaker's own portal counts (`data/kemnaker/` and `build/`)

These are the **portal's own advertised totals** — the weights any posting sample must be calibrated
to. All four are public CSV downloads from `paskerid.kemnaker.go.id/documents/`, no gate.

| File | What it is | Status |
|---|---|---|
| `data/kemnaker/Lowongan_Kerja_Menurut_Kategori_Lapangan_Usaha_Tahun_2022-2024.csv` | Postings and advertised slots by industry (KBLI 1-digit), 2022–24. Finance & insurance: **1,195 → 797 → 726** | repo |
| `data/kemnaker/Lowongan_Kerja_di_Karirhub_Menurut_Golongan_Pokok_Jabatan_Tahun_2022-2024.csv` | The same by occupation group (KBJI). Clerical (group 4): 1,751 → 3,341 → 2,034 | repo |
| `build/sector.csv` | Byte-identical copy of the industry file — **duplicate, should move to `data/kemnaker/`** | repo (duplicate) |
| `build/occ.csv` | Duplicate of the occupation file | repo (duplicate) |
| `build/emp.csv` | **Postings by experience requirement, 2022–24.** `0-1 tahun`: 1,833 → 1,807 → **2**. See the flag below — do not plot this as a trend without checking with Kemnaker | repo |
| `build/prov.csv` | Employers posting by province: national 2,483 → 2,730 → 2,644; DKI Jakarta 389 → 492 → 576 | repo |

> **Flag on `emp.csv`.** The portal's own `0-1 tahun` (entry-level) postings fall from 1,807 in 2023 to
> **2** in 2024, while `tidak ada informasi` (not stated) absorbs 5,126. A collapse that extreme is far
> more likely a change in how the portal captured the field than a collapse in entry-level hiring — our
> own ad sample shows entry-level wording in roughly one in ten finance/BPO ads. **Treat it as a
> data-capture question for Kemnaker, not as a finding.** It is a strong candidate for the one
> interview question the plan asks for.

### E. Pages and reports (`build/`, deployed via `dist/`)

| File | What it is | Live URL | Status |
|---|---|---|---|
| `build/spar-id-postings.html` | Individual-postings report: method, refusals, coverage, AI-skill table, filterable posting table | `/build/spar-id-postings` | **live** |
| `build/spar-id-ecosystem-map.html` | Ecosystem, policy and bridge maps (~210 KB, SVG-driven) | `/build/spar-id-ecosystem-map` | **live** |
| `build/spar-id-overview.html` | Overview + 7 highlights + 4 policy scenarios + portal counts + exposure scores | — | **local** (deploy blocked) |
| `build/spar-id-model-demo.html` | Interactive scenario-model demo (current-data vs with-more-data) | see `dist/build/` | repo |
| `build/spar-signal-feasibility.html` | The S5 vacancy feasibility test write-up | see `dist/build/` | repo |
| `build/model_section.html` | Partial markup embedded into the dashboard build | — | repo |
| `build/eco_theme.css` | Shared light-theme tokens for the map and overview pages | — | repo |
| `build/spar-id-eco.svg`, `spar-id-bridge.svg`, `spar-id-policy.svg`, `spar-id-ecosystem-map.svg` | The SVG sources behind the ecosystem page | — | repo |
| `dist/index.html`, `dist/build/*` | Generated output — **never hand-edit**; what Cloudflare Pages serves | `spar-f26-id.pages.dev` (dashboard is gated, HTTP 401) | generated |

### F. Build scripts

| Script | What it does |
|---|---|
| `build/build_dashboard.py` | `data/*.csv` → `dist/index.html` (the gated dashboard) |
| `build/build_overview.py` | `data/id-postings/postings-*.csv` + `data/kemnaker/*.csv` → `build/spar-id-overview.html` (stdlib only) |
| `build/build_ecosystem_map.py` | `data/ecosystem-id-*.json` → `build/spar-id-ecosystem-map.html` + SVGs |
| `build/build_postings_report.py` | `postings-*.csv` + `summary.json` → `build/spar-id-postings.html` |
| `build/prep_postings.py` | Raw scrape → normalised, year-sharded CSVs (calls `ai_classify`) |
| `build/ai_classify.py` | The AI/data/digital-basic requirement classifier |
| `build/verify_postings.py` | Re-fetches a sample of rows and writes `verification.json` |
| `build/sync_sheets.py` | GSheets → `data/*.csv` (the hourly job; **needs creds**) |
| `build/check_parity.py` | Read-only diff: does the sheet still agree with `data/*.csv`, row for row? |
| `build/seed_sheet.py` | One-off seeding of the six tabs from `data/seed/` |
| `deploy.sh` | Build + `wrangler pages deploy` |
| `tools/scrape_karirhub.py` | Standalone, robots-aware scraper that writes the team schema |
| `functions/_middleware.js` | Access gate: dashboard gated, `/build/*` public |

### G. Task and continuity notes

| File | What it is |
|---|---|
| `SPAR_Fall2026_Shafira_Tasks.md` | Shafira's task card extracted from the six-week plan deck (roles, deliverables, dates) |
| `build/CTO-HANDOFF.md` | CRO → CTO handoff: open items, decisions left open |
| `.github/workflows/sync.yml` | Hourly sheet → repo sync (+ Apps Script dispatch) |
| `.github/workflows/deploy.yml` | Build + Cloudflare Pages deploy (runs only on push to `main`) |

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
| Tracker (India team progress) | Sheet `1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ` | the team |
| Register / skeleton / trackers | see "The sheets" below | the team |
| Audit trail | this repo, `data/*.csv` | the sync job |
| Team view | Cloudflare Pages (dashboard) | nobody — read-only, **gated** |
| Public view | Cloudflare Pages `/build/*` | nobody — read-only, **public** |

**Nothing writes back to Google Drive or Google Sheets.** This is a one-way mirror.

## The sheets

`data/sheets.json` maps a **tab name** to an output CSV; the Sheets API is used by tab name, so the
"CSV export only returns the first tab" gotcha does not apply.

| Sheet | ID | Tab(s) | What is in it |
|---|---|---|---|
| Core file — the register | `1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k` | `signals` (gid `838965401`), `triggers`, `Indonesia policy inventory`, `readiness`, `who-can-act`, `instruments` | 22 Indonesia signal rows; each policy document; the six readiness questions |
| SPAR signals skeleton (team) | `1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo` | `README`, `SIGNALS`, `(dani notes)`, `LOG` | S1–S10 signal definitions in three layers; the observation log |
| IND team progress | `1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ` | `Sheet1` | Every Indonesia deliverable with progress, status, PIC |

**Columns added 24 Nov (previously empty — revert ranges in `docs/SHEET-WRITE-2026-11-24.md`):**

| Sheet → tab | New columns | Contents |
|---|---|---|
| Core file → `signals` | `O`–`T` | `link` · `source_verbatim` · `confidence` · `data_status` · `not_verified` · `source_checked` |
| Skeleton → `SIGNALS` | `H`–`K` | Indonesian evidence · public source · status · gap/route |
| IND team progress → `Sheet1` | `G` | `Comments` — one line per task, plain language |

**Edit rules (all tabs):** header row is row 1 · `id` is the upsert and join key, never rename or
reorder · no merged cells, no blank spacer rows · one document per row · dates `YYYY-MM-DD` ·
`link` = the public source, not a Drive link · public sources only, no personal data · never rename a
header without telling CTO. Demo rows are marked `verified_by=DEMO`.

## Sync visibility — who changed what

Every sync run appends to `data/SYNC-LOG.md` (newest first): timestamp, source, editor when known, and
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
| `https://spar-f26-id.pages.dev/` | 401 — gated dashboard (expected) |
| `https://spar-f26-id.pages.dev/build/spar-id-postings` | 200 — public |
| `https://spar-f26-id.pages.dev/build/spar-id-ecosystem-map` | 200 — public |

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

> Tallied 2026-11-24 from the Core file `signals` tab (22 rows), the Perplexity verification run,
> Kemnaker's own portal counts, `IND team progress` and repo state. Supersedes the 2026-11-10 tally.
> **On PR #15 — not yet merged into main.**

```
Data spine        ████████████████████░░░░  88%  22 signal rows; OJK/Kemnaker/Pasker sources located; portal counts downloaded
Data list (lead)  ██████████████████████░░  92%  public source URL + verbatim + H/M/L on all 22 rows; 5 statuses corrected; unverified named
Part 3 (signals)  ██████████████░░░░░░░░░░  70%  678-word draft written from the sourced base; needs Shafira's read-through, not a rewrite
Part 4 (policy)   ██████░░░░░░░░░░░░░░░░░░  25%  who-can-act map + request routes ready; 600w with Ian pending (assembly, not discovery)
Shared sheet/repo ████████████████░░░░░░░░  75%  sheet ahead of repo; hourly sync failing, so the 29 Nov freeze is blocked
Section 5 (SPAR)  ██░░░░░░░░░░░░░░░░░░░░░░  10%  2,500w Indonesia chapter; data underpinning ready
Section 8 (Limits)█░░░░░░░░░░░░░░░░░░░░░░░   5%  not started (with Napat, Wed 2 Dec)
Interview (BPS)   ████░░░░░░░░░░░░░░░░░░░░  20%  question reframed as a data-availability enquiry; candidate question found (see the emp.csv flag)
Atlas site        ██████████░░░░░░░░░░░░░░  45%  ecosystem map + postings report live; overview/scenarios page built, deploy blocked
```

**Evidence behind the bars:** Core file `signals` — 22 rows · `triggers` 1 · `who-can-act` 6 ·
policy inventory 3 · readiness 3 (all `tbc`) · instruments 1 (DEMO) · postings 2,618 rows (2024→Oct
2026) · Kemnaker portal counts 2022–24 in `data/kemnaker/` · `docs/ID-SIGNAL-SOURCE-MATRIX.md`,
`docs/ID-PART3-DRAFT.md`, `docs/ID-READINESS-WORKSHEET.md`, `docs/ID-PENDING-24NOV.md`.

**Next due:** Sun 22 Nov (Part 3 + Part 4 — Part 3 drafted; Part 4 with Ian) → Sun 29 Nov (sheet
frozen into the repo) → Wed 2 Dec (§5 + §8 to Rachel). SPAR submission 14 Dec; Demo Day 19 Dec.

## Open items and blockers

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Hourly sheet → repo sync failing at its commit step | CTO / `@misshanna_bot` | The 29 Nov freeze; every `data/*.csv` consumer |
| 2 | Cloudflare Pages deploy auth failure (code 10000) | CTO / `@misshanna_bot` | Every new page going live |
| 3 | Readiness scoring — 3 documents × 6 questions | Shafira | Needs the six question texts (not recorded anywhere; the tab holds only `q1`–`q6`) |
| 4 | Regulator-facing requests: 15 routes surfaced to BPJS, OJK, Kemnaker, BPS, DPR Commission IX, plus a scope question on platform data obtained via web archives | **@clo before anything is sent** | Nothing sent to date |
| 5 | `data/id-signals.csv` etc. mirror stale vs the sheets | sync job (#1) | Dashboard accuracy |

## BoxCompute collection (24 Nov 2026)

**Why BoxCompute.** The lane's posting evidence currently rests on one government portal plus a
sampled archive (2,618 rows). The v2 brief (`docs/PROMPTS-BOXCOMPUTE-V2.md`) moves to an
**archive-first** design across 13 platforms, because that is both the ToS-clean route to volume and
the only route that reaches a platform's own published scale.

**Target (v2 brief, Step 1).** Per platform: `distinct posting URLs` by year, plus a coverage probe —
*counts first, no fetching until the counts exist*. Q1, honestly asked: **how much is actually
archived?** Until that is answered, any collection number is a guess.

**Collection runs in a BoxCompute sandbox, driven by the CLI** (`bxc sandbox exec`), not through the
web chat: the chat surface is not exposed by the CLI, SDK or REST API, and a scripted sandbox puts
results in the repo as artefacts instead of chat prose.

Artefacts produced by the run live under `data/boxcompute/`:

| File | What |
|---|---|
| `census.json` | per platform: CDX page probe, distinct URLs per year, and the scoped CDX target |
| `url_shapes/<host>.txt` | sampled distinct URLs — used to **derive** posting-pattern filters from evidence rather than guessing them |
| `census.log` | full request log, including every backoff |

**Method, and its limits.** Wayback CDX only: `collapsed=urlkey`, `statuscode:200`, one request every
3 s, backoff on 429/503/504, and a User-Agent that identifies the crawler as an academic study.
Three cautions are part of the result, not footnotes:

- **Distinct URLs ≠ postings ≠ hires.** A URL can be one ad or one search page; CDX volume is a
  property of the crawl, not of hiring. No figure from this run may be read as a level of demand.
- **CDX page counts are a volume probe only.** An assumed page size would be an invented figure, so
  the raw page count is reported and nothing is extrapolated from it.
- **Some hosts are too large for a single CDX response.** Piercing `jobstreet.co.id` and
  `linkedin.com` needs monthly pagination; where a host is skipped or throttled the table says so.

**Access is not the constraint.** From the sandbox: Wayback CDX **200**, Common Crawl index **200**,
Karirhub live **200**, Pasker ID **200**. By contrast Algolia (`algolia.kemnaker.go.id`, the
`L3WWP72HSI` shard) is **unreachable from both the sandbox and the agent network**, and Glints /
LinkedIn / JobStreet direct requests return **403/403/308**. The archive-first design is therefore
not a preference — it is the only route that works and the only one that respects the platforms.

---

## Non-negotiables

- **Consent gate.** Anything shown *publicly* needs AISA's consent first. Default private; the
  dashboard stays behind the access gate, and public reports are published only after sign-off.
- **No personal data.** See `data/PERSONAL-DATA-STOP.md`. Aggregates and totals/shares only — never
  raw individual ads — in anything shared beyond the team.
- **Framing.** This grades *documents*, never a government. No ranking, no scoring of institutions.
  Statements are "consistent with AI-driven change", never "caused by AI".
- **Never fabricate.** Unverified figures stay marked `[unverified — confirm]` or "not verified".
- **Light theme only** in any deliverable UI.
- **Not a CMS.** No write-back to Drive or Sheets.
