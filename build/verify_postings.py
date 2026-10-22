#!/usr/bin/env python3
"""Re-fetch every row's source page and compare it with the CSV.

  live rows    -> the Karirhub detail page embeds the vacancy JSON; compare
                  title, publishedAt, expiresAt, status and employer.
  archive rows -> the Wayback capture must load (HTTP 200) and contain the title
                  (and the employer, when the CSV has one).

Each row gets a status, written to data/id-postings/verification.json with --write
(prep_postings.py copies it into the CSV; the report shows it per row):

  verified         live row, every checked field matched the source page
  partly verified  archive row: the capture loads and title/employer/location match,
                   but the posting date is derived and the sector is a guess
  unverified       the source did not load or a checked field did not match

Stdlib only. Identified User-Agent, 0.4 s between live requests, 1 s between
archive requests (web.archive.org is slower and rate-limits). Read-only.

  python3 build/verify_postings.py                # all rows (~12 min)
  python3 build/verify_postings.py --limit 10     # first 10 live + first 5 archive
  python3 build/verify_postings.py --write        # refresh verification.json, then
  python3 build/prep_postings.py                  # re-run prep + report builder to carry it
"""
import argparse, csv, datetime, html, json, os, re, sys, time, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "data", "id-postings", "karirhub-id-postings-sample.csv")
VER_PATH = os.path.join(ROOT, "data", "id-postings", "verification.json")
LIVE_CHECKED = ["title", "posted_at", "deadline", "employer", "location", "listing status"]
LIVE_NOT_CHECKED = ["skills", "min_education", "content snippet", "AI/data flags (derived from content)"]
ARCH_CHECKED = ["capture loads (HTTP 200)", "title", "employer (if recorded)", "location"]
ARCH_UNVERIFIED = ["posted_at (derived from a relative label)", "sector / in-scope (keyword guess)",
                   "skills", "min_education", "content snippet", "AI/data flags (derived from content)"]
UA = {"User-Agent": "SPAR-F26-research/0.1 (academic feasibility test)"}
VAC = re.compile(r'"vacancy":\{"id":"[^"]+".*?"title":"(.*?)".*?"status":"(.*?)".*?'
                 r'"publishedAt":"(.*?)","expiresAt":"(.*?)","description"', re.S)


def norm(s):
    s = html.unescape((s or "").replace("\\u0026", "&"))
    return re.sub(r"\s+", " ", s).strip().lower()


def get(url):
    err = ""
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            return e.code, ""
        except Exception as e:  # timeout / reset: retry
            err = str(e)
            time.sleep(3)
    return 0, err


def check_live(r):
    code, page = get(r["url"])
    res = {"rec_id": r["rec_id"], "arm": "live", "http": code, "problems": []}
    if code != 200:
        res["problems"].append(f"HTTP {code}")
        return res
    page = page.replace('\\"', '"')
    m = VAC.search(page)
    if not m:
        res["problems"].append("vacancy JSON not found")
        return res
    title, status, pub, exp = m.groups()
    if norm(title) != norm(r["title"]):
        res["problems"].append(f"title csv={r['title']!r} page={title!r}")
    if pub[:10] != r["posted_at"]:
        res["problems"].append(f"posted csv={r['posted_at']} page={pub[:10]}")
    if exp[:10] != r["deadline"]:
        res["problems"].append(f"deadline csv={r['deadline']} page={exp[:10]}")
    if status != "published":
        res["problems"].append(f"status {status}")
    if r["employer"] and norm(r["employer"])[:15] not in norm(page):
        res["problems"].append(f"employer not on page: {r['employer']}")
    for k in ("location_city", "location_province"):
        if r[k] and norm(r[k]) not in norm(page):
            res["problems"].append(f"{k} not on page: {r[k]}")
    return res


def check_archive(r):
    code, page = get(r["url"])
    res = {"rec_id": r["rec_id"], "arm": "archive", "http": code, "problems": []}
    if code != 200:
        res["problems"].append(f"HTTP {code}")
        return res
    p = norm(page.replace('\\"', '"'))
    if norm(r["title"])[:25] not in p:
        res["problems"].append("title not in capture")
    if r["employer"] and norm(r["employer"])[:15] not in p:
        res["problems"].append(f"employer not in capture: {r['employer']}")
    for k in ("location_city", "location_province"):
        if r[k] and norm(r[k]) not in p:
            res["problems"].append(f"{k} not in capture: {r[k]}")
    return res


def status_of(res):
    if res["problems"]:
        return "unverified"
    return "verified" if res["arm"] == "live" else "partly verified"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="only the first N live (and N/2 archive) rows")
    ap.add_argument("--out", default="", help="write the raw per-row report as JSON")
    ap.add_argument("--write", action="store_true",
                    help="write data/id-postings/verification.json (full run, or with --ids)")
    ap.add_argument("--ids", default="",
                    help="comma-separated rec_ids to re-check; with --write they are merged into "
                         "the existing verification.json (use after a transient timeout)")
    a = ap.parse_args()
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    live = [r for r in rows if r["arm"] == "live"]
    arch = [r for r in rows if r["arm"] == "archive"]
    if a.limit:
        live, arch = live[:a.limit], arch[:max(1, a.limit // 2)]
    if a.ids:
        want = set(a.ids.split(","))
        live, arch = [r for r in live if r["rec_id"] in want], [r for r in arch if r["rec_id"] in want]
    out = []
    for group, fn, delay in ((live, check_live, 0.4), (arch, check_archive, 1.0)):
        for r in group:
            out.append(fn(r))
            time.sleep(delay)
    for arm in ("live", "archive"):
        s = [x for x in out if x["arm"] == arm]
        ok = [x for x in s if not x["problems"]]
        print(f"{arm}: {len(ok)}/{len(s)} clean")
        for x in s:
            if x["problems"]:
                print("  ", x["rec_id"], "; ".join(x["problems"]))
    if a.write:
        if a.limit:
            sys.exit("--write needs a full run (no --limit) or --ids")
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
        rows_out = {}
        for x in out:
            live_row = x["arm"] == "live"
            rows_out[x["rec_id"]] = {
                "status": status_of(x), "checked_at": now, "http": x["http"],
                "checked": LIVE_CHECKED if live_row else ARCH_CHECKED,
                "unverified": LIVE_NOT_CHECKED if live_row else ARCH_UNVERIFIED,
                "problems": x["problems"],
            }
        if a.ids and os.path.exists(VER_PATH):
            merged = json.load(open(VER_PATH))["rows"]
            merged.update(rows_out)
            rows_out = merged
        json.dump({"checked_at": now, "method": "build/verify_postings.py", "rows": rows_out},
                  open(VER_PATH, "w"), indent=1, ensure_ascii=False)
        print("wrote", VER_PATH)
    if a.out:
        json.dump(out, open(a.out, "w"), indent=1)
    sys.exit(0 if all(not x["problems"] for x in out) else 1)


if __name__ == "__main__":
    main()
