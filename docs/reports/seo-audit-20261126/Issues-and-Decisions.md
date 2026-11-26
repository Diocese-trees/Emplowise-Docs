# Issues and Decisions — Emplowise Website Audit 2026-11-26

Running log maintained after **every** phase. Each phase validates against the previous one.
Any contradiction found during a later phase is recorded here and propagated back into the
affected earlier document as a dated correction note (the earlier doc is never silently rewritten).

## Scope & ground rules (fixed at start)
- **Live site (subject of audit):** https://diocese-trees.github.io/Emplowise-Website-Phase-I/
- **Local website source:** `/data/emplowise` (Laravel app; origin = Diocese-trees/Emplowise-Website-Phase-I, HEAD `89a8e7f`)
- **Docs repo:** `/data/emplowise/_staging/Emplowise-Docs` (origin Emplowise-Docs, HEAD `252757c`)
- **Product repo:** `/data/emplowise/_staging/EmploStart` (origin EmploStart, HEAD `2679c1a`)
- **Name correction:** user's earlier "Qodar AI" → **Emplowise**. Note: a `wip` git remote is literally named
  `Diocese-trees/Emplowise-repo-qodar-ai-work-in-progress`; it is treated as the Emplowise WIP branch, not a
  separate brand. All audit copy uses "Emplowise".
- **Read-only:** no repo edits, no commits, no pushes, no live-site modification. Deliverables are the nine
  Markdown docs + ZIP under `/data/emplowise-audit-20261126`.
- **Truthfulness constraints (apply to every phase):**
  - No fabricated SERP rankings, backlink counts, or field (CrUX) Core Web Vitals without GSC/analytics/CrUX evidence.
  - No invented clients, case studies, results, endorsements, testimonials, or pricing beyond what is published.
  - FAQPage/HowTo schema recommended only where genuinely eligible; no promises of rich results.
  - `sameAs` / authors / dates must be truthful (no fake social profiles, no unauthored dates).

## Backup prerequisite (recorded, verified)
- Upstream `--mirror` clones + bundles at `/data/backups/20261126-shadow/` for Emplowise-Website-Phase-I,
  Emplowise-Docs, EmploStart. Manifest `manifest.json` all `verified: true`.
- SHA-256 + HEADs: website `89a8e7f8…`, Docs `252757c6…`, EmploStart `2679c1ac…`.
- Private shadows `Diocese-trees/{name}-shadow-20261126` pushed/verified; GitHub-managed `refs/pull/*`
  cannot be pushed → retained in local mirrors/bundles only.
- Downloadable archive: `/data/backups/20261126-shadow/Emplowise-Pre-Audit-Backups-20261126.zip` (9,736,921 bytes).
- Local checkouts correspond to latest `main`; originals and shadows must not be modified.

---

## Phase-by-phase log

### Phase 1 — Live crawl + backup record
Completed. See `Phase-1-Backup.md`. Issues raised below (carried into later phases).

| ID | Phase | Issue / observation | Decision | Status |
|----|-------|---------------------|----------|--------|
| I-01 | 1 | `/pitch-deck/` is linked 16× in nav/footer but is **not** in `sitemap.xml` | Correct — it is `noindex,follow` with self canonical. Keep excluded from sitemap. Flag in Phase 2/5 so we do not "add" it. | Open→resolved (no action) |
| I-02 | 1 | Legacy URLs `/pricing/ /career-hub/ /student-hub/ /ai-automation/ /team/` return **HTTP 200 meta-refresh stubs** on GitHub Pages, not the 301/308 defined in `routes/web.php` + `vercel.json` | GH Pages cannot run those rules. Stubs are `noindex,follow` + canonical to target → no duplicate risk, but weaker link-signal consolidation than a true 301. Raise in Phase 2 (tech) + Phase 8 (recommend host-level redirects). | Open |
| I-03 | 1 | **No `author`, `datePublished`, or `dateModified`** in any JSON-LD (all 15 pages) | Phase 5 must supply truthful authors/dates only; legal pages already show "Last updated 22 Nov 2026". Do not invent dates for service pages. | Open |
| I-04 | 1 | Footer "Socials" (LinkedIn, Facebook, Instagram, X, YouTube, WhatsApp) are `href="#"` **placeholders** | Phase 5 `sameAs` must be truthful — cannot cite profiles whose existence is unverified. Flag as a data gap needing client confirmation. | Open |
| I-05 | 1 | `og:image`/`twitter:image` identical on every page = `logo-primary.png` | Generic social preview. Phase 7/8 recommend page-specific OG images (no stock photos; brand-consistent). | Open |
| I-06 | 1 | `/faq/` has a real `FAQPage` schema (21 Q/A) — eligible markup already live | Phase 5 must NOT claim rich-result guarantees; note it is correctly implemented, only pitch-deck/terms/etc. could add more. | Open |
| I-07 | 1 | Contact page links to ChatGPT/Claude/Gemini/Perplexity with a prefilled "What is Emplowise…" prompt (AEO/GEO by design) | Good existing GEO surface. Build Phase 5 around it. | Open |
| I-08 | 1 | Team portraits are initials placeholders (MA/AH/SN), "official shoot" pending | Phase 8 rewrite may reference named people (they are real, config-sourced) but must not add fake headshots/photos or over-claim credentials beyond config. | Open |
| I-09 | 1 | EmploStart **product** app (`/data/emplowise/_staging/EmploStart`, deployed at diocese-trees.github.io/EmploStart/) is a **separate repo/deployment**; its `index.html` has no `canonical` and no `og:title` | Out of Phase 8 rewrite scope (website pages only) but recorded as cross-repo finding; recommend to owner. | Noted |
| I-10 | 1 | `/api/chat` and `/api/audit` are inert on GH Pages (404); site uses `api.web3forms.com` for contact + audit forms and a static chat widget | Phase 2 note: chat widget is client-side only; forms rely on third-party web3forms. | Open |
| I-11 | 1 | config has a `seo.team` entry but `/team` is only an anchor (`#team`) on what-we-are | Not a standalone indexable page; handled as a section in Phase 4. | Resolved (no action) |

### Phase 2 — Deep technical/SEO analysis
Completed. See `Phase-2-Deep-Analysis.md`. Lab curl evidence attached. Validated against Phase 1 (no contradiction).

| ID | Phase | Issue / observation | Decision | Status |
|----|-------|---------------------|----------|--------|
| I-12 | 2 | Versioned assets (`?v=`) return `cache-control: max-age=600` on GitHub Pages; repo `vercel.json` (86400) is ignored by GH Pages | Recommend `max-age=31536000, immutable` on a host that honours it, or accept GH Pages default + rely on `?v=`. Phase 6 CI/ops task. | Open |
| I-13 | 2 | Organization schema `url` has no trailing slash while page canonicals do (minor self-mismatch) | Align in Phase 8 schema block. | Open |
| I-14 | 2 | Missing `BreadcrumbList`, per-`Service` nodes, `WebSite`/`SearchAction`, and `dateModified` across all pages; legal "Last updated" not machine-readable | Phase 5 specifies which are truthful/eligible; Phase 8 drafts them. No fabricated dates for non-dated pages. | Open |
| I-15 | 2 | Field CWV, Lighthouse scores, keyword rank/volume/CTR, backlink/referring-domain counts **unavailable** (no GSC/analytics/CrUX/Ahrefs/headless in env) | Documented as measurement limits; only curl lab proxies reported. Phase 6 assigns collection to owners. | Open (accepted limit) |
| I-16 | 2 | Positive: 1 H1 on 14/14, titles 45-60 chars, descs 136-155, 0 missing alts, no orphan pages, no sitemap↔index mismatch, strong CSP/headers | Preserve these in Phase 8 rewrite; do not "fix" what is already correct. | Resolved (no action) |

### Phase 3 — Competitor & gap analysis
Completed. See `Phase-3-Gap-Analysis.md`. 5 competitors via web search + live fetch, cited. Validated vs Phase 2 (consistent).

| ID | Phase | Issue / observation | Decision | Status |
|----|-------|---------------------|----------|--------|
| I-17 | 3 | G-1: No regularly-published advice blog / informational content hub (competitors Core Bhive, ProHR Xpert, Osynix have `/blog`) | Phase 6 content plan + Phase 5 citable-answer strategy; keep "confirmed facts only" voice, no invented stats. | Open |
| I-18 | 3 | G-2: Emplowise absent from PK HR/PEO comparison directories (Manifest, Clutch) | Phase 6 outreach task (legit listing requests); no fabricated reviews. | Open |
| I-19 | 3 | Differentiators confirmed vs competitors: published PKR pricing, EmploStart free tool, native GEO/answer-engine prompts, anti-hype trust copy | Phase 5/8 amplify rather than "fix"; make machine-readable. | Open (positive) |
| I-20 | 3 | Competitor ranking/SOV/backlinks/AI-citation NOT measured; Xpezia 403 (unverified); Scaleup "from PKR 50k" only from a social post | Recorded as limits; do not upgrade to asserted facts anywhere downstream. | Open (accepted limit) |

### Phase 4 — Page/unit breakdown
Completed. See `Phase-4-Breakdown.md`. 15 pages + shared units decomposed; validated vs ExportStatic (15+5 stubs) and Phases 1–3.

| ID | Phase | Issue / observation | Decision | Status |
|----|-------|---------------------|----------|--------|
| I-21 | 4 | Proposed NEW unit types (U-1 blog … U-10 directories) do **not** exist today | Must stay labelled `[PROPOSED]` in Phases 5/6/8; not counted as "existing coverage" in final verification. | Open |
| I-22 | 4 | `/what-we-do/` bundles 14 services on one page (no per-service URLs) | Kept as-is in Phase 8 (single page rewrite); per-service split is U-3 `[PROPOSED]`, not a rewrite requirement. | Open |

### Phase 5 — SEO / AEO / GEO extraction & mapping
Completed. See `Phase-5-SEO-AEO-GEO-Extraction.md`. 11 AEO direct answers (all 42–54w, in 40–60 range) + 11 modular recommendations (all 147–178w, in 120–180 range). Validated vs Phases 1–4 (no contradiction; `[PROPOSED]` never asserted as existing).

| ID | Phase | Issue / observation | Decision | Status |
|----|-------|---------------------|----------|--------|
| I-23 | 5 | Truthful `sameAs`/author/date can only be added where real data exists (legal date 22 Nov 2026; real emails; **no** phone/profiles/photos) | Phase 8 schema emits only verifiable fields; everything else omitted + flagged for client. | Open |
| I-24 | 5 | `HowTo` deliberately NOT recommended (method is internal process, not user recipe; HowTo treatment restrictive) and no rich-result promises made | Honoured in Phase 8 schema blocks. | Resolved (no action) |
| I-25 | 5 | Footer "Socials" heading + 6 `#` links read as unfinished (users + crawlers) | Phase 7 UI: remove/relabel until real profiles exist; Phase 8 note. | Open |

### Phase 6 — 90-day research/action plan
Completed. See `Phase-6-Research-Plan.md`. Instrumentation-first 90-day plan (0–30 / 31–60 / 61–90) with Tool / Owner / Frequency / Trigger / Success-measure per task, standing cadences (§6.4) and a trigger catalogue (§6.5). Validated vs Phases 1–5: every task traces to an I-nn finding or a `[PROPOSED]` unit; no task asserts a rank, backlink, traffic or field-CWV outcome.

| ID | Phase | Issue / observation | Decision | Status |
|----|-------|---------------------|----------|--------|
| I-26 | 6 | No GSC, GA4, CrUX, rank or backlink data exists for the property, so the plan has **no baseline** to measure improvement against | Phase 6 is sequenced instrumentation-first (connect GSC + Bing Webmaster + consent-gated GA4 before any content claim); all success measures are stated as "first reading to be recorded", never as forecast deltas. | Open (accepted limit) |
| I-27 | 6 | Only three real people are evidenced in `config/emplowise.php` (Abdul Hadi, Samarah Nabil, Muhammad Ali); the plan needs ~4 skill tracks | Owners assigned to those three **by role already stated on the site** plus a generic `DEV` owner for build work; capacity/hours deliberately **not** estimated (no evidence). Flagged for client confirmation. | Open |
| I-28 | 6 | Phase 5 `[PROPOSED]` units (blog/guides, per-service pages, case studies) risk being read as committed roadmap | Every Phase 6 content task is written as **evaluate → gate on evidence** (e.g. guides only once 3 factual topics are confirmable; case studies only after a signed-off engagement). No publication cadence promised to third parties. | Resolved (guarded in plan) |

### Phase 7 — UI/UX plan
Completed. See `Phase-7-UI-UX-Plan.md`. Brand contract frozen from `_crawl/site.css` `:root` + `theme.css` (exact tokens listed §7.1), per-page wireframe notes for all 15 pages + 404 state, prioritised backlog UX-01…UX-18. Validated vs Phases 1–6 (no new brand token required; owners reused; `[PROPOSED]` units stay gated).

| ID | Phase | Issue / observation | Decision | Status |
|----|-------|---------------------|----------|--------|
| I-29 | 7 | 404 responses fall through to the **GitHub Pages default page** (off-brand, no navigation, no link back into the funnel) | UX-10: add a static `404.html` reusing `.page-head` + `.shortcut-grid`; no GH Pages config change needed. | Open |
| I-30 | 7 | `/faq/` filters and the proposed `/what-we-do/` pillar filter use `hidden`/display toggling — if applied at DOM level it would hide answers from crawlers and make `FAQPage` markup unfaithful | UX-06/UX-07 carry a hard acceptance rule: filter **presentation only**, all content stays in the DOM and in schema. | Resolved (guarded in plan) |
| I-31 | 7 | Accessibility assessment is a **static HTML/CSS review** (skip-link, landmarks, `aria-expanded`, 44px targets, `swap`); no axe/Lighthouse/SR run and no field testing was possible here | Phase 7 makes **no WCAG conformance claim**; specific contrast pairs (`--slate-500`, `--text-on-dark-soft`) and focus traps are listed "to verify when work is scheduled". | Open (accepted limit) |
| I-32 | 7 | Chat launcher, consent card and "back to top" all occupy the bottom-right/bottom-left corners; at ≤640px CSS already hides the launcher while consent is showing, but the `to-top` offset (`+62px`) assumes no consent card | Flagged in UX-15 for a stacking/focus-order check; no change made (works in the observed markup). | Open |

### Phase 8 — Full SEO rewrite of existing public pages
Completed. See `Phase-8-SEO-Rewrite.md`. All **15 inventoried public pages** rewritten (14 indexable + `/pitch-deck/` kept `noindex,follow`) with metadata, heading outline, body copy, CTA copy, link changes, JSON-LD and GEO notes; legal pages rewritten **for clarity only** (clause meaning preserved). Every title/description re-measured against the repo's own `emplowise:seo-audit` gate (§8.0a) and every AEO block re-counted (all 40–60 words). **No site file was modified.**

| ID | Phase | Issue / observation | Decision | Status |
|----|-------|---------------------|----------|--------|
| I-33 | 8 | `app/Console/Commands/EmplowiseSeoAudit.php` gates only **13 routes** — `/terms/` and `/privacy/` are **absent from `ROUTES`**, and on those two pages the configured primary keyword does **not** appear in title, H1, H2 or intro (the rule the other 13 must satisfy) | Phase 8 rewrites put the keyword back into both titles and recommends adding the two routes to `ROUTES`. Gate rules now documented in §8.0a and obeyed by every rewritten title/description. | Open (recommendation) |
| I-34 | 8 | The audit's fact-check compares against config literals **"Up to 20 employees" / "Up to 50 employees"**, while the Phase 5 AEO answers (reused verbatim in Phase 8) read "up to 20 **staff**" | Copy harmonised in §8.5 package blocks to the config wording; the reused Phase 5 answer blocks are left as-is so the audit and Phase 5 stay traceable, with this divergence recorded rather than silently edited. | Open (noted) |
| I-35 | 8 | `/portfolio/` claims "**WCAG AA contrast on the documented pairings**" in its own body copy; this audit never ran a contrast or AT check (Phase 7 I-31) | The claim is **the site's own**, not ours. Phase 8 does not repeat it as verified and flags it for a real contrast test before it stays on the page. | Open |
| I-36 | 8 | Phase 8 output is a **document**, not a deployed change: titles/descriptions on the live site and in `config/emplowise.php` are still the Phase 1 values | Explicitly out of scope (task forbade repo edits, commits, pushes). Handoff = apply §8.1–§8.16 into `config/emplowise.php` `seo.*`, then run `php artisan emplowise:seo-audit` + CI. | Open (by design) |

### Final verification & packaging

**Phase ordering log (strictly sequential, each validated against its predecessor before the next began)**
| Order | Phase | Deliverable | Validated against | Result |
|---|---|---|---|---|
| 1 | Live crawl & backup record | `Phase-1-Backup.md` | backup manifest `/data/backups/20261126-shadow/manifest.json`; `ExportStatic.php` page list; `sitemap.xml` | 15 pages + 5 stubs + 404 + API characterised; I-01…I-11 |
| 2 | Deep analysis | `Phase-2-Deep-Analysis.md` | Phase 1 inventory & per-page records | lab-only; I-12…I-16; no contradiction requiring a Phase 1 edit |
| 3 | Competitor gap analysis | `Phase-3-Gap-Analysis.md` | Phase 2 findings, web search sources [1]–[8] | I-17…I-20; unmeasured items kept unmeasured |
| 4 | Page/unit breakdown | `Phase-4-Breakdown.md` | Phases 1–3 + `SiteController.php` config dependencies | I-21…I-22; U-1…U-10 labelled `[PROPOSED]` |
| 5 | SEO / AEO / GEO mapping | `Phase-5-SEO-AEO-GEO-Extraction.md` | Phases 1–4 | I-23…I-25; 11 answers 42–54w, 11 recs 147–178w (re-counted) |
| 6 | 90-day research plan | `Phase-6-Research-Plan.md` | Phases 1–5 issue IDs | I-26…I-28; every task cites an I-nn or U-nn |
| 7 | UI/UX plan | `Phase-7-UI-UX-Plan.md` | Phase 1 §1.7 brand baseline, `_crawl/site.css` `:root`, Phases 2–6 | I-29…I-32; UX-01…UX-18; no new brand token |
| 8 | Full SEO rewrite | `Phase-8-SEO-Rewrite.md` | Phases 1, 2, 4, 5, 6, 7 + `EmplowiseSeoAudit.php` gate | I-33…I-36; 15/15 pages; all metadata re-measured |

**Nine-file manifest (all non-empty, verified with `stat`/`wc`)** — `Phase-1-Backup.md` 25,101 B · `Phase-2-Deep-Analysis.md` 13,529 B · `Phase-3-Gap-Analysis.md` 8,867 B · `Phase-4-Breakdown.md` 11,158 B · `Phase-5-SEO-AEO-GEO-Extraction.md` 21,410 B · `Phase-6-Research-Plan.md` 8,621 B · `Phase-7-UI-UX-Plan.md` 20,786 B · `Phase-8-SEO-Rewrite.md` 55,429 B · `Issues-and-Decisions.md` ~16 KB (grows with this entry). Evidence folder `_crawl/` (15 raw HTML pages + `site.css` + `extract.py` + `extracted.json` + `detailed_dump.txt`) is retained alongside but is **not** part of the nine-document deliverable set.

**Page coverage matrix (inventoried page → phase sections)**
| Page (15) | P1 | P2 | P4 | P5 | P7 | P8 |
|---|---|---|---|---|---|---|
| `/` | §1.3 | §2.2 | ✓ | 5.1 | ✓ | 8.1 |
| `/what-we-are/` | §1.3 | §2.2 | ✓ | 5.2 | ✓ | 8.2 |
| `/what-we-do/` | §1.3 | §2.2 | ✓ | 5.3 | ✓ | 8.3 |
| `/what-we-are-building/` | §1.3 | §2.9 | ✓ | 5.9 | ✓ | 8.4 |
| `/why-emplowise/` | §1.3 | §2.2 | ✓ | 5.4 | ✓ | 8.5 |
| `/free-hr-audit/` | §1.3 | §2.7 | ✓ | 5.5 | ✓ | 8.6 |
| `/faq/` | §1.3, §1.6 | §2.6 | ✓ | 5.6 | ✓ | 8.7 |
| `/contact/` | §1.3 | §2.4 | ✓ | 5.7 | ✓ | 8.8 |
| `/emplostart/` | §1.3 | §2.2 | ✓ | 5.8 | ✓ | 8.9 |
| `/company-profile/` | §1.3 | §2.2 | ✓ | 5.10 | ✓ | 8.10 |
| `/portfolio/` | §1.3 | §2.2 | ✓ | 5.10 | ✓ | 8.11 |
| `/docs/` | §1.3 | §2.2 | ✓ | 5.10 | ✓ | 8.12 |
| `/terms/` | §1.3 | §2.2 | ✓ | 5.11 | ✓ | 8.13 |
| `/privacy/` | §1.3 | §2.2 | ✓ | 5.11 | ✓ | 8.14 |
| `/pitch-deck/` (noindex) | §1.3 | §2.3 | ✓ | §5.0 shared | ✓ | 8.15 |
Coverage: **15 / 15 pages in Phase 7 and Phase 8**; 14 indexable pages in Phase 5 (`pitch-deck` handled under shared entity guidance by design).

**Constraints honoured**
- `/data/emplowise` **unmodified**: `git status --porcelain` returns empty; `HEAD = 89a8e7f`; no commit, no branch, no push performed anywhere.
- Backup sets at `/data/backups/20261126-shadow/` and the private `*-shadow-20261126` repos were **read-only** inputs (manifest cross-checked in Phase 1 §1.1); nothing was pushed to them.
- No fabricated data: field CWV, rankings, backlinks, traffic, AI citations, clients, testimonials, ratings, phone numbers, profile URLs and repository URLs are all recorded as **unavailable**, never invented.
- `[PROPOSED]` units (U-1…U-10) never presented as existing; Phase 6/7/8 keep them gated.

**Packaging** — the nine documents are archived as `Emplowise-Audit-20261126.zip` (documents only; `_crawl/` evidence stays in the workspace and is referenced by path).

