#!/usr/bin/env python3
"""sync_map_from_register.py - keep the ecosystem map's POLICY view in step with the register.

Why this exists
---------------
`data/ecosystem-id-map.json` was hand-folded from the Core-file workbook, so the map and the register
drifted apart in both directions: the map knew documents the register did not (RP3I, the 50,000-worker
programme, PEKA, the Sakernas x SIAPkerja join, the ILO-OJK-Kemenko collaboration), while seven
documents added to the register on 26 Nov were absent from the map. This script makes the register the
source for the policy view's node list.

What it does
------------
* `--check`  (default) prints the drift between `data/id-policy-inventory.csv` /
  `data/id-instruments.csv` and the map's policy nodes, and lists what `--write` would change.
  Read-only; safe to run in CI.
* `--write`  rebuilds `views.policy.nodes` from the register - keeping the hand-written `detail` text
  of nodes that already exist, adding a node for every register row that has none, and replacing the
  stale `pol-inst` placeholder with one node per lever in `id-instruments.csv`. `views/*/bands`,
  `views/*/edges`, `responsibility` and `marks` are never touched: the register describes documents,
  not relationships.

Node id mapping is explicit (below). Register ids are `ind-*`, map node ids are `pol-*`; nothing is
guessed from string shape.
"""
from __future__ import annotations

import argparse, csv, json, os, sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
MAP_JSON = os.path.join(DATA, "ecosystem-id-map.json")
INV_CSV = os.path.join(DATA, "id-policy-inventory.csv")
INST_CSV = os.path.join(DATA, "id-instruments.csv")

# register id -> map node id (explicit, reviewable)
ID_MAP = {
    "ind-ojk-ai-guide-2025": "pol-ojk",
    "ind-rp3i-2026-2030": "pol-rp3i",
    "ind-jkp-2022": "pol-jkp",
    "ind-paskerid-kemnaker": "pol-pasker",
    "ind-voc50k-2026": "pol-voc50k",
    "ind-peka": "pol-peka",
    "ind-kemnaker-sakernas-siapkerja": "pol-integ",
    "ind-trilat-ilo-ojk-kemenko-2026": "pol-trilat",
    "ind-uu27-2026": "pol-uu27",
    "ind-pp35-2021": "pol-pp35",
    "ind-pp6-2025": "pol-pp6",
    "ind-stranas-ka-2020-2045": "pol-stranas",
    "ind-prakerja": "pol-prakerja",
    "ind-pp44-2015": "pol-pp44",
    "ind-pp46-2015": "pol-pp46",
}

# policy band by document type / owner. Bands come from the map itself:
#   p1 Statutory & supervisory | p2 Social insurance | p3 Employment service & skills
#   p4 Planning & coordination | p5 Response menu (the levers, with price and speed)
def band_for(row: dict) -> str:
    owner = (row.get("owner_agency") or "").lower()
    typ = (row.get("type") or "").lower()
    if typ in ("law", "regulation", "guideline", "strategy", "supervisory", "practice"):
        return "p4" if typ == "practice" else "p1"
    if typ == "coordination":
        return "p4"
    if "bpjs" in owner:
        return "p2"
    if typ in ("programme", "data request"):
        return "p3" if "kemnaker" in owner or "prakerja" in owner else "p1"
    return "p4"


def read_csv(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh) if (r.get("id") or "").strip()]
    for r in rows:
        if not (r.get("document") or r.get("instrument")):
            raise SystemExit("row without a document/instrument name: {}".format(r.get("id")))
    return rows


def node_from_doc(row: dict) -> dict:
    """A policy node built only from register fields."""
    name = (row.get("short_name") or row.get("document") or "").strip()
    return {
        "id": ID_MAP.get(row["id"], "pol-" + row["id"].replace("ind-", "")),
        "band": band_for(row),
        "label": "{} - {}".format(name, (row.get("document") or "").strip())[:160],
        "sub": "{}. {}".format((row.get("type") or "tbc").capitalize(), (row.get("covers") or "").strip())[:300],
        "status": "real",
        "detail": "Owner: {}. Monitoring: {} - {}. Effective: {}. Status: {}. Generated from the register "
                  "(id {}); hand-written detail wins where a node already exists.".format(
                      row.get("owner_agency") or "tbc", row.get("monitoring") or "tbc",
                      row.get("monitoring_detail") or "tbc", row.get("effective_date") or "tbc",
                      row.get("status") or "tbc", row["id"]),
        "source": "register:id-policy-inventory.csv",
    }


def node_from_lever(row: dict) -> dict:
    return {
        "id": "lev-" + row["id"].replace("ind-inst-", ""),
        "band": "p5",
        "label": (row.get("instrument") or "").strip()[:160],
        "sub": "Cost: {}. Speed: {}.".format(row.get("cost") or "tbc", row.get("speed") or "tbc"),
        "status": "draft" if "draft" in (row.get("source_type") or "") else "real",
        "detail": "Covers: {}. Evidence: {}. Verified by: {}.".format(
            row.get("covers") or "tbc", row.get("evidence") or "tbc", row.get("verified_by") or "tbc"),
        "source": "register:id-instruments.csv",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="write the rebuilt policy view back to the JSON")
    args = ap.parse_args()

    mapdata = json.load(open(MAP_JSON, encoding="utf-8"))
    docs = read_csv(INV_CSV)
    levers = read_csv(INST_CSV)
    policy = mapdata["views"]["policy"]
    by_id = {n["id"]: n for n in policy["nodes"]}

    want = [node_from_doc(r) for r in docs]
    want_ids = {n["id"] for n in want}
    have_ids = set(by_id)
    missing_nodes = [n["id"] for n in want if n["id"] not in have_ids]
    orphan_nodes = [i for i in have_ids if i not in want_ids and i != "pol-inst"]

    print("register documents: {}   levers: {}   map policy nodes: {}".format(len(docs), len(levers), len(by_id)))
    print("\ndrift:")
    print("  in the register, missing from the map : {}".format(missing_nodes or "none"))
    print("  in the map, not in the register       : {}".format(orphan_nodes or "none"))
    print("  stale placeholder node                : {}".format("pol-inst" if "pol-inst" in have_ids else "none"))

    # keep hand-written nodes (richer detail), add the missing ones, swap the placeholder for levers
    nodes, kept, added = [], 0, 0
    for n in want:
        existing = by_id.get(n["id"])
        if existing:
            merged = dict(n)
            merged["detail"] = existing.get("detail") or n["detail"]      # hand-written wins
            merged["sub"] = existing.get("sub") or n["sub"]
            merged["label"] = existing.get("label") or n["label"]
            merged["status"] = existing.get("status") or n["status"]
            nodes.append(merged); kept += 1
        else:
            nodes.append(n); added += 1
    # hand-curated nodes with no register row would be dropped by the above - report, never silently
    dropped = [i for i in have_ids if i not in want_ids and i != "pol-inst"]
    if dropped:
        print("\nNOTE: these hand-curated nodes exist only in the map - add them to the register or they "
              "will be re-added by hand after a write: {}".format(dropped))
        for i in dropped:
            nodes.append(by_id[i])
    lever_nodes = [node_from_lever(r) for r in levers]
    nodes.extend(lever_nodes)
    print("\nresult: {} nodes ({} kept with hand-written detail, {} added, {} lever nodes, placeholder "
          "dropped)".format(len(nodes), kept, added, len(lever_nodes)))
    for n in nodes:
        if n["id"] not in have_ids:
            print("   + {:<16} {:<4} {}".format(n["id"], n["band"], n["label"][:64]))

    if not args.write:
        print("\n--check only: nothing written. Re-run with --write to rebuild views.policy.nodes.")
        return 0

    policy["nodes"] = nodes
    mapdata["_generated"] = {
        "by": "build/sync_map_from_register.py",
        "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "note": "views.policy.nodes rebuilt from the register (id-policy-inventory.csv + id-instruments.csv). "
                "bands, edges, marks and responsibility stay hand-curated.",
    }
    with open(MAP_JSON, "w", encoding="utf-8") as fh:
        json.dump(mapdata, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("\nWRITTEN {}".format(os.path.relpath(MAP_JSON, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
