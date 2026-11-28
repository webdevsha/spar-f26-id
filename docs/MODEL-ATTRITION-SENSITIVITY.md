# Attrition is the model's biggest lever — not adoption

**28 Nov 2026 · CRO for Shafira · Indonesia lane**
Method: `app/model.js` (verified against the sheet's `Summary`, zero delta) run twice on the same
scenarios, changing **one** input: whose separations count as absorption capacity.

- **Basis A — all leavers** (the current panel in `Feed_Panel`): attrition = every reported separation ÷
  headcount, including retirement, contract end and non-renewal. Weighted **6.11%**.
- **Basis B — voluntary leavers only**, where the bank publishes a voluntary rate (BRI 1.24%,
  Bank Mandiri 3.53%); every other bank unchanged. Weighted **4.38%**.

## What changes

| Scenario | Metric | Basis A (all leavers) | Basis B (voluntary only) | Difference |
|---|---|---|---|---|
| Slow | Layoffs 2026–2030 | 0 | 0 | — |
| Slow | JKP cost | Rp 0.0 bn | Rp 0.0 bn | — |
| Medium | Layoffs | 0 | 0 | — |
| Medium | Average hiring cut | 16% | 22% | +6 pts |
| **Extreme** | **Layoffs 2026–2030** | **602** | **7,718** | **+7,116 (12.8×)** |
| **Extreme** | **JKP cost** | **Rp 9.0 bn** | **Rp 115.3 bn** | **+Rp 106.3 bn** |
| Extreme | Into informal work | 245 | 3,135 | +2,890 |
| Extreme | Open unemployed | 245 | 3,135 | +2,890 |
| Extreme | Re-employed | 113 | 1,447 | +1,334 |
| Extreme | Headcount 2030 | 191,884 | 191,884 | **0** |

## The two things this tells us

**1. The headline number is a threshold effect, not a smooth estimate.** A 1.7-point change in attrition —
one input, two banks — multiplies extreme-scenario layoffs by **12.8** and JKP cost by **12.8**. The model
is not linear here: attrition is a *buffer*, and at 6.11% the panel absorbs roughly 13,300 separations a
year, which is more than the AI-driven reduction requires, so almost nothing becomes a dismissal. Take the
buffer down to 4.38% and the same AI path starts producing dismissals.

**2. Headcount 2030 does not move at all.** Every scenario's end-state is unchanged, because the headcount
path is set by adoption, not attrition. Attrition changes only the **composition** of the fall: absorbed
quietly, or paid for through JKP. That is the policy-relevant distinction — the same 12% fall can cost
Rp 9 bn or Rp 115 bn depending on whose exits you count as capacity.

## Which basis is right?

Neither is right by default, and this is a decision for the team, not for the drafting lane:

- **All leavers** is how firms actually shrink without layoffs — and it is what the register's `attrition`
  column has meant so far.
- **Voluntary only** is the more honest buffer for "AI made this role unnecessary": someone retiring was
  not displaced, and counting them as capacity overstates how smoothly the change can be absorbed. It is
  also only available for **two of the eight banks**, so it is a partial basis, not a clean alternative.

**Recommendation:** publish both, labelled, and never one without the other. The gap between Rp 9 bn and
Rp 115 bn *is* the finding — it says the answer to "how much does this cost?" depends on a definition
nobody has settled.

## Data conflicts found while wiring this in

| Bank | Problem |
|---|---|
| **BNI** | Panel carries **2,254** leavers; p6 evidence says **1,324**; BNI's own report states a **1.9%** turnover rate. 1,324 ÷ 27,201 = 4.9%, so the three numbers cannot all be right. Unresolved — do not publish a BNI attrition figure until it is. |
| **BRI** | Total turnover 5.58% × 84,949 = 4,740, against 3,323 reported leavers (3.9%). The published rate is on a different basis (average headcount or group scope). |
| **Mandiri** | Voluntary 3.53% against 2,868 ÷ 38,732 = 7.4% total — the largest total-to-voluntary gap in the panel, and plausible for a bank mid-restructuring. |
| **KB Bank** | 1,063 leavers on 2,334 staff = 45.5%, no rate published. It drives the 6.11% panel average on its own; worth a footnote wherever that number appears. |

## Files

- `Feed_Panel` columns **M** (total turnover rate), **N** (voluntary turnover rate), **O** (basis / note) —
  added 28 Nov, additive, nothing existing changed.
- `app/model.js` and the workbook `Model_*` sheets are unchanged: this is a sensitivity run, not a new
  default.
