# Prompts to run — Perplexity (verify) and BoxCompute (collect more postings)

**For:** Shafira · SPAR F26 Indonesia lane · 24 November 2026
Copy the block, paste it, run it. Nothing else needs to be explained to either tool.

---

# PART 1 — PERPLEXITY

## P1 · Main prompt (attach `ID-SIGNALS-PERPLEXITY-PACK.md` with it)

```
You are verifying the source line of a 22-row indicator register for a labour-market
early-warning study on Indonesia's banking and finance sector (SPAR Fall 2026, Economic
Shock Team). The attached file holds the framework, the 22 rows and the verification
questions (Blocks A-E). Work through the blocks in order.

HARD RULES
1. Never invent a URL, a figure, a report title or a release date. If a number cannot be
   confirmed, the answer is exactly "not verified" plus the closest primary source and
   where it would live.
2. Primary sources beat secondary: BPS, OJK, Kemnaker (incl. Satudata, Pasker ID), BPJS
   Ketenagakerjaan, JDIH/Setkab, ILO, World Bank, IMF, ESCAP, company annual and
   sustainability reports. Indonesian-language pages are fine and preferred when the
   English version lags.
3. Every checkable figure returns: number, unit, source page, release date, and one
   confidence tag — H (official statistics / company filing / industry body),
   M (named press reporting / survey), L (anonymous / vendor-commissioned).
4. This study writes "consistent with AI-driven change", never "caused by AI". For every
   row, give one alternative explanation that does not involve AI.
5. Public sources only. No personal data. Aggregates and shares, never individual ads.

OUTPUT
Return one table with 27 rows (Block A: 5 rows, Block B: 22 rows) with the columns:
block | row_id | status (supported / partly supported / gap) | source_url | figure_verbatim
| release_date | access (public / registration / paid / request-from-agency) | frequency
| history_back_to | confidence H/M/L | alternative_explanation | notes

Then three short lists, no prose:
(a) everything that could not be verified, with the request route to get it;
(b) every source that turned out to be secondary where a primary exists;
(c) any figure that contradicts the number in the attached register — flag the
    contradiction, do not silently replace it.
```

## P2 · The one follow-up worth spending a second query on

```
Of the 22 rows above, five are stated gaps: where dismissed finance workers go next, any
link from firm AI adoption to hires or wages, JKP claim approval and payment latency,
hiring by occupation inside banking, and placement/earnings outcomes of JKP training.
For each: (1) does any Indonesian source measure it at all, even privately or in an
academic paper? (2) if no, which single institution could produce it — BPS, Kemnaker,
BPJS Ketenagakerjaan, Bank Indonesia, OJK, LPEM UI, SMERU, World Bank? (3) what is the
request route and roughly what would it cost in time? Answer as a 5-row table:
gap | exists? | holder | route | time-to-obtain | confidence.
```

---

# PART 2 — BOXCOMPUTE (scrape more postings)

**Honest frame before you run it.** 2,618 rows took one portal plus a partial archive.
Getting to ~10,000 is not "scrape harder on the same page" — it is four levers, in this
order of value: **(1)** exhaust the Wayback CDX index instead of sampling it, **(2)** add
the *other* public Indonesian portals (Kemnaker Pasker ID, provincial Disnaker job pages),
**(3)** add a public corpus arm (Common Crawl job pages), **(4)** widen the sector filter
and label the widened rows instead of discarding them.

**One hard limit to respect, not route around.** JobStreet, Indeed and LinkedIn are out of
scope for this team — their terms forbid extraction and they sell this data. If a colleague
reached 10,000, ask which source: if it is one of those three, the dataset cannot be
published or shared with AISA/ESCAP, and that is a compliance problem, not a dataset.
Route it to @clo before using it.

## B1 · Session opener (paste first, in the same chat)

```
You are collecting a public dataset of Indonesian job postings for an academic-style
labour-market study. Work inside the sandbox, save every output, and give me download
links at the end. Follow this order and stop to report after each step.

RULES (non-negotiable)
- Public pages only. No login, no API keys, no paywalls, no anti-bot circumvention.
- Read and report robots.txt before touching any host; if it does not allow the path I
  need, say so and pick another source instead of working around it.
- No personal data: never collect recruiter names, phone numbers, e-mail addresses, or
  any applicant data. Employer names and job titles are fine.
- Politeness: at most 1 request every 2 seconds per host, 1 concurrent worker, respect
  429/503 with exponential backoff, identify as a research crawler.
- Advertised demand is NOT a census. Every output carries that caveat.

STEP 1 — Check the front door. For each host below, fetch robots.txt and tell me in a
table: host | allowed paths | disallowed | verdict (OK / NO).
   karirhub.kemnaker.go.id · paskerid.kemnaker.go.id · satudata.kemnaker.go.id ·
   disnaker portals for DKI Jakarta, Jawa Tengah, Jawa Barat, Jawa Timur ·
   web.archive.org (for the same hosts) · commoncrawl.org

STEP 2 — Probe. For each target, report HTTP status, content-type and whether the data is
in the HTML or arrives by JavaScript. Do not proceed on a 403 or a DNS failure — record it
and move on.

STEP 3 — Choose the working route and say which you chose: (a) server-rendered listing
pages, (b) the site's own search page read through the browser skill, (c) the Internet
Archive CDX index, (d) Common Crawl. Prefer (a), then (c).
```

## B2 · The collection brief (paste after Step 3 reports)

```
STEP 4 — Collect. Target: ~10,000 postings, Indonesia, and tag every row rather than
drop it. Cover in this order, writing each batch to CSV as you go so progress survives:

 A. karirhub.kemnaker.go.id — the live portal, ALL open finance/BPO/insurance categories
    (not a sample): walk every listing page and paginate to the end, then read each
    posting's own page for its full text and "Persyaratan Khusus" section.
 B. web.archive.org — exhaust the CDX index for every karirhub posting URL, all years
    2019→2026 (do NOT sample captures): query the CDX API per year and per URL pattern,
    then fetch the archived posting pages. Report how many unique posting URLs the archive
    knows about versus how many you could fetch.
 C. paskerid.kemnaker.go.id and the provincial Disnaker job pages you cleared in Step 1 —
    same fields where they exist.
 D. commoncrawl.org — count, then extract, Indonesian job-posting pages for the same
    hosts across available crawls, so we can show coverage over time. Report the count
    first and only extract if the count is meaningful.
 E. Only if A-D leave a gap your report can name: tell me which single additional public
    source would close it, and why.

FIELDS (one row per posting — keep this exactly, do not add or rename columns)
rec_id, arm, source, domain, domain_note, posted_at, posted_basis, captured_at,
location_city, location_province, title, employer, sector, in_scope, job_function,
skills, content, content_chars_full, requirements, ai_skill_required, ai_tier,
ai_evidence, ai_source, data_skill_flag, data_evidence, digital_basic_flag,
min_education, salary_shown, deadline, quota, url, original_url, verified_status,
verified_at, verified_fields, unverified_fields

RULES FOR THE FIELDS
- posted_at: the posting's own date. Write posted_basis as "exact (publishedAt)" when the
  page states it, otherwise "derived from relative label at capture" and say the error bar.
- sector: put your best label AND set in_scope to finance_bpo, outside_scope, or unknown.
  Never drop the widened rows — the outside_scope count is itself a finding.
- ai_tier: one of none / digital_basic / data_skill / ai_explicit.
  ai_explicit ONLY when the posting's requirements name an AI skill or tool.
  ai_evidence must contain the matched term plus the sentence it came from — never a bare
  Yes/No. ai_source records which field matched.
- requirements: the portal's Persyaratan Khusus text, up to 2,000 chars; empty when the
  posting has none (say "none rendered", not "failed").
- Dedupe: key on lowercased employer + normalised title + city + posting month. Report how
  many duplicates were removed and how many rows survive.

STEP 5 — Verify and report. Re-fetch a random 10% sample of rows and confirm title,
posted date, employer and location still match; write the per-row result to
verification.json. Then give me:
 1. rows per source and per year, and unique posting URLs found vs fetched;
 2. the duplicate count removed;
 3. a coverage-caveats section in plain English: what this sample does NOT show;
 4. the four CSV shards (by posting year, keep each file under 2 MB), verification.json,
    and a one-page HTML report in light theme with the coverage tables.
 5. share_file links for everything.
```

## B3 · The check worth running on any colleague's 10k dataset

```
Here is a job-postings dataset someone else collected. Without guessing, tell me: which
sources it came from (look at the URL/domain columns), whether any of them forbid
extraction in their terms or robots.txt, how many rows share the same employer and title
and month (duplication), how many rows have no posting date, and how many rows are
actually finance or insurance versus other sectors. Output: a 6-row audit table plus a
verdict on whether this dataset can be cited in a published report or only used as
internal signal.
```

---

## What "10,000" will and will not buy you

| Path | Rows reachable | Sector precision | Publishable |
|---|---|---|---|
| Karirhub live, exhaustive | ~1–2k | high (Swasta/government employer names) | yes |
| Wayback CDX, exhaustive (2019→2026) | +5–8k | medium (thin text in old captures) | yes |
| Pasker ID + provincial Disnaker | +1–3k | medium | yes |
| Common Crawl arm | count first | low (metadata only) | yes, as a coverage arm |
| JobStreet / Indeed / LinkedIn | large | — | **no — out of scope, ToS forbids** |

**The trade to make explicitly:** 10k rows that mix sectors give you volume and trend coverage;
2.6k finance-verified rows give you precision. Publish both, labelled — never average them into
one series without saying which arm each point came from. The `arm` and `in_scope` columns exist
for exactly this reason.
