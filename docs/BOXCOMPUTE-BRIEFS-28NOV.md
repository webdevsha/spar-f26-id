# BoxCompute briefs — 28 November 2026

Four paste-ready briefs for the open collection items. Each one assumes the **seven files in
`docs/boxcompute-kit/`** are attached, and each states its own output rule.

Shared rules for all four:

> Output one row per number in the attached `id-shock-data` schema — **31 columns**, `real or demo = real` —
> with `source`, `source URL`, `saved copy`, `captured on`, `captured by`, `verified?` and `confidence`
> filled. Where a figure is paywalled, blocked or absent, **record a row saying so**: a recorded gap is a
> result. Never infer a number; if you compute one, put the arithmetic in `how we counted it`. Public
> documents only, no personal data, one request per second per host, robots.txt respected, no login,
> paywall or CAPTCHA bypass.

---

## Brief 1 · BPS — everything we cannot reach through a browser

**Why this is one job:** `bps.go.id` returns **403** to plain fetches and a Cloudflare bot wall to headless
browsers; Firecrawl times out. Every BPS figure in the register is currently press-sourced, which is why it
carries confidence M.

**Targets**
1. **TPT (open unemployment), August 2026** — the press release *"Tingkat Pengangguran Terbuka (TPT) sebesar
   4,75 persen"*, 5 Nov 2026. We hold 4.75% via press; confirm from the release itself, with the released
   PDF (`BRS`) as the saved copy.
2. **Informal share, August 2026** — 57.93% / 85.73 m informal, 62.25 m formal. Confirm against the same
   release or the Sakernas tables.
3. **Finance and insurance employment (KBLI K), August 2026** — **ID-13, still `tbc`**. We use 1.62 m from
   secondary reporting. Want the Sakernas table row, by sex if published.
4. **Wage, finance and insurance, August 2026** — Rp5.35 m is single-outlet. Want the BPS table.
5. **Underemployment and youth unemployment** — 12.84 m (8.68%) and 17.50% are both press-sourced.

**Access notes to try, in order:** the `BRS` PDF path on `bps.go.id/pressrelease/...`; the `statistics-table`
API endpoint behind the table pages; the mirror at `satudata.kemnaker.go.id` for the KBLI K cut (Kemnaker
republishes Sakernas tables). Microdata is paid and out of scope — **record the paywall, do not buy.**

**What it unlocks:** every macro figure in the report moves from M to H, and ID-13 stops being `tbc`.

---

## Brief 2 · The gated whitepaper (ID-05's only remaining hole)

**The document:** *Digital Sovereign AI and the Future of Trusted Banking* — PERBANAS × IBM × K&A,
**34 pages**, launched 27 Oct 2026, English and Bahasa. Landing page `kiantara.com/whitepaper`; the download
sits behind a form requiring an **office email** (`go.kiantara.com/sovereign-ai-whitepaper`).

**What to look for inside, in priority order**
1. **Any per-institution or per-tier breakdown of the 34 / 18 / 4 / 12% stage split** — KBMI tier, asset
   size, or respondent role. This is the single thing that would fill `Feed_Panel`'s empty AI-stage column.
2. **The five maturity dimensions** (all between 2.66 and 2.82) with their individual scores.
3. **The readiness model's five levels** and how banks were placed on them.
4. **Policy mapping section** — which instruments banks actually cited, in what proportions (we hold PDP Law
   54, POJK 11/2022 49, SEOJK 29/2022 33, OJK AI guide 43, all out of 91).
5. Any statement about **workforce, headcount, roles or skills** — even a sentence. We expect none, and a
   documented absence is itself a finding for the report's "no AI instrument carries a labour clause" line.

**Rule:** do not submit a personal email or create an account. If the gate cannot be passed without one,
**record the gate** (URL, date, what it asks for) and stop.

---

## Brief 3 · Bank flows back to 2015 — the history ID-12 claims

**Why:** the team indicator table says ID-12's history goes back to 2015. We hold **2024 and 2025 only**, for
eight banks. Without the series, ID-12 is a snapshot presented as a trend.

**Targets, per bank** — BRI, BNI, BCA, CIMB Niaga, KB Bank, Mandiri, BTN, BSI:
1. **Total employees, year-end, 2015–2023** — annual report employee notes or sustainability reports.
2. **New hires and leavers per year, 2019–2023** — GRI 401-1 tables. Note the definition used (permanent vs
   total, including contract and retirement).
3. **Voluntary vs total turnover**, wherever a rate is published separately.
4. **BRI's employee count under one definition** — bank-only (84,949) vs group (>119,000). State which the
   report uses and why.
5. **BNI's leavers** — reconcile **1,324** (GRI 401-1) vs **2,254** (our panel) vs the stated **1.9%** rate
   (which implies ~4.9% on 27,201 staff). Three numbers, at most one right.

**Output:** one row per bank-year-metric, `period` = the financial year, `unit` naming the definition
(`employees, year-end, bank-only`). Flag any year where the definition changed — BRI changed turnover
methodology in 2024 and the series is not comparable across it.

---

## Brief 4 · Job-board totals and fill status — the two things S5 needs

**Why:** S5 counts vacancies and cannot see what filled them. Two separate errands, both public.

**A · Sector totals from the boards that block us.** Jobstreet (403), Indeed (503), Karir.com,
KitaLulus, Pintarnya, LinkedIn ID — for each: total postings and **finance/banking postings**, by month,
2024-01 to 2026-11. Our corpus covers Dealls, Glints and Kalibrr; these are the six channels it lacks.
Where a site blocks, **record the block** with the status code and date — a documented block is why the
register says "no sector total exposed".

**B · Fill status, from Pasker ID or any board that shows it.** For a sample of finance/banking vacancies:
was the ad closed, when, and is a hire recorded? Even 50 rows with a close-date would let us estimate the
first fill-rate for Indonesian bank vacancies — the measurement this study is missing.

**Rule:** no scraping behind a login, no CAPTCHA solving, no personal data of recruiters. If a board's
robots.txt disallows the path, stop and record it.

---

## What to do with the output

Append to **`id-shock-data`** in the Core file (rows go after `ind-ev-0130`), then run
`bash scripts/verify-all.sh` before anyone reads a number off it. The pre-flight checks in
`docs/PREFLIGHT.md` apply: header compare, duplicate check, empty-cell guard, grain check, revert range.
