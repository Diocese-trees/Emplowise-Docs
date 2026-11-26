# Emplowise-Docs

The single source of truth for every Emplowise document, the 2026 brand kit,
and the Office deliverables the main site serves.

The main site (`Emplowise-Website-Phase-I`) does not author documentation. It
consumes the canonical brand tokens and the built `exports/` from this repo, so
the website, the DOCX files and the PPTX share one palette and one set of
counts.

## Layout

| Path | What lives there |
| --- | --- |
| `docs/brand-kit/` | Brand kit, branding guidelines, company profile, portfolio, pitch deck, website breakdown, tool stack, the EMPLOWISE × START 14-prompt library, deliverable README |
| `docs/` | Static hosting on GitHub Pages, the Vercel deployment, repo topology, backups and restore, theme and motion, content editing guide, and the EmploStart chat research notes |
| `docs/reports/` | Internal executive reports: the 2026 executive report and its folder index. Never synced to the public site |
| `brand-tokens/` | `tokens.css` (runtime authority), `brand-tokens.json` (machine mirror), embedded logo cuts, the two self-hosted variable fonts |
| `generators/` | `build_docx.py`, `build_pptx.py`, `verify_office.py`, pinned requirements, and `report-ui/` (the executive report parts, builder and acceptance harness) |
| `exports/` | Built `.docx` and `.pptx` files, verified before they ship. These are the only files `sync.py` copies |
| `reports/` | Built internal report artifacts (`.html`, `.pdf`). Internal only, never synced |
| `scripts/` | `build.sh`, `build_report.sh`, `sync.py` (cross-repo sync), `check_tokens.py`, `check_links.py` |

## Build

```bash
python3 -m pip install -r generators/requirements.txt
make build          # or: bash scripts/build.sh
```

`make build` checks token parity, rebuilds seven DOCX and the eight-slide PPTX,
and runs `verify_office.py`, which fails on a missing package part, a broken
slide count, or an internal marker leaking into a document body.

The seventh DOCX, `Emplowise-Start-Prompt-Library-2026.docx`, documents the
EmploStart prompt library: fourteen prompts, one per letter of EMPLOWISE and
START, sourced from `EmploStart/data/prompt-library.json`.

## Internal reports

The [2026-11-26 SEO, AEO, GEO and conversion audit](docs/reports/seo-audit-20261126/README.md) contains all eight phase documents, the running issues log, preserved crawl evidence and an explicit coverage/limitations matrix. It is documentation only, not a deployed website rewrite.

```bash
make report        # token check + rebuild reports/*.html and the A4 PDF
make report-check  # the same, then the Playwright acceptance pass
make links         # every relative Markdown link in the repo resolves
```

`docs/reports/EXECUTIVE_REPORT_2026.md` is the Markdown source of the 2026
executive report. `generators/report-ui/` holds the three HTML parts, the
builder and the acceptance harness; `reports/` holds the built single-file
HTML and its print companion. The builder inlines the canonical fonts and logo
cuts from `brand-tokens/assets/`, so the finished file opens offline with no
network request.

The report is **internal**. It carries `[CANNOT VERIFY]` markers and a labelled
fictional case study, so it stays out of `exports/` and out of
`public/downloads/`. `sync.py` only copies `.docx` and `.pptx`, which keeps the
boundary mechanical rather than a matter of remembering. See
[`docs/reports/README.md`](docs/reports/README.md).

## Sync into the main site

```bash
make sync           # tokens.css + exports -> main/public/{css,downloads}
make sync-check     # fail if the main repo has drifted
```

The sync script finds the main repo at the sibling `Emplowise-Website-Phase-I`
checkout; pass `--main /path/to/main` to point elsewhere.

## Honesty and brand rules

- Tagline: **Clarity Built on Structure**. Philosophy: Empower people.
  Simplify work. Build momentum.
- Navy `#081B3E`, Teal `#0D9488`, Deep Teal `#0F766E`, Aqua `#5EEAD4`,
  Ice `#F0F9F9`, Off-White `#F7F7F7`, Slate `#1E293B`, White `#FFFFFF`.
- Montserrat 700/800 for display, Plus Jakarta Sans 400/500/600 for body.
- Zero neon glows, decorative gradients in body copy, or fake browser chrome.
- No raw `[To Verify]` markers in public HTML, DOCX or PPTX bodies. Internal
  reports under `docs/reports/` and `reports/` may carry `[CANNOT VERIFY]`
  markers, because they are never published.
- EmploStart is a voluntary, permanently free utility. Never claim UN
  endorsement or fabricate salaries, user counts, clients, placement rates or
  market size.
