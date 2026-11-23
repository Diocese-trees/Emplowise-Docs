# AGENTS.md — Emplowise-Docs

## Role in the three-repository ecosystem

This repo is the single source of truth for documentation and brand assets.
The other two repos consume it:

- **Emplowise-Website-Phase-I (main site)** consumes `brand-tokens/tokens.css`
  as `public/css/tokens.css` and `exports/*.docx|*.pptx` as
  `public/downloads/`. It serves the static `/docs` hub that links those files.
- **EmploStart (product)** is a standalone, permanently free career utility.

## Ownership

- Own: every `.md` document, the canonical tokens, the DOCX/PPTX generators,
  the built `exports/`, and the cross-repo sync script.
- Do not hand-edit the copies inside the main repo. Change them here, run
  `make build`, then `make sync`.
- Keep `brand-tokens/tokens.css` and `brand-tokens/brand-tokens.json` in
  lockstep; `scripts/check_tokens.py` enforces the core palette and tagline.

## Hard rules

- Brand Kit 2026 palette and type only. Zero neon glows, decorative gradients
  in body copy, or fake browser chrome.
- No raw `[To Verify]` markers in public HTML, DOCX or PPTX bodies.
- EmploStart is voluntary and permanently free. Never claim UN endorsement,
  certification or partnership. Never fabricate salaries, user counts, client
  logos, placement rates, or market size.
- B2B pages stay ROI-driven; EmploStart carries the public-good halo with a
  subtle B2B HR Audit bridge.

## Verification before shipping

```bash
make build        # token check + rebuild + verify-office
make sync-check   # main repo must match this repo
```

`verify_office.py` must print six DOCX passes and an eight-slide PPTX pass.
