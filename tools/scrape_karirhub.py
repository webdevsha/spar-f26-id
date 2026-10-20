#!/usr/bin/env python3
"""Minimal, polite scraper for Karirhub (Kemnaker) individual job postings.

Stdlib only — no pip install, no headless browser. It is the "detail stage" of the
pipeline described in docs/SCRAPING-WITH-BOXCOMPUTE.md: give it seed pages, it
collects posting links, reads each posting page, and writes one CSV row per
posting in the team's schema (timestamp / location / content / AI-skill / domain).

Usage
    python3 tools/scrape_karirhub.py --out out.csv --max 25
    python3 tools/scrape_karirhub.py --out out.csv --seeds https://karirhub.kemnaker.go.id/lowongan-dalam-negeri
    python3 tools/scrape_karirhub.py --urls my_links.txt --out out.csv

Why "seeds" and not keywords: Karirhub's keyword search runs on an Algolia API that
is not reachable from every network. Its category pages ARE server-rendered, so the
honest public route is: seed pages -> posting links -> posting pages. For a large
sweep, let the BoxCompute agent use the browser skill to collect more links first
(see the guide), then feed them here with --urls.

Ethics baked in: identifies itself, sleeps between requests, honours robots.txt,
never touches /api/ or /login, and refuses to store personal data.
"""
import argparse, csv, json, re, sys, time, urllib.error, urllib.parse, urllib.request

BASE = "https://karirhub.kemnaker.go.id"
UA = "SPAR-F26-research/0.1 (academic feasibility test; contact: team)"
DELAY = 0.4
DETAIL_RE = re.compile(r"/lowongan-dalam-negeri/lowongan/[a-z0-9\-]+")

# --- strict skill vocabulary -------------------------------------------------
# Word boundaries matter. A loose "ai" match fires on "AIA" (an insurer) and on
# "mengenai" (Indonesian for "regarding"), and "otomasi" fires on "otomatis".
AI_TERMS = [r"artificial intelligence", r"kecerdasan buatan", r"machine learning",
            r"deep learning", r"\bgenerative\s+ai\b", r"\bgen\s?ai\b", r"\bllm\b",
            r"\bchatgpt\b", r"\bcopilot\b", r"\brpa\b", r"robotic process automation",
            r"\botomasi\b", r"\bautomation\b", r"\bchatbot\b", r"computer vision",
            r"\bnlp\b", r"prompt engineering", r"\bdata scien(ce|tist)\b"]
DATA_TERMS = [r"analisis data", r"data analy(st|sis)", r"\bsql\b", r"\bpython\b",
              r"power bi", r"\btableau\b", r"\bbig data\b", r"data visuali[sz]ation",
              r"\bstatistik\b", r"\bstatistics\b", r"manajemen data", r"\bdatabase\b"]
AI_RE = re.compile("|".join(AI_TERMS), re.I)
AI_TOKEN = re.compile(r"(?<![A-Za-z])AI(?![A-Za-z])")   # uppercase only
DATA_RE = re.compile("|".join(DATA_TERMS), re.I)

FIN_RE = re.compile(r"bank|financ|asuransi|insurance|kredit|credit|pembiayaan|leasing|"
                    r"multifinance|fintech|pegadaian|investasi|investment|sekuritas|"
                    r"paylater|pinjaman|teller|underwriting|aktuaris|"
                    r"\bbpo\b|call center|contact center|outsourc", re.I)

PERSONAL_FIELDS = ("picName", "picIdNumber", "picEmail", "picPhone")


def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "id"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def check_robots():
    """Refuse to run if the site disallows us. Cheap insurance, prints the rule."""
    try:
        txt = get(BASE + "/robots.txt", timeout=15)
    except Exception as e:                       # no robots.txt reachable
        print(f"[robots] could not read robots.txt ({e}) — continuing, be gentle")
        return
    allows = re.search(r"(?im)^user-agent:\s*\*\s*$(?:\s*\n)?allow:\s*/", txt)
    print("[robots] " + ("Allow: / for * — OK" if allows else "no blanket Allow: / — check before scraping"))
    if not allows:
        sys.exit("robots.txt does not allow general crawling; stopping.")


def harvest(seeds):
    links = []
    for s in seeds:
        try:
            html = get(s)
        except Exception as e:
            print(f"[seed] {s} -> {type(e).__name__}: {str(e)[:70]}")
            continue
        found = sorted(set(DETAIL_RE.findall(html)))
        print(f"[seed] {s} -> {len(found)} posting links")
        links += found
        time.sleep(DELAY)
    seen, out = set(), []
    for l in links:
        if l in seen:
            continue
        seen.add(l)
        out.append(l)
    return out


def rsc_blob(html):
    """Karirhub is a Next.js app: the posting object rides inside streamed RSC chunks."""
    parts = []
    for m in re.finditer(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', html):
        try:
            parts.append(json.loads(m.group(1)))
        except Exception:
            pass
    return "".join(parts)


def find_object(blob, anchor='"vacancyable":{'):
    i = blob.find(anchor)
    if i < 0:
        return None
    start, depth = i, 0
    while start > 0:                              # walk back to the opening brace
        ch = blob[start]
        if ch == "}":
            depth += 1
        elif ch == "{":
            if depth == 0:
                break
            depth -= 1
        start -= 1
    depth, instr, esc = 0, False, False
    for j in range(start, len(blob)):             # then parse forward, respecting strings
        ch = blob[j]
        if instr:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                instr = False
            continue
        if ch == '"':
            instr = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(blob[start:j + 1])
                except Exception:
                    return None
    return None


def strip_html(s):
    if not s:
        return ""
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"</(p|li|div)>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&nbsp;", " ", s)
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def parse(html, url):
    obj = find_object(rsc_blob(html))
    if not obj:
        return None
    emp = obj.get("employer") or {}
    ent = emp.get("employerable") or {}
    industry = (ent.get("industry") or {}).get("name") or ""
    region = (obj.get("region") or {}).get("name") or ""
    parts = [p.strip() for p in region.split(",") if p.strip()]
    desc = strip_html(obj.get("description"))
    qual = strip_html(obj.get("qualification"))
    skills = obj.get("skills") or []
    blob = " ".join([obj.get("title") or "", desc, qual, " ".join(skills)])
    ai_hit = AI_RE.search(blob) or AI_TOKEN.search(blob)
    data_hit = DATA_RE.search(blob)
    return {
        "job_id": obj.get("id"),
        "posted_at": (obj.get("publishedAt") or "")[:10],
        "posted_basis": "exact (publishedAt)",
        "location_city": parts[0] if parts else "",
        "location_province": parts[-1] if parts else "",
        "title": obj.get("title") or "",
        "employer": emp.get("name") or "",
        "sector": industry,
        "skills": "; ".join(skills),
        "content": desc[:240],
        "ai_skill_required": "Yes" if ai_hit else "No",
        "ai_evidence": ai_hit.group(0) if ai_hit else "",
        "data_skill_flag": "Yes" if data_hit else "No",
        "data_evidence": data_hit.group(0) if data_hit else "",
        "min_education": (obj.get("minEducation") or {}).get("name", "")
                          if isinstance(obj.get("minEducation"), dict) else "",
        "deadline": (obj.get("expiresAt") or "")[:10],
        "quota": obj.get("quota") or "",
        "url": BASE + url,
        "domain": "PUBLIC",
        "source": "karirhub.kemnaker.go.id (live detail page)",
        "captured_at": time.strftime("%Y-%m-%d"),
    }


COLS = ["job_id", "posted_at", "posted_basis", "location_city", "location_province",
        "title", "employer", "sector", "skills", "content", "ai_skill_required",
        "ai_evidence", "data_skill_flag", "data_evidence", "min_education", "deadline",
        "quota", "url", "domain", "source", "captured_at"]


def main():
    ap = argparse.ArgumentParser(description="Scrape Karirhub individual postings (public pages).")
    ap.add_argument("--out", default="karirhub-postings.csv")
    ap.add_argument("--max", type=int, default=25, help="max posting pages to fetch")
    ap.add_argument("--since", default="", help="keep rows posted on/after YYYY-MM-DD")
    ap.add_argument("--finance-only", action="store_true", help="keep bank/insurance/BPO only")
    ap.add_argument("--seeds", nargs="*", default=[BASE + "/lowongan-dalam-negeri"])
    ap.add_argument("--urls", help="file with one posting URL per line (from the browser skill)")
    args = ap.parse_args()

    check_robots()

    if args.urls:
        links = [l.strip().replace(BASE, "") for l in open(args.urls) if l.strip()]
        print(f"[links] {len(links)} from {args.urls}")
    else:
        links = harvest(args.seeds)
    links = links[: args.max]
    print(f"[links] fetching {len(links)} posting pages at {DELAY}s apart")

    rows, skipped = [], 0
    for i, link in enumerate(links, 1):
        try:
            html = get(BASE + link)
            rec = parse(html, link)
        except urllib.error.HTTPError as e:
            print(f"  [{i}/{len(links)}] HTTP {e.code} — skipped (not retried)")
            skipped += 1
            continue
        except Exception as e:
            print(f"  [{i}/{len(links)}] {type(e).__name__} — skipped")
            skipped += 1
            continue
        if not rec:
            skipped += 1
            continue
        if args.since and rec["posted_at"] and rec["posted_at"] < args.since:
            skipped += 1
            continue
        if args.finance_only and not FIN_RE.search(
                " ".join([rec["title"], rec["employer"], rec["sector"], rec["content"]])):
            skipped += 1
            continue
        rows.append(rec)
        if i % 10 == 0:
            print(f"  [{i}/{len(links)}] kept {len(rows)}")
        time.sleep(DELAY)

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    ai = sum(1 for r in rows if r["ai_skill_required"] == "Yes")
    print(f"\n[done] {len(rows)} rows -> {args.out}  (skipped {skipped}; AI-flagged {ai})")
    print("[note] postings are advertised demand, not hires; keep the coverage caveat.")


if __name__ == "__main__":
    main()
