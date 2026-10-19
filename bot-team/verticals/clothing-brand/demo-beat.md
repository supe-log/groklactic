# Demo beat: "Design our first drop" (No Thought, orgId `no-thought`)

Hero product (`hero_product`, configurable): **natural-fabric hoodie**. Detail: an oatmeal hoodie with a small "No Thought" chest wordmark.
Backup mockup, in case of a live failure: `/workspace/groklactic/clothing/mockup-hoodie-01.png` (also at `fallback/04-hoodie-mockup.png`).

1. **Founder → Brand Chief of Staff:** "Design our first drop." This runs the Drop kickoff skill, which briefs Design Studio and Vendor Scout in parallel.
2. **Design Studio** runs the verified Higgsfield steps (tested live: under 30s and 0.25 credits per image):
   `balance {}` → `generate_image {"params":{"model":"gpt_image_2_5","aspect_ratio":"1:1","prompt":"x","get_cost":true}}` → 3× `generate_image {"params":{"model":"gpt_image_2_5","aspect_ratio":"1:1","count":1,"use_unlim":false,"prompt":"oatmeal natural-fabric hoodie, small 'No Thought' chest wordmark, minimalist studio product shot, soft natural light, no other logos"}}` → `jobs_wait {"jobs":[{"index":0,"job_id":"<id>"}],"timeout_seconds":15}`.
   About 0.75 credits total, well under the 50-credit cap. The 3 mockups are held as **proposals**.
3. **Vendor Scout** returns 3 cut-and-sew / fleece candidates. Each comes with source URLs, MOQ, price band, lead time, and certifications marked verified or unverified. No vendor is called "vetted".
4. **Outreach & Negotiation** drafts an RFQ to the top candidate as a **DraftExternalMessage card held for founder approval**. Nothing is sent. No price or MOQ is committed (the $500 cap applies).
5. **Founder gives 👎** on the RFQ: "ask for the minimum order quantity up front". Feedback is recorded with `POST /api/orgs/no-thought/feedback {botId:"outreach-and-negotiation", rating:"down", tag:"missing", comment:"ask for the minimum order quantity up front", source:"owner"}`. The local seed is `verticals/clothing-brand/examples/seed-feedback.jsonl`.
6. **Ops & Retro:** "Run the retro now". This calls `POST /api/orgs/no-thought/retro`, then `GET /changes?status=open`. The proposal is `add_rule` on `outreach-and-negotiation`: add an MOQ-first line to `verticals/clothing-brand/bots/outreach-and-negotiation/skills/rfq-draft/SKILL.md`. The founder approves, then `POST /changes/{id} {decision:"approved"}`, then UpdateSkill on rfq-draft, then `POST /changes/{id}/applied`.

Every routine stays paused throughout. Nothing sends, publishes, orders, or pays.
