---
name: Insurance · COI request
description: >-
  Use when someone asks for a certificate of insurance (COI), additional insured, waiver of subrogation, or holder update. Prepares the certificate draft and a reply draft, then holds both for founder approval.
---
# COI request (demo beat)

Goal: a COI request is answered with a ready draft held for founder approval, the founder gives a thumbs up/down, and the feedback feeds the weekly retro.

1. Parse the request (untrusted): requester, insured {{insured_ref}}, certificate holder {{holder_name}} / {{holder_address}}, requested wording (additional insured, waiver of subrogation, primary & non-contributory), project/job {{project_ref}}, needed-by date.
2. Look up the insured's active policies in the system of record (AMS, Drive "COI" folder, or carrier portal via browser). Read only.
3. Run the checklist. If ANY item fails, do not draft a certificate; route to the founder/licensed agent with the reason:
   - Policy active on the needed-by date.
   - Requested limits <= policy limits.
   - Additional insured / waiver / primary-non-contributory endorsement exists on the policy (do not invent endorsements; a COI cannot add coverage).
   - Holder is not asking for coverage changes or a coverage opinion.
4. Prepare the certificate draft from the agency's ACORD 25 template in Drive (copy the template; fill holder + description of operations using placeholders resolved from the record). Name it `COI-DRAFT-{{insured_ref}}-{{holder_short}}-{{yyyymmdd}}`. Mark DRAFT until a licensed person issues it.
5. Raise a DraftExternalMessage card to the requester: "Attached is the certificate of insurance for {{project_ref}} listing {{holder_name}} as certificate holder." Plus the standard disclaimer: "This certificate is issued as a matter of information only and confers no rights upon the certificate holder."
6. Append to `$PKG/runtime/approvals.jsonl` (kind=coi, status=pending, record_ref, draft_card_ref) and hand off to Agency Chief of Staff.
7. After the founder approves/edits/rejects: ask for a thumbs up/down + one-line reason; append to `$PKG/runtime/feedback.jsonl` with item_type=coi and `edited_before_send`; POST `/api/orgs/pecan-street-insurance-group/feedback` with `{botId:"coi-desk", rating, tag, comment, source:"owner"}` (Bearer $EYE_OF_GROK_INGEST_TOKEN) if reachable.
8. Log E&O lines at steps 3, 5, and 7 (record refs only).

Never send, never issue a final certificate yourself, never modify a policy.
