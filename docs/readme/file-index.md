# File index — everything we actually work on

Every path that is actually edited, grouped by function, with the reason each one exists.

---

[← Back to the README index](../../README.md)

---

## File index — everything we actually work on

**Status key:** `live` = published and reachable · `repo` = tracked here · `local` = built but not
deployed · `blocked` = waiting on infrastructure · `superseded` = kept for provenance only.

### A. Analysis, evidence and writing (`docs/`)

| File | What it is | Owner | Status |
|---|---|---|---|
| [ID-PENDING-24NOV.md](../../docs/ID-PENDING-24NOV.md) | The open/closed task ledger, with what "done" looks like per item | Shafira (ID lane) | repo |
| [ID-SIGNAL-SOURCE-MATRIX.md](../../docs/ID-SIGNAL-SOURCE-MATRIX.md) | Source matrix v2 — the 22-row verified source line, 5 status corrections, 2 attribution traps, 3 denominator traps | Shafira + CRO | repo |
| [ID-PART3-DRAFT.md](../../docs/ID-PART3-DRAFT.md) | Country Report Part 3 draft, 678 words, every figure traced; unverified figures left bracketed | Shafira | repo |
| [ID-PART4-DRAFT.md](../../docs/ID-PART4-DRAFT.md) | Country Report Part 4 v1 — who can act and the policies in place, reframed to the AI shock question: each instrument carries its verdict, three flags for Ian, word count stated honestly | Shafira + Ian | repo |
| [ID-PART8-LIMITS-DRAFT.md](../../docs/ID-PART8-LIMITS-DRAFT.md) | Report section 8 — limits, stated on the record | Shafira + Napat | repo |
| [ID-POLICY-SITE-PROPOSAL.md](../../docs/ID-POLICY-SITE-PROPOSAL.md) | **The design proposal** — ten patterns from the Windfall scenarios site that work for a policy reader, what we must not copy, the seven-route product, the two evidenceable scenario axes, the evidence grammar, the build plan and the five gates | CRO for Shafira | repo |
| [ID-CALL-RUNSHEET-26NOV.md](../../docs/ID-CALL-RUNSHEET-26NOV.md) | One-page run sheet for the SPAR call: six do-now items, six raise-on-call items, the numbers to have at hand, the two decisions needed | CRO for Shafira | repo |
| [ID-READINESS-WORKSHEET.md](../../docs/ID-READINESS-WORKSHEET.md) | 3 policy documents × 6 readiness questions, pre-loaded with the evidence each question answers from | Shafira | repo (untracked) |
| [ID-HANDOFF-HANNACHAN.md](../../docs/ID-HANDOFF-HANNACHAN.md) | Continuity handoff: truth map, boundaries, blockers, order of work | CRO | repo (untracked) |
| [ID-SIGNALS-PERPLEXITY-PACK.md](../../docs/ID-SIGNALS-PERPLEXITY-PACK.md) | The verification brief sent to Perplexity (blocks A–E, rules, output contract) | CRO | repo |
| [PROMPTS-PERPLEXITY-BOXCOMPUTE.md](../../docs/PROMPTS-PERPLEXITY-BOXCOMPUTE.md) | Copy-paste prompt set: Perplexity verification (P1, P2) and the first BoxCompute collection brief (B1–B3) | CRO | repo |
| [PROMPTS-BOXCOMPUTE-V2.md](../../docs/PROMPTS-BOXCOMPUTE-V2.md) | **Current** collection brief — archive-first, three record kinds, 34-field schema, comparability gate (supersedes B1–B3) | CRO | repo |
| [SCRAPING-WITH-BOXCOMPUTE.md](../../docs/SCRAPING-WITH-BOXCOMPUTE.md) | Plain-English guide to scraping with BoxCompute, using this Indonesia run as the worked example | CRO | repo |
| [SHEET-WRITE-2026-11-24.md](../../docs/SHEET-WRITE-2026-11-24.md) | Audit + revert instructions for every shared-sheet write, 24–26 Nov (Core file `signals` O–T, skeleton `SIGNALS` H–K, `SIGNALS_ID` E–J + highlighting, `IND team progress` G, `SIGNALS` J) | CRO | repo |
| [MODEL-INDONESIA.md](../../docs/MODEL-INDONESIA.md) | How the scenario model maps onto Indonesia: what the data identifies, what must be calibrated | CRO + Natraj | repo |
| [back-up-research.md](../../docs/back-up-research.md) | Evidence notes behind the six measures M1–M6, with sources per indicator | CRO | repo |
| [apps-script-trigger.gs](../../docs/apps-script-trigger.gs) | Apps Script `onChange` hook → `repository_dispatch`, so a sheet edit reaches the repo in seconds | CTO | repo |

### B. Signal register and registers data (`data/`)

| File | What it is | Owner | Status |
|---|---|---|---|
| [id-signals.csv](../../data/id-signals.csv) | Mirror of the register's `signals` tab — **currently stale**: repo holds 9 rows, the sheet holds 22 | sync job | repo (stale) |
| [id-policy-inventory.csv](../../data/id-policy-inventory.csv) | Policy inventory: 3 documents (OJK AI guide, JKP, Pasker ID) | team | repo |
| [id-readiness.csv](../../data/id-readiness.csv) | Readiness scoring join — all `q1`–`q6` still `tbc` | Shafira | repo (open) |
| [id-who-can-act.csv](../../data/id-who-can-act.csv) | The who-can-act map: 6 organisations with proposed doors | Shafira + Rachel | repo |
| [id-instruments.csv](../../data/id-instruments.csv) | Instrument map — **DEMO row only**, needs real rows | team | repo (open) |
| [id-triggers.csv](../../data/id-triggers.csv) | Trigger card(s) — one row so far | Akbar | repo |
| [sheets.json](../../data/sheets.json) | Tab name → output CSV map used by the sync | CTO | repo |
| [SYNC-LOG.md](../../data/SYNC-LOG.md) | Append-only record of every sync run: editors, `+added / −removed`, changed `id`s | sync job | repo |
| [PERSONAL-DATA-STOP.md](../../data/PERSONAL-DATA-STOP.md) | The no-personal-data rule and what it means row by row | CRO | repo |
| [ecosystem-id-map.json](../../data/ecosystem-id-map.json), [ecosystem-id-domains.json](../../data/ecosystem-id-domains.json) | The Indonesia ecosystem & policy map (actors, instruments, support routes) that renders as a public page. **`views.policy.nodes` is now generated** from the register by [build/sync_map_from_register.py](../../build/sync_map_from_register.py) (22 nodes: 8 hand-written kept, 8 added, 6 levers); bands, edges, marks and `responsibility` stay hand-curated | Shafira + Rachel | repo |
| [ecosystem-ph-v0.json](../../data/ecosystem-ph-v0.json) | Philippines ecosystem stub — kept in this repo for parity; PH lane owns the content | BG | repo |
| [model-id-demo.json](../../data/model-id-demo.json) | Inputs for the interactive model demo | CRO + Natraj | repo |
| `seed/*.tsv` | Original seed rows used to create the sheet tabs | CTO | superseded |

### C. The postings dataset (`data/id-postings/`)

| File | What it is | Owner | Status |
|---|---|---|---|
| [postings-2024.csv](../../data/id-postings/postings-2024.csv) (1.4 MB) · [postings-2025.csv](../../data/id-postings/postings-2025.csv) (1.8 MB) · [postings-2026.csv](../../data/id-postings/postings-2026.csv) (0.4 MB) | 2,618 archived Indonesian finance/BPO postings, 2024-02 → 2026-10, one row per posting, 37 columns | Shafira | repo |
| [README.md](../../README.md) | Schema, provenance, ethics, coverage limits for the dataset | Shafira + CRO | repo |
| [summary.json](../../data/id-postings/summary.json) | Counts used by the report builder (sectors, months, AI tiers, provinces) | build | repo |
| [verification.json](../../data/id-postings/verification.json) | Per-row re-fetch results (411 of 2,618 checked) | build | repo |
| [karirhub-id-postings-sample.csv](../../data/id-postings/karirhub-id-postings-sample.csv) | The original 331-row sample from the first successful scrape | CRO | repo |
| [perplexity-id-data.md](../../data/id-postings/perplexity-id-data.md) | The verification run: 22 rows, 5 priority figures, request routes, contradictions | Shafira (run) | repo |

### D. Kemnaker's own portal counts (`data/kemnaker/` and `build/`)

These are the **portal's own advertised totals** — the weights any posting sample must be calibrated
to. All four are public CSV downloads from `paskerid.kemnaker.go.id/documents/`, no gate.

| File | What it is | Status |
|---|---|---|
| [data/kemnaker/Lowongan_Kerja_Menurut_Kategori_Lapangan_Usaha_Tahun_2022-2024.csv](../../data/kemnaker/Lowongan_Kerja_Menurut_Kategori_Lapangan_Usaha_Tahun_2022-2024.csv) | Postings and advertised slots by industry (KBLI 1-digit), 2022–24. Finance & insurance: **1,195 → 797 → 726** | repo |
| [data/kemnaker/Lowongan_Kerja_di_Karirhub_Menurut_Golongan_Pokok_Jabatan_Tahun_2022-2024.csv](../../data/kemnaker/Lowongan_Kerja_di_Karirhub_Menurut_Golongan_Pokok_Jabatan_Tahun_2022-2024.csv) | The same by occupation group (KBJI). Clerical (group 4): 1,751 → 3,341 → 2,034 | repo |
| [build/sector.csv](../../build/sector.csv) | Byte-identical copy of the industry file — **duplicate, should move to `data/kemnaker/`** | repo (duplicate) |
| [build/occ.csv](../../build/occ.csv) | Duplicate of the occupation file | repo (duplicate) |
| [build/emp.csv](../../build/emp.csv) | **Postings by experience requirement, 2022–24.** `0-1 tahun`: 1,833 → 1,807 → **2**. See the flag below — do not plot this as a trend without checking with Kemnaker | repo |
| [build/prov.csv](../../build/prov.csv) | Employers posting by province: national 2,483 → 2,730 → 2,644; DKI Jakarta 389 → 492 → 576 | repo |

> **Flag on [emp.csv](../../build/emp.csv).** The portal's own `0-1 tahun` (entry-level) postings fall from 1,807 in 2023 to
> **2** in 2024, while `tidak ada informasi` (not stated) absorbs 5,126. A collapse that extreme is far
> more likely a change in how the portal captured the field than a collapse in entry-level hiring — our
> own ad sample shows entry-level wording in roughly one in ten finance/BPO ads. **Treat it as a
> data-capture question for Kemnaker, not as a finding.** It is a strong candidate for the one
> interview question the plan asks for.

### E. Pages and reports (`build/`, deployed via `dist/`)

| File | What it is | Live URL | Status |
|---|---|---|---|
| [build/spar-id-postings.html](../../build/spar-id-postings.html) | Individual-postings report: method, refusals, coverage, AI-skill table, filterable posting table | [`/build/spar-id-postings`](https://spar-f26-id.pages.dev/build/spar-id-postings) | **live** |
| [build/spar-id-ecosystem-map.html](../../build/spar-id-ecosystem-map.html) | Ecosystem, policy and bridge maps (~210 KB, SVG-driven) | [`/build/spar-id-ecosystem-map`](https://spar-f26-id.pages.dev/build/spar-id-ecosystem-map) | **live** |
| [build/spar-id-overview.html](../../build/spar-id-overview.html) | Overview + 7 highlights + 4 policy scenarios + portal counts + exposure scores | — | **local** (deploy blocked) |
| [build/spar-id-model-demo.html](../../build/spar-id-model-demo.html) | Interactive scenario-model demo (current-data vs with-more-data) | see `dist/build/` | repo |
| [build/spar-signal-feasibility.html](../../build/spar-signal-feasibility.html) | The S5 vacancy feasibility test write-up | see `dist/build/` | repo |
| [build/model_section.html](../../build/model_section.html) | Partial markup embedded into the dashboard build | — | repo |
| [build/proposal-wireframe.html](../../build/proposal-wireframe.html) | The one-page light-theme wireframe for the proposed report site — hero, four findings tiered, the 2×2 with its undrawn quadrant, the outlook strip and the compare strip. Uses only figures already verified in the register; unsigned scenario bands print `bracket pending` | — | repo (not deployed) |
| [build/eco_theme.css](../../build/eco_theme.css) | Shared light-theme tokens for the map and overview pages | — | repo |
| [build/spar-id-eco.svg](../../build/spar-id-eco.svg), [spar-id-bridge.svg](../../build/spar-id-bridge.svg), [spar-id-policy.svg](../../build/spar-id-policy.svg), [spar-id-ecosystem-map.svg](../../build/spar-id-ecosystem-map.svg) | The SVG sources behind the ecosystem page | — | repo |
| [dist/index.html](../../dist/index.html), `dist/build/*` | Generated output — **never hand-edit**; what Cloudflare Pages serves | [spar-f26-id.pages.dev](https://spar-f26-id.pages.dev) (dashboard is gated, HTTP 401) | generated |

### F. Build scripts

| Script | What it does |
|---|---|
| [build/build_dashboard.py](../../build/build_dashboard.py) | `data/*.csv` → [dist/index.html](../../dist/index.html) (the gated dashboard) |
| [build/build_overview.py](../../build/build_overview.py) | `data/id-postings/postings-*.csv` + `data/kemnaker/*.csv` → [build/spar-id-overview.html](../../build/spar-id-overview.html) (stdlib only) |
| [build/build_ecosystem_map.py](../../build/build_ecosystem_map.py) | `data/ecosystem-id-*.json` → [build/spar-id-ecosystem-map.html](../../build/spar-id-ecosystem-map.html) + SVGs |
| [build/build_postings_report.py](../../build/build_postings_report.py) | `postings-*.csv` + [summary.json](../../data/id-postings/summary.json) → [build/spar-id-postings.html](../../build/spar-id-postings.html) |
| [build/prep_postings.py](../../build/prep_postings.py) | Raw scrape → normalised, year-sharded CSVs (calls `ai_classify`) |
| [build/ai_classify.py](../../build/ai_classify.py) | The AI/data/digital-basic requirement classifier |
| [build/verify_postings.py](../../build/verify_postings.py) | Re-fetches a sample of rows and writes [verification.json](../../data/id-postings/verification.json) |
| [build/sync_sheets.py](../../build/sync_sheets.py) | GSheets → `data/*.csv` (the hourly job; **needs creds**) |
| [build/check_parity.py](../../build/check_parity.py) | Read-only diff: does the sheet still agree with `data/*.csv`, row for row? |
| [build/sync_map_from_register.py](../../build/sync_map_from_register.py) | `--check` (default) prints the drift between the register and the ecosystem map; `--write` rebuilds the map's **policy nodes** from `id-policy-inventory.csv` + `id-instruments.csv`. Keeps hand-written node detail; never touches bands, edges, marks or the responsibility map |
| [build/seed_sheet.py](../../build/seed_sheet.py) | One-off seeding of the six tabs from `data/seed/` |
| [deploy.sh](../../deploy.sh) | Build + `wrangler pages deploy` |
| [tools/scrape_karirhub.py](../../tools/scrape_karirhub.py) | Standalone, robots-aware scraper that writes the team schema |
| [functions/_middleware.js](../../functions/_middleware.js) | Access gate: dashboard gated, `/build/*` public |

### G. Task and continuity notes

| File | What it is |
|---|---|
| [SPAR_Fall2026_Shafira_Tasks.md](../../SPAR_Fall2026_Shafira_Tasks.md) | Shafira's task card extracted from the six-week plan deck (roles, deliverables, dates) |
| [build/CTO-HANDOFF.md](../../build/CTO-HANDOFF.md) | CRO → CTO handoff: open items, decisions left open |
| [.github/workflows/sync.yml](../../.github/workflows/sync.yml) | Hourly sheet → repo sync (+ Apps Script dispatch) |
| [.github/workflows/deploy.yml](../../.github/workflows/deploy.yml) | Build + Cloudflare Pages deploy (runs only on push to `main`) |

---
