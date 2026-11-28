# Backtest addendum — the verdict flips at the measured exposure

**28 Nov 2026 · CRO for Shafira · corrects `MODEL-BACKTEST.md`**
The original backtest was run at the **30% exposure placeholder**. Exposure is now **0.582, measured**.
The instrument verdict below is the corrected one. **The earlier "1 : 80" no longer stands.**

---

## What changed

| | At 0.30 (placeholder) | At 0.582 (measured) |
|---|---|---|
Extreme dismissals, 2026–2030 | 602 | **25,826** |
JKP claims at 0.83 take-up | 500 | **21,436** |
Claims per year | ~100 | **~4,287** |
Share of one year's 90,513 claims | 0.11% | **4.74%** |
Noise floor of the series | 8.8% | 8.8% |
Signal-to-noise | 1 : 80 | **1 : 1.9** |
Layoffs needed for a 1% move | 1,090 (1.8× the whole five-year case) | 1,090 (the model produces **23.7×** that) |

## The corrected verdict

**The instrument is not blind after all — at the measured exposure it is marginal.** The extreme case now
implies **4.74% of a year's claims against an 8.8% noise floor**, so it sits *inside* the noise band but
within a factor of two of it. Two consecutive years of that would be visible; one year would not.

**And the two scenarios that matter most stay invisible.** Slow and Medium still produce **zero
dismissals** — the adjustment happens entirely through not replacing leavers. So the finding sharpens
rather than dissolves:

> The national JKP series can, just about, see the extreme case. It cannot see the likely one. A quiet
> hiring slowdown leaves no trace in any series we hold.

## What this means for the report

The line *"S8 is blind to this shock"* is too strong as written and has been corrected to *"blind to the
likely shock, marginal on the extreme one"*. That is a weaker claim and a more useful one: it says the
measurement gap is specifically about **hiring**, not about **dismissals** — which is exactly what the
policy asks target.

## Method note, so this is checkable

Dismissals and JKP cost taken from the sheet's `Summary` at `Feed_Panel` exposure 0.582, reproduced by
`app/model.js` (`scripts/verify-app-vs-sheet.js`, zero delta). Claims = dismissals × 0.83 take-up
(`Inputs`). Base year 90,513 claims (2025, verified). Noise floor 8.8% = the gap between the two mid-2026
annualisations (88,000 and 96,000) as a share of 90,513.

**The lesson worth keeping:** a backtest is only as good as the assumption it is run at. Ours said 1 : 80
and that number was quoted three times before the exposure changed. Both are now in the repo.
