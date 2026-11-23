#!/usr/bin/env python3
"""Fail if brand-tokens.json and tokens.css disagree on the core palette.

The two files are a deliberate pair: tokens.css is what the browser loads,
brand-tokens.json is what generators and docs read. This guard keeps the core
eight brand colours and the tagline in lockstep.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = ROOT / "brand-tokens" / "tokens.css"
JSON = ROOT / "brand-tokens" / "brand-tokens.json"


def main() -> int:
    css = CSS.read_text(encoding="utf-8").lower()
    data = json.loads(JSON.read_text(encoding="utf-8"))
    core = data["color"]["core"]
    problems = 0
    for name, hexv in core.items():
        if name.startswith("_"):
            continue  # documented spec swatches, not runtime tokens
        if not isinstance(hexv, str) or hexv.lower() not in css:
            print(f"MISSING {name} {hexv} in tokens.css", file=sys.stderr)
            problems += 1
    tagline = data.get("tagline", "")
    brand_md = (ROOT / "docs" / "brand-kit" / "BRAND_KIT.md")
    if brand_md.exists() and tagline not in brand_md.read_text(encoding="utf-8"):
        print(f"MISSING tagline {tagline!r} in BRAND_KIT.md", file=sys.stderr)
        problems += 1
    if problems:
        print(f"\n{problems} token mismatch(es)", file=sys.stderr)
        return 1
    print(f"brand tokens in sync ({sum(1 for k in core if not k.startswith('_'))} core colours, tagline present)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
