# id-shock-data — column dictionary

One row = **one number, for one indicator, for one period, from one source**.
Append-only. Never overwrite a row; correct it by adding a new row and pointing the old one at it.

Sheet: **Core file → `id-shock-data`**
https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=1470529234

---

## Block A — readable (columns A–P, always visible)

| # | Column | Type | Notes |
|---|---|---|---|
| A | `id` | text | `ind-ev-0001`, sequential, never reused |
| B | `measure (Akbar)` | enum | M1 – M6, see below |
| C | `signal` | enum | S1 – S11, see below |
| D | `indicator_no` | text | key into the indicator table: `ID-15`, `PH-16` |
| E | `layer` | enum | AI uptake · Business · Hiring · Strain and response · Jobs and pay · Spillover |
| F | `indicator` | text | the data series, one series per row |
| G | `the number` | number or text | as published; `tbc` when not obtainable — never a guess |
| H | `unit` | text | people · postings · branches · claims · IDR · % · sq m · months |
| I | `period` | text | as published: `Jun 2025`, `Q1 2026`, `Jan–Aug 2026`, `as at 30 Jun 2025` |
| J | `what this tells us` | sentence | plain reading of *this* number **and what it does not say** |
| K | `why it matters` | sentence | link to the shock thesis; copy intent from the indicator table's "Why this indicator" |
| L | `verified?` | enum | `Yes` · `Partly` · `No` · `Contradicted` |
| M | `checked on` | date + who | `2026-11-27 — CRO/BoxCompute` |
| N | `confidence` | enum | `H` · `M` · `L` |
| O | `possible other factors` | text | the alternative explanations. Mandatory. Never leave blank when the number moves |
| P | `priority` | text | from the indicator table: `INDONESIA TOP 5 #4`, `Signal rank 1`, `Gap` |

## Block B — technical (columns Q–AE, hide the block for reading)

| # | Column | Type | Notes |
|---|---|---|---|
| Q | `source` | text | publisher or document name |
| R | `source URL` | url | the exact page, API endpoint or file — not a homepage |
| S | `release cadence` | text | monthly · quarterly · annual · twice yearly · one-off · continuous |
| T | `history back to` | year | earliest year the series covers |
| U | `threshold` | text | trigger or decision threshold, if the indicator has one |
| V | `forecast question` | text | the 2027 / 2030 question the series is meant to answer |
| W | `how we counted it` | enum | `table` · `filing` · `stated by publisher` · `pages × per-page` · `news claim` · `derived` |
| X | `access barrier` | enum | `public` · `paywalled` · `insider` · `not published` |
| Y | `ground row` | text | `id` of the record that confirms this one (blank on ground rows) |
| Z | `match key` | text | `entity\|indicator\|period`, lowercase, no spaces |
| AA | `saved copy` | text | local path + sha256 of the page/PDF actually read |
| AB | `captured on` | date | ISO |
| AC | `captured by` | text | BoxCompute job name |
| AD | `origin` | enum | `Akbar` · `CRO/BoxCompute` · `ID team` · `PH team` · `Natraj` · `Napat` |
| AE | `real or demo` | enum | `real` · `demo` |

---

## Controlled vocabularies

**Measures (Akbar's six)**
- `M1` Sector employment and exposure
- `M2` AI deployment and workforce change
- `M3` Recruitment and vacancies
- `M4` Job loss and worker destinations
- `M5` Worker support capacity
- `M6` Consumption and fiscal effects

**Signals**
- `S1` Capability milestone
- `S2` Employers' AI targets
- `S3` AI adoption rate
- `S4` Forecast
- `S5` Hiring rate
- `S6` Layoffs and closures
- `S7` Office and branch footprint
- `S8` Unemployment-benefit claims
- `S9` Worker destinations
- `S10` Training demand
- `S11` Spillover *(proposed — M6 currently has no signal; do not use until approved)*

**Crosswalk**

| Measure | Signals | Typical indicator_no |
|---|---|---|
| M1 | S1, S6 | ID-01, ID-13 |
| M2 | S2, S3, S10 | ID-04, ID-05, ID-06, ID-24 |
| M3 | S5 | ID-09 |
| M4 | S6, S8, S9 | ID-11, ID-12, ID-17, ID-21, ID-22 |
| M5 | S8, S10 | ID-19, ID-23, ID-25 |
| M6 | S11 (proposed) | none yet |

## Verification rules

1. `Yes` — a ground source states the number, and the row names the file, table and period that do so.
2. `Partly` — the number is stated but a known caveat qualifies it (revised monthly, shares of respondents, one conflicting figure).
3. `No` — single press mention, or the page could not be opened and the value came from a search excerpt.
4. `Contradicted` — two sources disagree. Keep **both** values in separate rows, each with the other's `id` in `what this tells us`.
5. A news item is never confirmed by another news item. Two outlets quoting one press release is still `No`.
6. `confidence` is about the source, not about how much you like the number: `H` official/audited, `M` survey or single reputable outlet, `L` excerpt-only or unnamed methodology.

## Non-negotiables

- No `tbc` replaced by an estimate. If it is derived, `how we counted it = derived` and the arithmetic goes in `what this tells us`.
- No row without a `source URL` or an explicit `not published`.
- No PII, no login-walled scrapes, no individual job postings.
- Every number that moves gets `possible other factors` filled — that column is the difference between evidence and advocacy-by-assertion.
