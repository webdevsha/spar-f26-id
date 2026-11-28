# Shafira's task progress (SPAR Fall 2026)

The full mirror of the `Shafira's tasks` tab, with due dates and status.

---

[← Back to the README index](../../README.md)

---

## Shafira's task progress (SPAR Fall 2026)

> Tallied **2026-11-28** from the `SIGNALS_ID` indicator table, the Core file (9 tabs: 22 signals,
> 16 policy instruments, 6 levers, 6 bodies), the generated ecosystem map (22 policy nodes), the
> Perplexity verification run, Kemnaker's own portal counts, `IND team progress` and repo state.
> Supersedes the 2026-11-26 tally.

```
Data spine        ███████████████████████░   97%  22 signals + 16 policies + 6 levers; id-shock-data 48 evidence rows (ID-12 x33, ID-17 x5, run-1 x10)
Data list (lead)  ███████████████████████░   95%  public source + verbatim + H/M/L on all rows; sources compiled per shared indicator; duplicates cleared
Part 3 (signals)  ███████████████████░░░░░   80%  country report v0.4 drafted end to end on the sourced base - shocks, ads, backtest, asks; needs Shafira's read
Part 4 (policy)   ████████████████████░░░░   85%  v1 written and reframed; its data is in the register; waiting on Ian's read + the word trim
Shared sheet/repo ██████████████████████░░   93%  register, model, app and postings tabs agree; sync job still failing, so the freeze is not safe
Section 5 (SPAR)  ██░░░░░░░░░░░░░░░░░░░░░░   10%  2,500w Indonesia chapter; report v0.4 is the raw material
Section 8 (Limits)██████████████░░░░░░░░░░   60%  draft ready to read with Napat
Interview (BPS)   █████░░░░░░░░░░░░░░░░░░░   20%  question reframed as a data-availability enquiry
Atlas site        ████████████████░░░░░░░░   65%  postings evidence added, light theme, 8-bank panel, net flows; deploy still not done
```

**Backfilled from the Hermes logs — Thu 26 and Fri 27 Nov.** Work that happened in the sessions but did
not leave a commit, recorded here so the progress bar is not flattering itself:

| When | What she did | Where it lives now |
|---|---|---|
| **Thu 26, 09:24–10:07** | Directed the `SIGNALS_ID` build point by point: the six own indicators pulled out of the tab, the new column, the no-redundancy rule ("if yes, must show details that makes it cited"), indicator **names only**, verdict first in the review, duplicates removed, one compiled source per shared indicator, acronyms in place of `P7`/`P8` | skeleton `SIGNALS_ID` |
| **Thu 26, ~11:00** | Restructured the Core `signals` tab with `signal_code`, `indicator_no`, `data_layer`, `next_step`, `origin_code` — the columns the 26 Nov merge had to respect | Core file `signals`, now 23 columns (re-verified 28 Nov) |
| **Fri 27, 18:46–18:54** | Set the **ground layer** going — the official files (Kemnaker Satudata PHK, OJK banking statistics, BPS, BPJS JKP) — and prototyped an `id-shock-data` tab, 29 columns, with the first real platform counts. **Jobstreet publishes a total (68,114 postings); most Indonesian boards are JS-only and publish nothing** | tab was closed on her instruction; the schema and the counts survive in the kit below |
| **Fri 27, 18:58–19:08** | Built the **BoxCompute kit** so the collection can run without her narrating it: a 92-line self-contained prompt, the ID+PH indicator spine as CSV, Akbar's six measures as PDF, a column dictionary and a 37 KB source registry | [`docs/boxcompute-kit/`](../../docs/boxcompute-kit/) |
| **Fri 27, 18:59–19:03** | Read the team's `SPAR indicator table — ID + PH (draft 26 Nov 2026)` (25 indicators per country) and Akbar's six measures, and set the crosswalk **S1–S10 × M1–M6** before writing anything | kit + the indicator table |
| **Fri 27, 19:33–19:34** | The 22-row merge into `signals` overwrote her `M1:W1` headers. It was reported immediately rather than papered over; the header row is now clean and 23 columns wide — I re-verified it on 28 Nov | Core file `signals` |
| **Fri 27, 18:30 Jakarta** | Indonesia team call with Akbar and Natraj (calendar) | — |

Two honest footnotes. **The `id-shock-data` tab she closed leaves the ground-layer collection designed but
not running** — the kit is its executable form, so the next step is a BoxCompute run, not more design. And
**None of the Friday work was in the repo until now**: the kit sat in `~/.hermes/projects/productivity/`
and the sheet was deleted, which is exactly the gap that makes a progress bar lie.

**Moved on 26 Nov — the indicator table, and the register made navigable:**

- **S1–S10 each mapped to an Indonesia indicator**, every row linked to the exact register row it came
  from (S3 and S4 correctly show none, because no indicator exists for them yet).
- **Source compiled per shared indicator.** Where one indicator serves several signals, its `Source`
  cell now carries the union of what backs it (e.g. M1 → `ILO · BPS`), so the same indicator reads
  identically wherever it appears.
- **Policy mapped and de-coded.** Every instrument is named in full with its acronym — `UU 27/2026`,
  `POJK 11/POJK.03/2022 and PADK OJK 1/2026`, `JKP (PP 37/2021)`, `Stranas KA 2020-2045`, `Kartu Prakerja` — and hyperlinked to
  its official source. Full titles, status and links live once in the tab's `README`, not on every row.
- **The long review cell is now three columns: `Verdict` · `Capability` · `Details`.** The full reading
  sits on the first row of each signal; the other rows of that signal carry the verdict and the
  capability line plus a one-line pointer, so no paragraph is repeated 2–5 times.
- **Reframed to the team's own question.** Each `Details` line now closes on what the signal *cannot*
  tell us about an AI economic shock — e.g. S5: *"a fall in banking vacancies caused by AI would look
  identical to a fall caused by a change in the rules."*
- **Float-up highlighting on the rows that should be raised, not just read.** Rose `#FCE8E6` = the
  shock would be invisible (S1, S3, S4); amber `#FFF2CC` = the number exists but cannot be read as an
  AI shock on its own (S5–S10); plain = S2 only. The key sits on the tab's `README`.
- **Duplicates and dead weight removed:** the indicator column was checked for repeats, the stray
  leftover row was cleared, layer definitions and the policy legend were moved out of the repeated
  cells into the tab's `README`, and one broken pointer (S8 had lost the row it pointed at) was rebuilt.
- **The sheets are now navigable.** 134 cross-tab links: a policy name jumps to its register row, a
  signal code to its definition, an actor to its lever, a lever back to the actor. `SIGNALS_ID`'s policy
  column links **each instrument name separately** to its own row in the register.
- **Part 4 in the register, so the map can read it.** `Indonesia policy inventory` 3 → **16 rows**;
  `instruments` DEMO → **6 real levers**; new generator
  [build/sync_map_from_register.py](../../build/sync_map_from_register.py) keeps the map's policy nodes in
  step with the register (9 → **22 nodes**), which is why the map page now shows `UU 27/2026`,
  `PP 6/2025`, `POJK 11`, `Stranas KA`, `RP3I` and the six levers.

**Moved on 28 Nov — the product, and the reference base:**

- **Studied the Windfall scenarios site** (`scenarios-2030.windfalltrust.org`) and wrote the proposal:
  ten patterns that work for a policy reader, what we must not copy, seven routes (five already built),
  two scenario axes our own evidence can support, and the evidence grammar — see
  [docs/ID-POLICY-SITE-PROPOSAL.md](../../docs/ID-POLICY-SITE-PROPOSAL.md).
- **A wireframe that shows it** — [build/proposal-wireframe.html](../../build/proposal-wireframe.html), light
  theme, using only figures already verified in the register; unsigned scenario bands print
  `bracket pending` rather than an invented midpoint.
- **The reference base indexed** — [docs/REFERENCE-LIBRARY.md](../../docs/REFERENCE-LIBRARY.md) cites the
  twelve third-party documents we rely on instead of redistributing them; eight of the twelve are
  voluntary corporate disclosures, which is itself one of the study's findings.
- **Work log added** — [the 24–28 Nov log](#work-log--everything-built-2428-november-2026) records every
  artefact with the PR or audit entry that carries it.
- **The model was backtested against the series that claims to measure it.** National JKP claims carry an
  8.8% noise floor inside two months; Extreme's ~100 claims a year is 0.11% of that. To shift the annual
  number 1% needs 1,090 layoffs in one year — 1.8× the model's entire five-year Extreme total. The model
  survives; the instrument does not. See [MODEL-BACKTEST](../../docs/MODEL-BACKTEST.md).
- **Attrition turned out to be the biggest lever, not adoption.** All-leavers attrition (6.11%) gives 602
  Extreme layoffs and Rp 9.0 bn; voluntary-only (4.38%) gives 7,718 and Rp 115.3 bn — a 12.8× swing with
  2030 headcount unchanged. Published as a sensitivity, not a new default: [MODEL-ATTRITION-SENSITIVITY](../../docs/MODEL-ATTRITION-SENSITIVITY.md).
- **The model sheet was brought to v0.3b** (and renamed): 8-bank panel with reported hires, leavers and
  turnover; `Feed_Panel` gained total and voluntary turnover columns; panel 218,129 and 2030 headcount
  216,951 / 210,346 / 191,884 — reproduced by `app/model.js` in node with zero delta.
- **The register went to 38 evidence rows** (`id-shock-data`, 31 columns): 27 new p6 rows of bank-level
  hires, leavers and turnover, appended after a schema and duplicate check.
- **The team table's stale ID-12 was refreshed** to the Dec-2025 panel, with the BNI contradiction and the
  turnover split appended to its notes rather than replacing what was there.
- **The six readiness question texts now exist** — reconstructed from the worksheet's own A–F evidence
  blocks, written into `readiness!M1:N8` with the "grades documents, never a government" caution, and
  labelled a proposal for Akbar to confirm.
- **Everything the next BoxCompute run needs is in one kit**: [`docs/boxcompute-kit/`](../../docs/boxcompute-kit/),
  now including the register export, plus the six collection targets in
  [DATA-FEED-GAPS-28NOV](../../docs/DATA-FEED-GAPS-28NOV.md) and the shareable summary in
  [TEAM-SHARE-28NOV](../../docs/TEAM-SHARE-28NOV.md).
- **The 1.03m-advertisement corpus is in, analysed and reconciled.** Banking exposure **0.582** (20,088 ads,
  94.3% in G2-G4), the crawl validated against a same-month census within **0.57 pt**, and only **Dealls**
  reconciles against our own `id-postings` (ratio **0.84**, median month **0.97**, monthly spread
  **0.30-1.67**) - which sets the noise floor for any postings claim. Two new tabs (`postings-monthly`,
  `postings-exposure`) plus `postings-recon`; Glints and Kalibrr are truncated and must never be trended.
- **The country report is drafted as v0.4** - eight-bank panel, measured exposure, the backtest verdict, the
  attrition sensitivity, the four asks: `docs/COUNTRY-REPORT-v0.4.md` (HTML rendered alongside).
- **The app and atlas were refined and moved to a light theme**: a postings section with the monthly panel
  and exposure by category, the corrected panel KPI (218,129 across eight banks, not 151,340 across five),
  and a postings section in the atlas that gives S5 its supply side.

**Pull requests:** [#35](https://github.com/webdevsha/spar-f26-id/pull/35) the first progress tally ·
[#36](https://github.com/webdevsha/spar-f26-id/pull/36) Part 4 v1 + the register and map work ·
[#37](https://github.com/webdevsha/spar-f26-id/pull/37) the tab links and the link graph ·
[#38](https://github.com/webdevsha/spar-f26-id/pull/38) the proposal, the wireframe and the work log —
**all four merged**. [#39](https://github.com/webdevsha/spar-f26-id/pull/39) carries the one-pager, the
scenario export and the reference-library index, and **cannot merge yet**: the `main` ruleset requires
CodeQL to be clean at error severity, and alert
[#4](https://github.com/webdevsha/spar-f26-id/security/code-scanning/4)
(`py/clear-text-storage-sensitive-data`, `build/build_overview.py:607`) is open on `main`. That alert sits
on the base branch, so it holds every pull request until it is fixed or dismissed. Part 4 itself:
[docs/ID-PART4-DRAFT.md](../../docs/ID-PART4-DRAFT.md) (the section has no Google Doc; the repo draft is its
only home).

**Evidence behind the bars:** `id-shock-data` — **38 evidence rows** (31 columns) · `SIGNALS_ID` — 18 indicator rows across S1–S10, verdict + capability on
every row, 10 full readings, 9 of 10 signals flagged for float-up · Core file `signals` — 22 rows ·
`triggers` 1 · `who-can-act` 6 · policy inventory **16** · readiness 3 (all `tbc`) · instruments **6 real
levers** (the DEMO placeholder is gone) ·
postings 2,618 rows (2024→Oct 2026) · Kemnaker portal counts 2022–24 in `data/kemnaker/` ·
[docs/ID-SIGNAL-SOURCE-MATRIX.md](../../docs/ID-SIGNAL-SOURCE-MATRIX.md),
[docs/ID-PART3-DRAFT.md](../../docs/ID-PART3-DRAFT.md), [docs/ID-READINESS-WORKSHEET.md](../../docs/ID-READINESS-WORKSHEET.md), [docs/ID-PENDING-24NOV.md](../../docs/ID-PENDING-24NOV.md),
[docs/SHEET-WRITE-2026-11-24.md](../../docs/SHEET-WRITE-2026-11-24.md) (revert ranges for every sheet write, 24–26 Nov).

**Open question on the table:** **M6 has no row** in `SIGNALS_ID` — coverage is M1 ×6, M2 ×5, M3 ×2,
M4 ×6, M5 ×5, plus rows still without an indicator. Either a signal carries M6, or it should be marked
unused so the register's six-measure structure does not look one short.

**Next due:** Fri 27 Nov (one interview about data gaps) → Sun 29 Nov (sheet frozen into the repo —
blocked by the sync failure) → Wed 2 Dec (§5 + §8 to Rachel). SPAR submission 14 Dec; Demo Day 19 Dec.
