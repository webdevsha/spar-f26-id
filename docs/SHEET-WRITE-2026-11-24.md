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
