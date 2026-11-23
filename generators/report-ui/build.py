#!/usr/bin/env python3
"""Build the internal executive report as one self-contained HTML file.

The report is an internal document. It carries [CANNOT VERIFY] markers and a
labelled fictional case study, so it is never synced into public/downloads and
never served by the public site.

    python3 generators/report-ui/build.py            # writes reports/*.html
    python3 generators/report-ui/build.py --pdf      # also writes reports/*.pdf
    make report                                      # same, from the repo root

Everything the artifact needs is in this repository: the three build parts in
generators/report-ui/parts/, the canonical logo cuts and the two self-hosted
variable fonts in brand-tokens/assets/. Fonts and logos are inlined as base64,
so the finished file opens offline from file:// with no network request.
"""

from __future__ import annotations

import argparse
import base64
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]      # Emplowise-Docs/
PARTS = ROOT / "generators" / "report-ui" / "parts"
ASSETS = ROOT / "brand-tokens" / "assets"
OUT_DIR = ROOT / "reports"
STEM = "Emplowise-Executive-Report-2026"

PLACEHOLDERS = {
    "__MONTSERRAT__": ASSETS / "fonts" / "montserrat-e56e84e5-latin.woff2",
    "__JAKARTA__": ASSETS / "fonts" / "jakarta-fdb05bf0-latin.woff2",
    "__LOGOMARK__": ASSETS / "logo-mark.png",
    "__LOGOLIGHT__": ASSETS / "logo-primary-375.png",
    "__LOGODARK__": ASSETS / "logo-reverse-375.png",
}


def b64(path: pathlib.Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def build_html() -> pathlib.Path:
    html = "".join((PARTS / name).read_text(encoding="utf-8")
                   for name in ("01-head.html", "02-body.html", "03-script.html"))
    for token, asset in PLACEHOLDERS.items():
        if token not in html:
            raise SystemExit(f"placeholder missing from the parts: {token}")
        if not asset.exists():
            raise SystemExit(f"brand asset missing: {asset}")
        html = html.replace(token, b64(asset))
    for token in PLACEHOLDERS:
        assert token not in html, token
    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / f"{STEM}.html"
    out.write_text(html, encoding="utf-8")
    return out


def _pdf_playwright(html: pathlib.Path, out: pathlib.Path) -> bool:
    """A4 print companion, with every reveal and timeline month expanded."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    chromium = next((shutil.which(n) for n in ("chromium", "chromium-browser", "google-chrome")
                     if shutil.which(n)), None)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=chromium, args=["--no-sandbox"]) if chromium \
            else pw.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(html.as_uri())
        page.wait_for_timeout(700)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(700)
        page.evaluate("document.querySelectorAll('.month').forEach(m => m.classList.add('is-past'))")
        page.pdf(path=str(out), format="A4", print_background=True,
                 margin={"top": "12mm", "bottom": "12mm", "left": "10mm", "right": "10mm"})
        browser.close()
    return True


def build_pdf(html: pathlib.Path) -> pathlib.Path:
    """Render the print companion. Playwright gives A4; Chromium CLI is the fallback."""
    out = OUT_DIR / f"{STEM}.pdf"
    if _pdf_playwright(html, out):
        return out
    chromium = next((shutil.which(n) for n in
                     ("chromium", "chromium-browser", "google-chrome", "chrome")
                     if shutil.which(n)), None)
    if not chromium:
        print("no Chromium and no Playwright: skipping the PDF companion", file=sys.stderr)
        return out
    print("Playwright unavailable: Chromium CLI fallback prints US Letter", file=sys.stderr)
    with tempfile.TemporaryDirectory() as profile:
        cmd = [chromium, "--headless=new", "--no-sandbox", "--disable-gpu",
               f"--user-data-dir={profile}", "--no-pdf-header-footer",
               "--virtual-time-budget=8000",
               f"--print-to-pdf={out}", html.as_uri()]
        subprocess.run(cmd, check=True, capture_output=True, timeout=180)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", action="store_true", help="also render the print companion")
    args = parser.parse_args()

    html = build_html()
    print(f"{html.relative_to(ROOT)}  {html.stat().st_size / 1024:.1f} KB")
    if args.pdf:
        pdf = build_pdf(html)
        if pdf.exists():
            print(f"{pdf.relative_to(ROOT)}  {pdf.stat().st_size / 1024:.1f} KB")
    print("internal document: do not sync into public/downloads")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())