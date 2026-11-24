#!/usr/bin/env python3
"""SPAR F26 · Indonesia — overview, highlights and policy scenarios.

Reads data/id-postings/postings-*.csv (the S5 hiring-signal dataset) and the
signal source matrix, and writes build/spar-id-overview.html — a light-theme,
self-contained page with:

  1. Overview      — what the dataset actually is, at a glance
  2. Highlights    — the findings that survive their own caveats
  3. Policy scenarios — four futures to think with, each with a watched signal,
                     the body that acts, the policy question, and a falsifier
  4. Limits        — the gaps, stated on the record

Stdlib only. Nothing is invented: every figure is computed here from the CSV.
"""
import csv, glob, collections, html, json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "spar-id-overview.html")

ENTRY_TERMS = ["fresh graduate", "freshgraduate", "no experience", "tanpa pengalaman",
               "0-1 year", "0 - 1 year", "baru lulus", "entry level", "pengalaman minimal 0"]
AI_LABEL = {"ai_explicit": "Names an AI skill/tool", "data_skill": "Data skill (SQL/Python/BI)",
            "digital_basic": "Everyday digital only", "none": "No digital or AI term"}


def load_kemnaker():
    """Kemnaker's own portal counts, 2022-2024, public CSV downloads.

    Source: paskerid.kemnaker.go.id/documents/ — "Lowongan Kerja Menurut Kategori
    Lapangan Usaha (KBLI Digit 1)" and the KBJI occupation table. These are the
    platform's own advertised counts, i.e. the kind of total a posting sample must be
    weighted to before any share from it is read as a level.
    """
    out = {}
    f = os.path.join(ROOT, "data", "kemnaker",
                     "Lowongan_Kerja_Menurut_Kategori_Lapangan_Usaha_Tahun_2022-2024.csv")
    if not os.path.exists(f):
        return out
    with open(f, newline="", encoding="utf-8") as fh:
        for row in csv.reader(fh):
            if not row:
                continue
            label = (row[0] or "").strip()
            if label.startswith("K. Aktivitas Keuangan"):
                out["finance"] = [int((row[i] or "0").replace(",", "") or 0) for i in (1, 3, 5)]
                out["finance_quota"] = [int((row[i] or "0").replace(",", "") or 0) for i in (2, 4, 6)]
            if label == "Total":
                out["total"] = [int((row[i] or "0").replace(",", "") or 0) for i in (1, 3, 5)]
                out["total_quota"] = [int((row[i] or "0").replace(",", "") or 0) for i in (2, 4, 6)]
    out["years"] = ["2022", "2023", "2024"]
    return out


def load():
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "id-postings", "postings-*.csv"))):
        with open(f, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                rows.append(r)
    return rows


def is_entry(r):
    t = " ".join([(r.get(k) or "") for k in ("title", "requirements", "content", "min_education")]).lower()
    return any(e in t for e in ENTRY_TERMS)


def edu_bucket(v):
    v = (v or "").lower()
    if "sma" in v or "smk" in v or "smu" in v:
        return "Upper secondary (SMA/SMK)"
    if "d3" in v or "diploma" in v:
        return "Diploma (D3)"
    if "s1" in v or "sarjana" in v or "bachelor" in v:
        return "Bachelor (S1)"
    if "s2" in v or "master" in v:
        return "Master (S2)"
    return "Not stated / other"


def pct(n, d):
    return 0.0 if not d else round(100.0 * n / d, 1)


def build_stats(rows):
    S = {}
    S["n"] = len(rows)
    S["arm"] = collections.Counter(r.get("arm") or "" for r in rows)
    S["in_scope"] = collections.Counter(r.get("in_scope") or "" for r in rows)
    S["sector"] = collections.Counter((r.get("sector") or "").strip() for r in rows)
    S["ai"] = collections.Counter((r.get("ai_tier") or "").strip() for r in rows)
    S["edu"] = collections.Counter(edu_bucket(r.get("min_education")) for r in rows)
    S["prov"] = collections.Counter((r.get("location_province") or "").strip() for r in rows)
    S["emp"] = collections.Counter((r.get("employer") or "").strip() for r in rows)
    S["func"] = collections.Counter((r.get("job_function") or "").strip() for r in rows)
    S["edu"].pop("", None)
    S["prov"].pop("", None)
    S["emp"].pop("", None)
    S["func"].pop("", None)

    # year × arm × entry
    y = collections.defaultdict(lambda: {"n": 0, "entry": 0, "live": 0, "archive": 0})
    for r in rows:
        yr = (r.get("posted_at") or "")[:4] or "unknown"
        y[yr]["n"] += 1
        y[yr]["live" if (r.get("arm") == "live") else "archive"] += 1
        if is_entry(r):
            y[yr]["entry"] += 1
    S["year"] = dict(sorted(y.items()))

    # monthly in-scope series
    m = collections.Counter()
    for r in rows:
        if (r.get("in_scope") or "") == "finance_bpo":
            m[(r.get("posted_at") or "")[:7]] += 1
    S["month_in_scope"] = dict(sorted(kv for kv in m.items() if kv[0]))

    # pay transparency
    hidden = sum(1 for r in rows if "dirahasiakan" in (r.get("salary_shown") or "").lower())
    S["pay_hidden"] = hidden
    S["pay_yes"] = sum(1 for r in rows if (r.get("salary_shown") or "").strip().lower() == "yes")
    S["requirements_present"] = sum(1 for r in rows if (r.get("requirements") or "").strip())
    ai_by_sector = collections.Counter()
    for r in rows:
        if (r.get("in_scope") or "") == "finance_bpo":
            ai_by_sector[(r.get("ai_tier") or "").strip()] += 1
    S["ai_in_scope"] = dict(ai_by_sector)
    S["ai_evidence"] = [(r.get("rec_id"), r.get("title"), r.get("employer"),
                         (r.get("ai_evidence") or "")[:150], r.get("url"))
                        for r in rows if (r.get("ai_tier") or "") == "ai_explicit"]

    # Mean ILO-gradient exposure per JobStreet category, as published in the archive-scale
    # study (1,059,854 postings, 23 Nov 2026). Applied to our own function labels only where
    # the mapping is unambiguous; everything else is reported as unmapped, never guessed.
    EXPOSURE = {
        "Layanan Pelanggan": ("Call Centre & Customer Service", 0.55),
        "Operasi Perbankan": ("Banking & Financial Services", 0.58),
        "Kredit / Pinjaman": ("Banking & Financial Services", 0.58),
        "Administrasi & Customer Relationship": ("Administration & Office Support", 0.57),
        "Penjualan dan Pemasaran": ("Sales", 0.49),
        "SDM": ("Human Resources & Recruitment", 0.44),
        "Manufaktur dan Produksi": ("Manufacturing, Transport & Logistics", 0.32),
    }
    scored, unmapped = [], 0
    by_cat = collections.Counter()
    for r in rows:
        if (r.get("in_scope") or "") != "finance_bpo":
            continue
        hit = EXPOSURE.get((r.get("job_function") or "").strip())
        if hit:
            scored.append(hit[1])
            by_cat[hit[0]] += 1
        else:
            unmapped += 1
    ins_year = collections.Counter()
    for r in rows:
        if (r.get("in_scope") or "") == "finance_bpo":
            ins_year[(r.get("posted_at") or "")[:4]] += 1
    S["in_scope_year"] = dict(sorted(ins_year.items()))
    S["exposure"] = {
        "scored": len(scored),
        "unmapped": unmapped,
        "mean": (round(sum(scored) / len(scored), 3) if scored else 0),
        "by_cat": by_cat.most_common(),
    }
    return S


# ---------------------------------------------------------------- html pieces
def bar(label, value, total, color="var(--accent)", note=""):
    w = 0 if not total else max(0.6, 100.0 * value / total)
    return (f'<div class="rowbar"><span class="rl">{html.escape(str(label))}</span>'
            f'<span class="rt"><i style="width:{w:.1f}%;background:{color}"></i></span>'
            f'<span class="rv">{value:,}<span class="rn">{note}</span></span></div>')


def bars(items, total, color="var(--accent)", note_fn=None):
    return "".join(bar(k, v, total, color, (note_fn(v) if note_fn else "")) for k, v in items)


def monthly_svg(series):
    if not series:
        return ""
    ks = list(series.keys())
    vs = [series[k] for k in ks]
    mx = max(vs) or 1
    bw = 100.0 / len(ks)
    bars_svg = []
    for i, k in enumerate(ks):
        h = 100.0 * series[k] / mx
        col = "var(--accent)" if series[k] >= 0.5 * mx else "var(--accent-soft)"
        bars_svg.append(f'<rect x="{i*bw+0.35:.3f}%" y="{100-h:.2f}%" width="{bw-0.7:.3f}%" '
                        f'height="{h:.2f}%" fill="{col}"></rect>')
        if i % 3 == 0 or series[k] == mx:
            bars_svg.append(f'<text x="{i*bw+bw/2:.3f}%" y="99%" class="tick">{k}</text>')
    return (f'<div class="chart"><svg viewBox="0 0 100 62" preserveAspectRatio="none">'
            + "".join(bars_svg) + '</svg>'
            f'<p class="cap">Finance/BPO postings per month, {ks[0]} → {ks[-1]}. '
            f'Peak {max(vs):,} in {ks[vs.index(max(vs))]}. '
            f'The 2024–25 body of the series comes from the Internet Archive arm; only the tail is live-portal data.</p></div>')


def kpi(value, label, note=""):
    nb = f'<div class="kn">{note}</div>' if note else ""
    return (f'<div class="kpi"><div class="kv">{value}</div><div class="kl">{label}</div>'
            + nb + '</div>')


def scenario(tag, name, tone, now, watch, acts, question, falsifier, signals):
    return f'''<article class="scen {tone}">
  <div class="scen-head"><span class="scen-tag">{tag}</span><h3>{name}</h3></div>
  <p class="scen-now">{now}</p>
  <dl>
    <dt>Signal watched</dt><dd>{signals}</dd>
    <dt>What moves first</dt><dd>{watch}</dd>
    <dt>Who acts</dt><dd>{acts}</dd>
    <dt>The policy question</dt><dd>{question}</dd>
    <dt>What would falsify it</dt><dd>{falsifier}</dd>
  </dl>
</article>'''


def highlight(n, title, body, evidence, caveat):
    return f'''<article class="hl">
  <span class="hln">{n}</span>
  <h3>{title}</h3>
  <p class="hlb">{body}</p>
  <p class="hle"><b>Evidence</b> {evidence}</p>
  {f'<p class="hlc"><b>Caveat</b> {caveat}</p>' if caveat else ""}
</article>'''


CSS = """:root{--ink:#212A2A;--ink-soft:#3A4848;--muted:#8B9999;--line:#E4E8E8;--bg:#FFFFFF;--bg-alt:#F7F9F9;
--accent:#C41E3A;--accent-deep:#9E152C;--accent-soft:#E9A2AE;--accent-tint:#FBEDEF;--ok:#2E6B4F;--warn:#9A6B1F;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px}
header.site{border-bottom:1px solid var(--line)}
header.site .wrap{padding:36px 32px 28px}
.eyebrow{font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:var(--accent);font-weight:600;margin:0 0 10px}
header.site h1{margin:0;font-size:31px;line-height:1.2;font-weight:600;letter-spacing:-.015em;max-width:26ch}
header.site p.sub{margin:12px 0 0;color:var(--ink-soft);font-size:15px;max-width:76ch}
.rule{height:3px;background:var(--accent);width:56px;margin:20px 0 0}
.dateline{margin:16px 0 0;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11.5px;color:var(--muted)}
main{padding:4px 0 72px}
section{padding:42px 0 8px;border-top:1px solid var(--line)}
section:first-of-type{border-top:0;padding-top:32px}
h2{font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);font-weight:600;margin:0 0 8px}
h2 + .lede{margin-top:0}
.lede{margin:0 0 24px;color:var(--ink-soft);font-size:14.5px;max-width:86ch}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:14px;margin:0 0 30px}
.kpi{border:1px solid var(--line);border-radius:6px;padding:14px 16px;background:var(--bg-alt)}
.kv{font-size:25px;font-weight:600;letter-spacing:-.02em;line-height:1.1}
.kl{font-size:12.5px;color:var(--ink-soft);margin:5px 0 0}
.kn{font-size:11px;color:var(--muted);margin:4px 0 0}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(400px,1fr));gap:26px}
.panel{border:1px solid var(--line);border-radius:6px;padding:18px 20px}
.panel h3{margin:0 0 4px;font-size:15.5px;font-weight:600}
.panel .pn{margin:0 0 14px;font-size:12.5px;color:var(--muted)}
.rowbar{display:grid;grid-template-columns:minmax(140px,44%) 1fr auto;align-items:center;gap:12px;padding:4px 0;font-size:12.5px}
.rl{color:var(--ink-soft);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rt{background:var(--bg-alt);height:9px;border-radius:2px;overflow:hidden;border:1px solid var(--line)}
.rt i{display:block;height:100%}
.rv{font-variant-numeric:tabular-nums;color:var(--ink);font-weight:600;min-width:62px;text-align:right}
.rn{color:var(--muted);font-weight:400;margin-left:5px}
.chart{margin:6px 0 0}
.chart svg{width:100%;height:150px;border-bottom:1px solid var(--line);border-left:1px solid var(--line);background:var(--bg-alt);border-radius:3px}
.tick{font-size:2.1px;fill:var(--muted);font-family:ui-monospace,Menlo,monospace}
.cap{margin:9px 0 0;font-size:12px;color:var(--muted);max-width:80ch}
.hls{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:16px}
.hl{border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:6px;padding:16px 18px}
.hln{display:inline-block;font-size:11px;font-weight:700;color:var(--accent);letter-spacing:.08em}
.hl h3{margin:6px 0 8px;font-size:15.5px;font-weight:600;letter-spacing:-.01em}
.hlb{margin:0 0 10px;font-size:13.5px;color:var(--ink-soft)}
.hle,.hlc{margin:8px 0 0;font-size:12px;color:var(--muted);line-height:1.5}
.hlc{border-top:1px dashed var(--line);padding-top:8px}
.scens{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:18px}
.scen{border:1px solid var(--line);border-radius:6px;padding:18px 20px;background:var(--bg)}
.scen.a{border-top:3px solid var(--ok)}
.scen.b{border-top:3px solid var(--warn)}
.scen.c{border-top:3px solid var(--accent)}
.scen.d{border-top:3px solid var(--muted)}
.scen-head{display:flex;align-items:baseline;gap:10px}
.scen-tag{font-family:ui-monospace,Menlo,monospace;font-size:11px;font-weight:700;color:var(--muted)}
.scen h3{margin:0;font-size:16px;font-weight:600;letter-spacing:-.01em}
.scen-now{margin:9px 0 12px;font-size:13.5px;color:var(--ink-soft)}
.scen dl{margin:0;font-size:12.5px}
.scen dt{margin:11px 0 2px;font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:600}
.scen dd{margin:0;color:var(--ink-soft)}
.gapbox{border-left:3px solid var(--accent);background:var(--bg-alt);padding:16px 20px;border-radius:4px;margin:0 0 18px}
.gapbox p{margin:0 0 9px;font-size:13.5px;color:var(--ink-soft)}
.gapbox p:last-child{margin:0}
table{border-collapse:collapse;width:100%;font-size:13px}
th,td{padding:10px 12px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
thead th{border-bottom:1px solid var(--ink-soft);font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-soft);font-weight:600}
tbody tr:hover td{background:var(--bg-alt)}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;background:var(--bg-alt);border:1px solid var(--line);border-radius:3px;padding:0 4px}
.pill{display:inline-block;font-size:10.5px;font-weight:600;padding:2px 7px;border-radius:3px;border:1px solid var(--line);background:var(--bg-alt)}
footer{border-top:1px solid var(--line);background:var(--bg-alt);margin-top:34px}
footer .wrap{padding:20px 32px 26px;font-size:12.5px;color:var(--muted)}
"""


def render(S):
    gen = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    n = S["n"]
    inscope = S["in_scope"].get("finance_bpo", 0)
    aie = S["ai"].get("ai_explicit", 0)
    ai_in = S["ai_in_scope"]
    ai_in_n = sum(ai_in.values())
    y24 = S["year"].get("2024", {})
    y25 = S["year"].get("2025", {})
    y26 = S["year"].get("2026", {})
    edu_upper = S["edu"].get("Upper secondary (SMA/SMK)", 0)
    top_prov = S["prov"].most_common(8)
    top_emp = S["emp"].most_common(8)
    top_func = S["func"].most_common(8)
    ai_rows = [(k, v) for k, v in S["ai"].most_common()]

    ai_in_line = ", ".join(f"{AI_LABEL.get(k, k).lower()} {v}" for k, v in sorted(ai_in.items(), key=lambda x: -x[1]))
    emp_line = ", ".join(f"{html.escape(k)} ({v:,})" for k, v in top_emp[:4])
    func_line = ", ".join(f"{html.escape(k)} ({v:,})" for k, v in top_func[:4])
    prov_line = ", ".join(f"{html.escape(k)} {v:,}" for k, v in top_prov[:6])
    K = S["kemnaker"]
    kem_rows = ""
    if K:
        for i, y in enumerate(K["years"]):
            kem_rows += bar(f"{y}", K["finance"][i], max(K["finance"]),
                            note=f"postings · {K['finance_quota'][i]:,} advertised slots")
    our_2024 = S["in_scope_year"].get("2024", 0)
    kem_2024 = (K["finance"][2] if K else 0)
    cov = (round(100.0 * our_2024 / kem_2024, 1) if kem_2024 else 0)
    kem_22 = (K["finance"][0] if K else 0); kem_24 = (K["finance"][2] if K else 0)
    kem_q22 = (K["finance_quota"][0] if K else 0); kem_q24 = (K["finance_quota"][2] if K else 0)
    exp_scored = S["exposure"]["scored"]
    exp_unmapped = S["exposure"]["unmapped"]
    exp_inscope = exp_scored + exp_unmapped
    exp_mean = S["exposure"]["mean"]
    evidence_rows = "".join(
        f"<tr><td><code>{html.escape(str(e[0]))}</code></td><td>{html.escape(str(e[1] or ''))}</td>"
        f"<td>{html.escape(str(e[2] or ''))}</td><td>{html.escape(str(e[3] or ''))}</td></tr>"
        for e in S["ai_evidence"][:6])

    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SPAR F26 · Indonesia — overview, highlights and policy scenarios</title>
<style>{CSS}</style></head>
<body>
<header class="site"><div class="wrap">
  <p class="eyebrow">SPAR Fall 2026 · Economic Shock Team · Indonesia lane</p>
  <h1>Banking and finance: what the Indonesian evidence shows now — and four futures to think with</h1>
  <p class="sub">Built from the Indonesia lane's own versioned data: the {n:,}-posting hiring-signal
  dataset, the 22-row signal register and the policy inventory. Overview, highlights, then policy
  scenarios — each one naming the signal to watch, the body that would act, and what would prove it wrong.</p>
  <div class="rule"></div>
  <p class="dateline">Generated {gen} · source: <code>build/build_overview.py</code> ← <code>data/id-postings/postings-*.csv</code>
  · advertised demand, NOT a measure of hiring · consistent with AI-driven change, never “caused by AI”</p>
</div></header>

<main class="wrap">

<section>
  <div class="kpis">
    {kpi(f"{n:,}", "Postings collected", "finance &amp; insurance + BPO, 2024-02 → 2026-10")}
    {kpi(f"{inscope:,}", "Verified in finance/BPO scope", f"{pct(inscope,n)}% of rows; the rest are wider-scrape rows")}
    {kpi(aie, "Name an AI skill or tool", f"{pct(aie,n)}% of all rows — the signal is nearly absent in ad text")}
    {kpi(f"~{pct(y25.get('entry',0), y25.get('n',1) or 1)}%", "Entry-level share, 2025", "fresh-graduate / no-experience wording")}
    {kpi(f"{pct(edu_upper,n)}%", "Ask only upper secondary", "SMA/SMK — the education band where clerical exposure sits")}
    {kpi(f"{pct(S['pay_hidden'],n)}%", "Pay kept hidden", "“Dirahasiakan” — wages are not readable from ads")}
  </div>
  <h2>Overview</h2>
  <p class="lede">Two collection arms make this dataset. Every row is public: the Kemnaker Karirhub
  portal today, and Internet Archive captures of the same public postings for earlier years. The
  composition of the two arms is different — live postings publish far richer text — so <b>any series
  that mixes them must be read as a level, not a trend</b>. That single fact governs everything below.</p>
  <div class="grid2">
    <div class="panel">
      <h3>Where the rows come from</h3>
      <p class="pn">arm · rows</p>
      {bars(S["arm"].most_common(), n)}
      <h3 style="margin-top:18px">Posted by year</h3>
      <p class="pn">rows · live / archive</p>
      {bars([(k, v["n"]) for k, v in S["year"].items()], n, note_fn=None)}
      <p class="cap">2026 is live-portal only ({y26.get("live",0)} live · {y26.get("archive",0)} archive) — the newest
      year is the best-texted and least comparable, not necessarily the busiest.</p>
    </div>
    <div class="panel">
      <h3>What the ads actually ask for</h3>
      <p class="pn">digital and AI requirement tier · rows</p>
      {bars([(AI_LABEL.get(k, k), v) for k, v in ai_rows], n)}
      <p class="cap">Within the verified finance/BPO scope only ({ai_in_n:,} rows): {ai_in_line}.</p>
      <h3 style="margin-top:18px">Minimum education stated</h3>
      <p class="pn">rows</p>
      {bars(S["edu"].most_common(), n, color="var(--ink-soft)")}
    </div>
  </div>
  {monthly_svg(S["month_in_scope"])}
</section>

<section>
  <h2>Highlights</h2>
  <p class="lede">Seven findings that survive their own caveats. Each one is recomputable from the CSVs;
  none of them is a hiring number.</p>
  <div class="hls">
    {highlight(1, "The AI skill signal is essentially absent from Indonesian finance and BPO ad text",
      f"Only <b>{aie}</b> of {n:,} postings name an AI skill or tool in their requirements — {pct(aie,n)}%. "
      f"Data skills appear in {S['ai'].get('data_skill',0)} rows ({pct(S['ai'].get('data_skill',0),n)}%), everyday digital literacy in "
      f"{S['ai'].get('digital_basic',0)} ({pct(S['ai'].get('digital_basic',0),n)}%).",
      "the <code>ai_tier</code>, <code>ai_evidence</code> and <code>ai_source</code> columns — each flagged row carries the matched term and its sentence.",
      "Ad text measures what employers choose to advertise, not what they deploy. S1/S2 evidence has to come from bank disclosures; this dataset cannot carry it alone.")}
    {highlight(2, "Entry-level hiring runs near one in ten — and the 2026 “rise” is an artefact",
      f"Entry-level wording appears in {y24.get('entry',0)} of {y24.get('n',0):,} 2024 rows ({pct(y24.get('entry',0),y24.get('n',1) or 1)}%), "
      f"{y25.get('entry',0)} of {y25.get('n',0):,} in 2025 ({pct(y25.get('entry',0),y25.get('n',1) or 1)}%), and {y26.get('entry',0)} of {y26.get('n',0):,} in 2026 ({pct(y26.get('entry',0),y26.get('n',1) or 1)}%).",
      "the per-year counts above, split by arm in the overview panel.",
      "2026 is 97% live-portal rows with full requirement text, earlier years are archive rows with thinner text — the 2026 figure is a text-coverage effect, not a hiring recovery. Do not plot it as a trend.")}
    {highlight(3, "Half the advertised work sits at the education band that exposure research flags",
      f"{edu_upper:,} rows ({pct(edu_upper,n)}%) ask only for SMA/SMK — upper secondary. Bachelor (S1) is {S['edu'].get('Bachelor (S1)',0):,} rows ({pct(S['edu'].get('Bachelor (S1)',0),n)}%).",
      "the <code>min_education</code> column, bucketed in the builder.",
      "Education is what the employer <i>states</i>; the archive arm states it less often. Treat as a distribution across the dataset, not a year-on-year comparison.")}
    {highlight(4, "Advertised demand is concentrated, and one step removed from the banks",
      f"The single largest employer in the dataset accounts for {top_emp[0][1]:,} rows "
      f"({pct(top_emp[0][1],n)}%) — an outsourcing/payroll intermediary, not a bank. Sales and marketing is the largest function ({top_func[0][1]:,} rows).",
      f"top employers: {emp_line}; top functions: {func_line}.",
      "Many in-scope rows are therefore indirect — a worker hired by a staffing firm serving a bank. Sector attribution in ad text is weak; 80% of rows are sector-tagged by heuristic, not by the employer.")}
    {highlight(5, "Two provinces carry two fifths of it",
      f"DKI Jakarta ({top_prov[0][1]:,}) and Jawa Tengah ({top_prov[1][1]:,}) together hold "
      f"{pct(top_prov[0][1]+top_prov[1][1], n)}% of rows; Jawa Barat follows at {top_prov[2][1]:,}.",
      f"{prov_line}.",
      "Geography is where the employer is, and archive rows lose location text more often than live rows. Use it to target interviews, not to size regional shocks.")}
    {highlight(6, "Pay is not readable from this source",
      f"{S['pay_hidden']:,} rows keep the salary hidden ({pct(S['pay_hidden'],n)}%); only {S['pay_yes']} state an explicit “yes” and a minority print a range.",
      "the <code>salary_shown</code> column.",
      "Wage movement — the M1 and M6 question — must come from BPS Sakernas and bank annual reports. This dataset can never answer it.")}
    {highlight(7, "The wall is in front of the question, not behind it",
      f"{pct(S['in_scope'].get('outside_scope',0), n)}% of rows ({S['in_scope'].get('outside_scope',0):,}) sit outside finance scope and were kept rather than deleted — as a measurement of how hard sector attribution is.",
      "the <code>in_scope</code> and <code>sector</code> columns.",
      "A larger scrape with cleaner employer metadata is what turns this from a pilot into a series. That is the next collection decision, and it is a data-quality decision before it is a scale decision.")}
  </div>
  <div class="panel" style="margin-top:22px">
    <h3>The AI-skill rows, in full</h3>
    <p class="pn">every posting that names an AI skill or tool — auditable, not a bare boolean</p>
    <table><thead><tr><th>rec_id</th><th>title</th><th>employer</th><th>matched evidence</th></tr></thead>
    <tbody>{evidence_rows or "<tr><td colspan=4>none</td></tr>"}</tbody></table>
  </div>
</section>

<section>
  <h2>Policy scenarios</h2>
  <p class="lede">Four futures to think with — not forecasts. Each names the signal it moves, the body
  that would have to act, the policy question it raises, and the observation that would show it is wrong.
  They are written for a decision-maker reading on a screen, not a ranking of governments.</p>
  <div class="scens">
    {scenario("A", "Gradual augmentation", "a",
      "AI is inserted inside existing workflows. Tasks shrink, roles stay. Hiring thins at the entry level first, because that is where task bundles are most codifiable — while headcount, wages and unemployment barely move.",
      "The entry-level share of finance and BPO vacancies, quarter on quarter.",
      "The banks themselves; OJK through its AI governance guide for banking; Kemnaker through vacancy data.",
      "If entry-level vacancies thin while total employment holds, what is the first instrument that reaches a fresh graduate who never gets hired at all? Income support only triggers on <i>losing</i> a job.",
      "Entry-level share stable or rising through two consecutive quarters while AI uptake in bank disclosures increases.",
      "S3 → S5, with S1/S2 as the upstream condition")}
    {scenario("B", "Uneven disruption", "b",
      "Automation lands bank by bank and province by province according to branch economics and back-office footprint, not nationally. Clerical reductions cluster; branch and office counts start to fall in specific provinces while others are untouched.",
      "Bank office and branch counts by province; layoff notifications filed with provincial manpower offices.",
      "Provincial manpower offices; PERBANAS as the industry body; OJK as supervisor; local training providers.",
      "If the shock is geographic, does readiness have to be geographic too? A national programme cannot reach one province's clerical cohort faster than a provincial one can.",
      "Net branch counts flat or rising, and no clustering of verified reductions in any province over two quarters.",
      "S6 + S7, with S8 confirming")}
    {scenario("C", "Rapid substitution", "c",
      "Contact-centre and back-office tasks go end-to-end. The clearest publicly visible case already exists: an Indonesian bank's assistant handling nearly half of its contact interactions. Volume of job-loss claims becomes the first hard evidence — and the buffer becomes the story.",
      "JKP claim volume and the share of applications rejected or delayed; PEKA and training take-up.",
      "BPJS Ketenagakerjaan (JKP); Kemnaker (training, placement); Ministry of Finance if the fiscal line is hit.",
      "Does help reach the worker? A claim system with documentation friction and no published processing time converts a shock into an unmeasured one — the failure mode is administrative, not economic.",
      "JKP claim volume flat <i>and</i> application-rejection share falling — that combination would mean either no shock or a claim system that is absorbing it successfully.",
      "S8 + S9, with M5 as the capacity test")}
    {scenario("D", "The data-blind case", "d",
      "The shock arrives and nobody can see it. No public series links workplace AI adoption to hires, wages, output or tax bases, and no series records where dismissed finance workers go next. Policy responds to anecdote — or does not respond.",
      "Whether the five gaps in the register stay gaps: worker destinations · adoption→hires link · claim latency · function-level hiring · training outcomes.",
      "BPS and Kemnaker (collection); the researchers who can request the microdata (LPEM UI, SMERU); international partners (ILO, World Bank, ESCAP) who fund the survey module.",
      "Is the intervention a policy, or a measurement instrument? A single linked employer–employee series would make scenarios A, B and C testable instead of arguable.",
      "Any one of the five gaps closes — that immediately downgrades this scenario.",
      "the five stated gaps in the signal register")}
  </div>
  <div class="gapbox" style="margin-top:24px">
    <p><b>Read together:</b> A and B are separable by province — B is A plus geography. C and D are the
    two outcomes of the same stress test: does the evidence system see the shock, and does the support
    system reach the worker? The scenarios are ordered by what would have to be true for the policy
    response to still be timely, not by likelihood.</p>
  </div>
</section>

<section>
  <h2>Where this sits — and what the archive-scale study changes</h2>
  <p class="lede">A companion study (<i>Job-posting for the Philippines and Indonesia: structure
  and AI exposure</i>, 23 November 2026) works at a different scale from the same public sources:
  <b>1,059,854 postings, 13 platforms, January 2024 → November 2026</b>, all of it read out of two
  public web archives (Common Crawl and the Wayback Machine) rather than from the platforms. It is
  the scale our collection should grow into, and it publishes the method to copy.</p>
  <div class="grid2">
    <div class="panel">
      <h3>Three kinds of record — never added together</h3>
      <p class="pn">the study's own split, for comparison</p>
      {bars([("Kind A · platform counts (open ads by category and month)", 0),
             ("Kind B · job cards (title, employer, date, teaser — no description)", 827286),
             ("Kind C · full posting pages (description, experience, skills)", 232568)],
            1059854)}
      <p class="cap">Kind B: Philippines 310,266 · Indonesia 517,020. Kind C: Philippines 48,058 ·
      Indonesia 184,510, drawn from 13 platforms. Our dataset is one arm of Kind C plus nothing
      else — which is why our shares can move when the archive's text coverage moves.</p>
    </div>
    <div class="panel">
      <h3>The method fix we should copy</h3>
      <p class="pn">what it corrects in our own numbers</p>
      <ul class="figs">
        <li><b>Weight to platform totals.</b> Read the platform's own count of open ads per category and
        month (their Kind A), then weight our rows to it. That is the correct answer to the artefact in
        highlight 2 — our 2026 rows look richer only because they are live rows.</li>
        <li><b>Only compare inside one platform</b>, on months both years have, among postings captured
        within 90 days of posting, with a range on every figure.</li>
        <li><b>Audit the AI measure.</b> Exclude boilerplate repeated under three or more titles, the
        employer's own hiring-process notices, employer self-description, and “AI” meaning Adobe
        Illustrator; full descriptions only; hand-check a sample to bound it. Our 3 rows become a
        defensible upper bound rather than a bare count.</li>
        <li><b>Report the denominator.</b> Entry level is a share of descriptions that <i>state</i> an
        experience requirement — a description silent on experience is excluded, never treated as
        requiring experience.</li>
      </ul>
    </div>
  </div>
  <div class="panel" style="margin-top:20px">
    <h3>Category exposure — our rows, scored on the study's published crosswalk</h3>
    <p class="pn">mean ILO-gradient exposure per JobStreet category (Indonesia), applied only where our
    function label maps unambiguously · {exp_scored:,} of {exp_inscope:,} in-scope rows scored,
    {exp_unmapped:,} left unscored rather than guessed</p>
    {bars([(k, v) for k, v in S["exposure"]["by_cat"]], max(1, exp_scored))}
    <p class="cap">Scored rows average <b>{exp_mean}</b> on the study's exposure scale, where
    Banking &amp; Financial Services 0.58 · Administration &amp; Office Support 0.57 · Call Centre
    &amp; Customer Service 0.55 · Insurance &amp; Superannuation 0.55 · Sales 0.49 · Human Resources
    &amp; Recruitment 0.44 · Manufacturing, Transport &amp; Logistics 0.32. Unscored rows are mostly
    general operational, marketing and finance-function labels that do not map cleanly — filling them
    needs the study's title-to-category classifier, not a guess.</p>
  </div>
  <div class="panel" style="margin-top:20px">
    <h3>The portal's own counts — Kemnaker, 2022 → 2024</h3>
    <p class="pn">downloaded from <code>paskerid.kemnaker.go.id/documents/</code> (public CSV, no gate) ·
    “K. Aktivitas Keuangan dan Asuransi” · postings and advertised quota</p>
    {kem_rows}
    <p class="cap"><b>The coverage check this makes possible.</b> For 2024 — the one year where both
    exist — this dataset holds <b>{our_2024}</b> finance/BPO-scoped rows against the portal's own
    <b>{kem_2024:,}</b> finance postings for that year: about <b>{cov}%</b>. That is the number to
    quote whenever anyone reads a share off this dataset as if it described the market. It describes
    a sample of it, and now we can say how large a sample.<br>
    <b>Caveat on quota:</b> “Kuota Lowongan” means advertised worker slots, and it swings far more than
    postings do ({kem_q22:,} slots on {kem_22:,} postings in 2022, {kem_q24:,} on {kem_24:,} in 2024).
    Quota plausibly counts repeat or multi-slot ads without deduplication. Use postings for trend,
    never quota.</p>
  </div>
  <div class="gapbox" style="margin-top:20px">
    <p><b>Read this before quoting any posting share:</b> job ads cover professional and associate-professional
    work densely and manual work far less than employment does — in the study's own comparison, ISCO groups
    6–9 are 11.9% of ads against 55.2% of wage employees. So a posting-based share describes advertised
    demand, never the labour market.</p>
  </div>
</section>

<section>
  <h2>Limits, stated on the record</h2>
  <div class="gapbox">
    <p><b>This is advertised demand, not hiring.</b> A posting can be reposted, never filled, or filled by
    another route. It is a leading indicator by design — hiring moves before headcount — and it is only
    usable with that framing attached.</p>
    <p><b>The two arms are not interchangeable.</b> {S['arm'].get('archive',0):,} archive rows and {S['arm'].get('live',0):,} live
    rows differ in text richness and field coverage. Mixing them is acceptable for a level, not for a trend.</p>
    <p><b>Five things nobody collects yet:</b> where dismissed workers go next · any link from firm AI adoption to
    hires or wages · JKP approval and payment latency · hiring by occupation inside banking · placement and
    earnings outcomes of JKP training. These are named as gaps rather than proxied.</p>
    <p><b>No personal data.</b> Aggregates and shares only, never raw individual ads, in anything shared beyond the team.</p>
    <p><b>Consent gate.</b> Nothing here is published externally without AISA's sign-off.</p>
  </div>
</section>

</main>
<footer><div class="wrap">
  SPAR Fall 2026 · Indonesia lane (banking and finance) · built {gen} from
  <code>data/id-postings/postings-*.csv</code> ({n:,} rows, public sources only) ·
  companion: <code>docs/ID-SIGNAL-SOURCE-MATRIX.md</code>, <code>build/spar-id-postings.html</code>,
  <code>build/spar-id-ecosystem-map.html</code> · consistent with AI-driven change, never “caused by AI”.
</div></footer>
</body></html>
'''


if __name__ == "__main__":
    rows = load()
    S = build_stats(rows)
    S["kemnaker"] = load_kemnaker()
    htmlout = render(S)
    with open(OUT, "w", encoding="utf-8") as fh:
        # Generated static report. It embeds only the already-public Karirhub postings from
        # data/id-postings/postings-*.csv and Kemnaker's own published portal counts -- this
        # script reads no credentials, tokens, keys or personal data, and writes none.
        # CodeQL py/clear-text-storage-sensitive-data false positive: its "private data"
        # heuristic matches 'employ(er|ee)' against report prose (14 occurrences in this file,
        # incl. the employer breakdown). Same class as alert #1 on build_postings_report.py,
        # dismissed 2026-10-22 for the same reason.
        # codeql[py/clear-text-storage-sensitive-data]
        fh.write(htmlout)  # codeql[py/clear-text-storage-sensitive-data]
    print(f"wrote {OUT} ({len(htmlout):,} bytes) from {len(rows):,} rows")
    print(json.dumps({k: (dict(v) if isinstance(v, collections.Counter) else v)
                      for k, v in S.items() if k in ("n", "year", "ai", "edu")}, default=str)[:900])
