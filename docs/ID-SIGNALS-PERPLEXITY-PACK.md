# Indonesia signals — Perplexity verification pack

**Prepared for:** Shafira (SPAR Fall 2026 · Economic Shock Team · Indonesia Data Lead)
**Prepared:** 24 November 2026 · **Deadline:** today 20:00 MYT
**Companion file:** `docs/ID-SIGNAL-SOURCE-MATRIX.md` (the drafted answer — this pack is the *task list* to finish it)

---

## 0. How to use this file

Upload this file to Perplexity (Pro / Deep Research) and run the blocks **in order**. Block A is
the five figures that must be confirmed today. Block B is the source line for all 22 rows. Block C
verifies the five gaps really are gaps. Block D closes the two blind spots. Block E gives you the
interview question.

Every answer you get back goes into the Core file → `signals` tab as a new `link` column (Meta
rule 5: **the public source, not a Drive link**).

---

## 1. What the work is

SPAR Fall 2026 (Economic Shock Team) is testing one finding: **AI uptake and hiring move first,
jobs and pay next, and job-loss claims and official unemployment last.** Indonesia's anchor sector
is **banking and finance**. Indonesia contributes 22 indicator rows to the team's indicator table.

The team's signal skeleton — `SPAR_signals_skeleton` tab `SIGNALS` — defines **ten signals in
three layers**:

| Code | Signal | Layer |
|---|---|---|
| S1 | Capability milestone — a model/product can now do a whole clerical task end-to-end | capability |
| S2 | Employers' AI targets — employer links AI to cost savings or headcount | adoption |
| S3 | AI adoption rate — share of firms that use or plan to use AI | adoption |
| S4 | Forecast — industry body or regulator revises its jobs/revenue outlook and names AI | adoption |
| S5 | Hiring rate — entry-level vacancies and new-hire rate (moves before headcount) | labour |
| S6 | Layoffs and closures — a firm announces AI-linked job cuts or closes a site/branch | labour |
| S7 | Office and branch footprint — offices/branches shrink | labour |
| S8 | Unemployment-benefit claims — new job-loss benefit claims from the sector | labour |
| S9 | Worker destinations — where people go after leaving: informal work, or out of the labour force | labour |
| S10 | Training demand — sector workers sign up for AI or reskilling programmes | labour |

Indonesia's rows are also tagged to the six measures used in the midterm workbook:
**M1** sector employment & exposure · **M2** AI deployment & workforce change · **M3** recruitment
& vacancies · **M4** job loss & worker destinations · **M5** worker support capacity ·
**M6** consumption & fiscal effects.

### Rules — hold Perplexity to these

1. **Wording:** write "consistent with AI-driven change", never "caused by AI". Every row carries
   an alternative explanation (there can be many causes for one incident).
2. **Confidence tag:** **H** = official statistics, company filings, industry body ·
   **M** = named press reporting, surveys · **L** = anonymous reports, vendor-commissioned work.
3. **Primary over secondary.** BPS, OJK, Kemnaker, BPJS Ketenagakerjaan, JDIH/Setkab, ILO, IMF,
   World Bank beat any news article that reports them. Indonesian-language sources are fine and
   preferred where the English version lags.
4. **No invented links or figures.** If a number cannot be confirmed, the answer must say
   **"not verified"** and give the closest primary source, not a plausible substitute.
5. **Every checkable figure needs:** the number, the source page, the release date, and the unit.
6. **Public sources only. No personal data.** Aggregates and shares only, never raw individual ads.

---

## 2. Block A — confirm these five figures first (highest priority)

Each is currently sourced from a local evidence document or a shared deck, not from a public page.
Confirm the number and replace the source with the page you actually opened.

| # | Figure to confirm | Currently sourced from | What to return |
|---|---|---|---|
| A1 | **BCA: 2,550 employees** received AI-related training during 2025 | local doc *Bank AI deployment and worker support in Indonesia* | BCA Sustainability Report 2025 (or annual report) — page number, exact phrase, H/M/L tag. If the wording is "digital" or "technology" training rather than AI, say so — the classification matters. |
| A2 | **BRI Sabrina: 45%** of **21,535,701** Contact BRI interactions; unanswered questions **9.33% → 4%** (2024 → 2025); users **4.31m → 5.85m** | local doc | BRI Annual Report 2025 — the exact page and table. Confirm whether "handled" means fully automated (no human) or contained in the AI channel. |
| A3 | **JKP payment/claim cases: 237,550 (2023) · 250,594 (2024) · 431,086 (2025)** and separately **distinct recipient workers: 57,960 (2024) · 90,513 (2025)** | local doc, from BPJS 2024–25 integrated reports | BPJS Ketenagakerjaan integrated report / financial statements — confirm both series and confirm they are **not** interchangeable (cases can recur for the same worker). |
| A4 | **17% of JKP applications rejected** (incomplete/invalid documentation), May 2025 parliamentary hearing | local doc | The hearing record (DPR / Komisi IX) or BPJS statement — date, denominator, and whether it covers one reporting period only. |
| A5 | **Sector size 1.65 million employed** in financial & insurance activities (August 2025) and exposure **21.7%** of jobs above minimal exposure / **93.9%** of clerical support workers with some exposure | shared deck `Akbar Indonesia.pdf` p2–4; ILO method | BPS Sakernas August 2025 for the sector size (also give the formal/informal split if published); ILO Working Paper 140 for the exposure figures. State the exposure threshold used. |

---

## 3. Block B — the public source line for all 22 rows

For **each** row return the six fields: `status` (supported / partly supported / gap) ·
`source URL` · `what the source actually says` (verbatim figure + release date) ·
`access` (public / registration / paid / request from agency) · `frequency` (monthly/quarterly/annual) ·
`history back to` (first year available).

| Row | id | Signal(s) | Measure | What it measures | Verification question for Perplexity |
|---|---|---|---|---|---|
| 1 | ind-sig-sakernas | S5 Hiring rate; S7 (employment/hours by industry) | M1 | Employment, hours and pay by industry, with occupation codes | Give the BPS Sakernas series for **financial and insurance activities**: employment, hours, and average wage, August round, and the first year the sector breakdown is available. Is the sector split published down to occupation (ISCO/ KBJI) codes? |
| 2 | ind-sig-ilo-exposure | S1 Capability milestone | M1 | Task-based AI exposure mapped to standard occupation codes | Confirm ILO Working Paper 140 (Gmyrek et al., *Generative AI and Jobs: A Refined Global Index of Occupational Exposure*) provides Indonesia-level or occupation-level exposure figures and the mapping to ISCO-08. Give the paper's own stated limits. |
| 3 | ind-sig-baseline-exposure | S1 | M1 | 21.7% of jobs above minimal exposure; 93.9% of clerical support workers with some exposure | Give Indonesia's exposure distribution from ILO WP140 (or the closest published figures) with the threshold definition. If Indonesia is not separately published, say so. |
| 4 | ind-sig-baseline-sector-size | S5, S6, S7 (baseline) | M1 | 1.65m employed in financial & insurance activities, Aug 2025 | Confirm from BPS Sakernas August 2025 (or the nearest August round). Give the formal vs informal split within the sector if published. |
| 5 | ind-sig-bank-ai-usecases | S2 Employers' AI targets | M2 | Named AI use-cases in annual/sustainability reports of BCA, Bank Mandiri, BRI, BNI, CIMB Niaga (DIVA, VIRA, Kopra, Sabrina, BRIBRAIN, transaction risk scoring) | Find the report page for **each** of the five banks naming the AI system, and whether it is in production or a pilot. Give the year it was announced. If a system cannot be traced to a primary report, mark it unconfirmed. |
| 6 | ind-sig-baseline-genai-use | S2 | M2 | GenAI use rose from 11.7% to 12.7% of the working-age population across 2025 (Microsoft estimate) | Confirm from Microsoft's AI Economy Institute diffusion reporting: Indonesia's share of working-age adults using generative AI, and the two dates compared. Is there an Indonesian national equivalent (BPS/APJII) with a firmer sampling frame? |
| 7 | ind-sig-bank-ai-training | S10 Training demand (internal upskilling) | M2 | BCA: 2,550 employees in AI-related training, 2025 | See A1. Also: does any other Indonesian bank publish an AI/technology training headcount for 2025? |
| 8 | ind-sig-contact-centre-share | S1, S2 (proxy — never S7) | M2 | BRI Sabrina handled 45% of 21,535,701 Contact BRI interactions; unanswered 9.33%→4%; users 4.31m→5.85m | See A2. Also find whether BRI publishes contact-centre **headcount or staffing** alongside it — that is the piece needed before this can ever speak to jobs. |
| 9 | ind-sig-karirhub | S5 Hiring rate | M3 | Vacancy postings with job titles, employers, dates | For Kemnaker Pasker ID / Karirhub: is there a public statistics page or an open-data extract of vacancy counts by month and occupation? What does Kemnaker charge or require for a detailed extract? Is there an archived view (Internet Archive) usable for a time series? |
| 10 | ind-sig-bank-function-hiring | S2 → S5 (M2/M3) | M3 | Function-specific vacancies/hires/exits timed against confirmed AI deployment | Does **any** Indonesian source publish hiring or separation by occupation *within* banking, timed to a system rollout? If none, name the closest proxy and who holds the data. |
| 11 | ind-sig-jkp-claims | S8 Unemployment-benefit claims | M4 | Claims after eligible layoffs | Does BPJS Ketenagakerjaan publish JKP claims by **industry or occupation** (i.e. can financial-sector claims be isolated)? Request route: what does BPJS require for a sector-level breakdown? |
| 12 | ind-sig-jkp-cases-v-recipients | S8 | M4 | Cases vs distinct recipients: 237,550 / 250,594 / 431,086 vs 57,960 / 90,513 | See A3. Return the exact definitions BPJS uses for "case/payment" vs "recipient", so the two are never divided into each other. |
| 13 | ind-sig-jkp-rejections | S8 (access friction) | M4 | 17% of applications rejected for documentation | See A4. Is there a full-year rejection rate anywhere, and any breakdown by reason? |
| 14 | ind-sig-jkp-reform-break | S8 (structural-break caveat) | M4 | PP No. 6 of 2025 (effective 7 Feb 2025) changed generosity, claim timing, contribution conditions | Confirm the effective date, the three changes, and that it creates a break in comparability across 2024/2025. Cite JDIH/Setkab, not a news summary. |
| 15 | ind-sig-jkp-processing-time | S8 extension (M5 service friction) | M5 | Applications → approvals/rejections → first payment, by cohort, median/p90 days | Is any operational waiting-time figure published (annual report, Ombudsman/ ORI report, DPR hearing, BPJS service-standard disclosure)? If none, say "not published" and name the request route. |
| 16 | ind-sig-jkp-training-outcomes | S10 → S9 | M5 | Training applications, slots, starts, completions, wait times, placements, 3/6-month earnings | Does Kemnaker or BPJS publish post-training employment or earnings outcomes for JKP recipients — and specifically for ex-bank workers? If not, is there an evaluation (LPEM UI, SMERU, World Bank, ILO) that measures it? |
| 17 | ind-sig-peka-training | S10 Training demand | M5 | Aug 2026: 1,426 benefit recipients across 45 locations (entrepreneurship/livelihood, incl. families and heirs) | Confirm the announcement, date, and scope. Is there a cumulative national figure (total PEKA participants) to put the 1,426 in proportion? |
| 18 | ind-sig-jkk-rtw | Not aligned — JKK ≠ JKP (S9 caution) | M5 | 97.30% return-to-work for the JKK rehabilitation programme, 2025 report | Confirm the 97.30% figure and its denominator (work-injury / occupational-disease cases entering rehabilitation), so it is never read as a JKP placement rate. |
| 19 | ind-sig-branch-footprint | S7 Office and branch footprint | M2 | Bank branch and office counts | From OJK Statistik Perbankan Indonesia: bank office/branch counts by year (and by bank if published). Also: do banks state a reason for closures in annual reports (digital migration, cost, consolidation)? |
| 20 | ind-sig-worker-destinations | S9 Worker destinations | M4 + M6 | No public series gives next employer, occupation, formal/informal status, hours or wage after job loss | Verify the gap: is there **any** Indonesian linked employer–employee or post-displacement follow-up source (BPJS JHT withdrawals, Sakernas flows, academic panel data)? Explain why JHT withdrawals are not a substitute. |
| 21 | ind-sig-gap-adoption-hires | S2 → S5 (bridge) | M2 | No public series links workplace AI adoption to hires, wages, output and tax bases | Verify the gap: does **any** Indonesian firm-level survey link AI adoption to employment or wage outcomes (BPS survey, Bank Indonesia survey, LPEM, world bank firm survey)? Name what exists and what it misses. |
| 22 | ind-sig-baseline-informal | S9 Worker destinations | M4 + M6 | Feb 2026: 87.74m informal vs 59.93m formal workers | Confirm from BPS (Sakernas Feb 2026 or nearest round) and give the same split for the financial & insurance sector. Why does this matter? Payroll and JKP cover only part of the labour market. |

---

## 4. Block C — the five gaps (verify they are genuinely gaps)

For each, the answer must be either **(i)** "no public source exists — closest proxy is X, held by Y,
request route Z" or **(ii)** a source, in which case the row moves from gap to partly supported.

| Gap | Row | What to search for |
|---|---|---|
| G1 | ind-sig-worker-destinations | Any Indonesian post-displacement destination series (LinkedIn/job-board flows, BPJS JHT, academic panel) |
| G2 | ind-sig-gap-adoption-hires | Any Indonesian firm-level AI-adoption-to-employment link |
| G3 | ind-sig-jkp-processing-time | Any published JKP approval/payment latency |
| G4 | ind-sig-bank-function-hiring | Any banking hiring/separation published by occupation or function |
| G5 | ind-sig-jkp-training-outcomes | Any placement/earnings outcome measured for JKP training |

---

## 5. Block D — the two blind spots (S3 and S4)

- **S3 — AI adoption rate.** Indonesia's rows currently have no firm-level adoption series. Is there
  a national or regulator-published share of **firms** using AI (BPS survey, OJK/BI survey, APJII,
  Kominfo/Komdigi)? Microsoft's figure is population use, not firm adoption — do not let the two be
  treated as the same signal.
- **S4 — Forecast.** Has any Indonesian industry body or regulator (PERBANAS, OJK, BPS, Bappenas)
  revised a banking employment or revenue outlook **and named AI** as a reason? If no such statement
  exists, that is a finding about the state of the policy conversation, not an evidence gap to fill.

---

## 6. Block E — the one interview question (BPS or Kemnaker)

Requested by the plan: *"ask BPS or Kemnaker about data gaps in one interview."*

> "For financial and insurance activities, you publish employment, hours and pay, and you publish
> vacancies through Pasker ID/Karirhub. What is **not** published is where dismissed finance workers
> go next — their next occupation, formal or informal status, hours and wage — and no series links
> workplace AI adoption to hires or wages. Are either of those collected at any level, even
> internally? If a researcher requested the sector-level breakdown, what would the route and
> conditions be?"

Return: whether the question is answerable, by whom, and what the request route is.

---

## 7. Source keys (start here — verify, don't assume)

| Key | Source | URL |
|---|---|---|
| BPS-SAKERNAS | BPS Sakernas, August round (national labour force survey) | https://www.bps.go.id/id/statistics-table |
| BPS-INFORMAL | BPS employment status (formal/informal) | https://www.bps.go.id/id/statistics-table |
| OJK-SPI | OJK Statistik Perbankan Indonesia (monthly) | https://ojk.go.id/id/kanal/perbankan/data-dan-statistik/statistik-perbankan-indonesia/default.aspx |
| PASKER | Kemnaker vacancy portals | https://paskerid.kemnaker.go.id/ · https://karirhub.kemnaker.go.id/ |
| KEMNAKER-PHK | Kemnaker Satudata — workers affected by layoffs (PHK) | https://satudata.kemnaker.go.id/data/kumpulan-data/3010 |
| BPJS-JKP | BPJS Ketenagakerjaan JKP programme + reporting | https://www.bpjsketenagakerjaan.go.id/jaminan-kehilangan-pekerjaan.html |
| ILO-WP140 | ILO Working Paper 140 — refined global index of occupational exposure | https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure |
| MS-DIFFUSION | Microsoft AI Economy Institute — AI diffusion reporting | https://www.microsoft.com/en-us/corporate-responsibility/topics/ai-economy-institute/reports/global-ai-diffusion-report/ |
| BCA-SR25 | BCA Sustainability Report 2025 | https://pustaka.bca.co.id/ESG/2026/File/20260212-SR25-BCA-EN.pdf |
| BRI-AR25 | BRI Annual Report 2025 | https://bri.co.id/documents/20123/56786/Annual%20Report%20BRI%20Tahun%202025_English%20Version.pdf |
| PP6-2025 | PP No. 6 of 2025 — JKP benefit reform, effective 7 Feb 2025 | JDIH / Setkab (search "PP 6 2025 JKP") |

**Local files you already hold** (Perplexity cannot open these — paste the figure, not the file):

| File | Where | What it gives you |
|---|---|---|
| `docs/ID-SIGNAL-SOURCE-MATRIX.md` | repo `webdevsha/spar-f26-id` | the drafted answer to all 22 rows |
| *Bank AI deployment and worker support in Indonesia* | shared Drive folder `1WW-Af6uO5_k9MQeHpnbIqjqvyeHo0-el` | where every bank figure in the sheet came from |
| `Akbar Indonesia.pdf` (p2–4) | shared Drive folder | baselines: sector size, exposure, informality |
| Core file `signals` tab | Sheets id `1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k` | the 22 rows as they stand |
| `SPAR_signals_skeleton` | Sheets id `1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo` | S1–S10 definitions and the README rules |
| `build/spar-id-postings.html` | repo (public) | 2,618 Karirhub postings 2024 → Oct 2026, the S5 evidence |

---

## 8. Output format to ask Perplexity for

One table, 27 rows, no prose:

```
block | row_id | status (supported/partly/gap) | source URL | figure_verbatim | release_date |
access (public/registration/paid/request) | frequency | history_back_to | confidence H/M/L |
alternative_explanation | notes
```

Then a short section listing: **(a)** anything that could not be verified, **(b)** every source that
turned out to be secondary when a primary exists, **(c)** any figure that contradicts the number
currently in the sheet — flag the contradiction rather than quietly replacing it.
