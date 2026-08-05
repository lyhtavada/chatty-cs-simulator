---
category: Common Issues
topic: Points Earning Issues
source: reports/weekly-faqs/joy + cs2 KB
---

Q: A customer placed an order but didn't get any points.
Q: Why does the activity log show no Place Order earning event for this order?
A: Work through these in order:

1. **Order hasn't reached the reward status yet** — points fire on the trigger set in Settings → Order (**Paid** or **Fulfilled**). The underlying webhook can also lag Shopify by 40-90 minutes.
2. **Customer checked out as Guest, not a Member** — if the earning rule rewards members only, a guest order earns nothing.
3. **Program was in Sandbox/Test mode** when the order was placed — only test-list emails earn during that window; switching to Live afterward doesn't retroactively credit it.
4. **Payment method excluded** — a program can exclude orders paid via store credit or gift card.
5. **Program date range, product/collection conditions, or order-level exclusions** (tag, source, payment gateway, B2B) don't match — including a Settings → Order filter that sits outside the program's own conditions.

If none of these explain it, collect the order number and customer email — do NOT ask the merchant to check app settings themselves, the team verifies the activity log and order data directly. Create a ticket and append `<escalate_human>`.

---

Q: Why does every customer already show as a "Member," and why didn't they get the sign-up bonus?
Q: My customer never signed up but Joy already lists them as a Member.
A: These are two different things. **Becoming a Member** happens automatically with Shopify's Customer Accounts (SSO) — anyone who leaves an email anywhere on the store (checkout, newsletter form, account creation) gets marked "Enabled" by Shopify, and Joy reads that as a Member.

This is not the same as earning the **Sign-up reward**, which only fires through one of 3 paths:
1. **Storefront** — the customer logs in to a customer account AND the Joy embed widget is active on the theme.
2. **Widget popup "Join"** — customer opens the widget and joins.
3. **POS** — a guest buyer is identified as a member at checkout.

Leaving an email alone never grants the reward. The other common cause: the account was **created before the Sign-up program's start date** — existing customers don't qualify by default; escalate with `<escalate_human>` if the merchant wants a manual pass to include them. If a merchant wants to stop auto-Member status from a bare email, point them to **Settings → General → Customer Eligibility → Manually assigned customers only** — note this changes eligibility going forward, not retroactively for customers already marked as Members.

---

Q: Why aren't social/Instagram follow points being awarded?
Q: A customer left a Google review but never got points.
Q: A customer wrote a product review but didn't receive points.
A: Depends on the program type:

**Social follow/share** is trust-based — there's no API to verify a real follow, so points are awarded on the customer clicking "Complete" in the widget. This is industry-wide, not Joy-specific.

**Instagram-specific programs** (comment, story reply/mention, live comment) need an Instagram Business/Creator account connected under **Integrations → Instagram**, and the customer must link their own Instagram username inside the widget's "Ways to Earn" section **before** the tracked action — an unlinked account can't be auto-detected.

**Product reviews / Google reviews** — check in order:
1. The review app is **Connected** under Integrations, and a **Write a review** (or Google reviews) program exists.
2. The review is actually **Published**, not still pending.
3. The customer is a **Member**, not a guest.
4. **Settings → General → Default status for Product reviews / Google Maps reviews** — if set to **Pending**, points wait for manual approval at **Customers → Activities → Review activities** (or the Google Reviews tab). This is the most common cause and is not a bug — switch to **Approved** to auto-credit future reviews.

Note: Judge.me's own "not eligible for coupon" message is a separate Judge.me Coupons feature, unrelated to Joy points — don't treat it as evidence Joy points are missing.

If all checks pass and points are still missing, escalate with `<escalate_human>`.

---

Q: A customer's birthday reward didn't fire even though their birthday was today.
Q: "Complete birthday info" reward gave 0 points when I tested it.
A: These are two separate rewards.

**"Complete birthday info"** grants points once, immediately, the first time a customer submits their birthday through the widget — unrelated to the actual birthday date.

**The birthday reward itself** needs all of these true:
1. **30-day anti-fraud rule** — the birthday must have been saved at least 30 days before the actual birthday, or the reward defers to next year (e.g. birthday = June 1 → must be saved by May 2).
2. Customer is a registered **Member**, not a Guest.
3. The date falls inside the configured **window** (Exact date, Birth month, or Around birthday for Manual claim).
4. **Claim method** matches what happened — Automatic (auto-added) vs Manual (customer must click Claim in the widget within the window).

If the 30-day rule blocked it, explain the reward will fire next year automatically — or use the **"Trigger birthday reward"** button directly on the customer's profile in Joy Admin for an immediate one-off. If all four conditions are met and it's still missing, escalate with `<escalate_human>` including customer email, birthday date, and the date the birthday was saved.

Note: customers can't edit their own birthday after first entry — only the merchant can, from the customer's profile.

---

Q: A long-time customer is still stuck on a low VIP tier even though they've spent a lot.
Q: Do points I add manually count toward a customer's VIP tier?
A: **VIP tier progress and redeemable point balance are two separate metrics.** A customer's tier is based on total lifetime points/spend/orders earned toward the tier — not their current spendable balance. A customer with 810 lifetime points and a 1,000-point threshold is still short even if they've redeemed most of their balance down to a low number.

Manually-adjusted points (via Customers → adjust points) are, by default, **excluded** from VIP tier accumulation — check the **"include in tier calculation"** option at the time of adjustment if the merchant wants a manual add to also count toward tier progress.

---

Q: I'm hitting a "transaction limit reached" message — can I get unlimited transactions?
A: A **transaction** here means any point-related activity (a customer earning points from an order, or redeeming points for a reward) — it is NOT a Shopify order or payment. This is **not gated behind a paid plan** — any merchant who asks can have it enabled, regardless of plan. Don't frame it as a pricing/upsell question or redirect to pricing.

CS cannot enable it directly in chat. Collect the store URL and escalate to the team with `<escalate_human>` — it's usually enabled at no extra cost.

---

Q: How does point expiration timing actually work? Why did a customer's points expire early?
A: Set up at **Reward programs → Point Expiration**, three modes:
- **Full inactivity** (Essential+) — the whole balance expires after N days with no earn/spend activity; any activity resets the clock for the *entire* balance.
- **Fixed date** (Essential+) — everything expires on one calendar date regardless of when earned.
- **Expiration by earning date / FIFO** (Ultimate only) — each batch expires N days after it was individually earned.

If expiration looks wrong, check which mode is active and confirm the clock is running from the customer's actual last activity, not store launch. Points earned before a mode switch keep the old logic unless the team runs a sync to reapply the new one.
