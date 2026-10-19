# Clothing / merch vertical (worked example: No Thought, orgId `no-thought`)

This is the same package format as insurance, and it adapts to **any** clothing or merch business (a DTC label, a band, a traveling chess club that wants tees). Nothing brand-specific is hardcoded in the bots:

1. **Brand discovery runs first** (skill `brand-discovery`, Brand Chief of Staff). It asks once for website/social links and uploads (or 3 lines of description), uses the optional **Adapter** plugin (id `70141458`) for cited business context when available, else web fetch/browser, and writes `$PKG/runtime/clothing-brand/brand-profile.json` (shape: `brand-profile.template.json`). Every fact has a source URL or is marked `unverified` / `founder-stated`.
2. Every other skill starts with "Read the brand profile first" and uses `{{brand_name}}`, `{{category}}`, `{{audience}}`, `{{city}}`, `{{aesthetic}}`, `{{palette}}`, `{{materials}}`, `{{hero_product}}`, `{{wordmark}}`. Vendor Scout picks the vendor type from the product (cut-and-sew/mills for premium garments; blanks + print/embroidery/print-on-demand for merch). Customer reply states only `product_facts` / `ship_window` / `payments_note` from the profile.
3. **No Thought is the worked example only:** `examples/no-thought.brand-profile.json` is used when business_id is `no-thought` (its customer-reply facts: "merino-back fleece", "ships about 6 weeks after the preorder closes", Stripe test mode).

Skill names are prefixed `Clothing · ...` (insurance uses `Insurance · ...`) so both teams can coexist on one account. `$PKG` = the package root (the repo's `bot-team/` folder); runtime files live in `$PKG/runtime/clothing-brand/`. No personal PII.

| Bot (slug) | Job | Routines (paused) |
|---|---|---|
| Brand Chief of Staff (`brand-chief-of-staff`) | Brand discovery (first), approval queue, daily brief, Drop kickoff ("Design our first drop"), 👍/👎 after each decision | Weekdays 8:07 AM CT |
| Design Studio (`design-studio`) | Higgsfield mockups (verified steps), mood boards, tech-pack outline, ad creatives (quote first) | Mon 9:37 AM CT |
| Vendor Scout (`vendor-scout`) | Manufacturer, mill, and trims research with a source URL on every claim; comparison table | Wed 10:17 AM CT |
| Outreach & Negotiation (`outreach-and-negotiation`) | RFQs, follow-ups, counteroffers. Draft cards only. Tracks thread state | Weekdays 11:12 AM CT |
| Launch & Growth (`launch-growth`) | Waitlist, launch plan, content calendar, Higgsfield shorts, TikTok via `tiktok_prepare_publish` only | Mon 10:47 AM CT |
| Ops & Retro (`ops-retro`) | Samples, landed cost/COGS, PO drafts (Stripe test mode), retro ("Run the retro now") | Fri 4:17 PM CT; Tue/Thu 9:52 AM CT |

**Caps:** `spend_cap_usd` 500 and `credit_cap_per_run` 50. Founder approval is required for any outbound message, batch or video generation, run over the credit cap, publish, PO, deposit, sample payment, contract, or price/MOQ commitment over the cap. Nothing orders or pays without the founder. No IP-infringing designs.

**Files:** `plan/clothing-brand.plan.json`, `team.json` (also copied to `clothing-team.json` in the package root), `intake/clothing-brand.intake.json`, `bots/*/instructions.md` and `skills/*/SKILL.md`, `examples/seed-feedback.jsonl`, `examples/no-thought.brand-profile.json`, `brand-profile.template.json`, `demo-beat.md`, `../../exports/no-thought.teamplan.json`.

**Higgsfield tool names** are checked by the validator against `config/higgsfield-tools.json` (a snapshot of the real `user-Higgsfield` catalog).

**Seed feedback field names:** `examples/seed-feedback.jsonl` uses the local log shape (`bot`, `reason`). The eye-of-grok API expects `botId` and `comment` (`POST /api/orgs/{orgId}/feedback` with `{botId, rating, tag, comment, source}`), so map `bot -> botId` and `reason -> comment` when posting a seed line.
