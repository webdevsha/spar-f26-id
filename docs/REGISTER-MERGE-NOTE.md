# Merging `signals` and `id-shock-data` — what worked, and what it exposed

**28 Nov 2026** · new tab **`signals-evidence`** in the Core file · 62 rows × 18 columns

## How the merge was done

The obvious key — `indicator_no` — **does not join**. `signals.indicator_no` holds measure codes
(`M4 JOB LOSS AND WORKER DESTINATIONS`), while `id-shock-data.indicator_no` holds indicator codes
(`ID-17`). A first attempt joining on it returned **0 matches**.

The key both registers genuinely share is the **signal code, S1–S10**. That joins **46 of 62** evidence rows.

## What the merged tab shows

| Column group | From |
|---|---|
`evidence_id`, `measure`, `the_number`, `unit`, `period`, `verified`, `confidence`, `source`, `source_url`, `checked_on` | `id-shock-data` |
`signal_name`, `signal_status`, `signal_type`, `signal_next_step` | `signals` (first row per S-code) |
`evidence_indicator` **and** `signal_indicator`, side by side, plus an `indicator_match` flag | both, so the mismatch is visible rather than hidden |

## Two structural findings

**1 · The two registers are numbered differently, and 46 of 46 linked rows disagree.** Every joined row has
`indicator_match = no`, because `signals` carries M-codes where `id-shock-data` carries ID-codes. This is not
a data error — it is two numbering schemes that were never reconciled. Until one is aligned, no indicator-level
join is possible in either direction.

**2 · `S3 — AI adoption rate` has no row in `signals`.** It is the only S-code without a definition, and it
happens to be the signal ID-05 sits under. So ID-05's **14 evidence rows** currently hang off a signal that has
no owner, no status and no next step. That is why the adoption gap never showed up in the signal-level gap
list: the signal was never registered.

## What to do about it

1. **Add the missing `S3` row to `signals`** — type, holder, status `gap`, next step, and the 14 evidence rows
   behind it. Additive; nothing existing changes.
2. **Renumber one side.** Either `signals.indicator_no` takes ID-codes (matching the evidence register and the
   team indicator table), or `id-shock-data` gains an `m_code` column. My recommendation: add `m_code` to the
   evidence register — it preserves both schemes and breaks nothing.
3. **Then rebuild `signals-evidence`** — it is generated, so re-running is one command.


---

## Fixed, 28 Nov — both items closed additively

**1 · `S3` now exists in `signals`** as `ind-sig-ai-adoption-rate` — type `dataset`, status **`gap`**,
confidence `H (stages) / M (trend)`, indicator `M2 AI deployment and workforce change`, next step naming the
three moves (paper, OJK series, cross-check against the 8-bank survey). All ten codes S1–S10 are now defined.

**2 · `m_code` added to both registers.** `signals` gains column **X** (52 rows, extracted from the
`indicator_no` prefix); `id-shock-data` gains column **AF** (62 rows, the measure). The evidence register's
grid was widened to 34 columns to hold it.

**3 · `signals-evidence` rebuilt** on `signal_code` + `m_code`: **62 rows, 0 unlinked, 25 exact m_code
matches.** The 37 that do not match are not errors — a signal routinely spans more than one measure (S8 runs
across M4 and M5), which is exactly why the code alone could never be the join key.

What remains open is the deeper one: `signals.indicator_no` still holds measure names where the evidence
register holds indicator codes. `m_code` makes the measure join possible; an **indicator** join still needs a
deliberate renumbering, and that is a team decision, not a lane one.
