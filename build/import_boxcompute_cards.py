#!/usr/bin/env python3
"""Map BoxCompute-harvested job_cards into the postings CSV schema.

Reads the sandbox's card output and emits rows in the SAME 36-column schema as
data/id-postings/postings-*.csv, so the page and the Sheet can carry them.

Honesty rules
-------------
* arm is "boxcompute_census", never "archive"/"live" -- these rows come from a
  different collection method and a different population (platform-wide, all
  sectors), so they must stay separable from the finance/BPO panel.
* in_scope uses the repo's OWN classifier (FIN_WORDS / FIN_EMPLOYER, copied
  verbatim from build/prep_postings.py) -- not a new rule invented here.
* posted_basis is carried through unchanged. If it is capture_proxy, the date
  is the crawl date, NOT the posting date, and downstream code can see that.
* ai_skill_required is left "No" with ai_source explaining that a card teaser
  cannot establish an AI requirement -- that needs a full description, which
  only stage 3 produces. Claiming otherwise would inflate the AI signal.

Usage:
  python3 build/import_boxcompute_cards.py <cards.jsonl> [--out DIR]
"""
import argparse
import csv
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data", "id-postings")

# --- copied verbatim from build/prep_postings.py (do not diverge) ---------
FIN_WORDS = re.compile(
    r"bank|asuransi|insurance|bancassurance|kredit|credit|pembiayaan|leasing|multifinance|"
    r"fintech|pegadaian|investasi|investment|sekuritas|reksa|paylater|pinjaman|"
    r"teller|collection|collector|underwriting|aktuaris|"
    r"bpo|call center|contact center", re.I)
FIN_EMPLOYER = re.compile(
    r"financ|fifgroup|adira|\bbfi\b|home credit|indomobil finance|oto multiartha|"
    r"kredivo|akulaku|amartha", re.I)

TAG = re.compile(r"<[^>]+>")
DATA_TERMS = ["sql", "python", "excel", "power bi", "tableau", "dashboard",
              "big data", "data analyst", "analitik", "statistik"]


def clean(t):
    return re.sub(r"\s+", " ", TAG.sub(" ", t or "")).strip()


def header():
    """Column order, taken from the live dataset so it cannot drift."""
    for f in sorted(glob.glob(os.path.join(D, "postings-*.csv"))):
        with open(f) as fh:
            return next(csv.reader(fh))
    sys.exit("no postings-*.csv found to read the schema from")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cards")
    ap.add_argument("--out", default=os.path.join(D, "postings-boxcompute.csv"))
    a = ap.parse_args()

    cols = header()
    seen, out = set(), []
    stats = {"read": 0, "dupe": 0, "no_title": 0, "in_scope": 0}

    for line in open(a.cards):
        line = line.strip()
        if not line:
            continue
        try:
            c = json.loads(line)
        except ValueError:
            continue
        stats["read"] += 1

        url = c.get("source_url")
        title = clean(c.get("title"))
        if not url or url in seen:
            stats["dupe"] += 1
            continue
        if not title:
            stats["no_title"] += 1
            continue
        seen.add(url)

        employer = clean(c.get("employer"))
        teaser = clean(c.get("teaser"))
        blob = " ".join([title, employer])
        in_fin = bool(FIN_WORDS.search(blob) or FIN_EMPLOYER.search(employer))
        if in_fin:
            stats["in_scope"] += 1

        dterms = sorted({t for t in DATA_TERMS if t in (title + " " + teaser).lower()})
        ts = str(c.get("archived_at") or "")

        row = dict.fromkeys(cols, "")
        row.update({
            "rec_id": "BC-%06d" % (len(out) + 1),
            "arm": "boxcompute_census",
            "source": "%s (Wayback, BoxCompute census)" % (c.get("platform") or ""),
            "domain": "PUBLIC",
            "domain_note": "public web archive; identified crawler, 1 request / 2 s",
            "posted_at": c.get("posted_at") or "",
            "posted_basis": c.get("posted_basis") or "",
            "captured_at": ("%s-%s-%s" % (ts[:4], ts[4:6], ts[6:8])) if len(ts) >= 8 else "",
            "location_city": clean(c.get("location_city")),
            "location_province": "",          # not exposed on these platforms
            "title": title,
            "employer": employer,
            "sector": "",                     # no industry field on these platforms
            "in_scope": "finance_bpo" if in_fin else "outside_scope",
            "job_function": "",
            "skills": "",
            "content": teaser,
            "content_chars_full": "",         # cards carry a teaser, not the full ad
            "requirements": "",
            "ai_skill_required": "No",
            "ai_tier": "",
            "ai_evidence": "",
            "ai_source": "card teaser only - insufficient for an AI flag; needs stage-3 full description",
            "data_skill_flag": "Yes" if dterms else "No",
            "data_evidence": "; ".join(dterms),
            "digital_basic_flag": "",
            "min_education": "",
            "salary_shown": "",
            "deadline": "",
            "quota": "",
            "url": url,
            "original_url": url,
            "verified_status": "not checked",
            "verified_at": "",
            "verified_fields": "",
            "unverified_fields": "all (single parse from archive capture)",
        })
        out.append(row)

    with open(a.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(out)

    print("read %(read)d cards -> %(n)d rows  (dupes %(dupe)d, no title %(no_title)d)"
          % {**stats, "n": len(out)})
    print("in_scope=finance_bpo : %d (%.1f%%)"
          % (stats["in_scope"], 100.0 * stats["in_scope"] / max(1, len(out))))
    print("wrote %s" % a.out)


if __name__ == "__main__":
    main()
