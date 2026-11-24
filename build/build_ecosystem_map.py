#!/usr/bin/env python3
"""SPAR F26 Indonesia - three-map ecosystem / policy / bridge builder.

Reads data/ecosystem-id-map.json and emits, from one source:
  build/spar-id-ecosystem-map.html  self-contained light-theme page, 3 maps + tables
  build/spar-id-eco.svg             map 1  ecosystem (relationship)
  build/spar-id-policy.svg          map 2  policy
  build/spar-id-bridge.svg          map 3  ecosystem -> policy bridge
  build/spar-id-ecosystem-map.svg   map 1 alias (kept for the existing deck link)

Indonesia lane only. Read-only. Grades documents, never governments.
CONSENT GATE: not wired into the deploy path. build/*.html is PUBLIC on Cloudflare
Pages; publish only after AISA consent.
"""
import html
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
BUILD = os.path.join(ROOT, "build")
THEME = os.path.join(BUILD, "eco_theme.css")

INK, INK_SOFT, MUTED = "#212A2A", "#3A4848", "#8B9999"
LINE, BG, BG_ALT = "#E4E8E8", "#FFFFFF", "#F7F9F9"
ACCENT, ACCENT_DEEP, ACCENT_TINT = "#C41E3A", "#9E152C", "#FBEDEF"
ELL = "\u2026"  # ellipsis, marks text deliberately clipped on the map (full text is in the HTML)
CUR_VIEW = [""]  # view key currently being drawn, so nodes can carry it for the click handler

# Four line types, per the source note: solid existing / dashed proposed /
# dotted hypothesised transmission / red dashed named gap.
EDGE_STYLE = {
    "existing":     {"stroke": "#3E6B7A", "dash": "",        "label": "existing relationship (source-backed)"},
    "proposed":     {"stroke": "#8A6D1F", "dash": "7 5",     "label": "proposed data / coordination link"},
    "transmission": {"stroke": "#6B4E8A", "dash": "2 4",     "label": "hypothesised economic transmission"},
    "gap":          {"stroke": ACCENT,    "dash": "7 5",     "label": "named gap - the series does not exist"},
    "placeholder":  {"stroke": MUTED,     "dash": "2 3",     "label": "blocked / awaiting rows"},
}
BAND_TINT = [("#EEF4F7", "#D3E2EA", "#2E4A57"), ("#FBF3E2", "#EADFC2", "#7A5A18"),
             ("#F1EEF7", "#DED6EA", "#4C3A6B"), ("#EAF3EC", "#CBE0D1", "#2C5A38"),
             ("#F7F1EE", "#E8DAD3", "#6E4A38"), ("#F2F4F4", LINE, INK_SOFT)]
STATUS = {"real": ("#EAF3EC", "#CBE0D1", "#2C5A38", "populated"),
          "new": ("#EAF3EC", "#CBE0D1", "#2C5A38", "new"),
          "draft": ("#FBF3E2", "#EADFC2", "#7A5A18", "draft"),
          "gap": (ACCENT_TINT, "#F0D3D9", ACCENT_DEEP, "gap"),
          "placeholder": ("#F2F4F4", LINE, MUTED, "awaiting rows")}


def esc(v):
    return html.escape(str(v if v is not None else ""))


def load():
    with open(os.path.join(DATA, "ecosystem-id-map.json"), encoding="utf-8") as fh:
        return json.load(fh)


def wrap(text, width):
    out, cur = [], ""
    for w in str(text).split():
        cand = (cur + " " + w).strip()
        if len(cand) <= width or not cur:
            cur = cand
        else:
            out.append(cur); cur = w
    if cur:
        out.append(cur)
    return out


def text_lines(x, y, lines, size, fill, weight="normal", gap=None, anchor="start"):
    gap = gap or size * 1.3
    return "".join('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" font-weight="%s" '
                   'text-anchor="%s">%s</text>' % (x, y + i * gap, size, fill, weight, anchor, esc(l))
                   for i, l in enumerate(lines))

W = 1320
NODE_W, NODE_H, NODE_GAP, ROW_PITCH = 252, 102, 12, 114
NODE_X0, SLOT, PER_ROW = 208, 264, 4
BAND_LABEL_X, TOP, BAND_PAD = 24, 96, 26


def layout(view):
    """Row-major band layout. Returns (geo, band_geo, height)."""
    geo, band_geo, y = {}, {}, TOP
    for b in view["bands"]:
        ns = [n for n in view["nodes"] if n["band"] == b["id"]]
        rows = max(1, math.ceil(len(ns) / PER_ROW))
        for i, n in enumerate(ns):
            r, c = divmod(i, PER_ROW)
            geo[n["id"]] = (NODE_X0 + c * SLOT, y + r * ROW_PITCH, NODE_W, NODE_H)
        bh = rows * ROW_PITCH - NODE_GAP + BAND_PAD
        band_geo[b["id"]] = (y, bh, len(ns))
        y += bh
    return geo, band_geo, y + 44


def bez_mid(p0, p1, p2, p3):
    return ((p0[0] + 3 * p1[0] + 3 * p2[0] + p3[0]) / 8.0,
            (p0[1] + 3 * p1[1] + 3 * p2[1] + p3[1]) / 8.0)


def draw_node(x, y, n, band):
    _, stroke, txt = band
    st = STATUS.get(n.get("status", "real"), STATUS["real"])
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="6" fill="%s" stroke="%s"/>'
         % (x, y, NODE_W, NODE_H, BG, LINE),
         '<rect x="%s" y="%s" width="3.5" height="%s" rx="1.5" fill="%s"/>' % (x, y, NODE_H, txt)]
    lab_all = wrap(n["label"], 30)
    lab = lab_all[:2]
    if len(lab_all) > 2:
        lab[-1] = lab[-1][:28] + ELL
    o.append(text_lines(x + 14, y + 24, lab, 13.2, INK, "600", gap=16.5))
    yy = y + 24 + len(lab) * 16.5 + 8
    sub_lines = 1 if len(lab) == 2 else 2
    sub_all = wrap(n["sub"], 42)
    sub = sub_all[:sub_lines]
    if len(sub_all) > sub_lines:
        sub[-1] = sub[-1][:40] + ELL
    o.append(text_lines(x + 14, yy, sub, 10.2, MUTED, gap=12))
    mx = x + 14
    marks = n.get("marks") or ([n["tm"]] if n.get("tm") else [])
    for m in marks[:3]:
        mw = 6.1 * len(m) + 13
        o.append('<rect x="%.0f" y="%s" width="%.0f" height="15" rx="3" fill="%s" stroke="%s"/>'
                 % (mx, y + NODE_H - 20, mw, band[0], stroke))
        o.append(text_lines(mx + mw / 2, y + NODE_H - 9.5, [m], 9, txt, "600", 0, "middle"))
        mx += mw + 4
    return '<g class="ecnode" data-v="%s" data-id="%s">%s</g>' % (CUR_VIEW[0], n["id"], "".join(o))


def draw_edge(geo, i, e):
    style = EDGE_STYLE.get(e["kind"], EDGE_STYLE["existing"])
    (sx, sy, sw, sh), (tx, ty, tw, th) = geo[e["from"]], geo[e["to"]]
    p0 = (sx + sw, sy + sh / 2.0)
    p3 = (tx, ty + th / 2.0)
    dx = p3[0] - p0[0]
    if abs(dx) < 40:
        b, p0, p3 = 120.0, (p0[0], p0[1]), (p3[0], p3[1] + 0)
        p1 = (p0[0] + b, p0[1] + 40); p2 = (p3[0] + b, p3[1] - 40)
    else:
        b = min(130.0, max(34.0, abs(dx) * 0.42))
        p1 = (p0[0] + b, p0[1]); p2 = (p3[0] - b, p3[1])
    mid = bez_mid(p0, p1, p2, p3)
    dash = ' stroke-dasharray="%s"' % style["dash"] if style["dash"] else ""
    col = style["stroke"]
    return ('<path d="M%.0f,%.0f C%.0f,%.0f %.0f,%.0f %.0f,%.0f" fill="none" stroke="%s" '
            'stroke-width="1.5" opacity="0.62" marker-end="url(#a-%s)"%s/>'
            '<circle cx="%.0f" cy="%.0f" r="11" fill="%s" stroke="%s" stroke-width="1.3"/>%s'
            % (p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], col, e["kind"], dash,
               mid[0], mid[1], BG, col,
               text_lines(mid[0], mid[1] + 4, [str(i + 1)], 10.5, col, "600", 0, "middle")))


def build_svg(view, title, subtitle, footer):
    geo, band_geo, H = layout(view)
    used = []
    for e in view["edges"]:
        if e["kind"] not in used:
            used.append(e["kind"])
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
         'font-family="-apple-system,BlinkMacSystemFont,Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif">'
         % (W, H, W, H)]
    o.append("<defs>")
    for k in used:
        o.append('<marker id="a-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
                 'markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
                 'fill="%s" opacity="0.75"/></marker>' % (k, EDGE_STYLE[k]["stroke"]))
    o.append("</defs>")
    o.append('<rect width="%d" height="%d" fill="%s"/>' % (W, H, BG))
    o.append(text_lines(BAND_LABEL_X, 44, [title], 21, INK, "600"))
    o.append(text_lines(BAND_LABEL_X, 66, [subtitle], 12.5, MUTED))
    o.append('<rect x="%d" y="78" width="56" height="3" fill="%s"/>' % (BAND_LABEL_X, ACCENT))
    for bi, b in enumerate(view["bands"]):
        y, bh, cnt = band_geo[b["id"]]
        tint, stroke, txt = BAND_TINT[bi % len(BAND_TINT)]
        o.append('<rect x="%d" y="%s" width="%d" height="%s" rx="6" fill="%s" opacity="0.5"/>'
                 % (BAND_LABEL_X, y - 8, W - 2 * BAND_LABEL_X, bh, tint))
        o.append(text_lines(BAND_LABEL_X + 14, y + 16, [b["title"].upper()], 11.5, txt, "700"))
        o.append(text_lines(BAND_LABEL_X + 14, y + 33, wrap(b["sub"], 24)[:3], 10, MUTED, gap=12))
    for i, e in enumerate(view["edges"]):
        if e["from"] in geo and e["to"] in geo:
            o.append(draw_edge(geo, i, e))
    for bi, b in enumerate(view["bands"]):
        _, _, txt = BAND_TINT[bi % len(BAND_TINT)]
        for n in view["nodes"]:
            if n["band"] == b["id"] and n["id"] in geo:
                o.append(draw_node(geo[n["id"]][0], geo[n["id"]][1], n,
                                   (BAND_TINT[bi % len(BAND_TINT)][0], BAND_TINT[bi % len(BAND_TINT)][1], txt)))
    lx = BAND_LABEL_X
    for k in used:
        s = EDGE_STYLE[k]
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.5"%s/>'
                 % (lx, H - 24, lx + 26, H - 24, s["stroke"],
                    ' stroke-dasharray="%s"' % s["dash"] if s["dash"] else ""))
        o.append(text_lines(lx + 33, H - 20, [s["label"]], 11, MUTED))
        lx += 33 + 6.2 * len(s["label"]) + 26
    o.append(text_lines(BAND_LABEL_X, H - 6, [footer], 10.5, MUTED))
    o.append("</svg>")
    return "".join(o)


def node_card(n, bi, vid=""):
    tint, stroke, txt = BAND_TINT[bi % len(BAND_TINT)]
    st = STATUS.get(n.get("status", "real"), STATUS["real"])
    marks = n.get("marks") or ([n["tm"]] if n.get("tm") else [])
    chips = "".join('<span class="chip" style="background:%s;border-color:%s;color:%s">%s</span>'
                    % (tint, stroke, txt, esc(m)) for m in marks)
    return ('<article class="dcard nodecard clickable" data-v="%s" data-n="%s" style="border-left-color:%s">'
            '<h4 class="dlabel" style="margin:0 0 3px">%s</h4>'
            '<p class="dsub">%s</p><p class="ddetail">%s</p>'
            '<div class="chips">%s</div>'
            '<p class="dsrc">%s</p></article>'
            % (esc(vid), esc(n["id"]), txt, esc(n["label"]), esc(n["sub"]), esc(n["detail"]),
               chips, esc(n.get("ev", ""))))


def edge_table(view):
    lab = {n["id"]: n["label"] for n in view["nodes"]}
    rows = []
    for i, e in enumerate(view["edges"], 1):
        s = EDGE_STYLE.get(e["kind"], EDGE_STYLE["existing"])
        rows.append('<tr><td><span class="num" style="background:%s;color:%s;border:1px solid %s">%d</span></td>'
                    '<td class="edge-from">%s<br><span class="edge-to">%s</span></td>'
                    '<td><span class="pill" style="background:%s;color:%s">%s</span></td>'
                    '<td><strong>%s</strong><div class="edge-flow">%s</div>'
                    '<div class="edge-ev">%s</div></td></tr>'
                    % (BG, s["stroke"], s["stroke"], i,
                       esc(lab.get(e["from"], e["from"])), esc(lab.get(e["to"], e["to"])),
                       "#F2F4F4", s["stroke"], esc(e["kind"]),
                       esc(e["label"]), esc(e["note"]), esc(e.get("status", ""))))
    return ('<table class="cond"><thead><tr><th>#</th><th>from &rarr; to</th><th>type</th>'
            '<th>what the relationship is</th></tr></thead><tbody>%s</tbody></table>' % "".join(rows))


def view_section(vid, view, svg, tag_color, tag_bg):
    bands = {b["id"]: b for b in view["bands"]}
    blocks = []
    for bi, b in enumerate(view["bands"]):
        ns = [n for n in view["nodes"] if n["band"] == b["id"]]
        if not ns:
            continue
        blocks.append('<div class="rowband"><div class="rowhead"><b style="color:%s">%s</b>'
                      '<i>%s</i></div><div class="cards">%s</div></div>'
                      % (BAND_TINT[bi % len(BAND_TINT)][2], esc(b["title"]), esc(b["sub"]),
                         "".join(node_card(n, bi, vid) for n in ns)))
    return ('<section id="%s"><div class="viewhead"><h3>%s</h3>'
            '<span class="viewtag" style="background:%s;color:%s">%d nodes &middot; %d edges</span></div>'
            '<p class="lede">%s</p><div class="gapbox"><p>%s</p></div>'
            '<div class="mapbox">%s</div>%s%s</section>'
            % (vid, esc(view["title"]), tag_bg, tag_color,
               len(view["nodes"]), len(view["edges"]), esc(view["sub"]), esc(view["note"]),
               svg, "".join(blocks), edge_table(view)))


def responsibility_table(doc):
    r = doc["responsibility"]
    head = "".join("<th>%s</th>" % esc(c) for c in r["cols"])
    rows = []
    for x in r["rows"]:
        rows.append("<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>"
                    "<td class=\"edge-ev\">%s</td><td class=\"edge-flow\">%s</td></tr>"
                    % (esc(x["m"]), esc(x["owner"]), esc(x["validator"]), esc(x["decider"]),
                       esc(x["deliverer"]), esc(x["break"]), esc(x["strengthen"])))
    return '<table class="cond"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (head, "".join(rows))


def reference_blocks(doc):
    lane = doc["lane"]
    pops = "".join('<li><strong>%s</strong> &mdash; %s</li>' % (esc(p["name"]), esc(p["note"]))
                   for p in lane["populations"])
    marks = "".join('<li><strong>%s</strong> %s &mdash; %s</li>'
                    % (esc(m["code"]), esc(m["q"]), esc(m["sub"])) for m in doc["marks"])
    return ("<h4 style=\"margin:22px 0 8px;font-size:13px\">Ecosystem boundary &mdash; %s</h4><ul>%s</ul>"
            "<p class=\"lede\" style=\"margin:10px 0 0\">First case: %s</p>"
            "<h4 style=\"margin:26px 0 8px;font-size:13px\">The six measures</h4><ul>%s</ul>"
            % (esc(lane["boundary"]), pops, esc(lane["first_case"]), marks))


DRAWER_JS = """
(function(){
  var M = window.SPAR_MAP || {}, open = null;
  function byId(v,id){ var ns=(M[v]&&M[v].nodes)||[]; for(var i=0;i<ns.length;i++) if(ns[i].id===id) return ns[i]; return null; }
  function edgesFor(v,id){ return ((M[v]&&M[v].edges)||[]).filter(function(e){return e.f===id||e.t===id;}); }
  function lab(v,id){ var n=byId(v,id); return n?n.label:id; }
  function esc(s){ return String(s===undefined||s===null?"":s).replace(/[&<>"]/g,function(c){
    return {"&":"&amp;","<":"&lt;",">":"&gt;","\\"":"&quot;"}[c]; }); }
  function show(v,id){
    var n=byId(v,id); if(!n) return;
    var es=edgesFor(v,id), h="";
    h+='<p class="d-eyebrow">'+esc(n.bandTitle)+(n.status?' &middot; '+esc(n.status):'')+'</p>';
    h+='<h3 class="d-title">'+esc(n.label)+'</h3>';
    h+='<p class="d-sub">'+esc(n.sub)+'</p>';
    if(n.marks&&n.marks.length) h+='<div class="chips">'+n.marks.map(function(m){
        return '<span class="chip">'+esc(m)+'</span>';}).join("")+'</div>';
    h+='<p class="d-detail">'+esc(n.detail)+'</p>';
    if(n.ev) h+='<p class="d-src">'+esc(n.ev)+'</p>';
    if(es.length){
      h+='<h4 class="d-h4">'+es.length+' relationship'+(es.length>1?'s':'')+'</h4><ul class="d-eg">';
      es.forEach(function(e){
        var out=(e.f===id), other=out?e.t:e.f;
        h+='<li><span class="d-dir">'+(out?"&rarr;":"&larr;")+'</span> <b>'+esc(lab(v,other))+'</b>'
          +' <span class="d-kind k-'+esc(e.k)+'">'+esc(e.k)+'</span><br><span class="d-en">'
          +esc(e.label)+'</span>'+(e.note?'<br><span class="d-eo">'+esc(e.note)+'</span>':'')+'</li>';
      });
      h+='</ul>';
    } else { h+='<p class="d-eo">No drawn relationship touches this node &mdash; an orphan on the map is itself worth a look.</p>'; }
    document.getElementById("dbody").innerHTML=h;
    document.getElementById("drawer").classList.add("on");
  }
  function close(){ document.getElementById("drawer").classList.remove("on"); }
  document.addEventListener("click", function(ev){
    var t=ev.target.closest?ev.target.closest("[data-n]"):null;
    if(t){ show(t.getAttribute("data-v"), t.getAttribute("data-n")); return; }
    if(ev.target.id==="dclose"||ev.target.id==="dscrim"||ev.target.closest&&ev.target.closest("#dscrim")) close();
  });
  document.addEventListener("keydown", function(e){ if(e.key==="Escape") close(); });
  Array.prototype.forEach.call(document.querySelectorAll(".clickable"), function(el){
    el.setAttribute("tabindex","0"); el.setAttribute("role","button");
    el.addEventListener("keydown", function(e){ if(e.key==="Enter"||e.key===" "){ e.preventDefault();
      show(el.getAttribute("data-v"), el.getAttribute("data-n")); }});
  });
})();
"""


def js_payload(doc):
    """Compact node/edge payload for the click handler."""
    band_titles = {v: {b["id"]: b["title"] for b in view["bands"]}
                   for v, view in doc["views"].items()}
    out = {}
    for v, view in doc["views"].items():
        out[v] = {
            "nodes": [{"id": n["id"], "label": n["label"], "sub": n["sub"], "detail": n["detail"],
                       "ev": n.get("ev", ""), "status": n.get("status", ""),
                       "bandTitle": band_titles[v].get(n["band"], ""),
                       "marks": n.get("marks") or ([n["tm"]] if n.get("tm") else [])}
                      for n in view["nodes"]],
            "edges": [{"f": e["from"], "t": e["to"], "k": e["kind"], "label": e["label"],
                       "note": e.get("note", "")} for e in view["edges"]],
        }
    return json.dumps(out, ensure_ascii=False)


def build_html(doc, svgs):
    v = doc["views"]
    css = open(THEME, encoding="utf-8").read()
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>SPAR F26 \u00b7 Indonesia \u2014 ecosystem, policy and bridge maps (v1)</title>
<style>%s</style></head><body>
<header class="site"><div class="wrap">
  <p class="eyebrow">SPAR Fall 2026 \u00b7 Indonesia lane \u00b7 ecosystem &amp; policy mapping (v1)</p>
  <h1>Three maps, not one</h1>
  <p class="sub">The ecosystem map shows who is positioned where. The policy map shows what the rules and
  programmes actually say. The bridge maps the join \u2014 and that join is where this lane earns its place:
  the institution best able to <em>observe</em> a problem is usually not the institution authorised to
  <em>act</em> on it. Kept separate so that claim is visible instead of blurred. Indonesia only;
  the Philippines lane is the contrast case.</p>
  <div class="rule"></div></div></header>
<main><div class="wrap">
  <section id="frame"><h2>Framing</h2>
    <p class="lede">Organised around <strong>functions</strong>, not a flat list of organisations \u2014 who
    observes AI deployment, who observes workers, who delivers support, and who can authorise a response.
    No single stakeholder can establish an AI-related labour shock: banks document deployment, labour
    institutions observe separations and support uptake, BPS shows population outcomes, and financial and
    fiscal authorities assess wider transmission. These maps connect those partial views without assuming
    they are already linked.</p>
    %s
    <p class="lede" style="margin-top:22px">Institutional responsibilities are source-backed. Proposed data
    requests, pain points and research roles are analytical recommendations \u2014 not claims that any entity
    already collects or will release the fields. Anchor sector: <strong>%s</strong>.</p>
  </section>
  %s
  <section id="resp"><h2>Responsibility map</h2>
    <p class="lede">%s</p>
    %s
  </section>
</div></main>
<footer><div class="wrap">v1, Indonesia lane only \u00b7 source: private repo <code>spar-f26-id</code> \u00b7
refined against <code>outreach/aisafety-ea/spar26-ecosystem.md</code> \u00b7 internal until AISA consent \u00b7
grades documents, never governments. Generated by <code>build/build_ecosystem_map.py</code>.</div></footer>
<div id="drawer" aria-hidden="true"><div id="dscrim"></div>
<aside class="d-panel" role="dialog" aria-modal="true" aria-label="Node detail">
<button id="dclose" aria-label="Close">&times;</button><div id="dbody"></div></aside></div>
<p class="hint">Click any card or any box in a map to see the full detail and every relationship that touches it.</p>
<script>window.SPAR_MAP = %s;</script>
<script>%s</script>
</body></html>""" % (css, reference_blocks(doc), esc(doc["lane"]["anchor"]),
                      view_section("eco", v["ecosystem"], svgs["ecosystem"], "#2E4A57", "#EEF4F7")
                      + view_section("pol", v["policy"], svgs["policy"], ACCENT_DEEP, ACCENT_TINT)
                      + view_section("bri", v["bridge"], svgs["bridge"], "#4C3A6B", "#F1EEF7"),
                      esc(doc["responsibility"]["note"]), responsibility_table(doc),
                      js_payload(doc), DRAWER_JS)


FOOT = ("solid = existing relationship  \u00b7  dashed = proposed  \u00b7  dotted = hypothesised  "
        "\u00b7  numbers index the table below")


def main():
    doc = load()
    v = doc["views"]
    specs = [("ecosystem", "spar-id-eco.svg", "Ecosystem (relationship) map", "Actors by function"),
             ("policy", "spar-id-policy.svg", "Policy map", "Documents, monitoring and levers"),
             ("bridge", "spar-id-bridge.svg", "Ecosystem \u2192 policy bridge",
              "Who observes, validates, decides, delivers")]
    out = {}
    for key, fn, title, sub in specs:
        CUR_VIEW[0] = key
        svg = build_svg(v[key], title, sub, FOOT)
        out[key] = svg
        with open(os.path.join(BUILD, fn), "w", encoding="utf-8") as fh:
            fh.write(svg)
    with open(os.path.join(BUILD, "spar-id-ecosystem-map.svg"), "w", encoding="utf-8") as fh:
        fh.write(out["ecosystem"])
    with open(os.path.join(BUILD, "spar-id-ecosystem-map.html"), "w", encoding="utf-8") as fh:
        fh.write(build_html(doc, out))
    for k in v:
        print("%-10s %d nodes %d edges -> %s" % (k, len(v[k]["nodes"]), len(v[k]["edges"]),
                                                 os.path.getsize(BUILD + "/spar-id-ecosystem-map.html")))
    print("wrote 4 svg + 1 html in", BUILD)


if __name__ == "__main__":
    main()
