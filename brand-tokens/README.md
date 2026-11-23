# Canonical brand tokens

This folder is the single source of truth for the Emplowise Brand Kit 2026.

- `tokens.css` is the runtime token sheet the main site loads as
  `public/css/tokens.css`. It is the authority for colours, type, spacing,
  layout, radius, shadow and motion.
- `brand-tokens.json` is the machine-readable mirror for generators, docs and
  CI parity checks. Keep it in lockstep with `tokens.css`.
- `assets/` holds the vector-clean logo cuts the Office generators embed
  (`logo-primary-375.png`, `logo-reverse-375.png`, `logo-mark.png`) and
  `assets/fonts/` holds the two self-hosted variable WOFF2 files
  (`montserrat-e56e84e5-latin.woff2`, `jakarta-fdb05bf0-latin.woff2`). They are
  byte-identical to the copies the main site serves from `public/fonts/`.
- `generators/report-ui/build.py` inlines these fonts and cuts as base64 into
  the internal executive report, so that artifact needs nothing outside this
  repository and opens offline.

## Sync into the main site

```bash
python3 scripts/sync.py tokens   # copy tokens.css into the main repo
python3 scripts/sync.py all      # tokens + built Office exports
python3 scripts/sync.py check    # fail if the main repo has drifted
```

The sync script defaults to the main repo at `Emplowise-Website-Phase-I/`
next to this one; pass `--main /path/to/main` to override.

## Rules

- Only edit tokens here. Never hand-edit the copy in the main repo.
- Zero neon glows, decorative gradients in body copy, or fake browser chrome.
- Monospace is reserved for file names and code samples, never for marketing
  headings.
