---
category: Common Issues
topic: Customer Data & Export Issues
source: reports/weekly-faqs/joy + cs2 KB
---

Q: How do I export my Joy customer / points data?
Q: I don't see an Export button on the Customers page.
A: For activity-level exports: **Customers → Activities** → set a date range → choose Export type (Earned/Redeemed) → enter an email to receive the file. For a full customer list: **Customers → Export** — if that button isn't visible, it needs to be **enabled by the Joy team first**; collect the store URL and escalate, `<escalate_human>`.

Exports are **CSV only** (no native Excel) — open in Google Sheets or convert manually if needed. There's no in-app sort by points value, and no combined "Customer name + Order ID + Points earned" report built in — for that specific combination, or a VIP tier column added to the standard export, the team can generate it manually on request for a given period.

---

Q: A single customer shows up as two different accounts in Joy.
Q: Can you merge duplicate customer accounts?
A: Shopify creates two separate customer IDs when identifying info doesn't match exactly — most often when a customer buys in-store via POS without using the same email/phone as their online account. Joy then reflects two distinct customers.

Verify with the merchant that the two accounts are the same person and collect both emails. If they agree, escalate to the team to perform the merge (CS does not merge accounts directly in Joy — it depends on Shopify's own customer merge), `<escalate_human>`. After merging, Joy syncs points/tier into the single remaining account.

If the duplicate came from a **wrong email entered at POS** (not a genuine two-account case): the team can remove the misplaced points/activity from the wrong account but can't move them without the correct email, since Joy's customer data syncs from Shopify. Have the merchant correct the Shopify customer's email first, let it sync, then escalate to adjust points onto the correct account.

---

Q: My Joy customer count doesn't match my Shopify customer count.
A: After install, all customers should sync from Shopify to Joy automatically — sync can fail for some. Ask the merchant for their Shopify customer count to confirm the mismatch. If it persists, escalate with the store URL to trigger a customer sync, `<escalate_human>`.

---

Q: Searching for a customer by name returns nothing, even though they exist.
A: There was a known bug in name-based search that's since been fixed. Have the merchant search by **email**, **order ID**, or **coupon code** instead — those always work reliably from the Quick Search bars on the Joy homepage and Reward programs page. If name search specifically still fails after trying that, collect the store URL and a sample customer name and escalate, `<escalate_human>`.

---

Q: Can I get a retroactive points update for orders placed before the earning rule existed?
Q: Can you bulk-add points or credit customers for past orders?
A: There's no self-serve retroactive sync — the team runs it manually for a merchant-specified date range, applying the **current** rule settings (rate, product eligibility) to historical orders and skipping cancelled/refunded ones. It doesn't touch other programs (e.g. sign-up bonus) — those need their own separate sync request. If the merchant also uses VIP Tiers, confirm whether tier points should be recalculated at the same time — the tier program has its own start date gating which historical points count toward progress. Collect store URL and date range, then escalate, `<escalate_human>`.

**After any import or sync, points and Amount Spent don't recalculate on their own** — the merchant needs to **Launch** (or re-launch) the relevant program to trigger recalculation.
