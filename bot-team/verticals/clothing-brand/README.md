# Clothing brand vertical: No Thought (orgId `no-thought`)

This is the same package format as insurance. The real-world baseline is the **No Thought GM / Brand / Product / Growth** bot briefs (`baseline_source` in `clothing-team.json`). The founder's real brand is used; there's no personal PII.

| Bot (slug) | Job | Routines (paused) |
|---|---|---|
| Brand Chief of Staff (`brand-chief-of-staff`) | Approval queue, daily brief, Drop kickoff ("Design our first drop"), 👍/👎 after each decision | Weekdays 8:07 AM CT |
| Design Studio (`design-studio`) | Higgsfield mockups (verified steps), mood boards, tech-pack outline, ad creatives (quote first) | Mon 9:37 AM CT |
| Vendor Scout (`vendor-scout`) | Manufacturer, mill, and trims research with a source URL on every claim; comparison table | Wed 10:17 AM CT |
| Outreach & Negotiation (`outreach-and-negotiation`) | RFQs, follow-ups, counteroffers. Draft cards only. Tracks thread state | Weekdays 11:12 AM CT |
| Launch & Growth (`launch-growth`) | Waitlist, launch plan, content calendar, Higgsfield shorts, TikTok via `tiktok_prepare_publish` only | Mon 10:47 AM CT |
| Ops & Retro (`ops-retro`) | Samples, landed cost/COGS, PO drafts (Stripe test mode), retro ("Run the retro now") | Fri 4:17 PM CT; Tue/Thu 9:52 AM CT |

**Caps:** `spend_cap_usd` 500 and `credit_cap_per_run` 50. Founder approval is required for any outbound message, batch or video generation, run over the credit cap, publish, PO, deposit, sample payment, contract, or price/MOQ commitment over the cap. Nothing orders or pays without the founder. No IP-infringing designs.

**Files:** `plan/clothing-brand.plan.json`, `team.json` (also copied to `/workspace/groklactic/clothing-team.json`), `intake/clothing-brand.intake.json`, `bots/*/instructions.md` and `skills/*/SKILL.md`, `examples/seed-feedback.jsonl`, `demo-beat.md`, `../../exports/no-thought.teamplan.json`.

**Higgsfield tool names** are checked by the validator against `config/higgsfield-tools.json` (a snapshot of the real `user-Higgsfield` catalog).
