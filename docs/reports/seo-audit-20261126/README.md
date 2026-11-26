# Emplowise SEO, AEO, GEO and conversion audit

Snapshot: 2026-11-26. Subject: Emplowise, not Qodar AI. Source website HEAD: `89a8e7f`. This is internal documentation, not a published website rewrite.

## Phase coverage and acceptance

| Stage | Deliverable | Coverage | Remaining limitation |
| --- | --- | --- | --- |
| 1. Backup | [Phase-1-Backup.md](Phase-1-Backup.md) | 15 public pages, metadata, content, links, assets, repository backups | Full unabridged copy also lives in [_crawl/detailed_dump.txt](_crawl/detailed_dump.txt) |
| 2. Deep analysis | [Phase-2-Deep-Analysis.md](Phase-2-Deep-Analysis.md) | Technical, on-page, content, entities, linking, lab/mobile observations | Field CWV, rankings, backlinks and traffic not measured without owner data |
| 3. Competitor gaps | [Phase-3-Gap-Analysis.md](Phase-3-Gap-Analysis.md) | Five researched competitors, qualitative gap priorities | Not a proven top-five ranking or AI-citation leaderboard; one blocked competitor page |
| 4. Breakdown | [Phase-4-Breakdown.md](Phase-4-Breakdown.md) | Existing pages, proposed units, dependencies and metrics | Proposed pages are not implemented |
| 5. SEO/AEO/GEO | [Phase-5-SEO-AEO-GEO-Extraction.md](Phase-5-SEO-AEO-GEO-Extraction.md) | Page-specific mappings, shared guidance, direct answers and modular recommendations | Some supporting pages use shared/grouped recommendations, not separate full extraction blocks |
| 6. Research | [Phase-6-Research-Plan.md](Phase-6-Research-Plan.md) | 90-day owners, tools, frequency and decision triggers | Research plan delivered; 90-day execution has not happened |
| 7. UI/UX | [Phase-7-UI-UX-Plan.md](Phase-7-UI-UX-Plan.md) | All 15 pages and 404, frozen brand contract, backlog | Wireframe notes, not implemented screens; OG artwork not produced |
| 8. Rewrite | [Phase-8-SEO-Rewrite.md](Phase-8-SEO-Rewrite.md) | Full copy proposals for all 15 pages, metadata, CTA, links and schema | Documentation only; full Laravel SEO/CI validation required after applying copy |

**Coverage: 8 of 8 phase documents delivered, plus the issues log. This does not mean 8 phases of website implementation have shipped.** Limitations above remain open and must not be represented as measured evidence or deployed changes.

## Validation and evidence

[Issues-and-Decisions.md](Issues-and-Decisions.md) records the phase sequence, cross-phase decisions and the page coverage matrix. [_crawl/extracted.json](_crawl/extracted.json) holds structured crawl records; [_crawl/site.css](_crawl/site.css) preserves observed brand tokens. Original sources are preserved, not overwritten by the proposed rewrite.

Pre-audit private shadows were created for Website, Docs and EmploStart, with all branches/tags verified. GitHub-owned pull-request refs are retained in local bundles, not pushed into shadow repositories. A further verified Docs bundle was created before publishing these audit files.

## Implementation boundary

No route, brand asset, price or public website copy is changed by this documentation commit. Do not sync this folder into public downloads. Apply the rewrite only in a separate reviewed implementation change, preserve legal meaning, and run the site's SEO audit, test suite and browser checks before release. Data access and claimed ownership of profiles/authors must be verified before introducing analytics, sameAs, dates or performance claims.
