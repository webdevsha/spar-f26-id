# BoxCompute prompt v2 — aligned to the archive-scale study (1,059,854 postings)

**Why v2.** You sent the study behind the Claude artifact: *Job-posting for the Philippines and
Indonesia: structure and AI exposure* (data as of 23 Nov 2026, **1,059,854 postings**, Jan 2024 →
Nov 2026, **13 platforms**, built entirely from **public web archives** — Common Crawl and the
Internet Archive's Wayback Machine). Our current collection is 2,618 rows from one government
portal plus a sampled archive. **v2 supersedes B1–B3 in `PROMPTS-PERPLEXITY-BOXCOMPUTE.md`.**
Perplexity (Part 1) is unaffected — run that as already sent.

## What changed, in one table

| # | v1 (ours) | v2 (aligned to the study) | Why it matters |
|---|---|---|---|
| 1 | Portal-first, archive as a secondary arm | **Archive-first, two archives** (Common Crawl + Wayback), platforms as the unit | Their 1.06M comes from archives, not from hitting platforms. This is also the ToS-clean route to 10k+. |
| 2 | One `arm` column (live / archive) | **Three kinds, never added together:** `counts` (platform's own ad counts by category+month), `job_card` (title·employer·location·category·date·teaser, no description), `full_page` (whole posting) | Adding them is the single easiest way to publish a wrong number. They are three different questions. |
| 3 | Karirhub + a few hosts | **13 platforms**: JobStreet, Glints, Pintarnya, KitaLulus, Dealls, LinkedIn, Kalibrr, Karir.com, Bossjob (+ our Karirhub) | Cross-platform is the only way to see whether a move is real or platform-specific. |
| 4 | Mix years freely | **Only compare within one platform · only postings captured within 90 days of posting · only calendar months both years have** | Archive volume per month is a property of the crawl, not of hiring. |
| 5 | Point estimates | **Every figure carries a range; series are marked beyond-range / within-range / "archives disagree"** | "Within its range" ≠ "nothing changed". They say so explicitly. |
| 6 | Unweighted | **Weight job cards to the platform's own monthly category totals** (their Kind A) | This is the fix for the artefact we flagged: our 2026 rows look richer only because they are live rows. |
| 7 | "AI mention" = keyword hit | **AI mention with four exclusions + full descriptions only + a hand-check** | See the rules block below. Their hand check: 35–36 of 40 random hits were genuinely about the job. |
| 8 | "Entry level" = fresh-graduate wording | **EO and E2, defined narrowly, with the denominator reported** | See below. |
| 9 | Exposure described in prose | **Every posting mapped to an ILO exposure gradient; classification checked against the platform's own category** | Their classifier agrees with the platform's own category on 56.9–77.2% of postings. |

---

## B-v2.1 · Session opener (paste first)

```
You are collecting a public dataset of Indonesian and Philippine job postings for an
academic-style labour-market study. Everything must come from PUBLIC WEB ARCHIVES
(the Internet Archive's Wayback Machine and Common Crawl) — do not send requests to the
job platforms themselves. Work in the sandbox, write each batch to disk as you go, and
give me download links at the end. Stop and report after each step.

RULES (non-negotiable)
- Public archive sources only. No login, no API keys, no paywalls, no anti-bot
  circumvention, and no direct requests to job platforms.
- No personal data: never collect recruiter names, phone numbers, e-mail addresses or
  applicant data. Employer names, titles and locations are fine.
- Reading archived pages is a crawl courtesy, not a right: at most 1 request every
  2 seconds, one worker, respect 429/503 with backoff, identify as a research crawler.
- An archive is NOT the labour market and NOT all the postings on a platform. Every
  output says so.

STEP 1 — Confirm the archives answer. For web.archive.org and commoncrawl.org (plus the
CDX API) report: which endpoints respond, their rate limits, and how to query by URL
pattern and by year. Report status, content-type and an example response.

STEP 2 — Inventory, per platform, per country, per year. For each platform below, use the
CDX API to count distinct archived URL patterns by year, 2024 → 2026, PH and ID separately.
Output one table: platform | year | country | distinct posting URLs found | captures.
No fetching yet — I want the counts first.
   jobstreet.co.id / jobstreet.com.ph · glints.com · pintarnya.id · kitalulus.com ·
   dealls.com · linkedin.com/jobs · kalibrr.com · karir.com · bossjob.co.id ·
   karirhub.kemnaker.go.id (ours)

STEP 3 — Choose the working route and say which: (a) CDX index + archived posting pages,
(b) archived listing/category pages for platform counts, (c) Common Crawl index for
coverage over time. You will need (a) and (c) together.
```

## B-v2.2 · The collection brief (paste after Step 2 reports)

```
STEP 4 — Collect in THREE KINDS. Keep them in separate files and NEVER add them together.

 KINDS
 A. counts   — the platform's own count of open ads, by category and month, read from
               archived category pages. No individual postings behind these rows.
               Save as jobs_counts.csv
 B. job_card — entries on archived listing pages: title, employer, location, category and
               sub-category, listing date, and the one-line teaser. NO description.
               Save as jobs_cards.csv
 C. full_page— whole archived posting pages: title, employer, full description and, where
               the platform shows them, salary, experience, education, skills.
               Save as jobs_full.csv

FIELDS — one row per record. Do not rename or drop columns.
record_id, data_kind, platform, country, url, original_url, domain_note,
posted_at, posted_basis, captured_at, capture_lag_days,
location_city, location_province,
title, employer, category_platform, category_jobstreet, sub_category,
description, description_chars, salary_shown, skills,
experience_stated, experience_min_years, eo_no_experience, e2_two_years_or_less,
min_education, ai_mention, ai_terms_matched, ai_evidence, ai_ai_source_field,
ai_excluded_reason, gradient, exposure_score, verification_status

FIELD RULES
- data_kind: counts | job_card | full_page. counts rows carry only platform, country,
  category, month, ad_count.
- capture_lag_days: days between posted_at and captured_at. Records with
  capture_lag_days > 90 are flagged and excluded from year-to-year comparisons
  (they stay in the file — exclusion happens downstream, not by deletion).
- ai_mention: TRUE only when the TITLE or DESCRIPTION names AI, machine learning,
  ChatGPT, LLM or the like in a sentence about the JOB. Set ai_excluded_reason and
  ai_mention=FALSE when the only hit is:
    (1) company boilerplate — the same sentence repeats word-for-word under 3+ job titles;
    (2) the employer's own hiring-process notice ("we may use AI tools in our hiring");
    (3) the employer describing itself ("a leading AI-powered platform");
    (4) "AI" meaning Adobe Illustrator.
  Record the matched term and the sentence in ai_evidence, and which field it came from in
  ai_ai_source_field. Use FULL DESCRIPTIONS ONLY — job cards and teasers are not eligible.
  Save 200 random TRUE rows to a separate file for a hand-check of the upper bound.
- experience_stated: TRUE when the description states a minimum experience or says none is
  needed. A description SILENT on experience is experience_stated=FALSE, and is excluded
  from EO/E2 — it is never counted as asking for experience.
- eo_no_experience: TRUE when the description says no experience is needed or gives zero
  years. e2_two_years_or_less: TRUE for EO, or a stated minimum of at most two years.
  Exclude internships from both. Report the share of descriptions that state a requirement
  at all, per platform per year — that share itself moves.
- Exclude listing pages captured after the job closed (they keep only part of the text).
- gradient / exposure_score: map title → platform category → the study's crosswalk to the
  ILO exposure gradients, and record the score. Flag rows you cannot map rather than
  guessing. Report the classifier's agreement rate against the platform's own category on
  a sample.

STEP 5 — Verify and report. Re-fetch a random 5% of full_page rows and confirm title,
employer, posted date and location; write verification.json. Then give me:
 1. counts per platform / country / year, and distinct URLs found vs fetched;
 2. duplicates removed and the dedupe key used
    (lowercased employer + normalised title + city + posting month);
 3. for every headline share, the RANGE and the verdict — beyond range / within range /
    archives disagree / too few records — computed within one platform at a time, on
    months both years have, capture lag ≤ 90 days;
 4. the weighting: platform monthly category totals (Kind A) and a weighted share
    alongside the unweighted one;
 5. the hand-check result for the AI-mention upper bound;
 6. a coverage-caveats section in plain English, including what the ads cannot speak to
    (job ads cover professional work densely and manual work far less than employment does);
 7. the CSV shards (each under 2 MB), verification.json, the hand-check file, and a
    one-page HTML report in light theme; share_file links for everything.
```

## B-v2.3 · The comparability gate (run before any number goes in a report)

```
For each share you are about to report, answer line by line: which platform? which years?
are both years the same archive? are they the same calendar months? is the mean capture lag
≤ 90 days? what is the range? is the change beyond the range? If any answer is "no" or
"unknown", the number is descriptive of the archived postings only and must be labelled
that way rather than reported as a change.
```

---

## What this buys us, concretely

1. **The 10k target becomes honest.** Archives are the route, not circumvention: the platforms
   keep 90 days of ads; the archives keep years, and reading them is a crawl-courtesy
   question, not a terms question.
2. **It fixes our known artefact.** Our 2026 rows look text-richer only because they are live
   rows. Weighting job cards to platform monthly totals is the correct method, and we can now
   copy it.
3. **It raises our AI-skill measure from keyword to auditable.** Four exclusions, full
   descriptions only, a hand-check on 200 rows, matched term + sentence stored per row — our
   current 3-of-2,618 headline becomes a defensible upper bound instead of a bare count.
4. **It gives our entry-level measure a real denominator** (descriptions that state a
   requirement) — without which the share can move for reasons that have nothing to do with
   hiring.
5. **It adds the exposure gradient** our register only describes in prose, with the category
   scores published in the study (Banking & Financial Services 0.58, Administration & Office
   Support 0.57, Call Centre & Customer Service 0.55 for Indonesia, Insurance & Superannuation
   0.55, Sales 0.49, HR 0.44, Engineering 0.33, Manufacturing/Transport & Logistics 0.32).

## One compliance flag — @clo, before anyone reuses the study's data

The study includes **LinkedIn, JobStreet and Indeed-class platforms via archived pages**. Our
team's standing decision was that those platforms are out of scope. The archive route is a
different posture from live scraping, but it is still *reuse* of their data, so **the scope
decision needs an explicit re-confirmation** before any archived-platform rows go into anything
shared with AISA, ILS-DOLE or ESCAP. Flagged, not assumed either way.
