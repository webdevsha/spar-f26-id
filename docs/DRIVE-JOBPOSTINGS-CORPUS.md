# The shared Drive job-postings corpus — what it is, how to use it, where it lives

**28 Nov 2026 · CRO for Shafira · Indonesia lane**
Source folder: [`17BpgebhRToagaK8YzB5h4SGQ4z7RYEwy`](https://drive.google.com/drive/folders/17BpgebhRToagaK8YzB5h4SGQ4z7RYEwy)
Aggregates committed to: [`data/postings-corpus/`](../data/postings-corpus/) — **19 files, 211 KB**.

---

## 1 · What it is

A BoxCompute run that scraper-harvested **job advertisements across Indonesia and the Philippines** and
then scored each occupation for AI exposure. Not a survey, not an official series — an **archive** of what
employers advertised.

| Headline | Value |
|---|---|
Total postings | **1,035,176** |
With a full job description | 192,898 |
From job cards only | 842,278 |
Platforms with descriptions | 13 |
Indonesia | 532,583 cards · 152,641 descriptions |
Philippines | 309,695 cards · 40,257 descriptions |
Months covered | **2024-01 → 2026-11** |
ISCO occupations scored | 276 (396 crosswalk rows, 392 mapped) |
Crosswalk confidence | A 234 · B 111 · **C 47** |

The folder holds five layers: `cc_scope_output` and `cc_fetch_output` (Common Crawl scope and fetches —
`scope_jobs.csv` alone is 1 GB), `processed_output` (`postings_clean.csv` 818 MB, `postings_text.jsonl`
455 MB), `exposure_output` (the scored aggregates), `report_output` (JSON summaries), and
`wayback_*` (archive-based counts plus **81,320 cached HTML pages, 3 GB**).

---

## 2 · What it answers for us — file by file

| Our need | File | What it gives |
|---|---|---|
| **The model's exposed share `x` — currently a 30% assumption with no source** | `exposure_class.csv` | **Banking & Financial Services: mean exposure 0.582, and 94.3% of its postings sit in exposure groups G2–G4** (Indonesia; 20,088 cards). Insurance 0.544 · Administration 0.569 · Call centre 0.540 |
| **S5 hiring-rate series** | `exposure_monthly.csv` | A monthly series back to **2023-11**: open ads 35,747 → mean exposure ~0.415 → exposed share 53.9%, with a `comparable` flag per month |
| **AI-skill signal in ads** | `monthly_indicators.csv` | 593 rows × 33 columns: postings, `bpo_share`, `finance_share`, `ai_share`, `ai_title_share`, by platform × month × country |
| **Is the postings mix representative?** | `isco2_postings_vs_employment.csv` | Postings share vs employment share for 259 ISCO-2 groups — shows which occupations are over- and under-advertised |
| **Credibility line for the methodology page** | `exposure_validation.csv` | A crawl estimate checked against a **same-month census**: 0.4127 vs 0.4144, max gradient difference **0.57 pt** (Indonesia, 2025-09) |
| **How good is the title → occupation model?** | `title_model_eval.csv` | Indonesia: 432,897 training titles, 106,974 test, **57.5% exact subcategory, 73.3% broad, exposure MAE 0.051** |
| **Who is advertising** | `employer_concentration.csv` | Per platform: employers, top-5 share, Gini, **`agency_share`** (staffing intermediaries) |
| **What was thrown away** | `timeframe_excluded.csv` | Exclusions by platform and reason: before-window, after-window, stale date, no date |
| **Archive reliability** | `wayback_flags_v2.csv` | 631 flagged rows from the Wayback-based counts |
| **Corpus provenance** | `headline.json`, `inventory.json`, `count_sources.json` | Totals, the platform × year inventory, and how many archived counts exist per level and archive |

---

## 3 · Where it goes

| Layer | Home | Why |
|---|---|---|
**Raw** — `postings_clean.csv` (818 MB), `postings_text.jsonl` (455 MB), `scope_jobs.csv` (1 GB), the 81,320 HTML pages (3 GB) | **Stay on Drive. Never in the repo.** | Two reasons, both hard: the repo is **public**, and raw ad text carries employer names and contact details — committing it would be a personal-data breach, not a size problem. The external-output gate applies before any of it leaves the team. |
**Aggregates** — the 19 files above (211 KB) | **Committed**: [`data/postings-corpus/`](../data/postings-corpus/) | Small, no personal data, and citable in a report. These are what the numbers in a written deliverable should rest on. |
**Not yet pulled** — `sub_totals.csv` (1.5 MB) | Drive, on request | Below the raw layer but above the aggregate layer; pull it when the archive counts are actually used. |

Rule of thumb applied: **if it cannot be printed in a 20-page report, it does not enter the repo.**

---

## 4 · Content analysis — what the corpus actually says

1. **Banking is the most AI-exposed sector in the corpus**, and not by a small margin: mean exposure
   **0.582** with **94.3%** of its ads in G2–G4, against 0.491 for Sales and 0.452 for advertising/media.
   That independently supports the study's whole premise — the sector we chose is the one the exposure
   literature flags.
2. **The estimate is validated, not just asserted.** On the one month with both a census and a crawl,
   the weighted card estimate sits **within 0.57 of a percentage point** of the census. That is the single
   strongest quality claim available anywhere in our evidence base.
3. **The Indonesia series is uneven across platforms.** Glints ID shows **35,666 postings in 2025 and 8 in
   2026**; Indeed shows 1. Any month-on-month reading that mixes platforms is measuring *the crawler*, not
   the labour market. The `comparable` flag in `exposure_monthly.csv` is the guard.
4. **AI-skill demand is a small share of ads** (`ai_share`, `ai_title_share` in `monthly_indicators.csv`) —
   consistent with the register's finding that Indonesian employers rarely name AI in a posting.
5. **Staffing agencies are visible** (`agency_share` per platform). An ad placed by an agency is demand for
   a *placement*, not a named employer's headcount — which is exactly the distinction S5 fails to make.
6. **Postings mix ≠ employment mix** (`isco2_postings_vs_employment.csv`). Advertising skews toward
   white-collar and sales roles; the corpus over-represents the very occupations it scores as exposed.

---

## 5 · Feed needs, gaps and assumptions

### Gaps the corpus cannot close

| Gap | Consequence |
|---|---|
No **filled / not-filled** outcome per ad | A posting is demand, not a hire. S5's blind spot is untouched by this corpus. |
No **wage** field worth using | The JKP cost and wage questions still rest on BPS/Sakernas. |
No **bank-only** split in the monthly series | `finance_share` is finance *and insurance*; banking is only separable at the category level in `exposure_class.csv`. Needs OJK or Pasker ID for a true banking series. |
Indonesia validation covers **two months** (2025-09, 2025-12) and one crawl each | Defensible for those months; not a standing guarantee. |
**47 crosswalk rows at confidence C** | Some categories are mapped loosely — check `crosswalk_scored.csv` before quoting a subcategory figure. |
Platform coverage is **crawl-dependent** | 2026 Indonesia is thin outside JobStreet; Dealls and Glints panels break in-year. |

### Assumptions to state whenever these numbers are used

1. **Advertised ≠ actual demand.** Postings measure what employers chose to publish, on platforms that
   allow crawling.
2. **Deduplication is imperfect.** `dedup_groups.csv` (10 MB, on Drive) records the merges; re-posts inflate
   counts to an unknown degree.
3. **Exposure is a task-based score**, transferred across countries by a title → category model (73.3%
   broad accuracy in Indonesia), not measured displacement.
4. **Cards ≠ descriptions.** Two-thirds of the corpus is job cards (title plus category), so the AI-skill
   analysis rests on the 192,898 descriptions, of which 152,641 are Indonesian.
5. **The Philippines is the comparison lane, not the subject.** PH numbers appear here only to validate the
   method.

### The one immediate use

`exposure_class.csv` gives banking an exposure of **0.582** where the model currently assumes **0.30** —
and `MODEL-ATTRITION-SENSITIVITY.md` already showed that a single assumption moving can multiply extreme
outcomes by 12.8×. Wiring 0.582 in (with the definition stated) is the highest-value change available from
this corpus, and it is a model decision for the team, not a quiet edit by the lane.
