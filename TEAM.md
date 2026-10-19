# Team 4 run sheet (Grok Bot Hackathon, Oct 19 2026)

All times are CT. Build stops at 8:30, when judges come around for about 5 minutes per team.

## Who does what
**Logan (captain, drives the demo)**
- Runs the eye-of-grok app on his Mac (`localhost:3010`).
- 7:10 dry run with Demo Coach.
- Approves the setup-template export card in his 1:1 chat with Setup Architect.

**Isaac (narrator and fresh-bot tester)**
Isaac uses **a brand-new Grok Bot that has never seen any of this**. That's the Track 2 proof and our accuracy check.
1. **Install, by 7:05.** Paste in only: "Read https://github.com/supe-log/groklactic (branch bot-team), install the Setup Chief of Staff from `bot-team/setup-cos-template.md`, then say Build my team for the business No Thought." Don't add any other hints.
2. **Accuracy scorecard, posted in the team chat by 7:25.** Mark each line pass or fail, and note anything that needed a human:
   - [ ] Six bots built, with names matching `bot-team/clothing-team.json`: Brand Chief of Staff, Design Studio, Vendor Scout, Outreach & Negotiation, Launch & Growth, Ops & Retro.
   - [ ] Every routine paused.
   - [ ] The founder rules are in each bot: nothing sends, no PO, deposit, publish or spend without approval, nothing over $500, Stripe test mode.
   - [ ] Outreach & Negotiation, prompt "Draft an RFQ for the hoodie": a real RFQ draft, held for approval and not sent.
   - [ ] Launch & Growth, prompt "Is the hoodie merino, and when does it ship?": answers from the brand facts and doesn't make anything up.
   - [ ] Launch & Growth, prompt "I want a refund": held for the founder.
   - [ ] Ops & Retro, prompt "Run the retro now": proposes exactly one change and waits for approval.
   - [ ] Count how many questions it asked and how many minutes the whole run took.
3. **In the demo** Isaac also plays the customer, asking the merino, ship-date and refund questions live.
4. **Narration.** He reads the 60-second pitch in `bot-team/demo.md` aloud twice against a timer.

**Reset and screenshots (Chief of Staff, on Logan's Mac)**
- Rehearse only on a throwaway id such as `nt-rehearse-1`, because the reset doesn't clear old feedback. Keep `no-thought` clean for the judges, and post its first 👎 just before 8:30.
- During the 7:10 dry run, capture each screen that works into `bot-team/fallback/`.

**Jeff (optional)**
- Install the Adapter plugin, which Dylan's email asks for. Be a second pair of eyes during rehearsal.

## Timeline
- 7:10 cutoff: if the No Thought six-bot plan isn't served by the app, the dry run and the demo lead with insurance (`/u/ins-test-1842/team` works today), and clothing becomes the Higgsfield bonus beat.
- 7:05: the customer-reply skill and the template link are ready.
- 7:10 to 7:40: dry run. 7:45: final push.
- 8:00: freeze. 8:00 to 8:25: rehearse twice. 8:30: judging.

## Rules
- Nothing sends without Logan. All messages are drafts.
- Payments stay in Stripe test mode, and nothing over $500 goes through without approval.
- No secrets and no `grok-bot-app/` code in the repo.

## Rehearsal rule
Rehearse on a throwaway id (e.g. `no-thought-rehearsal`), never on `no-thought`. `?reset=1` does not clear stored feedback.
Quick health check on Logan's Mac: `INGEST_TOKEN=<token> INDUSTRY=small_business ./scripts/demo-check.sh <throwaway-id>`.
