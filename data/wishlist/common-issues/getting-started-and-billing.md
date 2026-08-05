---
category: Common Issues
topic: Getting Started, Setup & Billing
source: KB (cs2.avada.net wishlist-agent) + weekly FAQ mines
---

Q: How do I get started with Joy Wishlist?
Q: What does Joy Wishlist do?
A: Joy Wishlist lets customers save products they're interested in for later — it captures purchase intent data and tracks which saved products convert to purchases.

Setup (2 quickstart steps) from the Dashboard:
1. **Enable App** — click Enable, then Save in Theme Editor, then click Refresh to confirm it's active.
2. **Customize wishlist appearance** — set up how customers access their wishlist (header icon / floating button / menu page) and how the wishlist button behaves under **Wishlist Design**.

---

Q: Is Joy Wishlist free?
Q: How much does the app cost?
A: Joy Wishlist is currently free. Do not state specific plan limits or future pricing beyond this — verify against the current Shopify App Store listing before quoting anything further, or escalate a specific pricing question to CS Leader.

---

Q: My wishlist page is completely blank.
A: A blank Wishlist page is almost always one of these:
1. The page hasn't been added to store navigation — **Shopify Admin → Content → Menus → Main menu → Add menu item → select the "My wishlist" page the app generated → Save.**
2. The app embed isn't enabled — **Online Store → Themes → Customize → App embeds → turn ON Joy Wishlist**, then Save.
3. (Rarer, but confirmed) the page is using the default page template with its content block hidden — go to **Online Store → Themes → Customize → switch the top dropdown to Pages → select the wishlist page → assign it a dedicated template (e.g. "wishlist-page") → make sure the page content block inside that template isn't toggled hidden.** If a dedicated template already exists, check block visibility first before assuming it's a navigation or embed issue.

Also confirm the merchant is previewing the correct theme (draft vs. live) — a frequent mix-up.

---

Q: What do the Dashboard metrics mean?
A: The Dashboard shows three store-wide metrics:
- **Total Items Added** — products added to all customer wishlists
- **Unique Customers** — different customers who added products
- **Conversion Rate** — Total items paid / Total items added × 100%
There's no per-product breakdown here.

---

Q: I changed the app language but the storefront is still in English.
A: The "App's language" setting (English, French, German, Italian, Spanish, Japanese) only changes the admin dashboard language — not storefront-facing customer text. For what customer-facing text is or isn't translatable, see the translations topic.

---

Q: I switched the Wishlist Page display type (e.g. Full page to Drawers) but nothing changed on the storefront.
A: The setting itself very likely applied correctly server-side — this is usually a browser/CDN cache issue, not a saving failure. Ask the merchant to hard-refresh or clear their cache and check again before escalating.

---

Q: How do I add the wishlist page to my main menu, or change its label?
A: Go to **Shopify Admin → Content → Menus → Main menu → Add menu item → select the "My wishlist" page → Save.** To rename the label, edit it directly on the same Menus screen. There's no self-serve setting to move the page to a custom URL/page — the tech team can assign a custom template via CSS on request.
