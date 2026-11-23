#!/usr/bin/env bash
# Rebuild the internal executive report from its three parts and the canonical
# brand assets. Internal only: the output is never synced to public/downloads.
set -euo pipefail

cd "$(dirname "$0")/.."

python3 scripts/check_tokens.py
python3 generators/report-ui/build.py --pdf

echo
echo "reports/ is current. Internal document: do not run sync.py on it."
