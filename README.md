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
| `docs/brand-kit/` | Brand kit, branding guidelines, company profile, portfolio, pitch deck, website breakdown, tool stack, deliverable README |
| `docs/` | Static hosting, repo topology, theme and motion, content editing guide, hosting, and the EmploStart chat research notes |
| `brand-tokens/` | `tokens.css` (runtime authority), `brand-tokens.json` (machine mirror), embedded logo cuts |
| `generators/` | `build_docx.py`, `build_pptx.py`, `verify_office.py`, pinned requirements |
| `exports/` | Built `.docx` and `.pptx` files, verified before they ship |
| `scripts/` | `build.sh`, `sync.py` (cross-repo sync), `check_tokens.py` |

## Build

```bash
python3 -m pip install -r generators/requirements.txt
make build          # or: bash scripts/build.sh
```

`make build` checks token parity, rebuilds six DOCX and the eight-slide PPTX,
and runs `verify_office.py`, which fails on a missing package part, a broken
slide count, or an internal marker leaking into a document body.

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
- No raw `[To Verify]` markers in public HTML, DOCX or PPTX bodies.
- EmploStart is a voluntary, permanently free utility. Never claim UN
  endorsement or fabricate salaries, user counts, clients, placement rates or
  market size.
