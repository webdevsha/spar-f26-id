# Open items, blockers and the BoxCompute collection

What is still open, stated plainly, plus the 24 November BoxCompute collection record.

---

[← Back to the README index](../../README.md)

---

## Open items and blockers

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Hourly sheet → repo sync failing at its commit step | CTO / `@misshanna_bot` | The 29 Nov freeze; every `data/*.csv` consumer |
| 2 | ~~Cloudflare Pages deploy auth failure (code 10000)~~ — **closed 28 Nov 2026**: deploy verified working (30 files + Functions bundle, deployment `6bf9dacb`) | CTO / `@misshanna_bot` | Was: every new page going live |
| 3 | Readiness scoring — 3 documents × 6 questions | Shafira | Needs the six question texts (not recorded anywhere; the tab holds only `q1`–`q6`) |
| 4 | Regulator-facing requests: 15 routes surfaced to BPJS, OJK, Kemnaker, BPS, DPR Commission IX, plus a scope question on platform data obtained via web archives | **@clo before anything is sent** | Nothing sent to date |
| 5 | [data/id-signals.csv](../../data/id-signals.csv) etc. mirror stale vs the sheets | sync job (#1) | Dashboard accuracy |

## BoxCompute collection (24 Nov 2026)

**Why BoxCompute.** The lane's posting evidence currently rests on one government portal plus a
sampled archive (2,618 rows). The v2 brief ([docs/PROMPTS-BOXCOMPUTE-V2.md](../../docs/PROMPTS-BOXCOMPUTE-V2.md)) moves to an
**archive-first** design across 13 platforms, **Indonesia only** (the Philippines lane was dropped on 24 Nov as this study covers Indonesia), because that is both the ToS-clean route to volume and
the only route that reaches a platform's own published scale.

**Target (v2 brief, Step 1).** Per platform: `distinct posting URLs` by year, plus a coverage probe —
*counts first, no fetching until the counts exist*. Q1, honestly asked: **how much is actually
archived?** Until that is answered, any collection number is a guess.

**Collection runs in a BoxCompute sandbox, driven by the CLI** (`bxc sandbox exec`), not through the
web chat: the chat surface is not exposed by the CLI, SDK or REST API, and a scripted sandbox puts
results in the repo as artefacts instead of chat prose.

Artefacts produced by the run are committed under [`data/boxcompute/`](../../data/boxcompute/):

| File | What |
|---|---|
| [census.json](../../data/boxcompute/census.json) | per platform: CDX page probe, distinct URLs per year, the scoped CDX target, and whether the host was capped |
| [patterns.json](../../data/boxcompute/patterns.json) | per host: distinct URLs → **posting-like** URLs, the rate, and the URL shapes behind both — the derivation of the posting filters from evidence rather than guesswork |
| [url_shapes/](../../data/boxcompute/url_shapes) | sampled distinct URLs, one file per host (e.g. [kitalulus.com.txt](../../data/boxcompute/url_shapes/kitalulus.com.txt)) |
| [census.log](../../data/boxcompute/census.log) | full request log, including every backoff |
| [harvest.log](../../data/boxcompute/harvest.log) | Stage 2 `job_card` harvest progress, bucket by bucket |

**Method, and its limits.** Wayback CDX only: `collapsed=urlkey`, `statuscode:200`, one request every
3 s, backoff on 429/503/504, and a User-Agent that identifies the crawler as an academic study.
Three cautions are part of the result, not footnotes:

- **Distinct URLs ≠ postings ≠ hires.** A URL can be one ad or one search page; CDX volume is a
  property of the crawl, not of hiring. No figure from this run may be read as a level of demand.
- **CDX page counts are a volume probe only.** An assumed page size would be an invented figure, so
  the raw page count is reported and nothing is extrapolated from it.
- **Some hosts are too large for a single CDX response.** Piercing `jobstreet.co.id` and
  `linkedin.com` needs monthly pagination; where a host is skipped or throttled the table says so.

**Census complete (24 Nov, 10 Indonesian platforms).** The census produced a number that must
**not** be quoted as-is, and finding that out is the run's first real result.

Raw distinct-URL counts are dominated by non-postings: on KitaLulus, 16,172 of 183,982 distinct URLs
are `/_next/image` paths; on Dealls, tens of thousands are city × category *search permutations*.
Posting patterns were therefore **derived from the data** — see
[patterns.json](../../data/boxcompute/patterns.json) — and applied as a filter:

| Platform | 2024 | 2025 | 2026 (to 30 Nov) | Distinct URLs | Posting-like | Rate |
|---|---:|---:|---:|---:|---:|---:|
| Glints ⚠️ *capped* | 100,000 | 100,000 | 33,876 | 233,876 | 136,451 | 58.3% † |
| KitaLulus | 49,881 | 72,729 | 61,372 | 183,982 | 71,076 | 38.6% |
| Dealls | 17,946 | 26,471 | 31,928 | 76,345 | 67,647 | 88.6% |
| Kalibrr | 28,039 | 12,423 | 2,518 | 42,980 | 29,455 | 68.5% |
| JobStreet ID ⚠️ *capped* | 20,000 | 0 | 0 | 20,000 | 18,327 | 91.6% † |
| LinkedIn Jobs ⚠️ *capped* | 0 | 0 | 20,000 | 20,000 | 20,000 | 100.0% † |
| Karirhub (ours) | 5,772 | 7,266 | 270 | 13,308 | 12,390 | 93.1% |
| Karir.com | 4,118 | 2,197 | 1,006 | 7,321 | 52 | 0.7% † |
| Pintarnya | 0 | 0 | 0 | 0 | 0 | — |
| Bossjob | 0 | 0 | 0 | 0 | 0 | — |
| **Total (10 of 10 ID)** | | | | **597,812** | **355,398** | 59.4% |

Three cautions are part of the result, not footnotes:

- **The total is a floor, not a total.** Three hosts stopped at a per-request cap — Glints at exactly
  100,000 for two consecutive years, JobStreet ID and LinkedIn at 20,000 — so those rows are minimums.
- **† The filter errs both ways.** It over-counts where a URL is a search permutation, and
  under-counts where the real pattern was not anticipated: Karir.com's pattern is
  `/opportunities/<num>` (4,658 URLs), so its rate reads wrongly near-zero. JobStreet ID and LinkedIn
  each returned a zero year whose neighbours are full — a failed query, not a year without vacancies —
  so those cells are unusable. Posting-like is a **per-platform sanity signal, never a cross-platform
  ranking.**
- **Distinct URLs ≠ postings ≠ hires.** A URL can be one ad or one search page; CDX volume is a
  property of the crawl, not of hiring. 2026 is a partial year and is not comparable on its own.

**Stage 2 (`job_card` harvest) is running**, chained into Stage 3 (`full_page`). Stratified 25 URLs per
platform-month, extracted via schema.org `JobPosting` where the page carries it, falling back to
OpenGraph. Every row carries `posted_basis` (`jsonld` | `capture_proxy`) so a crawl date can never be
read as a posting date, and rows without a title or employer go to a rejected file rather than being
emitted blank. Progress in [harvest.log](../../data/boxcompute/harvest.log).

**Access is not the constraint.** From the sandbox: Wayback CDX **200**, Common Crawl index **200**,
Karirhub live **200**, Pasker ID **200**. By contrast Algolia (`algolia.kemnaker.go.id`, the
`L3WWP72HSI` shard) is **unreachable from both the sandbox and the agent network**, and Glints /
LinkedIn / JobStreet direct requests return **403/403/308**. The archive-first design is therefore
not a preference — it is the only route that works and the only one that respects the platforms.

---
