# Analysis refinement — what the new evidence changed

**28 Nov 2026 · after the BoxCompute briefs batch (ind-ev-0136 to 0153) and the BNI correction**

## The headline numbers, refined

| | Before today | Now |
|---|---|---|
Panel | 8 banks, 218,129 staff | unchanged |
Weighted attrition | 6.11% (BNI at the unsourced 2,254) | **5.68%** (BNI at the verified 1,324) |
Extreme dismissals at 0.582 | 25,826 | **27,578** |
Extreme JKP at 0.582 | Rp 385.8 bn | **Rp 412.0 bn** |
Headcount 2030 | 215,844 / 203,030 / 167,214 | **unchanged** |

**A data correction made the model harsher.** Removing 930 people from BNI's separations removed absorption
capacity, so more of the same shock becomes a dismissal: +1,752 dismissals, +Rp 26 bn. Headcount 2030 does not
move, because attrition never sets the size of the fall — only how it is absorbed. That is now the clearest
demonstration of the point in `MODEL-SENSITIVITY-GRID.md`.

## Three findings the new rows force

**1 · Fill status does not exist publicly, anywhere.** Not on the six boards we cannot reach, and not on the
ones we can. Pintarnya returns 27,376 site-wide and an identical count for `keyword=bank` — the filter is
client-side. No board publishes a close-with-hire flag, so **an ad that disappears is indistinguishable from an
ad that was filled.** Pasker ID publishes aggregate placements, not vacancy outcomes. This is now recorded as a
structural property of the Indonesian market, not a collection failure — and it is the measurement the entire
study waits on.

**2 · The job-board gap is documented, not just acknowledged.** Every block now has a status code and a date:
Jobstreet 403 with robots disallow; Indeed 403, hardened from 503 in run 1; Karir.com 200 but a 3.8 KB
JavaScript shell; LinkedIn robots-disallowed; KitaLulus a parameter mismatch rather than an empty market;
Pintarnya reachable but unfilterable. Six channels, **zero usable sector totals** — which is why S5's
finance-specific cut has never existed.

**3 · BPS has a working door, and it is not a browser.** The press-release page and the statistics-table page
both 403, but `webapi.bps.go.id` answers **400 — the "no API key" response.** A free self-service key lifts
every BPS figure from M to H and fills ID-13, without a browser, a scrape or a workaround. Everything we hold
from BPS today came from an **archived snapshot** of the release; the API is the durable route.

## What the analysis now says, in one paragraph

Banking is the most AI-exposed sector measured in Indonesia (0.582, highest of 29 categories over 20,088
advertisements), and eight large banks are still net-hiring by 8,490 people. The modelled 2030 fall — 1.0%,
6.9% or 23.3% depending on adoption speed — arrives with **zero dismissals in two of three cases**, because
attrition absorbs it. Every instrument in the register triggers on dismissal. And the one series that could
catch a quiet hiring slowdown, JKP claims, can just about see the extreme case and cannot see the likely one.
The shock, if it comes, lands on people who were never dismissed: the applicant who is not hired.

## What is still unsaid

No series links a bank's AI adoption to its headcount; none follows a worker after they leave; the readiness
rubric is drafted but unscored; and the panel is 13% of the sector. Those four sentences are the honest limits of
everything above.
