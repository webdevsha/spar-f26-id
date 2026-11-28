# The pipeline

How a spreadsheet edit becomes a committed, deployed artefact.

---

[← Back to the README index](../../README.md)

---

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
