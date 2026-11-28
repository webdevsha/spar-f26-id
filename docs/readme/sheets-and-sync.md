# The sheets, and who changed what

Every tab with a direct link, plus the sync-visibility rules that make an edit traceable.

---

[← Back to the README index](../../README.md)

---

## The sheets

[data/sheets.json](../../data/sheets.json) maps a **tab name** to an output CSV; the Sheets API is used by tab name, so the
"CSV export only returns the first tab" gotcha does not apply.

| Sheet | ID | Tab(s) | What is in it |
|---|---|---|---|
| Core file — the register | [1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit) | `signals` (gid `838965401`), `triggers`, `Indonesia policy inventory`, `readiness`, `who-can-act`, `instruments` | 22 Indonesia signal rows; each policy document; the six readiness questions |
| SPAR signals skeleton (team) | [1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo](https://docs.google.com/spreadsheets/d/1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo/edit) | `README`, `SIGNALS`, `SIGNALS_ID`, `(dani notes)`, `LOG` | S1–S10 signal definitions in three layers; **`SIGNALS_ID` = the Indonesia indicator table** (indicator · source · policy · verdict · capability · details); the observation log. `README` carries the policy legend, the layer definitions and the float-up key |
| IND team progress | [1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ](https://docs.google.com/spreadsheets/d/1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ/edit) | `Sheet1` | Every Indonesia deliverable with progress, status, PIC |

### Direct links — every tab, clickable

The sheets are navigable: cells carry cross-tab links, so a policy name jumps to its row in the register
and a signal code jumps to its definition. Use these links directly, or click through from the cells.

| Sheet | Tab | Link |
|---|---|---|
| Core file | `signals` (22 rows, the register) | [gid=838965401](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=838965401) |
| Core file | `Indonesia policy inventory` (16 rows) | [gid=562214644](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=562214644) |
| Core file | `instruments` (6 levers) | [gid=2122536552](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=2122536552) |
| Core file | `who-can-act` (6 bodies) | [gid=2093456593](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=2093456593) |
| Core file | `triggers` | [gid=778752423](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=778752423) |
| Core file | `readiness` | [gid=597313565](https://docs.google.com/spreadsheets/d/1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k/edit#gid=597313565) |
| Skeleton | `SIGNALS_ID` (the indicator table) | [gid=265881413](https://docs.google.com/spreadsheets/d/1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo/edit#gid=265881413) |
| Skeleton | `SIGNALS` (signal definitions) | [gid=514284320](https://docs.google.com/spreadsheets/d/1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo/edit#gid=514284320) |
| Skeleton | `README` (legend + keys) | [gid=179910438](https://docs.google.com/spreadsheets/d/1XhtoLn9hjkk_c0vwSuVT8LIfZyq19VdwWPOFpQi5Wmo/edit#gid=179910438) |
| Tracker | `Shafira's tasks` | [IND team progress](https://docs.google.com/spreadsheets/d/1EhtGDNQjZSM9_BoFw1V2F90rKN69_V7IUPTqKgHOcWQ/edit) |

**Cross-tab link graph (written 26 Nov, 134 cells — only where a cell was plain text, so no existing
hyperlink was overwritten):**

| From | Cell | Goes to |
|---|---|---|
| Core `signals` | `ian_signal` · `holder` | the `SIGNALS` row · the `who-can-act` row |
| Core `who-can-act` | `proposed_door` · `relevant_data_or_programme` | the `instruments` lever · the `policy inventory` row |
| Core `instruments` | `evidence` | the `who-can-act` row named in the cell |
| Core `Indonesia policy inventory` | `owner_agency` · `short_name` | the `who-can-act` row · the `readiness` row |
| Core `triggers` | `agency` · `action` | the `who-can-act` row · the lever it describes |
| Core `readiness` | `document` | the `policy inventory` row |
| Skeleton `SIGNALS` / `SIGNALS_ID` | `#` | each other's row for that signal |
| Skeleton `SIGNALS_ID` | `Indonesia's policy` | **each instrument name links to its own register row** (`textFormatRuns`, 18 cells / 55 links, wording unchanged) |
| Skeleton `README` | legend `P1`–`P10` names | the `policy inventory` row |

**Columns added 24–26 Nov (previously empty — revert ranges in [docs/SHEET-WRITE-2026-11-24.md](../../docs/SHEET-WRITE-2026-11-24.md)):**

| Sheet → tab | New columns | Contents |
|---|---|---|
| Core file → `signals` | `O`–`T` | `link` · `source_verbatim` · `confidence` · `data_status` · `not_verified` · `source_checked` |
| Skeleton → `SIGNALS` | `H`–`K` | Indonesian evidence · public source · status · gap/route |
| IND team progress → `Sheet1` | `G` | `Comments` — one line per task, plain language |
| Skeleton → `SIGNALS_ID` | `E`–`J` | `Indonesia's indicator` (name only, linked to the register row) · `Source` (compiled per shared indicator) · `Indonesia's policy` · `Verdict` · `Capability` · `Details` (the old single review column, split three ways on 26 Nov) |
| Skeleton → `SIGNALS` | `J` | `Relevant Policies` — the same instruments as `SIGNALS_ID`, one row per signal |
| Core file → `Indonesia policy inventory` | rows 5–17 | **3 → 16 rows.** The 7 other instruments the indicator table names (`UU 27/2026`, `PP 35/2021`, `PP 6/2025`, `Stranas KA`, `Kartu Prakerja`, `PP 44/2015`, `PP 46/2015`), the 5 the ecosystem map knew and the register did not (`RP3I 2026-2030`, the 50,000-worker programme, `PEKA`, `Sakernas × SIAPkerja`, the ILO–OJK–Kemenko collaboration) and `POJK 11/PADK 1` |
| Core file → `instruments` | rows 2–7 | **DEMO placeholder → 6 real levers**, one per actor's door in Part 4, each citing the `who-can-act` row or trigger card it rests on |

**Edit rules (all tabs):** header row is row 1 · `id` is the upsert and join key, never rename or
reorder · no merged cells, no blank spacer rows · one document per row · dates `YYYY-MM-DD` ·
`link` = the public source, not a Drive link · public sources only, no personal data · never rename a
header without telling CTO. Demo rows are marked `verified_by=DEMO`.

**Data is additive (Sha, 28 Nov 2026).** New data goes into the tab, row or column that already needs
it — never by replacing or removing what is there. Existing values and headers stay unless Sha says
otherwise in the session that is doing the work. Where a correction cannot be avoided, the superseded
reading stays and the new one is added beside it with its own period and vintage, so both can be cited.
This is why `app/data.js` now carries the August-round labour series *and* `LABOUR_ALT` for the
February and November readings instead of overwriting one with the other.

## Sync visibility — who changed what

Every sync run appends to [data/SYNC-LOG.md](../../data/SYNC-LOG.md) (newest first): timestamp, source, editor when known, and
per tab the `+added / −removed` counts with the changed `id`s. The dashboard renders the newest
entries in its **Recent changes** panel, and the commit message carries the editor.

| Trigger | Latency | Cost |
|---|---|---|
| Hourly cron (`17 * * * *`) | up to 60 min | negligible |
| Apps Script `onChange` → `repository_dispatch` | seconds | none (fires only on real edits) |

**Honest limit:** the service account reads cell *values*, not authorship. "Who edited" is only
knowable via the Apps Script trigger. Scheduled runs log the editor as unknown — expected, not a bug.

> **Currently failing.** `sync-sheets` fails on every hourly run: step *Sync tabs to CSV* succeeds,
> step *Commit if changed* fails. Consequence: the repo no longer mirrors the sheets (9 signal rows
> against the tab's 22), so the dashboard reads stale data and the 29 Nov sheet freeze cannot proceed.
> Owner: CTO / `@misshanna_bot`.
