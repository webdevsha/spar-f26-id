#!/usr/bin/env python3
"""Generate paste-ready seeding rows for the Google Sheet, one TSV per tab.

Reads data/*.csv (the versioned audit trail) and writes data/seed/<csv>.tsv —
tab-separated so it pastes straight into a Sheets tab without CSV quoting
surprises. Generated, never hand-edited: re-run after any CSV change.

Idempotent: writes only when the content changed.
"""
import csv
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SEED = os.path.join(DATA, "seed")

with open(os.path.join(DATA, "sheets.json"), encoding="utf-8") as fh:
    mapping = json.load(fh)

os.makedirs(SEED, exist_ok=True)
written = []

for tab, csv_name in mapping.items():
    path = os.path.join(DATA, csv_name)
    if not os.path.exists(path):
        print(f"[skip] {tab}: {csv_name} not present")
        continue
    with open(path, newline="", encoding="utf-8") as fh:
        rows = [r for r in csv.reader(fh) if any((c or "").strip() for c in r)]
    if not rows:
        print(f"[skip] {tab}: empty")
        continue
    out = "\n".join("\t".join(c.replace("\t", " ").replace("\n", " ") for c in r) for r in rows) + "\n"
    dest = os.path.join(SEED, os.path.splitext(csv_name)[0] + ".tsv")
    old = open(dest, encoding="utf-8").read() if os.path.exists(dest) else None
    if out != old:
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(out)
        print(f"[seed] {tab:28s} -> seed/{os.path.basename(dest)}  ({len(rows)-1} data rows + header)")
    else:
        print(f"[seed] {tab:28s} unchanged")
    written.append((tab, os.path.splitext(csv_name)[0] + ".tsv", len(rows) - 1))

print("\n--- seed contents ---")
for tab, f, n in written:
    print(f"  {tab:28s} {f:26s} {n} data row(s)")
