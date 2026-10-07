#!/usr/bin/env python3
"""GSheets -> data/*.csv sync for the SPAR F26 Indonesia lane, with a changelog.

Auth: a read-only Google **service account** whose JSON key is provided as the
env var GOOGLE_SERVICE_ACCOUNT (or a file path in GOOGLE_SERVICE_ACCOUNT_FILE).
Share the sheet with the service-account email as Viewer. Nothing here writes
back to the sheet.

Config: data/sheets.json maps a tab NAME -> output file. Using the Sheets API
by tab name (not the CSV export URL) means the per-gid gotcha disappears.

Every run appends a human-readable entry to data/SYNC-LOG.md recording WHAT
changed (added / removed / edited ids) and, when the run was triggered from the
sheet, WHO changed it (SYNC_ACTOR, supplied by the Apps Script trigger).

Idempotent: writes a file only if its content changed, so the scheduled job
produces no empty commits.
"""
import csv
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
CONFIG = os.path.join(DATA, "sheets.json")
LOG = os.path.join(DATA, "SYNC-LOG.md")
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
ALLOW_SHRINK = False


def creds():
    raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT")
    if raw:
        return json.loads(raw)
    path = os.environ.get("GOOGLE_SERVICE_ACCOUNT_FILE")
    if path and os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    sys.exit("No service-account credentials: set GOOGLE_SERVICE_ACCOUNT (JSON) or GOOGLE_SERVICE_ACCOUNT_FILE.")


def load_csv_rows(path):
    """-> (header, rows) ; both empty when the file is missing/blank."""
    if not os.path.exists(path):
        return [], []
    with open(path, newline="", encoding="utf-8") as fh:
        parsed = [r for r in csv.reader(fh) if any((c or "").strip() for c in r)]
    if not parsed:
        return [], []
    return parsed[0], parsed[1:]


def diff_rows(old_rows, new_rows):
    old_map = {r[0].strip(): r for r in old_rows if r and r[0].strip()}
    new_map = {r[0].strip(): r for r in new_rows if r and r[0].strip()}
    added = sorted(set(new_map) - set(old_map))
    removed = sorted(set(old_map) - set(new_map))
    changed = sorted(k for k in set(new_map) & set(old_map) if new_map[k] != old_map[k])
    return added, removed, changed


def write_log_entry(lines):
    """Prepend a dated entry under the SYNC-LOG.md title (newest first)."""
    header = "# Sync log — Google Sheet -> repo\n\nNewest first. Auto-written by `build/sync_sheets.py`.\n"
    body = ""
    if os.path.exists(LOG):
        with open(LOG, encoding="utf-8") as fh:
            existing = fh.read()
        if existing.startswith(header):
            body = existing[len(header):].lstrip("\n")
    with open(LOG, "w", encoding="utf-8") as fh:
        fh.write(header + "\n" + "\n".join(lines) + "\n\n" + body)


def main():
    global ALLOW_SHRINK
    ALLOW_SHRINK = "--allow-shrink" in sys.argv[1:]

    sheet_id = os.environ.get("SHEET_ID")
    if not sheet_id:
        sys.exit("SHEET_ID is not set (the Google Sheet's ID from its URL).")
    if not os.path.exists(CONFIG):
        sys.exit(f"Missing {CONFIG}")

    actor = (os.environ.get("SYNC_ACTOR") or "").strip()
    source = (os.environ.get("SYNC_SOURCE") or "").strip() or (
        "sheet edit (real-time trigger)" if actor else "scheduled / manual run"
    )

    with open(CONFIG, encoding="utf-8") as fh:
        mapping = json.load(fh)

    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    credentials = service_account.Credentials.from_service_account_info(creds(), scopes=SCOPES)
    service = build("sheets", "v4", credentials=credentials, cache_discovery=False)

    changed = 0
    refused = 0
    entry_lines = []

    for tab, out_name in mapping.items():
        try:
            result = (
                service.spreadsheets()
                .values()
                .get(spreadsheetId=sheet_id, range=f"'{tab}'")
                .execute()
            )
        except Exception as exc:  # noqa: BLE001 - report and keep going
            print(f"[warn] tab '{tab}' failed: {exc}")
            entry_lines.append(f"- `{tab}`: **error** — {exc}")
            continue

        rows = result.get("values", [])
        buf = io.StringIO()
        writer = csv.writer(buf, lineterminator="\n")
        for row in rows:
            writer.writerow(row)
        content = buf.getvalue()

        out = os.path.join(DATA, out_name)
        old_header, old_rows = load_csv_rows(out)
        new_rows = [r for r in rows[1:] if any((c or "").strip() for c in r)]

        old_rows_count = len(old_rows)
        new_rows_count = len([r for r in new_rows if any((c or "").strip() for c in r)])

        # SAFETY GUARD: never silently drop rows.
        if old_rows and not ALLOW_SHRINK and new_rows_count < old_rows_count:
            print(
                f"[sync] REFUSED {tab}: sheet has {new_rows_count} data rows but {out_name} has "
                f"{old_rows_count}. Not overwriting. Re-run with --allow-shrink if this is intended."
            )
            entry_lines.append(
                f"- `{tab}`: **refused** — sheet has {new_rows_count} rows, repo has {old_rows_count}"
            )
            refused += 1
            continue

        old_text = open(out, encoding="utf-8").read() if os.path.exists(out) else None
        if content != old_text:
            added, removed, edited = diff_rows(old_rows, new_rows)
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(content)
            changed += 1
            print(f"[sync] {tab} -> {out_name} ({len(rows)} rows)")
            bits = [f"+{len(added)} / −{len(removed)}"]
            if added:
                bits.append("added: " + ", ".join(added[:6]) + ("…" if len(added) > 6 else ""))
            if removed:
                bits.append("removed: " + ", ".join(removed[:6]) + ("…" if len(removed) > 6 else ""))
            if edited:
                bits.append("edited: " + ", ".join(edited[:6]) + ("…" if len(edited) > 6 else ""))
            entry_lines.append(f"- `{tab}`: " + " · ".join(bits))
        else:
            print(f"[sync] {tab} unchanged")

    if entry_lines:
        stamp = __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime(
            "%Y-%m-%d %H:%M UTC"
        )
        who = actor or "unknown editor (scheduled run)"
        write_log_entry([f"## {stamp} — {source}", f"_by: {who}_", ""] + entry_lines)
        print("[log] appended SYNC-LOG.md entry")

    print(f"done. {changed} file(s) updated, {refused} refused.")


if __name__ == "__main__":
    main()