#!/usr/bin/env bash
# Local build + deploy of the SPAR F26 Indonesia dashboard.
# Requires CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID in the environment
# (or in a sibling .env). Sets nothing secret itself.
set -euo pipefail
cd "$(dirname "$0")"

python3 build/build_dashboard.py
wrangler pages deploy dist --project-name spar-f26-id --branch main