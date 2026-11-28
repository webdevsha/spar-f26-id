# BoxCompute run #1 — what it found, and what it says we cannot use

**28 Nov 2026 · digest of `id-shock-run-report-r1.md` · rows appended: `ind-ev-0107`–`0116`**

Run #1 built 107 rows; 38 were already in the register, and **10 are new** — now appended, so
`id-shock-data` holds **48 evidence rows** (`ind-ev-0069`–`0116`).

## What the 10 new rows are

| id | Measure | Indicator | The number | Verified? |
|---|---|---|---|---|
0107 | M1 | ID-02 Sabrina | 45% of interactions | **Contradicted** |
0108 | M1 | ID-02 Sabrina | 9.1 million interactions | **Contradicted** |
0109 | M1 | ID-15 offices | 21,035 (Mar 2025) | **Contradicted** |
0110 | M1 | ID-15 offices | 23,538 (Jun 2025) | **Contradicted** |
0111 | M2 | PH-06 firms using AI | 14.9% | **Contradicted** |
0112 | M2 | PH-06 firms using AI | about 3% | **Contradicted** |
0113 | M4 | ID-21 informal | 57.93% (Aug 2026) | Partly |
0114 | M4 | ID-22 TPT | 4.75% (Aug 2026) | Partly |
0115 | M5 | ID-20 wage | Rp5.35 million (Aug 2026) | No |
0116 | M1 | ID-13 finance employment | tbc | No |

Six of the ten are **contradiction pairs kept side by side** — the register now records both readings of
three series rather than picking one silently. That is the additive rule doing its job.

## Values that moved against the team indicator table

| Indicator | Table says | Run says | Basis |
|---|---|---|---|
ID-22 open unemployment | 4.68% (Feb 2026) | **4.75%** (Aug 2026) | press coverage of BRS; BPS page bot-blocked |
ID-21 informal share | 59.42% (Feb 2026) | **57.93%** (Aug 2026) | same |
ID-20 finance wage | Rp5.05m (Feb 2026) | **Rp5.35m** (Aug 2026) | single outlet, headline only |
ID-12 bank headcount | BRI 84,949; BNI 26,935 | **BNI 27,201; BCA 26,435; BTN 11,414; CIMB 1,729 leavers** | six bank reports |

⚠️ Those four are **not yet reflected in the team table** — the lane's call, not a quiet edit.

## Three contradictions worth understanding

1. **BRI Sabrina.** SR 2025 p.95 gives **45% of 21,535,701** interactions (≈9.69m). The table carries
   **9.1m** from the annual report — and the run searched both the 870-page AR and the 298-page SR:
   **the figure is not there.** Both rows kept.
2. **OJK office count.** 21,035 (Mar 2025) vs 23,538 (Jun 2025) — three months apart and *rising* by 2,503
   in a series that otherwise falls. A **definition break, not a trend**; a third series (portal, ~3,400/mo)
   is not comparable with either. Never chain or sum them.
3. **PIDS adoption.** 14.9% of firms vs "about 3% across industries" in the same release — most likely two
   units (any-tool firm share vs industry-level rate), not an arithmetical error.

## Still blocked, and by what

| Indicator | Blocker |
|---|---|
ID-13 finance/insurance employment | bps.go.id returns **403**, bot-verification wall headless; microdata **paywalled (USD 444 Aug 2025, USD 129 Feb 2026)** |
ID-09 job boards | Jobstreet **403**, Indeed **503**, robots-disallowed or query ignored — no sector total exposed |
ID-17 JKP audited figures | the LK/LPP 2025 PDF is **single-page, no text layer**; no OCR attempted |
ID-02 9.1m Sabrina | absent from both BRI PDFs |
PH-06 "about 3%" | wording absent from the saved PIDS release; secondary reporting only |

## The list to keep in front of the team: unsafe to quote as-is

- **BTN 1.96% turnover** — 802 hires and 224 exits against a headcount *fall* of 1,433; not a separations
  measure at all.
- **BRI 5.58% turnover** — methodology changed in 2024; not comparable with 2023's 3.24%.
- **CIMB Niaga ~16% churn** — an order of magnitude above peers; never average with BNI/BRI/BCA.
- **Fifth Third 3,508 hires / 16.4%** — a **US bank** filed in the same folder. Not Indonesia. Never summed.
- **Any OJK office series** — three definitions in circulation.
- **BPS Aug 2026 figures** — press-sourced, primary page blocked; verify against the BRS before publication.
- **PIDS 3%** — secondary reporting only; do not attribute to PIDS without the discussion paper.

## One integrity gap the report itself raised — unresolved

The run assumed the highest existing id was `0106`. It warns that rows **`ind-ev-0001`–`0068`** (nine
pre-existing platform rows plus 59 run-1 rows) were **not in the export it received**. Our register starts at
`0069`, so those 68 rows are **not in the tab**. Either they sit in a file we have not seen, or they were
never appended anywhere. **Nothing is lost from today's work** — the 10 new rows are appended and sequenced
correctly — but the register is currently 68 rows short of what the run believes it built. Worth resolving
before the next append.

## Housekeeping done by the run

`sources-registry.json` extended 50 → 63 entries (nothing removed); raw copies with sha256 under
`feed/id-shock/raw/<indicator_no>/2026-11-28-*`; one request per second per host; robots.txt respected;
no login, paywall or CAPTCHA bypassed.
