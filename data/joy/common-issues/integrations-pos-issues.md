---
category: Common Issues
topic: Integrations & POS Issues
source: reports/weekly-faqs/joy + cs2 KB
---

Q: How does Joy sync with Klaviyo, and what variables do I use?
Q: Does Joy sync to Omnisend the same way it does to Klaviyo?
A: Both sync the same **profile properties**, updated automatically as they change in Joy: points balance, VIP tier, member status, referral link, birthday.

Klaviyo template syntax: `{{ person|lookup:'Joy Loyalty Points'|default:'' }}` (also `'Joy Vip tier'`, `'Joy member status'`, `'Joy Referral URL'`, `'Birthday'`) for profile data. Use `event|lookup` instead of `person|lookup` for data carried by a triggering event (e.g. bonus points on an Earn/Tier-reach flow), since profile properties can briefly lag the event by a few seconds — if a tier-reach email shows the wrong/previous tier, switch that specific email to the **event** property.

Omnisend has the same fields as Klaviyo, plus a manual **Sync Again** button if a recent change hasn't reflected yet.

If a merchant confirms the integration is connected but the sync still looks incomplete or variables are empty, ask which profile they're previewing, request a screenshot of the Klaviyo/Omnisend profile, and escalate with `<escalate_human>`.

---

Q: My Shopify Flow workflow using Joy actions/triggers isn't working.
A: Common causes: Flow setup itself is incorrect, the Shopify Flow integration isn't enabled in Joy, or a bug. Check in order:
1. What is the merchant trying to achieve (intended trigger, action, goal)?
2. Confirm **Joy Admin → Integrations → Shopify Flow** toggle is on.
3. Ask for a screenshot of the Flow configuration.

If the integration isn't enabled, guide the merchant to enable it. If it's enabled and setup looks correct but still fails, request store access (ask permission, collect the collaborator code) and escalate with store URL, intended flow logic, screenshots, and confirmation the integration is enabled, `<escalate_human>`.

---

Q: The Shopify Pixel "Connect" button doesn't complete — it just reopens the Joy app.
Q: My Joy pixel shows "Disconnected" in Shopify Customer Events.
A: This is a recognized, recurring issue. First fix: reopen the Joy app and re-accept/re-authorize the permission prompt — Shopify sometimes requires a freshly-scoped grant that the first click doesn't complete. Then check **Shopify Admin → Settings → Customer Events** (or Checkout Settings → Tracking and analytics → App pixels) for "Connected" status. If re-authorizing doesn't fix it, toggling the **Referral program** off and back on can also refresh the pixel connection, since the pixel is tied to referral tracking specifically.

If a merchant only uses Joy for points/VIP tiers with no referral, sign-up, or reward-celebration popups, **no App Blocks are required** on the Thank You/Order Status page at all. If re-authorizing doesn't surface a connect option or the pixel stays Disconnected, escalate for the team to recreate the pixel, with store URL, a screenshot of Customer Events, and a short video of the Connect button behavior, `<escalate_human>`.

---

Q: Does Joy have an API for custom integrations?
A: Yes — REST API v2 and a Webhook API (customers, point transactions, rewards, VIP tiers, referrals, 20+ real-time events), exclusive to the **Ultimate** plan. Lower plans get a `PLAN_UPGRADE_REQUIRED` error. Generate credentials at **Settings → Developers → Manage keys**.

---

Q: My POS tile shows an error, is stuck loading, or points aren't syncing at the register.
A: POS redemption requires **Advanced or Ultimate**; Essential POS supports earn-only points display. Self-fix first: update the Shopify POS app to the latest version, then remove and re-add the Joy tile from scratch (the tile should be named "Joy Loyalty" after re-adding). Confirm the relevant earn/redeem program has **Sales channels** including **POS** — programs aren't POS-enabled by default. Also confirm a customer was attached to the sale **before payment completed** — Shopify doesn't retroactively pass customer info to Joy if it's added only when emailing the receipt afterward.

If it persists, collect device model, OS version, and Shopify POS app version, and escalate with `<escalate_human>`. If it's a permissions error specifically, check **Shopify Admin → Settings → Users and permissions** (or Roles) — the POS staff account needs Joy app access enabled under App permissions (or, for role-based stores, "Use apps that work with Shopify POS" + "Manage POS UI extensions" under Point of Sale permissions).

---

Q: A customer added in-store (POS) can't access their loyalty account online.
A: With **New Customer Accounts**, the customer logs in online with the **same email** used at POS via the email/one-time-code flow — no password needed. In-store and online activity tie to the same email and the same points balance. If they're seeing a separate account, that's usually a duplicate-account case (different email/phone at POS vs online) — see the customer-data topic for merging.

---

Q: Joy is causing a console error, redirect, or "Missing Key" message on my storefront.
A: Collect the store URL, the exact page/action, and a screenshot of the console error. These are usually theme/snippet/Liquid or configuration issues, sometimes merchant-side theme errors rather than Joy itself. If the app pixel is involved, check **Settings → Customer Events** to confirm Joy is enabled. Request temporary collaborator/theme access if investigation is needed, escalate to the team, and ask the merchant to revoke access afterward, `<escalate_human>`.
