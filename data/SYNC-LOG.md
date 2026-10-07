# Sync log — Google Sheet -> repo

Newest first. Auto-written by `build/sync_sheets.py`.

## 2026-10-07 — sheet reconciled with the repo
_by: CTO (one-off, not an edit)_

- Sheet was carrying the original 8 demo rows while the repo held the real rows curated from
  Akbar's deck. The repo's data was pushed **up** into the sheet so the sheet is the source of
  truth again, and the hourly cron was re-enabled.
- `Indonesia policy inventory`: 8 demo rows -> 3 real rows
- `readiness`: 8 -> 3
- `signals`: 0 -> 9 · `triggers`: 0 -> 1 · `who-can-act`: 0 -> 6 · `instruments`: 0 -> 1
