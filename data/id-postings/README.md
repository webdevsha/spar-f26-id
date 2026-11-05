# id-postings — Karirhub individual postings, preliminary scrape

**Window:** 2024-01-01 → 2026-10-20. The live portal only lists current postings (2025-10-20 → 2026-10-20); everything earlier is Web Archive.

**Archive arms:** Jan 2024 – 19 Oct 2025 backfill: 2,159 postings from 2,189 Wayback captures. 20 Oct 2025 – 20 Oct 2026: 128 more from the only 88 captures that exist for that period (the archive barely crawled Karirhub then). One request every 2 s, one worker.

**Persyaratan Khusus** (the portal's "special requirements" section) is captured for every row: 195 of 281 live and 2262 of 2337 archive (2457 of 2618 overall). Where it is missing the portal renders no such section for that posting — not a parse failure. Full text sits in the CSV column `requirements`.
**Collected:** 2026-10-20 (UTC) from this VM.
**Scope:** Indonesian **finance & insurance** plus **BPO** postings (the two sectors SPAR's S5
hiring signal cares about), tagged with timestamps, locations, content and an AI-skill flag.

This is the dataset behind `build/spar-id-postings.html`. It is a **sample of advertised
demand**, not a census of vacancies, and not a measure of hiring.

## Files

| File | Rows | What |
|---|---|---|
| `postings-<year>.csv` | 2,618 | one row per posting: 281 live + 2,337 archived, 2024-02 → 2026-10. Sharded by posting year (`postings-2024.csv`, `-2025.csv`, `-2026.csv`) because a single file passed 3.5 MB at this size, over the 2 MB per-file limit the publishing tool enforces |
| `summary.json` | — | counts used by the report builder |
| `verification.json` | 411 checked of 2,618 | per-row result of re-fetching the source: 281 live + 50 originals + 130 sampled archive rows (written by `build/verify_postings.py --write`) |

Read the shards with a CSV parser, not `cat`: concatenating them repeats each file's header. The `postings-*.csv` glob is what the build scripts use, so a future split into half-years (`postings-2025-h1.csv`, …) needs no code change.

## Sources — every row is PUBLIC

| `arm` | Source | Domain | Gate |
|---|---|---|---|
| `live` | `karirhub.kemnaker.go.id/lowongan-dalam-negeri/lowongan/<slug>-<uuid>` | **PUBLIC** | none — government portal, `robots.txt` = `Allow: /` |
| `archive` | `web.archive.org` capture of the same public posting pages | **PUBLIC** | none — public archive |

No login, no API key, no paid feed, no access request, no anti-bot circumvention was used.
Where a platform refused us (Kalibrr KJS API, BCA candidate API, JobStreet, Indeed) the arm is
simply absent — see the "What worked, what refused us" table in the HTML report.

## Schema

| Column | Meaning |
|---|---|
| `rec_id` | `IN-P-###` row id, stable per build |
| `arm` | `live` (portal today) or `archive` (Wayback capture) |
| `source`, `url` | exact page the row came from |
| `domain`, `domain_note` | PUBLIC for all rows, with the reason |
| `posted_at` | posting date — **the team's timestamp** |
| `posted_basis` | `exact (publishedAt)` for live rows; `derived from relative label at capture` for archive rows |
| `captured_at` | when we fetched it |
| `location_city`, `location_province` | **location** |
| `title`, `employer`, `sector`, `job_function` | who is advertising what |
| `skills` | skills list as printed on the ad |
| `content` | **content** — first 240 chars of the ad body (truncated on purpose) |
| `content_chars_full` | length of the full description before truncation |
| `requirements` | the portal's *Persyaratan Khusus* (special requirements) text, up to 2,000 chars; empty when the posting has none |
| `ai_skill_required` | **Yes/No** — Yes only when the posting's `requirements` (Persyaratan Khusus) names an AI skill or tool. 3 rows qualify |
| `ai_tier` | `none` · `digital_basic` · `data_skill` · `ai_explicit` |
| `ai_evidence` | the matched term plus a snippet of the sentence — auditable, never a bare boolean |
| `ai_source` | where the match came from (`requirements` when the flag is Yes) |
| `data_skill_flag` | data analysis / SQL / Python / BI named |
| `data_evidence` | the matched data term |
| `digital_basic_flag` | ordinary digital literacy only (Excel, Office, "komputer") |
| `min_education`, `salary_shown`, `deadline`, `quota` | extra attributes kept for later analysis |
| `original_url` | the original Karirhub posting URL (same as `url` for live rows; for archive rows, the page the capture was taken of) |
| `verified_status` | `verified` (live; every checked field matched the source) · `partly verified` (archive; capture loads and title/employer/location match, but date is derived and sector is a guess) · `unverified` (source failed or a field mismatched) · `not checked` |
| `verified_at` | date the source was re-fetched |
| `verified_fields`, `unverified_fields` | what was compared against the source, and what could not be (or the mismatch, if `unverified`) |
| `in_scope` | `finance_bpo` (498 rows; 217 are archive rows classified by keyword guess) or `outside_scope` |

## Flag method — the AI flag now comes from Persyaratan Khusus

`ai_skill_required` is **Yes only when the posting's own Persyaratan Khusus names an AI skill or
tool** — the rule the team asked for. The term list is explicit (kecerdasan buatan, machine
learning, ChatGPT, prompt engineering, computer vision, named tools and libraries) and
word-bounded, because the earlier loose pass was wrong in both directions:

| mistake | effect |
| --- | --- |
| `keras` | matched the everyday word *pekerja keras* ("diligent worker") — 66 rows |
| `genai` | matched inside *mengenai* ("regarding") |
| `ai tools` | matched inside *Menguasai tools* |
| `llm` | matched inside *fulfillment* |
| "AI" in a design ad | usually means Adobe Illustrator, not artificial intelligence |
| never reading the requirements section | the section that actually states the skills wanted |

Automation-only wording (RPA, *otomasi*, big data, predictive analytics) is deliberately **not**
counted. A mention that appears only in the ad description stays **No** and is kept in
`ai_evidence` prefixed `context only` (5 rows), so a reader sees it without the flag claiming
more than it knows. **161 rows have no Persyaratan Khusus section at all**, so nothing can be
concluded about their requirements.

Result: **3 of 2,618 rows are Yes** — *Artificial Intelligence Staff*, *Data Analyst* (degree in
data science), and a live *Data Entry & Administrative Support* ad that asks for willingness to
use AI tools. That near-absence is a finding about **advertised** demand, not about AI use on
the job. Widen the sample and re-run before drawing an S5 conclusion.

## Ethics

- **robots.txt respected** — only public posting pages; `/api/`, `/admin/`, `/login` never touched.
- **No personal data** — no applicant names, CVs, e-mails, phone numbers or recruiter contacts.
  Company names appear only as the employer published them in a public advertisement.
  Consistent with `../PERSONAL-DATA-STOP.md`.
- **Identified crawler, rate limited** — `User-Agent: SPAR-F26-research/0.1 (academic feasibility test)`,
  ~0.35 s between requests.
- **Minimal re-publication** — ad bodies truncated to 240 characters so the repo is not a mirror
  of the platform. Full text stays in local scratch and is not committed.
- **No circumvention** — refusals were recorded, not defeated.

## Provenance per arm — how real is each row?

| `arm` | Rows | Verification | Weak spots |
|---|---|---|---|
| `live` | 281 | Full re-fetch on 2026-10-20 with `build/verify_postings.py`: **281 of 281** returned HTTP 200 with the same title, `publishedAt` date, deadline and employer as the stored row | Closed listings disappear later; this arm is a snapshot of what was open on 2026-10-20 |
| `archive` (Oct 2025 onward) | 50 | Every row links to its `web.archive.org` capture (URL in the `url` column); all 50 captures returned 200 and contained the title (employer too, where recorded) | Dates are **derived** from the relative label on the captured page ("3 days ago"), 2 rows lack an employer name, 32 lack a skills list, and the sector is a keyword guess on title + employer, labelled `(guessed … unverified)` in the `sector` column (the archived page has no industry field) |
| `archive` (backfill, Feb 2024 – Oct 2025) | 2,159 | Parsed once from the capture when downloaded. A **random sample of 100** (seed 20261104) was re-fetched: **100 of 100** loaded and matched title, location and employer. The other 2,059 are `not checked` | Same weak spots as the archive arm, **and worse dates**: 1,512 of 2,159 carry a month-level label ("3 months ago"), so their `posted_at` is only good to about ±15 days (`posted_basis` says which). Coverage is whatever the Internet Archive crawled: Aug 2024, Dec 2024 and Jul 2025 are heavy, Jan–Jul 2024 nearly empty. 26 captures had no date label and 2 could not be fetched, so they are excluded, not guessed |

So: no row is invented. The live arm is directly verifiable against the platform today; the
archive arm is real but reconstructed from rendered text, and its dates carry ±1 day of slack.

## Corrections (2026-10-20 audit)

An audit re-fetched all 331 source pages and found four defects in the first build. All are
fixed in `build/prep_postings.py` and the CSV regenerated from the raw crawl:

| Defect | Rows | Cause | Fix |
|---|---|---|---|
| `location_province = "Indonesia"` | 40 archive | Locations print as `CITY, PROVINCE, Indonesia`; the parser took the last part as the province. The report wrongly called these "nationwide" postings | Drop the trailing country, then province = last part, city = the part before it. 0 rows now have `Indonesia` as a province |
| Site slogan inside the title | IN-P-330, IN-P-331 | Parser used the page `<title>` ("Dapatkan pekerjaan dari seluruh dunia : Karirhub - …") | Slogan stripped; titles now `Guru Bahasa Inggris` and `Operator Perakitan Komponen Plastik Injection` |
| Blank location | IN-P-331 | Longer `kelurahan, kecamatan, kabupaten, province` format was not parsed | Recovered from the capture: Kabupaten Bekasi, Jawa Barat |
| Over-broad archive sector guess | 4 rows flip scope | Keywords were searched in the ad body and included loose tokens (`cs `, `dana`, `outsourc`), so an HR Officer at a ceramics firm counted as finance; FIFGROUP (a multifinance company) did not | Match title + employer + job function only; generic tokens removed; `financ` counts on the employer name only; FIFGROUP and a few known lenders added. IN-P-283 now in scope; IN-P-305, -321, -325 now out. In-scope total 290 → 288 |

Also cosmetic: `Dki Jakarta` (from `str.title()`) is now `DKI Jakarta` on 44 live rows.

Not fixable from the data, and now stated rather than implied: the two slogan-title captures show
no employer name, 32 archive rows have no skills list, archive dates are derived from relative labels,
and the archive finance/not-finance label is still a guess.

`build/verify_postings.py` re-checks every row against its source (live: title, date, deadline,
employer, location; archive: capture loads and contains the title, location and employer). The result is
stored per row (`verified_status` in the CSV, `verification.json`) and shown on the page.
Workflow: `verify_postings.py --write` → `prep_postings.py` → `build_postings_report.py`. Run it before trusting a rebuilt CSV.

## Limits — do not read these numbers as a trend

1. **Recency skew.** 187 of the 288 in-scope rows were posted in Oct 2026, because open listings
   are the ones still online. The archive arm now reaches back to Feb 2024 but is lumpy (see above). Nov–Dec 2025 is partly covered by the archive; **Jan–Jul 2026 stays nearly empty (about 17 rows)** because neither source has it: the portal only lists open postings and the Internet Archive barely captured Karirhub detail pages then. No amount of re-crawling today recovers those months.
2. **One keyword sweep.** The 281 live rows came from a single harvest pass, not an exhaustive
   month-by-month crawl. Volumes are a floor, not a total.
3. **Employer aliases.** `PT X` and `X` are not merged; one employer can appear as many
   city-level postings (e.g. 32 rows for one BPTN Syariah role type).
4. **Archive timestamps** are derived from relative labels ("2 days ago") at capture time.
5. **Advertised demand ≠ hires.** Postings cannot establish hiring rates or employment.

## Regenerate

```bash
python3 build/prep_postings.py           # raw crawl -> data/id-postings/  (needs the local crawl)
python3 build/build_postings_report.py   # data/id-postings/*.csv -> build/spar-id-postings.html
```

The raw detail-page harvest (`scratch/feas/out_postings.csv`) is **deliberately not committed** — it
holds the full ad text. So `prep_postings.py` only runs on a machine that has the crawl; the report
builder runs anywhere, straight from the committed CSV.

## Takedown

If Karirhub or the Internet Archive objects to this slice, delete
`postings-<year>.csv`, `summary.json` and `build/spar-id-postings.html`, and say so
in the commit message. Nothing else in the repo depends on them.
