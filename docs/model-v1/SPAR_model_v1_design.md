# SPAR Indonesia model v1.0: design

Status: design for team review. Stress test, not a forecast. Probabilities, phi and the role-mix share are placeholders.

## 1. Narrative

The shock arrives as an empty chair, not as a dismissal. Banks lose work to AI first through hires they do not make and leavers they do not replace. Only in the extreme case does it become dismissals. The model asks four questions in order.

1. How much work can AI take? Exposure of bank roles: role-mix share x = 0.45, with the postings index 0.582 as a cross-check on task exposure, ILO 21.7% of Indonesian jobs and 93.9% of clerical jobs.
2. How fast will banks adopt it? 18% operational today (ID-05), reaching 30%, 52% or 85% by 2030, 2029 or 2028.
3. Where does the adjustment land? Hires not made, then attrition, then dismissals.
4. Who is protected, and would we see it in time? JKP covers dismissal. Nothing covers a job that was never offered.

What the panel model says (8 banks, 218,129 staff, 2027 to 2030):

| | Slow (40%) | Medium (50%) | Extreme (10%) |
|---|---|---|---|
| Headcount change | -1.0% | -6.9% | -23.3% |
| Hires not made | 1,917 | 13,001 | 29,257 |
| Dismissals | 0 | 0 | 15,702 |
| JKP cost, Rp bn | 0 | 0 | 412 |

At sector scale (x7.4, an upper bound because the 1.62m includes insurance) Extreme dismissals run near 97,000 and 108,000 in 2027 and 2028, above all 90,513 JKP recipients of 2025. Medium produces no dismissal and no JKP claim, so the layoff and JKP signals stay silent while the entry-level pipeline narrows by roughly 37,000 to 42,000 seats a year.

## 2. Three layers, six modules

Layers: panel (observed, 8 banks, 13% of the sector); sector (range, panel as lower bound, 1.62m finance and insurance as upper bound); economy (formal 62.25m, informal 85.73m, youth, macro, Moody's overlay).

Modules after Akbar's measures: M1 stock and exposure; M2 adoption driver; M3 hiring channel; M4 exits and destinations; M5 protection capacity; M6 spillover. M1 to M4 run today. M5 and M6 are specified, with most inputs needing a feed.

## 3. Sheets

See sheet_architecture.csv (26 tabs in six bands: guide, output, parameters, feed, engine, check). Thirteen are new; the other 13 exist in v0.4 or extend it.

## 4. Questions to indicators to tabs

See question_map.csv.

## 5. Fingerprints

Each scenario predicts movement on S1 to S10 (see fig_scenario_fingerprint). In the quiet cases the model moves hiring (S5) but S6 and S8 stay at zero. The loud case moves S6, S8 and S9, which are the least readable for finance today. This fills the empty Forecast 2027/2030 column for ID-09, 11, 12, 13 and 17.

## 6. Flags for the team

1. Exposure double counting (resolved in v1.0). x is now the role-mix share, 0.45 (midpoint of 25.7% core exposed roles and 65.3% including credit and loan roles, from 144 verified banking postings). The postings index 0.582 is kept only as a cross-check on task exposure e; it sits closest to e Medium (0.53), which supports Medium as the central case. At x = 0.582 the panel results were 2,480 / 16,815 hires not made and 27,578 dismissals (Extreme); Medium has zero dismissals at every x up to 0.65. x is still a placeholder until GRI 2-7 or Sakernas KBJI by KBLI K is available. This supersedes the 0.582 choice in DECISIONS-28NOV.md.
2. Growth baseline. The model assumes hires equal leavers (g = 0). The 2025 panel shows 21,812 hired against 12,392 left, net +9,420 (4.3% of panel staff). Under that baseline, AI shows as growth foregone and dismissals are less likely. Add g as an input and run both.
3. Basis A (all leavers, 5.68%) and Basis B (voluntary, 4.38%) differ 12.8 times in Extreme dismissals. Label every table.
4. Scale-up uses KBLI K, not banks. OJK bank employee total is still needed.
5. ID-09 and ID-20 are unverified; finance employment for 2025 and 2026 is from secondary sources.
6. Only one trigger is drafted. The Watch level and the hiring-side row are proposals for mentor review.
7. Readiness scales (team 0 to 2, mine) are not yet merged.
