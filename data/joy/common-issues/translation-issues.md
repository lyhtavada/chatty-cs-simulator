---
category: Common Issues
topic: Translation Issues
source: reports/weekly-faqs/joy + cs2 KB
---

Q: My widget or loyalty page content isn't translating correctly.
Q: Translations reverted after a theme update.
A: First check the default language at **Settings → Translations** isn't still sitting on English. Most remaining cases are a **third-party translation app** (Translate & Adapt in particular) overriding Joy's own translated fields — check for overridden rows for the affected language and remove them.

If custom translations that were already entered suddenly reverted (commonly after a theme update), that's a real bug worth escalating with the specific fields affected — don't use "Revert to default" as the fix, since that wipes **all** custom translations, not just the broken ones. Escalate with `<escalate_human>` if it's a genuine reversion.

---

Q: Which parts of Joy can't be translated at all?
A: Two things genuinely can't be translated through Joy:
- **Reward product names** shown in redeem rewards — pulled directly from the Shopify product record, so they follow whatever the product is named in Shopify. Fix by editing the product title itself, or using Shopify's own product-title translation (not Joy's).
- Some **VIP tier description strings** inside Customer Accounts can still show untranslated — log the specific surface for the team.

Plan gating: editing English content is available on all plans; changing the default language is Essential+; auto Detect Language is Advanced+.

---

Q: A notification email variable shows raw/untranslatable text — can I edit it?
A: Some system-generated notification variables produce fixed auto-composed text that can't be directly edited or translated in the template editor. Workaround: delete that variable from the email template and type custom wording instead, using whichever narrower variable the template offers for just the value (e.g. the reward amount) rather than the full auto-generated sentence, if one is available. If the merchant needs the exact variable name for their template, escalate with a screenshot of the affected email so the team can confirm it, `<escalate_human>`.

---

Q: I want to add a language that isn't in Joy's translation list.
A: Collect the requested language and the store URL, then escalate to the team with `<escalate_human>` — this is a feature/data request the team handles directly, not a self-serve setting. Update the merchant once the team responds.

---

Q: The Point Calculator variable text I edited broke, and the live number stopped updating.
A: The Point Calculator (**On-site content → Product page → Point calculator**) shows a live "earn X points on this product" preview driven by a placeholder variable in its text template. If a merchant free-types over that placeholder instead of editing around it, the live number stops updating and shows static/broken text instead. Guide them to undo the free-typed edit and confirm the calculator preview updates again as they change a variant/price; if the placeholder was lost and can't be restored from undo, escalate with a screenshot of the current text, `<escalate_human>`.
