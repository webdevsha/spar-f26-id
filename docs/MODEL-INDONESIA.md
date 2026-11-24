# A small model for the Indonesia case

**How to take the scenario-based structural proposal and run it on Indonesia.**

Source: `SPAR_Model_Proposal_V1.pdf` ("AI, Employment, and Labor-Market Resilience in the
Philippines and ASEAN"). That proposal is written around the Philippines. This document maps
it onto the Indonesia lane, says exactly which Indonesian numbers exist today, and lists what
still has to be scraped or requested before the model can be calibrated rather than assumed.

Companion artifact: `build/spar-id-model-demo.html` \u2014 the interactive demo built from
this design, showing the current-data case and the with-more-data case side by side.

---

## 1. Why a small model, and why this one

The proposal's own discipline is what makes it tractable: it does **not** try to invent a new
structural model or produce a single headline forecast. It keeps the well-established chain

```
AI shock -> labour demand -> displacement -> micro (search) -> iota (matching) -> employment, unemployment, wages
                                                   s_L -> labour's share of output -> wages
```

and asks what happens under different assumptions. Three parameters carry the analysis:

| Parameter | Meaning | Where it acts |
|---|---|---|
| `s_L` | Labour share of income | Distribution of output \u2192 wages |
| `\u00b5` | Occupational mobility in the search process | Can displaced workers search in another occupation? |
| `\u03b9` | Curvature of the matching function | How sharply does worker\u2013vacancy imbalance bind? |

Everything else \u2014 exposure, employment, GDP, vacancies, wages \u2014 is meant to be
**measured or calibrated from local data**, not theorised. That is the discipline this document
follows: *estimate what the data can identify, calibrate what must be assumed, stress-test the
assumptions that matter.*

For Indonesia this matters because the three parameters interact with two features the proposal
flags for ASEAN generally and Indonesia exhibits sharply:

1. **A large informal sector.** 87.74m informal vs 59.93m formal workers (Feb 2026, BPS). The
   matching model is a *formal* labour-market model: JKP claims and vacancy postings only see
   the formal side. \u00b5 is therefore an estimate of mobility within the observed part, and
   the informal destination is an unmodelled sink. This must be stated, not hidden.
2. **A structural break in the safety net.** PP No. 6 of 2025 (effective 7 Feb 2025) changed
   JKP generosity, claim timing and contribution conditions. Any calibration that uses JKP
   claim volume across 2024\u201325 is reading a rule change, not only a labour-market change.

## 2. The Indonesian instantiation

Same chain, Indonesian objects. Set the anchor sector as **finance & insurance (banking)**,
with clerical support as the exposed occupation group \u2014 consistent with the ecosystem and
policy maps.

### 2.1 What we already have (in this repo or cited by it)

| Object | Indonesian value we hold | Source |
|---|---|---|
| Anchor sector size | **1.65m** employed, finance & insurance, Aug 2025 | BPS Sakernas, via `data/id-signals.csv` |
| Exposure, sector | **21.7%** of jobs above-minimal GenAI exposure | ILO method, via `id-signals.csv` |
| Exposure, occupation | **93.9%** of clerical support workers have some exposure | ILO method, via `id-signals.csv` |
| Vacancies (sample) | **331** individual postings, finance/BPO, one-year window | `data/id-postings/` (this lane's harvest) |
| Sector composition of that sample | Banking 144 \u00b7 BPO 118 \u00b7 Insurance 19 | `id-postings/summary.json` |
| Employer AI deployment | 5 banks, named use cases (DIVA, VIRA, Kopra, Sabrina, BRIBRAIN) | `id-signals.csv` |
| Capacity substitution | Sabrina: 45% of 21,535,701 Contact BRI interactions | `id-signals.csv` |
| Internal upskilling | BCA: 2,550 employees received AI-related training, 2025 | `id-signals.csv` |
| Separations (claims) | 431,086 claim cases (2025); 90,513 distinct recipients (2025) | BPJS Ketenagakerjaan, via `id-signals.csv` |
| Access friction | 17% of JKP applications rejected, May 2025 hearing | `id-signals.csv` |
| Informal share | 87.74m informal vs 59.93m formal, Feb 2026 | BPS, via `id-signals.csv` |
| Training programme (new) | 50,000 laid-off workers, 21 centres, priority for non-JKP | setkab.go.id, 22 Oct 2026 |

### 2.2 The parameter-by-parameter plan

**`s_L` \u2014 labour share.** Indonesian source: BPS national accounts, compensation of
employees \u00f7 gross value added, for finance & insurance specifically (not the whole economy
\u2014 a national `s_L` would drown the sector signal). The proposal's illustrative 0.60 \u2192 0.45
is a *scenario*, not an Indonesian estimate; the Indonesian baseline must be read off the
accounts. Status: **not yet collected.**

**`\u00b5` \u2014 occupational mobility.** The proposal is explicit that the baseline should be
calibrated from *observed occupational transitions*, and equally explicit that `\u00b5` is not the
literal probability of switching occupation but a parameter governing how effectively one group
searches in another's market. Indonesian source: the previous-job / job-change variables in
Sakernas microdata (region \u00d7 occupation \u00d7 industry cells), which SILASTIK catalogues.
Status: **must be requested**; nothing in the current repo measures transitions.

**`\u03b9` \u2014 matching curvature.** No Indonesian estimate is proposed; take the literature
benchmark and vary it (0.5 / 1.27 / 2.0 as in the source) as sensitivity. Status: **assumed,
by design.**

**Vacancies `V` and searchers `S`.** This is where this lane has an unusual advantage: it has
already harvested real postings, and it holds a claims series. `V` can be built from Karirhub
postings *if* a trend can be extracted; `S` from JKP claim/recipient flows. Both currently
have the same fatal flaw \u2014 see \u00a73, item 2.

**Matching efficiency `\u03c7`.** Not separately identified at this stage; folded into the
scenario range rather than estimated. State that on the record.

---

## 3. What we still need \u2014 and two problems in what we already have

Listed in the order they block the model. "Scrape" = this lane can harvest it from public
sources. "Request" = needs an institutional ask (see `build/spar-id-ecosystem-map.html`, map 3,
for who to ask and why they would answer).

### Two problems in the current data, stated plainly

**Problem 1 \u2014 the AI-skill flag does not work yet.** Of 288 in-scope postings, **1** is
flagged `ai_explicit`; 31 are `digital_basic`, 9 `data_skill`, 247 `none`. The flag is a keyword
matcher over posting text, and posting text almost never names AI even when the role is exposed.
Reading exposure off these flags would understate it by an order of magnitude. **Fix:** stop
keyword-matching and map Kemnaker occupation codes (KBJI/ISCO) onto the ILO Gmyrek exposure
index instead \u2014 the crosswalk is the method that already produced the 21.7% / 93.9% figures
in `id-signals.csv`. The flags stay as a secondary signal only.

**Problem 2 \u2014 we have a sample, not a time series.** 187 of 331 rows carry capture month
2026-10, with only 6 rows in 2025-10. That is a *harvest artifact*: the live arm was read
recently, so recent postings dominate. The archive arm (50 rows) is the only part with genuine
historical depth and it is thin. **A vacancy trend cannot be built from this.** Do not plot it
as a trend. **Fix:** a back-series harvest (below, item 1).

Both problems matter because `V` \u2014 vacancies \u2014 is one of the two inputs to the
matching function. An unusable `V` means `\u03b9` cannot be exercised against Indonesian data at all.

### The priority list

| # | What | Mode | Why it blocks the model | Blocker / route |
|---|---|---|---|---|
| 1 | **Karirhub back-series** \u2014 postings by month over 3+ years | scrape | Without it `V` has no trend and `\u03b9` has no Indonesian test | The Algolia search backend is unreachable from the build network; the current workaround (harvest detail-page URLs) only reaches recent listings. Needs an index/sitemap route or archive-depth harvesting |
| 2 | **Occupational transitions** \u2014 previous-job variables, repeated cross-sections | request | This is the *only* proposed calibration source for `\u00b5` | BPS / SILASTIK microdata access |
| 3 | **JKP claims by province and industry** | request | Denominators `S` at the geography that matters; enables the province concentration the trigger runs on | BPJS Ketenagakerjaan programme office; occupation detail currently unconfirmed |
| 4 | **Compensation of employees + GVA, finance & insurance** | scrape/request | This *is* the `s_L` baseline; without it `s_L` is an assumption pretending to be a number | BPS national accounts (public tables first, microdata if needed) |
| 5 | **Bank workforce by function/type over time** | request | The one series that could validate "deployment changed this function" | OJK supervision; PERBANAS or a bank-segment body to convene |
| 6 | **AI use-case extraction at scale** \u2014 annual/sustainability reports, all listed banks | scrape | We have 5 banks by hand; a dated deployment panel needs systematic extraction | Bank IR pages / IDX disclosures; PDF text extraction |
| 7 | **Posting wage fields** \u2014 normalise the salary column | scrape | Wage channel needs it; 278 of 331 rows carry a salary string | Already in the harvest; needs parsing to a numeric band, plus a decision on `Dirahasiakan` (6 rows) |
| 8 | **JKP processing latency** \u2014 applications \u2192 approvals \u2192 first payment by cohort | request | Measures support capacity (M5), the constraint that turns a displacement into a prolonged one | BPJS administrative records |
| 9 | **Training places vs placements** \u2014 the 50,000-worker programme and PEKA | request | Distinguishes capacity from participation; completion can substitute for outcome | Kemnaker + training centres |
| 10 | **Felden AIOE / ILO exposure crosswalk onto KBJI** | scrape | Fixes Problem 1 above; converts the postings corpus into an exposure-weighted panel | Public methodology + published crosswalk tables |

Items 1, 4, 6, 7 and 10 are **within this lane's own reach** \u2014 public sources, no permission
needed. Items 2, 3, 5, 8 and 9 need an institutional ask, which is what the bridge map is for.

## 4. What "small" means here, concretely

Deliberately bounded, so it can actually be built:

- **One country, one anchor sector, one exposed occupation group.** Not ASEAN, not all of finance.
- **Three free parameters** (`s_L`, `\u00b5`, `\u03b9`) on a grid \u2014 the proposal's 3\u00d73,
  which is nine cells each with an economic reading, not nine arbitrary simulations.
- **Two measured inputs** (`V`, `S`) from the lane's own data, once items 1 and 3 land.
- **Outputs:** employment, unemployment, job-finding rate, wages, and labour share \u2014 reported
  as paths under assumptions, never as a single forecast.
- **The deliverable is a resilience map**: which combinations produce temporary reallocation
  versus persistent unemployment and wage compression.

What it is *not*: a task-exposure model (borrowed from ILO), a forecasting model, or a model of
the informal sector (unmodelled sink, declared).

## 5. Honest limits, stated up front

1. **Formal-sector only.** The matching model cannot see the 87.74m informal workers who are the
   most likely destination for displaced clerical staff. This is the largest single limitation.
2. **A rule change sits inside the claims window.** PP No. 6 of 2025 breaks 2024\u201325
   comparability of JKP volumes.
3. **Claim cases are not distinct workers.** 431,086 cases vs 90,513 recipients (2025):
   payment recurs for the same worker. Never use one as the other.
4. **Attribution.** A warning can justify investigation or early support without proving AI
   causation. The proposal's own framing \u2014 "under this magnitude of shock and this degree of
   mobility, the model implies this path" \u2014 is the standard to hold to.
5. **`\u03c7` is not identified** at this stage and is folded into the scenario range.

## 6. Next three moves

1. **Fix the exposure flag** (item 10) \u2014 cheapest, and it makes the existing 331-row corpus
   usable immediately rather than after more scraping.
2. **Attempt the Karirhub back-series** (item 1) \u2014 the single highest-value scrape, because
   it turns `V` from a sample into a series and is fully within our own reach.
3. **Draft the `\u00b5` request** (item 2) \u2014 the only route to calibrating mobility rather
   than assuming it, and the ask most likely to be answered because SILASTIK already catalogues
   the microdata publicly.
