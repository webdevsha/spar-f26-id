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
        inv_rows.append(
            "<tr>"
            f'<td class="mono">{esc(rid)}</td>'
            f"<td><strong>{esc(row.get('document'))}</strong><br><span class=\"muted\">{esc(row.get('short_name'))}</span></td>"
            f"<td>{esc(row.get('type'))}</td>"
            f"<td>{esc(row.get('owner_agency'))}</td>"
            f"<td>{esc(row.get('covers'))}</td>"
            f"<td>{esc(row.get('monitoring'))}</td>"
            f'<td class="mono">{esc(row.get("effective_date"))}</td>'
            f"<td>{esc(row.get('status'))}</td>"
            f"<td>{link_cell}</td>"
            f'<td class="mono">{esc(row.get("last_checked"))}</td>'
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
    inv_html = "".join(inv_rows) or '<tr><td colspan="11" class="muted">No rows yet — add documents to the inventory sheet.</td></tr>'
    grid_html = "".join(grid_rows) or f'<tr><td colspan="9" class="muted">No rows yet.</td></tr>'

    built = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>SPAR F26 · Indonesia — policy readiness</title>
<style>
  :root {{ --cream:#faf7f0; --moss:#4a5d3a; --moss-l:#6b7f4e; --wood:#8b6f47; --ink:#2c2c2c; --line:#e3ddcf; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--cream); color:var(--ink);
         font:15px/1.5 ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }}
  header {{ background:var(--moss); color:#f6f2e8; padding:22px 28px; }}
  header h1 {{ margin:0 0 4px; font-size:19px; letter-spacing:.2px; }}
  header p {{ margin:0; font-size:13px; opacity:.85; }}
  nav {{ background:#f2ede1; border-bottom:1px solid var(--line); padding:9px 28px; font-size:13px; }}
  nav a {{ color:var(--wood); margin-right:16px; text-decoration:none; font-weight:600; }}
  main {{ padding:22px 28px 60px; max-width:1400px; }}
  section {{ margin-bottom:38px; }}
  h2 {{ font-size:15px; text-transform:uppercase; letter-spacing:.08em; color:var(--moss); border-bottom:2px solid var(--line); padding-bottom:6px; }}
  table {{ border-collapse:collapse; width:100%; font-size:13px; background:#fffdf8; }}
  th,td {{ border:1px solid var(--line); padding:7px 9px; text-align:left; vertical-align:top; }}
  th {{ background:#f2ede1; color:var(--moss); font-weight:600; }}
  tr:nth-child(even) td {{ background:#fbf8f1; }}
  .mono {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12px; color:var(--wood); }}
  .muted {{ color:#8a8578; }}
  .pill {{ display:inline-block; min-width:38px; text-align:center; padding:1px 6px; border-radius:9px;
           font-size:11px; font-weight:600; border:1px solid var(--line); }}
  .pill.yes {{ background:#e3efd9; color:#33501f; border-color:#bcd4a8; }}
  .pill.partly {{ background:#f6ecd2; color:#6b5313; border-color:#e3d3a4; }}
  .pill.no {{ background:#f6ded9; color:#7a2f22; border-color:#e5bdb5; }}
  .answers {{ white-space:nowrap; }}
  a {{ color:var(--wood); }}
  footer {{ padding:16px 28px; border-top:1px solid var(--line); font-size:12px; color:#8a8578; }}
  .empty {{ color:#8a8578; font-style:italic; }}
</style>
</head>
<body>
<header>
  <h1>SPAR Fall 2026 · Indonesia — policy inventory &amp; readiness</h1>
  <p>From AI Exposure to Economic Shock — early-warning triggers for Southeast Asia. Read-only view.</p>
</header>
<nav>
  <a href="#inventory">Inventory</a>
  <a href="#readiness">Readiness grid</a>
  <a href="#blindspots">Blind spots</a>
</nav>
<main>
  <section id="inventory">
    <h2>Policy inventory ({len(inventory)} document{'s' if len(inventory) != 1 else ''})</h2>
    <table>
      <thead><tr>
        <th>id</th><th>document</th><th>type</th><th>owner / agency</th><th>covers</th>
        <th>monitoring</th><th>effective</th><th>status</th><th>link</th><th>last checked</th><th>readiness</th>
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
    <p class="muted" style="font-size:12px;margin-top:8px;">This grid grades <em>documents</em>, not the country. The project does not rank or score any government.</p>
  </section>
  <section id="blindspots">
    <h2>Blind spots</h2>
    {blind_html}
  </section>
</main>
<footer>
  Built {built} · source: private repo <code>spar-f26-id</code> · internal until AISA consent ·
  grades documents, not governments.
</footer>
</body>
</html>
"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print(f"wrote {OUT} ({len(inventory)} inventory rows, {len(readiness)} readiness rows)")


if __name__ == "__main__":
    main()
