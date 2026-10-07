#!/usr/bin/env python3
"""SPAR F26 Indonesia dashboard builder — CSV -> dist/index.html.

Reads data/*.csv from the repo and emits ONE self-contained light-theme HTML
file. No live API needed to render: the dashboard builds from repo files alone.
Read-only. Grades documents, never governments.
"""
import csv
import datetime
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "dist", "index.html")

QUESTIONS = [
    ("q1", "Names AI-driven job loss as a risk (and which sectors)"),
    ("q2", "Assigns an owner and a budget"),
    ("q3", "Monitors something (indicators, data, frequency)"),
    ("q4", "Says what happens if the signal fires"),
    ("q5", "Reaches entry-level, provincial, informal and women workers"),
    ("q6", "Governs AI decisions inside firms (targets, monitoring, grading, consultation)"),
]


# The three named end results. Content is deliberately EMPTY — placeholders so
# the shape of the finished deliverables is visible early.
END_RESULTS = [
    {
        "title": "Country reports",
        "note": "The project's country write-up: what is at stake, moves to start now, triggers for when signals move.",
        "items": [
            {"country": "Indonesia", "owner": "Shafira (ours)", "due": "Drafts 29 Nov · full 4 Dec", "ours": True},
            {"country": "Philippines", "owner": "BG · Danielle · Joshua", "due": "Drafts 29 Nov · full 4 Dec", "ours": False},
        ],
    },
    {
        "title": "Ecosystem & policy map",
        "note": "The six-layer ecosystem map, becoming an annex on AISA's SEA Observatory. Co-owned with BG and Rachel.",
        "items": [
            {"country": "Indonesia", "owner": "Shafira (ours)", "due": "Rows added by 22 Nov", "ours": True},
            {"country": "Philippines", "owner": "BG (Cebu)", "due": "Rows added by 22 Nov", "ours": False},
        ],
    },
    {
        "title": "Notes for officials",
        "note": "The two-page brief an official can read: what is at stake, moves to start now, triggers for when signals move.",
        "items": [
            {"country": "Indonesia", "owner": "Shafira · Akbar (ours)", "due": "By 13 Dec", "ours": True},
            {"country": "Philippines", "owner": "BG · Danielle", "due": "By 13 Dec", "ours": False},
        ],
    },
]


def load_json(name):
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def ghost_bars(widths):
    return "".join(f'<span class="ghost-bar" style="width:{w}%"></span>' for w in widths)


def render_ecosystem(cfg, ghost=False):
    """Two-panel map: Actors and Programs | Data and Reports.
    ghost=True renders the same shape as inert skeleton bars."""
    if ghost:
        cats = "".join(
            '<div class="cat"><div class="cat-name">' + ghost_bars([52]) + "</div>"
            '<div class="chips">' + ghost_bars([46, 58, 40, 52]) + "</div></div>"
            for _ in range(4)
        )
        ds = "".join("<li>" + ghost_bars([70, 30]) + "</li>" for _ in range(6))
        rp = "".join("<li>" + ghost_bars([64, 34]) + "</li>" for _ in range(6))
    else:
        cats = "".join(
            '<div class="cat"><div class="cat-name">' + esc(c["name"]) + "</div>"
            '<div class="chips">'
            + "".join(f'<span class="chip chip-{esc(c["tone"])}">{esc(a)}</span>' for a in c["actors"])
            + "</div></div>"
            for c in cfg.get("categories", [])
        )
        ds = "".join(
            '<li class="' + ("strong" if d.get("strong") else "") + '">' + esc(d["name"])
            + (f'<span class="ds-note">{esc(d["note"])}</span>' if d.get("note") else "")
            + "</li>"
            for d in cfg.get("datasets", [])
        )
        rp = "".join(
            "<li>" + esc(r["name"]) + f'<span class="rp-src">&#8592; {esc(r["source"])}</span></li>'
            for r in cfg.get("reports", [])
        )
    extra = ""
    if not ghost:
        overlaps = "".join(f"<li>{esc(o)}</li>" for o in cfg.get("overlaps", []))
        extra = f'<ul class="overlaps">{overlaps}</ul>'
    src = cfg.get("source", {})
    attrib = ""
    if not ghost and src:
        attrib = (
            f'<p class="attrib">Source: {esc(src.get("title"))}, p.{esc(str(src.get("page")))} '
            f"&mdash; {esc(src.get('author'))}. Transcribed as v0; not yet verified.</p>"
        )
    return (
        '<div class="panels">'
        f'<div class="panel"><h5>Actors and Programs</h5><div class="cats">{cats}</div>{extra}</div>'
        '<div class="panel"><h5>Data and Reports</h5><div class="two-col">'
        f'<div><div class="col-head">Datasets</div><ul class="flow">{ds}</ul></div>'
        f'<div><div class="col-head">Reports</div><ul class="flow">{rp}</ul></div>'
        f"</div></div></div>{attrib}"
    )


def ghost_paper(eyebrow, paragraphs, callout=False, narrow=False):
    body = "".join(f'<div class="para">{ghost_bars([100, 97, 92, 99, 46])}</div>' for _ in range(paragraphs))
    tail = ""
    if callout:
        tail = '<div class="callout">' + ghost_bars([30]) + f'<div class="para">{ghost_bars([96, 88])}</div></div>'
    return (
        f'<div class="paper{" narrow" if narrow else ""}">'
        f'<div class="paper-eyebrow">{esc(eyebrow)}</div>'
        f'<div class="paper-title">{ghost_bars([72])}</div>'
        f'<div class="paper-meta">{ghost_bars([38, 26])}</div>'
        '<div class="paper-rule"></div>'
        f"{body}{tail}</div>"
    )


def end_result_cards():
    eco = load_json("ecosystem-ph-v0.json")
    out = []
    for block in END_RESULTS:
        slug = block["title"].lower().replace(" & ", "-").replace(" ", "-")
        cards = []
        for item in block["items"]:
            cls = "card ours" if item["ours"] else "card"
            tag = '<span class="tag tag-ours">our lane</span>' if item["ours"] else '<span class="tag">partner</span>'
            if block["title"] == "Ecosystem & policy map":
                status = (
                    '<span class="status-dot dot-ghost"></span>Ghosted — shape only, not filled yet.'
                    if item["ours"]
                    else '<span class="status-dot dot-real"></span>v0 loaded — from the team\u2019s own page 5.'
                )
            else:
                status = '<span class="placeholder">Placeholder — no content yet.</span>'
            cards.append(
                f'<article class="{cls}">'
                f'<div class="card-head"><h4>{esc(item["country"])}</h4>{tag}</div>'
                f'<p class="card-owner">{esc(item["owner"])}</p>'
                f'<p class="card-due">{esc(item["due"])}</p>'
                f'<p class="card-body">{status}</p>'
                f'<a class="card-cta" href="#mock-{slug}">View demo visual &#8594;</a>'
                "</article>"
            )
        if block["title"] == "Ecosystem & policy map":
            stage = (
                '<div class="panel-group"><div class="panel-group-head">'
                '<span class="flag flag-real">Philippines</span> v0 &mdash; transcribed from the team\u2019s page 5</div>'
                + render_ecosystem(eco, ghost=False)
                + '</div><div class="panel-group"><div class="panel-group-head">'
                '<span class="flag flag-ghost">Indonesia</span> ghosted &mdash; shape only, awaiting our rows</div>'
                + render_ecosystem(eco, ghost=True)
                + "</div>"
            )
        elif block["title"] == "Notes for officials":
            stage = (
                '<div class="mock-row">'
                + ghost_paper("Officials\u2019 note \u2014 Indonesia", 4, callout=True, narrow=True)
                + ghost_paper("Officials\u2019 note \u2014 Philippines", 4, callout=True, narrow=True)
                + "</div>"
            )
        else:
            stage = (
                '<div class="mock-row">'
                + ghost_paper("Country report \u2014 Indonesia", 3)
                + ghost_paper("Country report \u2014 Philippines", 3)
                + "</div>"
            )
        out.append(
            f'<div class="result-block" id="result-{slug}">'
            f'<h3 class="result-title">{esc(block["title"])}</h3>'
            f'<p class="result-note">{esc(block["note"])}</p>'
            f'<div class="cards">{"".join(cards)}</div>'
            f'<div class="mock" id="mock-{slug}">'
            f'<p class="mock-label">Demo visual &mdash; the shape of the finished {esc(block["title"].lower())}. '
            f"Ghosted bars are placeholders, not content.</p>"
            f'<div class="mock-stage">{stage}</div></div>'
            "</div>"
        )
    return "".join(out)


def read_text(rel_path):
    path = os.path.join(ROOT, rel_path)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def render_model():
    """The interactive signal -> trigger -> shock model, kept in its own files so
    the JS is not embedded in a Python f-string."""
    data = load_json("model-id-demo.json")
    markup = read_text("build/model_section.html")
    if not data or not markup:
        return ""
    return (
        "<script>window.SPAR_MODEL = "
        + json.dumps(data, ensure_ascii=False)
        + ";</script>\n"
        + markup
    )


def render_recent_changes(limit=8):
    """Render the newest entries of data/SYNC-LOG.md."""
    path = os.path.join(DATA, "SYNC-LOG.md")
    if not os.path.exists(path):
        return '<p class="muted">No sync history yet.</p>'
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    entries = []
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            if current:
                entries.append(current)
            current = {"head": line[3:].strip(), "meta": "", "items": []}
        elif current is not None:
            stripped = line.strip()
            if stripped.startswith("_by:"):
                current["meta"] = stripped.strip("_")
            elif stripped.startswith("- "):
                current["items"].append(stripped[2:])
    if current:
        entries.append(current)

    if not entries:
        return '<p class="muted">No sync history yet.</p>'

    out = []
    for e in entries[:limit]:
        items = "".join(f"<li>{inline_code(esc(i))}</li>" for i in e["items"]) or '<li class="muted">no data changed</li>'
        meta = f'<span class="chg-meta">{esc(e["meta"])}</span>' if e["meta"] else ""
        out.append(
            '<div class="chg">'
            f'<div class="chg-head"><span class="chg-when">{esc(e["head"])}</span>{meta}</div>'
            f'<ul class="chg-list">{items}</ul>'
            "</div>"
        )
    return "".join(out)


def inline_code(s):
    """Wrap `backticked` spans in <code> after escaping."""
    parts = s.split("`")
    out = []
    for i, part in enumerate(parts):
        out.append(f"<code>{part}</code>" if i % 2 else part)
    return "".join(out)


def read_csv(name):
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as fh:
        return [row for row in csv.DictReader(fh) if any((v or "").strip() for v in row.values())]


def esc(v):
    return html.escape((v or "").strip())


def main():
    inventory = read_csv("id-policy-inventory.csv")
    readiness = read_csv("id-readiness.csv")
    readiness_by_id = {(r.get("id") or "").strip(): r for r in readiness}

    # Blind spots: a document scoring "no" on q3 (no monitoring) or q4 (no action rule).
    blind_spots = []
    for row in readiness:
        misses = [label for key, label in QUESTIONS if (row.get(key) or "").strip().lower() == "no"]
        if (row.get("q3") or "").strip().lower() == "no" or (row.get("q4") or "").strip().lower() == "no":
            blind_spots.append({"doc": (row.get("document") or row.get("id") or "").strip(), "misses": misses})

    demo_rows = [r for r in inventory if (r.get("verified_by") or "").strip().upper() == "DEMO"]

    inv_rows = []
    for row in inventory:
        rid = (row.get("id") or "").strip()
        rd = readiness_by_id.get(rid, {})
        answers = "".join(
            f'<span class="pill {esc((rd.get(k) or "").strip().lower())}">{esc(rd.get(k) or "–")}</span>'
            for k, _ in QUESTIONS
        )
        link = (row.get("link") or "").strip()
        link_cell = '<a href="' + esc(link) + '">link</a>' if link else ""
        verified = (row.get("verified_by") or "").strip()
        badge = f' <span class="pill demo">{esc(verified)}</span>' if verified.upper() == "DEMO" else ""
        inv_rows.append(
            "<tr>"
            f'<td class="mono">{esc(rid)}</td>'
            f"<td><strong>{esc(row.get('document'))}</strong>{badge}<br><span class=\"muted\">{esc(row.get('short_name'))}</span></td>"
            f"<td>{esc(row.get('type'))}</td>"
            f"<td>{esc(row.get('owner_agency'))}</td>"
            f"<td>{esc(row.get('covers'))}</td>"
            f"<td>{esc(row.get('monitoring'))}</td>"
            f'<td class="mono">{esc(row.get("effective_date"))}</td>'
            f"<td>{esc(row.get('status'))}</td>"
            f"<td>{link_cell}</td>"
            f'<td class="mono">{esc(row.get("last_checked"))}</td>'
            f'<td class="mono">{esc(verified)}</td>'
            f'<td class="answers">{answers}</td>'
            "</tr>"
        )

    grid_head = "".join(f"<th title=\"{esc(label)}\">Q{i+1}</th>" for i, (_, label) in enumerate(QUESTIONS))
    grid_rows = []
    for row in readiness:
        cells = "".join(
            f'<td><span class="pill {esc((row.get(k) or "").strip().lower())}">{esc(row.get(k) or "–")}</span></td>'
            for k, _ in QUESTIONS
        )
        grid_rows.append(f'<tr><td class="mono">{esc(row.get("id"))}</td><td>{esc(row.get("document"))}</td>{cells}<td>{esc(row.get("score"))}</td></tr>')

    blind_html = (
        "<ul>" + "".join(f'<li><strong>{esc(b["doc"])}</strong> — missing: {esc("; ".join(b["misses"]) or "—")}</li>' for b in blind_spots) + "</ul>"
        if blind_spots
        else '<p class="muted">No rows yet.</p>'
    )
    inv_html = "".join(inv_rows) or '<tr><td colspan="12" class="muted">No rows yet — add documents to the inventory sheet.</td></tr>'
    grid_html = "".join(grid_rows) or f'<tr><td colspan="9" class="muted">No rows yet.</td></tr>'
    results_html = end_result_cards()
    changes_html = render_recent_changes()
    model_html = render_model()

    banner_html = (
        f'<div class="banner"><div class="wrap"><strong>Demo data.</strong> {len(demo_rows)} of {len(inventory)} '
        f"inventory rows are placeholders (verified_by = DEMO) — illustrative only, replace with verified v0 rows. "
        f"The end-result cards are empty placeholders.</div></div>"
        if demo_rows
        else ""
    )

    built = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>SPAR F26 · Indonesia — policy readiness</title>
<style>
  :root {{ --ink:#212A2A; --ink-soft:#3A4848; --muted:#8B9999; --line:#E4E8E8;
           --bg:#FFFFFF; --bg-alt:#F7F9F9;
           --accent:#C41E3A; --accent-deep:#9E152C; --accent-deeper:#7A1022; --accent-tint:#FBEDEF; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
         font:16px/1.6 -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif; }}
  a {{ color:var(--accent-deep); text-decoration:none; border-bottom:1px solid var(--accent-tint); }}
  a:hover {{ border-bottom-color:var(--accent); }}
  .wrap {{ max-width:1180px; margin:0 auto; padding:0 32px; }}
  header.site {{ border-bottom:1px solid var(--line); }}
  header.site .wrap {{ padding-top:32px; padding-bottom:26px; }}
  .eyebrow {{ font-size:12px; letter-spacing:.13em; text-transform:uppercase; color:var(--accent);
              font-weight:600; margin:0 0 10px; }}
  header.site h1 {{ margin:0; font-size:31px; line-height:1.22; font-weight:600; letter-spacing:-.015em; }}
  header.site p.sub {{ margin:10px 0 0; color:var(--ink-soft); font-size:15px; max-width:64ch; }}
  .accent-rule {{ height:3px; background:var(--accent); width:56px; margin:18px 0 0; }}
  nav.site {{ border-bottom:1px solid var(--line); background:var(--bg-alt); }}
  nav.site a {{ display:inline-block; padding:12px 0; margin-right:26px; font-size:13.5px; font-weight:500;
                color:var(--ink-soft); border-bottom:2px solid transparent; }}
  nav.site a:hover {{ color:var(--accent); border-bottom-color:var(--accent); }}
  .banner {{ background:var(--accent-tint); border-bottom:1px solid var(--line);
             color:var(--accent-deeper); font-size:13.5px; }}
  .banner .wrap {{ padding-top:11px; padding-bottom:11px; }}
  main {{ padding:4px 0 72px; }}
  section {{ padding:40px 0 8px; border-top:1px solid var(--line); }}
  section:first-of-type {{ border-top:0; }}
  h2 {{ font-size:12px; letter-spacing:.13em; text-transform:uppercase; color:var(--muted);
        font-weight:600; margin:0 0 8px; }}
  .lede {{ margin:0 0 24px; color:var(--ink-soft); font-size:14.5px; max-width:78ch; }}
  .result-block {{ margin-bottom:34px; }}
  .result-title {{ margin:0 0 4px; font-size:19px; font-weight:600; letter-spacing:-.01em; }}
  .result-note {{ margin:0 0 16px; color:var(--muted); font-size:13.5px; max-width:80ch; }}
  .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }}
  .card {{ border:1px solid var(--line); border-radius:6px; padding:18px 20px; background:var(--bg); }}
  .card.ours {{ border-left:3px solid var(--accent); }}
  .card-head {{ display:flex; align-items:center; justify-content:space-between; gap:12px; }}
  .card-head h4 {{ margin:0; font-size:16px; font-weight:600; }}
  .tag {{ font-size:10.5px; letter-spacing:.09em; text-transform:uppercase; font-weight:600;
          color:var(--muted); border:1px solid var(--line); border-radius:3px; padding:2px 7px; white-space:nowrap; }}
  .tag-ours {{ color:var(--accent-deep); border-color:var(--accent-tint); background:var(--accent-tint); }}
  .card-owner {{ margin:12px 0 2px; font-size:13.5px; color:var(--ink-soft); }}
  .card-due {{ margin:0; font-size:12.5px; color:var(--muted); }}
  .card-body {{ margin:14px 0 0; padding-top:12px; border-top:1px dashed var(--line); font-size:13.5px; }}
  .placeholder {{ color:var(--muted); font-style:italic; }}
  table {{ border-collapse:collapse; width:100%; font-size:13px; }}
  th,td {{ padding:9px 11px; text-align:left; vertical-align:top; border-bottom:1px solid var(--line); }}
  thead th {{ border-bottom:1px solid var(--ink-soft); font-size:11.5px; letter-spacing:.07em;
              text-transform:uppercase; color:var(--ink-soft); font-weight:600; white-space:nowrap; }}
  tbody tr:hover td {{ background:var(--bg-alt); }}
  .mono {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12px; color:var(--muted); }}
  .muted {{ color:var(--muted); }}
  .pill {{ display:inline-block; min-width:40px; text-align:center; padding:1px 6px; border-radius:3px;
           font-size:11px; font-weight:600; border:1px solid var(--line); }}
  .pill.yes {{ background:#EAF3EC; color:#2C5A38; border-color:#CBE0D1; }}
  .pill.partly {{ background:#FBF3E2; color:#7A5A18; border-color:#EADFC2; }}
  .pill.no {{ background:var(--accent-tint); color:var(--accent-deeper); border-color:#F0D3D9; }}
  .pill.demo {{ background:#F2F4F4; color:var(--muted); border-color:var(--line); font-size:10px;
                letter-spacing:.05em; }}
  .answers {{ white-space:nowrap; }}

  /* --- demo visuals / ghost mode --- */
  .card-cta {{ display:inline-block; margin-top:14px; font-size:12.5px; font-weight:600; }}
  .status-dot {{ display:inline-block; width:7px; height:7px; border-radius:50%; margin-right:7px;
                 vertical-align:middle; }}
  .dot-real {{ background:var(--accent); }}
  .dot-ghost {{ background:var(--line); border:1px solid var(--muted); }}
  .mock {{ margin-top:18px; border:1px solid var(--line); border-radius:6px; background:var(--bg-alt);
           padding:16px 18px 18px; }}
  .mock-label {{ margin:0 0 14px; font-size:12.5px; color:var(--muted); }}
  .mock-stage {{ display:flex; flex-direction:column; gap:18px; }}
  .mock-row {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:16px; }}
  .panel-group {{ background:var(--bg); border:1px solid var(--line); border-radius:5px; padding:14px 16px; }}
  .panel-group-head {{ font-size:12px; color:var(--muted); margin-bottom:12px; }}
  .flag {{ display:inline-block; font-size:10.5px; letter-spacing:.08em; text-transform:uppercase;
           font-weight:600; border-radius:3px; padding:2px 7px; margin-right:8px; }}
  .flag-real {{ background:var(--accent-tint); color:var(--accent-deep); }}
  .flag-ghost {{ background:#F2F4F4; color:var(--muted); }}
  .panels {{ display:grid; grid-template-columns:1fr 1fr; gap:20px; }}
  @media (max-width:900px) {{ .panels {{ grid-template-columns:1fr; }} }}
  .panel h5 {{ margin:0 0 12px; font-size:11px; letter-spacing:.1em; text-transform:uppercase;
               color:var(--ink-soft); font-weight:600; padding-bottom:6px; border-bottom:1px solid var(--line); }}
  .cat {{ margin-bottom:10px; }}
  .cat-name {{ font-size:11.5px; font-weight:600; color:var(--ink-soft); margin-bottom:5px; }}
  .chips {{ display:flex; flex-wrap:wrap; gap:5px; }}
  .chip {{ font-size:11.5px; padding:2px 8px; border-radius:3px; border:1px solid var(--line);
           background:var(--bg-alt); color:var(--ink-soft); }}
  .chip-gov {{ background:#F2F4F4; }}
  .chip-industry {{ background:#FBF3E2; border-color:#EADFC2; }}
  .chip-multi {{ background:#EEF4F7; border-color:#D3E2EA; }}
  .chip-strategy {{ background:var(--accent-tint); border-color:#F0D3D9; color:var(--accent-deep); }}
  .overlaps {{ margin:10px 0 0; padding-left:18px; }}
  .overlaps li {{ font-size:12px; color:var(--muted); margin-bottom:4px; }}
  .two-col {{ display:grid; grid-template-columns:1fr 1fr; gap:16px; }}
  .col-head {{ font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted);
               font-weight:600; margin-bottom:7px; }}
  .flow {{ list-style:none; margin:0; padding:0; }}
  .flow li {{ font-size:12.5px; padding:6px 9px; border:1px solid var(--line); border-radius:3px;
              margin-bottom:6px; background:var(--bg-alt); }}
  .flow li.strong {{ border-left:3px solid var(--accent); }}
  .ds-note {{ display:block; font-size:10.5px; color:var(--accent-deep); margin-top:2px; }}
  .rp-src {{ display:block; font-size:10.5px; color:var(--muted); margin-top:2px; }}
  .attrib {{ margin:12px 0 0; font-size:11.5px; color:var(--muted); font-style:italic; }}
  .ghost-bar {{ display:inline-block; height:9px; border-radius:3px; background:#E9EDED;
                margin:0 3px 3px 0; vertical-align:middle; }}
  .paper {{ background:var(--bg); border:1px solid var(--line); border-radius:4px; padding:20px 22px; }}
  .paper.narrow {{ max-width:100%; }}
  .paper-eyebrow {{ font-size:10.5px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted);
                    font-weight:600; }}
  .paper-title {{ margin:10px 0 8px; }}
  .paper-meta {{ margin-bottom:12px; }}
  .paper-rule {{ height:2px; background:var(--accent-tint); width:40px; margin-bottom:16px; }}
  .para {{ margin-bottom:9px; line-height:1; }}
  .callout {{ border-left:3px solid var(--accent-tint); background:var(--bg-alt); padding:11px 13px;
              margin-top:12px; }}
  .chg {{ border-bottom:1px solid var(--line); padding:12px 0; }}
  .chg:last-child {{ border-bottom:0; }}
  .chg-head {{ display:flex; align-items:baseline; justify-content:space-between; gap:14px; }}
  .chg-when {{ font-size:13.5px; font-weight:600; }}
  .chg-meta {{ font-size:12px; color:var(--muted); }}
  .chg-list {{ margin:7px 0 0; padding-left:18px; }}
  .chg-list li {{ font-size:13px; margin-bottom:3px; }}
  .chg-list code {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12px;
                    background:var(--bg-alt); border:1px solid var(--line); border-radius:3px;
                    padding:0 4px; }}
  ul {{ margin:0; padding-left:20px; }}
  li {{ margin-bottom:7px; font-size:14px; }}
  footer {{ border-top:1px solid var(--line); background:var(--bg-alt); }}
  footer .wrap {{ padding-top:18px; padding-bottom:22px; font-size:12.5px; color:var(--muted); }}
</style>
</head>
<body>
<header class="site">
  <div class="wrap">
    <p class="eyebrow">SPAR Fall 2026 · Indonesia</p>
    <h1>Policy inventory &amp; readiness</h1>
    <p class="sub">From AI Exposure to Economic Shock — early-warning triggers for Southeast Asia. Read-only view.</p>
    <div class="accent-rule"></div>
  </div>
</header>
<nav class="site"><div class="wrap">
  <a href="#results">End results</a>
  <a href="#model">Model</a>
  <a href="#inventory">Inventory</a>
  <a href="#readiness">Readiness grid</a>
  <a href="#changes">Recent changes</a>
  <a href="#blindspots">Blind spots</a>
</div></nav>
{banner_html}
<main><div class="wrap">
  <section id="results">
    <h2>End results</h2>
    <p class="lede">The three named deliverables, both countries. Placeholders for now — the shape is here so we can
    see where each one lands before there is content to put in it.</p>
    {results_html}
  </section>
  {model_html}
  <section id="inventory">
    <h2>Policy inventory ({len(inventory)} document{'s' if len(inventory) != 1 else ''})</h2>
    <table>
      <thead><tr>
        <th>id</th><th>document</th><th>type</th><th>owner / agency</th><th>covers</th>
        <th>monitoring</th><th>effective</th><th>status</th><th>link</th><th>last checked</th><th>verified</th><th>readiness</th>
      </tr></thead>
      <tbody>{inv_html}</tbody>
    </table>
  </section>
  <section id="readiness">
    <h2>Readiness grid — six questions</h2>
    <table>
      <thead><tr><th>id</th><th>document</th>{grid_head}<th>score</th></tr></thead>
      <tbody>{grid_html}</tbody>
    </table>
    <p class="muted" style="font-size:12.5px;margin-top:12px;">This grid grades <em>documents</em>, not the country.
    The project does not rank or score any government.</p>
  </section>
  <section id="changes">
    <h2>Recent changes</h2>
    <p class="lede">What the Google Sheet has sent us, newest first — written automatically by the sync.
    When the real-time trigger is wired, the editor\u2019s name appears with each entry.</p>
    {changes_html}
  </section>
  <section id="blindspots">
    <h2>Blind spots</h2>
    {blind_html}
  </section>
</div></main>
<footer><div class="wrap">
  Built {built} · source: private repo <code>spar-f26-id</code> · internal until AISA consent ·
  grades documents, not governments.
</div></footer>
</body>
</html>
"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print(f"wrote {OUT} ({len(inventory)} inventory rows, {len(readiness)} readiness rows)")


if __name__ == "__main__":
    main()
