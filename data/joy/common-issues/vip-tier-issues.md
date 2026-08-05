---
category: Common Issues
topic: VIP Tier Issues
source: reports/weekly-faqs/joy + cs2 KB
---

Q: A customer reached a VIP tier but didn't get the entry reward.
Q: I added a new entry reward to a tier — will existing members in that tier get it?
A: Entry rewards fire **once**, the first time a customer reaches a tier, and are **not retroactive** — customers already in the tier when the reward is created or edited do not get it automatically, nor do customers who joined before the VIP tier program launched.

Set entry rewards at **Joy Admin → Membership → VIP Tiers → [tier] → Entry reward → Add reward** (NOT under Tier privileges — that's a separate, ongoing mechanism). Changes to a tier's threshold, calculation rule, or entry reward are **saved but stay inactive until you re-Launch** the tier program.

If a merchant wants a member who **dropped and later re-reached** the tier to get the entry reward again, that's a separate, persistent setting — not something tied to re-Launch: **Allow giving entry reward again after being downgraded** (checkbox), at **Membership → VIP Tiers → Tiers tab → Tier configuration settings → Customer management**. Leave it off by default; it only applies to customers who dropped out of the tier and re-entered it (via admin edits, tier imports, or natural demotion), not to customers newly reaching the tier for the first time.

If the reward was created before the customer reached the tier and is still missing, escalate with `<escalate_human>` including customer email, tier name, and entry-reward setup time.

---

Q: A customer is in the right VIP tier but isn't getting their ongoing perk/privilege (free shipping, discount).
Q: A tier perk works for some customers in a tier but not others.
A: **Privileges/perks are different from Entry rewards** — perks apply automatically on every qualifying order while the customer holds the tier; entry rewards fire once.

Check in order:
1. Customer is logged in to the correct account and genuinely in that tier.
2. **Discount combination** — perks are automatic discounts; if another discount is already on the cart and combination isn't enabled on the perk, it won't apply (enabling it means it will also stack with sitewide sales — confirm that's wanted).
3. **Set maximum discount amount** or **Apply discount only once per order** settings may be limiting the perk as designed.
4. Privilege perks require **Advanced or Ultimate** — confirm the merchant's plan.
5. For a Free-product perk, confirm the product is still eligible/in stock — an out-of-stock selection generates no code.

Test live logged in as a tier member through cart → checkout. If setup is correct but it's still inconsistent, escalate with two customer emails (works + doesn't-work), tier name, and a screenshot of the perk setup, `<escalate_human>`.

---

Q: Can different VIP tiers earn points at different rates?
Q: Can I set a decimal multiplier like 1.5x for a tier?
A: Yes. As a tier privilege, the **Bonus Points** perk gives whole-number multipliers only (2×, 3×, 4×) — configure at **Membership → VIP Tiers → [tier] → Tier privileges → Add perks**.

**For a fractional rate like 1.5×**, use the **Place order** earning program's **"Who to reward"** setting instead: set it to **"Only customers in a VIP tier can earn points"** — this reveals one earning-rate field per tier, and fractional values (e.g. 1.5) are accepted there. This is reached via **Reward programs → Earning programs → Place an order**; it does NOT require Shopify Flow. Requires a VIP Tier program already set up and enabled. (VIP Tiers themselves, and this per-tier rate configuration, are Advanced/Ultimate only either way.)

---

Q: All (or most) of my customers suddenly dropped to the lowest VIP tier.
Q: My customers' tiers or points look wrong after I edited VIP tiers.
A: This is almost always a **re-assessment, not lost data**. Changing a tier's threshold, changing the calculation rule (Points earned / Amount spent / Number of orders), or re-launching VIP Tier makes Joy re-evaluate every customer against the new rule — if a threshold went up, many customers can fall to the lowest tier at once.

Also check: if the metric is **Amount spent** and customer spend hasn't fully synced from Shopify, tiers can calculate on incomplete data; and whether a tier import file ran in parallel (imports can overwrite tiers). Remember **VIP tier points** (cumulative, drives tier progress) and **point balance** (what's redeemable) are separate metrics — adjusting one does not resync the other.

If the reassessment explanation doesn't account for it, or the merchant needs customers restored to prior tiers, escalate with store URL, when it happened, old vs new thresholds, and a screenshot of tier settings, `<escalate_human>`.

---

Q: What VIP tier features need which plan?
Q: Can a tier discount apply automatically at checkout with no code?
A: VIP Tiers themselves (multiple tiers, per-tier perks, different earning rates) require **Advanced or Ultimate**. **Tier Assessment** (rolling-window re-evaluation to keep/demote based on spend/orders over time) is Advanced/Ultimate **plus** requires the Joy team to enable it per-shop — it's not self-serve for every store yet. A per-tier discount CAN apply automatically at checkout with no code, configured as a Bonus Points/Discount **privilege perk** under Tier privileges (behaves like an automatic discount, can combine with point redemption via its own Combinations setting). Redeem-at-checkout with zero friction is Ultimate + Shopify Plus only. The Loyalty Dashboard/Hub block on the account page is Advanced+.

When a merchant asks for rolling-window tier maintenance: confirm their plan is Advanced+, then escalate to have Tier Assessment enabled, `<escalate_human>`.

Known limitations to communicate, not promise fixes for: no built-in quarterly-reset preset for Tier Assessment, and customers have no on-widget indicator of time-to-demotion — communicate timing via tier emails instead. Tier Assessment also does not apply to **Exclusive (manually-assigned) tiers** — those have no rolling-window renewal mechanism; a merchant wanting annual requalification for an ambassador tier must reassign manually.

---

Q: Can I manually assign a customer to a special tier (ambassador, wholesale, influencer)?
A: Yes — **Exclusive tiers** (Advanced, Ultimate), separate from the auto-progressing VIP system:
1. **Membership → New tier** → check **"Exclusive tier (Manual only)"** → set entry rewards + perks → Save.
2. **Joy Admin → Customers → [name] → Assign to exclusive tier.**

The red warning shown when assigning is expected — it means the customer's **tier qualification points** get set to that tier's entry threshold; their redeemable point balance is unaffected. Limits: one exclusive tier per customer at a time, manual assignment only (no auto progression), and members in an exclusive tier don't concurrently progress through regular VIP tiers.
