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
