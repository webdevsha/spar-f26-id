# Sheet writes, 2026-11-24 (CRO) — what to clear if you want a revert

Two shared team sheets were written with Sha's explicit instruction. Nothing else was touched;
no existing column, header or value was renamed, reordered or deleted.

## 1. Core file -> `signals` tab  (`1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k`, gid 838965401)
**Wrote:** columns `O:T`, rows 1-23 (header + all 22 rows). Columns O:T were EMPTY before.
- O `link` — public source URL (Meta rule 5)
- P `source_verbatim` — the figure or finding as published
- Q `confidence` — H / M / L
- R `data_status` — supported / partly supported / gap
- S `not_verified` — what remains unverified, in words
- T `source_checked` — `2026-11-24 - Perplexity ID verification run`

**Revert:** clear range `signals!O1:T23`.

## 2. SPAR_signals_skeleton -> `SIGNALS` tab (`1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo`)
**Wrote:** columns `H:K`, rows 1-11 (header + S1-S10). Columns H:K were EMPTY before.
- H `ID evidence (Shafira, 24 Nov 2026)`
- I `ID source (public)`
- J `ID status`
- K `ID gap / route`

**Revert:** clear range `SIGNALS!H1:K11`.

## Provenance
Content is transcribed from `data/id-postings/perplexity-id-data.md` (the Perplexity verification
run, 24 Nov) and from `data/kemnaker/*.csv` (Pasker ID public downloads, fetched 24 Nov).
Unverified figures are written as "not verified" - none were replaced or smoothed.

## Note
The hourly `sync-sheets` workflow is currently failing at its commit step, so these sheet edits
will NOT appear in the repo's `data/*.csv` until that is fixed. The repo mirror still holds 9
signal rows against this tab's 22.

## 3. `IND team progress` (`1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ`, tab `Sheet1`)
**Wrote:** column `G`, rows 1-21. Column G was EMPTY before.
- G1 header `Comments (concise) - updated 24 Nov 2026` (the new column asked for, placed after PIC)
- G15 unknown row `Policy readiness review` — comment: scoring outstanding (readiness tab still 3 documents x q1-q6 all `tbc`); what moved is the source line (OJK AI guide, JKP + PP 6/2025, Pasker ID) and the request routes to OJK / BPJS PPID / Kemnaker PPID
- G18 `Job-postings dashboard` — comment: report live; coverage calibrated against Kemnaker's own counts (66 finance/BPO rows for 2024 vs the portal's 726 = about 9.1%); new overview + scenarios page built but NOT public yet (Cloudflare deploy token, code 10000)

**Deliberately NOT changed:** `Progress` and `Status` values on either row, and every other row of the
sheet. The percentages are a judgement about Shafira's work, so they stay as she set them until she
says otherwise. Comments on rows where she is a co-PIC (10, 12, 13, 14, 16) were also left blank.

**Revert:** clear range `Sheet1!G1:G21`.

## 4. `IND team progress` - second pass (plan items + clickable links)
Same sheet, later on 24 Nov.
- **Links (column C) on existing rows 3, 4, 6, 7, 8, 10, 11, 13, 17, 19, 21** - the named artefacts now carry URLs beneath the name (Labor Microdata folder + Microdata Findings.pptx, the Bank AI deployment doc, Midterm Report, SPAR model, Core file, triggers tab, interviewee sheet, Indonesia Op-Ed). Revert: restore the plain names that were there before (row-by-row).
- **Progress / Status / Comments on rows 11, 13, 14, 15, 16** - Decision calendar 50->80% Ready for review; Signal watchlist 50->80% Ready for review; Data inventory 50->75%; plus refreshed one-line comments. Revert: set those cells back to 50% / In progress.
- **New block rows 22-35** - section header `C. Shafira's six-week-plan items (country report, data, site)` and 13 task rows, each with Details, Links, Progress, Status, PIC, Comment. Revert: clear `Sheet1!A22:G35`.

## 5. Correction - Sheet1 writes reversed, and a separate tab added

**Sha restored the tracker (`Sheet1`) to its 18:44 version**, which reverses writes 2 and 4 of this
note: the `Sheet1!A22:G35` block is gone, the Progress/Status moves are back to 50% / In progress,
and the Links additions were reduced to the rows that already had a link at 18:44. Sheet1 now stands
at 21 rows and is **not touched again by CRO work**.

Still present in that restored version: the one-line comments added by write 1 on rows 12, 14, 15,
16 and 18 (column G). To clear them: `Sheet1!G12`, `G14`, `G15`, `G16`, `G18`.

**New tab added instead: `Shafira's tasks`** (same spreadsheet, `1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ`).
- Same header row as Sheet1: `Work | Details | Links | Progress | Status | PIC | Comments`
- 20 rows, Shafira's own work only (solo or co-PIC), plain language, header row frozen and bold
- Revert: delete the tab, or clear `'Shafira's tasks'!A1:G21`

### `Shafira's tasks` - Links column made clickable
Plain-text URLs are not clickable in Sheets, so column `C` (rows 2-21) was rewritten as
`=HYPERLINK("url","Short label")`, joined with a middot when a row needs two links. Column widths,
text wrapping and top alignment were set, and the header row is frozen and bold.
Verified by reading the computed values back: 20 label rows, no spreadsheet errors, no blanks.
**Revert:** clear `'Shafira's tasks'!C2:C21`.

## 6. `SPAR_signals_skeleton` - `SIGNALS_ID` tab filled (mapping only)
Requested: map the Core-file signal ids onto the team skeleton. Only the two columns Sha had
already added were filled - `E Indonesia's indicator` and `F Source`. No column was added,
renamed or reordered, and the `SIGNALS` tab was left exactly as it was.

- `E` = the Core file's own ids, taken from its `ian_signal` column (so the mapping is the team's,
  read back rather than re-invented): S1 ilo-exposure, baseline-exposure, contact-centre-share (proxy);
  S2 bank-ai-usecases, baseline-genai-use, contact-centre-share, bank-function-hiring (bridge);
  S5 karirhub, sakernas, baseline-sector-size, gap-adoption-hires (bridge);
  S6 baseline-sector-size; S7 branch-footprint, sakernas, baseline-sector-size;
  S8 jkp-claims, jkp-cases-v-recipients, jkp-rejections, jkp-reform-break, jkp-processing-time;
  S9 baseline-informal, worker-destinations, jkp-training-outcomes, jkk-rtw (caution);
  S10 bank-ai-training, peka-training, jkp-training-outcomes.
- **S3 and S4 are written as explicit "None - blind spot"**, because the register holds no
  Indonesian indicator for either. That is the finding, not a gap to fill in.
- `F` = the public source(s) behind that signal's Indonesian evidence; left as "-" for S3/S4.
- All 22 Core-file ids appear at least once. Column widths set, wrapped, top-aligned.

**Revert:** clear `'SIGNALS_ID'!E2:F11`.

### `SIGNALS_ID` final layout (mapping, one indicator per row)
Rebuilt per instruction. Header row 1 was Sha's and is preserved; columns added: `G Source
verbatim`, `H Confidence`, `I Not verified` (headers written to G1:I1).
- **One indicator per row** - 29 rows, so a signal with three indicators (e.g. S1) has three rows,
  repeating the `#`, `Signal`, `Layer` and `What it means` values.
- `E Indonesia's indicator` - **full names**, register signal name plus its measure label
  (e.g. "GenAI exposure index - M1 Sector employment and exposure"), each hyperlinked to that exact
  row in the Core file (`#gid=838965401&range=A<row>`).
- `F Source` - taken from the Core file's `link` column, shown as a short clickable label
  ("BPS", "OJK - Statistik Perbankan Indonesia", "BPJS Ketenagakerjaan", ...).
- `G/H/I` - the register's `source_verbatim`, `confidence`, `not_verified` per indicator.
- S3 and S4 are single rows reading simply `None` in Indonesia's indicator (per instruction), with `-` in the source and register columns. The reason they are empty lives in the register's own notes and in `docs/ID-SIGNAL-SOURCE-MATRIX.md`.
- Column widths set, wrapped, top-aligned, header bold.

**Revert:** clear `'SIGNALS_ID'!A2:I30` and `'SIGNALS_ID'!G1:I1`.

**Correction (S3 / S4):** on instruction, the indicator cell for S3 (AI adoption rate) and
S4 (Forecast) now reads simply `None`, with `-` in the source and register columns. The reasons
(no Indonesian firm-level adoption series; no AI-named outlook revision) stay in the register's own
notes and in `docs/ID-SIGNAL-SOURCE-MATRIX.md`, not on this tab.

**Correction (measure labels):** `E` now carries **all** of each indicator's measures, not just the
first one - so `Workers and spending` reads `M4 Job loss and worker destinations · M6 Consumption and
fiscal effects`, and **M6 is visible on the tab for the first time**. Alignment is now derived from
the sheet's own `#` column, so a row cannot take the wrong indicator. Visible measures: M1 x7 rows,
M2 x7, M3 x2, M4 x6, M5 x5, M6 x1 (distinct indicators: M1 four, M2 six, M3 two, M4 six, M5 four, M6 one).

## 7. `SPAR_signals_skeleton` -> `SIGNALS_ID` policy columns (G and H)
Sha inserted two columns; both were filled for all 29 indicator rows. No other column touched.
- `G Indonesia's policy` - a **numbered list** (1., 2., 3. ...) of the Indonesian instruments that
  bear on that row's indicator / signal.
- `H Policy review against the indicator` - how far those instruments actually engage it, ending in a
  plain verdict (partial / silent / covers demand partially / strongest instrument, weakest
  self-measurement).

Instruments named (each located and checked 24-25 Nov 2026): UU 27/2026 Pelindungan Ketenagakerjaan
(in force 28 Oct 2026); PP 35/2021 (contracts, outsourcing, termination); PP 37/2021 (JKP);
PP 6/2025 (JKP amendment, 7 Feb 2025); Permenaker 5/2024 (Labour Market Information System - the
legal basis for Pasker ID / Karirhub); OJK *Tata Kelola Kecerdasan Artifisial Perbankan Indonesia*
(AI governance guide); POJK 38/POJK.03 + SEOJK 21 (IT risk management for banks); Stranas KA
2020-2045; Kartu Prakerja; PP 44/2015 (JKK, JKM) and PP 46/2015 (JHT).

**Two gaps this exposed, not yet actioned:** the register's policy inventory still holds only three
documents, so UU 27/2026, PP 35/2021, Permenaker 5/2024, POJK 38 and Stranas KA are not in it and
cannot be scored for readiness; and the 28 Oct 2026 labour-law change is a fresh comparability break
on top of PP 6/2025.

**Revert:** clear `'SIGNALS_ID'!G2:H30`.

### `SIGNALS_ID` - de-duplication and citation pass (columns E, G, H + README legend)
- **E `Indonesia's indicator`** now carries the register id and the signal codes each indicator serves,
  e.g. `Contact-centre automation share (ind-sig-contact-centre-share · serves S1, S2) - M2 ...`. Six
  indicators legitimately serve more than one signal (bank-function-hiring S2/S5; baseline-sector-size
  S5/S6/S7; contact-centre-share S1/S2; gap-adoption-hires S2/S5; jkp-training-outcomes S9/S10;
  sakernas S5/S7) - the reuse is now stated in the cell instead of looking like a duplicate.
- **G `Indonesia's policy`** uses **stable codes P1-P10** (numbered, identical on every row) with a short
  cite, so a repeated instrument reads the same everywhere and can be cited by code.
- **H `Policy review against the indicator`** opens with the codes it relies on, e.g. `[P6 P7 P8] ...`,
  so each verdict is traceable to the instruments in G.
- **Legend added to the `README` tab (rows 20-32)**: P1-P10 with full titles, status and official source
  links (P3 points to the BPJS regulation index - no deep link verified, stated as such).
- Column F (`Source`) was left untouched and verified: no row has an empty Source.

**Revert:** clear `'SIGNALS_ID'!E2:H30` (E/G/H only - restore F if you also want the source labels gone)
and `'README'!A20:D32`.

### `SIGNALS_ID` legibility pass (E, G, H)
- **E** now shows only our indicator name - one of the six measures, e.g. `M1 Sector employment and
  exposure` - hyperlinked to the register row it came from. Parenthetical qualifiers were removed from
  this column on instruction; they remain on the register row and in the source matrix.
- **G** lists each instrument **name first, code in brackets**, hyperlinked to its official source:
  `1. AI governance guide for banks (OJK)` etc. The numbering is per row but the codes (P1-P10) are
  stable, so the same instrument reads identically on every row.
- **H** is written in full sentences with the **verdict first** and the codes spelled out for legibility,
  e.g. `Verdict: partial. Governance is covered, but capability is not. Both the AI governance guide for
  banks (P6) and the technology-risk rules for banks (P7) ...`. Every instrument mention is a hyperlink.
  Acronyms are expanded in place (JKP = job-loss insurance scheme; OJK = the financial regulator;
  PP/UU referred to by what they do).
- Read back: 29 rows, no row missing its Source, E holds only the six measure names plus `None`.

**Revert:** clear `'SIGNALS_ID'!E2:H30` (restores the previous wording only if it is re-run; column F is
never written by these passes).

### `SIGNALS_ID` dedup + acronym pass (C, F, H) and `README` legend
Instruction: check duplicates in the indicator column, compile the source per shared indicator, drop my
shorthand codes from the review column in favour of real acronyms, and shorten any column that repeats
the same analysis on every row.

1. **`F` (Source) compiled per shared indicator.** Six indicators sit on more than one row; the Source cell
   is now the union of everything behind that indicator, written identically on every row it appears on:
   - `M1 Sector employment and exposure` -> `ILO · BPS`
   - `M2 AI deployment and workforce change` -> `BRI Sustainability Report 2025 · BCA · Microsoft AI diffusion report · World Bank · OJK - Statistik Perbankan Indonesia`
   - `M3 Recruitment and vacancies` -> `World Bank · Kemnaker Pasker ID`
   - `M4 Job loss and worker destinations` -> `BPJS Ketenagakerjaan · Kemnaker JDIH - PP 6/2025 · BPS`
   - `M5 Worker support capacity` -> `BPJS FAQ (service standard) · ILO · BPJS Ketenagakerjaan`
2. **`H` (policy review): no more P-codes.** Every instrument is named in full first, acronym in brackets:
   `UU 27/2026`, `PP 35/2021`, `JKP (PP 37/2021)`, `PP 6/2025`, `Permenaker 5/2024`, `OJK` guide,
   `POJK 38/SEOJK 21`, `Stranas KA 2020-2045`, `Kartu Prakerja`, `PP 44/2015 and PP 46/2015`.
   Verified: zero bare `P<digit>` tokens left in H.
3. **`H` dedup within a signal.** Each signal lists several indicators in consecutive rows and the review
   was identical on all of them (S8 five times, S2 four times, ...). The full review now sits on the
   **first row of each signal**; the repeat rows carry one line instead:
   `Verdict: <verdict>. The same instruments apply to this indicator as to the first <S#> row above -
   see that row for the full review.` Removes 18 duplicated paragraphs.
4. **`C` (Layer) shortened.** It carried the definition inside the cell on every row
   (`labor\n(The labors are affected)` x20, `adoption\n(...)` x6, `capability\n(...)` x2). The cell now
   holds the layer word only; the three definitions moved to `README` rows 34-37, stated once.
5. **Stray duplicate row cleared.** `E30` held an old-style long label
   `JKP training slots, waiting times and employment outcomes - M5 Worker support capacity (S10 -> S9;
   linked outcomes not verified)` with every other column blank. That register row is already live on the
   S9/S10 rows, so `E30` was cleared as a duplicate.
6. **`README` legend retitled** (`A20`): the codes are now marked internal-only, since the table no longer
   cites them; the full titles, status and official links are unchanged.

**Revert:** `'SIGNALS_ID'!C2:C30` and `'SIGNALS_ID'!H2:H30` back to the pre-dedup wording,
`'SIGNALS_ID'!F2:F30` back to one source per row, `'SIGNALS_ID'!E30` re-enter the label,
`'README'!A20:D22` + `'README'!A34:D37` clear. Columns F/G/I/K were never touched by the H/C writes.

### `SIGNALS_ID` coherence audit (read-only, plus one tidy-up)
Audit of the whole tab after the dedup pass. **Note the tab changed under us:** it held 29 data rows when
the dedup pass ran and 27 when the audit ran - two S2 rows were removed in between (rows are 2-28 now).
Every write landed on the row it was aimed at, so the alignment held: each signal still carries its full
review on its first row and the one-line pointer on the repeats.

Findings:
1. **No true duplicate rows.** Rows sharing the same (signal, indicator) pair differ in the evidence
   columns on purpose: `S5·M1` r9/r10, `S7·M1` r14/r15, `S8·M4` r16-r19, `S9·M4` r21/r22,
   `S9·M5` r23/r24, `S10·M5` r26/r27. Each pair/triple is a **different source and a different verbatim
   quote for the same indicator** - which is what columns I/J/K exist for. The compiled Source (F) now
   surfaces both.
2. **Signal blocks are contiguous and self-consistent.** S1-S10 in order, one layer per signal, one
   "What it means" per signal, one verdict per signal, no row without a policy instrument.
3. **Cross-tab parity: names and layers match** the `SIGNALS` tab exactly for S1-S10.
4. **Gap - `SIGNALS` tab "Relevant Policies" (column J) is empty on all 10 rows.** The policy mapping
   only lives in `SIGNALS_ID`. Cross-tab coherence item, not yet written (needs the user's word).
5. **Gap - M6 has no row.** Only M1-M5 appear (M1 x6, M2 x5, M3 x2, M4 x6, M5 x5, plus 3 rows with no
   indicator yet). M6 "Consumption and fiscal effects" is defined in the register but unmapped here.
6. **Wording nit - S9's verdict is `silent` while its indicator column is filled.** Same word as S3/S4,
   which have no indicator at all. Proposed: `Verdict: silent on policy.` (4 cells: r21 full + r22-r24
   pointers) so the two cases cannot be confused. Not applied - content call.
7. **Tidy-up applied:** `A28:K28` cleared - a leftover all-blank row that still carried `-` in the
   Source column.

**Revert:** re-enter `-` in `'SIGNALS_ID'!F28` for item 7. Items 4-6 are unwritten proposals.

### Coherence fixes applied (approved 26 Nov) - `SIGNALS_ID` H, `SIGNALS` J
1. **`SIGNALS_ID` H21:H24 - S9 verdict reworded.** `Verdict: silent.` -> `Verdict: silent on policy.` on the
   full review (r21) and on the three pointer rows (r22-r24). Reason: S9 has a filled indicator column, so
   plain `silent` read the same as S3/S4, which genuinely have no indicator at all. On S9 it is the policy
   that is silent, not the data.
   Read back: `Verdict: silent on policy. Nothing follows a worker after they leave. Even the old-age and
   injury schemes (PP 44/2015 and PP 46/2015) pay out whether a person resigned or retired ...`
2. **`SIGNALS` J2:J11 - "Relevant Policies" filled** (was empty on all 10 rows). One row per signal, built
   from the `SIGNALS_ID` policy mapping, numbered and hyperlinked, instruments named with acronyms.
   - S1 3 · S2 3 · S3 3 · S4 2 · S5 4 · S6 4 · S7 3 · S8 4 · S9 3 · S10 4 instruments, all links live.
   - Example S8: `1. Job-loss insurance scheme (JKP, PP 37/2021) 2. Change to job-loss insurance (PP 6/2025)
     3. Employment law of October 2026 (UU 27/2026) 4. Work-injury, death and old-age schemes (PP 44/2015, PP 46/2015)`

**Tab state when written:** 25 indicator rows (rows 2-26), S1-S10 contiguous, full review on the first row of
each signal + pointer on the repeats, no row missing a Source, no bare P-codes. The tab is being edited live -
it has gone 29 -> 25 rows during this session - so re-read before the next positional write.

**Revert:** `'SIGNALS_ID'!H21:H24` back to `Verdict: silent.`; clear `'SIGNALS'!J2:J11`.

### `SIGNALS_ID`: review column split into three (H | I | J)
Instruction: the policy review cell was too long - give it a verdict column, a capability column and a
details column.

- **Structural:** two columns were inserted at index 8-9 (`inheritFromBefore=true`), so the review column
  keeps column H and the evidence columns shifted right: `Source verbatim` I->K, `Confidence` J->L,
  `Not verified` K->M. No data was retyped by the shift; all three evidence columns carried over intact
  (verified: no row lost K, and the E/G hyperlink formulas are still live).
- **New headers:** `H1 Verdict` | `I1 Capability` | `J1 Details` (H1 was `Policy review against the indicator`).
- **H (Verdict)** - the call only: `partial` (S1, S2, S5, S6, S10) | `silent` (S3, S4) |
  `silent about jobs` (S7) | `strongest instrument, weakest self-reporting` (S8) | `silent on policy` (S9).
- **I (Capability)** - one short line of what is covered and what is missing: S1 `Governance covered;
  capability not` | S2 `Oversight covered; headcount effects not` | S3 `Nothing reports an adoption rate` |
  S4 `No disclosure duty at all` | S5 `Vacancies counted; filling not` | S6 `Event recorded; banking split
  not` | S7 `Office counts published; staffing link absent` | S8 `Payouts recorded; own performance not` |
  S9 `Payouts counted; destinations not` | S10 `Training funded; outcomes not linked`.
- **J (Details)** - the full sentences with instruments named and hyperlinked, on the first row of each
  signal; later rows of the same signal carry the one-line pointer instead.
- **S8 repair:** the live row deletions had removed the S8 row that held the full review, leaving two
  pointers to a row that no longer existed. The full S8 text was rebuilt on the surviving first S8 row.

**Revert:** delete the two inserted columns (I and J) with `DeleteDimensionRequest` on sheetId 265881413
range 8-9, then restore `H1` to `Policy review against the indicator` and put the pre-split review text
back into H (the pre-split wording is in the earlier entry above).

**Tab state when written:** 18 indicator rows (rows 2-19), S1-S10 contiguous, every signal's first row
carries the full detail. The tab continues to be edited live.

### `SIGNALS_ID` float-up highlighting + `README` key
Instruction: colour the rows whose finding should be floated up. Light theme only (pale fills).

- **Rose `#FCE8E6` - "nothing can answer this today"**: S3 (r6), S4 (r7). No published AI adoption rate
  anywhere, and no duty on any ministry, regulator or industry body to publish an AI-linked jobs or
  revenue forecast.
- **Amber `#FFF2CC` - "series broken / tracking missing"**: S6 (r11), S8 (r14-r15), S9 (r16-r17).
  Two stacked legal breaks in the claims series (PP 6/2025 on 7 Feb 2025, UU 27/2026 on 28 Oct 2026,
  implementing rules not due until 28 Oct 2027) and no destination tracking after job loss.
- Colour applied across columns A-M of each flagged row, so the whole block reads as flagged.
- **`README` rows 39-41:** "FLOAT-UP KEY" - rose and amber swatches with their meaning, once.
- Left uncoloured on purpose: S1, S2, S5, S7, S10 - usable with the caveat already written in their
  Capability cell. S1's "capability not covered" gap is a candidate to add if the user wants it.

**Revert:** clear `backgroundColor` on `'SIGNALS_ID'!A6:M7` (rose), `'SIGNALS_ID'!A11:M11`,
`'SIGNALS_ID'!A14:M15`, `'SIGNALS_ID'!A16:M17` (amber); clear `'README'!A39:D41`.
Guard: row numbers shift if rows are added/removed - re-read before reverting.

### `SIGNALS_ID` AI-economic-shock reframe + highlight re-tier
Instruction: findings and analysis must relate to the AI economic shock (the SPAR Economic Shock Team's
question); refine the highlights accordingly.

- **`I` Capability rewritten** so each line names the shock consequence, not just the column gap:
  S1 `The shock's onset is not recorded` | S2 `Announced intent only, never the headcount effect` |
  S3 `No adoption rate, so the shock cannot be sized` | S4 `No AI-linked forecast, so no early warning` |
  S5 `Vacancies counted; what filled or killed them, not` | S6 `Event recorded, but not split by sector and
  the series is broken` | S7 `Offices counted, but never the staffing behind them` | S8 `Payouts recorded,
  but the series has two breaks and no pace` | S9 `Payouts counted, then the trail stops` |
  S10 `Training funded, but no link to a job or earnings`.
- **`J` Details rewritten** so every signal ends on its AI-shock implication - e.g. S5 "a fall in banking
  vacancies caused by AI would look identical to a fall caused by a change in the rules"; S8 "the closest
  thing Indonesia has to a shock meter for bank workers, and it cannot yet measure its own timing"; S10
  "Indonesia can show that retraining happened in response to AI, but not whether it worked".
  Verdict column unchanged. Pointer rows reworded to "...the full AI economic shock reading."
- **Highlights re-tiered** on one criterion - can the row answer "is AI causing an economic shock in
  Indonesian banking?"
  - **rose `#FCE8E6`** ("the shock would be invisible"): S1 (r2-r3), S3 (r6), S4 (r7)
  - **amber `#FFF2CC`** ("number exists, cannot be read as AI alone"): S5 (r8-r10), S6 (r11), S7 (r12-r13),
    S8 (r14-r15), S9 (r16-r17), S10 (r18-r19)
  - **plain**: S2 only (banks self-disclose AI intent, so it can carry an AI reading)
  All data rows were cleared to white first, so the tiering is deterministic rather than layered.
- **`README` rows 39-42:** key reframed to the shock question, now four lines (header, rose, amber, plain).

**Revert:** clear `backgroundColor` on `'SIGNALS_ID'!A2:M19`; `'README'!A39:D42` clear. Row numbers shift
with the live edits - re-read first.

### Core file: Part 4's data into the register (26 Nov) - `Indonesia policy inventory` + `instruments`
Instruction: Part 4 (who can act / policies in place) must exist in Google Sheets too, so the data can
feed the ecosystem map and the policy inventory readily.

1. **`Indonesia policy inventory` A5:M11 - 3 rows -> 10.** The 3 existing ids were untouched
   (`ind-ojk-ai-guide-2025`, `ind-jkp-2022`, `ind-paskerid-kemnaker`); 7 added, matching exactly the
   instruments the `SIGNALS_ID` indicator table names (the P1-P10 legend):
   `ind-uu27-2026` (law, in force 28 Oct 2026, implementing rules due 28 Oct 2027) · `ind-pp35-2021` ·
   `ind-pp6-2025` (effective 7 Feb 2025) · `ind-stranas-ka-2020-2045` · `ind-prakerja` ·
   `ind-pp44-2015` (JKK, JKM) · `ind-pp46-2015` (JHT). Existing 13-column schema kept; unknown values
   left `tbc`, per the register's own convention.
2. **`instruments` A2:L7 - the DEMO placeholder replaced with 6 real lever rows**, one per actor's door
   in Part 4: `ind-inst-ojk-supervision` · `ind-inst-kemnaker-pasker` (the only lever with a stated lead
   time: within 30 days, per the trigger card; cost not yet estimated) · `ind-inst-jkp-monitoring` ·
   `ind-inst-bps-sakernas` · `ind-inst-perbanas-outreach` · `ind-inst-ilo-method`. All are marked
   `source_type=draft`, `verified_by="CRO draft - needs Akbar + mentor review"`, with the evidence cell
   pointing at the who-can-act row or the trigger card each one rests on. Cost/speed stay `tbc` where
   nothing sourced says otherwise.
3. **Repo mirror updated by hand** (the hourly sync is still failing): `data/id-policy-inventory.csv`
   (10 rows) and `data/id-instruments.csv` (6 rows) now match the sheets, so the map and dashboard read
   the same data once the sync is restored. This is a manual mirror, not a new source of truth.

**Found while doing it (not fixed - needs a decision):** the ecosystem map's policy view
(`data/ecosystem-id-map.json`) is out of step with the register **in both directions** - it holds nodes
the inventory does not (`pol-rp3i` RP3I 2026-2030, `pol-voc50k` the 50,000-worker programme), and the
7 documents just added are absent from it.

**Revert:** clear `'Indonesia policy inventory'!A5:M11`; re-enter the DEMO row at `'instruments'!A2:L2`
and clear `'instruments'!A3:L7`; restore the two CSVs from git (`git checkout HEAD~ -- data/id-policy-inventory.csv data/id-instruments.csv`).

### Cross-tab navigation links + register<->map loop (26 Nov, evening)
Instruction: make the sheet data clickable across tabs so the sheets are navigable.

**Links written (134 cells, every one only where the cell was plain text - no existing hyperlink was
overwritten):**
- Core `signals`: `M ian_signal` -> skeleton `SIGNALS` row; `E holder` -> Core `who-can-act` row (37 links)
- Core `who-can-act`: `E proposed_door` -> Core `instruments` lever row; `D relevant_data_or_programme`
  -> Core `Indonesia policy inventory` row (9 links)
- Core `instruments`: `G evidence` -> the `who-can-act` row named in the cell (6 links)
- Core `Indonesia policy inventory`: `E owner_agency` -> `who-can-act` row; `C short_name` -> `readiness`
  row for the same id (16 links)
- Core `triggers`: `E agency` -> `who-can-act`; `F action` -> the lever it describes (job fair/retraining
  -> `ind-inst-kemnaker-pasker`)
- Core `readiness`: `B document` -> `inv` row for the same id (3 links)
- Skeleton `SIGNALS`: `A #` -> first `SIGNALS_ID` row for that signal (10 links)
- Skeleton `SIGNALS_ID`: `A #` -> `SIGNALS` row (18 links)
- Skeleton `README`: legend `B` (P1-P10 names) -> Core `inv` rows (8 links)

**Cross-file links added later:** `SIGNALS_ID` column `G` - the policy cells had reverted to plain text,
so each instrument name now carries its own link (textFormatRuns, 18 cells / 55 link spans) pointing at
that instrument's row in the Core file's `Indonesia policy inventory`. The cell text was not changed.

**New inventory row:** `ind-pojk11-padk1` (row 17) - her wording now reads "Technology-risk rules for
banks (POJK 11/POJK.03/2022 and PADK OJK 1/2026)", so the register needed a row to link to. The old
"POJK 38/SEOJK 21" reference is superseded; not re-inserted anywhere.

**Register <-> map loop:**
- `Indonesia policy inventory` 15 -> 16 rows; `instruments` 6 levers.
- New generator `build/sync_map_from_register.py` (default `--check` is read-only): policy nodes
  9 -> 22 in `data/ecosystem-id-map.json` (8 hand-written nodes kept, 8 added, 6 lever nodes replacing the
  `pol-inst` placeholder). `bands`, `edges`, `marks` and `responsibility` are never touched.
- Map page rebuilt: 22 policy nodes, and it now shows UU 27/2026, PP 6/2025, POJK 11, Stranas KA, PEKA,
  RP3I and the six levers.

**Revert:** clear the hyperlink/textFormatRuns on the ranges above (they all previously held plain text);
delete `ind-pojk11-padk1` from `'Indonesia policy inventory'!A17:M17`; `git checkout` the map JSON + page
to restore the 9-node policy view.

### Bank AI shock model sheet (v0.2 -> v0.3b), 28 Nov
Instruction: update `1GdULcdyhkJRwzTLH7xcFP4xnLC5tYFHnk-5vaGduTSE` from the local
`SPAR_Indonesia_Bank_AI_shock_model_v0.3b.xlsx` where it needs data.

Method: cell-level diff of all 15 tabs, then write only where v0.3b carries something the sheet lacks
or carries a sourced correction. **55 cells written.**

- `Feed_Panel` 49 cells: hires/leavers per bank now filled from each bank's 2025 sustainability report
  (GRI 401-1) - E5:F12 and the missing B/C headcount+date cells for Mandiri, BTN, BSI; headcount and
  as-of corrections for BNI (27,201 Dec 2025), BCA (26,435), CIMB Niaga (10,775), KB Bank (2,334);
  basis column now cites the report rather than Kontan/ID-12; `Status` 'Needs feed' -> 'Observed' for
  Mandiri, BTN, BSI; notes carry page references.
- `Data_Feed` 6 cells: D4, E4, D7, E7, D14, E14 status lines now describe the fed state.

Deliberately NOT written: `Inputs`, `Scenarios`, `Moody_Scenarios` (their differences are formatting -
0.034 vs 3.4% - not data), `Summary` and `Model_*` (already identical and formula-driven), and the
formula columns `Feed_Panel` H/I (recomputed by the sheet itself: per-bank attrition 3.9 / 8.3 / 3.3 /
16.0 / 45.5 / 7.4 / 2.0 / 6.2%, panel 6.11%).

Effect: panel headcount 150,523 -> 218,129; 2030 headcount under the three scenarios now 216,951 /
210,346 / 191,884 (was 150,523 / 145,940 / 133,131); Extreme still shows 602 cumulative layoffs.

**Revert:** re-paste v0.2 values into `Feed_Panel!D5:F12`, `Feed_Panel!B6:C12`, `Feed_Panel!K10:K12`,
`Feed_Panel!L5:L12`, `Data_Feed!D4:E4`, `Data_Feed!D7:E7`, `Data_Feed!D14:E14` from the v0.2 export;
the formula columns recalculate on their own.

### Model sheet rename + id-shock-data p6 append, 28 Nov
- **Renamed** the model spreadsheet: title `SPAR Indonesia - Bank AI shock model v0.2` -> `... v0.3b`.
  Revert: set the title back.
- **Appended** `id-shock-p6-new.tsv` (27 rows, 31 columns) to Core file `id-shock-data` at
  **A13:AE39**, after checking the header matched the existing schema column for column and that no
  `id` or `match_key` already existed. The tab now holds 38 evidence rows (run3: 11, p6: 27).
  All 27 are M1 / S6 / ID-12 - bank-level hires, leavers and turnover - and they agree with the panel
  now in `Feed_Panel`: BRI 12,070 new hires and 3,323 leavers appear in both.
  Revert: clear `id-shock-data!A13:AE39`.

### Feed_Panel turnover columns (model sheet), 28 Nov
Instruction: wire voluntary turnover alongside total turnover for what the model does not use yet.

Added **M4:O12** - `Total turnover rate (feed)`, `Voluntary turnover rate (feed)`, `Turnover basis /
note` - filled from the p6 rows in Core `id-shock-data` (BRI 5.58% / 1.24%; BNI 1.9%; BCA 3.4%;
Mandiri 3.53%) with the counts-only banks left blank and the calc stated in the note column.
Nothing existing was changed; the checked-empty guard refused to write if M:O had held data.
Revert: clear `Feed_Panel!M4:O12` (model sheet `1GdULcdyhkJRwzTLH7xcFP4xnLC5tYFHnk-5vaGduTSE`).

