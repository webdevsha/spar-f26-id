#!/usr/bin/env python3
"""Normalise the raw Karirhub scrape (scratch/feas/out_postings.csv) into the
team-facing schema: timestamp | location | content | AI-skill flag | domain.

Writes  data/id-postings/karirhub-id-postings-sample.csv
and     data/id-postings/summary.json   (stats used by build_postings_report.py)

Ethics: descriptions are truncated to SNIPPET chars on purpose -- we keep enough
text to judge the AI-skill question without republishing whole platform pages.
"""
import csv, json, os, re, collections, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "scratch", "feas", "out_postings.csv")
OUTDIR = os.path.join(ROOT, "data", "id-postings")
SNIPPET = 240

# --- strict skill definitions (the previous run used a loose "ai" substring that
# --- matched Indonesian words and company names -- e.g. "komputer" flagged as AI)
AI_TERMS = [
    r"artificial intelligence", r"kecerdasan buatan",
    r"machine learning", r"deep learning", r"\bgenerative\s+ai\b", r"\bgen\s?ai\b",
    r"large language model", r"\bllm\b", r"chatgpt", r"\bcopilot\b",
    r"\brpa\b", r"robotic process automation", r"\botomasi\b", r"\bautomation\b",
    r"\bchatbot\b", r"computer vision", r"\bnlp\b", r"prompt engineering",
    r"\bdata scien(ce|tist)\b",
]
DATA_TERMS = [
    r"analisis data", r"data analy(st|sis)", r"\bsql\b", r"\bpython\b", r"\br\b(?= programming)",
    r"power bi", r"\btableau\b", r"data science", r"big data", r"data visuali[sz]ation",
    r"\bstatistik\b", r"\bstatistics\b", r"data management", r"manajemen data",
    r"\bdatabase\b", r"\bpandas\b", r"\bsas\b", r"\bspss\b",
]
DIGITAL_TERMS = [
    r"\bkomputer\b", r"microsoft office", r"\bexcel\b", r"\bword\b", r"\bdigital\b",
    r"\baplikasi\b", r"\bsoftware\b", r"\bms office\b",
]
AI_RE = re.compile("|".join(AI_TERMS), re.I)
# standalone uppercase "AI" only: a case-insensitive \bai\b would fire on Indonesian
# words and on "genai" inside "mengenai"
AI_TOKEN = re.compile(r"(?<![A-Za-z])AI(?![A-Za-z])")
DATA_RE = re.compile("|".join(DATA_TERMS), re.I)
DIGITAL_RE = re.compile("|".join(DIGITAL_TERMS), re.I)


def skill_class(text):
    """Return (ai_hit, data_hit, digital_hit) as matched strings or ''."""
    a = AI_RE.search(text or "") or AI_TOKEN.search(text or "")
    d = DATA_RE.search(text or "")
    g = DIGITAL_RE.search(text or "")
    return (a.group(0) if a else "", d.group(0) if d else "", g.group(0) if g else "")


# Sector for ARCHIVED rows only (live rows carry the portal's own industry field).
# The captured page exposes no industry, so we guess from sector-bearing fields.
# The first version also searched the ad body and used loose tokens ("cs ", "dana",
# "outsourc"), which made an HR Officer at a ceramics firm "finance". Now:
#   * look only at title + employer + job_function, never the description;
#   * generic tokens that do not name a sector (customer service, outsourcing, cs) are out;
#   * "financ" counts on the employer name only -- an in-house "Finance & Accounting"
#     role at a property firm does not make the employer a finance firm.
FIN_WORDS = re.compile(
    r"bank|asuransi|insurance|bancassurance|kredit|credit|pembiayaan|leasing|multifinance|"
    r"fintech|pegadaian|investasi|investment|sekuritas|reksa|paylater|pinjaman|"
    r"teller|collection|collector|underwriting|aktuaris|"
    r"bpo|call center|contact center", re.I)
FIN_EMPLOYER = re.compile(
    r"financ|fifgroup|adira|\bbfi\b|home credit|indomobil finance|oto multiartha|"
    r"kredivo|akulaku|amartha", re.I)


def archive_in_finance(r):
    return bool(FIN_WORDS.search(" ".join([r["title"], r["employer"], r["job_function"]]))
                or FIN_EMPLOYER.search(r["employer"]))


# The captured <title> tag is "Dapatkan pekerjaan dari seluruh dunia : Karirhub - <job>";
# an older parser kept that site slogan as part of the job title.
SLOGAN = re.compile(r"^\s*Dapatkan pekerjaan dari seluruh dunia\s*[-:\u2013]\s*(Karirhub\s*[-\u2013]\s*)?",
                    re.I)


def title_province(p):
    """str.title() turns 'DKI JAKARTA' into 'Dki Jakarta'; keep the acronyms."""
    return re.sub(r"\b(Dki|Diy)\b", lambda m: m.group(1).upper(), p.title())


def clean_title(t):
    return clean(SLOGAN.sub("", t or ""))


def split_location(loc):
    """'CITY, PROVINCE, Indonesia' -> ('CITY', 'PROVINCE'). The portal prints the country
    as a trailing component on some pages. The old parser took the LAST component as the
    province, so every such row got province='Indonesia' (40 archive rows). Drop the
    country first, then province = last component, city = the one before it."""
    parts = [x.strip() for x in (loc or "").split(",") if x.strip()]
    if parts and parts[-1].lower() == "indonesia":
        parts = parts[:-1]
    if len(parts) >= 2:
        return parts[-2], parts[-1]
    return (parts[0] if parts else ""), ""


def clean(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def wayback_meta():
    """The raw crawl keeps the capture filename (ts_slug-uuid); rebuild the archive URL
    from it so every archived row is traceable. Returns {(title, captured): (url, file)}."""
    meta = os.path.join(ROOT, "scratch", "feas", "wb_details.json")
    if not os.path.exists(meta):
        return {}
    out = {}
    for r in json.load(open(meta)):
        fp = r.get("file", "")
        f = os.path.basename(fp).replace(".html", "")
        if "_" not in f:
            continue
        ts, rest = f.split("_", 1)
        if len(ts) == 14 and ts.isdigit():
            out[(r.get("title") or "", r.get("captured") or "")] = (
                f"https://web.archive.org/web/{ts}/"
                f"https://karirhub.kemnaker.go.id/lowongan-dalam-negeri/lowongan/{rest}",
                os.path.join(ROOT, "scratch", "feas", fp))
    return out


def capture_location(path):
    """Fallback when the raw parser found no location: the rendered page prints
    '<job title>|<location>|Diposting' (some captures use a longer
    'kelurahan, kecamatan, kabupaten, province, Indonesia' form)."""
    try:
        h = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""
    h = re.sub(r"<(script|style).*?</\1>", "", h, flags=re.S)
    t = re.sub(r"<[^>]+>", "|", h)
    t = re.sub(r"\s+", " ", re.sub(r"\|[\s|]*\|", "|", t))
    m = re.search(r"Memuat\.\.\.\s*\|\s*[^|]+\|\s*([^|]+?)\s*\|\s*Diposting", t)
    return clean(m.group(1)) if m else ""


def main():
    rows = list(csv.DictReader(open(SRC)))
    wb = wayback_meta()
    out, i = [], 0
    for r in rows:
        live = r["arm"] == "live"
        raw_title = r["title"]          # capture lookups are keyed on the raw crawl title
        r["title"] = clean_title(raw_title)
        sector = clean(r["sector"])
        blob = " ".join([r["title"], r["employer"], r["desc"], r["skills"], r["job_function"]])
        # sector for archived rows is not exposed on the captured page -> classify
        if not sector:
            fin_hit = archive_in_finance(r)
            sector = ("Finance/BPO (guessed from title/employer, unverified)" if fin_hit
                      else "Outside finance scope (guessed, unverified)")
        in_fin = live or (fin_hit and sector.startswith("Finance"))
        ai_hit, data_hit, dig_hit = skill_class(blob)
        if ai_hit:
            tier = "ai_explicit"
        elif data_hit:
            tier = "data_skill"
        elif dig_hit:
            tier = "digital_basic"
        else:
            tier = "none"
        if live:
            city = clean(r["location"]).split(",")[0] if clean(r["location"]) else ""
            province = title_province(clean(r["province"]))
        else:
            loc = clean(r["location"]) or capture_location(
                wb.get((raw_title, r["captured"] or ""), ("", ""))[1])
            city, province = split_location(loc)
            province = title_province(province)
        i += 1
        out.append({
            "rec_id": f"IN-P-{i:03d}",
            "arm": "live" if live else "archive",
            "source": "karirhub.kemnaker.go.id (live detail page)" if live
                      else "web.archive.org snapshot of karirhub.kemnaker.go.id",
            "domain": "PUBLIC",
            "domain_note": "Open government portal, no login; robots.txt Allow: /" if live
                           else "Public archive mirror of a public government portal page",
            "posted_at": r["posted"],
            "posted_basis": r["posted_basis"],
            "captured_at": r["captured"] or "2026-10-20",
            "location_city": city,
            "location_province": province,
            "title": clean(r["title"]),
            "employer": clean(r["employer"]),
            "sector": sector,
            "in_scope": "finance_bpo" if in_fin else "outside_scope",
            "job_function": clean(r["job_function"]),
            "skills": clean(r["skills"]),
            "content": clean(r["desc"])[:SNIPPET],
            "content_chars_full": r["desc_chars"],
            "ai_skill_required": "Yes" if ai_hit else "No",
            "ai_tier": tier,
            "ai_evidence": ai_hit or ("" if not data_hit else ""),
            "data_skill_flag": "Yes" if data_hit else "No",
            "data_evidence": data_hit,
            "digital_basic_flag": "Yes" if dig_hit else "No",
            "min_education": clean(r["min_education"]),
            "salary_shown": clean(r["salary_shown"]),
            "deadline": clean(r["deadline"]),
            "quota": clean(r["quota"]),
            "url": r["url"] or wb.get((raw_title, r["captured"] or ""), ("", ""))[0],
            "_in_fin": in_fin,
        })

    os.makedirs(OUTDIR, exist_ok=True)
    cols = [k for k in out[0] if not k.startswith("_")]
    with open(os.path.join(OUTDIR, "karirhub-id-postings-sample.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in out:
            w.writerow({k: r[k] for k in cols})

    fin = [r for r in out if r["_in_fin"]]
    live = [r for r in out if r["arm"] == "live"]
    arch = [r for r in out if r["arm"] == "archive"]
    arch_fin = [r for r in arch if r["_in_fin"]]

    def tally(rs, key):
        return dict(collections.Counter(r[key] for r in rs).most_common())

    summary = {
        "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "window": ["2025-10-20", "2026-10-20"],
        "totals": {
            "rows": len(out), "live": len(live), "archive": len(arch),
            "finance_scope": len(fin), "archive_finance": len(arch_fin),
        },
        "sector": tally(live, "sector"),
        "month": dict(sorted(collections.Counter(r["posted_at"][:7] for r in fin).items())),
        "month_archive": dict(sorted(collections.Counter(r["posted_at"][:7] for r in arch).items())),
        "province": tally(fin, "location_province"),
        "employer_top": dict(collections.Counter(r["employer"] for r in fin).most_common(10)),
        "ai": {
            "flagged": sum(1 for r in fin if r["ai_skill_required"] == "Yes"),
            "of": len(fin),
            "tier": tally(fin, "ai_tier"),
            "data_flag": sum(1 for r in fin if r["data_skill_flag"] == "Yes"),
        },
        "by_sector_ai": {},
        "archive_quality": {
            "rows": len(arch),
            "missing_employer": sum(1 for r in arch if not r["employer"]),
            "missing_skills": sum(1 for r in arch if not r["skills"]),
            "missing_url": sum(1 for r in arch if not r["url"]),
            "sector_keyword_matched": sum(1 for r in arch if r["sector"].startswith("Finance")),
            "province_missing": sum(1 for r in arch if not r["location_province"]),
            "province_is_country": sum(1 for r in out if r["location_province"] == "Indonesia"),
            "date_derived": sum(1 for r in arch if r["posted_basis"].startswith("derived")),
        },
        "education": tally(fin, "min_education"),
        "salary_shown": tally(fin, "salary_shown"),
    }
    for sec in ("Banking & Financial Services", "Business Process Outsourcing (BPO)",
                "Insurance"):
        rs = [r for r in fin if r["sector"] == sec]
        summary["by_sector_ai"][sec] = {
            "n": len(rs),
            "ai": sum(1 for r in rs if r["ai_skill_required"] == "Yes"),
            "data": sum(1 for r in rs if r["data_skill_flag"] == "Yes"),
            "digital": sum(1 for r in rs if r["ai_tier"] in ("digital_basic", "ai_adjacent", "ai_explicit")),
        }
    json.dump(summary, open(os.path.join(OUTDIR, "summary.json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps(summary["totals"], indent=1))
    print("wrote", OUTDIR)


if __name__ == "__main__":
    main()
