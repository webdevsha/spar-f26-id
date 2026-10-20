#!/usr/bin/env python3
"""Render build/spar-id-postings.html from data/id-postings/{_rows.json,summary.json}.

Self-contained: no CDN, no fonts, no analytics. The posting table is client-side
sortable/filterable from an embedded JSON array.
"""
import json, os, html, csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data", "id-postings")
rows = list(csv.DictReader(open(os.path.join(D, "karirhub-id-postings-sample.csv"))))
S = json.load(open(os.path.join(D, "summary.json")))

for r in rows:
    r["fin"] = 1 if r.get("in_scope") == "finance_bpo" else 0
FIN = [r for r in rows if r["fin"]]
AQ = S["archive_quality"]

MONTHS = ["2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03",
          "2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10"]
live_m = S["month"]
arch_m = S["month_archive"]
prov = S["province"]
sector = S["sector"]
bai = S["by_sector_ai"]
emp_top = S["employer_top"]

n_all = S["totals"]["rows"]
n_live = S["totals"]["live"]
n_arch = S["totals"]["archive"]
n_fin = S["totals"]["finance_scope"]
ai_n = S["ai"]["flagged"]
ai_of = S["ai"]["of"]
data_n = S["ai"]["data_flag"]
uniq_emp = len({r["employer"] for r in FIN if r["employer"]})
uniq_prov = len({r["location_province"] for r in FIN if r["location_province"] and r["location_province"] != "Indonesia"})


def esc(s):
    return html.escape(str(s or ""))


def bars_month():
    w, h, pad = 940, 210, 34
    bw = (w - 2 * pad) / len(MONTHS)
    mx = max([live_m.get(m, 0) + arch_m.get(m, 0) for m in MONTHS] + [1])
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="postings per month">']
    out.append(f'<line x1="{pad}" y1="{h-pad}" x2="{w-pad}" y2="{h-pad}" stroke="#E3E7E7"/>')
    for i, m in enumerate(MONTHS):
        x = pad + i * bw + bw * .18
        bwid = bw * .64
        a = arch_m.get(m, 0); l = live_m.get(m, 0)
        ha = (a / mx) * (h - 2 * pad)
        hl = (l / mx) * (h - 2 * pad)
        if a:
            out.append(f'<rect x="{x:.1f}" y="{h-pad-ha:.1f}" width="{bwid:.1f}" height="{ha:.1f}" fill="#0F6E7A" opacity=".85"><title>{m}: {a} archived</title></rect>')
        if l:
            out.append(f'<rect x="{x:.1f}" y="{h-pad-ha-hl:.1f}" width="{bwid:.1f}" height="{hl:.1f}" fill="#C41E3A"><title>{m}: {l} live</title></rect>')
        tot = a + l
        if tot:
            out.append(f'<text x="{x+bwid/2:.1f}" y="{h-pad-ha-hl-5:.1f}" font-size="10" fill="#212A2A" text-anchor="middle">{tot}</text>')
        out.append(f'<text x="{x+bwid/2:.1f}" y="{h-pad+15}" font-size="9.5" fill="#8B9999" text-anchor="middle">{m[2:]}</text>')
    out.append("</svg>")
    return "".join(out)


def hbars(d, total=None, color="#C41E3A", unit="", topn=10):
    items = list(d.items())[:topn]
    mx = max([v for _, v in items] + [1])
    out = ['<div class="hbars">']
    for k, v in items:
        pct = v / mx * 100
        out.append(f'<div class="hrow"><span class="hlab">{esc(k) or "(blank)"}</span>'
                   f'<span class="hbar"><i style="width:{pct:.1f}%;background:{color}"></i></span>'
                   f'<span class="hval">{v}{unit}</span></div>')
    out.append("</div>")
    return "".join(out)


ETH = [
    ("robots.txt respected", "ok",
     "karirhub.kemnaker.go.id/robots.txt is <code>User-agent: * → Allow: /</code> with only admin/dashboard/api/login disallowed. We fetched only public <code>/lowongan-dalam-negeri/lowongan/…</code> pages and never touched the disallowed paths."),
    ("No personal data", "ok",
     "No applicant names, CVs, e-mail addresses, phone numbers or recruiter contacts were collected. Rows hold company names only, as published in the public advertisement — consistent with <code>data/PERSONAL-DATA-STOP.md</code>."),
    ("Identified crawler + rate limit", "ok",
     "Requests carried <code>User-Agent: SPAR-F26-research/0.1 (academic feasibility test)</code> and slept ~0.35 s between pages (~1.5k pages, single-threaded pool of 4). No parallel hammering, no retries against 4xx."),
    ("No anti-bot circumvention", "warn",
     "We did <b>not</b> spoof tokens, rotate proxies or solve challenges. Where a platform refused us (Kalibrr KJS API 400/404, BCA candidate API 403, JobStreet/Indeed 403) we recorded the refusal and stopped — that is why those arms are absent, not because the data does not exist."),
    ("Public domain only", "ok",
     "Every row is PUBLIC: a government portal page (live arm) or its public Internet Archive capture (archive arm). No logins, no paid feeds, no access requests were used."),
    ("Minimal re-publication", "warn",
     "Ad text is truncated to 240 characters and skills/attributes are kept as short fields, so the repo does not become a wholesale mirror of the platform. Full text stays in local scratch only."),
    ("Coverage-bias caveat stated", "warn",
     "The count of rows here is <b>not</b> the number of vacancies that existed. Live listings only survive while open, so the panel is recency-skewed; archive captures are uneven. Every chart below is labelled as a sample, not a census."),
    ("Advertised demand ≠ hires", "warn",
     "Postings measure advertised labour demand. They do not establish hiring rates, filled positions or employment — the distinction the team flagged for the IMF-inspired scenario work."),
]


def eth_rows():
    out = []
    for title, mark, body in ETH:
        badge = ('<span class="pill green">PASS</span>' if mark == "ok"
                 else '<span class="pill amber">CAVEAT</span>')
        out.append(f'<tr><td class="et">{badge}</td><td><b>{title}</b><br><span class="etx">{body}</span></td></tr>')
    return "".join(out)


METHOD = [
    ("Karirhub individual posting pages (live)",
     "karirhub.kemnaker.go.id/lowongan-dalam-negeri/lowongan/&lt;slug&gt;-&lt;uuid&gt;",
     "WORKS", "ok",
     "281 finance/BPO postings with exact <code>publishedAt</code>, province + city, employer, education, skills and description. Server-rendered — no Algolia needed once you have the detail URL."),
    ("Karirhub search API (Algolia app L3WWP72HSI)",
     "algolia.kemnaker.go.id · *.algolianet.com",
     "BLOCKED", "bad",
     "DNS does not resolve from this network (<code>No address associated with hostname</code>). This is the point where the earlier Hermes attempt stalled. Worked around by harvesting detail URLs from keyword result pages instead."),
    ("Internet Archive (CDX + snapshots)",
     "web.archive.org/cdx/search/cdx · /web/&lt;ts&gt;/…",
     "PARTIAL", "warn",
     "50 archived postings inside the window (9 finance-matched). Coverage is dense for Oct–Dec 2025, then collapses — good for a 12-month baseline, unusable as a monthly panel on its own."),
    ("Kalibrr / BNI recruitment career page",
     "recruitment.bni.co.id (Kalibrr tenant 24707) · kalibrr.com/kjs/…",
     "BLOCKED", "bad",
     "Page loads, but the tenant is a client-side Kalibrr app: <code>__NEXT_DATA__</code> carries only company metadata, and the KJS endpoints answer <code>400 BAD REQUEST</code> / <code>404</code>. No postings retrievable without their private API."),
    ("BCA career portal",
     "karir.bca.co.id/candidate/api/*",
     "BLOCKED", "bad",
     "Only <code>/candidate/api/city</code> is open (200, returns the city dictionary); every vacancy endpoint returns <code>403</code>. Needs a session token — out of scope for a public-data test."),
    ("Pasker ID / Satu Data Kemnaker aggregates",
     "paskerid.kemnaker.go.id · satudata.kemnaker.go.id",
     "AGGREGATE", "warn",
     "2022–2024 official vacancy counts by occupation/sector/province. Public, but count-level — cannot carry a timestamp+location+content row. Kept as the historical baseline (see the other report)."),
]


def method_rows():
    out = []
    for name, url, status, cls, note in METHOD:
        out.append(f'<tr><td><b>{name}</b><br><code>{url}</code></td>'
                   f'<td class="c"><span class="pill {cls}">{status}</span></td>'
                   f'<td>{note}</td></tr>')
    return "".join(out)


DOMAIN = [
    ("Karirhub posting page (live arm)", "PUBLIC", "ok",
     "Government portal, no login, robots <code>Allow: /</code>. Published by the employer through the Ministry's own system."),
    ("Web Archive capture of the same page", "PUBLIC", "ok",
     "Public mirror; the underlying record is the same public posting. Capture timestamps differ from posting dates — we keep both fields."),
    ("Pasker ID / Satu Data CSVs", "PUBLIC", "ok",
     "Open government data, 2022–2024, aggregate counts."),
    ("Kalibrr tenant API (BNI, others)", "PRIVATE-PLATFORM", "warn",
     "Commercial platform behind an API key; we could not read it without circumventing their controls, so we did not."),
    ("Bank career portals (BCA, Mandiri)", "PRIVATE-PLATFORM", "warn",
     "Publicly visible UI, but vacancy data sits behind a session/API layer and each bank's ToS governs reuse. Would need per-bank permission."),
    ("JobStreet / Indeed / LinkedIn", "PRIVATE-PLATFORM", "bad",
     "403 to non-browser clients and explicit anti-scraping terms. Not used."),
]


def domain_rows():
    out = []
    for name, d, cls, note in DOMAIN:
        out.append(f'<tr><td><b>{name}</b></td><td class="c"><span class="pill {cls}">{d}</span></td><td>{note}</td></tr>')
    return "".join(out)


sector_bars = hbars({k: v for k, v in sector.items()}, color="#C41E3A")
prov_bars = hbars(prov, color="#0F6E7A", topn=10)

AI_ROWS = "".join(
    f'<tr><td>{esc(k)}</td><td class="n">{v["n"]}</td><td class="n">{v["ai"]}</td>'
    f'<td class="n">{v["data"]}</td><td class="n">{v["digital"]}</td>'
    f'<td class="n">{(v["ai"]/v["n"]*100 if v["n"] else 0):.1f}%</td></tr>'
    for k, v in bai.items())

TABLE_JSON = json.dumps([{
    "id": r["rec_id"], "posted": r["posted_at"], "basis": r["posted_basis"],
    "loc": r["location_city"] or r["location_province"],
    "prov": r["location_province"], "title": r["title"], "emp": r["employer"],
    "sector": r["sector"], "content": r["content"], "skills": r["skills"],
    "ai": r["ai_skill_required"], "tier": r["ai_tier"], "ai_ev": r["ai_evidence"],
    "data": r["data_skill_flag"], "edu": r["min_education"], "arm": r["arm"],
    "fin": r["fin"], "url": r["url"], "src": r["source"], "dom": r["domain"],
    "cap": r["captured_at"],
} for r in rows], ensure_ascii=False)

HTML = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>SPAR F26 · Indonesia — Karirhub individual postings (preliminary scrape)</title>
<style>
:root{{--ink:#212A2A;--soft:#3A4848;--muted:#8B9999;--line:#E3E7E7;--bg:#FFFFFF;--alt:#F7F9F9;
      --cr:#C41E3A;--cr2:#9E152C;--cr3:#7A1022;--tint:#FBEDEF;--teal:#0F6E7A;--teal-t:#E7F1F2}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);line-height:1.6;
  font:16px/1.6 -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",Roboto,Helvetica,Arial,sans-serif}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 32px}}
a{{color:var(--cr2);text-decoration:none;border-bottom:1px solid var(--tint)}}a:hover{{border-bottom-color:var(--cr)}}
header.site{{border-bottom:1px solid var(--line)}}header.site .wrap{{padding:34px 32px 26px}}
.eyebrow{{font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:var(--cr);font-weight:600;margin:0 0 10px}}
h1{{margin:0;font-size:31px;line-height:1.2;font-weight:600;letter-spacing:-.015em}}
header.site p.sub{{margin:10px 0 0;color:var(--soft);font-size:15px;max-width:76ch}}
.accent-rule{{height:3px;background:var(--cr);width:56px;margin:18px 0 0}}
.banner{{background:var(--tint);border-bottom:1px solid var(--line);color:var(--cr3);font-size:13.5px}}
.banner .wrap{{padding:11px 32px}}
main{{padding:6px 0 72px}}
section{{padding:38px 0 6px;border-top:1px solid var(--line)}}section:first-of-type{{border-top:0}}
h2{{font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);font-weight:600;margin:0 0 8px}}
h3{{font-size:18px;margin:22px 0 6px;font-weight:600;letter-spacing:-.01em}}
.lede{{margin:0 0 22px;color:var(--soft);font-size:14.5px;max-width:84ch}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:14px;margin:6px 0 8px}}
.kpi{{border:1px solid var(--line);border-radius:6px;padding:16px 18px;background:var(--bg)}}
.kpi .v{{font-size:27px;font-weight:600;letter-spacing:-.02em;line-height:1.1}}
.kpi .l{{font-size:12px;color:var(--muted);margin-top:6px;text-transform:uppercase;letter-spacing:.08em}}
.kpi.acc{{border-left:3px solid var(--cr)}} .kpi.tl{{border-left:3px solid var(--teal)}}
table{{width:100%;border-collapse:collapse;font-size:13.5px;margin:12px 0}}
th,td{{border-bottom:1px solid var(--line);padding:9px 10px;text-align:left;vertical-align:top}}
thead th{{background:var(--alt);font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:600;position:sticky;top:0;z-index:2}}
td.n{{text-align:right;font-variant-numeric:tabular-nums}}
td.c{{text-align:center}}
.pill{{display:inline-block;font-size:10.5px;font-weight:700;padding:2px 8px;border-radius:999px;white-space:nowrap;letter-spacing:.03em}}
.pill.ok,.pill.green{{background:#E7F4EA;color:#1E7A3C}}
.pill.warn,.pill.amber{{background:#FFF4E0;color:#8A5800}}
.pill.bad{{background:var(--tint);color:var(--cr3)}}
.pill.grey{{background:#EFF2F2;color:#5A6A6A}}
.card{{border:1px solid var(--line);border-radius:6px;padding:18px 20px;margin:14px 0;background:var(--bg)}}
.card.acc{{border-left:3px solid var(--cr)}} .card.tl{{border-left:3px solid var(--teal)}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
@media(max-width:820px){{.grid2{{grid-template-columns:1fr}}}}
.hbars{{margin:6px 0 0}}
.hrow{{display:grid;grid-template-columns:200px 1fr 46px;align-items:center;gap:10px;margin:5px 0;font-size:12.5px}}
.hlab{{color:var(--soft);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.hbar{{background:#F0F3F3;height:11px;border-radius:2px;overflow:hidden}}
.hbar i{{display:block;height:100%}}
.hval{{text-align:right;color:var(--muted);font-variant-numeric:tabular-nums}}
.verdict{{background:var(--ink);color:#fff;border-radius:6px;padding:20px 22px;margin:4px 0 24px}}
.verdict p{{color:#D7E0E0;margin:0;font-size:14.5px;max-width:92ch}} .verdict b{{color:#fff}}
.legend{{font-size:12px;color:var(--muted);margin:6px 0 0}}
.legend i{{display:inline-block;width:10px;height:10px;border-radius:2px;margin:0 5px 0 12px;vertical-align:middle}}
.et{{width:110px}} .etx{{color:var(--soft);font-size:13px}}
.controls{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:14px 0 6px}}
.controls input[type=search]{{flex:1 1 240px;padding:8px 11px;border:1px solid var(--line);border-radius:5px;font-size:13.5px;font-family:inherit}}
.chip{{border:1px solid var(--line);background:var(--bg);border-radius:999px;padding:5px 12px;font-size:12.5px;cursor:pointer;font-family:inherit;color:var(--soft)}}
.chip.on{{background:var(--ink);color:#fff;border-color:var(--ink)}}
select{{padding:7px 9px;border:1px solid var(--line);border-radius:5px;font-size:13px;font-family:inherit;background:var(--bg)}}
.tblwrap{{max-height:640px;overflow:auto;border:1px solid var(--line);border-radius:6px;margin:10px 0}}
.tblwrap table{{margin:0;font-size:12.5px}}
.tblwrap thead th{{cursor:pointer;user-select:none}}
.tblwrap td{{border-bottom:1px solid #F0F3F3}}
.tt{{font-weight:600}} .te{{color:var(--muted);font-size:11.5px}}
.tc{{color:var(--soft);font-size:12px;line-height:1.45}}
.aiy{{color:var(--cr2);font-weight:700}} .ain{{color:var(--muted)}}
footer{{border-top:1px solid var(--line);margin-top:40px;padding:18px 0 40px;font-size:12px;color:var(--muted)}}
code{{background:#F0F3F3;padding:1px 5px;border-radius:4px;font-size:12px}}
ul.tight{{margin:8px 0 0;padding-left:20px}} ul.tight li{{margin:5px 0;font-size:14px;color:var(--soft)}}
.note{{font-size:12.5px;color:var(--muted);font-style:italic}}
</style></head><body>

<header class="site"><div class="wrap">
<p class="eyebrow">SPAR F26 · Indonesia lane · S5 hiring signal · preliminary scrape test</p>
<h1>Individual job postings, not just aggregates — Karirhub, last 12 months, finance &amp; BPO</h1>
<p class="sub">First successful pass on the team's row format (timestamp · location · content · AI-skill flag · public/private).
{n_all} postings recovered for the window 20 Oct 2025 – 20 Oct 2026, of which {n_fin} fall in the finance/BPO scope.
Every row is traceable to a public URL. This is a <b>sample</b>, not a census.</p>
<div class="accent-rule"></div>
</div></header>

<div class="banner"><div class="wrap">
<b>Headline:</b> the block that stopped the Hermes attempt was the Algolia search API — we routed around it by harvesting detail-page URLs and reading server-rendered posting pages. Algolia is still unreachable here; Kalibrr and bank-portal APIs still refuse us.
</div></div>

<main class="wrap">

<section>
<h2>The result</h2>
<div class="kpis">
  <div class="kpi acc"><div class="v">{n_all}</div><div class="l">postings recovered</div></div>
  <div class="kpi acc"><div class="v">{n_fin}</div><div class="l">finance / BPO scope</div></div>
  <div class="kpi"><div class="v">{n_live} <span style="font-size:15px;color:var(--muted)">live</span></div><div class="l">+ {n_arch} from Web Archive</div></div>
  <div class="kpi"><div class="v">{uniq_emp}</div><div class="l">distinct employers</div></div>
  <div class="kpi"><div class="v">{uniq_prov}</div><div class="l">provinces represented</div></div>
  <div class="kpi tl"><div class="v">{ai_n}<span style="font-size:15px;color:var(--muted)"> / {ai_of}</span></div><div class="l">AI-skill flagged</div></div>
</div>

<div class="verdict"><p><b>What this proves.</b> A timestamped, location-tagged, content-bearing panel of Indonesian finance-sector vacancies is obtainable from public data
without an access request — but only the last ~3 months are dense. Reaching a genuine 12-month series needs the archive arm plus repeated collection from now on.
The AI-skill question is answerable in principle ({ai_n} explicit hits, {data_n} data-skill hits, {S["ai"]["tier"].get("digital_basic",0)} "digital-basic" postings), but the base rate is low enough that keyword flags alone will not carry Dani's and Akbar's classification — that needs the deferred LLM/human pass on the stored content.</p></div>
</section>

<section>
<h2>What worked, what refused us</h2>
<p class="lede">Six routes were tried in this session. Only two produced postings. The refusals are recorded as evidence, not worked around.</p>
<table><thead><tr><th style="width:34%">Route</th><th style="width:12%">Status</th><th>Evidence / why</th></tr></thead>
<tbody>{method_rows()}</tbody></table>
<p class="note">Blocked ≠ absent: JobStreet, Indeed, LinkedIn, Kalibrr and the banks all hold finance postings. They are simply gated, and the gate is the finding for the public/private split.</p>
</section>

<section>
<h2>Coverage — read this before trusting any trend</h2>
<p class="lede">Postings per month in the window. Red = live portal, teal = archived capture. The shape is a collection artefact, not a hiring trend.</p>
<div class="card">{bars_month()}
<p class="legend"><i style="background:var(--cr)"></i>live portal &nbsp;<i style="background:var(--teal)"></i>Web Archive</p>
<p class="note">187 of the {n_fin} in-scope rows were posted in Oct 2026 because open listings are the ones still online. The archive arm covers Oct–Dec 2025 and then thins out. A real monthly series needs the same crawl repeated every month.</p></div>

<div class="grid2">
  <div class="card tl"><h3 style="margin-top:0">Sector split ({n_fin})</h3>{sector_bars}
  <p class="note">BPO is well represented (118) — relevant to Dani's question about AI skills in BPO roles.</p></div>
  <div class="card tl"><h3 style="margin-top:0">Top provinces</h3>{prov_bars}
  <p class="note">"Indonesia" = nationwide posting with no single province; kept, not dropped.</p></div>
</div>
</section>

<section>
<h2>AI-skill signal — the team's question, first cut</h2>
<p class="lede">Two independent flags per posting: <b>AI-skill</b> (text names AI/ML/automation/GenAI/RPA) and <b>data-skill</b> (data analysis, SQL, Python, BI). "Digital-basic" counts postings whose text shows ordinary digital literacy only (Excel, Office, "komputer").</p>
<table><thead><tr><th>Sector</th><th class="n">postings</th><th class="n">AI-skill flag</th><th class="n">data-skill flag</th><th class="n">digital-basic</th><th class="n">AI rate</th></tr></thead>
<tbody>{AI_ROWS}</tbody></table>
<div class="card acc"><h3 style="margin-top:0">How the flag was computed — and the bug we caught</h3>
<p style="margin:0 0 8px;font-size:14px;color:var(--soft)">The first pass used a loose substring match (any "ai", "genai", "otomasi"). It flagged <b>5</b> postings as AI-required. Spot-checking them showed most were artefacts:</p>
<ul class="tight">
<li><code>komputer</code> — computer literacy in a Teller BRILink ad, counted as AI.</li>
<li><code>AIA</code> — the insurer's name, matched by the letters "ai".</li>
<li><code>mengenai</code> — the ordinary Indonesian word "regarding"; it contains <code>g-e-n-a-i</code>.</li>
</ul>
<p style="margin:8px 0 0;font-size:14px;color:var(--soft)">Re-run with word-boundary rules on a fixed term list, the honest count is <b>{ai_n} of {ai_of}</b> — one posting, titled "Finance Automation", which is a genuine but narrow hit (the role automates finance workflows; it does not ask for ML skills). <b>Lesson for Akbar's categorisation plan:</b> keyword flags need word boundaries plus a manual spot-check, and the deferred LLM pass is the right call — a naive keyword count would have overstated AI demand by 5×.</p></div>
<p class="note">Interpretation: in this sample AI requirements are near-absent from advertised BPO and banking postings. That is a finding about <i>advertised entry-level demand</i> — Indonesian bank/BPO ads for frontline and collections roles rarely list tooling. It does not show that AI skills are not used on the job. Widen the sample before drawing an S5 conclusion.</p>
</section>

<section>
<h2>The detailed data — {n_all} rows in the requested format</h2>
<p class="lede">Sortable and filterable. <code>AI-skill required?</code> is the keyword flag; <code>domain</code> is PUBLIC for every row (source URLs included).
Download: <a href="../data/id-postings/karirhub-id-postings-sample.csv">karirhub-id-postings-sample.csv</a>.</p>
<div class="controls">
  <button class="chip on" data-f="all">All ({n_all})</button>
  <button class="chip" data-f="fin">Finance/BPO ({n_fin})</button>
  <button class="chip" data-f="live">Live portal ({n_live})</button>
  <button class="chip" data-f="arch">Archive ({n_arch})</button>
  <select id="fsector"><option value="">all sectors</option><option>Banking &amp; Financial Services</option><option>Business Process Outsourcing (BPO)</option><option>Insurance</option></select>
  <select id="fai"><option value="">AI flag: any</option><option value="Yes">AI-skill: yes</option><option value="No">AI-skill: no</option></select>
  <input type="search" id="q" placeholder="search title, employer, content, skills, province…">
</div>
<div class="tblwrap"><table id="tbl">
<thead><tr>
  <th data-k="id" style="width:74px">#</th>
  <th data-k="posted" style="width:96px">posted ↕</th>
  <th data-k="loc" style="width:150px">location</th>
  <th data-k="title">content — title / employer / snippet / skills</th>
  <th data-k="ai" style="width:86px">AI-skill?</th>
  <th data-k="dom" style="width:86px">domain</th>
</tr></thead><tbody id="tb"></tbody></table></div>
<p class="note" id="count"></p>
<p class="note"><b>How real is each row?</b> The {n_live} live rows were re-fetched at random after the build — every one returned 200 with the same title, posting date and employer. The {n_arch} archive rows all link to their Wayback capture, but their dates are derived from the relative label on the captured page ("3 days ago"), {AQ['missing_employer']} lack an employer name, {AQ['missing_skills']} lack a skills list, and their sector is keyword-matched because the archived page did not expose the industry field.</p>
<p class="note">The CSV also carries <code>ai_evidence</code> / <code>data_evidence</code> — the exact matched term behind each flag, so any row can be audited.</p>
<p class="note">Timestamps: live rows use the platform's own <code>publishedAt</code> (exact). Archive rows are derived from the relative label on the captured page ("2 days ago") and are marked as such in the CSV's <code>posted_basis</code>.</p>
</section>

<section>
<h2>Was this done ethically?</h2>
<p class="lede">Marks against the checklist the team agreed: robots/ToS, personal data, access gating, re-publication, and honesty about coverage.</p>
<table><tbody>{eth_rows()}</tbody></table>
<div class="card acc"><b>Short answer:</b> yes — this slice is public-domain, robots-permitted, rate-limited, contains no personal data, and did not bypass any access control. The two caveats are deliberate: we truncated ad text rather than mirroring the platform, and we refuse to present the sample size as a vacancy count.</div>
</section>

<section>
<h2>Public vs private — what each source is</h2>
<table><thead><tr><th style="width:32%">Source</th><th style="width:16%">Domain</th><th>Note</th></tr></thead><tbody>{domain_rows()}</tbody></table>
<p class="note">Every row shipped in the CSV is <b>PUBLIC</b>. Nothing here is licensed, purchased or access-granted.</p>
</section>

<section>
<h2>What to refine next (and what would change the answer)</h2>
<div class="grid2">
<div class="card tl"><h3 style="margin-top:0">Cheap wins</h3><ul class="tight">
<li>Re-run the live crawl monthly; the same script keeps the panel current and turns the sample into a series.</li>
<li>Widen keyword harvesting (teller, collection, underwriting, fintech, paylater) — the current 281 is one keyword sweep, not a full month.</li>
<li>Pull the Wayback CDX list for the whole year rather than the sampled snapshots, to fill Oct 2025 – Jul 2026.</li>
<li>Store full descriptions locally, classify with an LLM pass, ship only the flags — Akbar's "whichever is more convenient".</li>
</ul></div>
<div class="card acc"><h3 style="margin-top:0">What still blocks a real S5 panel</h3><ul class="tight">
<li>No historical depth on the live portal: closed postings disappear, so pre-Aug-2026 is archive-only.</li>
<li>Kalibrr / bank portals hold better-structured data but are gated — needs permission, not cleverness.</li>
<li>Duplicate detection across employer aliases (PT X vs X) is unsolved; the 32 Kasih Anugrah rows are one employer, many city-level postings.</li>
<li>Postings ≠ hires. For a hiring-rate signal we need a second data source (employment statistics, or job-board fill indicators).</li>
</ul></div>
</div>
</section>

<footer>
Generated {S["generated"]} · window {S["window"][0]} → {S["window"][1]} · source: karirhub.kemnaker.go.id public posting pages + web.archive.org captures ·
dataset <code>data/id-postings/karirhub-id-postings-sample.csv</code> · internal, consent-gated — do not republish outside the team without AISA sign-off.
</footer>
</main>

<script>
const ROWS = {TABLE_JSON};
let state = {{f:"all", sector:"", ai:"", q:"", sort:"posted", dir:-1}};
const $ = s => document.querySelector(s);
function match(r){{
  if(state.f==="fin" && !r.fin) return false;
  if(state.f==="live" && r.arm!=="live") return false;
  if(state.f==="arch" && r.arm!=="archive") return false;
  if(state.sector && r.sector!==state.sector) return false;
  if(state.ai && r.ai!==state.ai) return false;
  if(state.q){{
    const h=(r.title+" "+r.emp+" "+r.content+" "+r.skills+" "+r.prov+" "+r.loc+" "+r.sector).toLowerCase();
    if(!h.includes(state.q.toLowerCase())) return false;
  }}
  return true;
}}
function esc(s){{return (s||"").replace(/[&<>]/g,c=>({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c]));}}
function render(){{
  const rows = ROWS.filter(match).sort((a,b)=>{{
    let x=a[state.sort]||"", y=b[state.sort]||"";
    if(state.sort==="posted"){{x=a.posted;y=b.posted;}}
    return x<y? state.dir : x>y? -state.dir : 0;
  }});
  const shown = rows.slice(0,400);
  $("#tb").innerHTML = shown.map(r=>`<tr>
    <td class="te">${{r.id}}</td>
    <td class="te">${{r.posted}}${{r.arm==="archive"?'<br><span style="font-size:10px">~derived</span>':''}}</td>
    <td>${{esc(r.loc)}}<br><span class="te">${{esc(r.prov)}}</span></td>
    <td><span class="tt">${{esc(r.title)}}</span> <span class="te">· ${{esc(r.emp)}}</span>
        <div class="tc">${{esc(r.content)}}</div>
        <div class="te">${{esc(r.sector)}}${{r.skills?' · skills: '+esc(r.skills):''}}${{r.edu?' · min edu: '+esc(r.edu):''}}</div></td>
    <td class="c">${{r.ai==="Yes"?'<span class="aiy">Yes</span>':'<span class="ain">No</span>'}}${{r.tier&&r.tier!=="none"?'<br><span class="te">'+esc(r.tier)+'</span>':''}}</td>
    <td class="c"><span class="pill ok">PUBLIC</span></td></tr>`).join("");
  $("#count").textContent = `showing ${{shown.length}} of ${{rows.length}} matching rows (${{ROWS.length}} in dataset). Rows are a sample of advertised demand, not a vacancy count.`;
}}
document.querySelectorAll(".chip").forEach(b=>b.onclick=()=>{{
  document.querySelectorAll(".chip").forEach(x=>x.classList.remove("on"));
  b.classList.add("on"); state.f=b.dataset.f; render();
}});
$("#fsector").onchange=e=>{{state.sector=e.target.value;render();}};
$("#fai").onchange=e=>{{state.ai=e.target.value;render();}};
$("#q").oninput=e=>{{state.q=e.target.value;render();}};
document.querySelectorAll("#tbl thead th").forEach(th=>th.onclick=()=>{{
  const k=th.dataset.k; if(!k) return;
  state.dir = (state.sort===k)? -state.dir : (k==="posted"? -1: 1);
  state.sort=k; render();
}});
render();
</script>
</body></html>
"""

out = os.path.join(ROOT, "build", "spar-id-postings.html")
open(out, "w").write(HTML)
print("wrote", out, len(HTML), "bytes")
