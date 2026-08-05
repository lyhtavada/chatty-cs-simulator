---
category: Common Issues
topic: Widget & Loyalty Page Display Issues
source: reports/weekly-faqs/joy + cs2 KB
---

Q: The loyalty widget isn't showing on my storefront at all.
Q: My customers can't see the Joy widget button anywhere.
A: Check these four, in this order (recent cases are far more often #2 or #3 than #1):

1. **App embed off** — Shopify Admin → Online Store → Themes → Customize → **App embeds** → **Joy Loyalty - Widget** must be on → Save.
2. **"Hide widget button" enabled** — On-site content → Widget → Widget design → Setup → Advanced → Display.
3. **"Display after login" is on** — guests never see it; test while logged in first.
4. **Customer Eligibility set to "Manually assigned customers only"** — Settings → General — hides the widget from everyone not manually added.

Note the widget also can't display on Shopify's **New Customer Account "Profile" page** specifically — that's a Shopify platform limitation, not a Joy bug; it shows normally on every other storefront page after login. The "App embed Active/Inactive" status badge inside Joy admin can itself be inaccurate (a theme-sync display issue) — if points are earning normally in the activity log, treat the badge as cosmetic, don't escalate it as functional. If none of the four checks resolve it, collect the store URL and escalate, `<escalate_human>`.

---

Q: The launcher button overlaps my cart / chat / navigation button.
Q: How do I move the widget to an exact position?
A: Split the request into two kinds:

**Rough clearance** (move it away from the checkout/Add-to-Cart button) — self-serve: **On-site content → Widget → Widget design → Setup → Settings → Launcher** → Alignment (bottom-left/bottom-right), size, border radius, plus **Advanced → Display → Page restriction** to hide it on conflicting pages.

**Exact placement** ("put it exactly here," pixel offset, matching another button's size) — the built-in settings can't do this; it needs **custom CSS from the team**. Collect a screenshot/mockup of the target position, the page URL, the device (with OS if mobile-specific), and the collaborator code, then escalate, `<escalate_human>`.

If a conflicting floating button on the page **isn't Joy's**, we can't move it — check the storefront first; several cases each week turn out to belong to another app (chat widgets in particular).

---

Q: Should I be on the Classic or Unified widget? How do I check which one I have?
A: **Unified (v4)** is the current, actively-developed version; **Classic (v3)** is deprecated and no longer offered to new setups.

Check which you're on at **On-site content → Widget → Widget design** (or **Setup**): a **full sidebar** (Header/Body/Footer/Extensions/Advanced) with a live storefront preview = Unified (v4); **4 horizontal tabs** (Widget theme/Membership card/Display/Advanced) = Classic (v3).

Switch anytime with **Switch to Unified** — all existing Joy data (points, programs, customers, translations) carries over untouched, and both versions never run simultaneously. A handful of features (Milestone UI, interactive website popup, Wallet pass/QR, Submit receipt, branded reminder popup) still render in Classic style even on Unified stores. We also offer a **free setup service** to style the Unified widget or loyalty page to match the store's branding — collect the store URL and escalate if the merchant wants this, `<escalate_human>`.

---

Q: Can I customize the images/logo/banner shown in the widget?
Q: The widget shows a "Your Logo" placeholder instead of my actual logo.
A: A preset theme only sets sample images — it never locks them. To use your own images, edit each image where it lives, block by block (there's no single "images" page):

1. Open **Joy Admin → On-site content → Widget → Widget design → Setup**.
2. In the left sidebar, navigate to the block with the image (Header → Logo / Header background, or Body → Membership card → Default avatar / Guest card / Member card image, or an Image banner/Image with text custom block).
3. Click **Upload image** (or paste a URL) — the live preview updates immediately.
4. **Save.**

**"Your Logo" showing is expected, not a bug** — it's the default placeholder when no image has been uploaded at Header → Logo. The fix is simply to upload one (or click **Use store logo**).

---

Q: How do I hide the widget on specific pages, or show it only after login?
A: Both live under **Joy Admin → On-site content → Widget → Widget design → Setup → Advanced**, on two different tabs, and are available on **every plan including Starter (free)**:

- **Advanced → Display**: "Hide widget from guests" (only logged-in customers see it), "Hide widget button" (turn off to always show it).
- **Advanced → Popup**: "Page restriction" ("Show on specific pages") — off by default (shows everywhere); toggle on, then check Home/Product/Collection/Cart/Blog/Custom pages.

Common mistake: "Show on specific pages" is under **Popup**, not Display. Custom page restriction beyond the standard page types requires backend configuration — escalate with the specific page URL(s), `<escalate_human>`.

---

Q: My cart drawer shows a Redeem button and "0 points" to logged-out guests.
A: This is a known display gap with the cart-drawer redeem block (**Joy: Redeem in line**) — it doesn't consistently hide itself from guests. Confirm the shopper genuinely isn't logged in (rule out an SSO/session timing issue first). If the redeem block is still showing to a confirmed guest, collect the store URL and theme, and escalate for the team to check, `<escalate_human>`.

---

Q: How do I customize the loyalty page — text, colors, images, layout?
Q: Can your team set up or style my loyalty page?
A: Build/edit at **Shopify Admin → Online Store → Themes → Customize → [Joy Loyalty page template]**. Add, remove, or reorder blocks from the left panel under **Add section/block → Apps**: Joy Hero Banner, Joy: How it works, Joy: Ways to earn, Joy: Ways to redeem, Joy: Rewards activity, Joy: Referral block, Joy: VIP Tier benefits, Joy: Sign-up banner, Joy: Loyalty Program FAQs, Joy: My rewards (Advanced/Ultimate only). Block order on the page is controlled in Theme Editor; the order of programs *within* Ways to earn/redeem is controlled in **Joy Admin → Reward programs**.

If the merchant wants the team to build/style it directly rather than doing it themselves: ask permission for store access, collect the collaborator code, and escalate with the request details, `<escalate_human>`. This is a free service on any plan; the team sends a preview before anything goes live.

---

Q: My loyalty page is blank / not showing anything.
A: Walk through this checklist:
1. **App embed** — Shopify Admin → Online Store → Themes → Customize → App Embeds → confirm **Joy Loyalty - Widget** is enabled → Save.
2. **Page template** — in Theme Editor, confirm the loyalty page uses the **Joy Loyalty** template, not a generic page template.
3. **Blocks** — confirm Joy blocks (Ways to earn, Ways to redeem, etc.) were actually added under the Apps section in Theme Editor.

Ask the merchant to hard-refresh (Cmd/Ctrl+Shift+R) after checking. If still blank, collect the store URL, the loyalty page URL, and what's already been checked, then escalate, `<escalate_human>`.

Related cause: if the eligibility setting is **"Manually assigned customers only"** (Settings → General), guests and unassigned members won't see the blocks/widget at all — switch to "All customers" if that's not intended.

---

Q: The Sign in / Sign up button on my loyalty page doesn't redirect anywhere / looks broken.
A: The Sign in/Sign up buttons are generic button blocks that need a destination URL set by the merchant, pointing to Shopify's account pages. In the Loyalty Page editor, set the button block's link:
- **Sign In:** `/account`
- **Sign Up:** `/account` for **New Customer Accounts** (the default for most stores — one page handles both sign in and register), or `/account/register` **only** for Legacy (Classic) accounts.

Tell the merchant to test on the **live storefront**, not in Theme Editor preview mode — preview mode won't redirect, which often makes a working button look broken.

---

Q: I clicked "Edit in theme editor" and got a 422 "page already exists" error.
A: The app auto-creates a loyalty page in **Online Store → Pages** the first time it's opened. If the page already exists from a previous click, re-creating it fails with a 422. Explain that the page was already created — guide the merchant to find it at **Online Store → Pages** (look for a page named "Loyalty" or similar) and continue customizing that existing page rather than trying to create a new one.

---

Q: My theme is OS 1.0 and Joy's blocks aren't showing / app blocks are blocked.
A: OS 1.0 themes don't fully support app blocks; Shopify recommends OS 2.0 for modern app integrations like Joy's. If the merchant is on OS 1.0 and wants to upgrade: explain the process — the team duplicates the current theme, upgrades the duplicate to OS 2.0, and the live theme is never modified during the process; nothing publishes without the merchant's confirmation. If they agree, request theme access and escalate for the team to perform the migration, `<escalate_human>`.
