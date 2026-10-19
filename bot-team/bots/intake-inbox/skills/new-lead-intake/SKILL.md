---
name: New lead intake
description: >-
  Use when a new prospect contacts the agency (email, web form, call note) to build a PII-safe intake record and checklist for Quote Prep.
---
# New lead intake

1. Create an intake record in the system of record (AMS or the agency's intake sheet) with lines of business requested and source. Do not store SSN/DL/DOB in notes.
2. Build the missing-info checklist from the line of business: personal auto ({{drivers}}, {{vehicles}}, {{prior_carrier}}), home ({{property_address}}, {{year_built}}, {{roof_year}}), commercial ({{fein_on_file}}, {{revenue}}, {{payroll}}, {{class_codes}}).
3. Draft (DraftExternalMessage card) a request for the missing items with a secure-upload link placeholder {{secure_upload_link}}; never ask for SSN by email.
4. Hand off to Quote Prep with record_ref and checklist status.
