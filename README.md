# spar-f26-id

**Technical spine of the SPAR Fall 2026 *Indonesia* lane** — the data and
deployment infrastructure behind the lane's AI-and-labour-market work.

This repository is not a document. It is the *machine* that turns the team's
spreadsheet edits into a versioned, auditable, and (where consented) public
evidence base. The analysis and narrative live in the shared deck and the
Google Sheets tracker; this repo keeps that work **reproducible, diffable, and
shippable** without anyone hand-coding a webpage or re-exporting a CSV.

---

## What this repo is for

The Indonesia lane produces three named end results (they are the
"end results" cards on the dashboard itself). This repository is built to
serve **all three from a single source of truth**:

| Workstream | The output it produces | How this repo serves it |
|---|---|---|
| **Research work** | **Country reports** — the country write-up: what is at stake, moves to start now, triggers for when signals move. Backed by the versioned policy-inventory, readiness-scoring and signal datasets | GSheets → tracked CSV → a build that renders the whole evidence base as a filterable dashboard; every edit is a git commit, so the research record is inherently versioned and auditable |
| **Policy advocacy** | **Notes for officials** — the two-page brief an official can read (what is at stake, moves to start now, triggers). Point a regulator at a gated URL instead of emailing a slide | The dashboard *is* the advocacy artefact: OJK, Kemnaker, BPJS, PERBANAS can be walked through the same data the brief is drawn from, and every figure traces back to source |
| **Public engagement** *(the "public dynamic" — the lane's **Ecosystem & policy map**, published as an annex on AISA's SEA **Observatory**)* | A public, living view of Indonesia's AI-in-labour ecosystem — e.g. the individual-postings report now live at `/build/spar-id-postings.html` | Cloudflare Pages ships the public report while the main dashboard stays access-gated; the consent gate (below) keeps "team-only" and "public" as a one-line switch, not a rebuild |

> **Term note:** "public dynamic" in the brief is the lane's *Ecosystem & policy
> map*, which becomes an annex on AISA's SEA **Observatory** — the live,
> externally shareable face of the work. Rendered here as *public engagement*.
> Swap the label if your house style prefers "dissemination" or "public
> communication."

The three outputs are not separate codebases. They are **three views of one
versioned dataset**, which is exactly why a single repo beats three
spreadsheets-and-a-Deck: the country report, the official brief, and the
public Observatory can never drift apart, because they are compiled from the
same source. The repo also keeps the *evidence base* they all draw on —
the policy inventory, the six readiness questions (`q1`–`q6`), and the
signal/who-can-act datasets — in a form that is diffable and auditable.

The three end results (from the dashboard config):

1. **Country reports** — Indonesia (Shafira, ours) · Philippines (BG · Danielle · Joshua). Drafts 29 Nov, full 4 Dec.
2. **Ecosystem & policy map** — the six-layer ecosystem map, co-owned with BG and Rachel; becomes an annex on AISA's SEA Observatory. Rows by 22 Nov.
3. **Notes for officials** — the two-page brief. Indonesia (Shafira · Akbar, ours) · Philippines (BG · Danielle). By 13 Dec.

---

## The pipeline

```text
GSheets (team edits) ──sync──▶ repo /data/*.csv ──build──▶ dist/index.html ──▶ Cloudflare Pages (gated dashboard)
Google Drive         ──walk──▶ spar-f26-drive-index.md ──▶ repo (audit trail)
build/*.html         ──copy──▶ dist/build/*            ──▶ Cloudflare Pages (PUBLIC reports, e.g. postings)
```

| Layer | Where | Who edits |
|---|---|---|
| Source of truth | Google Drive — folder `1WW-Af6uO5_k9MQeHpnbIqjqvyeHo0-el` | the team |
| Tracker | Google Sheets (see `data/sheets.json`) | the team |
| Audit trail | this repo, `data/*.csv` | the sync job |
| Team view | Cloudflare Pages `spar-f26-id` (dashboard) | nobody — read-only, **gated** |
| Public view | Cloudflare Pages `spar-f26-id` (`/build/*` reports) | nobody — read-only, **public** |

**Nothing writes back to Google Drive or Google Sheets.** This is a one-way
mirror: the team edits in familiar tools, the repo captures the result.

---

## Layout

```text
data/       synced CSVs (tracked, diffable) + sheets.json tab map
build/      build_dashboard.py (CSV → dist), sync_sheets.py (GSheets → CSV),
            prep_postings.py + build_postings_report.py (S5 hiring-signal report)
dist/       generated index.html + build/* reports — never hand-edit
functions/  _middleware.js — access gate: dashboard gated, /build/* public
.github/    sync.yml (hourly), deploy.yml (build + Pages deploy)
docs/       SCRAPING-WITH-BOXCOMPUTE.md, apps-script-trigger.gs
```

## The sheets

`data/sheets.json` maps a **tab name** to an output CSV. Tabs use the Sheets
API by name, so the "CSV export only returns the first tab" gotcha does not
apply here.

Tab `inventory` header row 1:

```text
id	document	short_name	type	owner_agency	covers	sectors	budget	budget_source	monitoring	monitoring_detail	effective_date	status	link	source_type	last_checked	verified_by	notes
```

Tab `readiness` (joined to `inventory` by `id`):

```text
id	document	q1	q2	q3	q4	q5	q6	score	blind_spot	notes
```

`id` is the upsert/join key — never rename or reorder it.

**Edit rules:** no merged cells · no blank/spacer rows · header only on row 1 ·
one document per row · dates `YYYY-MM-DD` · never rename a header without
telling CTO.

## Sync visibility — who changed what

Every sync run appends to **`data/SYNC-LOG.md`** (newest first): timestamp, source, the editor when
known, and per tab the `+added / −removed` counts with the actual changed `id`s. The dashboard renders
the newest entries in its **Recent changes** panel, and the commit message carries the editor.

Two ways a change reaches the repo:

| Trigger | Latency | Cost |
|---|---|---|
| Hourly cron (`17 * * * *`) | up to 60 min | negligible |
| Google Apps Script `onChange` -> `repository_dispatch` | seconds | none (fires only on real edits) |

To wire the real-time half, follow the setup block at the top of
**`docs/apps-script-trigger.gs`** — paste it into Extensions -> Apps Script, add a fine-grained
GitHub token (Actions: write, this repo only) to Script Properties, and add an `On change` trigger.

**Honest limit:** the service account can only read cell *values*, not authorship. So "who edited" is
only knowable via the Apps Script trigger (or the paid Drive Activity API). Scheduled runs log the
editor as unknown — that is expected, not a bug.

## Running it

```bash
python3 build/build_dashboard.py          # data/*.csv -> dist/index.html (+ dist/build/* reports)
./deploy.sh                               # build + wrangler pages deploy
python3 build/sync_sheets.py              # GSheets -> data/*.csv (needs creds)
```

## Secrets (never in this repo)

| Secret | Where | What |
|---|---|---|
| `SITE_PASSWORD` | Cloudflare Pages project secret | access-gate password (dashboard only; `/build/*` is public) |
| `SHEET_ID` | GitHub repo secret | the Google Sheet's ID |
| `GOOGLE_SERVICE_ACCOUNT` | GitHub repo secret | read-only service-account JSON |
| `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID` | GitHub repo secrets | Pages deploy |

Set the gate password with:

```bash
wrangler pages secret put SITE_PASSWORD --project-name spar-f26-id
```

## Individual postings test (S5 hiring signal)

The aggregate Kemnaker data answers "how many vacancies by occupation"; the team also asked for
**individual postings** with timestamps, locations, content and an AI-skill flag. First successful
pass, 2026-10-20:

| Artifact | What |
|---|---|
| `build/spar-id-postings.html` | visual report — method, refusals, coverage, AI-skill table, ethics marks, filterable posting table (**public** at `/build/spar-id-postings.html`) |
| `data/id-postings/postings-<year>.csv` | 2,618 rows (281 live + 2,337 archived), finance/BPO, 2024-02 → 2026-10, one CSV per year |
| `data/id-postings/README.md` | schema, provenance, ethics, limits |
| `build/prep_postings.py`, `build/build_postings_report.py` | CSV normaliser + report builder (stdlib only) |

All rows are **PUBLIC** (Karirhub posting pages + Internet Archive captures); no login, no API
key, no circumvention. The Algolia search backend is still unreachable from the build network —
the workaround is harvesting detail-page URLs and reading server-rendered posting pages.

### How to do it yourself

**[`docs/SCRAPING-WITH-BOXCOMPUTE.md`](docs/SCRAPING-WITH-BOXCOMPUTE.md)** — a plain-English guide to
scraping with BoxCompute, using this Indonesia run as the worked example: the five-step recipe, what
"blocked" looks like, the team's row format, the ethics checklist, troubleshooting and a glossary.
Runnable companion: `tools/scrape_karirhub.py` (stdlib only, robots-aware, writes the team schema).

## Shafira's task progress (SPAR Fall 2026)

> Tallied 2026-11-24 (evening) from the Core file `signals` tab (22 rows), the Perplexity
> verification run, Kemnaker's own portal counts, `IND team progress` and repo state.
> PR #15 (conflict-resolved against `main` after #14). Supersedes the 2026-11-10 and earlier-24-Nov tallies.

```
Data spine        ████████████████████░░░░  88%  22 signal rows; OJK/Kemnaker/Pasker sources located; portal counts downloaded
Data list (lead)  ██████████████████████░░  92%  public source URL + verbatim + H/M/L on all 22 rows; 5 statuses corrected; unverified named
Part 3 (signals)  ███████░░░░░░░░░░░░░░░░░  30%  evidence base complete and sourced; 700w narrative still to write (overdue since 22 Nov)
Part 4 (policy)   ██████░░░░░░░░░░░░░░░░░░  25%  who-can-act map now carries request routes, not just names; 600w with Ian pending
Shared sheet/repo ████████████████░░░░░░░░  75%  sheet ahead of repo; hourly sync still failing, so the 29 Nov freeze is blocked
Section 5 (SPAR)  ██░░░░░░░░░░░░░░░░░░░░░░  10%  2,500w Indonesia chapter; data underpinning ready
Section 8 (Limits)█░░░░░░░░░░░░░░░░░░░░░░░   5%  not started (with Napat, Wed 2 Dec)
Interview (BPS)   ████░░░░░░░░░░░░░░░░░░░░  20%  question reframed as a data-availability enquiry (Perplexity Block E); SPAR still confirming access
Atlas site        ██████████░░░░░░░░░░░░░░  45%  ecosystem map + postings report + new overview/scenarios page built; deployed 24 Nov and live (200)
```

**New evidence and artefacts behind the bars (2026-11-24):**
- Core file `signals` tab — **22 rows**, now with `link` · `source_verbatim` · `confidence` · `data_status` · `not_verified` (columns O–T, previously empty). Revert note: `docs/SHEET-WRITE-2026-11-24.md`.
- `SPAR_signals_skeleton` → `SIGNALS` — Indonesian evidence column added for all of S1–S10 (columns H–K).
- `data/id-postings/perplexity-id-data.md` — the verification run: 22 rows + 5-figure Block A + request routes + 8 contradictions/attribution traps.
- `docs/ID-SIGNAL-SOURCE-MATRIX.md` — **v2, Perplexity-grounded**: 5 status corrections, 2 attribution traps, 4 denominator traps, and what remains unverified.
- `data/kemnaker/*.csv` — Kemnaker's own portal counts, public downloads: finance & insurance **1,195 → 797 → 726** postings (2022–24); portal total 10,695 → 20,027 → 17,169.
- **Coverage check:** our finance/BPO rows for 2024 = **66** against the portal's own **726** → ≈ **9.1%** of the year's finance postings.
- `build/spar-id-overview.html` — overview + 7 highlights + 4 policy scenarios + portal counts + category exposure scores (285 of 512 in-scope rows scored, mean 0.541).
- `docs/PROMPTS-BOXCOMPUTE-V2.md` — archive-first collection brief aligned to the 1,059,854-posting archive study.
- `bright spot` — Part 3 is no longer blocked: the sourced evidence base it needs now exists.

**Blockers and flags (lanes: CTO / @misshanna_bot / @clo):**
1. `sync-sheets` still fails hourly at *Commit if changed* — repo CSV holds 9 signal rows against the tab's 22, so the dashboard reads stale data.
2. **Deploy is not broken** — verified 24 Nov: PR #14's merge fired `deploy-dashboard` (success, 21s) and `/build/spar-id-ecosystem-map`, `/build/spar-id-postings`, `/build/spar-id-model-demo` all return HTTP 200; the dashboard root correctly returns 401 (gate active). The earlier "auth code 10000 since 5 Nov" note did **not** reproduce (deploys also succeeded 18 Nov) and is removed. The real constraint: `deploy.yml` fires **only on push to `main`**, so this branch ships once it merges.
3. **@clo:** the verification surfaced 15 formal information requests to **BPJS, OJK, Kemnaker, BPS and DPR Commission IX**, and a scope question on platform data obtained via web archives (LinkedIn/JobStreet-class). Regulator-facing requests in the study's name need a compliance pass before any are sent. None have been sent.

**Next due from Shafira:** Sun 22 Nov (Part 3 + Part 4 — **overdue**) -> Sun 29 Nov (sheet frozen into the repo) -> Wed 2 Dec (§5 + §8 to Rachel). SPAR team meeting tonight 22:00 MYT.

---

## Non-negotiables

- **Consent gate.** Anything shown *publicly* (the `/build/*` Observatory reports) needs AISA
  consent first. Default private; the dashboard is behind the access gate until then, and public
  reports are published only after sign-off.
- **No personal data.** See `data/PERSONAL-DATA-STOP.md`.
- **Framing.** This grades *documents*, never a government. No ranking, no scoring.
- **Not a CMS.** No write-back to Drive or Sheets.
