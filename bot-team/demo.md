# Groklactic: Team 4 Demo Plan (No Thought clothing-brand pack)

**Event:** Galatiq x SpaceXSI Grok Bot Hackathon, Austin. **Judging 8:30 PM CT, Mon Oct 19 2026, ~5 min per team.**
**Timeline:** clothing-team.json due **7:05** · **dry run 7:10** · push to GitHub by **7:45** · **code freeze 8:00** · rehearsals **8:00–8:25** · judging **8:30** (all CT).
**This file holds the official 60-second pitch and click path.** plan.md defers to it. The insurance version is archived in `demo-insurance.md`.
**Last updated:** 6:45 PM CT (pivot to No Thought). Re-check every `[TODO: confirm]` at the 7:10 dry run.

> **One line:** Groklactic turns a 2-minute intake into a founder-approved Grok Bot team in one click. Tonight's customer is real: **No Thought**, Logan's natural-fabric athleisure brand in Austin.

---

## 0. Ground truth

| Thing | Status | Source |
|---|---|---|
| **No Thought** (real brand, founder Logan May, Austin) | Premium DTC athleisure in natural-forward fabrics (merino, TENCEL lyocell, performance linen blends, organic cotton; elastane only where needed; "never greenwash"). Run, tennis and gym. Bandit-level fashion taste, quiet logos, "tempo → coffee" wearability | `/workspace/no-thought/business-brief.md`, No Thought GM profile |
| Target customer | Austin runners, tennis players and gym-goers who are natural-fiber curious, have quiet style and are "coffee-after people". Community-first: waitlist, then hyperlocal run clubs and pop-ups, then limited drops | `no-thought-growth/austin-community-plan.md`, business brief |
| Palette | Limestone `#E8E2D6`, Clay, Bark, Soft Black (hero), accents ≤10% | `no-thought/brand-week1-draft.md` |
| Existing No Thought bot team (pitch proof) | **No Thought GM, Brand, Product, Growth** bots run on Logan's account. The clothing pack is distilled from their work | agent profiles 0f26bc1a / 3b3f7a40 / 78942183 / 2b986e12 |
| Hero product: **natural-fabric hoodie, oatmeal, small "No Thought" chest wordmark** | Not in the v0 SKU table (closest is the W1 warm-up layer). Fabric candidates come from Product's research, e.g. **Pontetorto Tecnowool merino-back fleece** or organic-cotton fleece. GSM and blend are ASSUMPTION | `fabric-shortlist-v0.md` §6, `fabric-research-v0.md` |
| Higgsfield test (Chief of Staff, 6:28 PM CT) | **<30 s, 0.25 credits, model `gpt_image_2_5`, 1:1.** Mockup at `/workspace/groklactic/clothing/mockup-hoodie-01.png` (copied to `fallback/04-hoodie-mockup.png`). Skill flow: `balance` → `get_cost` (held if over cap) → `generate_image` → `jobs_wait` | CoS steering |
| eye-of-grok app on Logan's Mac: **http://localhost:3010** | Intake (with industry picker), plan endpoint and feedback endpoint are being built by Claude Code, uncommitted. The Setup Architect assumes **On main (checked on GitHub 6:31 PM CT):** intake at `/start`, team at `/u/[orgId]/team`, `GET /api/orgs/[id]/plan` (`?format=recipes` or `?format=prompt`, 404 `plan_not_found` until intake is submitted), `/api/orgs/[id]/feedback`, `/api/orgs/[id]/retro`. Setup skill still assumes `/api/plan?business_id=`, so it must be updated or it falls back to local JSON | kickoff, `groklactic/README.md` |
| Map ingest `POST /api/local/snapshot` (loopback), 2.5 s redraw, reset `GET /api/orgs/mine?reset=1` | **Built** on eye-of-grok `main` | eye-of-grok README / LOCAL.md |
| Install link `grokbot://app/v1/bot-template?id=<share id>` | Format confirmed. **Share id `[TODO: confirm]`** | kickoff |
| Setup CoS trigger **"Build my team"**; retro trigger **"Run the retro now"** | Confirmed in `setup-chief-of-staff/template.md` / `README.md` (insurance package). The setup skill fetches from :3010 and **falls back to local JSON** | Setup Architect files |
| Insurance package (proof the generator works for any business) | **Built:** `insurance-team.json`. Roster: Agency Chief of Staff, Intake & Inbox, Renewals & Follow-ups, COI Desk, Quote Prep, Compliance & Ops | `/workspace/groklactic/` |
| `clothing-team.json` | **Not on disk at 6:45 PM CT** (due 7:05). Names below follow the GM's final list | GM override |
| Repos | github.com/supe-log/eye-of-grok (Sep 19 hackathon code + a docs branch today); github.com/supe-log/groklactic (**empty**) | GitHub |

### Clothing roster (GM final; must match clothing-team.json exactly)
| Bot | Job | Approval gate |
|---|---|---|
| **Brand Chief of Staff** | Routes work, keeps the approval queue, collects 👍/👎 | Everything external comes back to Logan |
| **Design Studio** | Higgsfield concepts, colorways, lookbook | Every Higgsfield credit spend shows a `get_cost` check, and anything over the cap waits for approval |
| **Vendor Scout** | Mills plus cut-and-sew factories via browser search; compares MOQ / price / lead time; shortlist | Research only |
| **Outreach & Negotiation** | Drafts RFQs and counteroffers | **Every send held for approval.** Nothing over $500 is agreed without Logan |
| **Launch & Growth** | Higgsfield ad creative, social calendar | Nothing publishes without OK |
| **Ops & Retro** | Samples, POs, payments (**Stripe test mode**), weekly retro (routine **paused**) | POs and deposits are draft-only. No real money moves |

**Founder rules (say them out loud):** nothing sends, publishes, orders or pays without Logan. Nothing over **$500** is agreed without him. Every email, PO, deposit and Higgsfield credit spend is draft-only or approval-gated. Payments stay in test mode.

---

## Demo roles

| Person | Role | Job |
|---|---|---|
| **Logan May** | **Driver** (and the real founder on screen) | His Mac, Grok Bot login and localhost:3010. Makes every click. Approves and thumbs as the founder. Answers technical Q&A |
| **Isaac Jaramillo** | **Narrator** | Gives the pitch and the talk track below, plus non-technical Q&A |
| **Jeff Pape** | **Fallback operator + timekeeper** | Second laptop with `fallback/` open in order. Signals 1:00 / 2:00 / 2:40. Calls "switch" after a 10 s stall |

**Prior-work line (Q&A):** "The map is eye-of-grok from our Sep 19 hackathon. Tonight we built the intake → plan → one-click install → approval → retro loop and the clothing and insurance packs."

---

## Demo inputs

### Intake (industry picker = Clothing / apparel brand) `[TODO: confirm field labels]`
| Field | Answer |
|---|---|
| Industry | Clothing / apparel brand (DTC) |
| Business | No Thought, Austin TX |
| Founder | Logan May (solo founder) |
| What you sell | Natural-fabric athleisure for run, tennis and gym: merino, TENCEL lyocell, linen blends, organic cotton |
| Stage | Pre-launch. Waitlist first, first drop in sampling |
| Tools | Gmail, Google Drive, Notion, Higgsfield, Shopify + Stripe (planned) |
| Top pain points | 1) Finding mills and factories and comparing MOQ / price / lead time. 2) Writing RFQs and chasing vendors. 3) Concept and ad creative. 4) Launch calendar |
| Rules | Nothing sends, publishes, orders or pays without me. Nothing over $500 agreed without me. Credit spend needs approval. Payments test mode only |
| Hero product | Natural-fabric hoodie, oatmeal, small "No Thought" chest wordmark |

### Design Studio prompt (beat 4)
```
Make a product concept for our hero piece: a natural-fabric hoodie in oatmeal,
relaxed fit, brushed fleece, small tonal "No Thought" wordmark on the left chest.
Quiet, premium, flat-lay on white. 1:1. Show me the cost before you generate.
```

### Vendor shortlist (beat 5): what a good result looks like
The **mill** rows are real public data from No Thought Product's research (`fabric-research-v0.md`, re-verify before outreach). The **factory** rows are **EXAMPLE DATA**, not real vendors.

| # | Vendor | Type | MOQ | Price | Lead time | Note |
|---|---|---|---|---|---|---|
| 1 | Pontetorto (Italy) | Mill: Tecnowool merino-back stretch fleece | Not public (ASSUMPTION: hundreds of kg/color) | Quote | Quote (EU lead times) | OEKO-TEX on site, re-verify |
| 2 | Ecological Textiles | Mill: GOTS organic cotton jersey/rib | From 1 m (sampling) | Quote | Quote | Good for samples |
| 3 | Ohyeah Textile | Mill: GOTS organic cotton/EL 200 gsm | 500 kg/color (stated) | Quote | Quote | MOQ too high for v0 |
| 4 | **[EXAMPLE] Eastside Cut & Sew, Austin TX** | Cut-and-sew | [EXAMPLE] 100 pcs | [EXAMPLE] $28–34/unit CMT | [EXAMPLE] 4–5 wks | Local, sample-friendly |
| 5 | **[EXAMPLE] Gulf Coast Knit Works, LA CA** | Cut-and-sew, fleece specialist | [EXAMPLE] 300 pcs | [EXAMPLE] $22–26/unit | [EXAMPLE] 6–8 wks | Better price, higher MOQ |

### RFQ draft (beat 6): Outreach & Negotiation output, **held for approval**
```
To: [EXAMPLE] production@eastside-cutsew.example.com
From: Logan May, No Thought
Subject: RFQ: natural-fabric hoodie sample + first run (No Thought, Austin)

Hi team,
I'm Logan, founder of No Thought, a natural-fabric athleisure brand here in Austin.
We're quoting our first hoodie: relaxed fit, merino-back or organic-cotton fleece
(we supply or nominate fabric), oatmeal, small tonal chest wordmark (embroidery).
Could you share unit price at 100 / 300 pcs, sample cost and timing, and
production lead time? Tech pack and reference image attached.
Thanks, Logan
```
*(The draft deliberately leaves out MOQ. That's what Logan's thumbs-down catches.)*
**On screen:** "Held for founder approval. Not sent." If a counteroffer goes above $500 total, the bot says "Over $500, needs Logan."

### Feedback (beat 7)
👎 on the RFQ draft, comment: **`Ask for the minimum order quantity up front.`**

### Retro (beat 8)
In **Ops & Retro**: `Run the retro now` (calls `POST /api/orgs/no-thought/retro`). Backup: click **Run retro (1 new feedback)** on the team page. Expected: it reads the 👎, proposes a diff to **Outreach & Negotiation's RFQ skill** (adds "Always ask for MOQ in the first message"), and **holds the change for Logan's approval**.

---

## 1. Live click path (3:00)

Pre-opened: tab 1 is `localhost:3010/start`, tab 2 is `/u/demo-insurance-agency/team` (for the swap), and the Grok Bot app sits in a second window. The Vendor Scout shortlist thread was **pre-run at 8:15** (browser search is slow).

| Time | Beat | Exact click / action (Logan) | On screen | Talk track (Isaac) |
|---|---|---|---|---|
| 0:00–0:10 | Hook | Tab 1 showing | Groklactic intake | "Logan, our captain, runs a real clothing brand, No Thought. Tonight his whole bot team gets built in one click." |
| 0:10–0:30 | **1. Intake + industry picker** | `http://localhost:3010/start`. Pick **Clothing brand** (needs Claude Code to add it to `INDUSTRY_OPTIONS`; else "Other small business"). Slug `no-thought`. Fields pre-filled; type only the Rules line live. Click **Design my Bot team** (shows "Designing…") | Form, then the generated plan | "Pick an industry, answer a few questions. The rule Logan sets: nothing sends, orders or pays without him, and nothing over $500." |
| 0:30–0:45 | **2. Team on the map** | Auto-redirects to `/u/no-thought/team`. Click the **Outreach & Negotiation** node | Logan (human), then Brand Chief of Staff, then 5 specialists. The node shows the approval rule | "Six bots: design, vendor scouting, outreach, launch, ops. Each has its own job, skills and paused routines." |
| 0:45–1:10 | **3. One-click install (Track 2)** | Click **Install** `[TODO: button]`, which opens `grokbot://app/v1/bot-template?id=[TODO: share id]`. Approve. In the Setup Chief of Staff, type **`Build my team`** | Setup CoS fetches the plan from :3010 (local JSON if unreachable) and creates the bots. Map redraws | "That Chief of Staff has never seen Groklactic. It reads the plan JSON and builds the team itself. That's Track 2." |
| 1:10–1:20 | **4a. Design Studio starts the hoodie** | Open **Design Studio**, paste the *Design Studio prompt* | `balance` → `get_cost`: **0.25 credits**, under cap, then `generate_image` starts (~30 s) | "Before it spends a single credit, it checks the cost against Logan's cap. Over the cap, it waits for him. This one's a quarter credit, so it goes." |
| 1:20–1:40 | **5. Vendor Scout shortlist** (during the render) | Switch to **Vendor Scout** (pre-run thread) | Shortlist table: MOQ / price / lead time | "Meanwhile Vendor Scout searched the web for mills and cut-and-sew shops and ranked them by minimum order, price and lead time. The mills are real, from Logan's product research." |
| 1:40–1:50 | **4b. Hoodie reveal** | Back to **Design Studio** (`jobs_wait` done) | Oatmeal hoodie, small "No Thought" wordmark | "And there's the concept piece. Natural fabric, quiet logo. Very No Thought. Next drop is the run short, and Design Studio does that one tomorrow." |
| 1:50–2:10 | **6. RFQ held for approval (Track 3)** | **Outreach & Negotiation**: `Draft an RFQ to #4 for the hoodie` | RFQ draft with **"Held for founder approval"** | "It writes the RFQ in Logan's voice and stops. A one-person company with a team that can't send, spend or sign without the founder. That's Track 3." |
| 2:10–2:20 | **7. Thumbs-down** | Back in tab 1 (`/u/no-thought/team`), **Step 2 · Rate the work**: 👎 on the **Outreach & Negotiation** card, comment `Ask for the minimum order quantity up front.` | Feedback saved (`POST /api/orgs/no-thought/feedback`, Bearer token) | "Logan coaches it like a new hire. One thumb, one sentence. Second time this week, so now it's a pattern." |
| 2:20–2:35 | **8. Retro** | **Ops & Retro**: `Run the retro now` (calls `POST /api/orgs/no-thought/retro`). Backup: click **Run retro (1 new feedback)** on the team page | Proposal: **add a rule** to Outreach & Negotiation ("ask for MOQ up front"), **awaiting founder approval** in `/api/orgs/no-thought/changes`; approve, then Chief of Staff marks it applied | "The retro turns feedback into a fix, and even the fix waits for Logan. The team gets better every week." |
| 2:35–2:55 | **Insurance swap** | Tab 2: `/u/pecan-street-insurance-group/team` if Claude Code serves `data-seed/pecan-street-insurance-group.plan.json` (our 6 bots); otherwise `/u/demo-insurance-agency/team` (the **See a demo agency** button, app-generated roster). Check which at 7:10. Don't re-submit live | Agency Chief of Staff, Intake & Inbox, Renewals & Follow-ups, COI Desk, Quote Prep, Compliance & Ops | "Same generator, any business. Here's an insurance agency: COI desk, renewals, quotes, all founder-approved." |
| 2:55–3:00 | Close | Map | — | "One intake. One click. One founder in control. That's Groklactic." |

**Cut rules:** if the render isn't done at 1:40, Jeff shows `04-hoodie-mockup.png` ("here's the one from rehearsal") and Logan reveals the live one later if it lands. At 2:20, skip straight to the retro. At 2:40, skip the insurance swap and say the line over the map.

---

## 2. Rubric map

| Beat | Works 30 | Real work 25 | Grok Bot use 20 | Clarity 15 | Uniqueness 10 | Emphasize |
|---|---|---|---|---|---|---|
| 1 Intake | ● live | ●● real brand, real founder | — | ●● | ● industry picker | "Real customer: Logan's brand." |
| 2 Map | ●● live redraw | ● | ● Chief of Staff pattern | ●● see the team | ●● | "See the team before you trust it." |
| 3 Install | ●●● | ● | ●●● **bot templates, skills, paused routines**, local fetch with JSON fallback | ● | ●● | **Track 2:** an unseen bot builds from the plan JSON |
| 4 Hoodie | ●● | ●● a real hero product | ●●● **Higgsfield plugin** with a cost check before spend | ●● visual wow | ●● | "Checks cost before it spends a credit." |
| 5 Shortlist | ● | ●●● actual sourcing work | ●● **browser search** | ● | ● | "Real mills, compared on MOQ, price and lead time." |
| 6 RFQ | ●●● | ●●● | ●● approval-gated drafts | ●● | ● | **Track 3:** one-person company, $500 cap, payments test mode |
| 7 Thumbs | ● | ● | ● memory | ● | ● | "One tap of feedback." |
| 8 Retro | ●● | ●● | ●●● **paused routine run on demand + memory** | ● | ●●● self-improving, human-gated | "Improves weekly. Logan only approves." |
| Insurance | ●● | ●● | ● | ●● | ●● | "Same generator, any business." |

Say the Grok Bot features out loud: **bot templates, skills, Higgsfield plugin, browser search, routines (paused), memory, Chief of Staff.**

---

## 3. Official 60-second pitch (~150 words, spoken by Isaac)

> Every founder has heard "just use AI agents." Then they stare at a blank chat.
>
> Logan, our captain, is building No Thought, a natural-fabric athleisure brand here in Austin. He's one person doing design, sourcing, vendor emails, and launch.
>
> Groklactic gives him a company. He answers one intake, and we design his Grok Bot team: a Chief of Staff, Design Studio, Vendor Scout, Outreach and Negotiation, Launch and Growth, and Ops and Retro. One click installs it.
>
> This pack came from Logan's real No Thought bot team, the GM, Brand, Product and Growth bots he already runs.
>
> You'll watch it design a hoodie in Higgsfield, shortlist real mills, and draft an RFQ that waits for Logan. Nothing sends, spends, or signs over five hundred dollars without him. Then his feedback becomes a fix.
>
> Same generator, any business.
>
> One intake. One click. One founder in control. That's Groklactic.

(~150 words, 55–60 s.)

---

## 4. Fallback plan

| Beat | What can fail | Spot it | Switch (Jeff) |
|---|---|---|---|
| 1 Intake | :3010 down, picker missing, plan endpoint errors | Spinner >5 s | `01-intake-clothing.png`, then `02-plan-clothing.png` |
| 2 Map | No redraw, old fixture | No Outreach node after 5 s | `03-map-clothing.png` |
| 3 Install | `grokbot://` doesn't open, wrong id, Setup CoS can't reach :3010 | Nothing after 5 s | **Built-in fallback:** the Setup CoS builds from local `clothing-team.json` ("even offline, same plan"). Else `05-install-card.png`, then `06-build-my-team.png`, then `07-roster-sidebar.png` |
| 4 Hoodie | Higgsfield slow (>40 s), credit or balance error, off-brand image | `jobs_wait` still running at 1:40 | `04-hoodie-mockup.png` (**exists now**, Higgsfield test: <30 s, 0.25 cr) |
| 5 Shortlist | Pre-run thread missing, browser search slow | — | `08-vendor-shortlist.png` |
| 6 RFQ | Slow response; bot tries to send (**must never happen**: stop) | Typing >15 s | `09-rfq-held.png` |
| 7 Thumbs | Endpoint 500 / no button | No confirmation | `10-thumbs-moq.png` |
| 8 Retro | Slow, generic, or can't find feedback | No diff after 20 s | `11-retro-diff.png` |
| Insurance | Picker or plan fails | — | `12-insurance-map.png` |
| Wifi | Hangs | — | Phone hotspot (pre-paired). :3010 is local |
| Mac dies | — | — | `clip-full-run.mov` on Jeff's laptop, Isaac narrates |

### Shot list: save to `/workspace/groklactic/fallback/`, capture during the **7:10 dry run** through 7:55
1. `01-intake-clothing.png`: picker on Clothing, fields filled
2. `02-plan-clothing.png`: generated plan
3. `03-map-clothing.png`: map with Logan, Brand Chief of Staff and 5 bots
4. `04-hoodie-mockup.png`: **done** (copy of `clothing/mockup-hoodie-01.png`)
5. `04b-cost-check.png`: Design Studio `get_cost` = 0.25 credits, under cap
6. `05-install-card.png`: template install card
7. `06-build-my-team.png`: Setup CoS mid-build (plus `06b-json-fallback.png` with :3010 stopped)
8. `07-roster-sidebar.png`: 6 bots in the Grok Bot sidebar
9. `08-vendor-shortlist.png`: Vendor Scout table
10. `09-rfq-held.png`: RFQ "held for founder approval"
11. `10-thumbs-moq.png`: 👎 + MOQ comment
12. `11-retro-diff.png`: retro diff to the RFQ skill, awaiting approval
13. `12-insurance-map.png`: insurance roster on the map
14. `clip-full-run.mov`: 3:00 recording of one clean run (Jeff, 7:40–7:55)

### Timeline and pre-flight (CT)
| Time | What |
|---|---|
| 7:05 | `clothing-team.json` lands. Demo Coach matches names and trigger phrases |
| **7:10** | **Dry run #1** on Logan's Mac. Capture shots 01–12 as it goes. Log stalls |
| 7:25–7:40 | Fix order and inputs; Claude Code fixes only blockers |
| by **7:45** | **Push** the safe files to supe-log/groklactic (per Setup Architect's list; no `.venv/`, `runtime/`, `.env*`, `~/.grokbot`, `grok-bot-app/`, tokens) |
| 7:40–7:55 | Jeff records `clip-full-run.mov` and fills missing shots |
| **8:00** | **CODE FREEZE** |
| 8:00–8:10 | Rehearsal #1 (timed 3:00 + pitch) |
| 8:10–8:15 | Fix talk track/tabs only. **Pre-run the Vendor Scout shortlist** so the thread is ready |
| 8:15–8:22 | Rehearsal #2. Must finish under 3:00 |
| 8:22–8:25 | Reset and lock (below) |
| 8:30 | Judging |

Reset and lock (8:22–8:25):
- [ ] Mac on power, Do Not Disturb, Slack/Messages quit, no `.env*` / terminal / tokens on screen
- [ ] `npm run dev` on **:3010**. Map reset `http://localhost:3010/api/orgs/mine?reset=1` `[TODO: confirm reset covers the new plan store]`
- [ ] Rehearsal bots: decide **reinstall live** (Setup CoS skips names that already exist) vs **show on a clean account** `[TODO: confirm]`. Delete nothing without Logan
- [ ] Tabs: intake (pre-filled, Clothing picked), `/u/mine`, spare. Grok Bot open: Setup CoS link, Design Studio, Vendor Scout (pre-run thread), Outreach & Negotiation, Ops & Retro
- [ ] Higgsfield balance checked (≥1 credit). Cap set. Stripe **test mode**
- [ ] Prompts in Notes in order: Design Studio prompt, RFQ ask, MOQ comment, "Run the retro now"
- [ ] Wifi + **phone hotspot tested**. Jeff's laptop: `fallback/` slideshow + clip queued. Timer ready

### 30-second version
1. (0–10 s) Isaac: "Groklactic builds a founder-approved Grok Bot team in one click. Here's Logan's real brand, No Thought." Show the map (or `03-map-clothing.png`).
2. (10–22 s) Show the hoodie (`04-hoodie-mockup.png`) and the RFQ held (`09-rfq-held.png`): "It designs, it sources, it drafts. Nothing sends or spends over $500 without Logan."
3. (22–30 s) Show `11-retro-diff.png`: "His feedback becomes a fix. Same generator, any business."

---

## 5. Open risks and TODOs

**Retro (GM final, 6:36 PM CT):** code stays at `RULE_AFTER_DOWNS = 2`. Right after `?reset=1`, Jeff posts the first 👎 from Logan's Mac with Setup Architect's command (no retro run):

```
curl -X POST http://localhost:3010/api/orgs/no-thought/feedback -H "Authorization: Bearer $EYE_OF_GROK_INGEST_TOKEN" -H "Content-Type: application/json" -d '{"botId":"outreach-and-negotiation","rating":"down","tag":"missing","comment":"ask for the minimum order quantity up front","source":"owner"}'
```

Logan's live 👎 (same comment) is the second, which triggers the proposal.

**Decided 6:35 PM CT (GM):** no tunnel. The install uses the export files; the 👎 and the retro run in Logan's browser on `localhost:3010`. Push only from `~/Projects/groklactic/groklactic-harness` (`bot-team`) by 7:45.


**Risks**
1. `clothing-team.json` lands at 7:05, five minutes before the dry run. Names and trigger phrases must be matched then (business_id and RFQ skill path already confirmed).
2. The install beat is the riskiest: share id unknown, rehearsal bots may collide. The JSON fallback is the backup.
3. Live Higgsfield render is ~30 s (test). Cover it with the cost-check talk track plus the Vendor Scout cut. The mockup is the backup.
4. The vendor shortlist mixes real mills (public research, needs re-verifying) with **example** factories. Say "example factories" if asked. Never send the RFQ.
5. Seed files may still say "Dana" (insurance). The on-screen founder is **Logan**.
6. Hoodie isn't on No Thought's v0 SKU list (the hero there is the run short). It's fine as a demo hero, but don't claim it's the launch SKU.
7. groklactic repo is empty. Push by 7:45.

**[TODO: confirm]**
- [ ] `clothing-team.json` bot names = Brand Chief of Staff / Design Studio / Vendor Scout / Outreach & Negotiation / Launch & Growth / Ops & Retro
- [x] Clothing `business_id` = `no-thought`; retro edits `verticals/clothing-brand/bots/outreach-and-negotiation/skills/rfq-draft/SKILL.md` (Setup Architect, 6:30 PM CT)
- [ ] Grok Bot template **share id**
- [ ] Intake path, industry picker labels, submit label, post-submit redirect
- [ ] Plan and feedback endpoints actually match the Setup Architect's assumed contract
- [ ] Where thumbs live (eye-of-grok UI or in-chat)
- [ ] Higgsfield credit cap value and current balance (test cost 0.25 cr, <30 s: confirmed)
- [ ] The insurance swap regenerates live, or loads the pre-generated plan
- [ ] `?reset=1` covers the new data. Rehearsal-bot reset approach
- [ ] Stripe test mode visible anywhere in Ops & Retro, or just stated
- [ ] plan.md updated to these names, Logan as founder, and the 7:10 dry run
