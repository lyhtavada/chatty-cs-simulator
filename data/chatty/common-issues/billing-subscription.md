---
category: Common Issues
topic: Billing & Subscription Issues
source: notion/Chatty FAQs
---

Q: A merchant is requesting a refund or wants to cancel their subscription.
Q: How do I handle billing and refund requests?
A: Follow this process:

**Step 1: Understand the reason** (use shortcut `!cancel-reason`)
- Why does the merchant want to cancel/refund?

**Step 2: If the issue is bugs or unmet expectations**
- Identify what the merchant expected from the app.
- Proactively offer to fix the issue, re-guide setup, or test the feature.
- If resolved, encourage continued use. Consult CSL about offering a discount for the next month.
- Follow up to ensure the problem is fully resolved before processing any refund.

**Step 3: If the merchant still wants to cancel/refund**
- Apologize and collect billing details using shortcut `!billing-details` (screenshot of invoice with app name, billing cycle, amount).
- Confirm whether the invoice has been paid.
- Guide the merchant to downgrade to Free plan to prevent further charges.

**Step 4: Create escalation card**
- Assign to CSL with full details using shortcut `!refund-process`.

**CRITICAL: CS must NEVER approve any refund without CSL approval. Unauthorized approvals make the CS agent personally liable.**

---

Q: The merchant cancelled their subscription but still sees charges.
Q: Why was the merchant charged after cancelling?
A: Shopify automatically charges when a subscription begins, even if cancelled afterward. The charge covers the billing period the merchant used before cancelling.

**Support flow:**
1. Verify the exact cancellation date and billing status.
2. Determine if the charge belongs to the current or previous billing period.
3. Explain the Shopify billing cycle to the merchant.
4. If the merchant did not use the app after being charged, create a refund request and assign to Billing/CSL.
5. Guide the merchant on proper cancellation timing to avoid future charges.

---

Q: A merchant is asking for a discount to upgrade to a paid plan.
Q: How do I handle discount requests for plan upgrades?
A: **CS must NEVER independently offer discounts.** All offers require Sales team or CSL approval.

**Process:**
1. Confirm which plan the merchant is interested in.
2. Offer a demo call with PM using shortcut `!chatty-demo-call`.
3. If the merchant doesn't book a call, escalate to `#sales-cs-success` Slack channel tagging @TungQT with: store name, current plan, desired plan, reason for discount, desired discount level, recent support history.
4. If approved: send the offer and guide the upgrade process.
5. If not approved: politely explain, emphasize app value, suggest continuing with the free trial.

---

Q: What is the LinkedIn 40% discount promotion?
Q: A merchant is asking about a discount for following Chatty on LinkedIn.
A: CS must never independently offer or confirm a discount — all discount promotions require Sales team or CSL approval.

- If the merchant references a promotional banner or offer, don't confirm eligibility or a discount code yourself.
- Collect the details (which promotion, what the merchant was shown) and check internally with the team before promising anything.

---

Q: How do I enable legacy plans for a merchant?
Q: Merchant needs access to old pricing plans.
A: This is not self-serve for CS. Collect the merchant's current plan and when they installed the app, then escalate to CS Leader — do not attempt to enable legacy plans directly.
