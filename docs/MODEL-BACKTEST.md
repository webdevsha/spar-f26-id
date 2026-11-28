# Backtest — can the JKP claims series actually see the shock?

**28 Nov 2026 · CRO for Shafira · Indonesia lane**
Sources: Core file `id-shock-data` rows `ind-ev-0069`–`ind-ev-0073` (BoxCompute run 3) for the reported
series; `app/model.js` (verified against the sheet's `Summary`, zero delta) for the model output.
Machine-readable version: [`data/model-backtest.json`](../data/model-backtest.json).

## Why this test exists

Every scenario number in this study rests on an instrument we have never checked against the series it
claims to be measured by. `S8 — unemployment-benefit claims` is the closest thing Indonesia has to a shock
meter for bank workers, so it is the right place to start: if the model's displacement cannot move that
number, then no reading of that number can detect the shock.

## The reported path

| Period | JKP recipients | Quality |
|---|---|---|
| 2025, full year | **90,513** | verified, high |
| to 30 Jun 2026 | **44,000+** (lower bound) | partial, medium |
| to 31 Aug 2026 | **~64,000** | low confidence, approximate |

Annualised, those two mid-year points imply **88,000** (Jun) and **96,000** (Aug) — a swing of **8.8% of
last year's total, inside two months.** That is the noise floor of the instrument, before anyone asks a
question about AI.

## What the model says

| Scenario | AI-attributable layoffs, 2026–2030 | Claims at 0.83 take-up |
|---|---|---|
| Slow | 0 | 0 — attrition absorbs the whole change |
| Medium | 0 | 0 — hiring falls, nobody is dismissed |
| Extreme | **602** | **500** |

Spread across five years, Extreme is about **100 claims a year** against a base of 90,513: **0.11% of one
year's total.**

## The detection calculation

| Question | Answer |
|---|---|
| Signal-to-noise on the national series | **1 : 80** (0.11% signal against an 8.8% noise floor) |
| Layoffs needed to move the annual number by **1%** in one year | **1,090** |
| That, as a multiple of the model's entire five-year Extreme total | **1.8×** |

## What the test concludes — two separate verdicts

**The model survives.** The reported path is flat within noise — 88,000 to 96,000 annualised against
90,513 — which is exactly what Slow and Medium predict. Nothing in the data contradicts the scenarios.

**The instrument does not.** To shift the national claims series by a detectable 1%, the shock would have
to be **1.8 times larger in a single year** than the model's whole five-year Extreme case. So:

> S8 is the strongest instrument in the register and it is still blind to this shock. Detection requires
> bank-level claims, or a within-bank separation series — not the national total.

That is a finding about measurement, not about AI, and it is the kind of finding a policy audience can act
on: it says precisely which series has to exist before anyone can claim to have seen an AI shock in
Indonesian banking.

## What would change the answer

1. **Bank-level JKP claims.** BPJS holds them by employer; the national total is the only published cut.
   One request through the `who-can-act` door to BPJS Ketenagakerjaan would settle it.
2. **A within-bank separation series.** `ID-14` (BCA turnover) is the seed: 860 leavers, 3.4%. At bank
   scale a displacement of 600 people is visible; at national scale it is rounding error.
3. **The 2026 full-year figure**, due early 2027. If the annualised 96,000 holds, the series is drifting up
   about 6% a year for reasons that have nothing to do with AI — which raises the bar further.

## Limits, stated

- The two mid-2026 values are **not** verified to the same standard as the 2025 figure: one is a lower
  bound, one is approximate. If they are wrong, the noise floor is wrong too.
- The model's take-up rate (0.83) and its wage cap come from `PP 6/2025`; the **cost** side of this test
  has not been backtested at all — only the volume.
- This test says nothing about whether AI is displacing bank workers. It says the national claims series
  cannot answer that question. Those are different claims and only the second one is proven here.
