#!/usr/bin/env python3
"""Check that the Google Sheet and data/*.csv agree, row for row.

Read-only. Run this before trusting a sync, after a hand-edit in the Sheet, and
before seeding — it answers "are the seeding rows already there?" with a diff
instead of a guess.

    python3 build/check_parity.py

Auth: prefers a read-only service account (GOOGLE_SERVICE_ACCOUNT_JSON, or
GOOGLE_SERVICE_ACCOUNT_FILE), same as sync_sheets.py. Falls back to the local
Hermes OAuth token at ~/.hermes/google_token.json for a developer's own run.
Exit code 0 = every tab matches; 1 = at least one tab differs.
"""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
CONFIG = os.path.join(DATA, "sheets.json")
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]
LOCAL_TOKEN = os.path.expanduser("~/.hermes/google_token.json")


def credentials():
    from google.oauth2 import service_account
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request

    raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT")
    if raw:
        return service_account.Credentials.from_service_account_info(json.loads(raw), scopes=SCOPES)
    path = os.environ.get("GOOGLE_SERVICE_ACCOUNT_FILE")
    if path and os.path.exists(path):
        return service_account.Credentials.from_service_account_file(path, scopes=SCOPES)
    if os.path.exists(LOCAL_TOKEN):
        d = json.load(open(LOCAL_TOKEN, encoding="utf-8"))
        c = Credentials(
            token=d["token"], refresh_token=d.get("refresh_token"),
            token_uri=d.get("token_uri", "https://oauth2.googleapis.com/token"),
            client_id=d.get("client_id"), client_secret=d.get("client_secret"),
            scopes=d.get("scopes"),
        )
        if c.expired and c.refresh_token:
            c.refresh(Request())
        return c
    sys.exit("No credentials: set GOOGLE_SERVICE_ACCOUNT or GOOGLE_SERVICE_ACCOUNT_FILE.")


def norm(rows):
    """Trim cells, drop trailing blanks, drop wholly blank rows — same both sides."""
    out = []
    for r in rows:
        r = [(c or "").strip() for c in r]
        while r and r[-1] == "":
            r.pop()
        if any(r):
            out.append(r)
    return out


def main():
    sheet_id = os.environ.get("SHEET_ID")
    if not sheet_id:
        sys.exit("SHEET_ID is not set (the Sheet's ID from its URL).")
    mapping = json.load(open(CONFIG, encoding="utf-8"))

    from googleapiclient.discovery import build
    svc = build("sheets", "v4", credentials=credentials(), cache_discovery=False)

    differ = 0
    print(f"{'tab':28s} {'sheet':>6s} {'repo':>6s}  parity")
    for tab, csv_name in mapping.items():
        sheet = norm(svc.spreadsheets().values()
                     .get(spreadsheetId=sheet_id, range=f"'{tab}'").execute().get("values", []))
        path = os.path.join(DATA, csv_name)
        repo = norm(list(csv.reader(open(path, newline="", encoding="utf-8")))) if os.path.exists(path) else []
        ok = sheet == repo
        print(f"{tab:28s} {len(sheet):6d} {len(repo):6d}  {'MATCH' if ok else 'DIFFERS'}")
        if not ok:
            differ += 1
            for i in range(max(len(sheet), len(repo))):
                s = sheet[i] if i < len(sheet) else None
                r = repo[i] if i < len(repo) else None
                if s != r:
                    print(f"    row {i + 1}\n      sheet: {s}\n      repo : {r}")

    print()
    print("No seeding needed - every tab already matches the repo CSVs exactly."
          if not differ else f"{differ} tab(s) differ - seed or re-sync.")
    return 1 if differ else 0


if __name__ == "__main__":
    sys.exit(main())
