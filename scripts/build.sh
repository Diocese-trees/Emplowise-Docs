#!/usr/bin/env bash
# Rebuild every Office deliverable from the Markdown sources and verify it.
set -euo pipefail

cd "$(dirname "$0")/.."

python3 scripts/check_tokens.py
python3 generators/build_docx.py
python3 generators/build_pptx.py
python3 generators/verify_office.py

echo
echo "exports/ is current. Run: python3 scripts/sync.py exports"
