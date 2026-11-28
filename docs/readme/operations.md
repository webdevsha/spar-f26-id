# Running it — build, deploy, URLs, secrets

The commands, the live URLs, and what must never enter the repo.

---

[← Back to the README index](../../README.md)

---

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

## Live URLs (re-verified 28 Nov 2026)

`app/` is the public face: `app/index.html` is deployed as the site root.

| URL | Status |
|---|---|
| [https://spar-f26-id.pages.dev/](https://spar-f26-id.pages.dev) | 401 — gated home (`app/index.html`, bank AI-shock scenarios) |
| [https://spar-f26-id.pages.dev/atlas.html](https://spar-f26-id.pages.dev/atlas.html) | 401 — gated (`app/atlas.html`, ecosystem and readiness atlas) |
| [https://spar-f26-id.pages.dev/dashboard.html](https://spar-f26-id.pages.dev/dashboard.html) | 401 — gated (generated policy-readiness dashboard) |
| [https://spar-f26-id.pages.dev/build/spar-id-postings](https://spar-f26-id.pages.dev/build/spar-id-postings) | 200 — public |
| [https://spar-f26-id.pages.dev/build/spar-id-ecosystem-map](https://spar-f26-id.pages.dev/build/spar-id-ecosystem-map) | 200 — public |

> **Deploy works.** Verified 28 Nov 2026: `wrangler pages deploy` uploaded 30 files, uploaded the
> Functions bundle (so the access gate shipped), and published deployment `6bf9dacb`. The previous
> "error code 10000, last success 22 Oct" note was stale and is retracted — the token in
> `~/.hermes/.env` authenticates fine. `./deploy.sh` is the tested path:
> it builds the dashboard, moves it to `dist/dashboard.html`, then copies `app/` over the root.

## Secrets (never in this repo)

| Secret | Where | What |
|---|---|---|
| `SITE_PASSWORD` | Cloudflare Pages project secret | access-gate password (dashboard only; `/build/*` is public) |
| `SHEET_ID` | GitHub repo secret | the Google Sheet's ID |
| `GOOGLE_SERVICE_ACCOUNT` | GitHub repo secret | read-only service-account JSON |
| `SYNC_PAT` | GitHub repo secret | PAT used by the sync job to push past the Main-rule code-scanning gate |
| `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID` | GitHub repo secrets + `~/.hermes/.env` locally | Pages deploy — **working as of 28 Nov 2026** |

```bash
wrangler pages secret put SITE_PASSWORD --project-name spar-f26-id
```

---
