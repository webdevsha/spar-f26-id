# id-postings — Karirhub individual postings, preliminary scrape

**Window:** 2025-10-20 → 2026-10-20 (past 12 months from collection).
**Collected:** 2026-10-20 (UTC) from this VM.
**Scope:** Indonesian **finance & insurance** plus **BPO** postings (the two sectors SPAR's S5
hiring signal cares about), tagged with timestamps, locations, content and an AI-skill flag.

This is the dataset behind `build/spar-id-postings.html`. It is a **sample of advertised
demand**, not a census of vacancies, and not a measure of hiring.

## Files

| File | Rows | What |
|---|---|---|
| `karirhub-id-postings-sample.csv` | 331 | 281 live + 50 archived postings, one row each |
| `summary.json` | — | counts used by the report builder |

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
| `ai_skill_required` | **Yes/No** — AI/ML/automation/GenAI/RPA named in text (word-boundary rules) |
| `ai_tier` | `none` · `digital_basic` · `data_skill` · `ai_explicit` |
| `ai_evidence` | the exact term that produced the flag — auditable, never a bare boolean |
| `data_skill_flag` | data analysis / SQL / Python / BI named |
| `data_evidence` | the matched data term |
| `digital_basic_flag` | ordinary digital literacy only (Excel, Office, "komputer") |
| `min_education`, `salary_shown`, `deadline`, `quota` | extra attributes kept for later analysis |
| `in_scope` | `finance_bpo` (290 rows) or `outside_scope` |

## Flag method — and the false positives it caught

The first keyword pass used a loose substring match (`ai`, `genai`, `otomasi`) and flagged **5**
postings as AI-required. Three of those were artefacts: `komputer` (computer literacy), `AIA`
(the insurer's name), and `mengenai` — the ordinary Indonesian word "regarding", which contains
the letters `g-e-n-a-i`. With word-boundary rules on a fixed term list the honest count is
**1 of 290** ("Finance Automation").

Consequence for the team's plan: naive keyword counting overstated AI demand 5×. Store the raw
content, flag conservatively, and let the deferred LLM/manual pass do the categorisation —
that is Akbar's "whichever is more convenient", and it is also the more accurate one.

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
| `live` | 281 | Random re-fetch after the build: **6 of 6** returned HTTP 200 with the same title, `publishedAt` date and employer as the stored row | Closed listings disappear later; this arm is a snapshot of what was open on 2026-10-20 |
| `archive` | 50 | Every row links to its `web.archive.org` capture (URL in the `url` column); 3 spot-checked captures returned 200 and contained the title | Dates are **derived** from the relative label on the captured page ("3 days ago"), 2 rows lack an employer name, 32 lack a skills list, and the sector is keyword-matched (the archived page did not expose the industry field) |

So: no row is invented. The live arm is directly verifiable against the platform today; the
archive arm is real but reconstructed from rendered text, and its dates carry ±1 day of slack.

## Limits — do not read these numbers as a trend

1. **Recency skew.** 187 of the 290 in-scope rows were posted in Oct 2026, because open listings
   are the ones still online. The archive arm covers Oct–Dec 2025 and then thins out.
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
`karirhub-id-postings-sample.csv`, `summary.json` and `build/spar-id-postings.html`, and say so
in the commit message. Nothing else in the repo depends on them.
