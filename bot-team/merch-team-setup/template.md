# Dolce & Grokbana (Grok Bot marketplace template)

**Description:** Install one bot and give it your company's website. It builds a team of 4 merch bots that designs, sources, quotes and sells your branded clothing, and nothing ships, sends or spends without your OK.

**Getting started skill:** `merch-team-setup` (`skills/merch-team-setup/SKILL.md`). The plan is self-contained, so it needs no website or login.

**Trigger:** "Build my team" or "Set up merch for <site>".

**Team (4):** Brand & Design, Vendor Scout, Outreach & Negotiation, Ops & Orders. Every routine starts paused, including Customer replies.

**Founder approval:** spending over $500, refunds, discounts and credits, new vendors, public use of the logo, and image generations. Payments run in Stripe test mode only, and all messages are draft-only.

**Plugins:** Adapter (70141458) is packed. Gmail or Outlook, Drive and Higgsfield are installed during the build.

**What it needs:** before building, the bot checks and tells you plainly what is ready and what is missing. Required: website reading (web fetch, falling back to the browser if the site blocks scraping, or your own 3-line description) and its own company inbox. Recommended: Gmail or Outlook, Google Drive, and Higgsfield for mockups. Optional: GitHub for retro pull requests, Stripe in test mode, and Adapter. Anything missing comes with a connect card or a fallback, and it never asks for keys or passwords.

**Company inbox:** at setup the bot claims its own `@mail.grokbot.com` address for vendors and customers. Every email out of it is still a draft until the owner approves it.

**Hard $500 limit:** anything over $500, whether one order or a day's total, is blocked outright and never split to get under the limit.

**Logistics:** Ops & Orders handles missed and late orders, shipping per customer, tracking and reships, all logged in `orders.csv`.

## Collaborating on this bot
This folder is the source of truth. To change the bot's prompts, routines or setup flow, edit `skills/merch-team-setup/SKILL.md` in a pull request to `dolce-grokbana`. Installed bots pick up the change through their paused **Repo sync** routine, or when the owner says "update yourself from GitHub". The owner approves before anything is applied.
