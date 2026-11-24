# Indonesia signals — source matrix (v2, Perplexity-grounded)

**What changed.** v1 (24 Nov, CRO draft) drew the source line from local artefacts — Akbar's shared
deck, the *Bank AI deployment* doc, my own reading of the primaries. **v2 replaces that with the
Perplexity verification run** (`data/id-postings/perplexity-id-data.md`, 24 Nov): 22 rows, a public
URL per row, the verbatim figure, an H/M/L tag, and — importantly — an explicit list of what is
**still not verified**. Everything below is transcribed from that run; nothing is added to it.

**How to read it.** ✅ supported · ◐ partly supported · ⭘ gap · **NV** = not verified in this run.

**The one rule this run enforces:** an unverified figure stays written as *not verified*. It is not
replaced, and it is not quietly kept. Several numbers currently sitting in the sheet without a source
fall into that class — they are listed in §1.

---

## 1. Corrections to apply before anything else (this is the real output)

### 1a. Status changes against the v1 draft

| Row | v1 said | v2 says | Why |
|---|---|---|---|
| `ind-sig-branch-footprint` | ◐ / ⭘ | **✅** | OJK SPI publishes the count table directly — “1.42.a. Perkembangan Jumlah Bank Umum dan Kantor Bank Umum”. Source line supported; specific office values **NV**. |
| `ind-sig-jkp-processing-time` | ⭘ gap | **◐** | **v1 was wrong.** BPJS publishes a service standard: payment “paling lama 3 (tiga) hari kerja”, SLA 3 working days. The *achieved* median/p90 is **NV** — that is the gap, not the standard. |
| `ind-sig-jkp-training-outcomes` | ⭘ gap | **◐** | **v1 was too strong.** ILO's implementation review reports “21 … reskilling … and 39 have employment placement” (2022). Aggregate placement reporting exists; training-linked, earnings-linked outcomes are **NV**. |
| `ind-sig-worker-destinations` | ⭘ gap | **◐** | **v1 was too strong.** Retrospective Sakernas variables (previous industry/occupation, reason and date of leaving) have supported destination research (2019–2022). A current banking-worker longitudinal series is **NV**. |
| `ind-sig-baseline-sector-size` | ✅ | **⭘ / NV** | 1.65 million and its formal/informal split are **NV**. The correct primary is BPS *Keadaan Angkatan Kerja* (all employed), not *Keadaan Pekerja*. |
| `ind-sig-jkk-rtw` | ✅ (as caution) | **⭘ / NV** | 97.30%, its year, numerator and denominator are all **NV**. Keep it out of the register until located in the JKK/RTW section of the BPJS integrated report. |
| `ind-sig-bank-function-hiring` | ⭘ | **⭘ confirmed** | World Bank–Bappenas OEVS collects occupation-level flows coded to KBJI, but banking coverage and rollout linkage are **NV**. |
| `ind-sig-gap-adoption-hires` | ⭘ | **⭘ confirmed** | No qualifying joined Indonesia dataset located; World Bank technology-adoption survey is the closest instrument. |
| `ind-sig-baseline-genai-use` | ◐ | **◐, confidence L** | Microsoft Q1 2026 report, appendix p.17: Indonesia 11.7 → 12.7 → **14.1%** (H1 2025, H2 2025, Q1 2026). Vendor telemetry, not a probability sample → **L**. Add the 14.1% point. |
| `ind-sig-bank-ai-usecases` | ◐ | **◐** | Five-bank audit incomplete; Kopra ≠ proof of a specific deployment; rollout dates and production/pilot splits **NV**. |

### 1b. Two attribution traps to fix in the sheet

- **BCA “2,550” appears twice.** The employee-training figure is on BCA's *Responsible AI* page. The
  sustainability report also prints **2,550 for suppliers** — that occurrence must never be cited as
  AI-trained employees.
- **DIVA is BCA's** collateral-valuation system. Any attribution to CIMB Niaga is unverified; CIMB's
  public evidence is AI in internal audit, not DIVA.

### 1c. Denominator traps

- **93.9%** is the share of Indonesian **clerical support workers** with exposure — not 93.9% of tasks,
  and not 93.9% of banking jobs.
- **21.7%** is above-minimal exposure, a different denominator from the clerical figure.
- **JKP cases vs recipients** stay separate: 431,086 payments for 90,513 workers (2025); 237,550 cases
  (2023) / 250,594 (2024); 57,960 recipients (2024, from attributed reporting — not an audited table).
  Never divide one by the other.
- **PP 6/2025** (effective 07 Feb 2025; contribution 0.36% of monthly wage; eligibility ≥12 months in
  24) is a comparability break, **not** a measured causal effect on claims.

---

## 2. The verified source line — 22 rows

| id | Status | Source (public) | Verbatim figure | Conf | Still not verified |
|---|---|---|---|---|---|
| `ind-sig-sakernas` | ◐ | BPS, *Keadaan Pekerja di Indonesia, Agustus 2025* | confirms coverage of industry, weekly hours, occupation, monthly wages | H | exact finance-sector figures; published industry × occupation cross-tab; first comparable year |
| `ind-sig-ilo-exposure` | ✅ | ILO Working Paper 140 (Gmyrek et al.) | “four progressively increasing exposure gradients”, ISCO-08 mapping | H | Indonesia-specific figures **inside WP140 itself** |
| `ind-sig-baseline-exposure` | ◐ | ILO national estimate + ILO occupation analysis | Indonesia 21.7% above minimal exposure; clerical support 93.9% | H | full Indonesia gradient distribution; numeric threshold boundaries; the underlying employment vintage |
| `ind-sig-baseline-sector-size` | ⭘ NV | BPS *Keadaan Angkatan Kerja, Agustus 2025* (correct primary) | not verified | H (source) | 1.65 million; formal/informal split |
| `ind-sig-bank-ai-usecases` | ◐ | BCA press release (2025-06-13); BRI AR 2025; Mandiri IR; BNI SR 2025; CIMB Niaga GCG 2025 | DIVA + VIRA named as implemented at BCA; Sabrina launched 2018 (BRI AR p.13); BNI = limited analytical use; CIMB = internal audit | H | BRIBRAIN; named BNI systems; rollout dates; production vs pilot; most exact pages |
| `ind-sig-baseline-genai-use` | ◐ L | Microsoft AI Diffusion Report 2026-Q1, appendix p.17 | Indonesia 11.7% / 12.7% / 14.1% (H1 2025, H2 2025, Q1 2026) | **L** | any BPS/APJII measure with a firmer sampling frame |
| `ind-sig-bank-ai-training` | ◐ | BCA *Responsible AI* page; CIMB Niaga directors' report | “2,550 relevant employees … AI-related training programs” during 2025 | H | page release date; other banks' comparable counts (BNI's MSME AI training is external participants — do not substitute) |
| `ind-sig-contact-centre-share` | ◐ | BRI Sustainability Report 2025, **p.95** | “45% of total 21,535,701 interactions across all Contact BRI channels” | H | unanswered 9.33%→4%; users 4.31m→5.85m; containment; contact-centre headcount or outsourced FTE |
| `ind-sig-karirhub` | ◐ | Pasker ID datasets + monthly dashboard | finance & insurance: 1,195 (2022) · 797 (2023) · 726 (2024) postings; quota 46,556 / 15,962 / 7,334 | H | joint month × occupation × finance extract; extract fees/conditions; usable archive history |
| `ind-sig-bank-function-hiring` | ⭘ | World Bank–Bappenas OEVS technical report; Pasker datasets | not verified | H (source) | any banking-only, rollout-linked hiring/separation series |
| `ind-sig-jkp-claims` | ◐ | BPJS JKP programme page + audited 2025 summary | 90,513 workers via 431,086 payments (2025) | H | industry/occupation tables isolating finance |
| `ind-sig-jkp-cases-v-recipients` | ◐ | BPJS integrated report; 2025 summary; recipient statement | 237,550 (2023) · 250,594 (2024) cases; 431,086 payments / 90,513 workers (2025); 57,960 recipients (2024) | H | formal deduplication method; older case-count definitions; audited recipient table |
| `ind-sig-jkp-rejections` | ◐ **M** | BPJS-hosted RRI/KBRN report of the 20 May 2025 hearing | “angka penolakan klaim … 17 persen” | **M** | denominator; exact cutoff; repeat applications; full-year rate; reason coding. Named speaker: Abdur Rahman Irsyadi (acting director) |
| `ind-sig-jkp-reform-break` | ◐ | Kemnaker JDIH PP 6/2025; BPK legal metadata; official regulation copy | effective 07 Feb 2025; 0.36% of monthly wage; ≥12 of 24 months | H | clause-level old/new benefit + deadline comparison (not certified here) |
| `ind-sig-jkp-processing-time` | ◐ | BPJS official FAQ + 2025 programme summary | JKP payment “paling lama 3 (tiga) hari kerja”; SLA 3 working days | H (standard) | **achieved** median/p90 by cohort; timestamp coverage |
| `ind-sig-jkp-training-outcomes` | ◐ | ILO implementation review (2022-09-13) | “21 participated in the reskilling training and 39 have employment placement” | H | training-cohort linkage; earnings; wait times; ex-bank-worker breakdown |
| `ind-sig-peka-training` | ◐ **M** | BPJS-hosted announcement (ANTARA text) + dated RRI report (2026-08-18) | “1.426 penerima manfaat … di 45 titik seluruh Indonesia” | **M** | absolute release date; cumulative national participation; distinct-person definition |
| `ind-sig-jkk-rtw` | ⭘ NV | BPJS integrated-report archive; programme benefits page | not verified | H (source) | 97.30%; reference year; numerator/denominator |
| `ind-sig-branch-footprint` | ✅ | OJK SPI archive + May 2025 SPI PDF | table “1.42.a. Perkembangan Jumlah Bank Umum dan Kantor Bank Umum” | H | particular office-count values; workshop coverage by bank; coded closure reasons |
| `ind-sig-worker-destinations` | ◐ | Sakernas-based post-separation research (2019–2022); BPS Feb 2026 labour-force publication; BPJS JHT page | not verified (variables documented) | **M** | current finance-specific destination series; next employer; hours/wages after exit |
| `ind-sig-gap-adoption-hires` | ⭘ | World Bank regional AI analysis; PERBANAS–IBM survey statement (2026-10-27) | not verified | **L** (vendor-linked) | any representative firm-adoption × hires/wages/output/tax linkage |
| `ind-sig-baseline-informal` | ◐ | BPS announcement 2026-05-06; BPS *Keadaan Angkatan Kerja, Feb 2026* | “Pekerja formal … 59,93 juta … informal … 87,74 juta” (Feb 2026) | H | finance/insurance formal–informal split; first consistent historical observation |

**Block A (the five figures) in the same run:** A1 BCA 2,550 → **supported** (see the supplier trap) ·
A2 Sabrina 45% → **confirmed p.95**, other two figures NV · A3 JKP series → **confirmed** with the
denominator caveat · A4 17% → **M**, hearing statement, 2025 year-to-date · A5 21.7% / 93.9% →
**supported**; the 1.65m sector size is **NV**.

---

## 3. What is still not verified — and the route to get it

These are **outreach**, not scraping. Each is a formal request to an institution; several are
regulators (see §5).

| # | Item | Holder | Route |
|---|---|---|---|
| 1 | achieved JKP approval → first-payment median/p90; timestamp dictionary | BPJS PPID | official information request; ask for dictionary first, then cohort aggregates |
| 2 | finance-specific JKP claims by KBLI; distinct workers vs payments | BPJS PPID | aggregate claims + coding dictionary + suppression rules |
| 3 | 2024 recipient audited table; case definitions; deduplication method | BPJS PPID | programme data dictionary + annual aggregate tables |
| 4 | hearing transcript/submission behind the 17% figure | DPR Commission IX secretariat; BPJS PPID | 20 May 2025 hearing record |
| 5 | JKK RTW definition and denominator | BPJS JKK/RTW programme owner | integrated-report section + denominator definition |
| 6 | sector employment (all employed), finance hours/wages, formal–informal split, industry × occupation cross-tab | BPS PST | online consultation; aggregate KBLI finance/insurance tables |
| 7 | Sakernas feasibility for a finance post-separation aggregate | BPS PST | ask for questionnaire-routing confirmation + unweighted sample sizes first |
| 8 | joint month × occupation × industry vacancy extract; extract terms | Kemnaker PPID / Pasker ID | postings and quota requested separately |
| 9 | JKP training starts/completions joined to placement and 3/6-month earnings | Kemnaker PPID (+ paper authors) | also obtain Muhyiddin et al. evaluation direct from the corresponding author |
| 10 | banking occupation hiring/exits (existing or new collection) | World Bank OEVS team; then OJK | coverage check first; a new OJK collection is a separate project |
| 11 | representative firm-level AI adoption × employment | BPS / OJK / BI / PERBANAS; World Bank survey team | request instruments, sampling frames, linked outcome fields |
| 12 | AI-named revision of banking jobs/revenue outlook (S4) | PERBANAS / OJK / BPS / Bappenas | dated forecast revisions |
| 13 | five-bank report-page audit; BRIBRAIN; named BNI systems; rollout dates | each bank's investor relations / corporate secretary | system-level disclosure references, not vendor case studies |
| 14 | Contact BRI unanswered-question and user series; contact-centre FTE | BRI Corporate Secretary (`humas@bri.co.id`) | annual tables + definitions |
| 15 | BCA page release date; historical training series; other banks' counts | BCA corporate secretary / IR | — |

---

## 4. The five gaps, as they now stand

| Gap | Verdict after verification | Lead holder | Route | Planning estimate |
|---|---|---|---|---|
| Where dismissed finance workers go next | **Partly — variables exist.** Sakernas records previous industry/occupation, reason and date of leaving, beside current status/occupation/hours/pay. Retrospective, not a tracking panel. | BPS | PST consultation: “previous finance/insurance industry × involuntary separation × current status”, with formality/occupation/hours/pay | 1–2 wks feasibility; 2–6 wks tabulation if accepted |
| Firm AI adoption ↔ hires/wages | **Not verified.** World Bank technology-adoption survey is the starting point; generic digital adoption ≠ AI adoption; employment levels ≠ hiring flows. | World Bank (Indonesia growth & jobs / tech survey team) | request questionnaire + variable dictionary + aggregate feasibility check | 2–4 wks for an availability answer |
| JKP approval → first-payment latency | **Partly.** A published 3-working-day *standard* exists; achieved distribution does not. | BPJS Ketenagakerjaan | PPID request: timestamp dictionary, then monthly cohort aggregates, median/p90, calendar vs working days | 2–4 wks availability; 4–8 wks custom aggregate |
| Hiring by occupation inside banking | **Partly — instrument exists.** OEVS collects firm industry, occupation rosters and hiring needs, but banking coverage is unverified; a historical pilot, not rollout-linked. | World Bank OEVS; then OJK | coverage check + questionnaire fields + sample counts | public reports now; 2–4 wks coverage; 4–8 wks tabulation |
| Placement/earnings outcomes of JKP training | **Yes in a paper, not as a national series.** Muhyiddin et al. report post-reskilling employment and self-reported wage/job-quality outcomes; achieved sample and fieldwork dates are unclear. | Kemnaker (+ paper authors) | paper now; Kemnaker PPID for linked starts/completions → placement → 3/6-month earnings, ex-finance split | paper immediate; 1–3 months for linkage if approved |

**Block E — the interview question, reframed.** Perplexity's verdict: ask it as a **data-availability
and access enquiry**, never as an assumption that data isn't published. Route through BPS PST and the
agency PPIDs and ask what is *collected*, what aggregate joins are feasible, and under what disclosure
conditions.

---

## 5. Why this now needs a @clo pass before it leaves the team

Items 3–5, 8–11 above are **formal information requests to regulators and ministries** — BPJS
Ketenagakerjaan, OJK, Kemnaker, BPS, DPR Commission IX. A request in the study's name creates a
record of who asked, for what, and under what framing. That is a compliance-layer decision, not a
research one: **route the request set to @clo before any of it is sent.** Nothing here has been sent.

---

## 6. What this unblocks in the deliverables

- **Part 3 (what the signals show now, 700w)** — the evidence base is now sourced row by row; the
  shape of the section is: 8 supported · 9–10 partly · 5 gaps, with S3 (firm adoption rate) and S4
  (AI-named forecast) named as blind spots.
- **Part 4 (who can act, policies in place, 600w)** — §3's holder column *is* the who-can-act map, now
  with routes rather than names.
- **`build/spar-id-overview.html`** — carries the portal's own counts (Kemnaker finance postings
  1,195 → 797 → 726) and the coverage check (66 of the portal's 726 finance postings for 2024 ≈ 9.1%),
  plus category exposure scores.
- **`docs/PROMPTS-BOXCOMPUTE-V2.md`** — the collection run to lift coverage; the Pasker ID CSVs are
  already downloaded into `data/kemnaker/`.
