# Indonesia signals — source matrix (why each indicator tallies to Ian's skeleton)

**What this is.** The verification pass for the **`signals` tab of the Core file**
(`1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k`) against the team skeleton
**`SPAR_signals_skeleton` → `SIGNALS`** (`1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo`,
signals **S1–S10** in three layers: capability · adoption · labour).

**Why it is needed.** The Core file already carries `ian_signal` (S-codes) and
`measure (Akbar)` (M1–M6) on every row — that is the *mapping*. What the Meta rules ask
for and what is still missing is the **source**: Meta rule 5 says *"link = the public
source, not a Drive link."* No public URL is recorded on any of the 22 signal rows yet.
This matrix closes that gap and states, per row, **why the tally holds** — and where it
only partly holds.

**Rule followed.** Consistent with AI-driven change, never "caused by AI" — every row
carries its alternative explanation. Nothing here invents a number: figures come from the
row text (Akbar's evidence note) or the cited source. Cells marked **VERIFY** are the ones
to confirm in Perplexity / BoxCompute before the row is called final.

Last checked: 2026-11-24 · CRO draft, uncommitted.

---

## Source keys

| Key | Public source |
|---|---|
| **BPS-SAKERNAS** | BPS Sakernas (national labour force survey, Aug round) — press release: https://www.bps.go.id/id/pressrelease/2026/11/05/169961/tingkat-pengangguran-terbuka--tpt--sebesar-4-75-persen---rata-rata-upah-buruh-sebesar-3-42-juta-rupiah.html · table portal: https://www.bps.go.id/id/statistics-table |
| **BPS-INFORMAL** | BPS Sakernas employment status (formal/informal) — same BPS portal, Feb round |
| **OJK-SPI** | OJK Statistik Perbankan Indonesia (monthly; branch/office counts, credit, labour cost): https://ojk.go.id/id/kanal/perbankan/data-dan-statistik/statistik-perbankan-indonesia/default.aspx |
| **PASKER** | Kemnaker vacancy portals — Pasker ID: https://paskerid.kemnaker.go.id/ · Karirhub: https://karirhub.kemnaker.go.id/ |
| **KEMNAKER-PHK** | Kemnaker Satudata — pekerja ter-PHK: https://satudata.kemnaker.go.id/data/kumpulan-data/3010 |
| **BPJS-JKP** | BPJS Ketenagakerjaan JKP programme + reporting: https://www.bpjsketenagakerjaan.go.id/jaminan-kehilangan-pekerjaan.html · claims news https://www.bpjsketenagakerjaan.go.id/berita/29487/... · financial statements 2025 https://www.bpjsketenagakerjaan.go.id/assets/uploads/laporan_keuangan/LK_LPP_2025.pdf |
| **ILO-WP140** | Gmyrek, Berg & Bescond, *Generative AI and Jobs: A Refined Global Index of Occupational Exposure*, ILO Working Paper 140: https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure |
| **MS-DIFFUSION** | Microsoft AI Economy Institute, *Global AI Diffusion Report*: https://www.microsoft.com/en-us/corporate-responsibility/topics/ai-economy-institute/reports/global-ai-diffusion-report/ |
| **BANK-DOC** | Local evidence artifact: `Bank AI deployment and worker support in Indonesia` (shared Drive folder `1WW-Af6uO5_k9MQeHpnbIqjqvyeHo0-el`) |
| **BCA-SR25** | BCA Sustainability Report 2025: https://pustaka.bca.co.id/ESG/2026/File/20260212-SR25-BCA-EN.pdf (**VERIFY** the 2025 training figure against the PDF's page) |
| **BRI-AR25** | BRI Annual Report 2025: https://bri.co.id/documents/20123/56786/Annual%20Report%20BRI%20Tahun%202025_English%20Version.pdf (**VERIFY** Sabrina interaction share) |
| **PP6-2025** | PP No. 6 of 2025 (JKP benefit reform, effective 7 Feb 2025) — JDIH/Setkab |
| **AKBAR-DECK** | `Akbar Indonesia.pdf` (shared deck, p2–4) — origin of the baselines |

---

## The matrix — 22 rows

**S-layer key:** S1 capability · S2–S4 adoption · S5–S10 labour.
**Status:** ✅ supported · ◐ partly supported · ⭘ gap (nobody collects it yet).

| # | id | Signal | Akbar | Source | Why the tally holds | Status |
|---|---|---|---|---|---|---|
| 1 | ind-sig-sakernas | **S5 Hiring rate** + S7 (employment/hours by industry) | M1 | **BPS-SAKERNAS** | Sakernas is the anchor series for the sector's employment, hours and pay by industry *and* carries occupation codes — it is the denominator every other indicator is read against. | ✅ |
| 2 | ind-sig-ilo-exposure | **S1 Capability milestone** | M1 | **ILO-WP140** | Provides task-level exposure mapped onto standard occupation codes, so "what current tech can do" is measured on the same occupational grid as Indonesian employment. | ✅ |
| 3 | ind-sig-baseline-exposure | **S1 Capability milestone** | M1 | **ILO-WP140** + **AKBAR-DECK** | 21.7% of jobs above minimal exposure, 93.9% of clerical support workers with some exposure — the concentration that makes clerical finance the right watch-point. | ✅ |
| 4 | ind-sig-baseline-sector-size | **S5 + S6 + S7 (baseline)** | M1 | **BPS-SAKERNAS** | 1.65m employed in financial & insurance activities (Aug 2025) sizes the exposure base; it sets the ceiling for any S5–S7 movement. | ✅ |
| 5 | ind-sig-bank-ai-usecases | **S2 Employers' AI targets** | M2 | **BANK-DOC** (BCA, Mandiri, BRI, BNI, CIMB Niaga annual/sustainability reports) | Named production deployments (DIVA, VIRA, Kopra, Sabrina, BRIBRAIN, risk scoring) are exactly the S2 evidence type — employer-stated intent tied to cost or headcount. *Alternative explanation:* disclosure is PR-legible; some use-cases are pilots. | ◐ — status/start date per use unconfirmed |
| 6 | ind-sig-baseline-genai-use | **S2 Employers' AI targets** | M2 | **MS-DIFFUSION** | Diffuse worker-side GenAI use (11.7% → 12.7% of working-age population through 2025, per Akbar's note) is the demand-side context that makes employer S2 targets credible. *Caveat:* it is population use, not firm adoption — keep it as context, not as S3. | ◐ |
| 7 | ind-sig-bank-ai-training | **S10 Training demand** (internal upskilling) | M2 | **BANK-DOC** + **BCA-SR25** | BCA: 2,550 employees in AI-related training during 2025 — loggable as training supply from inside the firm. *Limits:* says nothing about roles changed, redeployed or eliminated. | ◐ — one bank only |
| 8 | ind-sig-contact-centre-share | **S1 + S2 (proxy — never S7)** | M2 | **BRI-AR25** | BRI Sabrina handled 45% of 21,535,701 Contact BRI interactions; unanswered 9.33% → 4% (2024→2025); users 4.31m → 5.85m. Capability is *demonstrated at scale* in a clerical task. *Explicit guard:* service/usage, not jobs saved or lost — do not read as S7. | ◐ — proxy only |
| 9 | ind-sig-karirhub | **S5 Hiring rate** | M3 | **PASKER** (+ repo report `/build/spar-id-postings.html`, 2,618 postings 2024→Oct 2026) | Vacancy postings by title, employer and date are the S5 spine — hiring moves before headcount, so this is the earliest labour reading. *Limits:* totals and shares only; full extract to request from Kemnaker. | ✅ |
| 10 | ind-sig-bank-function-hiring | **S2 → S5 (M2/M3)** | M3 | **PASKER** + **OJK-SPI** + bank reports | Would time function-specific vacancies/hires/exits against confirmed production deployment. Today: candidate early-warning, **not** observed hiring collapse. The "20% year-on-year for two quarters" figure in the source doc is **illustrative only** — do not publish it as a threshold. | ⭘ |
| 11 | ind-sig-jkp-claims | **S8 Unemployment-benefit claims** | M4 | **BPJS-JKP** | Claims after eligible layoffs are the institutional trace of job loss, independent of firm announcements. *Limits:* occupation/industry detail unconfirmed. | ◐ |
| 12 | ind-sig-jkp-cases-v-recipients | **S8 Unemployment-benefit claims** | M4 | **BPJS-JKP** (financial statements / integrated reports) | 237,550 (2023) · 250,594 (2024) · 431,086 (2025) payment cases vs 57,960 (2024) · 90,513 (2025) distinct recipients — the row that **stops the two denominators being confused**. *Caveat:* payment cases can recur for the same worker. | ◐ |
| 13 | ind-sig-jkp-rejections | **S8 (access friction)** | M4 | **BPJS-JKP** — May 2025 parliamentary hearing | 17% of JKP applications rejected for incomplete/invalid documentation: measures friction in the claim path, which is what determines whether S8 shows the shock at all. *Caveat:* one reporting period, not a year rate. | ◐ |
| 14 | ind-sig-jkp-reform-break | **S8 (structural-break caveat)** | M4 | **PP6-2025** | PP 6/2025 (eff. 7 Feb 2025) changed generosity, claim timing and contribution conditions — so pre/post-2025 JKP levels are **not** comparable. *Caveat:* higher claims may reflect access take-up or duration, not job losses. | ✅ (as a documented break) |
| 15 | ind-sig-jkp-processing-time | **S8 extension (M5 service friction)** | M5 | **BPJS-JKP** — needs applications → approvals → first payment by cohort (median/p90) | Latency is the readiness indicator: it detects service-capacity bottlenecks during a surge. Reviewed public evidence does **not** establish operational waiting times. | ⭘ |
| 16 | ind-sig-jkp-training-outcomes | **S10 → S9** | M5 | **KEMNAKER-PHK** + **BPJS-JKP** — need slots, starts, completions, wait times, placements, 3/6-month earnings | Placement effectiveness for former bank workers is the question the row exists to answer; PEKA participation does not establish it. | ⭘ |
| 17 | ind-sig-peka-training | **S10 Training demand** | M5 | **BPJS-JKP** (BPJS announcements, Aug 2026) | 1,426 benefit recipients across 45 locations (entrepreneurship/livelihood, incl. families and heirs) — a concrete catalogue of activity. *Limits:* not proof of nationwide retraining capacity or of stable post-training earnings. | ◐ |
| 18 | ind-sig-jkk-rtw | **Not aligned — JKK ≠ JKP** (S9 caution) | M5 | **BPJS-JKP** | 97.30% return-to-work is the **JKK** work-injury rehabilitation outcome. Logged explicitly so it is never read as a JKP placement rate or as an AI-displacement outcome. | ✅ (as a caution row) |
| 19 | ind-sig-branch-footprint | **S7 Office and branch footprint** | M2 | **OJK-SPI** (branch/office counts) + **BANK-DOC** s.B/E | Bank branch and office counts are published monthly, so net change is observable. Current read: **unobserved candidate** — no paired closure-by-function series extracted. *Alternative explanation:* online migration, property cost, consolidation ≠ AI. | ◐ source exists · ⭘ linkage |
| 20 | ind-sig-worker-destinations | **S9 Worker destinations** | M4 + M6 | *(none — this is the stated gap)* | No public series gives next employer, occupation, formal/informal status, hours or wage after job loss. JHT withdrawals are **not** a substitute (they also cover resignation and retirement). | ⭘ |
| 21 | ind-sig-gap-adoption-hires | **S2 → S5 (bridge)** | M2 | *(none — this is the stated gap)* | No public series links workplace AI adoption to hires, wages, output and tax bases. Name it on the record rather than proxy it. | ⭘ |
| 22 | ind-sig-baseline-informal | **S9 Worker destinations** | M4 + M6 | **BPS-INFORMAL** | Feb 2026: 87.74m informal vs 59.93m formal workers — payroll and JKP capture only part of the labour market, so a finance-sector shock can move household spending without showing in JKP at all. | ✅ |

### Counts

- **Supported (✅):** 8 — rows 1 Sakernas · 2 ILO exposure · 3 exposure baseline · 4 sector size · 9 Karirhub · 14 JKP reform break *(as a documented break)* · 18 JKK caution *(as a caution row)* · 22 informal baseline
- **Partly (◐):** 9 — rows 5, 6, 7, 8, 11, 12, 13, 17, 19
- **Gap (⭘):** 5 — rows 10 same-function hiring after deployment · 15 JKP processing latency · 16 JKP training outcomes · 20 worker destinations · 21 adoption↔hires link

**Read-off for the report:** every S-code from S1 to S10 is touched by at least one Indonesian
row except **S3 (AI adoption rate)** and **S4 (Forecast)** — Indonesia has no firm-level
adoption series and no AI-named industry outlook revision. State both as blind spots, not
as absences of the shock.

---

## What to do with this (in order, before 20:00)

1. **Fill the source column.** Add a `link` column to Core file → `signals` and paste the
   public URL per row from the keys above (Meta rule 5: public source, not a Drive link).
2. **Run the five VERIFY cells** in Perplexity / BoxCompute: (a) BCA 2,550 employees in AI-related
   training, 2025; (b) BRI Sabrina — 45% of 21,535,701 Contact BRI interactions, unanswered
   9.33%→4%, users 4.31m→5.85m; (c) JKP payment cases 237,550 (2023) · 250,594 (2024) · 431,086
   (2025) and recipients 57,960 (2024) · 90,513 (2025); (d) JKP 17% rejection rate (May 2025
   hearing); (e) sector size 1.65m (Aug 2025) and exposure 21.7% / 93.9%. Replace each key with
   the page you actually opened.
3. **Mark the five ⭘ rows** as `status=gap` with the "nobody collects yet" wording — these
   are deliverables, not failures.
4. **Hand the ◐ rows** their one-line caveat (already written above) as the row note.

## Blockers found while checking (not yours to fix)

- **`sync-sheets` is failing on every hourly run** (step 5 *Sync tabs to CSV* succeeds,
  step 6 *Commit if changed* fails). Consequence: the repo's `data/*.csv` no longer mirrors
  the sheet — the repo holds **9 signal rows**, the sheet holds **22**. The dashboard and
  the prototype are therefore reading stale data. Lane: CTO / @misshanna_bot (the 9 Nov
  `SYNC_PAT` fix has lapsed — same class of failure as the Cloudflare token `t_7d505a7a`).
- **Cloudflare Pages deploys** last succeeded 22 Oct; the token failure (code 10000) is
  still open, so nothing new is reaching `spar-f26-id.pages.dev`.
