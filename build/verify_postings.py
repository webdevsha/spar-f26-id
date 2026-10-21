#!/usr/bin/env python3
"""Re-fetch every row's source page and compare it with the CSV.

  live rows    -> the Karirhub detail page embeds the vacancy JSON; compare
                  title, publishedAt, expiresAt, status and employer.
  archive rows -> the Wayback capture must load (HTTP 200) and contain the title
                  (and the employer, when the CSV has one).

Stdlib only. Identified User-Agent, 0.4 s between live requests, 1 s between
archive requests (web.archive.org is slower and rate-limits). Read-only.

  python3 build/verify_postings.py                # all rows (~12 min)
  python3 build/verify_postings.py --limit 10     # first 10 live + first 5 archive
  python3 build/verify_postings.py --out report.json
"""
import argparse, csv, html, json, os, re, sys, time, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "data", "id-postings", "karirhub-id-postings-sample.csv")
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
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="only the first N live (and N/2 archive) rows")
    ap.add_argument("--out", default="", help="write the per-row report as JSON")
    a = ap.parse_args()
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    live = [r for r in rows if r["arm"] == "live"]
    arch = [r for r in rows if r["arm"] == "archive"]
    if a.limit:
        live, arch = live[:a.limit], arch[:max(1, a.limit // 2)]
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
    if a.out:
        json.dump(out, open(a.out, "w"), indent=1)
    sys.exit(0 if all(not x["problems"] for x in out) else 1)


if __name__ == "__main__":
    main()
