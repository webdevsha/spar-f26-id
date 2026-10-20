# spar-f26-id

Technical spine of the SPAR Fall 2026 **Indonesia** lane — the *Access* line of
the deck's logistics table (Drive, slide repo, tracker, Observatory).

Read-only dashboard over a versioned, diffable repo. **Nothing writes back to
Google Drive or Google Sheets.**

```
GSheets (team edits) ──sync──▶ repo /data/*.csv ──build──▶ dist/index.html ──▶ Cloudflare Pages
Google Drive         ──walk──▶ spar-f26-drive-index.md ──▶ repo (audit trail)
```

| Layer | Where | Who edits |
|---|---|---|
| Source of truth | Google Drive — folder `1WW-Af6uO5_k9MQeHpnbIqjqvyeHo0-el` | the team |
| Tracker | Google Sheets (see `data/sheets.json`) | the team |
| Audit trail | this repo, `data/*.csv` | the sync job |
| View | Cloudflare Pages `spar-f26-id` | nobody — read-only, gated |

## Layout

```
data/       synced CSVs (tracked, diffable) + sheets.json tab map
build/      build_dashboard.py (CSV → dist), sync_sheets.py (GSheets → CSV)
dist/       generated index.html — never hand-edit
functions/  _middleware.js — Basic Auth access gate (password = SITE_PASSWORD secret)
.github/    sync.yml (hourly), deploy.yml (build + Pages deploy)
```

## The sheets

`data/sheets.json` maps a **tab name** to an output CSV. Tabs use the Sheets
API by name, so the "CSV export only returns the first tab" gotcha does not
apply here.

Tab `inventory` header row 1:

```
id	document	short_name	type	owner_agency	covers	sectors	budget	budget_source	monitoring	monitoring_detail	effective_date	status	link	source_type	last_checked	verified_by	notes
```

Tab `readiness` (joined to `inventory` by `id`):

```
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
python3 build/build_dashboard.py          # data/*.csv -> dist/index.html
./deploy.sh                               # build + wrangler pages deploy
python3 build/sync_sheets.py              # GSheets -> data/*.csv (needs creds)
```

## Secrets (never in this repo)

| Secret | Where | What |
|---|---|---|
| `SITE_PASSWORD` | Cloudflare Pages project secret | access-gate password |
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
| `build/spar-id-postings.html` | visual report — method, refusals, coverage, AI-skill table, ethics marks, filterable posting table |
| `data/id-postings/karirhub-id-postings-sample.csv` | 331 rows (281 live + 50 archived), finance/BPO, 2025-10-20 → 2026-10-20 |
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

## Non-negotiables

- **Consent gate.** Anything shown outside the team needs AISA consent first.
  Default private; the Pages URL is behind the access gate until then.
- **No personal data.** See `data/PERSONAL-DATA-STOP.md`.
- **Framing.** This grades *documents*, never a government. No ranking, no scoring.
- **Not a CMS.** No write-back to Drive or Sheets.