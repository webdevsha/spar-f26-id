# Work log — everything built, 24–28 November 2026

One entry per artefact, in the order it was built.

---

[← Back to the README index](../../README.md)

---

## Work log — everything built, 24–28 November 2026

One row per artefact. Every row is a file in this repo, a PR, or an entry in
[docs/SHEET-WRITE-2026-11-24.md](../../docs/SHEET-WRITE-2026-11-24.md) — nothing here is a claim without an artefact.

### 24 November — the ground work

| What | Where it landed |
|---|---|
| **First shared-sheet writes**: signal layer + evidence columns in the Core file (`signals` O–T), the skeleton (`SIGNALS` H–K), and `IND team progress` G | Core file + skeleton · audit and revert ranges in [SHEET-WRITE](../../docs/SHEET-WRITE-2026-11-24.md) |
| **README header made true and readable by policymakers** — claims narrowed to what the data carries | PR [#33](https://github.com/webdevsha/spar-f26-id/pull/33) |
| **Live intake made always-on** — sandbox collector publishing to the Worker | PR [#34](https://github.com/webdevsha/spar-f26-id/pull/34) |
| **Source verification**: 22-row source matrix (5 status corrections, 2 attribution traps, 3 denominator traps), the Perplexity verification pack, and the BoxCompute collection briefs | [ID-SIGNAL-SOURCE-MATRIX](../../docs/ID-SIGNAL-SOURCE-MATRIX.md) · [ID-SIGNALS-PERPLEXITY-PACK](../../docs/ID-SIGNALS-PERPLEXITY-PACK.md) · [PROMPTS-BOXCOMPUTE-V2](../../docs/PROMPTS-BOXCOMPUTE-V2.md) |
| **Kemnaker's own portal counts, 2022–24** — the only free vacancy series that needs no scrape | [data/kemnaker/](../../data/kemnaker/) |
| **Postings at scale**: Karirhub 13,308 and Dealls 44,417 distinct URLs proven collectable; 2,618 rows in the team schema (2024 → Oct 2026) | [data/id-postings/](../../data/id-postings/) · [build/spar-id-postings.html](../../build/spar-id-postings.html) |

### 26 November — the indicator table, and the register made navigable

| What | Where it landed |
|---|---|
| **`SIGNALS_ID` built**: S1–S10 each mapped to an Indonesia indicator, the name linked to the exact register row it came from, the source compiled once per shared indicator so the same indicator reads identically everywhere | Skeleton `SIGNALS_ID` · [SHEET-WRITE](../../docs/SHEET-WRITE-2026-11-24.md) |
| **Policy de-coded**: every instrument named in full with its acronym (`UU 27/2026`, `POJK 11/POJK.03/2022 and PADK OJK 1/2026`, `JKP (PP 37/2021)`, `Stranas KA 2020-2045`), hyperlinked, with titles and status in the tab's own `README` | Skeleton `README` + `SIGNALS_ID` G |
| **The one long review column split three ways** — *Verdict · Capability · Details*; full reading on the first row of each signal, one-line pointer on the rest; the broken S8 pointer rebuilt; duplicates and dead weight cleared | Skeleton `SIGNALS_ID` H–J |
| **Every reading reframed to the team's question** — each Details line closes on what the row cannot tell us about an AI economic shock | Skeleton `SIGNALS_ID` H–J |
| **Float-up highlighting**: rose = the shock would be invisible (S1, S3, S4); amber = the number exists but cannot be read as an AI shock alone (S5–S10); plain = S2 — with the key stated once on the tab `README` | Skeleton `SIGNALS_ID` A–M + `README` |
| **Task progress re-tallied** from the indicator table | PR [#35](https://github.com/webdevsha/spar-f26-id/pull/35) |
| **Part 4 v1 written** — who can act and the policies in place, reframed to the shock question, three flags for Ian, word count stated honestly against the 600-word target | [ID-PART4-DRAFT](../../docs/ID-PART4-DRAFT.md) · PR [#36](https://github.com/webdevsha/spar-f26-id/pull/36) |
| **Part 4's data into the register**: `Indonesia policy inventory` 3 → **16 rows**; `instruments` DEMO placeholder → **6 real levers**, one per actor's door, each citing the row it rests on | Core file · PR [#36](https://github.com/webdevsha/spar-f26-id/pull/36) |
| **Cross-tab navigation**: 134 hyperlinks so a policy name opens its register row, a signal code its definition, an actor its lever and a lever back to the actor; `SIGNALS_ID` column G re-linked **per instrument** (18 cells / 55 spans, wording untouched) | Three sheets · PRs [#36](https://github.com/webdevsha/spar-f26-id/pull/36), [#37](https://github.com/webdevsha/spar-f26-id/pull/37) |
| **The register now generates the map**: `build/sync_map_from_register.py` (`--check` = drift report) rebuilt the map's policy nodes 9 → **22** — 8 hand-written nodes kept with their detail, 8 added, 6 lever nodes replacing the stale placeholder; bands, edges, marks and the responsibility map untouched | PR [#36](https://github.com/webdevsha/spar-f26-id/pull/36) |
| **README given the tab directory**: every tab's deep link, plus the cross-tab link graph | PR [#37](https://github.com/webdevsha/spar-f26-id/pull/37) |
| **Call run sheet** for the 22:00 SPAR call — six do-now items, six raise-on-call items, the numbers at hand, the two decisions needed | [ID-CALL-RUNSHEET-26NOV](../../docs/ID-CALL-RUNSHEET-26NOV.md) |

### 28 November — the product proposal

| What | Where it landed |
|---|---|
| **Studied `scenarios-2030.windfalltrust.org`** (home, a scenario page, compare, methodology) and distilled ten communication patterns that work for a policy reader — the load-bearing ones: a quadrant deliberately left empty *with its reason*, a scenario range always printed next to a real number, and gaps drawn as dotted segments rather than footnoted | [ID-POLICY-SITE-PROPOSAL](../../docs/ID-POLICY-SITE-PROPOSAL.md) §1 |
| **Refused what we cannot honestly copy**: signed workshop ranges, monthly official series, status-quo policy | §2 |
| **Proposed one product, seven routes** — five of which already have a built artefact in this repo; the genuinely new page is `/compare` | §3 |
| **Scenario axes our evidence can carry**: pace of AI deployment in banking (S1–S3) × strength of the adjustment buffer (S8, S10, readiness) — four worlds, one deliberately undrawn, three variants that each break one assumption | §4 |
| **Evidence grammar per number**: real / team-reported / gap / demo, with H–M–L confidence and a checked-on date; unsigned bands print `bracket pending`, never a midpoint | §5 |
| **Wireframe** — one light-theme page showing the hero, the four tiered findings, the 2×2 with its hatched "not covered" quadrant, the outlook strip and the compare strip | [build/proposal-wireframe.html](../../build/proposal-wireframe.html) |
| **Five gates named**, each a question for a person rather than for the drafting lane | §8 |
| **This work log**, the file-index corrections and the PR status fixes | PR [#38](https://github.com/webdevsha/spar-f26-id/pull/38) |

### Still open, stated plainly

| Item | State |
|---|---|
| `sync-sheets` hourly job | **failing** — the repo CSVs were mirrored by hand; the 29 Nov freeze depends on this |
| Cloudflare deploy of the overview and the new pages | not deployed; `dist/` is generated output and deploy needs an explicit go-ahead |
| `Read Me_Methods` tab in the team indicator workbook | **empty** — the methodology page has nothing to render from |
| Every indicator threshold | `Deferred` — the compare page cannot draw a line it does not have |
| Readiness questions `q1`–`q6` | not recorded anywhere, so the buffer axis is half-blind |
| `M6` in the measure register | has no row in `SIGNALS_ID` |
| Scenario bands | unsigned — they belong to the team, not to the drafting lane |
| Last three items to verify with Ian, Napat and Akbar | needs the SPAR call |
