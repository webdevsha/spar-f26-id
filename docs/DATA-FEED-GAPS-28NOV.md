# What still needs feeding — and are ID-05 and ID-12 answered?

**28 Nov 2026 · CRO for Shafira · Indonesia lane**
Audited: model sheet `Inputs` / `Scenarios` / `Data_Feed` / `Feed_Panel`, Core file `signals` (7 rows at
`status=gap`), `readiness` (all `tbc`), `instruments` (cost/speed `tbc`), Core `id-shock-data` (38 rows),
team workbook `2_INDICATOR_TABLE` rows **ID-05** and **ID-12**, and `1_COLLECTION`.

---

## Part 1 · The short answer on your scope

| Your indicator | Verdict | The gap in one line |
|---|---|---|
| **ID-05** — stage of AI adoption in banks | **Not answered enough** | **Zero evidence rows** in the register. The whole indicator rests on one Kontan article about a white paper we do not hold, with no bank-level split and no second point in time. |
| **ID-12** — headcount at large banks | **Nearly there** | 33 evidence rows and all 8 banks, but the team table's `latest value` is **stale**, and the input the model actually needs — **function-level headcount** — is missing. |

Evidence rows in Core `id-shock-data` by indicator: **ID-12 = 33 · ID-17 = 5 · ID-05 = 0.**

---

## Part 2 · ID-05: what to collect

| # | What | Why it closes the gap | Where to look |
|---|---|---|---|
| 1 | **The PERBANAS / IBM / K&A white paper itself** (PDF, Oct 2026) | The 34 / 18 / 4% figures are currently cited to a Kontan write-up. Until we hold the paper we cannot state the sample frame, the definition of "operational", or the response base. | PERBANAS site/publications; IBM Indonesia newsroom; K&A; Kontan/Bisnis articles that name the report title |
| 2 | **Sample frame**: n = 91 is respondents — how many institutions, which tiers (KBMI 1–4), which roles answered | "91 respondents" and "91 banks" are different claims. The register currently says respondents. | same paper, methodology section |
| 3 | **Bank-level adoption stage**, even anonymised by tier | The model's `Feed_Panel` column `AI stage (feed)` is empty for all 8 banks. Without it, adoption timing is a national average applied to every bank. | annual reports, sustainability reports, press releases naming systems (Sabrina, VIRA, DIVA already found) |
| 4 | **A second point in time** — any 2025 or earlier PERBANAS/OJK survey with the same three stages | One point cannot show adoption *speed*, and speed is the Extreme scenario's whole premise. | OJK annual reports, PERBANAS surveys 2023–2025, earlier Kontan/Bisnis coverage |
| 5 | **Cross-check series** already half-held: Microsoft AI diffusion (14.8% Q2 2026), report-ai.org (rank 76/147) | Gives a country-level trend to sanity-check the bank-level stages | already cited in `Context_ID`; needs a second quarter to become a trend |

**What it unlocks:** a defensible `A0` (currently 18%), a second adoption anchor for the scenario fan, and
the ability to say whether Indonesian banks are ahead of or behind the country — which is the claim the
S3 row is *for*.

---

## Part 3 · ID-12: what to collect

| # | What | Status | Where to look |
|---|---|---|---|
| 1 | **Refresh `latest value`** — BNI 27,201 (Dec 2025), CIMB 10,775, KB 2,334, plus Mandiri 38,732, BTN 11,429, BSI 16,274 | **Stale in the team table** (it still says BNI 26,935 Jun 2025, CIMB 10,659 Mar 2026, KB 2,265) — we already hold the correct figures in `id-shock-data` | our own p6 rows; BNI/CIMB/KB/Mandiri/BTN/BSI 2025 reports |
| 2 | **Function-level headcount** (tellers, customer service, back office, credit admin) | **Missing — the model's biggest assumption** (`x` = 30%, no source) | GRI 2-7 in each sustainability report; OJK bank statistics; Sakernas KBJI by KBLI K |
| 3 | **Hires and leavers by year, 2019–2024**, all 8 banks | Only 2024–2025 held; `history back to 2015` is claimed but unbuilt | GRI 401-1 tables in earlier sustainability reports |
| 4 | **One BRI headcount definition** (bank-only 84,949 vs group >119,000) | Open — panel size swings 40% on the choice | BRI annual report employee note |
| 5 | **BNI reconciliation** — 2,254 (panel) vs 1,324 (p6) vs 1.9% (their own rate) | **Unresolved conflict** | BNI SR 2025 GRI 401-1 table, spot-check p.98 |
| 6 | Voluntary vs total turnover for the other six banks | Only BRI and Mandiri publish voluntary | each SR's turnover table |

**What it unlocks:** a real `x` (exposed share) instead of 30% assumed — which is the single assumption
`MODEL-ATTRITION-SENSITIVITY.md` shows can move extreme-scenario layoffs 12.8× — plus the attrition basis
the team can defend.

---

## Part 4 · Everything else still needing a feed

### 4a · Model inputs that are assumptions with no source

| Parameter | Value now | What would source it | What it changes |
|---|---|---|---|
| Exposed share of headcount `x` | **30%** | GRI 2-7 function headcount (ID-12 item 2) | Size of the shock; 12.8× sensitivity |
| Baseline headcount growth `g` | **0%** | Bank plans, credit growth (OJK SPI, BI) | Whether the counterfactual is flat or growing |
| Share of layoffs receiving JKP | **83%** | BPJS rejection statistics by year | JKP cost, and how much of the shock reaches the safety net |
| Matching efficiency `χ` | **0.5** | Calibrate against Sakernas transitions | How fast displaced workers are re-employed |
| Labour-market tightness `θ = V/S` | **0.6** | Vacancies (Pasker ID / Karirhub) ÷ unemployed (BPS) | Job-finding rate, `f(θ)` = 18.8% now |
| Matching curvature `ι` | **1** | Same as above | Shape of the matching function |
| Share of non-finders into informal work | **50%** | Sakernas transitions out of formal finance | Informal vs open unemployment split |
| Finance & insurance employment | **1.65 m** (marked `Needs feed`) | BPS Sakernas sector table | Panel coverage (currently 13.2% of the sector) |

### 4b · Scenario assumptions that need calibration

| Parameter | Slow / Medium / Extreme | What would calibrate it |
|---|---|---|
| Task exposure `e` | 24 / 53 / 82% | ILO index mapped to Indonesian KBJI occupations — global shares are being applied to Indonesian tasks |
| Pass-through `φ` | 62.5 / 66 / 73% | Any firm-level evidence on task automation rates; otherwise keep and label |
| Indonesia probability prior | 40 / 50 / 10% | **Two-round expert elicitation** (the biggest open judgement in the model) |
| Macro-bust overlay `m` | 0% | Portfolio flows, rupiah, imported AI spend — the external-shock channel |

### 4c · Open feeds listed in `Data_Feed` (unchanged)

Headcount by function · one BRI definition · full ID-05 paper · AI system start dates · calibrated `r` ·
Sakernas transitions · vacancies for teller/customer service/back office.

### 4d · Register gaps and unscored rows

**Seven `signals` rows sit at `status=gap`:** JKP reform structural break · worker destinations after exit ·
AI adoption not linked to headcount · JKP approval and payment latency · same-function banking hiring ·
bank branch and office footprint · JKP training slots and waiting time.
**`readiness`:** all six questions still `tbc` — the question texts are not recorded anywhere.
**`instruments`:** cost and speed `tbc` for all six levers.

---

## Part 5 · Ready-to-run BoxCompute brief

Paste this in, attaching the Core `id-shock-data` schema.

> **Mission.** Collect the missing inputs for two SPAR Indonesia indicators, ID-05 (stage of AI adoption in
> Indonesian banks) and ID-12 (headcount at large banks). Output one row per number in the attached
> `id-shock-data` schema — 31 columns, `real or demo = real`, every row with `source`, `source URL`,
> `saved copy`, `captured on`, `captured by`, `verified?` and `confidence`.
>
> **Targets, in priority order.**
> 1. PERBANAS / IBM / K&A AI-in-banking white paper, Oct 2026 — the PDF. Extract: response base, number of
>    institutions, definition of each adoption stage, and every percentage with its denominator.
> 2. The same three-stage adoption split from any earlier survey (2023–2025).
> 3. Function-level headcount from GRI 2-7 for BRI, BNI, BCA, CIMB Niaga, KB Bank, Mandiri, BTN, BSI.
> 4. Hires and leavers (GRI 401-1) for the same eight banks for 2019–2024, plus voluntary vs total turnover.
> 5. BNI's employee-leavers figure — reconcile 1,324 vs 2,254 vs the stated 1.9% turnover rate.
> 6. BRI's employee count under one definition (bank-only vs group).
>
> **Rules.** Public documents only. No personal data. Save the source file for every row. Where a figure is
> paywalled or absent, record a row saying so rather than leaving it out — a recorded gap is a result.
> Never infer a number; if you compute one, put the arithmetic in `how we counted it`.
