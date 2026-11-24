#!/usr/bin/env python3
"""Fill the census rows' sparse columns, using the repo's own rules.

The BoxCompute cards give title, employer, a city and a ~290-char teaser. That
is enough to derive several columns honestly, and enough to make a PRELIMINARY
AI screen -- but NOT enough for the AI flag the study actually wants, which
must rest on the full "Persyaratan Khusus" text (see stage3_fullpage.py). So the
AI column is filled and every value is labelled with its basis, rather than
being presented as if it came from the full page.

Nothing here invents a value: each column is either matched from an existing
field, mapped through a map derived from the original 2,618 rows, or left blank.

Rules reused verbatim from build/prep_postings.py:
  FIN_WORDS, FIN_EMPLOYER            -> in-scope / sector guess
  AI_TERMS, DATA_TERMS, DIGITAL_TERMS -> skill screens
"""
import argparse
import collections
import csv
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data", "id-postings")
CENSUS = os.path.join(D, "postings-boxcompute.csv")

# ---------------------------------------------------------------- repo rules
FIN_WORDS = re.compile(
    r"bank|asuransi|insurance|bancassurance|kredit|credit|pembiayaan|leasing|multifinance|"
    r"fintech|pegadaian|investasi|investment|sekuritas|reksa|paylater|pinjaman|"
    r"teller|collection|collector|underwriting|aktuaris|"
    r"bpo|call center|contact center", re.I)
FIN_EMPLOYER = re.compile(
    r"financ|fifgroup|adira|\bbfi\b|home credit|indomobil finance|oto multiartha|"
    r"kredivo|akulaku|amartha", re.I)
AI_TERMS = [r"artificial intelligence", r"kecerdasan buatan", r"machine learning",
            r"deep learning", r"\bgenerative\s+ai\b", r"\bgen\s?ai\b",
            r"large language model", r"\bllm\b", r"chatgpt", r"\bcopilot\b",
            r"\brpa\b", r"robotic process automation", r"\botomasi\b", r"\bautomation\b",
            r"\bchatbot\b", r"computer vision", r"\bnlp\b", r"prompt engineering",
            r"\bdata scien(ce|tist)\b"]
DATA_TERMS = [r"analisis data", r"data analy(st|sis)", r"\bsql\b", r"\bpython\b",
              r"power bi", r"\btableau\b", r"data science", r"big data",
              r"data visuali[sz]ation", r"\bstatistik\b", r"\bstatistics\b",
              r"data management", r"manajemen data", r"\bdatabase\b", r"\bpandas\b",
              r"\bsas\b", r"\bspss\b"]
DIGITAL_TERMS = [r"\bkomputer\b", r"microsoft office", r"\bexcel\b", r"\bword\b",
                 r"\bdigital\b", r"\baplikasi\b", r"\bsoftware\b", r"\bms office\b"]
AI_RE = re.compile("|".join(AI_TERMS), re.I)
AI_TOKEN = re.compile(r"(?<![A-Za-z])AI(?![A-Za-z])")   # bare "AI", case-SENSITIVE
DATA_RE = re.compile("|".join(DATA_TERMS), re.I)
DIGITAL_RE = re.compile("|".join(DIGITAL_TERMS), re.I)

# ------------------------------------------------------- city -> province
JAKARTA = re.compile(r"jakarta", re.I)
CITY_FALLBACK = {
    "bali": "Bali", "denpasar": "Bali", "yogyakarta": "DI Yogyakarta",
    "sleman": "DI Yogyakarta", "bantul": "DI Yogyakarta",
    "tangerang": "Banten", "tangerang selatan": "Banten", "serang": "Banten",
    "cilegon": "Banten", "bekasi": "Jawa Barat", "depok": "Jawa Barat",
    "bogor": "Jawa Barat", "karawang": "Jawa Barat", "cimahi": "Jawa Barat",
    "surabaya": "Jawa Timur", "malang": "Jawa Timur", "sidoarjo": "Jawa Timur",
    "gresik": "Jawa Timur", "semarang": "Jawa Tengah", "solo": "Jawa Tengah",
    "surakarta": "Jawa Tengah", "magelang": "Jawa Tengah",
    "medan": "Sumatera Utara", "palembang": "Sumatera Selatan",
    "makassar": "Sulawesi Selatan", "balikpapan": "Kalimantan Timur",
    "samarinda": "Kalimantan Timur", "pontianak": "Kalimantan Barat",
    "batam": "Kepulauan Riau", "pekanbaru": "Riau", "padang": "Sumatera Barat",
    "manado": "Sulawesi Utara", "banda aceh": "Aceh",
}

# --------------------------------------------------- title -> job function
JOBFUNC = [
    (re.compile(r"sales|penjualan|marketing|pemasaran|business develop|account exec", re.I),
     "Penjualan dan Pemasaran"),
    (re.compile(r"produksi|production|operator|manufaktur|qc\b|quality control|warehouse|gudang", re.I),
     "Manufaktur dan Produksi"),
    (re.compile(r"akuntan|accounting|finance|keuangan|audit|pajak|tax|staff keuangan", re.I),
     "Akuntansi & Keuangan"),
    (re.compile(r"kredit|credit|loan|pinjaman|collection|collector|penagih|analis kredit", re.I),
     "Kredit / Pinjaman"),
    (re.compile(r"customer service|layanan pelanggan|\bcs\b|call center|contact center", re.I),
     "Layanan Pelanggan"),
    (re.compile(r"\bhr\b|sdm|human resource|rekrut|recruit|personalia", re.I), "SDM"),
    (re.compile(r"developer|programmer|software|engineer|\bit\b|teknologi|data|network|sysadmin", re.I),
     "IT / Teknologi"),
    (re.compile(r"admin|administrasi|sekretar|secretary|office", re.I), "Administrasi & Sekretariat"),
    (re.compile(r"teller|cs\b|banking|bank\b|asuransi|insurance|aktuaris|underwrit", re.I),
     "Perbankan & Asuransi"),
    (re.compile(r"guru|dosen|teacher|trainer|pengajar|instruktur", re.I), "Pendidikan & Pelatihan"),
    (re.compile(r"dokter|perawat|nurse|medis|klinik|farmasi|apotek", re.I), "Kesehatan"),
    (re.compile(r"desain|design|kreatif|creative|content|media|sosial", re.I), "Kreatif & Media"),
    (re.compile(r"logistik|logistic|driver|pengemudi|kurir|ekspedisi|supply chain", re.I), "Logistik & Transportasi"),
    (re.compile(r"hukum|legal|law", re.I), "Hukum"),
]

RE_EDU = re.compile(r"\b(SD|SMP|SMA|SMK|SMU|D1|D2|D3|D4|S1|S2|S3|Diploma|Sarjana|Magister)\b",
                    re.I)
RE_SALARY = re.compile(r"Rp\.?\s?[\d.,]+\s?(juta|jt|ribu|rb)?", re.I)
RE_QUOTA = re.compile(r"(dibutuhkan|memerlukan|kuota)\s+(\d+)|(\d+)\s+(orang|posisi|lowongan)", re.I)
RE_DEADLINE = re.compile(
    r"(batas|deadline|paling lambat|ditutup)[^\d]{0,20}(\d{1,2}\s+\w+\s+\d{4}|\d{1,2}[-/]\d{1,2}[-/]\d{2,4})", re.I)


def norm_city(c):
    c = (c or "").strip().lower()
    c = re.sub(r",?\s*indonesia\s*$", "", c)
    c = re.sub(r"^(kota|kabupaten|kab\.?|kodya|adm\.?)\s+", "", c)
    c = re.sub(r"\s*(regency|city)\s*$", "", c)
    c = re.sub(r"\s*\(.*?\)", "", c)
    return re.sub(r"\s+", " ", c).strip()


def build_city_map():
    m = collections.defaultdict(collections.Counter)
    for f in sorted(glob.glob(os.path.join(D, "postings-*.csv"))):
        if f.endswith("postings-boxcompute.csv"):
            continue
        for r in csv.DictReader(open(f)):
            ci, pr = norm_city(r.get("location_city")), (r.get("location_province") or "").strip()
            if ci and pr and pr.lower() != "indonesia":
                m[ci][pr] += 1
    return {k: v.most_common(1)[0][0] for k, v in m.items()}


def job_function(title):
    for rx, name in JOBFUNC:
        if rx.search(title or ""):
            return name
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    city_map = build_city_map()
    with open(CENSUS, newline="", encoding="utf-8") as fh:
        rd = csv.DictReader(fh)
        cols = rd.fieldnames
        rows = list(rd)

    stats = collections.Counter()
    for r in rows:
        # ---- in_scope only ever had title+employer (job_function was blank),
        #      so derive job_function FIRST so the repo rule can use it.
        jf = job_function(r["title"])
        if jf:
            r["job_function"] = jf
            stats["job_function"] += 1

        # ---- province from the city, via the map learned from the original rows
        ci = norm_city(r.get("location_city"))
        prov = city_map.get(ci) or CITY_FALLBACK.get(ci) or (
            "DKI Jakarta" if JAKARTA.search(ci) else "")
        if prov:
            r["location_province"] = prov
            stats["province"] += 1

        # ---- sector, by the repo's own rule (title + employer + job_function)
        joined = " ".join([r["title"], r.get("employer") or "", r.get("job_function") or ""])
        in_fin = bool(FIN_WORDS.search(joined) or FIN_EMPLOYER.search(r.get("employer") or ""))
        r["in_scope"] = "finance_bpo" if in_fin else "outside_scope"
        r["sector"] = ("Finance/BPO (guessed from title/employer, unverified)" if in_fin
                       else "Outside finance scope (guessed, unverified)")
        stats["in_scope_fin"] += 1 if in_fin else 0

        txt = r.get("content") or ""

        # ---- skill screens, over the teaser
        ai = AI_RE.search(txt) or AI_TOKEN.search(txt)
        d = DATA_RE.search(txt)
        dg = DIGITAL_RE.search(txt)
        if ai:
            r["ai_skill_required"] = "Yes"
            r["ai_tier"] = "teaser-mention"
            r["ai_evidence"] = (ai.group(0) + " :: " +
                                txt[max(0, ai.start() - 40):ai.end() + 40].replace("\n", " "))
            r["ai_source"] = ("card teaser only - PRELIMINARY; the full-page pass "
                              "(stage 3) is what the study counts")
            stats["ai_yes"] += 1
        else:
            r["ai_source"] = ("card teaser only - no AI term in the teaser; not a "
                              "confirmed negative until the full page is read")
        r["data_skill_flag"] = "Yes" if d else "No"
        if d:
            r["data_evidence"] = d.group(0)
            stats["data_yes"] += 1
        r["digital_basic_flag"] = "Yes" if dg else "No"
        if dg:
            stats["digital_yes"] += 1

        # ---- fields the teaser sometimes carries outright
        e = RE_EDU.search(txt)
        if e and not r.get("min_education"):
            r["min_education"] = e.group(0).upper() if len(e.group(0)) <= 3 else e.group(0).title()
            stats["education"] += 1
        s = RE_SALARY.search(txt)
        if s and not r.get("salary_shown"):
            r["salary_shown"] = s.group(0)
            stats["salary"] += 1
        q = RE_QUOTA.search(txt)
        if q and not r.get("quota"):
            r["quota"] = q.group(0)
            stats["quota"] += 1
        dl = RE_DEADLINE.search(txt)
        if dl and not r.get("deadline"):
            r["deadline"] = dl.group(2)
            stats["deadline"] += 1

        # content_chars_full: the teaser length, since the full page is not yet read
        r["content_chars_full"] = str(len(txt))

        # unverified_fields must keep telling the truth about what is still a guess
        guessed = [c for c in ("location_province", "sector", "job_function",
                               "ai_skill_required", "min_education", "salary_shown",
                               "quota", "deadline") if (r.get(c) or "").strip()]
        r["unverified_fields"] = ",".join(guessed)

    print("rows:", len(rows))
    for k in sorted(stats):
        print("  %-18s %5d" % (k, stats[k]))

    if a.dry_run:
        print("(dry run -- nothing written)")
        return 0

    tmp = CENSUS + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, CENSUS)
    print("written:", CENSUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
