---
category: Common Issues
topic: Referral Program Issues
source: reports/weekly-faqs/joy + cs2 KB
---

Q: When exactly does the referrer get rewarded?
Q: My referral is enabled but the referrer never got their reward.
A: Flow: referrer shares their unique link → referee clicks it, lands on the referral page, enters their email → a **7-day cookie** stores the pending status → referee places an order **with the same email** → activity completes on the thank-you page → both sides are rewarded. The **referee's** reward issues immediately at the claim step; the **referrer's** reward stays pending until the referee's order reaches the shop's earn-status trigger — **Paid** by default (granted as soon as the referee's order is Paid), or **Fulfilled** (shows "Awaiting fulfilment" in the meantime — this is normal, not a failure).

If the referrer still didn't get rewarded, check the common blockers:
- **Different emails** — referee used a different email at claim vs checkout; both sides need the same email.
- Referee's order **subtotal is $0** — anti-cheat requires a subtotal greater than $0.
- **Anti-cheat block** — referrer and referee shared the same browser, email, or IP, or reused the same order.
- Referee's order was **fully refunded** and **Auto-revoke referrer reward** is on (the reward was granted then revoked).
- Referrer hit the **referral limit** — a per-program cap, or the Free plan's referral-order cap.
- **Cookie expired** (more than 7 days between click and purchase) — but the referrer can still be rewarded if the referee's order uses the same email entered at claim, even past the cookie window.
- **App pixel disabled** — check Shopify Admin → Settings → Customer Events → Joy is enabled; toggling the referral program off/on can re-sync it.
- The referral program is still in **Sandbox/preview** mode — go live for real rewards.

If everything checks out, escalate with referrer email, referee email, order number, and collaborator code if provided, `<escalate_human>`.

---

Q: Can I extend the 7-day referral cookie window?
A: The tracking cookie is **fixed at 7 days**, with no merchant-facing setting to extend it — but the link itself never expires and generates a fresh 7-day cookie on every new click. Even if the cookie technically expires before the referred friend orders, the referrer can still be rewarded if the friend's order uses the **same email** they entered when claiming the referral — Joy matches by order email, not solely the cookie.

---

Q: Is there any verification before the referee's discount code is issued?
A: By design, no — the referee's discount is issued as soon as they enter an email on the referral landing page, with no account or email-ownership verification at that step. This keeps the referral flow low-friction. Fraud is controlled separately by **Anti-cheat**, which blocks a referral if the referrer and referee share the same browser/email/IP address, or reuse the same order.

---

Q: Referral is enabled but I don't see it anywhere in the widget.
A: Referral sharing lives inside the loyalty widget itself (and, on Advanced+, the Referral Management block on the account page) — it isn't a separate floating element by default. Add the **Referral block** to the loyalty page or thank-you page for extra visibility, or use the `#joy-referral-program` deeplink in a menu item or button. If the section isn't showing in the widget at all, check it's toggled on under **On-site content → Widget → Referrals** AND that the underlying **Referral program** is turned on at **Reward programs → Referrals** — these are two separate switches.

---

Q: How can I see how many people have referred my brand, and what do the export status fields mean?
A: Referral performance shows in **Analytics → Referred revenue** and in **Referral Management**, which shows per-customer referral counts. For export status fields: "Pending"/"Awaiting fulfilment" means the referee claimed but the qualifying order hasn't reached the reward trigger yet; "Completed" means the referrer's reward has been granted. If a "Completed At" timestamp shows on a row still marked Pending, that's a display inconsistency in the export rather than the referral actually being complete — send the export to the team for review, `<escalate_human>`.

---

Q: What can store credit be used as a reward for, and can customers apply just part of their balance?
A: Store credit can only be granted as a reward from **three** sources: a **Place Order** earning rule, a **Milestone** reward (Advanced+), or the **Referral** program. Because store credit is Shopify's native balance rather than a Joy coupon, Joy has no control over partial use — once a customer applies store credit at checkout, Shopify applies the **entire balance**, not a chosen portion. There's no per-order cap or partial-redeem option today.
