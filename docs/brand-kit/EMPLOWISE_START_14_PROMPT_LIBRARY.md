# EMPLOWISE × START: the 14-prompt library, 2026

Fourteen letters, fourteen prompts. Every letter of the two-word acronym carries
exactly one prompt, so the library reads as a map of the whole job-search path
rather than a bag of tips. **EMPLOWISE** (P01–P09) gets you shortlisted and into
the interview. **START** (P10–P14) helps you ace the interview, land a fair
offer, and decide what comes next. Each prompt is a complete, rubric-driven
instruction set that runs on one local candidate record, asks only for what a
real recruiter would ask, and refuses to invent anything it was not given.

## 1. How the library is built

Two tracks, one spine. The five funnel stages the prompts serve are *Get
Shortlisted*, *Get Interview*, *Win Interview*, *Land Offer* and *Pivot & Grow*.
Nine prompts cover the first two stages, five cover the last three.

- **EMPLOWISE, P01–P09:** get shortlisted and into the interview.
- **START, P10–P14:** ace interviews, land fair offers, and pivot.

Three decisions shape every one of them:

1. **One record, many prompts.** The candidate vault holds a single profile and
   each prompt projects only the fields it needs, so a person fills the boring
   parts once instead of twelve times.
2. **A completeness gate on every prompt.** Either the prompt asks its questions
   before drafting (`ask_first`) or it writes a first draft immediately and
   flags what is missing instead of blocking (`direct_draft`).
3. **Honest scope.** Two prompts need facts that are not in the record and say
   so; the other twelve work entirely from what you paste.

## 2. Getting in: the three-lane candidate intake

Nobody starts with a blank form. The intake offers three independent lanes and
any one of them is enough to reach a useful first result; people switch lanes
freely and the vault merges what they give.

### Lane 1: the diagnostic test

Twelve short questions, about two to three minutes, no document required. The
answers set seven readiness dimensions and place the candidate in one of four
bands — **Foundation**, **Developing**, **Competitive** and
**Evidence-Backed** — rather than a fake score. Bands are chosen deliberately: a
one-decimal readiness number would imply a measurement instrument the app does
not have, so the library reports which band the evidence supports and what would
move it up.

### Lane 2: LinkedIn

Paste your profile URL and the profile text you see in the browser, and the
prompt questions that follow fill positioning, skills and history from it. The
disclosure is explicit and stays explicit: EmploStart does not scrape LinkedIn
and never has. It reads only what you paste, and it says so on the same screen
that asks for the URL.

### Lane 3: the CV

Upload a `.docx`, `.txt` or `.md` file and the local extractor recovers the text
without a network call. PDFs have no local extractor in this build, so the repair
path asks for the text pasted out of the document instead of pretending the
upload worked. Either way, the parse produces a draft profile and a short set of
delta questions — only the gaps the parser could not resolve.

### The vault behind all three lanes

Storage is local by default: the profile lives in this browser and nowhere else.
A session-only mode for a shared or lab computer keeps the record in tab storage
and clears any persistent copy the moment it is chosen. Field precedence is
fixed — manual, then `cv_parse`, then `linkedin_parse`, then the test — so a
machine-read value never overwrites something the person typed by hand, and every
import shows a parse preview before anything is written. Each prompt then carries
a 20 KB payload ceiling so one oversized paste cannot silently truncate the rest.

## 3. What the 2026 research changed

Five findings moved this library away from the prompt collections that circulate
in 2023-era career content.

Keyword counting is no longer the gate. Semantic and embedding-based screening
reads a resume for meaning and role fit, so the prompts normalise skill variants
and write for the underlying requirement instead of stuffing exact-match terms;
surface vocabulary still matters, but as a secondary concern inside a semantic
read.

Recruiter AI-slop fatigue is now a hiring constraint. Because model-written
generic copy floods the top of funnels, every prompt carries an explicit negative
constraint section: no invented metrics, employers or dates, and a named list of
banned clichés. Several prompts also carry a weak-versus-strong example so the
model has something concrete to avoid, not just a rule.

Functional rubrics beat decorative personas. The templates do not ask the model
to roleplay a whimsical character; they assign a working discipline — hiring
evidence analyst, compensation analyst, ATS parser auditor, offer negotiator —
and then define the rubric it must score against, with weights where weights
matter: evidence 40, recency 25, relevance 20, verifiability 15 in the inventory
prompt, and 2024 to 2026 work ranked above older work.

Interview evidence is scored, not vibes. The interview prompts use structured
one-to-five rubrics across situation, task, action and result, so a practice
round returns a number with a reason attached and a named weakness to fix. The
first-ninety-days prompt is built on the same logic: *Learn* in days one to
thirty, *Contribute* an early win by day sixty, *Own* a workflow by day ninety.

Abstention is a required behaviour. Analysis runs before conclusions, and a
missing fact is written as `[NOT PROVIDED]` while an unverifiable one is written
as `[CANNOT VERIFY]`, often with the exact search a person should run instead. A
plausible number that cannot be sourced counts as a failure, not a good answer.

Pasted text is treated as untrusted data. Because a CV or a job description can
contain instructions of its own, prompts wrap candidate material in tagged
delimiters and escape angle brackets before sending, so pasted text cannot steer
the model or break out of its data block. That is a prompt-injection control, and
it is stated to candidates as one.

## 4. The library at a glance

| Pillar | Letter | ID | Prompt | Gate | Web fallback | Funnel stage |
| --- | --- | --- | --- | --- | --- | --- |
| Evidence & Career Inventory | E | P01 | Build my evidence inventory | ask_first | No | Get Shortlisted |
| Market Value Assessment | M | P02 | Check what this role pays | ask_first | Yes | Get Shortlisted |
| Positioning & JD Semantic Decoder | P | P03 | Decode what this job really wants | ask_first | No | Get Shortlisted |
| LinkedIn & Digital Profile Architect | L | P04 | Rewrite my LinkedIn profile | direct_draft | No | Get Shortlisted |
| Optimized Human & ATS Resume Strategist | O | P05 | Rebuild my resume end to end | ask_first | No | Get Shortlisted |
| Work Proof & Portfolio Case Studies | W | P06 | Turn my work into case studies | direct_draft | No | Get Shortlisted |
| Instant Parser-Safe ATS Export | I | P07 | Export a parser-safe resume | direct_draft | No | Get Shortlisted |
| Strategic Outreach, Referrals & Cover Letters | S | P08 | Write outreach that gets replies | direct_draft | No | Get Interview |
| Error & Rejection Diagnostics | E | P09 | Diagnose why I am not getting replies | ask_first | No | Get Interview |
| Structured Interview & Claim Defensibility | S | P10 | Practise a scored interview | direct_draft | No | Win Interview |
| Take-Home, Case & 30-60-90 Day Pitch | T | P11 | Plan my take-home and first 90 days | direct_draft | No | Win Interview |
| Ask & Fair-Wage Offer Negotiation | A | P12 | Negotiate the offer fairly | ask_first | No | Land Offer |
| Reskilling, Credentials & Scholarship ROI | R | P13 | Check if this course is worth it | ask_first | Yes | Pivot & Grow |
| Trajectory: Career Pivot, Reimagination & Venture | T | P14 | Plan a pivot or stress-test a venture | ask_first | No | Pivot & Grow |

## 5. The fourteen prompts

Each entry states what it does, how its gate behaves, and whether it depends on
a web fallback. "No web fallback" means the prompt is designed to finish from the
record and the pasted material alone.

### P01 — E: Build my evidence inventory

Separates claimed skills from demonstrated outcomes, weights recent work, and
lists the proof still missing, ordered as evidence, recency, relevance and
verifiability. `ask_first`: it asks for one result you are proud of with the
number, who could confirm it, and how the last twelve months were actually spent
before writing anything. No web fallback.

### P02 — M: Check what this role pays

A six-step compensation read: local and remote ranges, what drives and what
suppresses them, a title-inflation check against your real scope, and a
confidence line for every figure. `ask_first`, because team size, budget or
revenue influence and the deadline on your decision change the answer. This
prompt **does** carry the web fallback: market bands are not in the record, so it
names what needs looking up and gives the exact query to run, writing `[CANNOT
VERIFY]` where it cannot ground a number.

### P03 — P: Decode what this job really wants

Reads a job description for the pain behind the requirements and the skill
variants that mean the same thing in different employers' vocabulary, then maps
you into a Strong, Partial or Gap matrix. `ask_first` on two things a posting
never says: team size and reporting line, and why the role exists now. No web
fallback.

### P04 — L: Rewrite my LinkedIn profile

Produces a recruiter-search headline of 120 characters or fewer, an About section
that reads as written by a person, reframed experience and a featured-proof list,
all from verified facts. `direct_draft`: the rewrite arrives immediately and the
two questions — the words recruiters should find you by, and plain, warm or
formal tone — are refinements rather than a gate. No web fallback.

### P05 — O: Rebuild my resume end to end

A five-step overhaul: job analysis, positioning, the rewrite itself, an
eight-metric audit, and a defensibility check on every claim you would have to
stand behind in an interview. Analysis is enforced before drafting. `ask_first`
for the current resume text, one or two pages, and anything that must survive the
rewrite such as a certification or a gap explanation. No web fallback.

### P06 — W: Turn my work into case studies

Converts projects, duties and freelance work into Problem, Context, Action,
Verified Outcome briefs you can put in front of a hiring manager. `direct_draft`,
with two questions held for the polish pass: which project you would happily walk
through, and what exists to prove it — file, repo, dashboard or client note. No
web fallback.

### P07 — I: Export a parser-safe resume

Generates single-column, variant-normalised plain text or LaTeX built for parser
accuracy, with zero commentary, greeting or filler that a human would enjoy and
an ATS would choke on. `direct_draft`; the two questions are the output format
(plain text or Overleaf LaTeX) and which contact line to print. No web fallback.

### P08 — S: Write outreach that gets replies

Cold emails, referral asks of 80 words or fewer, LinkedIn messages and cover
letters written so they cannot be swapped onto another candidate.
`direct_draft`, asking afterwards who you are writing to and what real connection
exists — shared school, event, colleague, a specific comment on their work. No
web fallback.

### P09 — E: Diagnose why I am not getting replies

A recruiter-style teardown of the CV, the job description and the profile that
names parser drops, silent rejections and the exact cuts to make first.
`ask_first`, because the diagnosis depends on volume and period, where applications
actually stop, and any feedback genuinely received rather than imagined. No web
fallback.

### P10 — S: Practise a scored interview

Behavioural questions mapped to the posting's competencies, each scored on a
structured one-to-five rubric across situation, task, action and result, plus the
hard follow-ups a hiring manager would use to test whether your claims hold.
`direct_draft`, then asks which stage you are preparing for and which story you
least want to be asked about. No web fallback.

### P11 — T: Plan my take-home and first 90 days

Builds a work-sample structure and a realistic *Learn* (days 1–30), *Contribute*
(days 31–60), *Own* (days 61–90) pitch, along with the five questions to ask the
employer about the brief. It never invents internal numbers, baselines or
headcount. `direct_draft`, asking for the brief itself, the hours expected and
the requested format. No web fallback.

### P12 — A: Negotiate the offer fairly

Audits total compensation rather than base salary, flags underpayment risk,
frames your alternatives and your walk-away point, and drafts both the
counter-offer email and the call script. `ask_first`, deliberately: base, bonus,
allowances, leave and equity, your real alternatives, and the number below which
you would decline are the whole negotiation. It works only from the offer details
supplied and never invents market rates. No web fallback.

### P13 — R: Check if this course is worth it

Filters courses, certifications and funding by demonstrated hiring ROI instead of
marketing claims, with no invented deadlines, seats or placement guarantees.
`ask_first` for the shortlist with costs and durations, what you can spend without
borrowing, and the study hours available per week. Like P02, this prompt **does**
carry the web fallback, because admission deadlines, fees and outcomes change and
must be checked.

### P14 — T: Plan a pivot or stress-test a venture

Two modes in one prompt: a transferable-skills pivot blueprint, or a venture
stress-test that writes its assumptions and risks down instead of cheering.
`ask_first` for which mode, the time and money you can spend before the next
income, and hard limits such as location, care duties or immigration status. No
web fallback.

## 6. Rules the whole library follows

- **Palette.** Navy `#081B3E`, Teal `#0D9488`, Deep Teal `#0F766E`, Aqua
  `#5EEAD4`, Ice `#F0F9F9`, Slate `#1E293B`. Same 2026 brand kit as the site and
  the rest of the Office deliverables; no neon glow, no decorative gradient in
  body copy.
- **Banned clichés.** *results-driven*, *dynamic*, *passionate*, *hardworking*,
  *team player*, *proven track record*, *delve*, *leverage*. They appear in the
  negative-constraint block of every prompt, and in the output checks, so a
  draft containing them is not finished.
- **Sustainability alignment is voluntary.** The library declares alignment with
  UN SDG 4 (quality education), SDG 8 (decent work and economic growth) and SDG
  10 (reduced inequalities); P02, P12, P13 and P14 also carry SDG 10 because they
  touch pay and access. This is voluntary alignment only — no UN endorsement,
  certification or partnership is claimed or implied.
- **Fair Jobs and Fair Wages Pledge.** The negotiation and market-value prompts
  exist to move pay conversations toward published, defensible ranges, consistent
  with the pledge Emplowise supports in its own hiring and client guidance.
- **Nothing is fabricated.** No salary, deadline, admission date, score,
  employer, date or metric is invented. Missing facts are `[NOT PROVIDED]`,
  unverifiable ones are `[CANNOT VERIFY]`, and the prompt says what to look up.
- **Four bands, not a score.** Readiness is reported as Foundation, Developing,
  Competitive or Evidence-Backed. A percentage or 0–100 readiness figure would
  imply precision the intake cannot support, so the product does not show one.
- **Free and local-first.** EmploStart is permanently free, needs no account, and
  keeps the candidate record on the person's own device. AI runs only when the
  user turns it on for a request, and the prompts disclose that in plain language.
