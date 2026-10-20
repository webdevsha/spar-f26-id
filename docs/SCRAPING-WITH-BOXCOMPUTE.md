# How to scrape with BoxCompute — Indonesia as the case study

**Audience:** anyone on the team who wants a real dataset of job postings and is not a
scraper. **Time to first CSV:** about 10 minutes. **What you need:** a browser and a
BoxCompute chat — no installs, no local Python, no command line on your own machine.

This guide uses the SPAR F26 Indonesia run as the worked example (Karirhub / Kemnaker,
finance & BPO, last 12 months) because it hit almost every obstacle you will meet: a
search API that would not resolve, a portal that renders client-side, a commercial job
board that refuses, and an archive that half-works.

---

## 0. The 60-second version

1. Ask the agent to **check the rules** (robots.txt, terms, personal data).
2. Ask it to **probe** the sites you care about and report which ones answer.
3. Ask it to **find one route that works** — usually a plain server-rendered page, not an API.
4. Ask it to **collect links, then read each page slowly**, and to save a CSV.
5. Ask it to **write an HTML report** with the coverage caveats, then **share the files**.

That is the whole method. Everything below is the detail behind those five lines.

---

## 1. What BoxCompute actually is (in plain words)

| Term | What it means for you |
|---|---|
| **BoxCompute chat** | Where you type. You talk to an agent that can run code, browse, read files and publish results. |
| **Sandbox / VM** | A small Linux computer the agent works in. It has its own disk (`/workspace`), Python, and network access. You never touch it directly. |
| **Terminal tab** | A shell into that same computer, if you want to type commands yourself. Optional. |
| **Files / Assets** | Where finished files go. `share_file` gives you a download link that survives the VM being deleted. |
| **Previews** | A temporary public URL for a local web page (used for the HTML reports). Expires after about an hour; the file itself stays in Assets. |
| **Skills** | Pre-packaged abilities the agent can call — the `browser` skill (headless Lightpanda), `xlsx`, `docx`, `web-search`, `web-fetch`. |

**Key point for laymen:** you do not need to know how to scrape. You need to know what a
*working route* looks like, so you can tell when the agent is guessing. That is what
section 3 teaches.

---

## 2. Before you scrape: the four rules

These are not optional, and they are the first thing to ask the agent to check.

1. **robots.txt.** The file at `site.com/robots.txt` says which paths a robot may read.
   Karirhub's says `User-agent: * → Allow: /` with only `/admin/`, `/dashboard/`,
   `/api/`, `/login` disallowed. So the posting pages are fair game; the API is not.
2. **Terms of service.** robots.txt is permission to *crawl*; the ToS is permission to
   *reuse*. If a site sells its data or forbids extraction, do not scrape it — ask the
   owner. (This is why JobStreet, Indeed and LinkedIn are out of scope for us.)
3. **Personal data.** Job ads contain company names — fine. They can also contain a
   recruiter's name, phone, e-mail, or applicant CVs — never collect those. Our repo rule
   is `data/PERSONAL-DATA-STOP.md`: public sources only, no personal data, ever.
4. **Honesty about coverage.** A scrape is a **sample**, not a census. Say so in the
   output. Never let a chart imply "this is how many vacancies existed".

---

## 3. The recipe, with the key terms explained

### Step 1 — Check the front door

Ask the agent: *"read robots.txt for these hosts and tell me what is allowed."*

If the answer is not a blanket `Allow: /` for the paths you need, stop and pick another
source. A refusal is information, not an obstacle to route around.

### Step 2 — Find out what answers

Ask: *"probe these URLs and tell me status, size and content type."*

You will get one of these, and each means something different:

| What you see | What it means | What to do |
|---|---|---|
| `200` + HTML | The page is reachable | Good — check whether the data is *in* the HTML |
| `No address associated with hostname` | **DNS block** — the host does not exist from this network | The API is unusable here. Find another route. |
| `403 Forbidden` | The server refuses non-browser clients | Treat as a "no". Do not spoof your way in. |
| `404 / 400 BAD REQUEST` | Wrong endpoint, or an endpoint that needs a signed request | Dead end without their key. |
| `200` but the page is empty of data | **Client-side rendering** — the rows arrive by JavaScript later | Either use the `browser` skill, or find a server-rendered page. |

In the Indonesia run this table is literally what happened: `algolia.kemnaker.go.id`
returned DNS failure, Kalibrr returned `400/404`, BCA returned `403`, and the Karirhub
*listing* page returned 200 with no rows in the HTML.

### Step 3 — Choose the route that works

Three routes, in order of preference:

1. **A server-rendered page.** The data is inside the HTML you just downloaded. Cheapest,
   most stable, easiest to audit. This is what won in Indonesia: the individual posting
   pages carry the whole vacancy object inside a Next.js payload.
2. **A public API with a public key.** Fine if the key is meant for browsers (it will be
   rate-limited, and that is the point). Not fine if you have to guess a token.
3. **An archive (Wayback Machine).** Good for "what did this page say in 2025", bad for
   completeness. Treat archived rows as a separate arm of the dataset, never mixed
   silently with live rows.

**The Indonesia trick worth remembering:** we could not search, but we could *read*.
Harvest posting URLs from the pages that do render (homepage, category page, or a
browser-driven keyword search), then fetch each posting page directly. No search API
required once you hold the URL.

### Step 4 — Collect links, then read pages politely

Rules the agent should follow, and that you should ask for explicitly:

- **Identify yourself** in the `User-Agent`, e.g.
  `SPAR-F26-research/0.1 (academic feasibility test; contact: team)`.
- **Sleep between requests** — 0.3–0.5 s is plenty for a portal like this.
- **Do not retry a refusal.** A `403` will still be a `403` on the tenth try; log it.
- **Cap the run.** "Fetch at most N pages" keeps a test cheap and keeps you a good citizen.

### Step 5 — Put it in the team's row format

The team agreed a schema. Every dataset should carry these five things:

| Column | Plain meaning |
|---|---|
| `posted_at` | when the job was advertised (the **timestamp**) |
| `location_city`, `location_province` | where the job is (the **location**) |
| `title`, `employer`, `sector`, `content`, `skills` | what the ad says (the **content**) |
| `ai_skill_required` + `ai_evidence` | does the ad ask for AI skills, and **which exact word** proved it |
| `domain` | **PUBLIC** (open portal, archive) or **PRIVATE-PLATFORM** (needs login/API/ToS permission) |

Two extra columns save arguments later: `posted_basis` (is the date exact, or derived
from "2 days ago"?) and `captured_at` (when *you* fetched it).

---

## 4. The Indonesia run, step by step

What the agent actually did, so you can copy the pattern.

```text
# 1. rules + reachability
GET https://karirhub.kemnaker.go.id/robots.txt        -> 200, "User-agent: *  Allow: /"
GET https://algolia.kemnaker.go.id                    -> DNS: no address
GET https://www.jobstreet.co.id                       -> 403
GET https://recruitment.bni.co.id                     -> 200, but Kalibrr app, no jobs in payload
GET https://karir.bca.co.id/candidate/api/jobs        -> 403  (only /city is open)

# 2. the route that worked: server-rendered posting pages
GET https://karirhub.kemnaker.go.id/lowongan-dalam-negeri            -> 8 posting links in HTML
GET https://karirhub.kemnaker.go.id/lowongan-dalam-negeri/lowongan/<slug>-<uuid>
    -> 200, Next.js payload contains title, employer, industry, region,
       publishedAt, expiresAt, quota, skills, description

# 3. harvest more links with the browser skill (keyword pages), then read each page
# 4. normalise to the team schema, flag AI skills with word boundaries, mark PUBLIC
# 5. build the HTML report + CSV, share the files
```

Result of that run: **331 postings** (281 live + 50 archived), **290 in finance/BPO
scope**, 144 banking / 118 BPO / 19 insurance, across 30 provinces, 20 Oct 2025 →
20 Oct 2026. Artefacts: `build/spar-id-postings.html` and
`data/id-postings/karirhub-id-postings-sample.csv`.

---

## 5. What "blocked" looks like — and what we did instead

Keep this table when you plan a new country. It saves a day.

| Route | Status in Indonesia | Why | Substitute |
|---|---|---|---|
| Karirhub search API (Algolia) | **BLOCKED** | DNS does not resolve from this network | Read posting pages directly |
| Kalibrr API / tenant job boards (e.g. BNI) | **BLOCKED** | Client-side app; KJS API returns 400/404 | Ask the platform, or skip |
| Bank career portals (BCA) | **BLOCKED** | Session token; 403 on vacancy endpoints | Per-bank permission |
| JobStreet / Indeed / LinkedIn | **BLOCKED** | Anti-scraping terms + 403 | Out of scope |
| Karirhub posting pages | **WORKS** | Server-rendered, public, robots-allowed | — |
| Wayback Machine captures | **PARTIAL** | Uneven coverage; only some months | Separate "archive" arm |
| Pasker ID / Satu Data Kemnaker | **AGGREGATE** | Official counts 2022–2024, no per-posting rows | Historical baseline only |

---

## 6. Two ways to run it

### A. Ask the agent (recommended for non-coders)

Paste this and fill in the brackets:

> Scrape **[site]** for **[country]** job postings in **[sector]** from **[start date]** to
> **[end date]**. First read robots.txt and tell me what is allowed, then probe the site and
> tell me which routes answer. Use only public pages — no login, no API key, no workarounds
> for a 403. Collect posting links, then read each posting page with a 0.4 s delay and a
> research User-Agent. Save a CSV with: posted_at, location_city, location_province, title,
> employer, sector, content (240-char snippet), skills, ai_skill_required with the exact
> matched word in ai_evidence, domain (PUBLIC or PRIVATE-PLATFORM), url, captured_at.
> Then build an HTML report showing coverage by month, sector split, the AI-flag counts and
> an ethics section, and give me the download links. Stop after **[N]** postings so it stays
> a feasibility test.

The agent will run everything in the sandbox and hand you links. You never see a command
line unless you open the Terminal tab.

### B. Run the script (for teammates who want to tinker)

`tools/scrape_karirhub.py` is the detail stage of the pipeline — stdlib only, no installs:

```bash
python3 tools/scrape_karirhub.py --out out.csv --max 25
python3 tools/scrape_karirhub.py --urls my_links.txt --out out.csv --finance-only --since 2025-10-20
```

It checks robots.txt, collects posting links from the seed pages, reads each posting page,
and writes the team schema. **Its limitation is honest and worth understanding:** the
category page only renders ~8 links, because the real search runs on the blocked Algolia
API. For volume, let the agent harvest links with the browser skill first, save them one
per line, and pass them with `--urls`.

---

## 7. Quality checks — do these before you send a number to anyone

1. **Open ten random rows and read them.** Does the title match the content? Is the
   location plausible?
2. **Look at the flag evidence.** Every `ai_skill_required = Yes` must name the word that
   triggered it. In Indonesia the first pass produced **four false positives**:
   - `komputer` — computer literacy in a teller ad, counted as AI;
   - `AIA` — an insurer's name, matched by the letters "ai";
   - `mengenai` — Indonesian for "regarding", which contains `g-e-n-a-i`.

   With word boundaries the honest count was **1 of 290**, not 5. A keyword count without
   evidence is a claim you cannot defend in a meeting.
3. **Chart by month before you believe anything.** In Indonesia, 187 of 290 rows were
   October 2026 — because open listings are the ones still online. That is a collection
   artefact, not a hiring boom.
4. **Check duplicates.** One employer advertising the same role in 32 cities is one job
   type, not 32 hiring decisions. Employer aliases (`PT X` vs `X`) are still unsolved.
5. **Say what the data is not.** Postings measure **advertised labour demand**. They do
   not measure hiring, filled roles or employment — the distinction the team flagged for
   the IMF-inspired scenario work.

---

## 8. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Dataset is empty, page looked fine in a browser | Client-side rendering | Use the `browser` skill (`action: "cdp"`) or find a server-rendered page |
| `403` on everything | Anti-bot or ToS | Stop. Ask the platform for access. Do not spoof headers. |
| Hostname does not resolve | DNS block on this network | Use an archive, or a different public route |
| Rows all from the last week | Open listings only survive while open | Add the archive arm; collect monthly going forward |
| Numbers look too high | Duplicates / one ad, many cities | Deduplicate on title + employer + content hash |
| AI flags look implausible | Substring matching | Word boundaries + `ai_evidence` + manual spot-check |
| Page loads but no JSON found | The site changed its framework | Ask the agent to re-inspect the HTML; do not hard-code a parser blindly |

---

## 9. Glossary (plain words, real terms kept)

- **Scraping** — reading public web pages with a program and turning them into a table.
- **robots.txt** — a file where a site says which pages robots may read.
- **Server-rendered** — the data is already in the HTML you download. Easy mode.
- **Client-side rendering** — the HTML arrives empty; JavaScript fetches the rows afterwards.
  Needs a headless browser, or a different page.
- **API** — a machine door into a site's data. Often needs a key, sometimes a paid one.
- **Headless browser** — a browser with no window (we use Lightpanda), so a program can
  load JavaScript pages and read the result.
- **CDP** — the protocol that lets a program drive that headless browser.
- **User-Agent** — the name a program gives when it requests a page. Ours says who we are.
- **Rate limit** — how often you may ask. We sleep ~0.4 s between pages.
- **Wayback Machine / CDX** — the Internet Archive. CDX is its index of *which* pages were
  captured and *when*.
- **PUBLIC vs PRIVATE-PLATFORM** — PUBLIC: open page or archive, no login. PRIVATE-PLATFORM:
  needs an account, a key, or the platform's permission.
- **Advertised demand** — how many jobs were *advertised*. Not how many people were hired.

---

## 10. Where things live

| Path | What |
|---|---|
| `tools/scrape_karirhub.py` | the runnable detail-stage scraper (this guide's example) |
| `data/id-postings/karirhub-id-postings-sample.csv` | the 331-row Indonesia dataset |
| `data/id-postings/README.md` | schema, provenance, ethics, limits, takedown |
| `build/spar-id-postings.html` | the visual report for that dataset |
| `build/spar-signal-feasibility.html` | the earlier aggregate (Pasker ID 2022–2024) feasibility test |
| `data/PERSONAL-DATA-STOP.md` | the project's hard rule on personal data |

**Rule of thumb for this repo:** if a scraped file has no provenance note, no ethics
section and no coverage caveat, it is not ready to share. The note is part of the dataset.
