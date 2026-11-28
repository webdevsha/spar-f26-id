# Where the Drive corpus data goes — grain decides the tab

**28 Nov 2026 · CRO for Shafira · Indonesia lane**
Short answer: **not into `id-postings`, and not a copy of its header.** The corpus is a different grain.
Three grains need three homes, and only one of them is a new tab each.

---

## 1 · Why `id-postings` cannot hold it

`id-postings` is **posting-level**: one row per advertisement, **17,196 rows × 36 columns** — `rec_id`,
`source`, `posted_at`, `title`, `employer`, `sector`, `content`, `ai_skill_required`, `ai_tier`,
`salary_shown`, `url`, `verified_status`… It was built around our own karirhub/Dealls scrape.

The corpus delivers three things, none of which fit that shape:

| Corpus layer | Grain | Rows | Why it breaks `id-postings` |
|---|---|---|---|
`postings_clean.csv` | one row per posting, **101 columns** | ~1.0 m | Would force 65 columns to stay blank, or overwrite our own fields. Also 818 MB with employer contact details — cannot go in a public repo. |
`exposure_monthly.csv` + `monthly_indicators.csv` | **country × platform × month** | 592 | There is no month column in `id-postings`, and one ad row cannot hold a monthly total. |
`exposure_class.csv` | **country × job category** | 30 | It is not about a posting at all; it is a score for a category. |

Adding a monthly row into a posting-level table would corrupt every count anyone ever runs on it — the
tab's whole value is that each row is one ad. **A new tab with the same header fails for the same reason**:
the data has no `rec_id`, no `title`, no `url`, and needs columns the header does not contain
(`month`, `mean_exposure`, `comparable`, `panel_break`).

**The rule I'd hold to:** *grain decides the tab.* Sort by "what is one row?", never by "what topic is it?"

---

## 2 · The three homes

### A · `id-postings` — unchanged
Posting-level, ours. 17,196 rows. Nothing from this corpus enters it.

### B · `postings-monthly` — **new tab, to build**
One row per **country × platform × month**.

| Column | From | Note |
|---|---|---|
`country` · `platform` · `segment` · `month` | `monthly_indicators.csv` | `month` as `YYYY-MM` |
`postings` | same | count of ads |
`bpo_share` · `finance_share` · `ai_share` · `ai_title_share` | same | the sector and AI-skill shares |
`open_ads` · `n_classes` · `mean_exposure` · `exposed_g2_g4_pct` · `comparable` | `exposure_monthly.csv` | joined on country × month (country-level, so it repeats per platform — mark it `country_level=1`) |
`panel_break` | derived | **1 when the month has fewer than 100 ads** |
`source_file` · `corpus_run` · `captured_on` | derived | provenance, every row |

**Load-ready file:** `data/postings-corpus/clean/monthly-platform.csv` — **592 rows, 17 platforms**.
**And** `monthly-country.csv` — **59 rows, 31 months, 2 countries** for the country-level series only.

### C · `postings-exposure` — **new tab, to build**
One row per **country × category**, plus a second block for occupations.

| Column | From | Note |
|---|---|---|
`country` · `category` · `classification` | `exposure_class.csv` | category kept verbatim, `classification` is the slug |
`exposure` · `exposed_g2_g4_pct` | same | the score that gives banking **0.582** |
`cards` | same | ad counts behind it |
`source_file` · `corpus_run` · `captured_on` | derived | provenance |

**Load-ready file:** `data/postings-corpus/clean/exposure-category.csv` — **30 rows**.
Occupations (`isco2_postings_vs_employment.csv`, 259 rows) belong in the same tab as a second block, or as
`postings-occupation` if the team prefers one grain per tab.

---

## 3 · Cleaning — yes, and it is already done

Five rules, applied and logged:

| Rule | What it does | Result |
|---|---|---|
**R1 window** | keep only 2024-01 → 2026-11 | `exposure_monthly`: 63 → **59 rows** (4 dropped) |
**R2 comparable / panel break** | flag any month with **<100 ads** | **306 of 592** platform-months flagged — half the platform series is too thin to trend |
**R3 grain** | never mix posting-level with monthly-level | enforced by keeping three files apart |
**R4 taxonomy** | category kept **verbatim** plus a mapped slug | no renaming, so our labels and theirs can be reconciled later |
**R5 provenance** | `source_file`, `corpus_run`, `captured_on` on every row | every figure traceable to a file |

Two cleaning steps deliberately **not** done, because they are team decisions:

1. **Interns.** The corpus separates `interns` from `non_intern` (Dealls 2024: 405 of 6,087). Counting interns
   as demand would inflate entry-level hiring — the exact place a shock shows first.
2. **Platform panels.** Glints ID has 35,666 ads in 2025 and **8** in 2026. Whether to drop the platform,
   or keep it flagged, changes the trend. My recommendation: keep, flagged, never aggregate without the flag.

---

## 4 · What stays on Drive, permanently

`postings_clean.csv` (818 MB, 101 columns) · `postings_text.jsonl` (455 MB) · `scope_jobs.csv` (1 GB) ·
`cc_fetch_text.jsonl` (358 MB) · **81,320 archived HTML pages (3 GB)**.

Two reasons, and neither is disk space: the repo is **public**, and raw ad text carries employer names and
contact details. If per-posting corpus data is ever needed inside the repo, the move is a **new
`postings-corpus-raw` tab with only the fields an analysis actually uses** — never the full 101.

---

## 5 · The cross-check this makes possible

Our `id-postings` is karirhub-derived; the corpus covers JobStreet, Dealls, Glints, Bossjob and 13 more.
Overlapping platforms (Dealls, Glints) let us ask a question nobody has answered for Indonesia: **do two
independent harvests of the same platform produce the same monthly shape?** If yes, S5's postings series
has a validation; if no, one of them is measuring its own crawler. That is worth one small comparison table
once the two tabs exist — and it would be the second real validation in the study, after the census check.
