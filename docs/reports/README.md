# docs/reports

Internal analysis documents. This folder holds the Markdown source of truth for
the 2026 internal executive report, cross-referenced against the rest of the
documentation so the readable version and the built interactive version describe
the same numbers.

| File | What it is |
| --- | --- |
| [`EXECUTIVE_REPORT_2026.md`](EXECUTIVE_REPORT_2026.md) | The full report: business context, dated Pakistan evidence, twelve copy blocks, the fictional case study, the dashboard model and formulas, the employee data format, ten priorities, eleven dated sources, the acceptance run |

## Visibility

**INTERNAL.** Nothing in this folder is synced into `public/downloads/` and
nothing here is published to the site. `scripts/sync.py` moves tokens and Office
exports only; `scripts/build_report.sh` writes to `reports/` and stops there.
Marker legends, `[CANNOT VERIFY]` items and verification notes stay visible in
these files and must be stripped before any of this text reaches a public page,
per the public-render rule in
[`../brand-kit/BRANDING_GUIDELINES.md`](../brand-kit/BRANDING_GUIDELINES.md).

## Where things live

| Path | Content |
| --- | --- |
| [`../../reports/`](../../reports/) | Built internal artefacts: `Emplowise-Executive-Report-2026.html` (self-contained, 295.8 KB, works from `file://`) and `Emplowise-Executive-Report-2026.pdf` (A4, 23 pages, controls hidden) |
| [`../../generators/report-ui/`](../../generators/report-ui/) | `build.py` (assembler), `parts/` (head, body, script), `test_report.py` (Playwright acceptance harness) |
| [`../../brand-tokens/`](../../brand-tokens/) | `tokens.css`, `brand-tokens.json`, and `assets/` with the logo cuts and the embedded fonts the report inlines |
| [`../../scripts/build_report.sh`](../../scripts/build_report.sh) | Token check, then build with the PDF step |

## Rebuild

```bash
make report         # from the repo root: check_tokens.py, then build.py --pdf
make report-check   # rebuild, then run the Playwright acceptance pass
```

Equivalent direct commands:

```bash
python3 generators/report-ui/build.py          # HTML only
python3 generators/report-ui/build.py --pdf    # HTML plus the print companion
python3 generators/report-ui/test_report.py    # serves reports/ on a free local port
```

The harness needs no manual server and no network: it starts its own static
server over `reports/` and prints a pass list plus a console-error count.

## Evidence and honesty rules that apply here

- Every external figure carries a source and a date, listed in the report
  appendix. An undated statistic is unusable, per the evidence tiers in
  [`../brand-kit/BRANDING_GUIDELINES.md`](../brand-kit/BRANDING_GUIDELINES.md).
- Where Pakistan-specific public data does not exist, the report writes
  `[CANNOT VERIFY]` and names the audit field that would settle it. The markers
  are removed only when an audit sample earns them.
- The case study is fictional and labelled as such in its own banner. The ledger
  is illustrative arithmetic on invented inputs, not a savings claim and not a
  promise. The unpriced compliance line stays unpriced because Emplowise does
  not guarantee legal outcomes.
- Dashboard numbers are model outputs on a seeded fictional register, not client
  measurements. They change when the model controls change, which is the point of
  the preview.
- No client names, no measured outcomes, no invented percentages, no UN
  endorsement, no fabricated salaries, user counts, logos or market size.
- Voice rules are enforced inside the built report as a live brand lint: no
  banned words, no em dashes, no exclamation marks, British spelling.
- The report never touches the frozen public copy. It may reframe it for an
  internal reader, but it must not contradict a number, a service name or a
  scope statement.

## Section to owner

| Report section | Rule it depends on | Owning document |
| --- | --- | --- |
| Step 1, business context | Confirmed facts, pillars, method, pricing bands, scope boundary | [`../brand-kit/COMPANY_PROFILE.md`](../brand-kit/COMPANY_PROFILE.md) |
| Step 1, positioning and buyer situations | Two ranked audiences, situation-led copy | [`../brand-kit/BRANDING_GUIDELINES.md`](../brand-kit/BRANDING_GUIDELINES.md) |
| Step 1b, dated evidence | Evidence tiers, dating, Open Evidence Ledger | [`../brand-kit/BRANDING_GUIDELINES.md`](../brand-kit/BRANDING_GUIDELINES.md), [`../brand-kit/README.md`](../brand-kit/README.md) |
| Step 2, copy blocks and lint | Voice, banned words, em dash, British spelling, frozen SEO copy | [`../brand-kit/BRANDING_GUIDELINES.md`](../brand-kit/BRANDING_GUIDELINES.md) |
| Step 2, where copy is edited | Config source for page copy and prices | [`../CONTENT_EDITING_GUIDE.md`](../CONTENT_EDITING_GUIDE.md) |
| Step 3, fictional case study | No fabricated clients, testimonials or measured outcomes | [`../brand-kit/BRANDING_GUIDELINES.md`](../brand-kit/BRANDING_GUIDELINES.md) |
| Step 4, placement and restraint | Which route carries which block | [`../REPO_TOPOLOGY.md`](../REPO_TOPOLOGY.md), [`../brand-kit/WEBSITE_BREAKDOWN.md`](../brand-kit/WEBSITE_BREAKDOWN.md) |
| Step 4, tokens, type, motion, contrast, targets | Brand Kit 2026 palette, type scale, durations, theme contract | [`../brand-kit/BRAND_KIT.md`](../brand-kit/BRAND_KIT.md), [`../THEME_AND_MOTION.md`](../THEME_AND_MOTION.md), [`../../brand-tokens/tokens.css`](../../brand-tokens/tokens.css) |
| Step 4b, employee data format | Intake schema and validation, audit wizard | [`../brand-kit/COMPANY_PROFILE.md`](../brand-kit/COMPANY_PROFILE.md) for scope, the generator parts for the schema |
| Priorities, delivery owners | Tooling and stack the work must stay inside | [`../brand-kit/TOOL_STACK.md`](../brand-kit/TOOL_STACK.md) |
| Verification record, hosting and publishing limits | Why this report is not part of the static public build | [`../STATIC_HOSTING.md`](../STATIC_HOSTING.md), [`../REPO_TOPOLOGY.md`](../REPO_TOPOLOGY.md) |
