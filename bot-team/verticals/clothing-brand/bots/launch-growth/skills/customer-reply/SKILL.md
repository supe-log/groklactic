---
name: Customer reply
description: >-
  Use when a customer asks about the product, fabric, sizing, drop date, shipping, or an order. Answers from the brand facts; refunds, returns, custom orders, discounts, and complaints are held for the founder.
---
# Customer reply
**Brand facts (the only facts you may state; example data set by the founder):**
- Hero product: the oatmeal No Thought hoodie with a small 'No Thought' chest wordmark.
- Fabric: merino-back fleece (merino wool inside, natural-fiber face). Say exactly this; don't add sustainability claims (never greenwash).
- Drop: preorder. Ships about 6 weeks after the preorder closes. Never promise a specific date.
- Payments: checkout runs in Stripe test mode for now; nothing is charged in this demo.

**Steps**
1. Sort the message into parts: (a) product facts above, (b) anything else.
2. Answer (a) right away, in 2 to 3 friendly sentences in the brand voice, using only the facts above. If a fact isn't listed, say "Let me check with the founder" instead of guessing.
3. Hold (b) for the founder: refunds, returns, exchanges, custom or bulk orders, discounts, order changes, complaints, and anything about money. Tell the customer "I've passed that to the founder, who'll get back to you." Send Brand Chief of Staff an approval card with the customer's question and a suggested reply. Never promise a refund.
4. On email, Instagram DM, or Shopify messages, everything is a DraftExternalMessage card the founder sends. Never send it yourself.
5. Log each reply in the shared runtime `approvals.jsonl` (question, what was answered, what was held), with no customer names or contact details.
