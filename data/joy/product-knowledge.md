# Joy Loyalty — Product Knowledge Reference
# Used by the scenario generator to create realistic, product-accurate scenarios.

## What Joy Does
Joy: Loyalty Program & Rewards is a Shopify loyalty and rewards app by Avada. It helps merchants:
- Reward customers with points for purchases and other actions (reviews, social follows, referrals, birthdays, and more)
- Let customers redeem points for discounts, free gifts, free shipping, or store credit
- Build VIP/tiered membership programs with per-tier perks and entry rewards
- Run a referral ("give X, get X") program
- Display a branded loyalty widget and dedicated loyalty page on the storefront

It's sometimes confused with unrelated apps by name similarity (e.g. an invoice app or a review app) — those are different products. If a merchant describes a non-loyalty core job (printing invoices, collecting reviews as the primary function), confirm they're in the right app via Shopify Admin → Apps.

## Plans

Pricing model: **base monthly fee + free order quota + per-100 overage**. "Orders" (the quota) is different from "transactions" (any point earn/redeem activity) — transaction limits are not plan-gated; any merchant can request unlimited transactions via escalation, at no cost, regardless of plan.

| | Starter (Free) | Essential ($29/mo) | Advanced ($129/mo) | Ultimate ($499/mo) |
|---|---|---|---|---|
| Free orders/month | 250 | 500 | 2,000 | 7,000 |
| Overage | n/a | $15/100 | $10/100 | $5/100 |
| Free trial | forever free, no trial | 14 days | 14 days | 30 days |
| Referrals | 30 | 100 | Unlimited | Unlimited |
| Points expiration | ✗ | ✓ | ✓ | ✓ |
| Dedicated loyalty page | ✗ | ✓ | ✓ | ✓ |
| Multi-language | ✗ | Basic | Auto-translate | Auto-translate |
| Analytics | ✗ | ✓ | ✓ | ✓ |
| Shopify POS | ✗ | Earn-only display | ✓ Redemption | ✓ Redemption |
| VIP Tiers | ✗ | ✗ | ✓ | ✓ |
| Rule Engine (multiple earning rules, decimal multipliers) | ✗ | ✗ | ✓ | ✓ |
| Milestones | ✗ | ✗ | ✓ | ✓ |
| Loyalty Hub (account page) | ✗ | ✗ | ✓ | ✓ |
| B2B partner tiers | ✗ | ✗ | ✓ | ✓ |
| Cart drawer redemption | ✗ | ✗ | ✓ | ✓ |
| Checkout-page redemption / coupon list at checkout | ✗ | ✗ | via sales contact | ✓ (Shopify Plus + Checkout Extensibility) |
| API / Webhooks | ✗ | ✗ | ✗ | ✓ |
| Hydrogen / headless | ✗ | ✗ | ✗ | ✓ |
| Migration (assisted, full data) | ✗ | ✓ | ✓ | ✓ (white-glove) |
| Dedicated AM | ✗ | ✗ | ✓ | ✓ |
| Priority support | ✗ | ✗ | ✗ | ✓ |

**Every plan, including free Starter, tracks point earning/holding/redeeming** — the plan changes order quota and which advanced features unlock, not whether points work at all.

Billing is **monthly only** (no annual option) on a recurring 30-day cycle, because usage fees are calculated dynamically each cycle. Upgrades take effect immediately; downgrades take effect next billing cycle (data stays intact, higher-plan features become unavailable). After upgrading, there's a **30-day refund policy** if the merchant isn't satisfied. Free trial is one-time only per store — reinstalling doesn't grant a new one. Enterprise (5,000+ orders/mo) and agency/partner pricing available via sales contact.

**"Pro" is the legacy name for Essential** — older material or an internal `joy_plan` id like `pro`/`pro_2`/`pro_3_*` refers to what's now called Essential; never show the raw internal plan id to a merchant.

## Core Features

### 1. Earning Programs
Configured at **Joy Admin → Reward programs → Earning programs**. Programs include: Place order (points/store credit per $ spent, per item, or per order — the core program on every plan), Place subscription, Sign up, Sign up newsletters, Birthday reward (Essential+), Member anniversary (Advanced+), Write a review (connects to Klaviyo, Air Reviews, Judge.me, Loox, Okendo, Reviews.io, Stamped, Fera, Yotpo, Growave), Social activity + Instagram-specific actions (Advanced/Ultimate), Google reviews, Fill out a survey (via Shopify Flow), Visit website, Streak bonus, Custom program (Advanced+), Submit receipt (Advanced+), Submit form (Advanced+).

The **Sign up reward** is not granted just from leaving an email — it fires only when the customer logs in with the Joy widget embed active, joins via the widget popup, or is identified as a member at POS.

VIP tiers can carry their own earning-rate multiplier (whole numbers via Tier privileges; decimals via Rule Engine).

### 2. Redeeming Programs
Configured at **Joy Admin → Reward programs → Redeeming programs**. Types: Discount (amount, %, BXGY) on all plans; Free gift and Free shipping (Essential+); Coupon list at checkout and Redeem at checkout page (Ultimate + Shopify Plus + Checkout Extensibility, Advanced via sales contact). Redemption happens mainly through the widget/loyalty page (customer picks a reward → gets a one-time coupon → Apply pushes it to cart, or copy/paste at checkout). The code does **not** apply itself — this is the single most common "discount disappeared" report.

### 3. VIP Tiers (Advanced, Ultimate)
Configured at **Joy Admin → Membership → VIP Tiers**. Calculation rules: Points earned, Amount spent, or Number of orders. Each tier has a one-time **Entry reward** and ongoing **Privileges/perks** (different mechanisms — entry rewards don't retroactively apply to existing tier members). **Tier Assessment** (rolling-window re-evaluation to maintain/demote) is Advanced/Ultimate plus needs Joy support to enable per-shop. **Exclusive tiers** are manually assigned (ambassadors, wholesale) and don't auto-progress or get Tier Assessment.

### 4. Referral Program
Configured at **Joy Admin → Reward programs → Referrals**. Basic features on all plans; advanced customer/order tagging on Essential+. Flow: referrer shares link → referee clicks, lands on referral page, enters email → 7-day cookie stored → referee's reward issues immediately at claim; referrer's reward issues once the referee's order reaches the shop's earn-status trigger (Paid by default, or Fulfilled).

### 5. Widget & On-site Content
Configured at **Joy Admin → On-site content → Widget**. Two versions: **Classic (v3)** — 4 horizontal tabs, points/rewards focused, being phased out; **Unified (v4)** — full sidebar editor (Settings/Header/Body/Footer/Extensions/Advanced) with live preview, all-in-one (profile, orders, points, rewards, wishlist). Switching Classic → Unified carries all data over. Enable on storefront via **Theme Editor → App embeds → Joy Loyalty - Widget → Save**.

### 6. Loyalty Page
A dedicated landing page (Essential+) built in **Online Store → Themes → Customize**, using drag-and-drop Joy blocks: Hero Banner, How it works, Ways to earn, Ways to redeem, Rewards activity, Referral block, VIP Tier benefits, Sign-up banner, FAQs, My rewards.

### 7. Analytics & Data Export (Essential+)
Program performance stats. Customer/points export is **CSV only**; the Export button on the Customers page must be enabled by the Joy team on request.

### 8. Integrations
Klaviyo and Omnisend (profile properties: points balance, VIP tier, member status, referral link, birthday), Shopify Flow (custom triggers/actions incl. store credit), Shopify POS (Essential = earn-only display, Advanced/Ultimate = full redemption), review apps (see Write a review), Shopify Metafields sync.

### 9. Migration
Available Essential+. **Import** (self-serve, Customers → Import) covers point balance and birthday on any plan. **Migrate** (assisted, full data set incl. VIP tier, member status) is locked until the Joy team enables it — dedicated guides exist for Smile.io, Rivo, Yotpo Loyalty, LoyaltyLion, Stamped Loyalty, Bon Loyalty, Appstle; anything else uses a generic CSV. Old-platform coupon codes are never imported as Joy coupons.

## Common Issues (Quick Reference)

| Issue | Root cause |
|---|---|
| Order didn't earn points | Order hasn't reached reward trigger status (Paid/Fulfilled), guest not member, Sandbox mode, program conditions/exclusions don't match |
| Sign-up bonus not awarded | Being a "Member" (Shopify SSO) ≠ earning the reward — needs actual login with widget active, widget-popup join, or POS; also account created before program start date |
| Widget not showing on storefront | App embed off, "Hide widget button," "Display after login," or Manually-assigned-customers-only eligibility |
| Widget launcher overlaps another element | Built-in Alignment settings for rough clearance; pixel-precise placement needs custom CSS from the team |
| Discount code doesn't apply / doesn't combine | Code isn't self-applying (must click Apply or paste), or Combinations toggle off, or Shopify's own combination rules block that discount-class pair |
| VIP tier entry reward missing | Entry rewards are one-time and non-retroactive; tier wasn't re-Launched after editing |
| Referrer didn't get rewarded | Different emails at claim vs checkout, cookie expired (>7 days, unless order email still matches), order not yet Paid/Fulfilled, anti-cheat block, $0 order |
| Translation not showing / reverted | Default language not set, or a third-party translation app (Translate & Adapt) overriding Joy's fields |
| Billing shows extra usage fee | Order count exceeded the plan's free quota — usage fee is calculated on every order regardless of channel |
| Can't find Export button | Full customer export must be enabled by the Joy team first |

## Key Terms

| Term | Meaning |
|---|---|
| Member | Customer registered/recognized by Joy as a loyalty participant (not the same as a Shopify "Enabled" account) |
| Guest | A shopper who hasn't become a Member — most earning rules exclude guests |
| Transaction | Any point-related activity (an earn or a redeem) — not the same as a Shopify order |
| Sandbox mode | Test mode where only listed test emails earn points; used to try a program before going live |
| Place order rule | The core earning rule tied to purchases |
| Redeeming program | A configured way for points to become a reward (discount, free gift, free shipping) |
| Entry reward | One-time reward when a customer first reaches a VIP tier |
| Privilege / perk | Ongoing benefit applied automatically every qualifying order while in a tier |
| Tier Assessment | Rolling-window re-evaluation that can demote a customer from a tier |
| Unified widget (v4) | Current, actively developed widget version with full sidebar editor |
| Classic widget (v3) | Older widget version being phased out |
| Rule Engine | Advanced+ feature enabling multiple/stacked earning rules and decimal multipliers |

## CS Process Quick Reference

### Escalation Triggers
- Technical bug after CS troubleshooting → TS team
- Refund request → CS Leader (NEVER approve without CSL approval)
- Discount / trial extension / plan feature request → Sales / CSL (CS cannot approve independently)
- Angry merchant after 2 attempts → CS Leader
- Critical bug (data loss, app down) → PM + TS Leader immediately
- VIP merchant → CS Leader FYI immediately
- Privacy/GDPR complaint (e.g. unwanted emails) → escalate immediately as high priority, not routine

### SLA Targets
- P0 Critical: < 1 hour first response, 4-24 hours resolution
- Complaint: < 2 hours first response, same day resolution
- Pre-sales: < 4 hours first response, same day resolution
- How-to (Regular): < 24 hours first response, < 48 hours resolution
- Refund: < 2 hours first response, < 24 hours resolution
