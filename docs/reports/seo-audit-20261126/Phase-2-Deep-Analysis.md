# Phase 2 — Deep Technical & On-Page Analysis
**Emplowise Website Audit · 2026-11-26 · builds directly on Phase 1**

Validated against `Phase-1-Backup.md`. All "lab" numbers are **single-region curl measurements from this
sandbox (edge region `southeastasia`, GitHub `x-cache` HIT)** — not user-real, not field data. **Field Core Web
Vitals, backlink data, and SERP rankings are UNAVAILABLE in this environment** (no Search Console, analytics,
CrUX API, Ahrefs/Moz/Majestic, or headless browser) and are therefore **not reported as metrics**.

## 2.1 Indexing & crawlability
- **Protocol/host:** HTTPS only, HTTP/2, `server: GitHub.com`, HSTS `max-age=31556952` on HTML (and preload via `vercel.json` on the Vercel path). ✔
- **robots.txt:** `Allow: /`, `Disallow: /api/`, valid `Sitemap:` line. Correct — API is inert on static anyway (Phase 1 §1.2).
- **sitemap.xml:** 14 URLs, all HTTP 200, all self-canonical, all indexable. **Accurate** — correctly excludes `pitch-deck` (which is `noindex,follow`). No sitemap↔index mismatch. ✔ (I-01 confirmed as non-issue.)
- **Meta robots:** no stray `noindex` on commercial pages; `noindex,follow` only on legacy stubs + pitch-deck; 404 `noindex`. Clean.
- **Canonical:** 14/14 self-referential with trailing slash; canonical↔sitemap↔internal-link all agree on the trailing-slash form. **No canonical/URL inconsistency detected.** ✔
- **Orphans / depth:** link-graph (indexable sources only) → **no orphan indexable pages**; max inlinks `free-hr-audit` 64, `what-we-are` 57, `index` 55; min `docs` 14, showcase/legal 15. Every page ≤2 clicks from home via header/footer.
- **Pagination / params / faceted URLs:** none (static brochure + one app). Low crawl-complexity site.

## 2.2 Legacy redirects (real finding, I-02)
`routes/web.php` and `vercel.json` declare `/pricing→/why-emplowise`, `/career-hub→/emplostart`,
`/student-hub→/emplostart`, `/ai-automation→/what-we-are-building`, `/team→/what-we-are#team` as **301/308**.
On the **live GitHub Pages deployment** these serve as **HTTP 200 HTML meta-refresh stubs** (verified: `content="0; url=…"` + `robots noindex,follow` + canonical→target). Consequences:
- ✅ No duplicate-content risk (noindex + canonical to target).
- ⚠️ Not a true HTTP redirect → weaker link-equity consolidation, extra byte/round-trip, and crawlers must parse the refresh. **Recommend host-level 301s** (Cloudflare/Vercel/nginx) or, if staying on GH Pages, keep meta-refresh but ensure no inbound links point at legacy URLs.

## 2.3 Security headers (site is unusually strong here)
- CSP `<meta>` on every page: `default-src 'self'`, script-src self + a specific SHA-256 for the inline theme bootstrap, `img-src 'self' data:`, `connect-src 'self' https://api.web3forms.com`, `form-action 'self' https://api.web3forms.com`, `base-uri 'self'`, `object-src 'none'`. Tight & consistent.
- Vercel path adds `X-Frame-Options DENY`, `X-Content-Type-Options nosniff`, `Referrer-Policy strict-origin-when-cross-origin`, `Permissions-Policy` (locks geolocation/mic/camera/payment/usb), HSTS preload. GH Pages serves HTML with `Strict-Transport-Security` (verified) but not the full set — **header parity depends on host** (note for the owner).

## 2.4 Mobile
- `viewport width=device-width, initial-scale=1` on all pages. Responsive via `--shell 1140px` + `clamp()` gutters; responsive logo `srcset`; dark-mode via `data-theme`. Self-hosted preloaded fonts.
- **No AMP, no separate m-dot** — single responsive DOM (correct modern approach).
- **Limitation:** tap-target sizing, font-size legibility, and layout-shift-on-load cannot be confirmed without a device/browser run → **mobile usability = lab-static-assumed, not verified.**

## 2.5 Page weight & performance — LAB PROXIES ONLY (measured)
Single-page home (most requests): 1 stylesheet, 5 deferred JS (theme/app/consent/chat/home), 3 `<img>` + 3 `srcset`, 2 inline scripts. Fonts preloaded.

| Resource | Raw | Transferred (measured) | Notes |
|----------|-----|------------------------|-------|
| HTML `/` | 48,283 B | 48.3 KB | edge-cached |
| `css/site.css` | 143,485 B | **26.6 KB gzip** | single render-blocking stylesheet |
| `js/chat.js` | 24,968 B | 7.6 KB gzip | deferred |
| `js/app.js`/`theme.js`/`consent.js` | ~18.8 KB | gzip ~5–6 KB | deferred |
| fonts Montserrat + Jakarta (woff2) | 37,956 + 27,348 B | 65.3 KB | preloaded, already compressed |
| logo webp 125 / png 375 | 2,106 / 12,837 B | — | responsive srcset used; good |
| favicon.ico | 5,068 B | — | — |

- **TTFB (lab, home, 3 samples):** 67–80 ms; **total** 81–102 ms (from `southeastasia` edge, cache HIT). Not representative of cold/global users.
- **Compression:** GitHub Pages edge serves **gzip** (verified `Content-Encoding: gzip`); **Brotli not offered** → assets ship gzip-only here (Vercel path would add br). CSS/JS are the only text payloads needing it; fine.
- **⚠️ Cache lifetime (real finding):** versioned assets (`?v=1795552040`) return **`cache-control: max-age=600`** on GH Pages — only 10 min for immutable, hash-busted files. The repo's `vercel.json` sets `max-age=86400` for `/css/ /js/ /fonts/ /img/ /downloads/` but **GH Pages ignores it**. **Recommend** `max-age=31536000, immutable` for versioned assets (via a host that honours it, or accept GH Pages default and rely on `?v=`).
- **Render-blocking:** one CSS file (26.6 KB gz) is render-blocking; below ~14 KB inlinable-critical threshold so inlining critical CSS is an option, not urgent.
- **Core Web Vitals:** **NOT MEASURED.** No LCP/INP/CLS field values (no CrUX/GSC) and no lab Lighthouse run in this environment. Do **not** quote CWV numbers. Revisit with PageSpeed Insights / Lighthouse in CI (Phase 6 owner task).

## 2.6 Structured data (entities)
- **Global** on every page: `@graph` with `[Organization, ProfessionalService]` `name="Emplowise HR Services"`, `areaServed=Country(Pakistan)`, `knowsAbout=[14 services]`, `hasOfferCatalog` = 3 `Offer`s (Starter 40000 PKR / Business 75000 / Enterprise Custom) pointing to `…/why-emplowise`. Prices are integers/`"Custom"` — parseable, but note `price:"Custom"` on an Offer is schema-valid yet yields no rich price; acceptable.
- **`/faq/`:** `FAQPage` with **21** `Question`/`acceptedAnswer` — correctly mirrors visible FAQ content. Eligible, validly typed; **no rich-result guarantee claimed** (I-06 honoured).
- **Showcase (`company-profile`,`portfolio`,`pitch-deck`):** `WebPage` + `isPartOf WebSite` + `about ProfessionalService`.
- **Gaps (I-03):** no `author`, `datePublished`, `dateModified` anywhere; no `address`/`geo`/`telephone`/`sameAs` on the Organization; no `BreadcrumbList`; no per-`Service` nodes on `/what-we-do/`; no `WebSite.potentialAction`/SearchAction. Missing `sameAs` + contact fields limit entity/Knowledge-Panel strength. Legal pages have a visible "Last updated 22 Nov 2026" that is **not** expressed as `dateModified`.
- **`url` casing note:** Organization `url` is `https://diocese-trees.github.io/Emplowise-Website-Phase-I` (no trailing slash) while page canonicals carry a trailing slash — trivial self/non-self canonical mismatch inside schema; recommend aligning.

## 2.7 On-page SEO (measured across 14 indexable pages)
- **Titles:** 45–60 chars, **0 >60**, all end `| Emplowise`, all include the page's primary keyword from config. Well-formed; home is the longest at 60 (borderline). ✔
- **Meta descriptions:** 136–155 chars, **0 >160 / 0 too short**, keyword-bearing, each ends with a benefit/CTA ("Book a free audit"). ✔
- **Headings:** every page has **exactly one H1** (14/14) using the config `h1`; logical H2/H3 nesting; no skipped-level sprawl detected. ✔
- **Thin content:** `/what-we-are-building/` 492 words (only page under ~600) — but it's a legitimate pre-launch teaser; `/contact/` 534, `/docs/` 687 (hub, low-text by design). Commercial pages 1,000–1,826 words. `/company-profile/` is the richest (1,826).
- **Keyword placement:** config pairs each page with a primary + 2 secondary keyword; keywords appear in title + H1 + intro + H2s → good topical focus. **These are target keywords, not measured rankings** (no rank data).
- **Images/alt:** standard pages reference 3 logo images, **all with `alt="Emplowise"`; 0 missing alt site-wide**. Pitch-deck carries 19 slide images, also all alts present. No hero/photographic content images (brand is text/illustration-led). ✔
- **OG / social (I-05):** full OG + Twitter cards on all pages, but `og:image`/`twitter:image` are the **same generic `logo-primary.png`** everywhere and `og:image` points at the 56 KB PNG. No `og:locale`, no `article:*`, no page-specific preview → weak share previews. `twitter:site`/`twitter:creator` absent (consistent with placeholder socials).
- **International/localisation:** single language `en`, Pakistan as market, **no `hreflang`** (not needed for one-language site; would matter if Urdu edition added). Currency shown as PKR text, not machine `priceRange`/`currenciesAccepted` on LocalBusiness.

## 2.8 Content quality & E-E-A-T
- **Trust signals (strong, unusual for a small site):** repeated "confirmed in writing after your Free HR Audit" disclosures instead of invented metrics; explicit "no published client case studies yet, and this page does not invent any"; "We do not publish invented percentages, savings, or client names"; "Voluntary alignment only. This is not a UN endorsement." Honest, low-risk copy — **positive for E-E-A-T**.
- **Named authors/People:** `/what-we-are/` names 3 real people with roles + credentials (config-sourced). **But** they are not wired to schema `author`/`founder`/`sameAs`, and portraits are initials placeholders → authorship is asserted visually, not machine-readable.
- **Freshness:** only legal pages show an explicit date (22 Nov 2026); site-wide `© 2026`; no `dateModified` → crawlers can't see update cadence despite `changefreq weekly` in sitemap.
- **Experience:** founder-origin story present; no testimonials/reviews (deliberate, per policy) — fine ethically, limits "social proof" SERP assets (can't be fabricated).

## 2.9 Links & authority
- **Internal:** healthy, hub-and-spoke (home ↔ free-hr-audit ↔ what-we-do); descriptive anchor text ("See the confirmed services", "Why Emplowise publishes HR pricing by headcount"). Only `/contact/` + `/emplostart/` use generic anchors for a few CTAs ("Open EmploStart"). No broken internal targets found among the 14 (+ stubs resolve).
- **External:** 4 outbound (answer-engine prompt deep-links on `/contact/`) + EmploStart product link. All same-organisation or answer engines → **no authoritative third-party citations** and **no `rel="sponsored"/"nofollow"` needed** (none are endorsements). No inbound-backlink data (unavailable).

## 2.10 Keyword / intent assessment (targets, NOT rankings)
Derived from `config/emplowise.php` primary/secondary keywords + visible copy:
| Page | Primary target | Intent | Note |
|------|----------------|--------|------|
| `/` | remote HR services in Pakistan | commercial | head term, well focused |
| `/what-we-are/` | HR outsourcing company in Pakistan | commercial/brand | doubles as about |
| `/what-we-do/` | HR operations outsourcing | commercial | service page |
| `/why-emplowise/` | why Emplowise / HR outsourcing pricing in Pakistan | commercial-comparison | pricing + why |
| `/free-hr-audit/` | free HR audit in Pakistan | lead-gen | highest in-degree (64) |
| `/emplostart/` | free ATS resume checker | informational→tool | different audience |
| `/what-we-are-building/` | AI automation for HR | informational | thin, pre-launch |
| `/faq/` | HR outsourcing questions | informational | 21 Q, AEO surface |
Legal/showcase/docs = navigational + brand-modifier. **No keyword-stuffing detected; no cannibalisation among pages** (each owns a distinct head term). **Actual rank/CTR/volume = unavailable** (no keyword tool).

## 2.11 Prioritised technical findings (feeds Phase 3 gaps + Phase 8)
**P0 (correctness/trust, cheap):**
- Add `dateModified` (and legal `datePublished`) to schema to match visible "Last updated"; align Organization `url` trailing slash. (I-03)
- Set long-lived `immutable` cache on versioned assets if moving hosts; else document GH Pages 600s limit. (§2.5)

**P1 (entity/AEO/GEO upside):**
- Add truthful `sameAs` **only once real profiles exist** (currently placeholders) + `address`/`areaServed`/`telephone` to Organization. (I-04)
- Add `BreadcrumbList`; consider per-`Service` nodes on `/what-we-do/`. (§2.6)
- Page-specific OG images (brand-consistent, no stock). (I-05)
- Host-level 301s for legacy URLs. (I-02)

**P2 (performance/content):**
- Optionally inline critical CSS; consider Brotli-capable host.
- `/what-we-are-building/` thin (492w) — acceptable as teaser; enrich when AI division ships.

## 2.12 Explicit measurement limits (no fabrication)
Unavailable, therefore **not asserted**: field CWV (CrUX/GSC), lab Lighthouse scores, keyword rankings/volumes/CTR, backlink/referring-domain counts, traffic/conversions, AI-engine citation presence (Phase 3). Only curl-measured lab proxies are cited, tagged as such.

## 2.13 Validation vs Phase 1
Confirms all Phase 1 issues with lab evidence (I-01 non-issue; I-02 measured meta-refresh; I-03/04/05 verified site-wide; I-06 FAQPage valid; I-10 web3forms connect-src in CSP). **No contradiction found** that requires editing Phase 1; Phase 1 remains authoritative for inventory, Phase 2 adds analysis.
