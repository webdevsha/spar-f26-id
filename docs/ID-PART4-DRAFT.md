# Indonesia — Country Report, Part 4: who can act, and the policies in place

**Draft v1 · 26 Nov 2026 · Shafira (Indonesia Data Lead), with Ian · target 600 words · overdue since Sun 22 Nov**

Sources: `SIGNALS_ID` (the Indonesia indicator table, verdict + capability per signal), the Core file's
`signals` tab (columns O–T), `data/id-who-can-act.csv`, `data/id-policy-inventory.csv`,
`data/id-triggers.csv`. This section grades **documents**, never a government, and ranks nobody. Where the
register says `tbc`, it stays `tbc` — that is the finding, not a gap to smooth over.

---

## Who can act, and what each one uniquely holds

Six bodies sit on the path from this evidence to a decision. Each has an entry door we already know and
one thing nobody else holds.

| Body | Type | What only they hold | The door |
|---|---|---|---|
| **OJK** | financial regulator | The banking data, plus the AI governance guidance the sector is being asked to follow | Banking supervision office |
| **Kemnaker** | ministry | Pasker ID / Karirhub — vacancy postings, titles, employers | Pusat Pasar Kerja |
| **BPJS Ketenagakerjaan** | social insurer | JKP claims and covered workers — the only national record of formal job loss | JKP programme office |
| **BPS** | statistics office | Sakernas — employment, occupation, wages: the denominator every share needs | Statistical service / SILASTIK |
| **PERBANAS** | industry body | Member banks and employer outreach — the sector's own channel | Secretariat |
| **ILO** | international organisation | The occupational-exposure method our exposure figures rest on | Employment specialist team |

The division of labour is the point. **OJK** can see workforce movement inside banks before anyone
publishes it, because it already supervises those institutions — which is why the trigger routes
*confirmation* through banking supervision and *action* through Kemnaker and the JKP office. **BPS** holds
the only series that can turn our posting sample into a share of something. **PERBANAS** is the realistic
route to employer-side evidence that no public series records. None of the six can carry the middle of the
chain alone.

## The instruments in place

Three instruments are recorded as existing. Their operational detail is largely unrecorded, and the
indicator table now states for each one what it can and cannot show.

- **OJK's AI governance guide for banks** — guidance aimed at the sector we are studying. Monitoring,
  budget and effective date are all `tbc`; the source states only that the guide exists. *Shock reading:
  governance is covered, capability is not — nothing in it records whether a machine can now finish a
  whole clerical task.*
- **Job-loss insurance (JKP)** — the instrument that actually pays out when formal employment ends. Claim
  volumes are monitorable and it is the closest thing Indonesia has to a shock meter for bank workers, but
  occupation detail is unconfirmed and its own processing time is not published. *Shock reading: payouts
  are recorded, the series has two breaks, and the pace is not measured.*
- **Pasker ID / Karirhub (Permenaker 5/2024)** — already the base of our posting evidence, and the
  instrument through which a vacancy-side response could be delivered. *Shock reading: vacancies are
  counted, but never whether they were filled.*

## What is not in place

No instrument in this register connects **workplace AI adoption to hires, separations or wages**. The
hiring link is not under-monitored because someone declined to monitor it; no series for it appears to
exist. Three consequences shape what this report can claim:

1. **The AI shock cannot be sized.** No published AI adoption rate exists anywhere — the regulator holds
   financial and technology-risk reports, the ministry holds vacancy data, and neither publishes one. No
   rule requires any body to publish a jobs or revenue forecast that mentions AI.
2. **The trail stops at dismissal.** Nothing follows a worker after they leave: the old-age and injury
   schemes pay out whether a person resigned or retired, and Kartu Prakerja records who joined training,
   not where they ended up.
3. **Policy itself moves the numbers.** The claims series carries two legal breaks — PP 6/2025 on
   **7 Feb 2025** and UU 27/2026 on **28 Oct 2026**, with implementing rules not due until 28 Oct 2027 —
   so any comparison across those dates must carry the break with it.

## Two things this section cannot settle yet

**Policy readiness is unscored.** The three documents are recorded, but the register's `q1`–`q6` columns
are empty and **the six question texts are not recorded anywhere**. A worksheet exists
(`docs/ID-READINESS-WORKSHEET.md`); scoring waits for the questions rather than being inferred.

**Any request in the study's name creates a record.** The verification run surfaced 15 formal information
requests to BPJS, OJK, Kemnaker, BPS and DPR Commission IX, plus a scope question on platform data
obtained through web archives. **None have been sent**, and all are routed to `@clo` before anything
regulator-facing leaves the team.

## Where Ian's input is needed (3 flags)

1. **Do we name PERBANAS and ILO as doors we would actually use,** or list them as context only?
2. **The division-of-labour paragraph** — keep it as our joint voice, or hand it to Ian to rewrite?
3. **Word budget:** measured honestly, the prose runs **~690 words with the table rows excluded**, against a
   600-word target — so roughly **90 words still need to come out**. My suggestion: cut item 3 of "What is
   not in place" first (it is the newest), then tighten the instruments list.

*Framing: each statement is consistent with AI-driven change, not caused by it. Credit cycles,
consolidation, employer recruiting practice and regulation (notably PP 6/2025) move these figures too, and
every row keeps its alternative explanation.*
