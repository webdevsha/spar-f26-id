# Decisions taken, and what they change

**28 Nov 2026 · CRO for Shafira · four decisions, recorded so nothing is quietly applied**

---

## 1 · Attrition basis — both, labelled, never one alone

Publishing both is now the rule. The two bases differ by a factor of **12.8** and neither is silent about it.

| Basis | Weighted attrition | Extreme dismissals (at 0.30 exposure) | Extreme JKP |
|---|---|---|---|
**A · all reported leavers** | 6.11% | **602** | **Rp 9.0 bn** |
**B · voluntary leavers only** (BRI, Mandiri) | 4.38% | **7,718** | **Rp 115.3 bn** |

Every table that carries a dismissal or JKP figure must carry a `basis` label in the row or the caption. The
report, the app and the workbook all say which basis is in use. Basis A is the default because it is what
every bank actually discloses; Basis B is the more honest absorption buffer but exists for only 2 of 8 banks.

## 2 · BNI — the figure we adopt, and the two we do not

Three numbers exist for the same thing. We adopt **1,324 leavers (GRI 401-1, BNI SR 2025)** and declare the
others unused.

| Figure | Source | Status | Why |
|---|---|---|---|
**1,324** | BNI SR 2025, GRI 401-1 table | **ADOPTED** | the only figure stated as a count of leavers in the sustainability report |
**2,254** | carried in our own `Feed_Panel` from the v0.3b load | **DECLARED UNUSED** | cannot be reproduced from the GRI table; origin unclear |
**1.9%** | BNI SR 2025 turnover rate | **DECLARED UNUSED** | implies ~4.9% on 27,201 staff, so it does not describe the same population as the count |

**BoxCompute then resolved the arithmetic (run of 28 Nov).** 1,324 / 27,201 = 4.87%, so 1.9% cannot be a
separations rate — but **515 non-retirement exits / 27,201 = 1.89%**, and BNI's own footnote says *"there is a
difference in calculation for employees whose employment relationship has ended for certain reasons."* So
**1.9% is a voluntary-exit rate published under a total-turnover label.**

And the 2,254 now has a provenance: it appears **once in the whole report, on p.145, as a training-participant
count** ("Digital & Social Selling … 2,254"). No GRI 401-1 row matches it. That is the exact near-miss that
gets copied into a panel by accident, and it inflated BNI's leaver input by up to 930 people. The register now
carries it as **`ind-ev-0144`, marked Contradicted**.

Consequence: BNI's attrition moves from 8.3% to **4.87%**, which lowers panel attrition slightly. The row in
`Feed_Panel` is *not* overwritten — the unsupported 2,254 stays visible with a note, because a register that
deletes its own mistakes cannot be audited.

## 2b · What the ID-05 source actually contains

BoxCompute checked the landing page and found the **34 / 18 / 4 / 12% stage split absent** from it — correct,
and worth recording, because our rows came from **IBM's newsroom release**, not the landing page. The split is
in the release; the landing page carries the governance figures instead (2.74 vs 3.98, 9% registry, 32% none).
The gated PDF remains the only route to a per-institution breakdown, and `go.kiantara.com` returns 404.

One line for the report's "no AI instrument carries a labour clause" claim: **no survey item in the published
summary concerns workforce, headcount or roles at all.**

## 3 · Exposure — both 0.30 and 0.582 travel, with their evidence

| Exposure | Where it comes from | Extreme dismissals | Extreme JKP |
|---|---|---|---|
**0.30** | placeholder, no source — the v0.3b default | 602 | Rp 9.0 bn |
**0.582** | measured: 20,088 Indonesian banking ads, 94.3% in G2–G4, crawl validated against a same-month census within 0.57 pt | **25,826** | **Rp 385.8 bn** |

The paper presents **0.582 as the measured case** and **0.30 as the placeholder it replaced**, with both
figures in the table rather than the newer one alone. Neither is described as a forecast.

## 4 · Deploy — approved

The site goes up at v0.4. Deploy is a publishing action on a public URL: the pages carry no personal data, no
licence-restricted text, and no regulator correspondence. `docs/Data feed/` (third-party reports) is already
public by Sha's earlier decision.

---

## Also resolved, from the team side

- **ID-13 microdata and the paid-data licence** — Akbar already holds them. ID-13 is no longer blocked on
  procurement; it is blocked only on extraction.
- **The BPS interview (due 27 Nov) is cancelled.** The question it was going to ask is now answered from the
  archived primary release instead: TPT 4.75%, employed 147.99 m, labour force 155.37 m, average wage
  Rp3.42 m — all verified from the release text.
