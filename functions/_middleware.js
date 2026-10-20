// Cloudflare Pages access gate — HTTP Basic Auth.
// The password is read from the Pages project secret SITE_PASSWORD
// (set with: wrangler pages secret put SITE_PASSWORD --project-name spar-f26-id).
// It is NEVER committed to this repo. If the secret is missing we fail CLOSED.
//
// Scope: the main dashboard (index.html / "/") is gated. Standalone reports
// under /build/ are PUBLIC (no password) so they can be shared directly.
export async function onRequest(context) {
  const { request, env, next } = context;

  const url = new URL(request.url);
  // Public: everything under /build/ (standalone reports like the postings page).
  if (url.pathname === "/build" || url.pathname.startsWith("/build/")) {
    return next();
  }

  const expected = env.SITE_PASSWORD;
  if (!expected) {
    return new Response("Access gate is not configured on this deployment.", {
      status: 503,
      headers: { "content-type": "text/plain; charset=utf-8" },
    });
  }

  const header = request.headers.get("Authorization") || "";
  if (header.startsWith("Basic ")) {
    let decoded = "";
    try {
      decoded = atob(header.slice(6));
    } catch (_) {
      decoded = "";
    }
    const sep = decoded.indexOf(":");
    const password = sep >= 0 ? decoded.slice(sep + 1) : "";
    if (password === expected) {
      return next();
    }
  }

  return new Response("Authentication required.", {
    status: 401,
    headers: {
      "WWW-Authenticate": 'Basic realm="SPAR F26 Indonesia", charset="UTF-8"',
      "content-type": "text/plain; charset=utf-8",
    },
  });
}
