#!/usr/bin/env bash
# Regenerate every verification this project relies on, in one pass.
# Usage: bash scripts/verify-all.sh [--quiet]
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
fail=0

echo "== 1. model.js reproduces the sheet's Summary (app state read from index.html) =="
if command -v node >/dev/null; then
  node scripts/verify-app-vs-sheet.js || fail=1
else
  echo "  SKIP: node not found"; fail=1
fi

echo
echo "== 2. app scripts parse =="
python3 scripts/extract-inline.py app/index.html > /tmp/_idx.js && node --check /tmp/_idx.js && echo "  app/index.html inline OK" || { echo "  FAIL index"; fail=1; }
node --check app/data.js && echo "  app/data.js OK" || { echo "  FAIL data.js"; fail=1; }

echo
echo "== 3. cleaned corpus files are Indonesia-only =="
python3 - <<'PY'
import csv
bad = 0
for f in ("data/postings-corpus/clean/monthly-country.csv",
          "data/postings-corpus/clean/monthly-platform.csv",
          "data/postings-corpus/clean/exposure-category.csv"):
    rows = list(csv.DictReader(open(f, encoding="utf-8-sig")))
    other = [r for r in rows if (r.get("country") or "").strip() not in ("Indonesia", "ID")]
    print("  {:<52} {:>4} rows, {} non-Indonesia".format(f.split("/")[-1], len(rows), len(other)))
    bad += len(other)
raise SystemExit(1 if bad else 0)
PY
[ $? -ne 0 ] && fail=1

echo
echo "== 4. no raw corpus layer is tracked =="
tracked=$(git ls-files | grep -cE "postings_clean|postings_text|scope_jobs|cc_fetch_text|wayback_fetch_output/html" || true)
echo "  raw layers tracked: ${tracked:-0}"
[ "${tracked:-0}" -ne 0 ] && { echo "  FAIL: raw corpus in git"; fail=1; }

echo
if [ "$fail" -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SOME CHECKS FAILED"; fi
exit "$fail"
