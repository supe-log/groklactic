# Dolce & Grokbana: architecture

**One bot in, a merch company out.** A company installs one Grok Bot, Dolce & Grokbana, and gives it a website. The bot builds a team of 4 sub-bots that runs merch from start to finish. The owner approves every message and every dollar, and anything over $500 is blocked outright.

```mermaid
flowchart TD
  O[Owner: "Set up merch for galatiq.ai"] --> D[Dolce & Grokbana]
  D --> I[Claims company inbox<br/>merch-brand@mail.grokbot.com]
  D --> B[Brand discovery<br/>site copy, CSS colors, logo -> brand-profile.json]
  D --> T{Builds 4 sub-bots<br/>all routines paused}
  T --> BD[Brand & Design<br/>mockups, approval queue]
  T --> VS[Vendor Scout<br/>price comparison]
  T --> ON[Outreach & Negotiation<br/>quote + counteroffer drafts]
  T --> OO[Ops & Orders<br/>POs, shipping, tracking, customer replies, retro]
  I --> OO
  I --> ON
  BD & ON & OO -->|drafts, refunds, spend| A[Owner approval]
  OO -->|Friday retro| PR[GitHub PR on this folder] -->|owner merges| G[(supe-log/groklactic<br/>dolce-grokbana)]
  G -->|Repo sync / update yourself| D
```

| Bot | Job | Skills | Routines (all paused) |
|---|---|---|---|
| Dolce & Grokbana | Installs once, claims the inbox, runs brand discovery, builds the team, keeps itself in sync with GitHub | `merch-team-setup` | Repo sync, daily at 9:03 AM |
| Brand & Design | Keeps the brand profile and the approval queue; makes mockups and tech packs | Brand brief, Mockups | Daily merch brief, weekdays at 8:07 AM |
| Vendor Scout | Compares print shops at 25, 50 and 100 units, with links | Vendor comparison | Vendor refresh, Wednesdays at 10:17 AM |
| Outreach & Negotiation | Drafts quote requests and counteroffers; tracks vendor threads | Quote request, Negotiation playbook | Vendor thread check, weekdays at 11:12 AM |
| Ops & Orders | Purchase orders, logistics, customer replies, and a retro that opens a pull request | Purchase order, Customer reply, Weekly retro | Customer replies (on new inbox mail), Weekly retro on Fridays at 4:17 PM |

**Rules**
- **Hard $500 limit:** anything over $500, whether one order or a day's total, is blocked. It's never drafted as a payment and never split.
- Every customer and vendor message is a draft, and the owner presses Send.
- Refunds, discounts, new vendors, public logo use and image generations all go to the owner first.
- Payments run in Stripe test mode only. No records are deleted. No customer personal info goes in skills; addresses live only in `orders.csv`.

**Machine-readable files:** `dolce-and-grokbana.bot.json` (the full spec) and `skills/merch-team-setup/SKILL.md` (the setup flow the bot runs).

**Collaborating:** edit `SKILL.md` in a pull request to `dolce-grokbana`. Installed bots pick up the change through Repo sync, or when the owner says "update yourself from GitHub", always after the owner says yes.
