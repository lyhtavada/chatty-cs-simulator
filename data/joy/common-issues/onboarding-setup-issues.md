---
category: Common Issues
topic: Onboarding, Setup & Migration
source: reports/weekly-faqs/joy + cs2 KB
---

Q: How do I set up Joy from scratch?
Q: How do I get started / launch my loyalty program?
A: Start at **Joy Admin → Reward programs**: create a **Place order** earning rule (points or store credit per $ spent), then a **Redeeming program** (discount, free gift, or free shipping). Build the storefront presence: add the **Joy Loyalty** loyalty page template at **Online Store → Themes → Customize** (Essential+ for the dedicated page; free-plan merchants can use the `#joy-home` widget deeplink instead), then enable the widget embed at **Theme Editor → App embeds → Joy Loyalty - Widget → Save**.

For a fuller build (VIP Tiers, Referral, Birthday rewards — Essential+ or above depending on the piece), configure each program, then test with **Sandbox Mode** before going live. Offer a pre-launch review, or (for larger programs) our team can build directly from a filled-in template sheet.

---

Q: Can your team set up or style my widget / loyalty page for free?
A: Yes — this is a free design/setup service on any plan. Have the merchant share a reference design or their brand colors/fonts, and if they want the team to configure it directly (not just advise), collect **collaborator access** via their 4-digit code (**Shopify Admin → Settings → Users → Security → Collaborator request code**). The team styles the widget and/or loyalty page and sends a preview before anything goes live on the storefront — nothing changes until the merchant approves. This also covers migrating from Classic to the Unified widget with a fresh restyle included. Don't promise a specific turnaround time — let the merchant know the team will follow up once they've reviewed the request. Escalate with `<escalate_human>` once details are collected.

---

Q: How do I test my program before launching (Sandbox Mode)?
A: Turn on **Sandbox mode** at **Reward programs → Sandbox Mode**, then click **Test list** and add test email(s) — only those accounts earn points while sandbox is active. Sign in on the storefront with a test account and run through signing up, placing an order, and redeeming, then verify the points landed under **Joy Admin → Customers**.

Two things that catch people out: the Joy embed widget must be active (an account earning nothing while logged in is usually a disabled embed, not a sandbox issue), and an email not on the test list earns nothing even though the customer is real. The sign-up reward also won't fire for an account that already existed before the program started — use a genuinely new test email.

---

Q: Can I migrate or import data from another loyalty app (Smile.io, Rivo, LoyaltyLion, etc.)?
A: Full migration is available on **Essential, Advanced and Ultimate**, bringing over customer name, email, phone, VIP tier name, birth date, member status, and point balance. There are dedicated guides for Smile.io, Rivo, Yotpo Loyalty, LoyaltyLion, Stamped Loyalty, Bon Loyalty, and Appstle; anything else (Marsello, Smartrr, Growave, custom platforms) uses the generic CSV route — the CSV only strictly requires a Point column, since identity and name sync from Shopify directly.

Two paths: **Import** (self-serve, no enabling needed) at **Customers → Import** — covers point balance and birthday only, on any plan. **Migrate** (assisted, full data set) — the tool at **Settings → Migration** is locked until the team enables it; ask which app the merchant is moving from and what data they need, then escalate, `<escalate_human>`. Coupon codes issued by the old platform are **not** imported as Joy coupons, and detailed order-level activity history doesn't migrate either. After any import, remember to re-**Launch** the relevant program to trigger recalculation of points and Amount Spent.

---

Q: Can I test my setup before making it public? Will enabling the widget affect my existing content?
Q: How do I preview the app on my live store without emailing customers?
A: Use **Sandbox mode** (see above) to test the full flow with only test-list emails earning, and enable the Joy app embed on a duplicate/draft theme to try the widget without touching the live store — use Shopify's Preview to test without affecting live customers. Enabling the embed on the live theme doesn't touch other page content; it only adds the Joy widget.

---

Q: How do I brand my point currency / rename "Points"?
A: **Joy Admin → Settings → General → Custom point label** — rename "Points" to match the store's brand (e.g. "Beans," "Glow Coins," "Story Points"). This is available regardless of plan.

---

Q: What earning rate should I set / how do I decide my program structure?
A: General guidance from the Joy playbook: a **sweet-spot** earning rate is 4-5% return (e.g. 100 points = $1, 2 points per $1 = 2% return — adjust up for a stronger incentive). Recommended starter setup: sign-up reward of ~100 points, 1 point per $1 spent, redemption at 100 points = $5 off (or similar), plus Free shipping/Free gift redemptions for variety, and a referral program ("Give $10, Get $10"). Loyalty also requires **Shopify Admin → Settings → Customer accounts** to be enabled (Legacy, New, or Shop app login) — this isn't optional.

---

Q: My import failed with "Non-existent customers" or orders imported at 0 points.
A: This usually means the CSV's identity column (email/phone/ID) didn't match an existing Shopify customer, or the Point column wasn't formatted as Joy expects. Ask the merchant to confirm the customer records exist in Shopify first (Joy doesn't create new Shopify customers from an import), check the CSV headers match Joy's expected format, and re-attempt. If it still fails after a clean re-check, collect the store URL and the CSV, and escalate, `<escalate_human>`.
