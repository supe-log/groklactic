# Groklactic: Team 4 Demo Plan

**Event:** Galatiq x SpaceXSI Grok Bot Hackathon, Austin. **Judging 8:30 PM CT, Mon Oct 19 2026, ~5 min per team** (top 5 present, awards 9:45).
**Code freeze 8:00 PM CT. Full rehearsal 8:00–8:25 PM CT.**
**Owner:** Groklactic Demo Coach. **This file holds the official 60-second pitch.** plan.md defers to it.
**Last updated:** 6:27 PM CT (plan.md reconciled). Re-check every `[TODO: confirm]` before 7:45 PM CT.

> **One line:** Groklactic turns a 5-minute business intake into a working, founder-approved Grok Bot team in one click. Our first customer is a small independent insurance agency.

---

## 0. Ground truth (what exists vs. what's being built)

| Thing | Status | Source |
|---|---|---|
| eye-of-grok repo | **Exists.** github.com/supe-log/eye-of-grok. `main` was last merged 2026-09-19 at 10:48 PM CT (PR #5). Next.js 16 org-map visualizer | GitHub |
| eye-of-grok org map (`/u/mine`, **Live / Edit / Mermaid** tabs, node click, status colors) | **Built** (from an earlier hackathon) | README / OVERVIEW / DEMO.md |
| Map ingest `POST /api/local/snapshot` (loopback only, no token). Map polls `GET /api/orgs/mine` every 2.5 s and redraws | **Built** | LOCAL.md |
| Reset map: `GET /api/orgs/mine?reset=1` | **Built** | README API table |
| Public deploy https://eye-of-grok.vercel.app | **Live** (HTTP 200 at 6:13 PM CT). Runs old `main`, so it does **not** have tonight's intake | curl |
| Tonight's local app on Logan's Mac: **http://localhost:3010** | Running (team kickoff). Repo docs still say :3002. **Use :3010** | Kickoff |
| Intake page, plan endpoint, feedback endpoint | **Being built now** (Claude Code). Claude Code is building exactly `GET /api/plan?business_id=pecan-street-insurance-group` and `POST`/`GET /api/feedback` on :3010 (per `config/eye-of-grok.config.json`); intake page path `[TODO: confirm with Claude Code]` | Kickoff |
| groklactic repo github.com/supe-log/groklactic | **Exists, empty** as of 6:13 PM CT | GitHub API |
| Template install link `grokbot://app/v1/bot-template?id=<share id>` | Link format confirmed. **Share id = `[TODO: Logan exports the Setup Chief of Staff template from Grok Bot by 6:50 PM CT (GM, moved up); first full dry run at 7:00 PM CT]`** | Kickoff |
| Repo: https://github.com/supe-log/groklactic (confirmed by Logan) | Confirmed | Logan |
| `/workspace/groklactic/insurance-team.json` (6 bots, 14 skills, 9 paused routines) + `setup-chief-of-staff/template.md` | **Done**, validator passes (`.venv/bin/python tools/validate.py`). Chief of Staff will put them on a `bot-team` branch of the groklactic repo; keep `.venv/` and `runtime/` out | Kickoff |
| Roster (final names): Agency Chief of Staff, Intake & Inbox, Renewals & Follow-ups, COI Desk, Quote Prep (draft-only), Compliance & Ops (runs the weekly retro). The Setup Chief of Staff is the installer template that builds them | **Confirmed** by the Setup Architect, 6:17 PM CT | Setup Architect |
| COI Desk holds its reply as a draft for founder approval | **Confirmed** by the Setup Architect | Steering |
| Retro skill turns thumbs feedback into a proposed fix | **Confirmed** by the Setup Architect | Steering |
| Setup skill fetches the plan from `http://localhost:3010` (configurable) and **falls back to local `insurance-team.json`** if the app is unreachable | **Confirmed** by the Setup Architect | Steering |
| Payments in test mode (Track 3) | **Not seen anywhere.** `[TODO: confirm]` whether it's built; if not, cut it from the talk track | — |
| plan.md (GM) | **Read at 6:25 PM CT.** It matches here on: freeze 8:00, rehearsal 8:00–8:25, submit 8:25–8:30, teammate files due 7:15, roles (Logan drives / Isaac narrates / Jeff fallback). It names demo.md as the source of truth for the click path and pitch. **Conflicts are listed in §5** | plan.md |
| eye-of-grok branch `docs/quickstart-harness` (commit `8e9af8a`, 6:11 PM CT) | Docs only, not merged. Tonight's intake/plan/feedback code is **uncommitted on Logan's Mac** | plan.md §1 |
| `/workspace/groklactic/` subfolders `bots/ config/ intake/ plan/ runtime/ setup-chief-of-staff/skills/getting-started/ tools/` | Scaffolding is there, but empty at 6:25 PM CT | ls |

**Rules for the demo:** no real outbound messages (every customer reply stays a draft), no secrets on screen (`.env*`, `~/.grokbot`, tokens), payments in test mode only, and no client PII. All demo data below is fictional and uses `example.com`.

---

## Demo roles

| Person | Role | Job during the 5 minutes |
|---|---|---|
| **Logan May** (captain) | **Driver** | His Mac, his Grok Bot login, localhost:3010. Makes every click below and talks only when Isaac hands off. Answers technical Q&A. |
| **Isaac Jaramillo** | **Narrator** | Gives the 60-second pitch, then the talk track for each beat (the "Talk track" column), then non-technical Q&A. |
| **Jeff Pape** | **Fallback operator + timekeeper** | Second laptop open to `/workspace/groklactic/fallback/` copies (a slideshow in shot order). Holds up fingers at 1:00, 2:00, and 2:45. Calls "switch" if a beat stalls more than 10 s. |

Roles match plan.md. Swap rule: if Isaac stumbles on the pitch in rehearsal #1, Logan narrates as well as drives, and Isaac takes timekeeping so Jeff can stay on fallback only.

**Prior-work line (say it once, in Q&A or at Close):** "The org-map visualizer is eye-of-grok from our Sep 19 hackathon. Tonight we built the intake → plan → one-click install → approval → retro loop and the insurance vertical."

---

## Demo inputs (type or paste these exactly)

### Sample business (fictional)
- **Name:** Pecan Street Insurance Group
- **Type:** Independent P&C insurance agency, Austin TX
- **Founder:** Dana Reyes (owner-agent). Email shown on screen: `dana@pecanstreet-ins.example.com`

### Intake answers
| Field `[TODO: confirm field labels on intake page]` | Answer |
|---|---|
| Industry | Independent insurance agency (commercial + personal lines) |
| Team size | 3 (owner-agent, 1 CSR, 1 part-time producer) |
| Tools | Gmail, Google Calendar, Google Drive, agency management system (AMS), carrier portals |
| Top pain points | 1) Certificate-of-insurance requests interrupt the day (≈15/week). 2) Renewals slip; no follow-up cadence. 3) Quote intake is messy and incomplete. 4) The inbox is a mess. |
| Rules / approvals | Nothing goes to a client without my approval. No coverage advice from bots. No client PII stored in templates. Payments in test mode only. |
| Goal | Get 10 hours a week back without hiring |

### Customer COI email (paste into the COI Desk or the demo inbox)
```
From: Marcus Lee <ops@lonestar-builders.example.com>
To: dana@pecanstreet-ins.example.com
Subject: COI needed - Riverside Medical Office project

Hi Dana,

We're starting work at the Riverside Medical Office build next Monday and the GC
needs a certificate of insurance before we can get on site.

Certificate holder:
  Austin Ridge General Contractors, LLC
  1200 Barton Springs Rd, Austin, TX 78704

They need General Liability and Auto, and want Austin Ridge GC listed as
additional insured. Can you send it by Thursday?

Thanks,
Marcus Lee
Lone Star Builders
```
**What a good answer looks like:** the COI Desk pulls the holder details, flags "additional insured needs endorsement check," drafts a reply plus a COI request summary for the CSR/AMS, and **holds it for Dana's approval** without sending. No coverage advice.

### Feedback (for the thumbs beat)
Thumbs **down** on the COI draft with the comment: `Always confirm the additional-insured endorsement is on the policy before promising a COI date.`

---

## 1. Live click path (≤3:00)

Before you start: localhost:3010 intake is open in tab 1, `/u/mine` map (already reset) in tab 2, and the Grok Bot app is open in a second window. See the pre-flight checklist.

| Time | Beat | Exact click / action (Logan, driver) | On screen | Talk track (Isaac, narrator) |
|---|---|---|---|---|
| 0:00–0:15 | Hook | Nothing. Tab 1 is showing. | Groklactic intake page | "Every small business wants an AI team. Nobody has time to design one. Groklactic does it in one form and one click." |
| 0:15–0:45 | **(a) Intake** | Tab 1 `http://localhost:3010/[TODO: confirm intake path]`. Fill in the fields from *Intake answers* (pre-filled except Pain points and Rules, which you type live). Click **[TODO: confirm submit button label]**. | Intake form, then the generated plan | "This is a three-person insurance agency in Austin. Their pain is COI requests, renewals, and quotes. Their rule: nothing goes to a client without the founder." |
| 0:45–1:05 | **(b) Proposed team on the map** | Switch to tab 2 `http://localhost:3010/u/mine` (or the post-submit redirect `[TODO: confirm]`). Click the **COI** node. | Org map: Dana (human), then Chief of Staff, then 5 specialists. The node panel shows the description and approval rule. | "Groklactic proposes the team: a Chief of Staff plus five specialists. Each one has its own job, skills, paused routines, and the approval rules Dana set." |
| 1:05–1:35 | **(c) One-click install** | Click **Install in Grok Bot** `[TODO: confirm button]`, which opens `grokbot://app/v1/bot-template?id=[TODO: share id]`. In Grok Bot, approve the install. Open the new Setup Chief of Staff and send `Build my team` (trigger confirmed by the Setup Architect; every routine starts paused). | The Grok Bot app shows the Setup CoS. It fetches the plan from localhost:3010 and creates the bots. The map redraws within 2.5 s if the CoS POSTs to `/api/local/snapshot`. | "One click installs a Chief of Staff that has never seen our product. It reads the plan JSON and builds the team itself. That's Track 2: a bot doing the job from the description alone." |
| 1:35–2:15 | **(d) COI answered, held for approval** | Open the **Certificates of Insurance** bot. Paste the *Customer COI email*. Send. | The bot extracts the holder and coverages, flags the additional-insured check, and shows a **draft reply marked "Awaiting founder approval"**. Nothing is sent. | "A real customer email. The COI Desk does the work: holder, coverages, endorsement flag. Then it stops. Dana approves. A one-person company with a team that can't go rogue. That's Track 3." |
| 2:15–2:30 | **(e) Feedback thumbs** | Click 👎 on the draft `[TODO: confirm thumbs location: eye-of-grok feedback UI or in-chat]`; `examples/seed-feedback.jsonl` already holds 3 COI thumbs-downs, 2 about missing turnaround time. Type the comment: `Tell the client when the signed certificate will arrive.` (matches the seeded feedback). Submit, which hits the feedback endpoint (skill expects `POST /api/feedback`; not on eye-of-grok main yet, so `[TODO: confirm with Claude Code]`). | Thumbs registered and the comment saved | "Dana gives feedback the way she would to a new hire. One thumb and one sentence." |
| 2:30–2:55 | **(f) Retro proposes an improvement** | Open the **Compliance & Ops** bot and send `Run the retro now` (confirmed: runs the retro skill right away, proposes one fix to a specific bot, and holds it for Dana's approval). | The retro reads the feedback and proposes a fix to **COI Desk**: "Always state the expected turnaround time for the signed certificate." (driven by the seeded feedback; untested live, so **rehearse it**) Shown as a **proposal for approval**, not applied. | "Every week the Compliance & Ops retro turns feedback into a proposed fix, and Dana approves it. The team gets better without her managing it." |
| 2:55–3:00 | Close | Switch back to the map tab. | Full team map | "Intake to a working, supervised AI team in three minutes. That's Groklactic." |

**Hard cut points:** if the clock shows 2:00 and you're not at beat (d), skip (e) and go to the (f) screenshot. If it shows 2:45, go straight to Close.

---

## 2. Rubric map

| Beat | Works (30) | Real work (25) | Grok Bot use (20) | Clarity (15) | Uniqueness (10) | Say to the judges |
|---|---|---|---|---|---|---|
| (a) Intake | ● live form plus plan endpoint | ● real agency pains (COI, renewals) | — | ●● one screen, plain words | ● vertical-first | "A real business, real pains, 5 minutes." |
| (b) Map | ●● live redraw, 2.5 s poll | ● roster maps to the actual workflow | ● Chief of Staff pattern, group-chat cap respected | ●● you can *see* the company | ●● nobody else visualizes the team before install | "You see the team before you trust it." |
| (c) Install | ●●● the riskiest beat; show it really happens | ● | ●●● bot template, skills, routines (paused), local fetch with JSON fallback | ● | ●● one-click company | **Track 2:** "A bot that never saw Groklactic reads plan JSON and builds the team." |
| (d) COI draft | ●●● end-to-end on a real email | ●●● a task agencies do ~15×/week | ●● memory + skills + approval gate | ●● | ● | **Track 3:** "One-person company: customer, bot roster, founder approval rules. Payments in test mode `[TODO: confirm]`." |
| (e) Thumbs | ● endpoint persists | ● | ● | ● | ● | "Feedback is one tap." |
| (f) Retro | ●● | ●● | ●●● routines + memory, self-improvement loop | ● | ●●● a self-improving team with a human gate | "The team improves weekly. The founder only approves." |

**Emphasis:**
- **Works (30):** say "this is live" at (c) and (d), then let the screen prove it. Don't apologize for stubs; skip them.
- **Real work (25):** use the numbers: ~15 COIs a week, the 10-hours-a-week goal, draft-only replies.
- **Grok Bot use (20):** name the features out loud: *bot templates, skills, routines, memory, local computer access, Chief of Staff.*
- **Clarity (15):** one business, one email, one thumbs, one fix. No jargon.
- **Uniqueness (10):** "intake → map → install → self-improving retro" is the loop nobody else shows.

---

## 3. Official 60-second pitch (~150 words, to be spoken)

> Every small business owner has heard "just use AI agents." Then they open a blank chat and give up.
>
> Take Dana. She runs a three-person insurance agency in Austin. Fifteen times a week, a contractor emails asking for a certificate of insurance, and her whole afternoon goes with it.
>
> Groklactic fixes that. Dana fills out one intake. We design her Grok Bot team: a Chief of Staff and five specialists for COIs, renewals, quotes, inbox, and compliance, each with skills, routines, and her approval rules built in. One click installs it.
>
> You'll watch a bot that has never seen our product read the plan and build the team. Then you'll see a real COI request answered and held for Dana's approval, and a Compliance & Ops retro turn her feedback into a fix.
>
> Grok Bot already gives us templates, memory, routines, and a computer. We turn that into a company.
>
> One form. One click. One founder in control. That's Groklactic.

(≈150 words, about 55–60 s at a calm pace. Isaac delivers it before beat (a). If the judge is strict about 5 minutes total, this pitch plus the 3:00 click path leaves about 1:00 for Q&A. If time is tight, use the hook line only.)

**Persona note:** this pitch uses **Dana / Austin**. plan.md §5 draft uses "Maria / Round Rock". This file is official; GM, please update plan.md to Dana.

---

## 4. Fallback plan

### Per-beat failure → detect → switch

| Beat | What can fail | Spot it fast | Switch (Jeff) |
|---|---|---|---|
| (a) Intake | localhost:3010 down, form errors, plan endpoint 500 | Blank page or spinner for more than 5 s | Show `01-intake-filled.png`, then `02-plan-generated.png`. Narrator: "Here's the plan it generated at rehearsal." |
| (b) Map | Map doesn't redraw, shows the old fixture, or nodes overlap | Old sample names visible / no COI node after 5 s | Show `03-map-team.png` and `04-map-coi-node.png`. Driver runs `GET /api/orgs/mine?reset=1` only during pre-flight, never live |
| (c) Install | `grokbot://` link doesn't open, template id wrong, install approval hangs, Setup CoS can't reach :3010 | Nothing happens 5 s after the click, or an error card appears | **Built-in fallback beat:** the setup skill falls back to local `insurance-team.json`. Narrator: "Even offline, it builds from the JSON. Same plan, no app needed." If install itself fails, show `05-template-install.png`, then `06-setup-cos-building.png`, then `07-roster-created.png` |
| (d) COI | Slow model response (>20 s), bot sends instead of drafting (must never happen), wrong bot | Typing indicator past 15 s | Narrator fills with talk track to 20 s, then shows `08-coi-email.png` and `09-coi-draft-held.png`. If a bot ever tries to send: stop, it's a demo-breaker. Show the screenshot |
| (e) Thumbs | Feedback endpoint 500, button missing | No confirmation | `10-thumbs-feedback.png` |
| (f) Retro | Retro slow or generic, routine paused and won't trigger | No proposal after 20 s | `11-retro-proposal.png`. Narrator reads the proposed fix aloud |
| Any | Wifi dies | Page loads hang | Turn on the phone hotspot (pre-paired). The local app on :3010 keeps working offline; only Grok Bot model calls need the network |
| Any | Logan's Mac freezes | — | Jeff plays `clip-full-run.mov` on his laptop while Isaac narrates |

### Shot list: capture by **7:55 PM CT** (before the freeze), on Logan's Mac, full-window, no secrets in frame
Save to `/workspace/groklactic/fallback/` (copy from the Mac with CopyToBox or AirDrop to Jeff's laptop):

1. `01-intake-filled.png`: intake form with every demo answer filled in
2. `02-plan-generated.png`: plan result after submit
3. `03-map-team.png`: `/u/mine` with Dana, the CoS, and 5 specialists
4. `04-map-coi-node.png`: COI node panel open (description + approval rule)
5. `05-template-install.png`: the Grok Bot template install card from `grokbot://app/v1/bot-template?id=…`
6. `06-setup-cos-building.png`: Setup CoS mid-run (fetching the plan / creating bots)
7. `06b-setup-cos-json-fallback.png`: Setup CoS using the local `insurance-team.json` fallback (app stopped)
8. `07-roster-created.png`: Grok Bot sidebar showing the 6 new bots
9. `08-coi-email.png`: the COI email pasted into the COI Desk
10. `09-coi-draft-held.png`: draft reply showing "awaiting founder approval"
11. `10-thumbs-feedback.png`: thumbs-down plus comment saved
12. `11-retro-proposal.png`: Compliance & Ops retro's proposed fix
13. `clip-full-run.mov`: a 3-minute screen recording of one clean rehearsal run (QuickTime, ⌘⇧5)

### Pre-flight checklist and rehearsal (all CT)

**7:15–7:40: first full end-to-end run on the Mac** (plan.md). Capture screenshots 01–12 opportunistically while it runs.
**7:40–7:55: record `clip-full-run.mov`** and fill any missing screenshots (Jeff, per plan.md). Logan checks that every `[TODO: confirm]` is filled.

**8:00: CODE FREEZE.** No commits, no `npm install`, no restarts unless something is broken.

**8:00–8:10: rehearsal run #1** (full 3:00, timed by Jeff). Note every stall.
**8:10–8:15: fix the run order only** (talk track, tab order, pre-fills). No code.
**8:15–8:22: rehearsal run #2.** Must finish under 3:00.
**8:22–8:25: reset state and lock** (below).

Reset and lock checklist (8:22–8:25):
- [ ] Logan's Mac on power, Do Not Disturb ON, notifications off, Slack/Messages quit
- [ ] Display mirroring / projector tested; browser zoom 125%; dark/light theme chosen
- [ ] `npm run dev` running on **:3010** (terminal minimized, not on screen)
- [ ] Map reset: open `http://localhost:3010/api/orgs/mine?reset=1` once, then reload `/u/mine` `[TODO: confirm reset still applies to the new intake/plan store]`
- [ ] Bots installed during rehearsal: decide **delete-and-reinstall live** vs. **pre-installed, show install on a second account** `[TODO: confirm with Setup Architect]`. Don't delete anything without Logan
- [ ] Tab 1: intake at localhost:3010 (pre-filled except pain points/rules). Tab 2: `/u/mine`. Tab 3: blank (spare)
- [ ] Grok Bot app open, logged in as Logan, Setup CoS template link ready in a text snippet
- [ ] COI email and feedback comment ready in a clipboard manager / Notes, in order
- [ ] No `.env.local`, `~/.grokbot`, token, or terminal visible on screen
- [ ] Payments: test mode only, if shown at all `[TODO: confirm]`
- [ ] Wifi on venue network; **phone hotspot paired and tested** as backup
- [ ] Jeff's laptop: fallback folder open in Preview slideshow, `clip-full-run.mov` queued
- [ ] Timer ready (Jeff's phone)

### 30-second ultra-short version (if time is cut)
1. (0–10 s) Isaac: "Groklactic: one intake, one click, a Grok Bot team for a small business." Show `03-map-team.png` or the live map.
2. (10–22 s) Logan pastes the COI email into the COI Desk, live or `09-coi-draft-held.png`. Isaac: "A real COI request, done and held for the founder's approval."
3. (22–30 s) Show `11-retro-proposal.png`. Isaac: "And every week the Compliance & Ops retro turns her feedback into a fix. One founder, a whole team, always in control."

---

## 5. Open risks and TODOs

**Risks**
1. **Install beat (c) is the riskiest.** The template share id isn't confirmed, and a live install takes real time. Mitigation: JSON fallback beat plus screenshots 05–07.
2. **Port drift:** repo docs say :3002 and tonight's app is :3010. The setup skill must point at :3010. Check this in rehearsal.
3. **Re-install collisions:** bots from rehearsal may already exist, so a live install could duplicate them (duplicates copy the profile, not memory). Decide the reset approach by 8:15.
4. **Model latency** at (d) and (f) on venue wifi. Mitigation: talk-track filler, then screenshots after 20 s.
5. **Payments test mode (Track 3)** isn't confirmed built. Isaac says "payments run in test mode" only if it is built and shown. Otherwise drop the line.
6. The public Vercel site runs the old `main` without the intake. Don't use it for the demo.
7. The groklactic repo is empty. If a judge asks for the code, point to eye-of-grok. Never push `grok-bot-app/`, `.env.local`, `.vercel`, or `~/.grokbot`.

**`[TODO: confirm]` list (Logan/team to fill before 7:45 PM CT)**
- [ ] Intake page path on localhost:3010 and field labels
- [ ] Intake submit button label and post-submit redirect (plan view vs. map)
- [ ] Plan endpoint path (e.g. `/api/plan…`) used by the setup skill
- [ ] Feedback endpoint path and where the thumbs UI lives (eye-of-grok page or in-chat)
- [ ] Grok Bot template **share id** for `grokbot://app/v1/bot-template?id=…`
- [ ] "Install in Grok Bot" button exists on the plan/map page, or the driver pastes the link
- [ ] Exact bot display names from `insurance-team.json`
- [ ] Setup CoS trigger phrase (from `setup-chief-of-staff/template.md`)
- [x] Retro trigger: `Run the retro now` in Compliance & Ops chat (confirmed 6:17 PM CT)
- [ ] Whether the Setup CoS POSTs the roster to `/api/local/snapshot` (map redraw) or the map comes from the plan endpoint
- [ ] Whether `?reset=1` resets tonight's new data
- [ ] Payments test mode: built or cut
- [ ] Roster conflict: plan.md §3/§5 says **Sales / Support / Ops + CoS**. Kickoff and the Setup Architect say **CoS + Intake & Inbox, Renewals, COI, Quote Prep, Compliance & Ops**. demo.md uses the latter. Resolved: final names confirmed by the Setup Architect at 6:17 PM CT
- [ ] Unseen-bot (Track 2) beat: plan.md has Jeff run it on a separate fresh bot (a 3:00–3:45 slot in its 5-min path). demo.md folds it into beat (c), where the Setup CoS builds from plan JSON. If Jeff's recording is better, swap it in at (c) as a 10 s clip
- [ ] Stripe test-mode approval card (plan.md: NICE, only if green by 7:30). If shipped, add 10 s to beat (d) and take it from (e)
- [ ] Optional ngrok/Vercel public URL (plan.md NICE). Not needed for this click path
- [ ] plan.md timeline matches this file (freeze 8:00, rehearsal 8:00–8:25, judging 8:30)


> **Timeline update, 6:20 PM CT (GM):** share link by 6:50, first full dry run at 7:00 with `Run the retro now` rehearsed (the only beat not yet tested live), code freeze stays at 8:00. Publishable files are going to the `bot-team` branch of supe-log/groklactic under `bot-team/`.
