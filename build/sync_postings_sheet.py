#!/usr/bin/env python3
"""Sync the postings dataset into the id-postings-sample Google Sheet tab.

Idempotent by rec_id: rows already present are skipped, so this can be re-run
as often as the crawler writes new rows without ever duplicating.

Column order is read from the SHEET's own header row and matched by name, so the
CSV and the sheet cannot silently disagree. Any CSV column the sheet lacks is
added to the header row first, rather than dropped.

Usage:
    python3 build/sync_postings_sheet.py            # sync everything
    python3 build/sync_postings_sheet.py --dry-run  # report only
"""
import argparse
import csv
import glob
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "id-postings")
SHEET_ID = "1v_TCkJ79k-OOmEvrBq5F_8p8qxO4TjtweWQDXmiad1k"
TAB = "id-postings-sample"
CHUNK = 400

GAPI = os.path.expanduser(
    "~/.hermes/skills/productivity/google-workspace/scripts/google_api.py")


def service():
    spec = importlib.util.spec_from_file_location("gapi", GAPI)
    g = importlib.util.module_from_spec(spec)
    sys.modules["gapi"] = g
    spec.loader.exec_module(g)
    return g.build_service("sheets", "v4")


def load_rows():
    """Every posting row, from the same files the page builder reads."""
    out = []
    for f in sorted(glob.glob(os.path.join(DATA, "postings-*.csv"))):
        with open(f, newline="", encoding="utf-8") as fh:
            out.extend(csv.DictReader(fh))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    svc = service()
    rows = load_rows()
    print("dataset rows: %d" % len(rows))
    if not rows:
        return 1

    csv_cols = list(rows[0].keys())

    hdr = svc.spreadsheets().values().get(
        spreadsheetId=SHEET_ID, range="%s!A1:BJ1" % TAB
    ).execute().get("values", [[]])[0]

    # --- add any column the sheet is missing, don't drop it ---------------
    missing = [c for c in csv_cols if c not in hdr]
    if missing and not a.dry_run:
        add = hdr + missing
        svc.spreadsheets().values().update(
            spreadsheetId=SHEET_ID, range="%s!A1:BJ1" % TAB,
            valueInputOption="RAW", body={"values": [add]}).execute()
        hdr = add
        print("header extended with:", missing)
    elif missing:
        print("would extend header with:", missing)

    # --- what's already there --------------------------------------------
    col_a = svc.spreadsheets().values().get(
        spreadsheetId=SHEET_ID, range="%s!A2:A" % TAB).execute().get("values", [])
    existing = {(r[0] if r else "") for r in col_a}
    existing.discard("")
    print("already in sheet: %d" % len(existing))

    new = [r for r in rows if (r.get("rec_id") or "") not in existing]
    print("to append: %d" % len(new))
    if not new or a.dry_run:
        print("done (nothing written)")
        return 0

    # --- make room --------------------------------------------------------
    meta = svc.spreadsheets().get(
        spreadsheetId=SHEET_ID,
        fields="sheets(properties(sheetId,title,gridProperties))").execute()
    sid = have = None
    for s in meta["sheets"]:
        p = s["properties"]
        if p["title"] == TAB:
            sid = p["sheetId"]
            have = p["gridProperties"]["rowCount"]
            break
    need = len(existing) + len(new) + 10
    if need > have:
        svc.spreadsheets().batchUpdate(spreadsheetId=SHEET_ID, body={"requests": [{
            "updateSheetProperties": {
                "properties": {"sheetId": sid,
                               "gridProperties": {"rowCount": need}},
                "fields": "gridProperties.rowCount"}}]}).execute()
        print("grid expanded %d -> %d" % (have, need))

    # --- append by header name -------------------------------------------
    values = [[(r.get(c) or "") for c in hdr] for r in new]
    for i in range(0, len(values), CHUNK):
        batch = values[i:i + CHUNK]
        svc.spreadsheets().values().append(
            spreadsheetId=SHEET_ID, range="%s!A1" % TAB,
            valueInputOption="RAW", insertDataOption="INSERT_ROWS",
            body={"values": batch}).execute()
        print("  appended %d-%d" % (i + 1, i + len(batch)))

    print("done: %d rows appended" % len(values))
    return 0


if __name__ == "__main__":
    sys.exit(main())
