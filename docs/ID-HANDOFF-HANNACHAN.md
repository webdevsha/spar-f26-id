# Handoff — SPAR Fall 2026 Indonesia lane · pending items
**From:** CRO-chan (research synthesis) · **To:** Hannachan (EA continuity) · **Date:** 24 Nov 2026
**Why this file:** so the open items can be continued without re-deriving them. Everything below is
verified against the live sheets, the repo and the plan deck on 24 Nov. Self-contained: no other
context needed.

---

## 1. What this work is (six lines)

SPAR Fall 2026, Economic Shock Team. Two country cases: Philippines (IT-BPM) and **Indonesia
(banking & finance)**. Shafira is the **Indonesia Data Lead** and co-author of the SPAR report.
Demo Day 19 Dec; SPAR submission 14 Dec. The plan's checkpoints were **Sat 14 Nov · Sun 22 Nov ·
Sun 29 Nov · Wed 2 Dec**. One finding is being tested: *AI uptake and hiring move first, jobs and
pay next, job-loss claims and official unemployment last.*

## 2. Where the truth lives (open these before changing anything)

| What | Where |
|---|---|
| Signal register (22 Indonesia rows) | Sheet `1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k`, tab `signals` (gid `838965401`) — columns O–T are new: `link`, `source_verbatim`, `confidence`, `data_status`, `not_verified`, `source_checked` |
| Team signal skeleton S1–S10 | Sheet `1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo`, tab `SIGNALS` — columns H–K are new (Indonesian evidence, source, status, gap/route) |
| Team task tracker | Sheet `1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ`, tab `Sheet1` — column G `Comments` is new |
| Verification run (Perplexity, 22 rows + 5 figures + request routes) | `data/id-postings/perplexity-id-data.md` in the repo |
| Source matrix v2 (the analysis of that run) | `docs/ID-SIGNAL-SOURCE-MATRIX.md` |
| Repo | `github.com/webdevsha/spar-f26-id`, branch `cro/id-signal-source-matrix`, **PR #15** (PR #14 already merged) |
| Sheet-write audit + revert instructions | `docs/SHEET-WRITE-2026-11-24.md` |

## 3. Closed — do not redo

| Item | Closed by | Artefact |
|---|---|---|
| Data list: every signal → data status, source, confidence, gap | 24 Nov | Core file `signals` cols O–T; matrix v2 |
| Karirhub reading (counts, entry-level share, AI mentions) | 24 Nov | `build/spar-id-postings.html` (live); Kemnaker's own counts downloaded |
| Job-postings dashboard | live | `https://spar-f26-id.pages.dev/build/spar-id-postings` |
| Verifying the register's source line | 24 Nov | `docs/ID-SIGNAL-SOURCE-MATRIX.md` (5 status corrections; 2 attribution traps; 3 denominator traps) |

## 4. Open — the actual work

| # | Task | Due | Done looks like | Owner | Blocker |
|---|---|---|---|---|---|
| 1 | **Country Report Part 3 — what the signals show now (700w)** | 22 Nov (overdue) | Section the Indonesia chapter can absorb | Shafira reviews | none — **draft is written**, `docs/ID-PART3-DRAFT.md` (678 words) |
| 2 | **Country Report Part 4 — who can act, policies in place (600w)** | 22 Nov (overdue) | 600 words naming bodies, instruments, gaps — one voice with Ian | Shafira + Ian | none — the who-can-act map and request routes are ready to write from |
| 3 | **Policy readiness review — 3 documents × 6 questions** | overdue since 26 Oct | Every policy row scored, blind spot named | Shafira | **needs the six readiness question texts** (not recorded anywhere; the tab holds only `q1`–`q6` as column names). Worksheet ready: `docs/ID-READINESS-WORKSHEET.md` |
| 4 | Purchased-data licence scope — what the licence allows, written down | 14 Nov | A one-page licence note | Shafira + Akbar | not recorded yet |
| 5 | Ask BPS or Kemnaker about data gaps, in one interview | by 27 Nov | One interview, question asked | Shafira | SPAR still confirming interview access; question drafted (data-availability framing) |
| 6 | Shared sheet frozen into the AISA repo | **29 Nov** | Sheet and repo in step | CTO lane | **sheet→repo job failing hourly** |
| 7 | Decision calendar — confirm dates and owners (6 windows) | with the 22 Nov pack | 6 windows, confirmed | Shafira + Rachel | none |
| 8 | Signal watchlist — log new observations | ongoing | New observations added | Shafira + Ian | none |
| 9 | SPAR report §5 Indonesia (2,500w) | Wed 2 Dec → Rachel | Chapter in Akbar's single voice | Akbar (lead), Natraj, Shafira | none |
| 10 | SPAR report §8 Limits and next steps (300w) | Wed 2 Dec | 300 words | Shafira + Napat | none |
| 11 | Atlas site page | Jan 2027, AISA consent | Published page | Shafira | publication is consent-gated |

## 5. The two infrastructure failures in front of the work

1. **`sync-sheets` fails on every hourly run** — step *Sync tabs to CSV* succeeds, step *Commit if changed* fails. Effect: the repo's `data/*.csv` no longer mirrors the sheets (repo holds 9 signal rows against the tab's 22), so the dashboard reads stale data, and **item 6 cannot proceed**.
2. ~~**Cloudflare Pages deploy fails authentication (code 10000)** since 5 Nov.~~ **Retracted 28 Nov 2026:** deploys were verified working — `wrangler pages deploy` uploaded 30 files plus the Functions bundle and published deployment `6bf9dacb`. The token in `~/.hermes/.env` authenticates; `./deploy.sh` stages `app/` as the site root and keeps the generated dashboard at `/dashboard.html`. The public report and map URLs remain HTTP 200.

Both are **CTO / `@misshanna_bot`** lane: a Cloudflare API token regeneration with no expiry, and the
GitHub push credential for the sync job.

## 6. Boundaries — apply these without asking

- **Nothing external is sent without Sha's explicit go-ahead in the conversation that contains the request.** No emails, no messages, no posts, no form submissions.
- **Route to @clo before anything regulator-facing leaves the team.** The verification run produced **15 formal information requests** to BPJS, OJK, Kemnaker, BPS and DPR Commission IX, and raised a scope question about platform data obtained via web archives (LinkedIn/JobStreet-class). A request in the study's name creates a record. **None have been sent.**
- **Never fabricate a citation, a named person, a figure or an incident.** Unverified figures stay marked `[unverified — confirm]` or "not verified" — that is the register's discipline, not a placeholder to smooth over.
- **Grades documents, never a government.** No ranking, no scoring of institutions, in anything that leaves the team.
- **No personal data.** Aggregates and totals/shares only, never raw individual job ads, in anything shared beyond the team.
- **Light theme only** in any deliverable UI.
- **Do not change `Progress` or `Status` in the team tracker** — those are judgements about people's work. Comments and links are fine.
- **Do not commit or deploy without instruction.** Work on `cro/id-signal-source-matrix`; a new PR is needed once PR #15 is merged.
- The sealed topic is not referenced under any framing.

## 7. What is needed from Sha before the overdue items can close

1. **The six policy-readiness question texts** (item 3) — paste them or name the doc holding them. Everything else in that item is prepared.
2. A yes/no on whether comments should also cover the rows where she is a co-PIC (tracker rows 10 and 13).

## 8. Suggested order (shortest path)

1. **Part 3 read-through** — the draft exists; 20 minutes of her attention, not a rewrite.
2. **Part 4 with Ian** — assembly from the map and routes already collected.
3. **Readiness scoring** — five minutes to paste the question texts, then mechanical scoring against collected evidence.
4. **Licence note** with Akbar — short.
5. **Interview question** to SPAR/BPS — due Fri 27 Nov, not tonight.
6. **Escalate the two infrastructure failures to CTO** — they gate item 6 (29 Nov) and every page going online.

---
*Compiled by CRO-chan, 24 Nov 2026, from: the plan deck (22 slides, updated 16 Nov), Core file
`signals` (22 rows), the Perplexity verification run, Kemnaker's public CSV downloads, the team
tracker, and repo/CI state. Figures quoted here are only those already verified in the register.*
