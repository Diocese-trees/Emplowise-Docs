# Phase 6 — 90-Day SEO / AEO / GEO Research & Action Plan
**Emplowise Website Audit · 2026-11-26 · builds on Phases 1–5**

Owners map to the three **real, config-sourced** people plus a web developer/agency; no invented staff.
Because **no analytics / GSC / keyword tool / rank tracker is connected today** (Phase 2 I-15), the first
workstream is *instrumentation* — every measured goal in this plan depends on it. Frequencies are cadence;
**triggers** are the events that fire a recurring task. **No forecasts, no invented traffic targets** — success
measures are stated as *what to instrument & what "good" directionally looks like*, not numeric predictions.

## 6.0 Roles
- **AH — Abdul Hadi** (Co-Founder, *Content Strategist & Strategic Marketer* per config) → content, SEO/GEO, directories.
- **SN — Samarah Nabil** (Co-Founder, *Senior HR Business Manager & Analyst*) → factual HR accuracy, service/scope claims, compliance copy sign-off.
- **MA — Muhammad Ali** (Advisor, governance) → approvals, entity/legal data, budget.
- **DEV** (web developer / agency owning `Emplowise-Website-Phase-I` + EmploStart) → schema, performance, deploy, hosts/redirects.

## 6.1 Phase 0–30 days — Instrument & fix correctness (P0)
| # | Task | Tool | Owner | Freq | Trigger | Success measure (instrument) |
|---|------|------|-------|------|---------|------------------------------|
| 1 | Connect **Search Console** + submit `sitemap.xml`; verify **Bing Webmaster** | GSC, Bing | AH (+DEV) | once, then weekly watch | after any new page | coverage report clean; 0 index errors |
| 2 | Add **GA4** behind existing consent (respects "off until opt-in") | GA4, Consent Mode | DEV | once | deploy | events fire only on consent |
| 3 | Wire `dateModified` (real), align Organization `url` slash, add `BreadcrumbList` (Phase 5 §5.x) | Laravel `layouts/app.blade.php`, Rich Results Test | DEV | per change | deploy | validator shows 0 errors |
| 4 | Fix/clarify footer **Socials** placeholders (I-04/I-25): link real profiles or drop the heading | GitHub repo | AH+DEV | once | profiles ready or not | no `href="#"` links live |
| 5 | Host-level **301s** for legacy URLs (I-02) via a redirect-capable edge/CDN | Cloudflare / Vercel / nginx | DEV | once | if leaving GH Pages | legacy URLs 301→target, not 200-stub |
| 6 | Long-lived **immutable** caching on `?v=` assets (I-12) | CDN/edge config | DEV | once | host move | `max-age≥31536000, immutable` |
| 7 | Baseline **Lighthouse CI** (mobile) in GitHub Actions — *fills the CWV gap* | Lighthouse CI, GitHub Actions | DEV | weekly + on PR | every merge | lab scores trended over time |
| 8 | Truthful **`Person`** schema on `what-we-are` (real roles, no placeholder photos) | blade + SR Test | DEV, SN verifies roles | once | role change | entity present, no fake `image` |

## 6.2 Phase 31–60 days — Amplify AEO/GEO (P1, highest-leverage differentiators)
| # | Task | Tool | Owner | Freq | Trigger | Success measure |
|---|------|------|-------|------|---------|-----------------|
| 9 | Publish the **home/why/contact AEO answers** from Phase 5 verbatim as on-page definition blocks | repo `config/emplowise.php` | AH drafts, SN fact-checks | per page | Phase 8 merge | each page has a standalone 40–60w answer |
| 10 | Keep the 3 **PKR prices** identical across visible copy, `Offer` schema, and `/contact/` engine prompts | `config/emplowise.php`, manual diff | AH+DEV | monthly + on change | any price edit | 3-way consistency check passes |
| 11 | Manual **GEO audit**: ask ChatGPT/Claude/Gemini/Perplexity the 6 brand questions; log how Emplowise is described | the 4 engines + a query log sheet | AH | fortnightly | new content / quarterly | answers match published facts; note citation presence (**measured, not assumed**) |
| 12 | Add `[PROPOSED]` **guides hub + 2–3 factual guides** ("HR policies for Pakistani startups", "payroll compliance Pakistan") | repo + `config` | AH writes, SN reviews, DEV ships | 2/month cadence | topic approved | pages indexable, `Article` schema, no invented stats |
| 13 | Add `WebApplication` (EmploStart) + `Service` (free audit) schema (Phase 5 §5.5/5.8) | blade, SR Test | DEV | once | deploy | valid; **no rating/aggregate** |
| 14 | **Directory/citation outreach** (G-2): legitimate listings on Manifest/Clutch/PK HR (no fake reviews) | outreach sheet | AH, MA approves | batch | profile data ready | listing live; NAP consistent |
| 15 | `sameAs` **only if real owned profiles exist**; else keep withheld (I-23) | blade | AH+MA | on demand | profiles launched | schema `sameAs` → verified URLs only |

## 6.3 Phase 61–90 days — Deepen & sustain
| # | Task | Tool | Owner | Freq | Trigger | Success measure |
|---|------|------|-------|------|---------|-----------------|
| 16 | Evaluate `[PROPOSED]` **per-service pages** (U-3) from `/what-we-do/` for top 5 search-demand services | GSC queries + keyword tool (Ahrefs/Semrush/GKP) | AH+DEV | one-off decision | data available in GSC | decide split; no cannibalisation |
| 17 | Refresh `/what-we-are-building/` thin page when AI modules change status | repo | SN+AH | on milestone | module ships | add real `SoftwareApplication` only when genuinely available |
| 18 | Add `dateModified` maintenance to the **content-editing workflow** (`CONTENT_EDITING_GUIDE.md`) | docs + PR checklist | DEV | every content PR | any copy change | no page ships without a real date if date-bearing |
| 19 | **Case-study gate**: publish client results **only once cleared in writing** (U-6); no premature `Review` schema | repo + client sign-off | MA approves, SN facts | as won | written clearance | first verified case study; honest until then |
| 20 | Quarterly **full re-crawl** (this audit's crawler) to catch new orphans/canonical drift | provided `_crawl/extract.py` | AH+DEV | quarterly | post-redesign | 14 indexable pages intact, sitemap matches |
| 21 | **CWV field check** once 28 days of CrUX data accrue post-indexing | PageSpeed Insights, CrUX | AH | monthly from here | data available | real field LCP/INP/CLS replace lab proxies |

## 6.4 Standing cadences (recurring)
- **Weekly (AH):** GSC coverage + query watch; log new impressions on `[PROPOSED]` guides.
- **Fortnightly (AH):** GEO audit (§6.2 #11) — record whether the 4 engines describe Emplowise correctly; cite-presence is *observed*, never predicted.
- **Monthly (DEV):** Lighthouse CI trend; asset cache + redirect health; web3forms submission sanity (I-10).
- **Monthly (AH+DEV):** price-consistency 3-way diff (#10).
- **Quarterly (all):** re-crawl + entity/schema review; decide the next `[PROPOSED]` unit batch.

## 6.5 Trigger catalogue
| Trigger event | Fire these tasks |
|---------------|------------------|
| Any deploy / PR merge | Lighthouse CI (#7), schema validate (#3,13) |
| Price or package change | 3-way price consistency (#10), Offer schema, engine prompts |
| Real social profile created | add `sameAs` (#15), fix footer (#4) |
| Client signs off a case study | publish case study + `Review` *only then* (#19) |
| AI module status changes | update `/what-we-are-building/` + `SoftwareApplication` (#17) |
| New guide published | AEO answer block (#9), `Article` schema, internal links (#12) |
| 28 days post-index | switch CWV from lab proxies to field data (#21) |

## 6.6 Measurement gaps this plan closes (and honest limits)
- **Now measurable after setup:** CWV (Lighthouse lab now, CrUX field after #21), impressions/CTR (GSC), conversions (GA4 + web3forms), rankings (GSC queries / optional rank tracker), backlinks (GSC links report / optional Ahrefs).
- **Still unverifiable at plan time (do NOT fabricate):** current rank positions, competitor share-of-voice, whether any AI engine already cites Emplowise (#11 measures it going forward), historical traffic. These were **unavailable in Phases 2–3** and remain so until tools connect — the plan sequences their collection rather than inventing values.
- **Tooling stack:** GSC + Bing + GA4 (consent-gated) + Lighthouse CI + this crawler + a keyword/rank tool + the 4 answer engines for GEO. Budget approval via MA.

## 6.7 Validation vs Phases 1–5
Every task traces upstream: correctness items → Phase 2 P0; AEO/GEO blocks → Phase 5 §5.x + Phase 1 §1.3 (contact prompts); guides/service-pages/case-studies/directories → Phase 3 gaps G-1/G-2/G-3 + Phase 4 U-1/U-3/U-6/U-10; owner roles → Phase 1 config (real people); instrumentation-first → Phase 2 I-15. **No contradiction.** Sequencing respects truthfulness rules (case study, `sameAs`, ratings all *gated on real data*).
