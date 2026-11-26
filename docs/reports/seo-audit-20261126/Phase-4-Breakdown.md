# Phase 4 — Page & Content-Unit Breakdown
**Emplowise Website Audit · 2026-11-26 · builds on Phases 1–3**

Every **existing** public page is decomposed to atomic units (purpose, intent, observable performance,
update cadence, dependencies, metrics-to-instrument). **"Performance" shows only what is observable without
analytics/GSC** (word count, in-degree, robots, metadata from Phase 1–2); traffic/rank/CTR/conversions are
**UNAVAILABLE** and listed as *metrics to instrument*, not values. **§4.4 lists proposed NEW unit types, each
labelled `[PROPOSED]`** — none exist today.

Source of truth for structure: `app/Http/Controllers/SiteController.php`, `routes/web.php`,
`app/Console/Commands/ExportStatic.php` (confirms export builds exactly **15 pages + 5 redirect stubs** — matches
Phase 1), and `config/emplowise.php` (16 SEO entries, 14 services, 3 packages, 21 FAQs, 6 EmploStart modules,
8 docs entries, 3 audiences, 4 values, 4 method stages).

## 4.1 Shared atomic units (rendered on every page — not "pages")
| Unit | Type | Depends on | Notes |
|------|------|-----------|-------|
| `<head>` SEO block | layout | `layouts/app.blade.php`, `seo.*`, `packages`, `services`, `brand` | title/desc/canonical/OG/Twitter/JSON-LD; single render-blocking `site.css` |
| Header nav | partial | `partials/header`, `copy.layout` | 9 items + logo + Free-HR-Audit CTA + theme toggle |
| Footer | partial | `partials/footer`, `copy.layout`, `brand` | Company/Resources/Socials columns; socials are `#` (I-04) |
| Chat widget ("Emplowise assistant") | partial | `partials/chat`, `js/chat.js` | client-side only; API inert on static (I-10) |
| Cookie/consent | partial | `partials/consent`, `js/consent.js` | "Cookies, kept light"; analytics/marketing off by default |
| Global JSON-LD (Org+Service+Offers) | layout | `brand`, `packages`, `services` | present on all 15 |
| **Team section** `#team` | section (not page) | `partials/team-showcase`, `seo.team`, `copy.team`, `js/team.js` | lives only on `/what-we-are/` (I-11) |
| **Social-links** block | section | `partials/social-links` | only on `/contact/` |

## 4.2 Existing pages — atomic breakdown

**`/` home** — `[existing]`
- Purpose: orient + route to 4 doors; capture Free-HR-Audit leads. Intent: **commercial / navigational hub**.
- Observable: 665 words, in-degree 55, 1 H1, title 60, desc 136. Sections: hero → delivery → stats(14/4/6) → 4 doors → 3 pillars → audit CTA.
- Depends: `seo.home`, `copy.home`, `brand`, `pillars`, `methodology`, `packages`, `student.prompts`; `js/home.js`.
- Update cadence: hero/pillars with offer changes (was `changefreq weekly`). Metrics to instrument: CTA CTR→audit, scroll depth, door-card clicks.

**`/what-we-are/`** — `[existing]` (doubles as About + Team + Audiences)
- Purpose: E-E-A-T, positioning, named team, audience segmentation. Intent: **commercial/brand + trust**.
- Observable: 1,020 words, in-degree 57, richest H-structure (1·8·10). Contains the only `#team` unit.
- Depends: `seo.what-we-are`, `mission`, `values`, `positioning`, `pending_inputs`, `copy.team`, `seo.team`; `partials.team-showcase`, `js/team.js`.
- Metrics: team-section engagement, "pending/confirmed" trust reads. Note: 4 real named people, portraits are placeholders (I-08).

**`/what-we-do/`** — `[existing]` (service catalogue)
- Purpose: detail 14 services / 3 pillars / 4-stage method; qualify fit. Intent: **commercial (service)**.
- Observable: 1,250 words, in-degree 36. No page-specific JS.
- Depends: `seo.what-we-do`, `pillars`, `services` (grouped by pillar), `methodology`, `outcomes`, `outcomes_note`.
- `[PROPOSED]` split: per-service detail pages (§4.4 U-3) would each become their own atomic unit targeting long-tail ("payroll outsourcing Pakistan"). Metrics to instrument if split: per-service entry, conversions by service.

**`/why-emplowise/`** — `[existing]` (pricing + why + comparison)
- Purpose: justify price, publish tiers, reduce pre-sales friction. Intent: **commercial-comparison / decision**.
- Observable: 1,109 words, in-degree 34, explicit pricing table.
- Depends: `seo.why-emplowise`, `packages`, `pricing_notes`, `services`.
- Metrics: price-table engagement, "Request a quote" vs "Book audit" ratio.

**`/free-hr-audit/`** — `[existing]` (primary conversion funnel — highest in-degree 64)
- Purpose: capture qualified leads via 4-step form (21 inputs + 2 selects). Intent: **transactional (lead gen)**.
- Observable: 721 words. Posts to `api.web3forms.com` (I-10).
- Depends: `seo.free-hr-audit`, `copy.free-hr-audit`, `packages`; `js/audit.js`; headcount bands, pain options, slots (controller-injected).
- Metrics: **form start/complete rate, drop-off per step, submissions/week** — all instrument-need (no analytics today).

**`/faq/`** — `[existing]` (21 Q + FAQPage schema)
- Purpose: answer objections; AEO surface. Intent: **informational → commercial assist**.
- Observable: 1,065 words, in-degree 18, FAQPage JSON-LD (21 Q). Sections: HR questions / Pricing / Audit / EmploStart / assistant.
- Depends: `seo.faq`, `faqs` (5 groups), `faq_note`; `js/faq.js`.
- Metrics: impressions/CTR on FAQ rich results (**cannot be promised** — I-06), per-question expand rate.

**`/contact/`** — `[existing]`
- Purpose: multi-channel contact incl. GEO answer-engine prompts. Intent: **transactional/navigational**.
- Observable: 534 words, only page with 4 external links. Sections incl. "Ask your favourite GPT".
- Depends: `seo.contact`, `copy.contact`; `partials.social-links`. Metrics: email clicks, AI-prompt clicks, audit referrals.

**`/emplostart/`** — `[existing]` (launcher → external product)
- Purpose: market the free career app; serve career-seeker audience. Intent: **informational/tool + audience builder**.
- Observable: 1,120 words, 6 modules + 14 prompts. Links out to product (`diocese-trees.github.io/EmploStart/`).
- Depends: `seo.emplostart`, `emplostart_url`, `emplostart_modules`, `fair_jobs_pledge`. Metrics: app-launch clicks (cross-domain), module engagement.

**`/what-we-are-building/`** — `[existing]` (AI division, pre-launch)
- Purpose: signal roadmap honestly. Intent: **informational / brand**. Thinnest (492 words, §2.7).
- Depends: `seo.what-we-are-building`, `copy`. No JS.
- Metrics: newsletter/waitlist interest (currently explicitly "no waitlist"). `[PROPOSED]` enrich when modules ship (G-1/§3.3).

**`/company-profile/`, `/portfolio/`, `/pitch-deck/`, `/docs/`** — `[existing]` showcase/hub
- Purpose: B2B proof + downloadable Office assets. Intent: **navigational / brand-proof / enablement**.
- Observable: 1,826 / 1,544 / 903 / 687 words; docs has most internal links (41, hub role); pitch-deck `noindex` (19 imgs); company-profile & portfolio explicit `index,follow`.
- Depends: `seo.*`, `showcase_pages.*`, `docs_index` (8 entries), `brand`; `deck.js` (pitch-deck); each `@push head/styles`. Downloads = `public/downloads/*-2026.{docx,pptx}`.
- Metrics: download click-throughs, deck views; portfolio = repo-proof, **no client case studies (policy)** → limits "review"/case-study schema.

**`/terms/`, `/privacy/`** — `[existing]` legal
- Purpose: compliance + trust. Intent: **navigational/legal**. Have visible "Last updated 22 Nov 2026" (only dated pages).
- Depends: `seo.terms/privacy`, `copy.legal.terms/privacy`. No JS.
- `[NOTE]` Phase 8 must **preserve substantive meaning** (rewrite copy, not terms). `dateModified` not yet in schema (I-14).

## 4.3 Performance summary (observable-only)
| Page | Words | In-deg | robots | Primary intent | Conversion role |
|------|------:|-------:|--------|----------------|-----------------|
| / | 665 | 55 | index | hub | →audit (primary) |
| /free-hr-audit/ | 721 | **64** | index | transactional | **form** |
| /what-we-are/ | 1020 | 57 | index | trust | →audit/pricing |
| /what-we-do/ | 1250 | 36 | index | service | →audit |
| /why-emplowise/ | 1109 | 34 | index | comparison | →quote/audit |
| /emplostart/ | 1120 | 34 | index | tool | →product app |
| /contact/ | 534 | 34 | index | contact | →email/GEO/audit |
| /what-we-are-building/ | 492 | 29 | index | brand/info | →services |
| /faq/ | 1065 | 18 | index | info | →audit/app |
| /company-profile/ | 1826 | 15 | index,follow | proof | →download/audit |
| /portfolio/ | 1544 | 15 | index,follow | proof | →audit |
| /docs/ | 687 | 14 | index | hub | →download |
| /pitch-deck/ | 903 | 15 | **noindex,follow** | proof | →download |
| /terms/ /privacy/ | 816/858 | 15/15 | index | legal | — |

*(rank / CTR / traffic / conversion values NOT AVAILABLE — no analytics/GSC; instrument in Phase 6.)*

## 4.4 Proposed NEW content-unit types — all `[PROPOSED]`, none currently exist
Derived from Phase 3 gaps (G-1 blog, G-2 directories, G-3 geo/service) + §4.2 split notes.
| ID | Unit | Why / gap | Intent | Truthfulness guard |
|----|------|-----------|--------|--------------------|
| U-1 | `[PROPOSED]` Advice **blog/article** hub (`/guides/` or `/blog/`) | G-1: no informational content | informational → AEO citable | only Pakistan HR facts the team can verify; no invented data |
| U-2 | `[PROPOSED]` **Individual guide/article** units (e.g., "HR policies for Pakistani startups") | G-1, SEO/AEO long-tail | informational | cite law sources; `dateModified` real |
| U-3 | `[PROPOSED]` **Service-detail page per each of 14 services** | §4.2 `/what-we-do/` split; targets long-tail commercial | transactional | scope "confirmed after audit"; no fake results |
| U-4 | `[PROPOSED]` **Comparison / alternative pages** ("Emplowise vs hiring in-house", vs enterprise consultancy) | D-1 pricing advantage | commercial-comparison | no disparaging/defamatory claims; competitor facts must be cited |
| U-5 | `[PROPOSED]` **City/geo landing** (Lahore/Karachi/Islamabad "remote HR") — only if pursuing local intent | G-3 | local commercial | must be honest: delivery is remote; no fake local office/address |
| U-6 | `[PROPOSED]` **Case-study units** | portfolio lacks them (policy) | trust/conversion | **only once cleared in writing** — currently forbidden to invent |
| U-7 | `[PROPOSED]` **Author profile pages** (`/team/{name}` or About anchors) → wire `Person`/`author`+`sameAs` | I-03, E-E-A-T | trust | real people; `sameAs` only if profiles exist |
| U-8 | `[PROPOSED]` **Glossary / definitions** ("HR outsourcing", "ATS score") | AEO/GEO extractable | informational | reuse FAQ/config copy |
| U-9 | `[PROPOSED]` **Lead-magnet resource** gated by Free-HR-Audit gap-list | conversion | lead gen | deliverable must actually exist |
| U-10 | `[PROPOSED]` **Directory/citation listings** (Manifest, Clutch, PK HR) | G-2 | off-site authority | legitimate listings; no fake reviews |

## 4.5 Validation vs Phases 1–3
Page set / dependencies / counts reconcile exactly with Phase 1 inventory and `ExportStatic.php` (15 pages + 5
stubs). Intent labels match Phase 2 §2.10. Proposed units trace to Phase 3 gaps G-1→U-1/U-2, G-3→U-5,
G-2→U-10, and Phase 2 entity gaps I-03/I-14→U-7/U-3. **No contradiction.** Every `[PROPOSED]` carries a truthfulness guard so Phase 8 stays honest.
