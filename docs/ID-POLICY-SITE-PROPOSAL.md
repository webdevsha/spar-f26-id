# Proposal — an Indonesia AI × Banking Jobs Monitor (policy-facing report site)

**For:** SPAR Fall 2026 · Economic Shock Team · Indonesia lane
**Author:** CRO-chan (draft for Shafira) · **Date:** 26 Nov 2026
**Status:** proposal — no build, no deploy, no decision taken on your behalf
**Inputs studied:** `scenarios-2030.windfalltrust.org` (home, one scenario page, compare, methodology) ·
Core file (9 tabs) · `SPAR indicator table — ID + PH (draft 26 Nov 2026)` (51 rows, ID-01…ID-25, PH-01…PH-25) ·
repo artefacts (`spar-id-overview`, `spar-id-ecosystem-map`, `spar-id-model-demo`, `spar-id-postings`,
`spar-signal-feasibility`)

---

## 1. What the Windfall site does that actually works

I read the site as a *communication instrument*, not as a design. Ten patterns, in the order a reader meets them.

| # | Pattern | Why it works for a policy reader |
|---|---|---|
| P1 | **Summary layer over a report.** The site is the summary; "Download full report" carries the method. | Two audiences, one source. A council member reads 6 minutes; a staffer checks the appendix. |
| P2 | **One framing sentence + exactly two CTAs** above the fold ("How adoption and competition could shape growth, jobs, and who benefits" → Explore ↓ / Download). | No menu archaeology. The reader knows what this is in one line. |
| P3 | **Two named dimensions, everything else held fixed**, drawn as a 2×2. | Reduces an unbounded argument to a thinkable space. |
| P4 | **One quadrant is deliberately empty — and says why.** "Not Covered … competition would likely cut prices and speed adoption toward Open Competition." | This is the single most credible thing on the site. Naming what you did not model buys trust for what you did. |
| P5 | **Quadrant cards carry a glyph** (circles = how concentrated the gains are). | Carries the distributional claim visually, before any number. |
| P6 | **Scenario pages open with an outlook strip**: 6 indicators, each "scenario range + latest actual + link". | The bracket sits *next to* the real number, so the reader can see the size of the claim. |
| P7 | **Compare page**: indicator switcher → history line + scenario bands → footnoted definition per indicator; **"Data gap · hover the dotted segment"**. | Gaps become part of the chart, not a footnote nobody reads. |
| P8 | **Every claim hyperlinked to a primary source**, with a "Definitions and Sources" block doing the heavy lifting. | A staffer can verify in one click. That is the whole game in policy work. |
| P9 | **Named variants that break one assumption** (*Investment Bust*, *On the Path Toward Superintelligence*). | "If we are wrong, here is the shape of wrong." |
| P10 | **Methodology page**: purpose, how developed, research foundations (what others already did), why these two dimensions, shared assumptions, calibration, and an explicit *what we do not model*. | Armour. It is what stops the first hostile question. |

**Illustrative-not-forecast disclaimer** is used consistently and precisely ("ranges are illustrative,
not forecasts; they hold today's policies in place"). That sentence is doing real work.

## 2. What we must not copy

| Their situation | Ours |
|---|---|
| A two-day workshop produced defensible ranges, then indicators were fitted to the scenario logic. | **We have no workshop output and no signed bands.** Any bracket we print would be invention, so brackets must stay visibly *unsigned* until the team signs them. |
| Seven of their indicators are monthly official series with published history. | **Most of our rows are annual, one-off, or team-reported-unverified.** `ID-13` (finance-sector employment) is still team-reported; `ID-09` portal counts are unverified; `ID-08` is a confirmed gap. |
| They assume policy stays at status quo. | We **cannot** — `UU 27/2026` landed on 28 Oct 2026 with no transition period and implementing rules not due until 28 Oct 2027; `PP 6/2025` already moved the claims series on 7 Feb 2025. Policy is inside our data. |
| Their gap is a US government shutdown (one dotted segment). | Our gaps are **structural**: no adoption rate is required of anyone (`S3`), no AI-linked forecast exists (`S4`), no instrument tracks a worker after dismissal (`S9`). |

So the spine of our site is **not** scenario drama. It is **evidence status**. That is also the thing an
AI council cannot get anywhere else, and it is the thing our register is uniquely able to show.

## 3. The product

**Working name:** *Indonesia Banking & AI Jobs Monitor, 2026–2030* — one site, seven routes, one download.

| Route | Windfall analogue | What it carries | Fed by | Status |
|---|---|---|---|---|
| `/` | home | Framing sentence · the four float-up findings · scenario matrix · download | `SIGNALS_ID` verdicts | to build (thin) |
| `/overview` | home lede | The banking job market in Indonesia: 22 signals, headcounts, branch counts, postings, wages | `signals`, `id-postings` | **exists** — `spar-id-overview.html` |
| `/adoption` | dimensions | S1–S4: capability milestones, disclosed systems, adoption stage, user share | `ID-01`…`ID-08` | **partly exists** (inside overview) |
| `/indicators` | compare (table half) | The signal → indicator → verdict table, ID-01…ID-25, with PH-01…PH-25 as the comparison lane | `2_INDICATOR_TABLE` | **exists as sheet** — needs a page |
| `/scenarios` | matrix + 3 scenario pages + 3 variants | Four quadrants, one "not covered", per-scenario outlook strip | `model-id-demo.json` + new `scenarios-id.json` | **partial** — `spar-id-model-demo.html` has signal → trigger → shock |
| `/compare` | compare | Indicator bands vs latest actual, dotted where unverified, definitions underneath | new `scenarios-id.json` | to build |
| `/ecosystem` | (no analogue) | Ecosystem map · policy inventory (16) · readiness · levers (6) · who-can-act (6) — all clickable | `ecosystem-id-map.json` (now generated from the register) | **exists** — `spar-id-ecosystem-map.html` |
| `/methodology` | methodology | Methods, sources, check log, what we do not model | collection tab + `SHEET-WRITE` log | **gap** — `Read Me_Methods` is empty |
| `/report` | Download full report | The country report: Parts 3–8 as one PDF | `docs/ID-PART*.md` | **partial** — Parts 3, 4, 8 drafted |

Note the shape: **five of nine routes already have a built artefact.** The proposal is therefore mostly
joining, framing and one genuinely new page (`/compare`), not a rebuild.

## 4. Scenario design that our evidence can carry

Windfall varies *adoption pace × market structure*. Market structure has no Indonesian banking analogue in
our register — we hold no data on AI-model concentration. Substituting it would be an invented axis.

**Proposed axes, each traceable to rows we already own:**

- **Axis A — pace of AI deployment in banking.** Evidenced by `S1` (capability milestone — what a machine
  can now finish), `S2` (systems banks disclose), `S3` (34% pilot / 18% operational / 4% across functions,
  Oct 2026; governance maturity 2.74/5).
- **Axis B — strength of the adjustment buffer.** Evidenced by `S8` (JKP: 90,513 workers, Rp1.01 trillion,
  2025; 60% of wage for up to 6 months; 3-working-day standard), `S10` (Prakerja, PEKA 4,336 participants,
  BCA 2,550 trained) and the **readiness score — currently unscored**. The hole is drawn, not hidden.

|  | **Buffer holds** | **Buffer thin** |
|---|---|---|
| **Deployment slow** | *Managed Adjustment* — hiring thins, exits absorb it, claims rise gently | *Quiet Squeeze* — hiring thins, nothing catches it, claims rise unseen |
| **Deployment fast** | *Absorbed Shock* — displacement real, JKP/Prakerja visibly load-bearing | *Few Winners, Many Leavers* — the float-up world: series break exactly when you need them |

**"Not covered" quadrant (in the Windfall manner):** fast deployment with an untested buffer is *not*
drawn as a fifth world, because our buffer evidence (`S8` self-reporting, `S9` no destination tracking)
cannot distinguish "the buffer worked" from "we stopped looking".

**Three variants — each breaks one assumption:**

1. **Capability break.** One bank automates a whole clerical function. What would we see? By `S1`'s own
   verdict, *nothing domestic* — the site's most uncomfortable page, and its most useful.
2. **Rule break.** `UU 27/2026`'s implementing rules arrive early, or a `PP 6/2025`-style amendment moves
   the claims series again → any 2025-vs-2026 comparison is void. Carries the exact break dates.
3. **Measurement break.** A Sakernas round is missed or an item is redefined — Windfall's dotted-segment
   pattern, applied to the series we actually rely on for the denominator.

**Hard rule for all of it:** indicator rows show `Threshold: Deferred` as *deferred*. The compare page must
be able to say "no threshold has been agreed" rather than imply one by drawing a line.

## 5. Evidence grammar — the thing that makes this policy-grade

Every number on the site wears four marks, and the legend is stated once:

| Mark | Meaning | In our data |
|---|---|---|
| ● | Real, checked, dated | `ID-17` JKP recipients (checked), `ID-15` bank offices (checked against two outlets), `ID-22` unemployment 4.68% |
| ◐ | Team-reported, unverified | `ID-13` finance-sector employment 1.65m, `ID-09` portal counts, `ID-04` named systems |
| ○ | Gap — nothing exists | `ID-08` (no AI-linked outlook), and the whole of `S3`/`S4` as *duties* |
| ▨ | Demo / illustrative | model demo inputs, unsigned scenario bands |

Each row also carries **H/M/L confidence** and a **"checked 26 Nov 2026"** stamp — we already hold these in
the collection tab, so the site can print provenance per number rather than per document. That is the
difference between our product and every other AI-and-jobs site: not more numbers, *signed* numbers.

## 6. Design system (house style, light only)

- Headings Georgia; body Arial; hairline rule under each section head; accent crimson `#b3122a`.
- **Light theme only** — no dark panels, no black hero. Tinted table header rows (`#f6f1ea`).
- Evidence tints: ● white · ◐ amber `#fff2cc` · ○ rose `#fce8e6` · ▨ hatched, never solid.
- Ranges printed as `4.68% — bracket pending` and never as a fabricated midpoint.
- One glyph per quadrant for the distributional claim (buffered vs passed-through), the way Windfall uses
  circle size.
- Print stylesheet for `/report`, because councils still circulate PDFs.

## 7. Build plan

| Phase | Work | Reuses | New |
|---|---|---|---|
| **1 · Shell** | One navigation + footer joining the five existing pages; `/` with framing sentence and the four float-up findings; evidence badges on every indicator row | overview, ecosystem-map, model-demo, postings, feasibility | `build/site_shell.py`, `data/evidence-legend.json` |
| **2 · `/compare`** | Indicator switcher, history line, unsigned band, dotted unverified segments, footnoted definitions | `2_INDICATOR_TABLE` (25 ID rows) | `data/scenarios-id.json` (bands left as `null` until signed) |
| **3 · `/scenarios`** | The 2×2, four quadrant pages, three variants | `model-id-demo.json` signal → trigger → shock | `data/scenarios-id.json` variant blocks |
| **4 · `/methodology` + `/report`** | Methods page written from the collection tab and check log; country report assembled from Parts 3–8 | `1_COLLECTION` check column, `SHEET-WRITE` audit | `docs/ID-REPORT-ASSEMBLY.md`, print CSS |

Nothing in phases 1–4 requires a decision from you beyond "go"; phases 2–3 require the gates below, and I
would rather the site show an empty slot than a number I invented.

## 8. The gates — who has to answer what

| Gate | Why it blocks the site | Who |
|---|---|---|
| **`Read Me_Methods` is empty** | `/methodology` is the page that survives hostile scrutiny; I can draft from the collection log, but the team's method statement is not mine to write | Akbar / Ian |
| **All thresholds `Deferred`** | `/compare` cannot draw a threshold line it does not have; if none will be agreed by 14 Dec, say so and the page states it | Ian / Natraj |
| **Readiness `q1`–`q6` missing** | Axis B (the buffer) is half-blind without them; the sheet holds only codes | Akbar |
| **`M6` has no row** | The six-measure register reads one short; a reader will notice | Ian |
| **Scenario bands unsigned** | Bands must be owned by the team, not by me. Until signed, the site prints `bracket pending` | Natraj / Ian |

## 9. How this speaks to an AI council specifically

Three moves, in this order, because a council's first question is always "what should we do":

1. **Lead with what Indonesia cannot currently see.** Not "AI may displace bank clerks" but *"no
   instrument in Indonesia requires anyone to report an AI adoption rate; the claims series carries two
   legal breaks; nothing follows a worker after dismissal."* Every one of those is a sentence a council
   can act on.
2. **Put the asks in one table with an owner and a date** — the `who-can-act` tab already holds the six
   bodies and their doors, so the same data that draws the ecosystem map produces the ask list.
3. **Show the measurement gap as the finding.** The honest headline of this study is that the shock would
   arrive before the statistics would show it. That is a stronger, more defensible claim than any scenario
   range, and it is the one thing we can prove today with 25 verified indicator rows.

---

## Appendix A — what I read, and what I did not

- Read in full: Windfall home, `few-winners`, `compare`, `methodology`.
- Read from our side: `2_INDICATOR_TABLE` (51 rows), `1_COLLECTION` (25 rows), all nine Core-file tabs,
  and the five built pages' section structure. `Read Me_Methods` returned **zero rows** — flagged as a gate.
- Not done, deliberately: no scenario numbers invented, no bands set, no page deployed, nothing merged.

## Appendix B — the one-page wireframe

`build/proposal-wireframe.html` — a single light-theme page showing the hero, the 2×2 with its "not
covered" quadrant, one scenario outlook strip, the evidence legend and the compare strip, using **only
numbers already verified in the register**. Unsigned bands are drawn as `bracket pending`.
