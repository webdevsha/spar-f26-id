#!/usr/bin/env bash
# Local build + deploy of the SPAR F26 Indonesia dashboard.
# Requires CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID in the environment
# (or in a sibling .env). Sets nothing secret itself.
set -euo pipefail
cd "$(dirname "$0")"

python3 build/build_dashboard.py

# app/ is the public face: app/index.html is the site root (home page).
# The generated readiness dashboard is KEPT, not deleted — it moves to
# /dashboard.html so nothing that existed before is lost.
if [[ -f dist/index.html ]]; then
  mv dist/index.html dist/dashboard.html
fi
cp app/*.html app/*.js app/*.json dist/
if [[ -d app/files ]]; then
  rm -rf dist/files
  cp -R app/files dist/files
fi

wrangler pages deploy dist --project-name spar-f26-id --branch main