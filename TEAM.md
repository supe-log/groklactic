# Team 4 run sheet (Grok Bot Hackathon, Oct 19 2026)

All times are CT. Build stops at 8:30, when judges come around for about 5 minutes per team.

## Who does what
**Logan (captain, drives the demo)**
- Runs the eye-of-grok app on his Mac (`localhost:3010`).
- 7:10 dry run with Demo Coach.
- Approves the setup-template export card in his 1:1 chat with Setup Architect.

**Isaac (narrator and Track 2 tester)**
Isaac tests on **his own Grok Bot**, which has never seen the product. That's the Track 2 proof.
1. Start a brand-new Grok Bot. Paste in only this: "Read https://github.com/supe-log/groklactic (branch bot-team), install the Setup Chief of Staff from `bot-team/setup-cos-template.md`, then say Build my team for the business No Thought."
2. Log every step that needs a human, and every error, in the team chat. Report by 7:25.
3. Learn the narration in `bot-team/demo.md`, including the line "Second time this week, so now it's a pattern."

**Jeff (customer, fallback, and reset)**
1. **The customer.** In the live demo, Jeff sends the brand's Launch & Growth bot a message as a customer: "Is the hoodie merino, and when does it ship? Also can I get a refund if it doesn't fit?" The bot answers the facts and holds the refund question for the founder.
2. **Fallback.** During the 7:10 dry run, screenshot every screen that works into `bot-team/fallback/` (numbered `01-...png`).
3. **Reset.** Before judging, run `?reset=1`, then post the first 👎 on Outreach & Negotiation with the `curl` in `bot-team/demo.md`.

## Timeline
- 7:00: the "Clothing brand" option is in the app, or we use "Other small business" with the name No Thought.
- 7:05: the customer-reply skill and the template link are ready.
- 7:10 to 7:40: dry run. 7:45: final push.
- 8:00: freeze. 8:00 to 8:25: rehearse twice. 8:30: judging.

## Rules
- Nothing sends without Logan. All messages are drafts.
- Payments stay in Stripe test mode, and nothing over $500 goes through without approval.
- No secrets and no `grok-bot-app/` code in the repo.
