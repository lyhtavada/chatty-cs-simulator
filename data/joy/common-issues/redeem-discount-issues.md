---
category: Common Issues
topic: Redemption & Discount Code Issues
source: reports/weekly-faqs/joy + cs2 KB
---

Q: A customer redeemed points but their discount disappeared / never applied.
Q: How do customers actually redeem their points?
A: The main path is the widget or loyalty page: customer logs in, opens **Redeem points**, picks a reward, clicks **Redeem** — Joy generates a one-time code. They then either click **Apply** to push the code to cart, or copy it and paste it at checkout manually.

**The code does not apply itself at checkout.** This is the single most common "my discount disappeared" report — points were spent, the code is valid, but nobody entered it. Unused codes are always retrievable from the widget's **My coupons** section. If a customer clicked Apply while their cart was empty, the discount is held and takes effect once items are added (a page refresh may be needed).

---

Q: My Joy discount code won't combine with another discount at checkout.
Q: The redeemed code isn't working / is rejected at checkout.
A: Check in this order:

1. **Combinations setting** on the redeeming program (Product/Order/Shipping classes) — Joy coupons don't stack by default, and this setting only affects **newly issued** codes, not codes already in customers' hands.
2. **Shopify's own combination rules** apply regardless of your setting: Product+Shipping and Order+Shipping always combine; Product+Product only on different line items (same-item stacking needs Shopify Plus); Product+Order or Order+Order need eligible-merchant status; **Shipping+Shipping never combines**. If the pair is in a never-combinable case, this isn't a Joy config issue — don't tell the merchant to "just enable combinations."
3. **The code's own conditions** — minimum order value, eligible products/collections, sales channel, expiry.
4. **The discount is bigger than the cart** — a fixed-amount reward larger than cart total can zero it out and error on some third-party checkout apps.

A workaround for two conflicting **Order**-class discounts: add a product/collection condition to the redeeming program (e.g. restrict to "all products") to make Joy generate a **Product**-class coupon instead — this is a configuration technique, not a bug fix, so test the result. Note: **Shopify's native store credit** has no Combinations setting at all (it's an account balance, not a discount code) and can't be blocked from stacking through Joy.

If everything checks out and it still fails, escalate with `<escalate_human>`.

---

Q: Can I edit a coupon after it's issued, or deactivate one without refunding the points?
Q: A customer's coupon is about to expire — can I extend it?
A: Once a coupon is generated, its **expiry and conditions can't be edited**. If a customer's code is expiring or expired, issue a replacement instead — revoke and let them re-redeem, or create a code directly in Shopify Admin → Discounts. Expired coupons are automatically hidden from the widget.

**To deactivate a code but keep the points spent** (i.e. no refund): don't use Joy's **Revoke** button — that always converts the coupon back into points by design, with no toggle to disable it. Instead, deactivate the code directly in **Shopify Admin → Discounts**. Note the coupon's status inside Joy may not auto-update to Expired afterward — flag to the team if the merchant needs it synced.

There's no bulk-deactivate for many/all coupons at once — escalate with the store URL and the list/criteria for a batch job, `<escalate_human>`.

---

Q: Can I set a minimum order requirement or multiple tiered redemption levels?
Q: Does a redeemed discount scale with the number of items in the cart?
A: Yes to minimum order — each redeeming program has its own **Minimum order requirement** field (Reward programs → Redeeming programs → [program] → Settings).

For **tiered redemption** (e.g. "100pts = $3 off," "500pts = $18 off"), create multiple separate **Fixed Discount** redeem rules, each at its own point cost. To cap value on a **Dynamic Discount** program, use its **Maximum discount % of cart total** field; a true fixed dollar cap requires switching to **Fixed Discount** mode.

**A redeemed reward is an order-level discount, applied once per order regardless of item quantity** — a cart with 2+ units of a product sees the same discount amount as with 1 unit. This is expected behavior, not a bug; there's no per-unit multiplication or cap.

---

Q: Why doesn't my product show up when I try to pick a free-gift reward?
Q: I hit a "too many products/variants" error setting up a discount program even though I selected fewer than 100 products.
A: **Only products published to the Online Store sales channel** sync to Joy's reward picker — Draft products, or ones removed from the Online Store channel, won't be selectable. The product must stay **Active** to be referenced (you can still hide its Buy button to keep it unbrowsable, or gate it via a VIP tier's Exclusive products/collections perk).

**The "too many products/variants" error actually counts variants, not products** — a handful of multi-variant products can add up to 100+ variants quickly. This is a hard cap from **Shopify's own Discount API**, not a Joy setting, and can't be raised. Workaround: group the products into a Shopify **Collection** and select the collection instead.

---

Q: Can used, one-time discount codes be auto-deleted or auto-expired from the Shopify discounts list?
A: No — Joy doesn't currently auto-expire or auto-delete a one-time-use code from Shopify's discounts list once it hits its usage limit, and this isn't on the near-term roadmap. Two workarounds: filter Shopify Admin → Discounts by **"Eligibility is not specific customer"** (Joy-issued codes are always customer-specific, so this filter hides them), or search by the redeeming program's custom code prefix and bulk-delete manually. Note this is different from a redeeming program's own **expiration** setting, which deactivates a coupon after a set duration but doesn't remove it from the Shopify list.

---

Q: A customer redeemed the same discount code twice / more than expected.
A: Each redeeming program's **Redemption limit** card has a per-customer cap (**Each customer's limit**) — if left blank, nothing stops repeat generation and use of the same coupon type. Set that field to prevent repeats going forward. For a code already used more than intended, deactivate it directly in Shopify Admin → Discounts (not Joy's Revoke, which refunds points).

---

Q: A reward redeemed from the cart drawer got cancelled or won't apply.
A: This is a known limitation specific to the **Redeem block inside the Cart Drawer** — a reward redeemed from there can get revoked or fail to apply correctly. If a merchant hits this, have the customer redeem the same reward from the **widget** or **loyalty page** instead, which don't have this issue. Flag to the team if it's affecting checkouts regularly.
