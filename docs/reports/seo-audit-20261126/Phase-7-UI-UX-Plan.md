# Phase 7 — UI/UX Plan (brand-preserving)

**Inputs:** `Phase-1-Backup.md` §1.4 (nav/footer), §1.7 (brand baseline), §1.3 (per-page content); `Phase-2-Deep-Analysis.md` §2.11 (P0/P1/P2); `Phase-3-Gap-Analysis.md` (G-1…G-4, D-1…D-4); `Phase-4-Breakdown.md` (U-1…U-10 `[PROPOSED]`); `Phase-5-SEO-AEO-GEO-Extraction.md` (AEO answer surfaces, I-25); `Phase-6-Research-Plan.md` (owners AH/MA/SN/DEV).
**Evidence files:** `_crawl/*.html` (15 rendered pages), `_crawl/site.css` (143,485 B, concatenated build of `tokens/base/layout/components/pages/showcase/chat/consent/theme.css`), `/data/emplowise/public/js/*.js` (9 files), `/data/emplowise/resources/views/**`.
**Ground rule:** this is a *plan only*. No Blade/CSS/JS file was modified in Phase 7. Every recommendation below is expressible inside the existing token system — no new typeface, no new hue outside the declared palette, no new logo.

---

## 7.1 Brand preservation contract (exact values — MUST NOT change)

### 7.1.1 Typography
| Role | Token | Exact stack | Files / weights in use |
|---|---|---|---|
| Display (H1–H3, brand marks, stat numbers) | `--font-display` | `"Montserrat","Helvetica Neue",Arial,sans-serif` | `fonts/montserrat-e56e84e5-latin.woff2` — declared 700 and 800, `font-display: swap`, latin `unicode-range` |
| Body / UI | `--font-body` | `"Plus Jakarta Sans","Segoe UI",system-ui,-apple-system,sans-serif` | `fonts/jakarta-fdb05bf0-latin.woff2` — 400, 500, 600 (+600/700 used in buttons), `swap` |
| Mono (kickers, breadcrumb, labels, numerals) | `--font-mono` | `"SFMono-Regular",ui-monospace,"Cascadia Code",Consolas,monospace` | **system mono — no webfont download** (keep it that way; it is free performance) |

Both webfonts are **self-hosted and preloaded** (2 `<link rel=preload>` in `layouts/app.blade.php`). Rule for all new units: reuse these three stacks via the tokens only; **no `font-family` literals** and no additional Google Fonts request. Kickers are `0.66rem` mono, `letter-spacing: 0.14em`, `text-transform: uppercase` — this is the single most recognisable text pattern on the site and must be copied exactly for any new card, tab or label.

### 7.1.2 Colour (light `:root`)
navy `#081b3e` · navy-900 `#050f26` · navy-800 `#0b2450` · navy-700 `#123061` · navy-600 `#1b3f7a` · teal `#0d9488` · teal-deep `#0f766e` · teal-600 `#0b8276` · aqua `#5eead4` · ice `#f0f9f9` · offwhite `#f7f7f7` · cyan `#22d3ee` · cyan-deep `#0891b2` · indigo `#4f46e5` · violet `#7c3aed` · magenta `#d946ef` · amber `#f59e0b` · amber-deep `#92400e` · rose `#e11d48` · slate `#16233c` / 700 `#334155` / 600 `#475569` / 500 `#54637a` / 400 `#94a3b8` / 300 `#cbd5e1` · line `#e4eaf1` · sand `#f8f4ee` · surface `#ffffff` / 2 `#f6fafb` / 3 `#eef5f7` / canvas `#f4f9fb` · text-on-dark `#c9d8ea`.
Semantic: success `#10b981` · warning `#f59e0b` · danger `#e11d48` · info `#0ea5e9`.

Gradients (name → exact stop list) are brand signatures, not decoration:
`--grad-brand` `linear-gradient(118deg,#0d9488 0%,#0891b2 52%,#4f46e5 100%)` (accent rules, H1 `em`) ·
`--grad-teal` `120deg,#0f766e,#0d9488 45%,#22d3ee` (primary buttons, active filters) ·
`--grad-aqua` `100deg,#5eead4,#22d3ee 55%,#60a5fa` ·
`--grad-student` `120deg,#4f46e5,#7c3aed 48%,#d946ef` (**reserved for EmploStart/career context only**) ·
`--grad-navy` `160deg,#0b2450,#081b3e 55%,#050f26` (hero, cta-band, footer) ·
`--grad-amber` `120deg,#f59e0b,#fb7185` · `--grad-sheen` · `--grad-hairline`.
**Rule:** a new section may reuse an existing gradient verbatim; it may not invent a new angle/stop combination. `--grad-student` must stay off corporate pages (that separation is the current IA's colour language).

### 7.1.3 Dark theme (`html[data-theme="dark"]`)
Separate token set, must be mirrored by any new component: `--d-page #050f26` · `--d-surface #08182f` · `--d-surface-2 #0a1d38` · `--d-surface-3 #0e2444` · `--d-ink #e9eff8` · `--d-ink-soft #a9b8cc` · `--d-ink-dim #7f8fa6` · `--d-line rgba(148,163,184,.16)` · `--d-accent #5eead4`. Mechanism: `<html data-theme>` written by `js/theme.js` (key **`emplowise:theme`**), gated by an `html.js-theme` class so the toggle is invisible without JS; logo swaps via `.brand .brand-logo--light/--dark`; `color-scheme: dark`; `::selection rgba(94,234,212,.32)`; `@media print` forces white/black. **Acceptance for all §7.8 items: renders correctly in light, dark, and with JS disabled.**

### 7.1.4 Logos & marks
`img/logo-primary.png` (+ `logo-primary-125/250/306/375.webp` srcset) for light chrome; `img/logo-reverse-102/204/306.webp` (+ `-306.png`, 306×78 intrinsic, `alt="Emplowise"`) for the navy footer/rail; `favicon.png` / `favicon.ico`; `og:image` currently = `logo-primary.png` (**I-05** → Phase 6 D30–60 task, must be produced *from these brand assets*, not stock).

### 7.1.5 Spatial system
`--shell 1140px` · `--prose 65ch` · `--gutter clamp(1.15rem,4vw,2.5rem)` · `--header-h 64px` · `--rail-w 184px` (≥1200px) · spacing `--s-1 0.25rem → --s-9 6rem` · radii `8/12/16/22/30/999px` (`xs,sm,lg,xl,pill`) · shadows `xs/sm/md/lg/teal/navy` + `--glow-aqua` · motion `--ease cubic-bezier(.22,.61,.36,1)`, `--ease-out (.16,1,.3,1)`, `--ease-spring (.34,1.4,.5,1)`, `--dur-fast .22s / --dur .42s / --dur-slow .95s` · z-scale `decoration -1 … skip 300` (header 100, consent 140, chat 160, toast 220).
**Rule:** new components take radius from the existing 6 steps and spacing from `--s-n`; minimum touch target stays 44px (already the standard: `.btn{min-height:44px}`, `.nav-toggle{44px}`, `.chat-close{44px}` at ≤520px).

---

## 7.2 Responsive model (as built — preserve, do not re-architect)
| Range | Header | Content | Notes |
|---|---|---|---|
| ≥1200px | **fixed left rail**, `--rail-w 184px`, `body{padding-left}`, vertical `.header-inner`, active nav marked by `inset 2px 0 0 aqua` | `.shell` 1140px | Distinctive; the rail is the brand's desktop signature |
| 1041–1199px | sticky top bar, `min-height 64px`, glass blur, `.is-stuck` compaction | `.shell` | |
| ≤1040px | `.nav-toggle` hamburger → `.main-nav` sheet; theme toggle relocates to `.nav-theme` inside the sheet | single column, grids collapse | sheet gets `--shadow-lg` |
| ≤900px | | `.legal-toc` un-sticks, full width | |
| ≤640px | | chat launcher hidden while consent bar present (`body.has-consent`) | |
| ≤520px | | chat panel becomes bottom sheet (`inset auto 0 0 0`, radius top only, `env(safe-area-inset-bottom)`) | |
| ≤560px | | consent card becomes edge-anchored, `.consent-body` collapsed until `.is-expanded` | |
| print | `.consent`/chat hidden, dark→light forced | | deck slides flatten |

## 7.3 Interaction inventory (JS already shipped — reuse before adding)
`app.js` (10.2 KB): sticky `.is-stuck`, `.reveal` scroll-in, `[data-open-chat]`, `is-scroll-locked` for the nav sheet, `is-error` form state · `theme.js` (3.0 KB) · `consent.js` (5.6 KB, key `emplowise:consent`, fires `emplowise:consent` CustomEvent that `chat.js`/GA-less stack listens for) · `chat.js` (25.0 KB, assistant panel, suggestions, quick chips) · `audit.js` (25.4 KB, 4-step wizard, `.repeat-item`, score ring, copy-to-clipboard) · `faq.js` (7.7 KB, search + group filters + accordion) · `home.js` (3.7 KB, `[data-count]` count-up, `.stack-bar i[data-fill]`, pointer parallax) · `team.js` (2.2 KB, tabbed panels, keyboard) · `deck.js` (3.0 KB, presenting mode). Motion is behind `.reveal`/`js-anim`; `prefers-reduced-motion` respected in the animation layers — **any new UI must not add motion without that guard**.

---

## 7.4 Per-page wireframe notes
Format: **current skeleton (observed landmarks) → keep → change (brand-safe) → AEO/GEO surface from Phase 5.**

### `/` (index) — `section.hero` → `#shortcuts` → `#pillars` → `.cta-band`
Keep: `--grad-navy` hero, `1.06fr / 0.94fr` hero grid with H1 capped at `19ch`, 4-up `.shortcut-grid`, `.pillar` cards, aurora `::before` on `.cta-band`.
Change: (a) "Four doors. Pick the one that fits." is the strongest IA device on the site — give the four cards a persistent `is-current`-style border so the chosen door is legible after scroll; (b) place the Phase-5 **home direct answer (42–60w)** as a short styled paragraph immediately under H1 in existing mono-kicker + body styling (no new component type: reuse `.hero-lead`), so snippet/answer engines read it first; (c) reduce `.stack-bar` decorative count if the numbers are not confirmable — never let a chart imply a statistic we have not published.

### `/what-we-are/` — `.page-head` → 3 plain sections → `#team` (`.team-tabs`/`.team-panel`) → 2 sections → `.cta-band`
Keep: team tab/window pattern with `.team-photo figcaption`, "Four rules" numbered cards, `#team` deep link used by nav `Meet The Team`.
Change: (a) add an in-page jump rail on desktop reusing `.show-jump` (already built for showcase pages) — this page has 8 H2s and no wayfinding; (b) make each team panel carry the truthful `Person` fields agreed in Phase 5 (name/role/`worksFor`; no invented photos or profiles → I-23), rendered with existing `.team-role`/`.team-tab-role` classes.

### `/what-we-do/` — `.page-head` → 2 tight sections → `.section--alt` → section → `.section--navy` → `.cta-band`
Keep: 14-service list grouped into the 3 pillar families, `.pillar--performance/--policy` colour-coded icon accents.
Change: (a) 14 services in one flow is a scan problem, not a content problem — introduce a pillar **filter** using the existing `.filter-btn` + `is-active` pattern from `faq.js` rather than splitting URLs (protects the Phase-4 decision I-22); (b) attach a two-line `.acc-panel`-style summary per service ready to become U-3 `[PROPOSED]` per-service pages later; (c) pin Phase-5 `/what-we-do/` direct answer under H1.

### `/why-emplowise/` — `.page-head` → 4 sections → `.cta-band`
Keep: `.price-grid` (3-up, `.price-card--featured`), published PKR figures — this is differentiator **D-1** and must stay visually loud.
Change: (a) price cards need an explicit "what is not included" footer row inside `.price-card` (already `.card-foot` exists) to match the page's own anti-hype tone; (b) reconcile the three price mentions site-wide (Phase 6 D31–60) so home/why-emplowise/company-profile show identical `Starter 40,000 / Business 75,000 / Enterprise Custom`; (c) Phase-5 answer block under H1.

### `/what-we-are-building/` — `.page-head.ai-hero` → tight section → `.ai-dashboard-section`
Thinnest page (492w). Keep the module cards (`.module-card`, `.is-live` vs `--build` status chips) — the honest live/build status is exactly the aesthetic differentiator.
Change: add one "how we will tell you when it ships" block reusing `.repeat-item`/`.aside-card` styling; do **not** add a waitlist widget without a verified intake channel (only the Free HR Audit form is verified → I-10).

### `/emplostart/` — `.launcher-head` → `#modules` → `#prompt-letters` → `#intake` → `#runs-where` → `#pledge` → `.cta-band`
Keep: `--grad-student` accents, 14-letter prompt library grid (`.prompt-card`, `.copy-btn`), the UN fair-jobs pledge band **with its disclaimer sentence** ("Voluntary alignment only…") — that sentence must never be dropped for visual tidiness.
Change: (a) the launcher head is the primary conversion moment; make the "open EmploStart" action the only `--grad-student` button above the fold; (b) `#prompt-letters` needs copy-feedback parity with `.copy-btn` states used by the audit wizard; (c) keep the free-tool claims strictly inside the confirmed tool list (no invented tool counts).

### `/faq/` — `.page-head` → tight section → 4 `.faq-group` → `.cta-band`
Keep: search box + `.filter-btn` group filters + accordion (`aria-expanded`, `.acc-icon`).
Change: (a) 21 questions live behind 4 group filters — set `hidden` only for display, never for crawlability (content already in DOM: verify after any change so `FAQPage` stays truthful → I-06); (b) add a "jump to answer" mono link per group using `.show-jump` styling; (c) surface the Phase-5 FAQ direct answer under H1.

### `/contact/` — `.page-head` → `.contact-section` → 3 `.contact-card` + resources nav + AI card
Keep: `.contact-panel` 1.3fr/0.7fr, "What happens next" numbered `.contact-step` with aqua numerals, "Ask your favourite GPT" `.prompt-card` row (GEO differentiator **D-3**).
Change: (a) **Socials card is the weakest UI on the site** — six `href="#"` circles reading "profile pending" (I-04/I-25). Brand-safe fix: hide the row until real URLs exist, or replace with the single verified channel (`hello@emplowise.com` + audit form) styled with `.contact-card-foot`; (b) the web3forms-powered form must show a visible success/failure path (`.is-error`, `.contact-copy-status`) since there is no server on GitHub Pages (I-10).

### `/free-hr-audit/` — `.page-head` → single `.section` (wizard)
Highest-value page; keep `.wizard` card, 4 steps (`Who / What does the team look like / When / Review`), `.bar-row` results, score ring, `.repeat-item`, copy button.
Change: (a) make step progress keyboard- and screen-reader-announced (`.sr-status` exists — confirm it is `aria-live="polite"`); (b) add a "nothing is uploaded, the audit runs in your browser" microcopy line in `.chat-note` styling — it is true (client-side, I-10) and it removes the main form-abandonment objection; (c) keep headcount bands and pain options exactly as config-declared, no invented percentages.

### `/company-profile/` — `.page-head.show-head` → `breadcrumb` → `.show-jump` → 9 sections → `.show-cta`
Thickest page (1826w) and already the best-structured. Keep: `show-band` alternation, `.table-wrap` data tables, `.aside-card`, download links.
Change: add `dateModified` display using the existing `.legal-updated` class (already used on terms/privacy) so the visible date and the Phase-6 schema date match (I-03).

### `/portfolio/` — `.page-head.show-head` → `#evidence-policy` → `#shipped` → `#systems` → `#case-standard` → `.show-cta`
Keep: **"shipped work only"** framing and the repository-proof pattern; the "case study standard, written down" block is the truthfulness moat (D-4).
Change: (a) each shipped artifact card should show repo + commit-ish proof link with the same `.tool-status` chip treatment used on EmploStart; (b) no client logos/names until a client authorises them — leave the existing placeholder-free layout intact rather than filling it with stock marks.

### `/docs/` — `.page-head.show-head` → `.show-jump` → 5 sections → `.cta-band`
Keep: jump rail, section cards, editable-download affordances (8 files).
Change: (a) label file formats and sizes next to each download using `.chip`; (b) add "last reviewed" using `.legal-updated` styling — a document hub with no dates reads stale (I-03 family).

### `/pitch-deck/` (noindex) — `.page-head.show-head` → `.show-cta`, 19 images, `deck.js` presenting mode
Keep: deck presentation, 8-slide framing, `noindex,follow` + deliberate sitemap exclusion (closed as non-issue, I-01).
Change: add a small "This page is not indexed — share the link directly" `.chat-note`-style caption so the noindex decision is legible to a human reviewer; add print fallback so `deck-presenting` degrades to a readable flow.

### `/terms/`, `/privacy/` — `.page-head--legal` → `.legal-toc` (sticky) → 8–9 `.legal-block`
Keep: TOC with aqua numerals, `.legal-updated` "Last updated 22 November 2026", plain-language headings.
Change: only the Phase-8 rewrite of wording, **substantive meaning preserved** (scope constraint); optionally add an anchor-copy control reusing `.copy-btn`.

### 404 (GitHub Pages default) 
Currently the platform default — off-brand. Brand-safe fix: add a `404.html` at repo root reusing `.page-head` + `.shortcut-grid` with four doors back into the funnel (no new visual language). *(No GH Pages configuration change required: a static `404.html` is honoured automatically.)*

---

## 7.5 Prioritised UX backlog
Effort S/M/L is relative size only — **no duration forecast** (Phase 6 I-26/I-27: no capacity data).

**P0 — trust & correctness (do first; each also unblocks a Phase-6 SEO item)**
| ID | Item | Brand risk | Dep | Owner | Acceptance |
|---|---|---|---|---|---|
| UX-01 | Remove/replace placeholder footer + contact "Socials" rows | low (uses `.contact-card-foot`) | I-04, I-25 | AH+DEV | no `href="#"` social circle anywhere; dark/light/print clean |
| UX-02 | Surface the 11 Phase-5 direct answers as styled lead blocks under each H1 | low (`.hero-lead`/mono kicker) | Phase 5 | AH | answer 40–60w visible above the fold on 11 pages |
| UX-03 | In-browser-audit privacy microcopy on `/free-hr-audit/` | none | I-10 | AH | sentence present, no over-claim |
| UX-04 | Price parity audit across home / why-emplowise / company-profile | none | I-19 | MA approves | 3 pages identical figures |
| UX-05 | Visible form success/failure states for all web3forms paths | low | I-10 | DEV | `.is-error` + status text on both outcomes |

**P1 — findability & depth**
| ID | Item | Brand risk | Dep | Owner |
|---|---|---|---|---|
| UX-06 | Reuse `.show-jump` rail on `/what-we-are/`, `/what-we-do/`, `/faq/` (≥1041px sticky) | low | — | DEV |
| UX-07 | Pillar `.filter-btn` filter over the 14 services (DOM stays complete) | low | I-22 | DEV+AH |
| UX-08 | Page-specific OG images generated from existing brand assets | must respect §7.1.2 | I-05 | AH |
| UX-09 | `.legal-updated` date treatment extended to docs + company-profile | none | I-03 | DEV |
| UX-10 | Brand-consistent `404.html` | medium (new page) | — | DEV+AH |
| UX-11 | Repo-proof chips on `/portfolio/` cards via `.tool-status` | low | D-4 | MA |
| UX-12 | Per-service expandable summary blocks (pre-work for U-3 `[PROPOSED]`) | low | I-21 | AH |

**P2 — polish & future**
| ID | Item | Notes |
|---|---|---|
| UX-13 | Critical-CSS split of `site.css` (143 KB single bundle) | Phase 2 P2; keep all token values identical |
| UX-14 | `prefers-reduced-motion` sweep for any new `.reveal`/`.is-active` transitions | accessibility guard |
| UX-15 | Consent card: add "manage" deep link parity with footer Cookie settings | uses existing `.consent-manage` |
| UX-16 | Rail navigation section grouping at ≥1200px (9 links is dense in 184px) | must not change the rail identity |
| UX-17 | `[PROPOSED]` guides hub (U-1) using `.card--flat` + `.show-jump` | gate on Phase 6 evidence, I-17/I-28 |
| UX-18 | `[PROPOSED]` case-study template (U-4) only after authorisation | gate on I-28; no invented clients |

## 7.6 Accessibility review (static code review — **not** a WCAG audit; no screen-reader or axe run performed)
Positive already in place: `.skip-link`, `aria-expanded` on accordions, `aria-label`+`title` on social icons, `aria-hidden`/`focusable=false` on decorative SVGs, 44px minimum controls, `:focus-visible` outlines (aqua in dark), `role`-free semantic landmarks (`header/nav/main/footer`), `alt` on 100% of images (Phase 2, 0 missing), `font-display: swap` (no invisible text), functional dark mode with `color-scheme`.
To verify when work is scheduled: contrast of `--slate-500 #54637a` and `--text-on-dark-soft #b9c9df` against their backgrounds; `.nav-group > summary` keyboard affordance; `.filter-btn` state announced to AT; chat panel focus trap and `Esc`; consent focus order vs chat launcher overlap at ≤640px; `sr-status` live region. **No claim of compliance level is made anywhere in this audit.**

## 7.7 Anti-drift list (explicitly out of scope)
New typefaces or external font CDNs · new hues outside §7.1.2 · re-shading `--grad-*` · new radii/shadow steps · replacing the ≥1200px left rail · stock photography or invented client logos · testimonials/ratings widgets (no data → Phase 5 forbids `Review`/`AggregateRating`) · animated counters that imply unpublished statistics · any change to the pledge disclaimer wording.

## 7.8 Validation vs Phases 1–6
All 15 inventoried pages covered by §7.4 (14 indexable + `pitch-deck`) plus the 404 state; every backlog item cites a Phase 1–5 issue ID; no item requires a new brand token (checked against §7.1); `[PROPOSED]` units (U-1…U-10) appear only as UX-12/17/18 and remain gated; Phase 6 owners used verbatim (AH/MA/SN/DEV).
**Limitations:** no user testing, session recording, heatmap, funnel analytics or field-performance data exists (I-26) — therefore no conversion-rate or bounce improvement is predicted for any item; prioritisation is qualitative (trust > findability > polish) and driven by evidence already captured. Screenshots were not taken; structure was derived from rendered HTML landmarks and the live stylesheet.
