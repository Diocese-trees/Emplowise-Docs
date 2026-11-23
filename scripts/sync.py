#!/usr/bin/env python3
"""Cross-repo sync for the Emplowise-Docs source of truth.

This repo owns the .md sources, the canonical brand tokens, and the built
Office exports. The main site consumes them. Run this script to push the
canonical copies into the main repo, or to check that they have not drifted.

    python3 scripts/sync.py tokens        # tokens.css -> main/public/css
    python3 scripts/sync.py exports       # exports/* -> main/public/downloads
    python3 scripts/sync.py all           # tokens + exports
    python3 scripts/sync.py check         # fail if main has drifted

The main repo defaults to the sibling checkout at ../../ (Emplowise-Website-
Phase-I); pass --main /path/to/main to override.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # _staging/Emplowise-Docs
DEFAULT_MAIN = ROOT.parents[1]                       # /data/emplowise
EXPORT_SUFFIXES = (".docx", ".pptx")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tokens_source() -> Path:
    return ROOT / "brand-tokens" / "tokens.css"


def exports_source_dir() -> Path:
    return ROOT / "exports"


def plan(actions: set[str], main: Path) -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []
    if "tokens" in actions or "all" in actions:
        pairs.append((tokens_source(), main / "public" / "css" / "tokens.css"))
    if "exports" in actions or "all" in actions:
        for src in sorted(exports_source_dir().glob("*")):
            if src.suffix in EXPORT_SUFFIXES:
                pairs.append((src, main / "public" / "downloads" / src.name))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "action",
        choices=["tokens", "exports", "all", "check"],
        help="what to sync, or 'check' to verify the main repo is current",
    )
    parser.add_argument("--main", type=Path, default=DEFAULT_MAIN,
                        help=f"path to the main repo (default: {DEFAULT_MAIN})")
    args = parser.parse_args()

    main_repo = args.main.resolve()
    if not (main_repo / "artisan").exists():
        print(f"error: {main_repo} does not look like the main repo (no artisan)", file=sys.stderr)
        return 2

    actions = {"all"} if args.action == "all" else {args.action}
    if args.action == "check":
        actions = {"tokens", "exports"}

    pairs = plan(actions, main_repo)
    if not pairs:
        print("nothing to sync", file=sys.stderr)
        return 1

    drift = 0
    for src, dst in pairs:
        if not src.exists():
            print(f"missing source: {src}", file=sys.stderr)
            drift += 1
            continue
        if args.action == "check":
            if not dst.exists():
                print(f"MISSING  {dst.relative_to(main_repo)}")
                drift += 1
            elif digest(src) != digest(dst):
                print(f"DRIFT    {dst.relative_to(main_repo)}")
                drift += 1
            else:
                print(f"ok       {dst.relative_to(main_repo)}")
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            print(f"synced   {dst.relative_to(main_repo)}")

    if args.action == "check":
        if drift:
            print(f"\n{drift} file(s) out of sync", file=sys.stderr)
            return 1
        print(f"\nall {len(pairs)} file(s) in sync")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
