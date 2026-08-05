---
category: Common Issues
topic: Billing & Plans
source: reports/weekly-faqs/joy + cs2 KB
---

Q: What's included on each plan (Starter vs Essential vs Advanced vs Ultimate)?
Q: What's the difference between Basic and Pro? (legacy plan names)
A: Pricing is **base monthly fee + free order quota + per-100 overage**:

| Plan | Base | Free orders/mo | Overage |
|---|---|---|---|
| **Starter** | $0 | 250 | n/a |
| **Essential** | $29/mo | 500 | $15/100 |
| **Advanced** | $129/mo | 2,000 | $10/100 |
| **Ultimate** | $499/mo | 7,000 | $5/100 |

Feature gating that comes up most: **VIP Tiers, Rule Engine, Cart Drawer redemption, Milestones, Loyalty Hub (account page), B2B tiers, Wallet passes** — Advanced and Ultimate only. **Points expiration, dedicated loyalty page, birthday rewards, free gift/free shipping redemption, analytics, migration** — Essential and up. **Checkout-page redemption, API/webhooks, Hydrogen/headless** — Ultimate only (checkout also needs Shopify Plus). **Stacking multiple simultaneous earning rules** (base rate + collection bonus + segment bonus, etc., all applying on the same action) needs the **Rule Engine**, which is Advanced+ — Essential doesn't have it. Free trials: 14 days (Essential/Advanced), 30 days (Ultimate), one-time only per store. **"Pro" is the legacy name for Essential** — never show the raw internal `joy_plan` id to a merchant, translate it to the current plan name.

Compare and upgrade at **Settings → Subscription → All plans**.

---

Q: My usage/order-quota fee seems too high — is it only counting Joy-assisted orders?
Q: Why do I see an extra Usage fee on my Shopify bill on top of the monthly fee?
A: No — the usage fee is calculated on **every** order processed through the store, regardless of sales channel (POS, Amazon, TikTok, marketplace-synced) or whether that specific order used a Joy discount, because Joy syncs all orders in real time to track program activity. Once the plan's free monthly order quota is exceeded, additional orders are charged in batches of 100 at the plan's overage rate.

If a merchant wants a specific channel excluded from the count (e.g. a marketplace channel not considered "real store traffic"): this is possible via a consistent order tag, but it removes those orders from the loyalty program **entirely too** (no points, no rewards) — confirm the merchant accepts that trade-off first, then escalate with store URL, tag, and reason, `<escalate_human>`.

Note: usage-fee counting starts the day the trial begins, but the Shopify billing cycle only starts after the trial ends — so the usage period and billing cycle are offset by the trial length (e.g. a 14-day trial creates a 14-day offset).

---

Q: Can I extend my free trial or get temporary access to paid features?
A: The 14-day (Essential/Advanced) or 30-day (Ultimate) trial is strictly **one-time per store** and can't be paused or extended once billing has started, even mid-setup. CS is **not authorized to approve this independently** — collect the store URL, why the merchant needs it, and which plan/feature, then escalate to Sales/CSL for a final decision, `<escalate_human>`. Do not say "I'll enable it for you" or imply automatic approval. If the trial isn't needed, the **30-day refund policy** after upgrading is the fallback, not a trial extension.

---

Q: I want a refund / I cancelled but I'm still being charged.
A: If a merchant cancelled after the trial ended, or mid-cycle, Shopify still bills for the cycle already used — that's expected Shopify billing behavior, not a Joy error. If the merchant genuinely didn't use the app after being charged, escalate to the team for refund consideration, `<escalate_human>`. Refund/cancellation decisions are never approved by CS directly — always escalate to CS Leader.

---

Q: Can I get a discount if I upgrade? / Can you recommend which plan I should be on?
A: CS must **not** offer a discount or recommend a specific plan independently — this risks a mismatch that hurts trust, and all offers must be approved by Sales or CSL first. Acknowledge the request, ask which plan they're interested in (for discount asks) or what they're trying to accomplish (for plan-recommendation asks), then say the request is being forwarded to the specialist team, and escalate with `<escalate_human>`. Do not say "I can offer you X%" or hint that a discount is available.

---

Q: I'm hitting a "transaction limit reached" message — can I get unlimited transactions?
A: A **transaction** = any point-related activity (earning or redeeming), NOT a Shopify order or payment. This is **not a paid-plan feature** — do not tell the merchant they need to upgrade, and do not redirect to pricing. Any merchant who asks can be escalated for it to be enabled, usually at no extra cost. Collect the store URL and escalate, `<escalate_human>` (see the dedicated unlimited-transactions flow for exact scripting).

---

Q: My dev store can't upgrade / I want to test a paid plan before committing.
A: Development stores (created via Partner or affiliate) can't accept app charges until transferred, or until the merchant chooses a paid Shopify plan — they can't upgrade Joy through the App Store this way. CS cannot enable plan features or extend trials independently in this case either. Collect the store URL, why they need the trial/paid access, which plan/feature, and (optionally) a contact email, then escalate to Sales/CSL, `<escalate_human>`.
