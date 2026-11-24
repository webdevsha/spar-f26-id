#!/usr/bin/env python3
"""Publish a live intake status file next to the postings page.

The page is static, so a committed JSON is the only thing it can read at
runtime without new credentials. The page fetches it from its own origin
(/build/boxcompute-status.json) -- no CORS, no new infra.

Counters come from the sandbox: rows actually written, per track.
"""
import json
import os
import re
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "boxcompute-status.json")
SBX = "sbx_650d101e2bc04637a29d920348855466"
BXC = shutil.which("bxc") or os.path.expanduser(
    "~/.nvm/versions/node/v22.23.0/bin/bxc")

PROBE = r'''
D=/workspace/spar-id-census
echo "BULK=$(wc -l < $D/job_cards_bulk.jsonl 2>/dev/null || echo 0)"
echo "CARDS=$(wc -l < $D/job_cards.jsonl 2>/dev/null || echo 0)"
echo "LIVE=$(wc -l < /workspace/live_karirhub.csv 2>/dev/null || echo 0)"
echo "BUCKETS=$(grep -c cards $D/bulk.log 2>/dev/null || echo 0)"
echo "ALIVE=$(pgrep -cf job_card_harvest_bulk || echo 0)"
'''


def main():
    try:
        out = subprocess.run([BXC, "sandbox", "exec", SBX, "--", "bash", "-c", PROBE],
                             capture_output=True, text=True, timeout=150)
        raw = out.stdout or ""
    except Exception:
        raw = ""
    v = {m.group(1): int(m.group(2)) for m in re.finditer(r"^(\w+)=(\d+)", raw, re.M)}
    if "BULK" not in v:
        print("sandbox unreachable; status not updated")
        return

    bulk, cards = v.get("BULK", 0), v.get("CARDS", 0)
    live = v.get("LIVE", 0)
    total = bulk + cards + live

    st = {
        "updated_utc": subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
                                      capture_output=True, text=True).stdout.strip(),
        "rows_total": total,
        "rows_bulk_archive": bulk,
        "rows_sample_pass": cards,
        "rows_live_portal": live,
        "buckets_done": v.get("BUCKETS", 0),
        "buckets_total": 185,
        "workers_alive": v.get("ALIVE", 0),
        "target": 100000,
        "note": ("Counts are rows written by the crawler, not yet filtered to "
                 "finance/BPO scope. Rate is bounded by the archive's "
                 "one-request-per-2s courtesy rule."),
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(st, open(OUT, "w"), indent=2)
    print("wrote %s  rows=%d (bulk %d, sample %d, live %d)"
          % (os.path.relpath(OUT, ROOT), total, bulk, cards, live))


if __name__ == "__main__":
    main()
