# BoxCompute run prompt — SPAR AI × economic shock (Indonesia), evidence collection into `id-shock-data`

Copy everything below the line into BoxCompute. Attach the five files listed in **Attachments** before you run it.

---

## MISSION

You are collecting **published economic evidence** on how AI adoption in Indonesia's finance sector is changing work, and writing it as rows into one Google Sheet tab. You are not writing analysis, not writing a report, and not drawing conclusions. You are producing a defensible, re-checkable record that a researcher can audit line by line.

Project: SPAR F26 — *From AI Exposure to Economic Shock*, Indonesia (with the Philippines as a comparison set). Anchor sector: finance and insurance, principally banks. Anchor workforce: clerical and routine banking roles.

Two frameworks run on every row, and every row must carry both:

- **Akbar's six measures** — `M1` sector employment and exposure · `M2` AI deployment and workforce change · `M3` recruitment and vacancies · `M4` job loss and worker destinations · `M5` worker support capacity · `M6` consumption and fiscal effects
- **The project's ten signals** — `S1` capability milestone · `S2` employers' AI targets · `S3` AI adoption rate · `S4` forecast · `S5` hiring rate · `S6` layoffs and closures · `S7` office and branch footprint · `S8` unemployment-benefit claims · `S9` worker destinations · `S10` training demand · `S11` spillover *(proposed, do not use unless a human approves)*

Crosswalk: M1→S1,S6 · M2→S2,S3,S10 · M3→**S5** · M4→S6,S8,S9 · M5→S8,S10 · M6→S11 (has no signal yet — record such rows with `signal` blank and flag them in the run report).

## ATTACHMENTS

1. `idph-2-indicator-table.csv` — the indicator spine. 50 indicators (ID-01…ID-25, PH-01…PH-25) with signal, layer, source, URL, cadence, history depth, latest known value, threshold, forecast question, priority and known caveats. **This is the authority on what to collect.** Do not invent indicators that are not in it.
2. `idph-1-collection.csv` — the evidence log as it stands, with checking notes and confidence ratings. Use it to avoid re-finding what is already verified, and to see the reconcilable conflicts.
3. `column-dictionary.md` — the 31 columns, their order (A–AE), controlled vocabularies and verification rules. **Follow it exactly.**
4. `akbar-indonesia-data-measures.pdf` — the six measures in their original framing, including the paywall and access caveats.
5. `sources-registry.json` — 50 seeded registry entries keyed by indicator number, each with URL, cadence, access barrier and method. You will extend this file, not replace it.

## OUTPUT CONTRACT

**Target:** the Google Sheet `Core file`, tab `id-shock-data`.
`https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=1470529234`

- **One row = one number, for one indicator, for one period, from one source.**
- Never one row per article. An article that reports three numbers produces three rows.
- **Append-only.** Never edit or delete an existing row. To correct one, append a new row and name the superseded `id` in `what this tells us`.
- Row 1 is the header and must not change. Continue `id` numbering from the highest existing `ind-ev-` value.
- If you cannot write to the Sheet, emit a CSV with the identical 31 columns and say so in the run report.

## WHAT TO COLLECT IN RUN #1 — in this order

**P1 · Refresh the nine platform totals (M3 / S5 / ID-09).** Nine rows already exist (`ind-ev-0001`…`ind-ev-0009`) — do **not** duplicate them; add today's snapshot alongside. Capture for each: Jobstreet Indonesia, Karir.com, Indeed Indonesia (sector queries — empty queries return nothing), Glints, Kalibrr, Dealls, Loker.id, TopKarir, Karirhub Kemnaker. Record the total exactly as the platform displays it, plus the query used. Where a platform exposes no total, write `tbc`, `how we counted it = not exposed`, and describe what a pagination walk would require. Kalibrr must be split ID/PH before any figure is usable.

**P2 · OJK Statistik Perbankan Indonesia (M2/M4 / S7 / ID-15).** The table carries commercial bank offices at 23,538 (Jun 2025) and notes *"data after Jun 2025 moved to the OJK portal and was not retrieved."* Close that gap: monthly offices and bank population from Jul 2025 to the latest release, from SPI Table 1.42.a and successors. Each month is its own row. Also look for labour/headcount columns while you are in the file.

**P3 · Kemnaker Satudata — PHK (M4 / S6 / ID-11).** Monthly layoff notifications from 2022 to the latest month, national, plus a finance/insurance split if published. Note in `possible other factors` that monthly figures are revised upward for up to six months, and mark the October 2026 labour-law change as a break in the series. This is also the confirmation source for trigger `ind-trg-fin-clerical-01` — record province and quarter so a future matching pass can use them.

**P4 · BPJS Ketenagakerjaan — JKP (M4, M5 / S8 / ID-17, ID-19).** Claim counts, recipients, payout, rejections, and any published processing time. The table has 90,513 workers / Rp1.01tn for 2025 and a stated 3-working-day standard with no achieved figure. Distinguish *claim cases* from *distinct recipients*; they are not the same and the table already warns about it. Mark PP 6/2025 (effective 7 Feb 2025) as a structural break — higher claims may mean wider access, not more job loss.

**P5 · BPS — sector size and pay (M1, M4 / S6, S9 / ID-13, ID-20, ID-21, ID-22).** Pull the KBLI K (finance and insurance) row of Sakernas — the table marks 1.65 million as team-reported and unverified. Also Feb/Aug 2026 employment, unemployment, formal/informal split and average wage. Public tables and news releases only: **microdata is paywalled (USD 444 Aug 2025, USD 129 Feb 2026) — do not attempt to acquire it, record `access barrier = paywalled`.**

**P6 · Bank filings (M2 / S2, S3 / ID-04, ID-12, ID-24).** For BCA, BRI, BNI, Mandiri, BTN, BSI, CIMB Niaga, Permata, Danamon: headcount, branch count, AI-training headcount, named AI systems, contact-centre automation share. Annual and interim reports from 2022; prioritise 2024–2026. Headcount is the highest-value number in the whole tab — it is sector-specific and every listed bank publishes it.

**P7 · Reconcile three known conflicts** (each becomes its own row with `verified? = Contradicted`):
- BRI Sabrina: 45% of 21,535,701 interactions (Sustainability Report 2025) vs 9.1m interactions in the annual report — 45% of 21.5m is about 9.7m.
- OJK offices: 23,538 (Jun 2025 series) vs a Kontan figure of 21,035 for Mar 2025.
- PIDS adoption: 14.9% of firms vs "about 3% across industries" in the same press release.

## VERIFICATION — the rule that makes this worth doing

- `Yes` only when a ground source states the number, and the row names the file, table and period.
- `Partly` when stated but qualified — shares of respondents, revised series, one conflicting figure.
- `No` for a single press mention, or when the page could not be opened and the value came from a search excerpt. Say which in `checked on`.
- `Contradicted` when sources disagree: **both values get rows**, neither is deleted.
- **A news item is never confirmed by another news item.** Two outlets quoting one release is still `No`.
- `confidence`: `H` official/audited · `M` survey or single reputable outlet · `L` excerpt-only or unnamed method.
- If a match cannot be made, leave `ground row` blank rather than guessing a link.

## NEVER

- Never replace `tbc` with an estimate. If you compute a number, set `how we counted it = derived` and put the arithmetic in `what this tells us`.
- Never write a row without a `source URL` or an explicit `not published`.
- Never scrape behind a login, paywall, or CAPTCHA. Never collect personal data, CVs, candidate profiles, or individual job postings.
- Never sum across sources with different definitions (Kemnaker PHK ≠ BPS employment change ≠ bank annual-report headcount). Record them separately.
- Never state that AI caused a change. `possible other factors` is mandatory on every row where a number moves — earlier digitalisation, branch consolidation, cost of funds, macro conditions, policy changes, portal attrition.
- Never use `S11` unless a human has approved it.

## HOUSEKEEPING

- Save every page, PDF or API response you actually read to `feed/id-shock/raw/<indicator_no>/<YYYY-MM-DD>-<slug>` and record path + sha256 in `saved copy`.
- Rate limit: one request per second per host. Respect robots.txt.
- Extend `sources-registry.json` with anything new you find; never remove entries.
- Formatting, if you touch it: light theme only, no dark fills, no coloured headings.

## RUN REPORT — end every run with this

1. Rows added, split by measure (M1–M6) and by `verified?`.
2. Indicators where the latest value **changed** since the attached indicator table, old → new.
3. Indicators still `tbc` or `No`, and exactly what is blocking each: login · paywall · portal down · series discontinued · no public source.
4. Contradictions found this run.
5. Anything that makes a row unsafe to quote, in one line each.

**Definition of done for run #1:** P1 refreshed with a dated snapshot for every platform that exposes a total; P2 and P3 complete from the last verified month to the latest release; P4 and P5 filled with whatever is publicly available; P6 attempted for at least BCA, BRI, BNI and Mandiri for 2025; P7 written as three `Contradicted` rows; run report emitted.
