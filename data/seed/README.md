# seed/ — paste-ready rows for the Google Sheet

**Generated. Do not hand-edit.** Re-run `python3 build/seed_sheet.py` after any
change to `data/*.csv`; these files are mirrored from the CSVs so the Sheet and
the repo cannot drift.

## Why these exist

The hourly `sync.yml` action reads the Google Sheet and **overwrites `data/*.csv`
with whatever the Sheet contains**. So the Sheet must be seeded with the current
CSVs first — otherwise the next sync reverts the repo to the older Sheet contents.

## How to seed (once, per tab)

1. Open the tracker Sheet (the one whose ID is in the `SHEET_ID` repo secret).
2. Create one tab per name in `data/sheets.json` — exact names, including
   `Indonesia policy inventory` (capital I, spaces, no trailing space):

   | Tab name | Seed file |
   |---|---|
   | `Indonesia policy inventory` | `id-policy-inventory.tsv` |
   | `readiness` | `id-readiness.tsv` |
   | `signals` | `id-signals.tsv` |
   | `triggers` | `id-triggers.tsv` |
   | `who-can-act` | `id-who-can-act.tsv` |
   | `instruments` | `id-instruments.tsv` |

3. Open the `.tsv`, select all, copy. In the Sheet click cell **A1** of that tab
   and paste — Sheets splits on tabs automatically.
4. Confirm row 1 is the header and the first column is `id` on every tab.

## Rules (from the repo README, repeated because they break the sync)

- No merged cells · no blank/spacer rows · header only on row 1.
- One document per row · dates `YYYY-MM-DD`.
- Never rename a header without telling CTO — the sync maps by header name.
- `id` is the upsert/join key. Never rename or reorder it.

## Order matters

Seed **before** the next `:17` hourly run, or between two runs. If a sync lands
first, re-run the seed — the CSVs in git are the source of truth and are
recoverable: `git checkout data/`.

## Contents right now

| Tab | Data rows | Note |
|---|---|---|
| `Indonesia policy inventory` | 3 | all real, sourced from Akbar's Indonesia.pdf |
| `readiness` | 3 | six questions all `tbc` — scoring is the 26 Oct deliverable |
| `signals` | 9 | 4 datasets + 1 stated gap + 4 baselines (Akbar deck) |
| `who-can-act` | 6 | BPS, OJK, Kemnaker, BPJS, PERBANAS, ILO (Akbar deck p3) |
| `triggers` | 1 | **DEMO placeholder** — tab is empty |
| `instruments` | 1 | **DEMO placeholder** — tab is empty |
