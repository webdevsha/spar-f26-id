# CTO handoff — spar-f26-id (2026-10-07)

From CRO. Two open items. Both are **proposals with the decisions left open** —
CRO does not pick the architecture here.

State handed over (verified, not assumed): the Google Sheet and `data/*.csv`
agree on all six tabs — `python3 build/check_parity.py` prints `MATCH` and exits 0.
DEMO rows repo-wide and sheet-wide: exactly 2, both in the empty tabs
(`triggers`, `instruments`).

---

## Item A — wire the two new scripts into CI

> **Note:** CTO's `dae700a` already added a **shrink-guard** to `sync_sheets.py`
> (a tab with fewer rows than the repo file is refused rather than silently
> truncating) and `573933e` re-enabled the cron after confirming sheet == repo.
> So the divergence risk is already covered at the **row-count** level. What
> follows is about the remaining gap and about seed drift — not a re-ask.

New, currently untracked in the working tree:

| Script | What it does | Runs against |
|---|---|---|
| `build/check_parity.py` | Read-only Sheet ↔ repo comparison, per tab, **cell by cell** — catches a row that changed content without changing count. Exits 1 on any difference. | the Sheet (read-only) |

`build/seed_sheet.py` is already committed (CTO, `573933e`).

The ask, in two halves:

1. **Keep the seed from drifting.** `data/seed/*.tsv` is generated from the CSVs;
   it goes stale the moment a CSV changes. Proposed: run `seed_sheet.py` in the
   build/deploy path so the deployed artifact and the seed always agree.
2. **Optional, complements the shrink-guard.** The shrink-guard compares *counts*;
   `check_parity.py` compares *cells*, so a same-length but edited row is still
   caught. Could run after the sync commit to annotate drift.

**Open for CTO:** where each step belongs (deploy build vs `sync.yml` vs a
separate workflow), and whether a parity failure should *warn* or *fail* the job.
CRO has no position on either.

## Item B — the dashboard renders 2 of 6 tabs

`build/build_dashboard.py` reads only `id-policy-inventory.csv` and
`id-readiness.csv`. The other four tabs now hold real data and are invisible on
the dashboard:

| Tab | Rows | Renders today |
|---|---|---|
| `Indonesia policy inventory` | 3 | yes |
| `readiness` | 3 | yes |
| `signals` | 9 | **no** |
| `who-can-act` | 6 | **no** |
| `triggers` | 1 (DEMO) | **no** |
| `instruments` | 1 (DEMO) | **no** |

The ask: add panels for `triggers` and `instruments` at minimum, and consider
`signals` + `who-can-act` since they are already populated.

**Second-order, worth a decision:** the demo banner keys off
`verified_by == "DEMO"` **in the inventory only**. The inventory is now real-only,
so the banner has disappeared — but there are still 2 DEMO rows, now in
`triggers` and `instruments`. Either the banner should count DEMO across all
tabs, or each tab should carry its own demo badge. CTO's call.

## Constraints that apply to both items

- **Consent gate.** Nothing shown outside the team until AISA consents; the Pages
  URL stays behind the access gate.
- **No personal data.** See `data/PERSONAL-DATA-STOP.md`.
- **Framing.** The readiness grid grades *documents*, never a government. No
  ranking, no scoring — the dashboard copy in `build_dashboard.py` already says so.
- **Not a CMS.** No write-back to Drive or Sheets.

## Provenance

- Data seeded from Akbar's shared deck `Indonesia.pdf`
  (`https://drive.google.com/file/d/1QVCKiq8Db5a-phu50jxsuQ1wbA23RMM7/view`) —
  pages 2–4 only. Fields the deck does not state are `tbc`; none were invented.
- Readiness answers are all `tbc` on purpose: scoring the six questions is the
  26 Oct deliverable, not this one.
