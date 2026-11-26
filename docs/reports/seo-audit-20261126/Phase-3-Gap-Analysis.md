# Phase 3 — Organic Competitor & Gap Analysis
**Emplowise Website Audit · 2026-11-26 · builds on Phases 1–2**

## 3.0 Method + honesty constraints
Five **relevant organic competitors** were identified by **web search** of the exact niche Emplowise targets —
*outsourced / managed remote HR for startups & SMEs in Pakistan* — plus the adjacent *free ATS career-tools*
space (EmploStart). For each, I attempted a live fetch to capture real title/H1/structure. **I do NOT claim these
are "the top five" ranking positions** (no rank/visibility tool available — see Phase 2 I-15), and **I do NOT
claim AI/answer-engine citation data** (not measured). Gaps are prioritised by **qualitative impact**, not
invented traffic/lead forecasts. Sources cited at §3.6.

## 3.1 Competitor profiles (evidence-based)

**C1 — Scaleup Connect (OneHR)** · `scaleupconnect.com` — live fetch HTTP 200 [2]
- Site title/H1 (verified): *"Scaleup Connect | Hire Now, Pay Later Recruitment."* A search-surfaced Facebook
  promo describes an "All-in-One HR Outsourcing Solution…for Startups, SMEs, and Growing Businesses…from **50,000
  PKR/month**" [1]; the guessed `/onehr` page **404'd** at check, so the "from PKR" figure is **from a social
  post, not a verified indexable product page** — flagged, not asserted as their published price.
- Most direct positioning overlap (startups/SMEs, all-in-one HR).

**C2 — Core Bhive** · `corebhive.com/hr-services/` — HTTP 200 [3]
- Verified title: *"HR Outsourcing & Payroll for SMEs in Lahore | Core Bhive."* H1: *"Your HR Team, Without the
  Overhead."* Full-cycle (recruitment, payroll, performance). Lab scan: 1 JSON-LD block, 5 H2, **~561 words**, `/blog` present, "ATS" mentioned.

**C3 — TRG HR** · `trg-hr.com/hr-outsourcing-services` — HTTP 200 [4]
- Verified title: *"HR Outsourcing Services in Pakistan | Trg HR"* with a meta description (payroll, recruitment,
  HR administration, employee management). H1: *"Best HR Outsourcing Services In Pakistan."* Lab scan: **2 JSON-LD
  blocks, 8 H2, ~2,312 words** (deepest page measured), no blog link on-page.

**C4 — ProHR Xpert** · `prohrxpert.com/…hire-pay-solutions…` — HTTP 200 [5]
- Title/H1: *"Hire & Pay Solutions in Pakistan: How ProHR Xpert Simplifies Global Workforce Management."*
  EOR / Hire-&-Pay angle (legal employer-of-record), broader than pure HR ops. Lab scan: **0 JSON-LD**, 12 H2, ~700 words, `/blog`.

**C5 — Xpezia Global** · `xpezia.com.pk/services/hr/` — **HTTP 403 (Cloudflare "Just a moment")** [6]
- Surfaced as *"Strategic HR Consultancy for Startups & Tech Teams…design HR systems, performance strategies,
  leadership coaching to scale teams."* **On-page NOT verified** (bot-blocked) → positioning taken only from the
  search snippet; treated as lower-confidence.

**Discovery-layer context (not direct competitors but where buyers compare):** The Manifest *"Best HR Outsourcing
Companies in Pakistan"* and Clutch *"Top PEO Firms in Pakistan"* list Assistring, HR Business Solutions, BCCI
Consulting, Grasp Solutions, Premier BPO, Netpace, Taraki, etc. [7][8] — Emplowise does not currently appear in
these third-party comparison lists (its own `/portfolio/` says no client case studies yet).

## 3.2 Side-by-side on-page comparison (measured lab data only)

| Signal | Emplowise (Phase 1–2) | Scaleup | Core Bhive | TRG HR | ProHR Xpert | Xpezia |
|--------|-----------------------|---------|------------|--------|-------------|--------|
| Public PKR price on page | ✅ **PKR 40,000 / 75,000 / Custom** | "from 50k" on social only | ❌ not on `/hr-services` | ❌ not captured | ❌ | n/a (blocked) |
| JSON-LD | ✅ org+offers **21-item FAQPage** per-page | n/c | 1 block | 2 blocks | 0 | n/a |
| Deeper content pages | ✅ 1,000–1,826w (14 pages) | n/c | ~561w (this pg) | ~2,312w (this pg) | ~700w | n/a |
| Free candidate tool | ✅ **EmploStart** (6 modules, 14 prompts, in-browser, no account) | ❌ | "ATS" mention only | "ATS" mention only | ❌ | n/a |
| AI/answer-engine affordance | ✅ **prefilled ChatGPT/Claude/Gemini/Perplexity prompts** on `/contact/` | ❌ | ❌ | ❌ | ❌ | n/a |
| Blog / resources hub | Docs hub (brand/commercial/eng) | n/c | ✅ `/blog` | ❌ (this pg) | ✅ `/blog` | n/a |
| Honest no-results disclosure | ✅ explicit | ❌ (uses testimonials/claims) | — | — | — | n/a |

Legend: ✅ present/verified · ❌ verified absent on checked page · n/c not checked · n/a blocked/na.

## 3.3 What competitors do that Emplowise could adopt (gaps → opportunity)

- **G-1 Content marketing / blog cadence.** Core Bhive, ProHR Xpert, Osynix maintain `/blog` hubs; TRG HR runs a
  "Top 5 Payroll Companies" listicle. Emplowise has a strong Docs/showcase hub but **no regularly-published advice
  blog** targeting informational queries (e.g., "HR policies for Pakistani startups", "payroll compliance
  Pakistan"). Impact: **High** — informational top-of-funnel + internal-link equity + AEO/GEO citability. Risk-free
  to add (fits their "confirmed facts only" voice if sourced carefully).
- **G-2 Third-party comparison presence.** Absent from The Manifest / Clutch / PK HR directories [7][8]. Impact:
  **Medium** — buyer-research surface + referral + credible citations (Google "about the author/entity" surface).
  Action is outreach/listing, not on-site content (no fabricated reviews).
- **G-3 Machine-readable local/geo signals.** Several competitors lean on city ("Lahore", "Pakistan") in title/H1.
  Emplowise targets Pakistan nationally but has **no `address`/`geo`/`areaServed` beyond a Country node, no
  `LocalBusiness`/`Service` schema, no city pages.** Impact: **Medium** for local intent ("HR outsourcing Lahore/
  Karachi") — but note Emplowise is deliberately *remote*, so this is a strategic choice, not a pure defect.
- **G-4 Richer structured data.** TRG HR ships 2 JSON-LD blocks; ProHR/Osynix ship 0. Emplowise already beats the
  weak ones and adds FAQPage — remaining upside is `Service`, `BreadcrumbList`, `WebSite`, `dateModified`
  (ties to Phase 2 I-14). Impact: **Low–Medium**.

## 3.4 Where Emplowise is already differentiated (keep / amplify)
- **D-1 Published transparent pricing** (PKR 40,000 / 75,000 by headcount) — rare; most competitors gate it. Strong AEO/GEO extractable fact.
- **D-2 EmploStart free career app** — no verified competitor offers a genuinely free, in-browser, no-account ATS/pivot tool; this is a unique moat and audience-builder (SDG-aligned, honestly labelled voluntary).
- **D-3 Explicit anti-hype trust copy** ("no invented percentages/results/client names") — differentiates on credibility vs competitors leaning on testimonials; well-suited to AI answer engines that value verifiable claims.
- **D-4 Native AI/answer-engine framing** — prefilled prompts to ChatGPT/Claude/Gemini/Perplexity; ahead of all checked competitors on **GEO readiness**.

## 3.5 Gap prioritisation (qualitative impact × effort; no invented forecasts)
| Rank | Gap | Impact | Effort | Phase that fixes |
|------|-----|--------|--------|------------------|
| 1 | G-1 advice blog + AEO citable content | High | Med | Phase 5/6/8 (content plan) |
| 2 | D-4/D-1 amplify GEO + published pricing in structured data | High | Low | Phase 5/8 |
| 3 | G-2 directory/citation presence | Medium | Low (outreach) | Phase 6 |
| 4 | G-3 geo/`Service`/`LocalBusiness` signals (if pursuing local intent) | Medium | Med | Phase 5/8 |
| 5 | I-14 `BreadcrumbList`/`dateModified`/schema completeness | Low–Med | Low | Phase 8 |
| 6 | G-4 structured-data depth | Low | Low | Phase 8 |

## 3.6 Sources
[1] Facebook post snippet (Scaleup Connect OneHR, "from 50000 PKR/month") via web search — social, unverified page.
[2] scaleupconnect.com (live fetch, HTTP 200, 2026-11-26).
[3] corebhive.com/hr-services/ (live fetch, HTTP 200).
[4] trg-hr.com/hr-outsourcing-services (live fetch, HTTP 200).
[5] prohrxpert.com Hire & Pay solutions article (live fetch, HTTP 200).
[6] xpezia.com.pk/services/hr/ (web search; live fetch returned HTTP 403 Cloudflare — **on-page unverified**).
[7] themanifest.com/pk/hr/outsourcing/services · [8] clutch.co/pk/hr/peo (comparison directories via web search).

## 3.7 Validation vs Phase 2 + limits
Gaps G-2/G-3/G-4 and differentiators D-1/D-3/D-4 map to Phase 2 sections (2.6 entity gaps, 2.8 E-E-A-T, 2.10 keywords) —
**consistent, no contradiction.** **Explicit limits:** competitor rankings, share-of-voice, backlink/DR, traffic, and
whether any competitor (or Emplowise) is cited by AI answer engines are **NOT measured** here — no SEO data platform
or live AI-engine query harness was available; only live page fetches + web-search snippets were used. Xpezia is
lower-confidence (403). Scaleup Connect's "from PKR" price is a social-post reference, not a verified indexable page.
