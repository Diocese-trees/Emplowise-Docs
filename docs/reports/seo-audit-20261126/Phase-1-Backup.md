# Phase 1 — Live Crawl & Backup Record
**Emplowise Website Audit · 2026-11-26**

Live subject: `https://diocese-trees.github.io/Emplowise-Website-Phase-I/`
Local website source: `/data/emplowise` (Laravel, HEAD `89a8e7f` = live). Docs: `/data/emplowise/_staging/Emplowise-Docs`. Product: `/data/emplowise/_staging/EmploStart`.

> **Granularity note:** this document stores the full granular per-page record (metadata, complete
> H1–H3, canonical/robots, OG, JSON-LD, every distinct internal-link target with anchor text, image
> alts, CTA inventory, entities, and full body text). The verbatim raw sources are preserved in this
> folder: `_crawl/*.html` (15 raw pages + 1 legacy stub + 404), `_crawl/extracted.json`
> (structured per-page), `_crawl/detailed_dump.txt` (full body text of all pages), `_crawl/site.css`
> (brand tokens). Where this doc says "full text in `detailed_dump.txt`", the unabridged body is there.

## 1.1 Backup prerequisite (verified before crawl)
Source: `/data/backups/20261126-shadow/manifest.json` (read-only verification; nothing modified).

| Repo | HEAD | Bundle | SHA-256 (head) | Private shadow | verified |
|------|------|--------|----------------|----------------|----------|
| Emplowise-Website-Phase-I | `89a8e7f8f5e676eb91ca75f2aad01470c95082a8` | Emplowise-Website-Phase-I.bundle (7,482,179 B) | `eb8cc343…b7ae1f` | `Emplowise-Website-Phase-I-shadow-20261126` | true |
| Emplowise-Docs | `252757c6505d669fc729853102fe755c3afe08d8` | Emplowise-Docs.bundle (1,783,383 B) | `201b133a…9a96c7` | `Emplowise-Docs-shadow-20261126` | true |
| EmploStart | `2679c1ac27f3c122010f10f0d35f789023b9d72e` | EmploStart.bundle (486,994 B) | `b921c9e0…048fd3f` | `EmploStart-shadow-20261126` | true |

- Fresh upstream `--mirror` clones at `/data/backups/20261126-shadow/{repo}.git`; all branches/tags pushed to the
  private shadows and verified. GitHub-managed `refs/pull/*` cannot be pushed → retained in local mirror/bundles only.
- Combined downloadable archive: `/data/backups/20261126-shadow/Emplowise-Pre-Audit-Backups-20261126.zip` (9,736,921 B).
- The website's `origin` HEAD `89a8e7f` matches the deployed site's `Last-Modified: Tue, 24 Nov 2026 20:27:50 GMT`, so the local source reflects live.

## 1.2 Indexable-URL inventory (live crawl)

**Live robots.txt:** `User-agent: *`, `Allow: /`, `Disallow: /api/`, `Sitemap: …/sitemap.xml`. (HTTP 200.)
**sitemap.xml:** 14 `<loc>` entries (home priority 1.0, all others 0.8; all `changefreq weekly`).

Crawl of all 14 sitemap URLs returned **HTTP 200**. A recursive internal-link crawl of those pages
discovered **1 further HTML page** and a set of **soft-redirect stubs + file downloads**:

| Category | Path | HTTP | In sitemap? | robots (meta) | Self canonical? | Notes |
|----------|------|------|-------------|---------------|-----------------|-------|
| Page | `/` (home) | 200 | ✅ | (default → index) | ✅ | Primary CTA = Free HR Audit |
| Page | `/what-we-are/` | 200 | ✅ | index (default) | ✅ | Contains `#team` anchor section |
| Page | `/what-we-do/` | 200 | ✅ | index | ✅ | Service catalogue |
| Page | `/what-we-are-building/` | 200 | ✅ | index | ✅ | AI "pre-launch" division |
| Page | `/why-emplowise/` | 200 | ✅ | index | ✅ | Pricing / packages |
| Page | `/emplostart/` | 200 | ✅ | index | ✅ | Launcher → external product app |
| Page | `/faq/` | 200 | ✅ | index | ✅ | FAQPage schema, 21 Q/A |
| Page | `/contact/` | 200 | ✅ | index | ✅ | Only page w/ external links (AI engines) |
| Page | `/free-hr-audit/` | 200 | ✅ | index | ✅ | Multi-step form (web3forms) |
| Page | `/terms/` | 200 | ✅ | index | ✅ | Legal; "Last updated 22 Nov 2026" |
| Page | `/privacy/` | 200 | ✅ | index | ✅ | Legal; "Last updated 22 Nov 2026" |
| Page | `/company-profile/` | 200 | ✅ | **index,follow** (explicit) | ✅ | Showcase |
| Page | `/portfolio/` | 200 | ✅ | **index,follow** (explicit) | ✅ | Showcase; repo-proof |
| Page | `/docs/` | 200 | ✅ | index | ✅ | Docs hub / downloads |
| **Extra** | `/pitch-deck/` | 200 | ❌ **NO** | **noindex,follow** | ✅ | Linked 16× (nav/footer) but deliberately excluded — consistent w/ noindex |
| Stub | `/pricing/` | 200 | ❌ | noindex,follow | → `/why-emplowise` | meta-refresh 301-equivalent |
| Stub | `/career-hub/` | 200 | ❌ | noindex,follow | → `/emplostart` | meta-refresh |
| Stub | `/student-hub/` | 200 | ❌ | noindex,follow | → `/emplostart` | meta-refresh |
| Stub | `/ai-automation/` | 200 | ❌ | noindex,follow | → `/what-we-are-building` | meta-refresh |
| Stub | `/team/` | 200 | ❌ | noindex,follow | → `/what-we-are` | meta-refresh |
| Error | (404 page) | **404** | n/a | noindex | n/a | title "Page not found \| Emplowise" |
| API | `/api/chat`, `/api/audit` | 404 | n/a | — | — | Laravel API **not deployed** on GH Pages |

**Total distinct indexable (`index`/default) HTML pages: 14** (sitemap) **+ 0** — pitch-deck is `noindex`. So the
indexable set = the 14 sitemap URLs. The 5 legacy stubs + pitch-deck are intentionally non-indexable.

**File downloads referenced (8, all `?v=1795552040` cache-busted):**
`Emplowise-Brand-Kit-2026.docx`, `Emplowise-Branding-Guidelines-2026.docx`, `Emplowise-Company-Profile-2026.docx`,
`Emplowise-Portfolio-2026.docx`, `Emplowise-Pitch-Deck-2026.pptx`, `Emplowise-Start-Prompt-Library-2026.docx`,
`Emplowise-Tool-Stack-2026.docx`, `Emplowise-Website-Breakdown-2026.docx`. Docs hub copy: *"Eight downloadable
documents and three live editions."*

**External (off-domain) destinations linked from the website:** only `/contact/` links out — to the EmploStart
product (`https://diocese-trees.github.io/EmploStart/`) and to four answer engines (ChatGPT, Claude, Gemini,
Perplexity) with a prefilled prompt. `/emplostart/` also links to the product app. No social or directory outbound links.

## 1.3 Per-page granular record

Legend for the header row of each page: **Title chars / Desc chars / H1·H2·H3 counts / images (missing-alt=0 on all) / internal links / external / JSON-LD blocks / body words / robots**.

Site-wide invariants (verified on all 15 HTML pages): `lang="en"`; `viewport width=device-width`;
`theme-color #081B3E` (→ `#050F26` in dark); **self-referential canonical with trailing slash**; full OG
+ Twitter card set; **`og:image` = `img/logo-primary.png` on every page (generic)**; a Content-Security-Policy
`<meta>`; a CSP-hash-whitelisted inline theme script; the global `Organization+ProfessionalService` JSON-LD;
identical header nav + footer; a "Cookies, kept light." consent block; and an "Emplowise assistant" chat widget.
All 3 logo images per standard page carry `alt="Emplowise"`; **0 images missing alt site-wide**.

---
### `/` (home) — 60/136, H1·H2·H3 = 1·4·3, imgs 3, int 38, ext 0, LD 1, 665 words, robots default
- **Title:** Remote HR Services in Pakistan for Growing Teams | Emplowise
- **Description:** Emplowise runs remote HR for startups and SMEs in Pakistan. Payroll, performance, and policy from PKR 40,000 a month. Book a free audit.
- **H1:** Remote HR services in Pakistan, run by one accountable team.
- **H2:** Four doors. Pick the one that fits. · What our remote HR services in Pakistan cover. · Start with a free HR audit. Leave with a gap list. · Cookies, kept light.
- **H3:** Payroll · Performance Management · Policy Making
- **Primary keywords (config):** remote HR services in Pakistan; HR outsourcing in Pakistan; managed HR services
- **CTAs:** Book a free HR audit · Open the EmploStart · Book the free audit · See how the four-stage method works
- **Stats block:** "Confirmed services 14 · Method stages 4 · Free modules in EmploStart 6 · Payroll inputs 4 · Review 4 · Policies 4"
- **Links:** free-hr-audit×2, what-we-do×4, why-emplowise, emplostart, contact, what-we-are(#team), pitch-deck, company-profile, portfolio, docs, faq, terms, privacy
- Full body text: `detailed_dump.txt` "PAGE: /".

### `/what-we-are/` — 59/143, 1·8·10, imgs 3, int 33, ext 0, LD 1, 1020 words, robots default
- **Title:** HR Outsourcing Company in Pakistan, Remote Team | Emplowise
- **Description:** Emplowise is an HR outsourcing company in Pakistan. A remote HR team installs payroll, performance, and policy structure for startups and SMEs.
- **H1:** An HR outsourcing company in Pakistan that answers directly.
- **H2:** Everyone knows who owns what. · Four rules that decide how we work. · How the Emplowise team splits the work. · Three audiences. One standard of clarity. · How an HR outsourcing company in Pakistan delivers. · What we confirm in writing after the audit. · Bring us your current HR reality. · Cookies, kept light.
- **H3 (values):** Clarity · Structure · Substance · Trust  **(team):** Muhammad Ali · Abdul Hadi · Samarah Nabil  **(audiences):** For startups · For SMEs · For career pivoters
- **Primary keyword:** HR outsourcing company in Pakistan
- **Team (real, config-sourced):** Muhammad Ali — Advisor (vision, governance, operational growth); Abdul Hadi — Co-Founder, Content Strategist & Strategic Marketer (also Strategic Partnerships at Advegen; The Creative Nexus; SDGs 1,3,4,8); Samarah Nabil — Co-Founder, Senior HR Business Manager & Analyst (9+ yrs; supported 2,000+ employees). *Portraits are initials placeholders (MA/AH/SN) pending official shoot.*
- **"Pending inputs" disclosure:** the page lists what is *confirmed in writing after the audit* — per-package inclusions, recruitment-fee inclusion, payroll tax scope, legal-advice qualifications, full-time vs shared rep, assessment cadence, contract length/notice, verified client results/testimonials/baselines, direct phone + inbox. **No invented metrics/results/client names.**
- CTAs: Book the free audit · See our HR outsourcing pricing in Pakistan · Open the free EmploStart · See the confirmed HR services

### `/what-we-do/` — 56/147, 1·8·10, imgs 3, int 34, ext 0, LD 1, 1250 words, robots default
- **Title:** HR Operations Outsourcing for Pakistani SMEs | Emplowise
- **H1:** HR operations outsourcing across three confirmed pillars.
- **H2:** Payroll · Performance Management · Policy Making · Fourteen services inside HR operations outsourcing. · A repeatable path from audit to review. · What changes when the structure lands. · See where your HR stack actually breaks. · Cookies, kept light.
- **Method (4 stages):** Assess → Identify → Improve → Review
- **Primary keyword:** HR operations outsourcing
- **Full service catalogue (14 services, 3 families)** — see §1.5.
- CTAs: Start with the audit · Book the free audit · See HR outsourcing pricing · Audit this pillar

### `/what-we-are-building/` — 59/141, 1·2·3, imgs 3, int 30, ext 0, LD 1, 492 words (thinnest), robots default
- **Title:** Where AI Fits: AI Automation for HR in Pakistan | Emplowise
- **H1:** Where AI fits: AI automation for HR, in the open.
- **H3 modules (all "In build"/pre-launch):** Payroll Engine · Performance Insight Layer · Policy Co-Pilot
- **Primary keyword:** AI automation for HR
- Explicit "Building Soon", "Static preview. No live data, no client records." Honest pre-launch framing.
- CTAs: See the confirmed HR services

### `/why-emplowise/` — 51/147, 1·6·4, imgs 3, int 34, ext 0, LD 1, 1109 words, robots default
- **Title:** Why Emplowise for Remote HR in Pakistan | Emplowise
- **H1:** Why Emplowise is the remote HR partner for growing teams.
- **H2:** One remote HR partner, with the price on the page. · What the price includes, and what it does not · Why Emplowise publishes HR pricing by headcount. · Every service that can sit inside a retainer. · Pick a package after the audit, not before. · Cookies, kept light.
- **Pricing (published):** Starter PKR 40,000/mo (≤20 staff); Business PKR 75,000/mo (≤50, "Core tier"); Enterprise Custom scoped monthly (50+). Inclusions "confirmed in writing after your Free HR Audit."
- **Primary keyword:** why Emplowise; also "HR outsourcing pricing in Pakistan"
- CTAs: Start with the free audit · Request a quote · Book the free audit · Read pricing questions

### `/emplostart/` — 54/143, 1·7·13, imgs 3, int 38, ext 0 (product link internal), LD 1, 1120 words, robots default
- **Title:** Free ATS Resume Checker and 6 Career Tools | Emplowise
- **H1:** A free ATS resume checker for career pivoters and job seekers.
- **6 modules (H3):** Career Pivot Planner · Career Reimagination Lab · Market Assessment · ATS Resume Analyzer · Interview Prep · Profile Builder
- **14-prompt library:** EMPLOWISE (P01–P09) + START (P10–P14), each letter = one prompt (ids P01–P14).
- **Local-first claims:** runs in-browser, nothing uploaded, optional AI off until consent, "Shared PC mode is session only", 0 accounts, 0 cost.
- SDG alignment (voluntary, "not a UN endorsement"): SDG 4 / 8 / 10.
- CTAs: Open EmploStart · Open in app · Open the 14-prompt library · Book the free HR audit · Read ATS resume questions

### `/faq/` — 53/143, 1·7·0, imgs 3, int 30, ext 0, LD 1 (FAQPage), 1065 words, robots default
- **Title:** HR Outsourcing Questions Answered Clearly | Emplowise
- **H1:** HR outsourcing questions answered with confirmed facts.
- **Sections (H2):** HR outsourcing questions · Pricing and packages · The free HR audit · EmploStart · Ask the Emplowise assistant · Ready for a real answer about your HR stack? · Cookies, kept light.
- **21 questions** (live FAQPage JSON-LD; matches config) — see §1.6 list.
- CTAs: Book the free audit · Open EmploStart free career tools

### `/contact/` — 51/143, 1·7·3, imgs 3, int 36, **ext 4**, LD 1, 534 words, robots default
- **Title:** Contact Emplowise for Remote HR Support | Emplowise
- **H1:** Contact Emplowise without a maze of forms.
- **H2:** Tell us what needs to work better. · What happens next · Email us · Socials · Resources · Ask your favourite GPT about Emplowise · Cookies, kept light.
- **Channels:** email `hello@emplowise.com` (mailto); Free-HR-Audit form (web3forms); chat assistant; **external answer-engine prompts**: ChatGPT, Claude, Gemini, Perplexity each prefilled *"What is Emplowise, what remote HR services does it offer in Pakistan, and what are its package prices?"* (a deliberate GEO affordance).
- Footer "Socials" links here are **`href="#"` placeholders** (LinkedIn, Facebook, Instagram, X, YouTube, WhatsApp) → **no verified profiles** (see Issue I-04).

### `/free-hr-audit/` — 58/149, 1·6·4, imgs 3, int 29, ext 0, LD 1, 721 words, robots default
- **Title:** Free HR Audit in Pakistan, Booked in 4 Minutes | Emplowise
- **H1:** A free HR audit in Pakistan, booked in four minutes.
- **Multi-step form (4 sections, 21 inputs + 2 selects):** Who are we speaking with? · What does the team look like? · When should we run it? · Review and submit.
- Headcount bands: 1-10 / 11-20 / 21-50 / 51-100 / 100+. Pain options: payroll / performance / policy / compliance / recruitment / reporting. Time slots: Morning 9-12 / Afternoon 12-16 / Evening 16-19.
- **Form posts to `https://api.web3forms.com/submit`** (`data-endpoint`, `access_key`) — works on static; Laravel `/api/audit` is inert on GH Pages (I-10).
- CTAs: Book the free audit · Back to the site

### `/company-profile/` — 51/143, 1·11·20, imgs 3, int 34, ext 0, LD 1 (WebPage), 1826 words (thickest), **robots index,follow**
- **Title:** Remote HR Company Profile: 2026 Edition | Emplowise
- **H1:** A remote HR company profile written for buyers, not archives.
- **H2:** What this remote HR company profile includes. · The gap Emplowise was built to fill. · Four buying situations, not four demographics. · What is in scope, and what is not. · Four stages, one sequence, four documents. · Fourteen services across three pillars. · Published retainers, billed monthly. · Three people own the work. · Three kinds of measurement, never merged. · Take the profile, or start with the audit…
- **Primary keyword:** remote HR company profile. Download: Company-Profile-2026.docx.

### `/portfolio/` — 47/152, 1·6·4, imgs 3, int 32, ext 0, LD 1 (WebPage), 1544 words, **robots index,follow**
- **Title:** Remote HR Portfolio of Shipped Work | Emplowise
- **H1:** A remote HR portfolio that lists shipped work only.
- **H2:** What this remote HR portfolio documents. · Four shipped artifacts, each with repository proof. · Supporting systems, also in the repository. · The case study standard, written down. · Inspect the work, then start with the audit.
- **Evidence standard (verbatim gist):** "Repo proof or nothing"; "Behaviour over assertion"; "No borrowed proof" (no client logo/testimonial/revenue/award); **"Emplowise has no published client case studies yet, and this page does not invent any."** Mentions repository/GitHub in text (4× github, 6× repository) but **no outbound repo URLs** in HTML.
- Primary keyword: remote HR portfolio. Download: Portfolio-2026.docx.

### `/docs/` — 49/155, 1·8·8, imgs 3, int 41 (highest), ext 0, LD 1, 687 words, robots default
- **Title:** Emplowise Documentation and Downloads | Emplowise
- **H1:** Emplowise documentation, with live editions and editable downloads.
- **H2 groups:** Brand system and writing rules. · What Emplowise sells, and the proof behind it. · The free career library candidates actually use. · How the site is built and shipped. · Notes that live with the code. · Need a document this hub does not carry?
- **Primary keyword:** Emplowise documentation. Downloads: Brand-Kit, Branding-Guidelines, Company-Profile, Portfolio, Pitch-Deck(.pptx), Prompt-Library (+ Tool-Stack, Website-Breakdown referenced elsewhere).
- CTAs: Download the brand kit / guidelines / profile / portfolio / deck / prompt library / breakdown / tool stack.

### `/pitch-deck/` — 57/136, 1·10·2, **imgs 19**, int 33, ext 0, LD 1 (WebPage), 903 words, **robots noindex,follow**, **NOT in sitemap**
- **Title:** Emplowise Pitch Deck: Eight Slides for Buyers | Emplowise
- **H1:** The Emplowise pitch deck, eight slides, one question each.
- **8 slides (H2):** Remote HR structure for growing Pakistani businesses · Informal HR breaks at thirty staff · One method, four stages, written outputs · Published retainers priced by headcount · A clear wedge between DIY and enterprise · Audit first, then EmploStart, then retainers · Shipped platform, not promised platform · From toolkit to retained client work · (+ closing: One free intake, one named lead, one gap map.)
- Only page with many images (19, all with alt) — slide graphics. Download: Pitch-Deck-2026.pptx.

### `/terms/` — 45/153, 1·9·0, imgs 3, int 31, ext 0, LD 1, 816 words, robots default · **"Last updated 22 November 2026"**
- **Title:** Terms of Service for HR Retainers | Emplowise
- **H1:** Terms of service, written to be read.  **H2:** Who we are · Using this site · The free HR audit · Retainers and scope · No guarantee of a business outcome · Intellectual property · Liability · Governing law and changes · Cookies.
- **Primary keyword:** Emplowise terms of service. Notable substance: published prices ≠ offer; Pakistan law; no guaranteed business outcome.

### `/privacy/` — 45/152, 1·9·0, imgs 3, int 31, ext 0, LD 1, 858 words, robots default · **"Last updated 22 November 2026"**
- **Title:** Privacy Policy and Cookie Choices | Emplowise
- **H1:** Privacy, in plain language.  **H2:** What we collect · Why we use it · Cookies and local storage · Sharing and processors · How long we keep it · Your choices and rights · Security and international processing · Contact and changes · Cookies.
- **Substance:** no data sold; analytics off until opt-in; processors incl. web3forms; cookie/localStorage (theme key `emplowise:theme`).

## 1.4 Shared navigation & footer (identical across pages)
**Header nav:** logo→`/` · **Meet Emplowise**→`/` · Our Story→`/what-we-are/` · What We Do→`/what-we-do/` ·
Meet The Team→`/what-we-are#team` · Why Us→`/why-emplowise/` · Where's AI→`/what-we-are-building/` ·
EmploStart→`/emplostart/` · Contact Us→`/contact/` · **[Free HR Audit]** (primary CTA) · Dark-mode toggle.
Note: home label is "**Meet Emplowise**" (both logo and a nav item point to `/`).

**Footer columns:** (CTA) Free HR Audit · **Socials**: LinkedIn, Facebook, Instagram, X, YouTube, WhatsApp — **all `href="#"` (placeholders)** ·
**Company**: Meet Emplowise, Our Story, What We Do, Meet The Team, Why Us, Company Profile, Portfolio, Where's AI, EmploStart ·
**Resources**: Pitch Deck, Documentation, FAQ, Contact Us, Free HR Audit · **Start here**: `hello@emplowise.com` ·
`© 2026 Emplowise HR Services. All rights reserved.` · tagline "**People analytics without bias, so CEOs can set new standards.**" · Terms · Privacy · Cookie settings.

## 1.5 Entity reference (from live + config)
**14 services → 3 operating families:**
- *Managed HR Operations (7):* Complete recruitment · Employee onboarding · HR documentation and employee records · Leave and attendance management · HR policies and SOPs · Payroll · Legal and compliance support
- *Organizational Intelligence (3):* Performance support · Employee relations and conflict support · Organizational assessments
- *Executive HR Partnership (4):* Monthly HR reporting · Ongoing HR consultation · Specialist HR consultant support · Dedicated HR representative

**3 pillars** = Payroll / Performance Management / Policy Making. **Method** = Assess·Identify·Improve·Review.
**Packages** = Starter 40,000 / Business 75,000 / Enterprise Custom. **Audiences** = startups · SMEs · career pivoters/talent.

## 1.6 FAQ questions (21, live schema + config)
1 What does Emplowise actually do? · 2 Is Emplowise a software product or a service? · 3 Who is the right fit? ·
4 Is delivery onsite or remote? · 5 Does Emplowise replace our leadership or board? · 6 Can you guarantee legal compliance? ·
7 How much does Emplowise cost? · 8 What is included in each package? · 9 Are recruitment fees included? ·
10 Does payroll include tax filing and salary disbursement? · 11 Is there a minimum contract length? ·
12 What is the Free HR Audit? · 13 How long does it take? · 14 What do I need to prepare? · 15 Is it really free? ·
16 Where do my details go? · 17 Is the EmploStart actually free? · 18 How does the ATS score work? · (+ remaining grouped in Pricing/audit/EmploStart sections).

## 1.7 Brand & technical assets (baseline for Phase 7)
- **Palette (CSS custom props):** navy `#081B3E`, teal `#0d9488`, teal-deep `#0f766e`, aqua `#5eead4`, ice `#f0f9f9`,
  cyan `#22d3ee`, indigo `#4f46e5`, violet `#7c3aed`, magenta `#d946ef`, amber `#f59e0b`, rose `#e11d48`, slate `#16233c`;
  semantic success/warning/danger/info; brand gradients (`--grad-brand` teal→cyan→indigo, `--grad-student` indigo→violet→magenta, `--grad-navy`, etc.).
- **Fonts (self-hosted woff2, preloaded):** display **Montserrat** (`fonts/montserrat-e56e84e5-latin.woff2`), body **Plus Jakarta Sans** (`fonts/jakarta-fdb05bf0-latin.woff2`), mono SFMono. Fallbacks Helvetica Neue / Segoe UI.
- **Logos:** `logo-primary.png` (light) + `logo-reverse` (dark) with responsive webp srcsets (125/250/306/375 px); favicon.png/.ico.
- **Layout tokens:** `--shell 1140px`, `--prose 65ch`, `--header-h 64px`, z-scale; light/dark via `data-theme` + localStorage.
- **Delivery:** Laravel source → static export (`app/Console/Commands/ExportStatic.php`) → GitHub Pages (`server: GitHub.com`, HTTP/2, HSTS, `Last-Modified 24 Nov 2026`). Dual path: `vercel.json` also present (redirects `permanent:true`→308, asset cache headers) for a Vercel route; the GH Pages deployment instead uses meta-refresh stubs.

## 1.8 Local-code ↔ live reconciliation & gaps (explicit)
- config `emplowise.php` is the single source of truth for titles/descriptions/keywords/H1/H2/intro of all 16 SEO entries (incl. non-page `team`); live pages match it exactly. ✔
- Legacy redirects defined in `routes/web.php` + `vercel.json` do **not** apply as 301/308 on GH Pages (soft stubs instead) — **I-02**.
- Schema lacks author/date/breadcrumb/service-level nodes — **I-03, I-05, I-06**.
- Socials are placeholders — **I-04**. Forms = third-party web3forms (client-side), API inert on static — **I-10**.
- EmploStart **product** repo (separate deployment) lacks canonical + og:title — **I-09** (outside rewrite scope, recorded).

## 1.9 Verification checklist (Phase 1 done)
- [x] robots.txt + sitemap.xml fetched and parsed
- [x] all 14 sitemap URLs crawled HTTP 200; extra `/pitch-deck/` discovered via crawl
- [x] 5 legacy stubs + 404 + inert API behaviour characterized
- [x] per-page: title/desc/H1-H3/canonical/robots/OG/schema/links/image-alts/dates/authors/body captured
- [x] nav + footer + CTAs + brand tokens + entity catalogue + downloads captured
- [x] raw HTML + `extracted.json` + `detailed_dump.txt` persisted in `_crawl/`
- [x] backup prerequisite recorded from manifest
- [x] gaps and contradictions logged to `Issues-and-Decisions.md` (I-01…I-11)
