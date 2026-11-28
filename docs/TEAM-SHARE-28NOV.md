# Team share — what changed, and what to attach for the next BoxCompute run

**28 Nov 2026 · Shafira (Indonesia lane) · shareable**

---

## A · What to attach in BoxCompute

Seven files, all in [`docs/boxcompute-kit/`](boxcompute-kit/). Attach every one — the prompt references
them by name.

| # | File | What it is for |
|---|---|---|
| 1 | **`BOXCOMPUTE-PROMPT.md`** | The brief itself (92 lines). Paste the mission text, then attach the rest. |
| 2 | **`idph-2-indicator-table.csv`** | The team indicator spine — 25 indicators per country (ID-01…ID-25, PH-01…PH-25), each with its signal. **This is what stops rows landing on the wrong indicator.** |
| 3 | **`idph-1-collection.csv`** | What the team has already collected. Send it so the run appends rather than re-collecting. |
| 4 | **`id-shock-data-current.csv`** | **New today** — all 38 evidence rows currently in the register (ID-12 ×33, ID-17 ×5, 12 sources). This is the exact schema and the exact state to extend. |
| 5 | **`column-dictionary.md`** | The 31-column output contract: field-by-field meaning, allowed values, what `real or demo`, `verified?` and `confidence` are supposed to contain. |
| 6 | **`sources-registry.json`** | Sources already known and cited, so the run reuses URLs instead of inventing them. |
| 7 | **`akbar-indonesia-data-measures.pdf`** | Akbar's six measures (M1–M6) — so the run knows which measure each row is feeding. |

**The six things to ask it for** (from [`DATA-FEED-GAPS-28NOV.md`](DATA-FEED-GAPS-28NOV.md) Part 5):
1. the PERBANAS / IBM / K&A white paper PDF (Oct 2026) — sample frame, stage definitions, denominators
2. the same three-stage adoption split from any earlier survey (2023–2025)
3. function-level headcount (GRI 2-7) for all eight banks
4. hires and leavers (GRI 401-1) 2019–2024, plus voluntary vs total turnover
5. BNI's leavers figure — reconcile 1,324 vs 2,254 vs the stated 1.9%
6. one BRI employee-count definition (bank-only 84,949 vs group >119,000)

**One rule to repeat in the prompt:** *where a figure is paywalled or absent, record a row saying so — a
recorded gap is a result.*

---

## B · Sheets updated

### B1 · Model workbook — now **"SPAR Indonesia - Bank AI shock model v0.3b"**
[open](https://docs.google.com/spreadsheets/d/1GdULcdyhkJRwzTLH7xcFP4xnLC5tYFHnk-5vaGduTSE/edit)

| Tab | What changed |
|---|---|
| `Feed_Panel` | **8-bank panel completed**: hires and leavers for every bank, Dec-2025 headcounts for BNI/BCA/CIMB/KB, and the three previously empty banks (Mandiri 38,732 · BTN 11,429 · BSI 16,274). Basis column now cites each bank's sustainability report instead of press. **Three new columns**: `Total turnover rate` (M), `Voluntary turnover rate` (N), `Turnover basis / note` (O). |
| `Data_Feed` | Status lines now read *fed / partly fed* instead of *needs feed*, with what remains open. |
| `Summary` | Recalculated: panel 218,129; 2030 headcount **216,951 / 210,346 / 191,884**; Extreme 602 layoffs, Rp 9.0 bn JKP. |
| `Inputs` · `Scenarios` | Unchanged — no assumption was silently moved. |

### B2 · Core file — the register
[open](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit)

| Tab | What changed |
|---|---|
| **`id-shock-data`** | **Built and now holds 38 evidence rows** (31 columns). Run 3: 11 rows on ID-17/ID-12. p6: 27 rows of bank-level hires, leavers and turnover. |
| `Indonesia policy inventory` | 3 → **16 rows** — the 7 other instruments the indicator table names, the 5 the map knew and the register did not, plus `POJK 11/PADK 1`. |
| `instruments` | DEMO placeholder → **6 real levers**, one per actor's door. |
| `readiness` | **The six question texts are now in the tab** (`M1:N8`) with the "grades documents, never a government" caution. All six scores still `tbc`. |
| `who-can-act` · `triggers` · `policy-inventory` | Cross-tab links added; nothing overwritten. |

### B3 · SPAR signals skeleton
[open](https://docs.google.com/spreadsheets/d/1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo/edit)

| Tab | What changed |
|---|---|
| **`SIGNALS_ID`** | The Indonesia indicator table: S1–S10 mapped to indicators, policy de-coded to real acronyms and hyperlinked, the long review split into **Verdict · Capability · Details**, float-up highlighting, and each instrument name linked to its own register row. |
| `README` | Policy legend, layer definitions, float-up key — stated once, not on every row. |
| `SIGNALS` | `Relevant Policies` column aligned to the same instruments. |

### B4 · Team workbook — the shared indicator table
[open](https://docs.google.com/spreadsheets/d/11Q2bYaWcMUh66kS_0omY74Ye-itG9Xb7fsJAE0fjmok/edit?gid=20261126#gid=20261126)

| Row | What changed |
|---|---|
| **ID-12** `latest value` | Refreshed from stale Jun-2025 figures to the **Dec-2025 panel**: BNI 27,201 · BCA 26,435 · CIMB 10,775 · KB 2,334 · Mandiri 38,732 · BTN 11,429 · BSI 16,274 · BRI 84,949 (bank only) · panel **218,129**. |
| **ID-12** `possible other factors` | Appended: the turnover split (BRI 5.58% / 1.24%, Mandiri voluntary 3.53%) and the **BNI contradiction** (1.9% vs 1,324 leavers on 27,201 = 4.9%). |
| `Read Me_Methods` | **Still empty** — the one tab in this workbook nobody has written. It blocks the methodology page. |

---

## C · Files added or changed in the repo

| File | What it is |
|---|---|
| [`docs/DATA-FEED-GAPS-28NOV.md`](DATA-FEED-GAPS-28NOV.md) | The full feed-gap audit, the ID-05/ID-12 verdict, and the ready-to-run BoxCompute brief |
| [`docs/MODEL-BACKTEST.md`](MODEL-BACKTEST.md) + [`data/model-backtest.json`](../data/model-backtest.json) | Backtest: the model survives, the instrument does not (1:80 signal-to-noise on national JKP claims) |
| [`docs/MODEL-ATTRITION-SENSITIVITY.md`](MODEL-ATTRITION-SENSITIVITY.md) | One input changed → Extreme layoffs 602 → 7,718 and JKP Rp 9 bn → Rp 115 bn, with 2030 headcount unchanged |
| [`docs/ID-POLICY-SITE-PROPOSAL.md`](ID-POLICY-SITE-PROPOSAL.md) + [`build/proposal-wireframe.html`](../build/proposal-wireframe.html) | The policy-facing report-site proposal modelled on the Windfall scenarios site, and its wireframe |
| [`docs/ID-READINESS-WORKSHEET.md`](ID-READINESS-WORKSHEET.md) | Now carries the six question texts and the evidence for each |
| [`docs/REFERENCE-LIBRARY.md`](REFERENCE-LIBRARY.md) | Every source document indexed with its size and what it is |
| [`docs/ID-CALL-RUNSHEET-26NOV.md`](ID-CALL-RUNSHEET-26NOV.md) | The call run sheet |
| [`docs/ID-PART4-DRAFT.md`](ID-PART4-DRAFT.md) | Part 4 v1 — who can act and the policies in place, reframed to the shock question |
| [`app/`](../app/) | The atlas + scenarios app: 8-bank panel with reported flows, net-flow column, the model re-verified against the sheet |
| [`docs/boxcompute-kit/`](boxcompute-kit/) | The seven attach files above, including today's register export |
| [`build/sync_map_from_register.py`](../build/sync_map_from_register.py) | Generates the ecosystem map's policy nodes from the register — drift is now detectable instead of silent |
| [`docs/SHEET-WRITE-2026-11-24.md`](SHEET-WRITE-2026-11-24.md) | Every sheet write with its exact revert range, 24–28 Nov |

---

## D · What to say to the team, and what needs their decision

**One paragraph:** the Indonesia lane now holds a complete eight-bank headcount panel with reported hires,
leavers and turnover, verified against the model (zero delta); 38 evidence rows in a 31-column register;
the policy inventory filled to 16 instruments; and the six readiness questions named. What is missing is
concentrated in two places — the adoption evidence behind ID-05 (one press article, no paper, no second
time point) and function-level headcount, which is the model's biggest remaining assumption.

**Three decisions that are theirs, not the lane's:**

1. **Which attrition basis to publish** — all leavers (Rp 9 bn in Extreme) or voluntary only (Rp 115 bn).
   Both are in the sheet; neither should go out alone.
2. **The BNI contradiction** — three numbers, at most one right.
3. **The readiness wording** — the six texts are a proposal reconstructed from the team's A–F framework;
   Akbar's phrasing should replace ours.
