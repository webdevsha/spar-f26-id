# Pre-flight — before any sheet write

Run these five checks. Every one of them has already caught a real error in this project.

| # | Check | What it caught |
|---|---|---|
| 1 | **Header compare** — read row 1 and diff against the incoming schema, column for column | would have appended 27 rows into a different shape |
| 2 | **Duplicate check** — build the set of existing `id` and `match_key` values first | would have double-added the run-3 rows |
| 3 | **Empty-cell guard** — refuse to write into a range that already holds data | would have overwritten the turnover columns |
| 4 | **Grain check** — one row = one ad, or one platform-month, or one category. Never mixed | would have put monthly totals into a posting-level tab |
| 5 | **Revert range** — write the exact range to clear into `docs/SHEET-WRITE-*.md` before writing, not after | every write so far has a documented revert |

Then: `bash scripts/verify-all.sh` must print ALL CHECKS PASSED.

Never: `git add -A` while untracked binaries sit in the tree. That is how 209 MB of PDFs and, later,
3 GB of corpus came within one command of the public repo.
