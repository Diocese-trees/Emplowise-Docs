# Phase 8 — Full SEO Rewrite of Every Existing Public Page

**Covers all 15 inventoried public pages** (14 indexable + `/pitch-deck/`, which stays `noindex,follow`) from the Phase 1 inventory. Nothing here is deployed: this document *is* the deliverable. Each page section gives **metadata · heading outline · rewritten body copy · CTA copy · link changes · JSON-LD · AEO block · GEO note**.

## 8.0 Rules this rewrite is written under
1. **Voice (unchanged brand register, British English):** plain, declarative, lightly dry. Short sentences. Concrete nouns. No superlatives, no "revolutionary/synergy/transformative", no exclamation marks, no emoji. en-GB spelling throughout (*organise, prioritise, licence* as noun, *authorised*). The house pattern is **claim → evidence → limit**: we state what we do, then what we cannot yet confirm.
2. **Truthfulness gates (hard):** no client names, logos, testimonials, review scores, case-study outcomes, savings percentages, or team-count claims that do not already exist in `config/emplowise.php`. Pricing stays exactly **PKR 40,000 / PKR 75,000 / Custom** with the standing qualifier *"confirmed in writing after your Free HR Audit"*. The EmploStart SDG wording keeps its disclaimer *"Voluntary alignment only. This is not a UN endorsement, certification, or partnership."*
3. **Structural SEO invariants kept:** one `H1` per page; trailing-slash self-referencing canonicals; titles ≤ 60 chars; descriptions 136–158 chars; every image keeps a descriptive `alt`; `robots` unchanged except where noted (only `/pitch-deck/` is `noindex,follow`).
4. **Fixes propagated from the issue log:** I-03 real dates only · I-04/I-25 no placeholder socials in copy or schema · I-05 page-specific OG descriptions (image work deferred, tracked as UX-08) · I-06 no `HowTo`, no rich-result promises · I-13 slash-aligned `Organization.url` · I-19 price parity · I-22 services stay on one URL · I-30 filters never remove content from the DOM.
5. **Every AEO answer below is carried verbatim from Phase 5** (all validated at 40–60 words) so the copy and the schema agree token-for-token.

---

## 8.0a The repo's own SEO gate (local-code evidence — binding on this rewrite)
`app/Console/Commands/EmplowiseSeoAudit.php` (`php artisan emplowise:seo-audit`, run in CI) enforces, for each route in its `ROUTES` list — **13 of the 15 pages**: home, what-we-are, what-we-do, what-we-are-building, why-emplowise, emplostart, faq, contact, free-hr-audit, company-profile, portfolio, pitch-deck, docs:

- **title 45–60 characters and it must end with `| Emplowise`**;
- **description 135–155 characters**;
- the **primary keyword must appear, case-insensitively, in `title`, `h1`, `h2` and `intro`**;
- **exactly two** `secondary_keywords`; titles, descriptions, primaries and secondaries must all be **unique across routes**;
- **no em dash or en dash** in those fields; banned words `leverage, ecosystem, landscape, holistic, seamless`; forbidden phrases `Pending Input, Foundation, Growth, Scale, Replit`;
- fact checks that fail the build if copy drifts: 3 packages; Starter `PKR 40,000` with capacity literal **"Up to 20 employees"**; Business `PKR 75,000` with **"Up to 50 employees"**; Enterprise price must be **null**; **14 services**; **3 pillars**; methodology exactly `Assess,Identify,Improve,Review`; **14** student prompts; and `seo.faq.h2` must equal the **first FAQ category**.

**How §8.1–8.15 comply:** every title is written *including* the ` | Emplowise` suffix and measured at 52–60 chars; every description measured at 139–154 chars; primary keywords re-inserted into titles; new lead H2s are **additional** headings that never replace the gated `h2` string; em dashes are kept out of the five gated fields (they remain fine in body prose); package capacity strings use the config literals.
**Gap this audit found (I-33):** `/terms/` and `/privacy/` are **absent from `ROUTES`**, so legal copy is not covered by the gate — and indeed neither page's primary keyword (`Emplowise terms of service`, `Emplowise privacy policy`) appears in its current title, H1, H2 or intro. The §8.13/§8.14 rewrites put the keyword back into the title while leaving the substantive clauses intact, and recommend adding the two routes to `ROUTES`.

---


## 8.1 `/` — Home

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (52, in-range incl. suffix) | `Remote HR Services in Pakistan, One Team \| Emplowise` |
| Description (145) | `Remote HR services in Pakistan for startups and SMEs. Payroll, performance and policy on one monthly retainer from PKR 40,000. Book a free audit.` |
| Canonical | `https://diocese-trees.github.io/Emplowise-Website-Phase-I/` (unchanged) |
| Robots | `index,follow` |
| OG / Twitter | `og:title` = title above; `og:description` = description above; `og:type=website`; `twitter:card=summary_large_image` |
| Primary keyword | remote HR services in Pakistan (present in title, H1, `h2` field and intro) · secondary (exactly 2, unique): *HR outsourcing in Pakistan*, *managed HR services* |

**Headings**
- H1: `Remote HR services in Pakistan, run by one accountable team.` *(kept — it is the strongest H1 on the site and matches the keyword)*
- H2: `Four doors. Pick the one that fits.` · `What our remote HR services cover.` · `Start with a free HR audit. Leave with a written gap list.` · `Priced by headcount, published on the page.` *(new, replaces nothing — it formalises the existing stat block)*
- H3: Payroll · Performance Management · Policy Making

**Body — rewritten**
*AEO block, place directly under H1 as `.hero-lead` (54w):*
> Emplowise is a remote HR service for startups and SMEs in Pakistan. It runs payroll inputs, performance cycles, and policy on one monthly retainer priced by headcount, from PKR 40,000 for up to 20 staff. Every engagement starts with a free HR audit and a written gap list, delivered remotely by one accountable team.

*Hero support (replaces the current second paragraph):*
> You do not need an HR department. You need someone who owns the work. Emplowise takes the payroll inputs, the appraisal cycle and the policy stack off your desk, and reports on them monthly like any other function. Same three people, every month, in writing.

*Four doors (`.shortcut-grid`) — card copy, same four targets as built:*
- **Our story** — Who we are, who signs the work, and what we will not pretend. → `/what-we-are/`
- **What we do** — Fourteen confirmed services across payroll, performance and policy. → `/what-we-do/`
- **Pricing** — PKR figures on the page, not behind a call. → `/why-emplowise/`
- **Free HR audit** — Four minutes, then a written gap list. → `/free-hr-audit/`
`/what-we-are-building/` stays out of the four doors, as today.

*Services section lead:*
> Three pillars carry the work: payroll inputs and cycles, performance management, and policy making. Fourteen services sit inside them. Anything outside that list gets written down as out of scope rather than quietly absorbed.

*Pricing section (new H2 band, uses existing `.price-card` markup):*
> Starter is PKR 40,000 a month for up to 20 staff. Business is PKR 75,000 for up to 50. Enterprise is quoted above 50. All monthly, all remote, all starting with the audit. Which services land in your retainer is confirmed in writing after that audit — we publish the price, not a guess at your scope.

*Audit band lead:*
> The audit is free, takes about four minutes to book, and ends with a prioritised gap list you can act on whether or not you hire us.

**CTA copy** `Book a free HR audit` (primary) · `Open the free EmploStart tools` · `See what we do` · `Why teams pick Emplowise`.
**Links** unchanged (38 internal) — the only addition is the new pricing H2 anchoring to `/why-emplowise/#pricing`.
**JSON-LD** keep `Organization` + `ProfessionalService`; set `url` to the trailing-slash canonical; add `description` identical to the AEO block's first sentence; add `WebSite`; add `BreadcrumbList` (Home root); add `dateModified` **only once a real content-change date is tracked** (I-03) — do not backfill.
**GEO** the four prefilled engine prompts on `/contact/` must ask the same question this page answers; mirror this paragraph in `Organization.description` so one definition is repeated, not three competing ones.

---

## 8.2 `/what-we-are/` — Our Story (E-E-A-T page)

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (58) | `HR Outsourcing Company in Pakistan, Named Team \| Emplowise` |
| Description (143) | `Emplowise is an HR outsourcing company in Pakistan. Three named people install payroll, performance and policy structure, then run it remotely.` |
| OG | `og:title` = title above; `og:description` = description above |
| Primary keyword | HR outsourcing company in Pakistan (in title, H1, `h2` field, intro) · secondary: *outsourced HR support*, *dedicated HR representative* |

**Headings**
- H1: `An HR outsourcing company in Pakistan that answers directly.`
- H2: `What Emplowise is, in one paragraph.` *(new, holds the AEO block)* · `Everyone knows who owns what.` · `Four rules that decide how we work.` · `How the Emplowise team splits the work.` · `Three audiences. One standard of clarity.` · `How an HR outsourcing company in Pakistan delivers.` · `What we confirm in writing after the audit.` · `Bring us your current HR reality.`

**Body — rewritten**
*AEO block under H1 (43w):*
> Emplowise is an HR outsourcing company in Pakistan delivering remote HR to startups and SMEs. A named team installs payroll, performance, and policy structure, then runs it, so founders stop acting as the HR helpdesk. Delivery is fully remote with direct founder access.

*Who we are:*
> Emplowise HR Services was built by three people who kept meeting the same problem: a company grows past twenty staff and nobody owns the HR. Not badly run — simply unowned. We took that on as a service rather than a slide, so the offer is deliberately narrow and the price is on the page.
> We are not an agency with a bench of subcontractors and we do not claim to be. Three named people own the work; where something sits outside our competence we say so and point you at a lawyer, a tax adviser or an auditor.

*Values (H3 Clarity / Structure / Substance / Trust), one line each:*
> **Clarity** — you always know who is responsible. **Structure** — paperwork exists before the argument does. **Substance** — we would rather publish a price than a promise. **Trust** — what we cannot confirm, we label as unconfirmed.

*Team (real, config-sourced; keep `#team` anchor):*
> **Muhammad Ali — Advisor.** Sets direction, governance and operational growth.
> **Abdul Hadi — Co-Founder, Content Strategist & Strategic Marketer.** Owns how Emplowise is written, positioned and found; also works on strategic partnerships at Advegen and The Creative Nexus, and volunteers against SDGs 1, 3, 4 and 8.
> **Samarah Nabil — Co-Founder, Senior HR Business Manager & Analyst.** Nine-plus years in HR, supporting more than 2,000 employees across cycles; owns the delivery mechanics.
> *Portraits are initials placeholders until the official shoot — keep the visible caption "pending official portraits" and emit no schema `image` (I-08).*

*Outlook / limits block:* keep the existing "what we confirm in writing after the audit" list verbatim in substance (per-package inclusions, recruitment fees, payroll tax scope, legal-advice limits, shared vs dedicated rep, assessment cadence, contract length, verified client results, direct phone and inbox). Rewritten lead:
> This page states nothing we cannot hand over in writing later. Client results, testimonials and baselines are absent because they have not been verified and published yet, not because we are shy about them.

**CTA copy** `Book the free HR audit` · `See HR outsourcing pricing in Pakistan` · `Open the free EmploStart tools` · `See the confirmed HR services`.
**Links** unchanged; `Meet The Team` nav item continues to target `/what-we-are/#team`.
**JSON-LD** add `Person` × 3 (`name`, `jobTitle`, `worksFor` → Organization, `description`; **no** `image`, **no** `sameAs`); add `founder`/`foundingDate` to `Organization` **only if the client confirms them**; `WebPage` with real `dateModified` once tracked.
**GEO** this is the page that answers "who is behind Emplowise" and "is Emplowise legitimate" — the founder-origin paragraph above is written to be quotable standalone.

---

## 8.3 `/what-we-do/` — Services

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (59) | `HR Operations Outsourcing for Teams in Pakistan \| Emplowise` |
| Description (146) | `HR operations outsourcing in Pakistan across payroll, performance and policy. Fourteen confirmed services, one four-stage method, remote delivery.` |
| Primary keyword | HR operations outsourcing (in title, H1, `h2` field, intro) · secondary: *payroll and compliance services*, *HR process management* |

**Headings**
- H1: `HR operations outsourcing across three confirmed pillars.`
- H2: `What "outsourcing" means here, exactly.` *(new AEO holder)* · Payroll · Performance Management · Policy Making · `Fourteen services inside HR operations outsourcing.` · `A repeatable path from audit to review.` · `What changes when the structure lands.` · `See where your HR stack actually breaks.`
- Each pillar H2 opens with a one-line extractable definition (below).

**Body — rewritten**
*AEO block (42w):*
> Emplowise provides HR operations outsourcing across three pillars: payroll, performance management, and policy making. Fourteen confirmed services sit inside them, each engagement follows a four-stage method (assess, identify, improve, review), and retainers start at PKR 40,000 a month, delivered remotely in Pakistan.

*Pillar one-liners:*
> **Payroll.** The inputs, the cycle and the paperwork around it, so the month closes without a founder chasing timesheets.
> **Performance Management.** Cycles, criteria and reviews that happen on a date rather than when someone remembers.
> **Policy Making.** Written rules, records and SOPs that survive the person who wrote them.

*Definition of the model (new short block):*
> Outsourcing here does not mean handing us an inbox and disappearing. It means the function has a named owner, a cadence and a document trail. You keep decisions; we keep the machinery.

*The fourteen services:* keep all 14 names and the three family groupings exactly as published (Managed HR Operations × 7, Organizational Intelligence × 3, Executive HR Partnership × 4), rendered as real text/table — **not** as an image. Add one factual clause per service (what it produces), e.g. *Leave and attendance management — a register, a monthly summary, and rules applied the same way twice.* Do **not** split into per-service URLs (I-22); a pillar filter may hide rows visually but every service stays in the DOM (I-30).

*Method (Assess → Identify → Improve → Review):* keep as four H3 steps with one sentence each; **no `HowTo` schema** (I-06/Phase 5 5.3).
*Outcomes block, rewritten to stay honest:*
> What changes when the structure lands is a shorter list than most vendors advertise: payroll arrives on a predictable date, appraisals have criteria written in advance, and policy questions have a document to point at. We will not promise you a retention number we have not measured.

**CTA copy** `Start with the audit` · `See HR outsourcing pricing` · `Book the free audit`.
**JSON-LD** keep `Service` coverage inside `OfferCatalog`; add `BreadcrumbList`; **no per-service `Service` nodes** until U-3 pages exist.
**GEO** the pillar one-liners plus the 14-item table are the chunkable asset; keep them as text after each pillar H2.

---

## 8.4 `/what-we-are-building/` — Where AI Fits *(thinnest page, +3 content blocks)*

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (56) | `AI Automation for HR in Pakistan, Pre-Launch \| Emplowise` |
| Description (150) | `Emplowise is building AI automation for HR in Pakistan: a payroll engine, a performance insight layer and a policy co-pilot. All three are pre-launch.` |
| Primary keyword | AI automation for HR (in title, H1, `h2` field, intro) · secondary: *HR payroll automation*, *HR policy co-pilot* |

**Headings**
- H1: `Where AI fits: AI automation for HR, in the open.`
- H2: `What this page is, and what it is not.` *(new)* · `Where AI automation for HR will plug in.` · `How you will know when something ships.` *(new — fixes the thinness honestly)*
- H3: Payroll Engine · Performance Insight Layer · Policy Co-Pilot

**Body — rewritten**
*AEO block (44w):*
> Emplowise is building an AI automation division for HR: a payroll engine, a performance insight layer, and a policy co-pilot. All three are pre-launch and shown as static previews with no live data, so the confirmed remote HR services remain the offer available today.

*Framing:*
> This page is a status report, not a shopfront. All three modules are static previews of work in progress; none of them touches a live client record. If you need the function today, buy the service, not the software.

*Module copy (two concrete sentences each, all already true):*
> **Payroll Engine — In build.** A calculator for the parts of a Pakistani payroll cycle that are arithmetic rather than judgement: inputs, deductions, and a repeatable monthly run sheet. Static preview. No live data, no client records.
> **Performance Insight Layer — In build.** A way to read appraisal scores across a team without a spreadsheet ritual, using the same four-stage method the retainer uses. Static preview. No live data.
> **Policy Co-Pilot — In build.** A drafting assistant for policies and SOPs that outputs a document for a human to approve, then a version trail. Static preview. No live data.

*New closing block (replaces a sign-up prompt, since none is verified — I-10):*
> How you will know when something ships: we will change the status chip on this page from "In build" to "Live" and say so on the documentation hub. Until then, no waitlist, no countdown, no claim of availability.

**CTA copy** `See the confirmed HR services` · `Read the documentation hub`.
**JSON-LD** `WebPage` + `BreadcrumbList` only. **No `Product`/`SoftwareApplication`, no `availability`** (Phase 5 5.9).
**GEO** the phrase *"All three are pre-launch"* must appear in the first 60 words so an engine cannot describe the modules as available.

---

## 8.5 `/why-emplowise/` — Pricing & Reason-why

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (58) | `Why Emplowise Publishes HR Pricing in Pakistan \| Emplowise` |
| Description (153) | `Why Emplowise: remote HR for growing teams in Pakistan with pricing on the page. Starter PKR 40,000, Business PKR 75,000, Enterprise custom, audit first.` |
| Primary keyword | why Emplowise (in title, H1, `h2` field, intro) · secondary: *remote HR partner in Pakistan*, *HR outsourcing pricing in Pakistan* |

**Headings**
- H1: `Why Emplowise is the remote HR partner for growing teams.`
- H2: `One remote HR partner, with the price on the page.` · `What the price includes, and what it does not` · `Why Emplowise publishes HR pricing by headcount.` · `Every service that can sit inside a retainer.` · `Pick a package after the audit, not before.` · `How we compare with the alternatives.` *(new — the reason-why comparison, evidence-safe)*

**Body — rewritten**
*AEO block (52w):*
> Emplowise publishes HR outsourcing pricing in Pakistan by headcount: Starter is PKR 40,000 a month for up to 20 staff, Business is PKR 75,000 for up to 50, and Enterprise is custom-quoted above 50. Each is a monthly retainer; which services are included is confirmed in writing after your free HR audit.

*Why publishing the price:*
> The alternative most founders weigh is a senior in-house hire: a full salary, benefits, recruitment time, and one person holding the whole function. The other is ad hoc consultant hours, which are cheaper per hour and own nothing after the invoice. Emplowise sits between the two: a standing function at a monthly number you can read before you call anyone. That is the whole argument, and it is why the price is not gated.

*Includes / does not include (new two-column block, `.card-foot`):*
> **Included in the retainer:** the fourteen confirmed services that fit your pillar need, a named lead, monthly reporting, and the document trail. **Not included:** legal advice, tax representation, statutory audit, recruitment fees unless written in, and any outcome that depends on records we do not hold.

*Package copy (identical figures everywhere — I-19):*
> **Starter — PKR 40,000 a month.** Up to 20 employees. The minimum viable function: payroll inputs, leave register, core policies.
> **Business — PKR 75,000 a month.** Up to 50 employees. The core tier: adds performance cycles, reporting cadence and broader policy coverage.
> **Enterprise — custom.** Above 50 employees. Scoped monthly after the audit. *(Capacity strings use the exact config wording "Up to 20 employees" / "Up to 50 employees" — the audit fact-check compares against those literals.)*

*Decision guidance:*
> Pick after the audit, not before. Published prices are honest; your scope is not visible from the outside. The audit exists to settle which services you actually need before a tier is chosen.

**CTA copy** `Start with the free audit` · `Request a scoped quote` · `Read the pricing questions in the FAQ`.
**Links** point the pricing questions link at `/faq/#pricing` anchor; `OfferCatalog` prices must equal these figures (verified equal at audit time).
**JSON-LD** keep `Offer` × 3; **no `priceValidUntil`, no discount, no `AggregateOffer`, no ratings**; add `BreadcrumbList`.
**GEO** price is the number engines get asked for; the AEO block, the table and the prompts must carry identical tokens.

---

## 8.6 `/free-hr-audit/` — Conversion hub *(highest in-degree)*

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (55) | `Free HR Audit in Pakistan, Written Gap List \| Emplowise` |
| Description (148) | `Book a free HR audit in Pakistan. Four minutes to share headcount, payroll, performance and policy pain points, then a prioritised written gap list.` |
| Primary keyword | free HR audit in Pakistan (in title, H1, `h2` field, intro) · secondary: *HR gap assessment*, *HR diagnostic review* |

**Headings**
- H1: `A free HR audit in Pakistan, booked in four minutes.`
- H2: `What you get back.` *(new, before the form)* · Who are we speaking with? · What does the team look like? · When should we run it? · Review and submit. · `Your free HR audit: next steps.`

**Body — rewritten**
*AEO block (46w):*
> Emplowise offers a free HR audit for startups and SMEs in Pakistan. In about four minutes you share headcount, payroll, performance, and policy pain points; Emplowise returns a structured review and a prioritised written gap list. It is delivered remotely and carries no cost or obligation.

*Above-form block:*
> You leave with a written gap list — what is missing, what is risky, and what to fix first. That document is yours whether or not you take a retainer, and it is the reason the audit is not a demo.

*Form intro:*
> Four short sections, in this order: who we are speaking with, what the team looks like, when to run it, and a review before you send. The checks you see while typing run in your browser; nothing reaches us until you press submit, and no payroll data is asked for at this stage.
*Step labels:* `1 Who are we speaking with?` · `2 What does the team look like?` · `3 When should we run it?` · `4 Review and submit.` Keep headcount bands (1-10 / 11-20 / 21-50 / 51-100 / 100+), pain options (payroll / performance / policy / compliance / recruitment / reporting) and slots (Morning 9-12 / Afternoon 12-16 / Evening 16-19) exactly as configured.

*Next steps (ordered list, extractable):*
> 1 We read what you sent. 2 We confirm a slot. 3 We run the review and send the gap list in writing. 4 If it makes sense, we propose a package — after the audit, not before.

**CTA copy** `Book the free audit` · `Back to the site`. **Trust microcopy** (new, next to submit): `No cost. No obligation. No payroll data at this stage.` — mirrors the terms clause on sensitive records.
**JSON-LD** add `Service` with `serviceType: "Free HR audit"`, `areaServed: Pakistan`, `provider` → Organization, `offers` `{ "@type": "Offer", "price": "0", "priceCurrency": "PKR" }`; `BreadcrumbList`.
**GEO** "free" and "four minutes" are the two facts engines repeat; both now appear in the answer block, the H1 and the schema.

---
## 8.7 `/faq/` — Answer surface (flagship AEO page)

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (57) | `HR Outsourcing Questions, Answered With Facts \| Emplowise` |
| Description (151) | `Twenty-one answers to HR outsourcing questions in Pakistan: pricing from PKR 40,000, what a retainer includes, the free audit and the EmploStart tools.` |
| Primary keyword | HR outsourcing questions (in title, H1, the `h2` field which must equal the first FAQ category, and intro) · secondary: *Emplowise pricing answers*, *HR scope questions* |

**Headings**
- H1: `HR outsourcing questions answered with confirmed facts.`
- H2: `The short answer.` *(new lead heading; the config `h2` field itself must remain `HR outsourcing questions` so it still equals the first FAQ category — the audit asserts that equality, see §8.0a)* · HR outsourcing questions · Pricing and packages · The free HR audit · EmploStart · Ask the Emplowise assistant · `Ready for a real answer about your HR stack?`

**Body — rewritten**
*Lead block under H1 (42w):*
> The questions below are answered with confirmed facts only: prices published in PKR, scope confirmed in writing after your free HR audit, and no claims about results the team has not yet verified. Where something is unconfirmed, the answer says so plainly.

*Answer-rewriting rule (apply to all 21):* each answer starts by naming the subject so the block survives extraction — **"Emplowise's Starter package is PKR 40,000 a month for up to 20 staff…"** rather than "It's PKR 40,000…". Keep the 21 questions and grouping as built (filters are visual only — I-30). Worked example, the pricing question (46w, carried from Phase 5 §5.6):
> Emplowise costs from PKR 40,000 a month: Starter for up to 20 employees, Business at PKR 75,000 for up to 50, and a custom Enterprise quote above 50. Every package is a monthly remote retainer; exact inclusions are confirmed in writing after your free HR audit.

*Copy tone for the compliance question (unchanged substance, tightened):*
> No. Emplowise is an HR function, not a law firm. We write policies that reflect Pakistani labour practice and flag where a lawyer must sign off. A compliance guarantee would be a lie, and it is not something we sell.

**CTA copy** `Book the free audit` · `Open the free EmploStart tools`.
**JSON-LD** keep `FAQPage` with all 21 Q/A, each `acceptedAnswer.text` matching the visible answer **character-for-character**; add `BreadcrumbList`; **no `HowTo`**, no display promise (I-06).
**GEO** the FAQ is the single most AI-citable asset — self-contained answers naming the brand are what an engine can quote without context.

## 8.8 `/contact/` — Channels + GEO affordance

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (57) | `Contact Emplowise About Remote HR in Pakistan \| Emplowise` |
| Description (139) | `Contact Emplowise for remote HR in Pakistan. Email the team, book the free HR audit, or ask ChatGPT, Claude, Gemini or Perplexity about us.` |
| Primary keyword | contact Emplowise (in title, H1, `h2` field, intro) · secondary: *Emplowise contact details*, *remote HR support contact* |

**Headings** — H1 unchanged: `Contact Emplowise without a maze of forms.`
H2: `Tell us what needs to work better.` · `What happens next` · `Email us` · `Ask your favourite GPT about Emplowise` · `Resources` · *(drop the `Socials` H2 — see I-04/I-25/UX-01)*

**Body — rewritten**
*AEO block (43w):*
> To contact Emplowise, email hello@emplowise.com, book the free HR audit on the site, or ask a connected AI assistant using the prefilled prompts for ChatGPT, Claude, Gemini, or Perplexity. Direct phone and inbox details are confirmed in writing after your free HR audit.

*Lead:*
> Two routes work today: the audit form and the shared inbox. Both reach the same three people. A direct line is handed over in writing after the audit, because an unmanaged number is worse than none.
*What happens next (4-step ordered list, extractable):* we read it → we reply within the working week → we confirm a slot → you get the written gap list.
*Socials block:* **remove** the six placeholder links (I-04, I-25). Replacement copy: `A LinkedIn page is in progress. Until the address is real, it is not on this page.`
*GEO prompts block:* keep the four prefilled engine links; the embedded question stays exactly *"What is Emplowise, what remote HR services does it offer in Pakistan, and what are its package prices?"* so the answer engines read the same three facts the page states.

**CTA copy** `Book the free HR audit` · `Email hello@emplowise.com` · `Ask ChatGPT about Emplowise`.
**JSON-LD** add `Organization.contactPoint` `{ contactType: "customer support", email: "hello@emplowise.com", availableLanguage: "English" }`; **no `telephone`, no `sameAs`** (I-04).
**GEO** this page *is* the GEO surface; the only change is that it stops pointing at empty profiles.

## 8.9 `/emplostart/` — Free product launcher *(different audience)*

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (54) | `Free ATS Resume Checker and 6 Career Tools \| Emplowise` |
| Description (153) | `EmploStart is a permanently free career app: a free ATS resume checker, interview prep, profile builder and three planning modules. Runs in your browser.` |
| Primary keyword | free ATS resume checker (in title, H1, `h2` field, intro) · secondary: *career pivot planning*, *mock interview practice* |

**Headings** — H1 unchanged: `A free ATS resume checker for career pivoters and job seekers.`
H2: `Free ATS resume checker and five more free tools.` · `The EMPLOWISE and START prompt library: 14 letters, 14 prompts.` · `Start with a questionnaire, your LinkedIn profile, or your CV.` · `Local by default. AI only when you choose it.` · `Free because the HR work funds it.` · `Hiring soon? Run the free HR audit before the first start date.`

**Body — rewritten**
*AEO block (46w):*
> EmploStart is a permanently free career app from Emplowise. It includes a free ATS resume checker, mock interview practice, a profile builder, and three planning modules — six tools that run in your browser with no account and optional AI, funded by Emplowise's remote HR services.

*Why it is free (new block, keeps the honesty that makes the claim believable):*
> EmploStart costs nothing because it is not the product. Emplowise is paid for by retained HR work; the career tools are the part of that expertise we give away. Six modules, no account, no upload, no countdown timer.
*Tool line-ups (H3 each, one factual sentence):* **ATS Resume Analyzer** — scores a CV against keyword and structure rules and lists the fixes. **Interview Prep** — mock questions with a scored answer rubric. **Profile Builder** — turns a questionnaire into a structured profile. **Career Pivot Planner · Career Reimagination Lab · Market Assessment** — the three planning modules.
*Prompt library:* keep all 14 (P01–P14, EMPLOWISE + START) with one line each on what the prompt produces.
*Local-first copy:* `Runs in your browser. Nothing is uploaded. AI stays off until you switch it on. Shared PC mode keeps the session only.`
*Pledge band:* keep SDG 4 / 8 / 10 alignment **and** the sentence *"Voluntary alignment only. This is not a UN endorsement, certification, or partnership."*

**CTA copy** `Open EmploStart free` (primary, → `https://diocese-trees.github.io/EmploStart/`) · `Open the 14-prompt library` · `Book the free HR audit`.
**Links** product link stays pointing at the live EmploStart deployment; no invented app-store URLs.
**JSON-LD** add `WebApplication` — `name: "EmploStart"`, `applicationCategory: "BusinessApplication"`, `operatingSystem: "Web"`, `url` → product, `offers { price: "0", priceCurrency: "PKR" }`, `featureList` = the six modules; **no users/rating/download counts** (none measured); `BreadcrumbList`.
**GEO** keep the free/no-account/local wording byte-identical to the product page once I-09 is fixed there, or engines will see two products.

## 8.10 `/company-profile/` — Buyer-facing fact sheet (indexable, thickest)

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (55) | `Remote HR Company Profile: The 2026 Edition \| Emplowise` |
| Description (152) | `The Emplowise remote HR company profile in one document: who we serve, the four-stage method, fourteen services, published retainers and the named team.` |
| Primary keyword | remote HR company profile (in title, H1, `h2` field, intro) · secondary: *Emplowise company document*, *HR service provider profile* |

**Headings** — H1 unchanged: `A remote HR company profile written for buyers, not archives.`
H2: `What this profile includes.` · `The gap Emplowise was built to fill.` · `Four buying situations, not four demographics.` · `What is in scope, and what is not.` · `Four stages, one sequence, four documents.` · `Fourteen services across three pillars.` · `Published retainers, billed monthly.` · `Three people own the work.` · `Three kinds of measurement, never merged.` · `Take the profile, or start with the audit.`

**Body — rewritten**
*AEO block (45w):*
> The Emplowise company profile is a single 2026 document covering who it serves (startups, SMEs, and emerging talent), its four-stage method, published monthly retainers of PKR 40,000, PKR 75,000, and a custom Enterprise quote, and the named team owning each part of remote HR delivery.

*Lead:*
> This is the page to send a founder, a finance lead or a procurement inbox. It carries the same facts as the .docx download, so nobody reconciles two versions of the company.
*Buying situations (rewrite of the four, keeping the substance):* **"We just hired number twenty-one."** · **"Payroll runs, nobody trusts it."** · **"Every policy lives in someone's head."** · **"We need an HR owner, not an HR hire."**
*Measurement rule (keep the three kinds separate, verbatim in meaning):* delivery metrics, quality metrics and business metrics are reported apart and never blended into one flattering number.
*Download block:* `Company Profile 2026 (.docx, editable)` — keep `?v=` cache versioning.

**CTA copy** `Download the 2026 profile` · `Book the free HR audit` · `Read the portfolio`.
**JSON-LD** keep `WebPage` + `isPartOf WebSite` + `about ProfessionalService`; add `BreadcrumbList`; add `dateModified` = the real edition date once tracked; `version: "2026"`.
**GEO** the profile is the canonical "facts about the company" surface — its figures must be the same numbers the home page, pricing page and schema publish.

## 8.11 `/portfolio/` — Shipped-work evidence (indexable)

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (59) | `Remote HR Portfolio of Shipped Work, Repo Proof \| Emplowise` |
| Description (143) | `A remote HR portfolio listing only shipped work: the platform, the career toolkit, the audit wizard and the brand system, each with repo proof.` |
| Primary keyword | remote HR portfolio (in title, H1, `h2` field, intro) · secondary: *shipped HR platform work*, *Emplowise work evidence* |

**Headings** — H1 unchanged: `A remote HR portfolio that lists shipped work only.`
H2: `What this portfolio documents.` · `Four shipped artifacts, each with repository proof.` · `Supporting systems, also in the repository.` · `The case study standard, written down.` · `Inspect the work, then start with the audit.`

**Body — rewritten**
*Lead (58w, evidence-only AEO block):*
> This portfolio lists work that exists in a repository, not work that exists in a slide. It documents four shipped artifacts, the supporting systems behind them, and the standard a future client case study will have to meet before it is published here. Emplowise has no published client case studies yet, and this page does not invent any.

*Evidence standard (four bullets, substance preserved, tightened):* **Repo proof or nothing.** **Behaviour over assertion** — a running demo counts for more than a description. **No borrowed proof** — no client logos, testimonials, revenue figures or awards until a client authorises them in writing. **Nothing implied** — a planned feature stays off this page.
*Shipped artifacts (the four already documented, no new names):* > **A1. Phase I web platform** — 14 routes from one controller, strict CSP with a single hashed inline script, self-hosted fonts, the four-step audit wizard, an 18-intent assistant; **A2. EmploStart: standalone, local-first career app** — six modules, deterministic local engines, no account, no payment, no advertising; **A3. Free HR Audit diagnostic**; **A4. 2026 brand system**. All four are labelled *Shipped* today and keep that label. Each keeps its existing "repo proof" line — the config names proof paths such as `routes/web.php`, `app/Console/Commands/ExportStatic.php`, `tests/Feature/`, `.github/workflows/ci.yml`. Do **not** turn those paths into outbound GitHub URLs unless the client confirms which repositories are public (Phase 1 found no outbound repo URLs on the live page).

**CTA copy** `Read the company profile` · `Book the free HR audit` · `Download the portfolio (.docx)`.
**JSON-LD** `WebPage` + `BreadcrumbList`. **No `Review`, no `AggregateRating`, no `CreativeWork` claims about client projects** (Phase 5 §5.12).
**GEO** the admission "no published client case studies yet" is a trust signal worth keeping in the first 60 words — engines that check claims find it consistent.

## 8.12 `/docs/` — Documentation hub (crawl hub, highest in-degree)

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (59) | `Emplowise Documentation, Downloads and Editions \| Emplowise` |
| Description (154) | `Every Emplowise document in one place: brand kit, company profile, portfolio, pitch deck and engineering notes, with live editions and editable downloads.` |
| Primary keyword | Emplowise documentation (in title, H1, `h2` field, intro) · secondary: *brand kit downloads*, *company profile document* |

**Headings** — H1 unchanged: `Emplowise documentation, with live editions and editable downloads.`
H2: `Emplowise documentation index` · `Brand system and writing rules.` · `What Emplowise sells, and the proof behind it.` · `The free career library candidates actually use.` · `How the site is built and shipped.` · `Notes that live with the code.` · `Need a document this hub does not carry?`

**Body — rewritten**
*Lead (53w, AEO answer block):*
> Every public Emplowise document lives here with its current edition marked, so a client, candidate or contractor works from the same file the team uses. Downloads are editable rather than flattened, and each carries a version stamp. The hub covers four groups: brand rules, commercial facts, the free career library, and engineering notes.

*Group copy:* **Brand** — kit, guidelines, writing rules, and the exact fonts/colours in use (Phase 7 §7.1). **Commercial** — company profile, portfolio, pitch deck, pricing terms. **Career** — EmploStart library and the 14 prompts. **Engineering** — build and export route, tool stack, website breakdown.
*Format labels:* annotate each download with format and edition, e.g. `Brand Kit .zip · 2026 edition`, `Pitch Deck .pptx · 2026 edition` — no file sizes until re-measured after the rewrite.
*Closing:* `If a document is out of date, the edition label is wrong. Say so at hello@emplowise.com and the hub gets fixed.`

**CTA copy** `Download the brand kit` · `Get the company profile` · `Ask for a missing document`.
**JSON-LD** `WebPage` + `BreadcrumbList` + `Dataset`-free (do not over-type a documents index).
**GEO** keep all 8 downloads as real `<a href>` links with `?v=` so both crawlers and engines can resolve the primary files.

## 8.13 `/terms/` — Legal (**clauses unchanged in substance**)

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (55) | `Emplowise Terms of Service for HR Retainers \| Emplowise` |
| Description (150) | `The terms covering the Emplowise website, the free HR audit and monthly remote HR retainers. Plain language, Pakistan law, scope confirmed in writing.` |
| Robots | `index,follow` (unchanged) · `datePublished`/`dateModified` = **2026-11-22** (verified on-page) |
| Primary keyword | Emplowise terms of service — **not** in the current H1/H2/intro, and `/terms/` is *excluded* from the `EmplowiseSeoAudit` ROUTES list, so the gate does not fail today (see §8.0a). Secondary: *remote HR service terms*, *HR retainer agreement Pakistan* |

**Headings** — H1 unchanged: `Terms of service, written to be read.` Eight H2 blocks retained 1:1 so every anchor and TOC entry survives: `Who we are` · `Using this site` · `The free HR audit` · `Retainers and scope` · `No guarantee of a business outcome` · `Intellectual property` · `Liability` · `Governing law and changes`.

**Body — rewritten for clarity only, obligation-for-obligation:**
> **Who we are.** These terms bind you and Emplowise HR Services ("Emplowise", "we"), a remote HR provider for businesses in Pakistan, contactable at hello@emplowise.com. They cover this website, the free HR audit and any paid retainer. They do not override a signed proposal or scope document: where the two conflict, the signed document controls.
> **Using this site.** The site is informational. It describes our services, method and published starting prices. It is not legal, tax or employment advice, and it is not a binding offer or quote. Prices, capacities and inclusions are indicative until confirmed in writing after your free HR audit. We may correct errors and change published prices at any time.
> **The free HR audit.** The audit is free and creates no obligation to buy. You receive a structured review of the information you share and a prioritised gap list. It is a diagnostic conversation, not a compliance certification, and it does not replace legal advice, a statutory audit or a review of your full records. Do not send payroll data, identity documents or other sensitive records until a secure route is agreed.
> **Retainers and scope.** Paid work runs on a monthly retainer. Scope, start date, named lead and exclusions are confirmed in writing before work begins. Prices are in Pakistani rupees and exclude applicable taxes unless the proposal states otherwise. Either party may end the retainer on the notice period stated in the proposal.
> **No guarantee of a business outcome.** We commit to the method, the deliverables and the response times in your scope. We cannot guarantee a hiring result, a revenue target or a regulatory outcome, because those depend on decisions and records outside our control.
> **Intellectual property.** Site content — text, templates and design — belongs to Emplowise or its licensors. You may read it and share links; you may not resell it or present it as your own. Templates and documents created for a client are licensed to that client for internal use during and after the engagement, as set out in the proposal.
> **Liability.** To the extent permitted by law, Emplowise is not liable for indirect or consequential loss, lost profits or loss of data. Total liability for a claim is limited to the fees paid for the month in which the issue arose. Nothing here limits liability that cannot lawfully be limited.
> **Governing law and changes.** These terms are governed by the laws of Pakistan, and the courts of Pakistan have jurisdiction. Changes are reflected in the date at the top of this page; material changes are flagged on the site before they take effect.

**Schema** add `WebPage` + `datePublished`/`dateModified` `2026-11-22` + `BreadcrumbList`; **no `FAQPage`/`HowTo`** (Phase 5 §5.11).

## 8.14 `/privacy/` — Legal (**clauses unchanged in substance**)

**Metadata**
| Field | Rewritten value |
|---|---|
| Title (55) | `Emplowise Privacy Policy and Cookie Choices \| Emplowise` |
| Description (145) | `How the Emplowise privacy policy works: what we collect, cookies and local storage, processors, retention, and how to access or delete your data.` |
| Robots | `index,follow` (unchanged) · `datePublished`/`dateModified` = **2026-11-22** |
| Primary keyword | Emplowise privacy policy — title now carries it; like `/terms/` this route is outside the audited ROUTES list (§8.0a). Secondary: *HR audit data privacy*, *cookie policy Pakistan* |

**Headings** — H1 unchanged: `Privacy, in plain language.` Retain all eight blocks: `What we collect` · `Why we use it` · `Cookies and local storage` · `Sharing and processors` · `How long we keep it` · `Your choices and rights` · `Security and international processing` · `Contact and changes`.

**Body — rewritten for clarity only:**
> **What we collect.** When you book a free HR audit we collect what you type: name, work email, company, headcount band, the areas you want reviewed and any notes. If you email us, we keep that message and our reply. Like most sites, our host may record technical details such as the requested page, browser type and IP address in server logs, used to keep the site working and secure.
> **Why we use it.** Audit responses are used to prepare and deliver the audit, to reply to you, and to record what was agreed. Technical logs are used to operate and protect the site. We do not sell personal data and we do not use it for advertising. Analytics and marketing storage stay off until you switch them on in the cookie panel.
> **Cookies and local storage.** One essential preference stores your cookie choice for up to 180 days, in a first-party cookie and in local storage so the panel does not reappear on every page. If you allow analytics or marketing, the relevant measurement may load later. **No third-party analytics or advertising tags are installed today.** You can change or withdraw your choice through the cookie settings link in the footer.
> **Sharing and processors.** We share data only with providers that help us run the site and reply to you — hosting and email form delivery — and they act on our instructions, not for their own marketing. We may disclose information where the law requires it or to protect the rights and safety of Emplowise, its clients or others.
> **How long we keep it.** Audit responses are kept while we assess fit and for a reasonable period afterwards so follow-up questions can be answered. Email is kept as long as needed to manage the relationship. You can ask for deletion at any time unless we must retain a record for a legal or accounting reason.
> **Your choices and rights.** You can request a copy of the personal data we hold, ask us to correct it, or ask us to delete it, and you can withdraw consent for optional cookies at any time. Email hello@emplowise.com; we may ask a clarifying question to confirm we are dealing with the right person.
> **Security and international processing.** We use HTTPS, access controls and reputable hosting providers. No method of transmission or storage is perfectly secure, so please do not send sensitive records until a secure route is agreed. Providers may process data outside Pakistan, where we rely on their contractual safeguards and keep the set of providers small.
> **Contact and changes.** Questions about this policy go to hello@emplowise.com. If we change the policy, we update the date at the top of this page.

**Schema** as terms. **Copy change required alongside this page:** privacy names "analytics and marketing" as optional — the truthful current state is *no third-party analytics installed* (I-26 dependency: revisit only once GA4 is actually deployed in Phase 6, and change both pages together).

## 8.15 `/pitch-deck/` — Investor deck (**stays `noindex,follow`**)

**Metadata**: Title (60) `Emplowise Pitch Deck: Eight Slides, One Question \| Emplowise`; description (150) `The Emplowise pitch deck in eight slides: product, problem, method, pricing, market wedge, go-to-market, shipped proof and roadmap. Shareable by link.`; config `h2` field stays `What the Emplowise pitch deck answers.` (carries the primary keyword, as the gate requires); **`robots: noindex,follow` retained**, absent from `sitemap.xml` retained (I-01 closed as intentional); keep the 19 image `alt`s.
**Headings**: H1 `The Emplowise pitch deck, eight slides, one question each.` (unchanged, gated keyword present) — the eight slide H2s are re-cut as questions: *Is this a real market?* · *Why does HR break at thirty staff?* · *What is the method?* · *What does it cost?* · *Who else serves this?* · *How does a client enter?* · *Is the platform shipped?* · *What happens next?* Closing H2: `One free intake, one named lead, one gap map.`
**Body**: no new claims; keep "shipped platform, not promised platform" and the no-client-case-study position. Add one caption line: `This deck is shareable by direct link and is not indexed by search engines.`
**CTA**: `Download the deck (.pptx)` · `Book the free HR audit`. **JSON-LD**: keep `WebPage`; no `BreadcrumbList` needed on a noindex page (avoids an orphan crumb).

## 8.16 Shared elements rewritten once, applied site-wide
| Element | Rewritten |
|---|---|
| Header nav labels | `Meet Emplowise` → **`Home`** for the item pointing to `/` (the logo already carries the brand; two labels for `/` is a findability problem, Phase 2 I-11 family). Rest unchanged: Our Story · What We Do · Meet The Team · Why Us · Where's AI · EmploStart · Contact Us · **[Free HR Audit]** |
| Footer "Socials" | heading + six placeholder links **removed**; replaced by `Contact` column: `hello@emplowise.com` + `Book the free HR audit` (UX-01, I-25) |
| Footer columns | Company / Resources / **Legal** (Terms · Privacy · Cookie settings) — links unchanged otherwise |
| Footer tagline | keep: *"People analytics without bias, so CEOs can set new standards."* — brand line, not a measurable claim |
| Copyright | `© 2026 Emplowise HR Services. All rights reserved.` |
| OG set | per-page `og:title` = page title + ` | Emplowise`; `og:description` = meta description; `og:image` stays the logo **until UX-08 delivers page-specific brand images**; `twitter:card=summary_large_image` |
| `robots.txt` / `sitemap.xml` | sitemap keeps the 14 indexable URLs; add `<lastmod>` **only with real dates** (I-03); legacy stub URLs keep canonical-to-target behaviour while host-level 301s are pending (I-02) |
| `Organization` node | `url` slash-aligned; `name: "Emplowise HR Services"`; `legalName` same; `areaServed: Country(Pakistan)`; `knowsAbout` = the 14 services; `contactPoint` email only; `sameAs` **absent** |

## 8.17 Master JSON-LD template (all values verified; nothing invented)
```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "@id": "https://diocese-trees.github.io/Emplowise-Website-Phase-I/#org",
      "name": "Emplowise HR Services", "legalName": "Emplowise HR Services",
      "url": "https://diocese-trees.github.io/Emplowise-Website-Phase-I/",
      "logo": { "@type": "ImageObject", "url": "…/img/logo-primary.png" },
      "description": "Remote HR services in Pakistan for startups and SMEs.",
      "areaServed": { "@type": "Country", "name": "Pakistan" },
      "knowsAbout": [ "Complete recruitment", "Employee onboarding", "HR documentation and employee records",
        "Leave and attendance management", "HR policies and SOPs", "Payroll", "Legal and compliance support",
        "Performance support", "Employee relations and conflict support", "Organizational assessments",
        "Monthly HR reporting", "Ongoing HR consultation", "Specialist HR consultant support", "Dedicated HR representative" ],
      "contactPoint": [{ "@type": "ContactPoint", "contactType": "customer support",
                         "email": "hello@emplowise.com", "availableLanguage": "English" }] },
    { "@type": "WebSite", "url": "https://diocese-trees.github.io/Emplowise-Website-Phase-I/",
      "name": "Emplowise", "inLanguage": "en-GB", "publisher": { "@id": "…/#org" } },
    { "@type": "BreadcrumbList", "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://diocese-trees.github.io/Emplowise-Website-Phase-I/" },
      { "@type": "ListItem", "position": 2, "name": "<Page>", "item": "<page canonical, trailing slash>" } ] },
    { "@type": "WebPage", "url": "<page canonical>", "name": "<H1>", "isPartOf": { "@id": "…/#website" },
      "about": { "@id": "…/#org" }, "inLanguage": "en-GB" }
  ]
}
```
Per-page additions only as specified: `FAQPage` (`/faq/`), `Service` price 0 (`/free-hr-audit/`), `WebApplication` (`/emplostart/`), `Person` × 3 (`/what-we-are/`), `datePublished`/`dateModified` `2026-11-22` (legal only).

## 8.18 Coverage, propagation and validation
**Coverage check — all 15 inventoried public pages rewritten:** `/`, `/what-we-are/`, `/what-we-do/`, `/what-we-are-building/`, `/why-emplowise/`, `/free-hr-audit/`, `/faq/`, `/contact/`, `/emplostart/`, `/company-profile/`, `/portfolio/`, `/docs/`, `/terms/`, `/privacy/`, `/pitch-deck/`. Non-page surfaces intentionally out of scope: the 5 legacy redirect stubs, `sitemap.xml`, `robots.txt`, the 8 downloads, and the EmploStart product deployment (I-09).
**Fixes propagated:** I-02 (stubs noted, host 301s deferred to Phase 6) · I-03 (legal dates only) · I-04/I-25 (socials removed from copy + schema) · I-05 (OG descriptions done, images tracked as UX-08) · I-06 (no `HowTo`, no promise) · I-08 (no `Person.image`) · I-11 (nav label split) · I-13 (slash-aligned `url`) · I-19 (identical PKR figures on 4 surfaces) · I-22 (no URL split) · I-30 (filters visual only).
**Consistency gates:** the 3 `Offer` prices == pricing page table == home pricing band == FAQ answer == engine prompt text; `Organization.description` == home AEO sentence 1; `FAQPage.text` == visible answers.
**Truthfulness audit of this rewrite:** zero client names, zero logos, zero testimonials, zero ratings, zero percentages, zero traffic or savings claims, no new price, no new service, no phone number, no profile URLs, no repository URLs, no invented founding date.
**Limitations:** (a) this is copy written from a static crawl — it has not been A/B tested and no ranking, traffic or conversion lift is claimed or forecast (I-26); (b) titles/descriptions are length-optimised but not validated against real SERP truncation widths; (c) `dateModified` remains absent on 12 pages because no real change date exists yet — deliberately not fabricated; (d) EmploStart product-page copy (separate deployment) is **not** rewritten here; (e) none of this was applied to `/data/emplowise` — the repo, its git state and the backups are untouched.

