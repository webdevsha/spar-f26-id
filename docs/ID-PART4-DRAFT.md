# Indonesia — Country Report, Part 4: who can act, and the policies in place

**Draft v0 · 24 Nov 2026 · Shafira (Indonesia Data Lead), with Ian · target 600 words · overdue since Sun 22 Nov**

Source of every row below: `data/id-who-can-act.csv`, `data/id-policy-inventory.csv`,
`data/id-triggers.csv`, and columns O–T of the Core file's `signals` tab. This section grades
**documents**, never a government, and ranks nobody. Where the register records a value as `tbc`,
it stays `tbc` here: that is the finding, not a gap to smooth over.

---

## Who can act, and what each one uniquely holds

Six bodies sit on the path from this evidence to a decision. Each has an entry door we already
know and one thing nobody else holds.

| Body | Type | What only they hold | The door |
|---|---|---|---|
| **OJK** | financial regulator | The banking data — and the AI governance guidance the sector is being asked to follow | Banking supervision office |
| **Kemnaker** | ministry | Pasker ID / Karirhub: vacancy postings, titles, employers | Pusat Pasar Kerja |
| **BPJS Ketenagakerjaan** | social insurer | JKP claims and covered workers — the only national record of formal job loss | JKP programme office |
| **BPS** | statistics office | Sakernas: employment, occupation, wages — the denominator every share needs | Statistical service / SILASTIK |
| **PERBANAS** | industry body | Member banks and employer outreach — the sector's own channel | Secretariat |
| **ILO** | international organisation | The occupational-exposure method this study's exposure figures rest on | Employment specialist team |

The division of labour is the point. **OJK** can see the workforce movement inside banks before
anyone publishes it, because it already supervises those institutions — that is why the trigger in
`id-triggers.csv` routes *confirmation* through banking supervision and *action* through Kemnaker
and the JKP office. **BPS** holds the only series that can turn our posting sample into a share of
something. **PERBANAS** is the realistic route to employer-side evidence that no public series
records. None of the six can carry the middle of the chain alone.

## The instruments in place

Three instruments are recorded as existing. Their operational detail is largely unrecorded:

- **OJK's AI governance guide for banks** (`ind-ojk-ai-guide-2025`) — guidance aimed at the sector
  we are studying. Monitoring, budget and effective date are all recorded `tbc` in the register; the
  source states only that the guide exists.
- **JKP, job-loss insurance** (`ind-jkp-2022`) — the instrument that actually pays out when formal
  employment ends. Claim volumes are monitorable; **occupation detail is unconfirmed**, which is
  precisely why the trigger runs on events and notifications rather than on a series.
- **Pasker ID / Karirhub** (`ind-paskerid-kemnaker`) — already the base of our posting evidence, and
  the instrument through which a vacancy-side response could be delivered. A detailed extract is
  still something to request, not something we hold.

## What is not in place

No instrument in this register connects **workplace AI adoption to hires, separations or wages**.
The hiring link is not under-monitored because someone declined to monitor it; no series for it
appears to exist. Two consequences follow, and they shape what this report can claim.

First, **policy readiness is unscored**. The three documents are recorded, but the register's `q1`–`q6`
columns are empty, so we cannot yet say which of these instruments is equipped for the change they
now face. A worksheet exists (`docs/ID-READINESS-WORKSHEET.md`); the six question texts are not
recorded anywhere, and scoring must wait for them rather than be inferred.

Second, **any request in the study's name creates a record**. The verification run surfaced 15 formal
information requests to BPJS, OJK, Kemnaker, BPS and DPR Commission IX, plus a scope question on
platform data obtained through web archives. None have been sent, and all are routed to @clo before
anything regulator-facing leaves the team.

*Framing: each statement is consistent with AI-driven change, not caused by it. Credit cycles,
consolidation, employer recruiting practice and regulation (notably PP 6/2025) move these figures
too, and each row keeps its alternative explanation.*

---
**Word count: ~600 (excluding header block and table scaffolding).** Next: fold Part 3 and Part 4 into
Akbar's single voice for the Indonesia chapter; Part 4's `tbc` cells stay as they are until the
readiness question texts arrive.
