# Indonesia lane — decision calendar

**Draft v0 · 24 Nov 2026 · Shafira, with Rachel · handoff item 7 (6 windows, dates and owners confirmed)**

The point of this file: a decision window is only real once it has a **date, a named owner, and an
artefact that closes it**. Windows still waiting on something are marked, not hidden.

| # | Window | Date | Closes when | Owner | Status |
|---|---|---|---|---|---|
| 1 | **Data-gap interview** | **Fri 27 Nov** | The BPS/Kemnaker data-availability question is asked in one interview | Shafira | Question drafted; SPAR still confirming interview access |
| 2 | **Sheet frozen into AISA repo** | **Sun 29 Nov** | Sheet and repo are in step, so the freeze is meaningful | CTO lane | ⚠️ **Blocked** — `sync-sheets` failing hourly at *Commit if changed*; repo holds 9 signal rows against the tab's 22 |
| 3 | **Indonesia chapter + limits to Rachel** | **Wed 2 Dec** | §5 Indonesia (~2,500w) and §8 Limits (~300w) handed over | Akbar (lead), Natraj, Shafira + Napat | Part 3 draft written; Part 4 draft written; §8 draft written |
| 4 | **SPAR report submission** | **Sun 14 Dec** | The team's report is submitted | Team (Akbar / Rachel) | — |
| 5 | **Demo Day** | **Sat 19 Dec** | Findings presented; the data underpins | Akbar & Danielle | — |
| 6 | **Publication on SEA Observatory** | **Jan 2027** (week of 18 Jan) | The Atlas page is public | Shafira | Consent-gated by AISA; requires sign-off first |

## Standing action attached to window 1

If the `id-triggers.csv` trigger fires — **AI-linked clerical reductions announced by two or more
banks in the same province within one quarter** — the response window opens at **30 days**, routed
OJK (confirm) → Kemnaker Pusat Pasar Kerja + JKP office (act). Cost of the response is **not yet
estimated**: it needs the instrument map to price, so this stays `[unpriced — confirm]`.

## What each window is actually gated on

- **Window 2** is the only one blocked by infrastructure, and it is not the lane's to fix. Until the
  hourly sync commits again, freezing the sheet would freeze a stale mirror.
- **Windows 1 and 6** are gated on **other people** — interview access (SPAR) and publication consent
  (AISA). Neither is a work item that more effort closes.
- **Window 3** is the one this lane controls, and it is now the furthest along.

*Framing: dates are the plan's own checkpoints. Recording a slip is not a judgement about anyone's
work — it is what makes the slip visible in time to act on it.*
