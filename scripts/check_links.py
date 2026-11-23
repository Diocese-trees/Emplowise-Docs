#!/usr/bin/env python3
"""Check that every relative Markdown link in this repo resolves.

Cross-references are part of the documentation contract: the brand kit, the
guidelines, the evidence ledger and the internal reports point at each other,
and a renamed file must not leave a dead link behind.

    python3 scripts/check_links.py
    make links

External URLs, mailto links and pure anchors are skipped. Exit code 1 means at
least one relative link points at a file that does not exist.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", "vendor", "__pycache__"}
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)")


def main() -> int:
    broken: list[str] = []
    checked = 0
    files = 0
    for md in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_DIRS for part in md.relative_to(ROOT).parts):
            continue
        files += 1
        text = md.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "data:", "tel:")):
                continue
            checked += 1
            if not (md.parent / target).exists():
                line = text[:match.start()].count("\n") + 1
                broken.append(f"{md.relative_to(ROOT)}:{line}: {target}")

    if broken:
        print(f"{len(broken)} broken relative link(s) of {checked} checked in {files} files:")
        for item in broken:
            print("  " + item)
        return 1
    print(f"cross-references ok: {checked} relative links in {files} Markdown files resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())