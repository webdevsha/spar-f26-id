#!/usr/bin/env python3
"""GSheets -> data/*.csv sync for the SPAR F26 Indonesia lane.

Auth: a read-only Google **service account** (recommended, team-owned) whose
JSON key is provided as the env var GOOGLE_SERVICE_ACCOUNT (or a file path in
GOOGLE_SERVICE_ACCOUNT_FILE). Share the sheet with the service-account email
as Viewer. Nothing here writes back to the sheet.

Config: data/sheets.json maps a tab NAME -> output file. Using the Sheets API
by tab name (not the CSV export URL) means the per-gid gotcha disappears.

Idempotent: writes the file only if the content changed, so the Action's
commit step produces no empty commits.
"""
import csv
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
CONFIG = os.path.join(DATA, "sheets.json")
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


def creds():
    raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT")
    if raw:
        return json.loads(raw)
    path = os.environ.get("GOOGLE_SERVICE_ACCOUNT_FILE")
    if path and os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    sys.exit("No service-account credentials: set GOOGLE_SERVICE_ACCOUNT (JSON) or GOOGLE_SERVICE_ACCOUNT_FILE.")


def main():
    sheet_id = os.environ.get("SHEET_ID")
    if not sheet_id:
        sys.exit("SHEET_ID is not set (the Google Sheet's ID from its URL).")
    if not os.path.exists(CONFIG):
        sys.exit(f"Missing {CONFIG}")

    with open(CONFIG, encoding="utf-8") as fh:
        mapping = json.load(fh)

    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    credentials = service_account.Credentials.from_service_account_info(creds(), scopes=SCOPES)
    service = build("sheets", "v4", credentials=credentials, cache_discovery=False)

    changed = 0
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
            continue
        rows = result.get("values", [])
        buf = io.StringIO()
        writer = csv.writer(buf, lineterminator="\n")
        for row in rows:
            writer.writerow(row)
        content = buf.getvalue()
        out = os.path.join(DATA, out_name)
        old = open(out, encoding="utf-8").read() if os.path.exists(out) else None
        if content != old:
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(content)
            changed += 1
            print(f"[sync] {tab} -> {out_name} ({len(rows)} rows)")
        else:
            print(f"[sync] {tab} unchanged")
    print(f"done. {changed} file(s) updated.")


if __name__ == "__main__":
    main()