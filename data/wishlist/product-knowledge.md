# Joy Wishlist — Product Knowledge Reference
# Used by the scenario generator to create realistic, product-accurate scenarios.

## What Wishlist Does
Joy Wishlist ("save for later") is a Shopify app by Avada that lets customers save products they're interested in. It:
- Captures purchase intent data and helps merchants understand customer preferences
- Tracks which saved products convert to purchases (Conversion Rate)
- Lets customers access their wishlist via a header icon, floating button, and/or a dedicated menu page
- Supports shareable wishlists via a public link
- Forwards wishlist events to Klaviyo, but only through a connected Joy Loyalty app (no standalone Klaviyo connection)

It's a smaller, simpler app than Chatty or Joy Loyalty — no plan tiers, no complex program engine. Most support requests are about getting the widget/icon/button to display correctly on a given theme, or about styling limits.

Joy Wishlist and Joy Loyalty are **separate, non-integrated apps** at the product level: a customer's wishlist doesn't surface inside the Joy Loyalty widget, and there's no way to earn loyalty points for wishlist actions. The only connection between them is the Klaviyo event-forwarding path above.

## Pricing
**Joy Wishlist is currently free.** There is no confirmed multi-tier pricing structure in the knowledge base — do not state specific plan limits or future pricing beyond "currently free." Any pricing question beyond that should be verified against the current Shopify App Store listing before answering, or escalated to CS Leader.

## Core Features

### 1. Getting Started
From the app Dashboard: (1) click **Enable**, then **Save** in the Theme Editor, then click **Refresh** to confirm the app is active; (2) customize how customers access the wishlist and how the Add-to-Wishlist button appears under **Wishlist Design**. The Dashboard shows three store-wide metrics: **Total Items Added**, **Unique Customers**, and **Conversion Rate** (Total items paid / Total items added × 100%) — there's no per-product breakdown here.

App language (**"App's language"** setting) can be set to English, French, German, Italian, Spanish, or Japanese — this changes the **admin dashboard** language only, not storefront-facing customer text.

### 2. Wishlist Access (Apps → Joy Wishlist → Wishlist Design → Wishlist Access)
The ONE fixed icon/button that opens the wishlist page (not per-product). Enable one or more:
- **Floating button** — fixed floating position on the storefront
- **Main menu page** — displays the wishlist page as a main menu item
- **Header icon** — displays in the header. Default position is **left of the profile/bag icon only** — cannot be placed to the right. Positioning is theme-dependent; multi-menu or custom-nav themes may need custom CSS/selectors from the tech team.

General settings here also control: item-count visibility ("Show/Hide number of items added"), button color (icon/background/border color), and icon type (Heart/Star/Flag/custom upload — recommended 1:1 square image under 200kb, no hard app-enforced spec).

### 3. Wishlist Button (Apps → Joy Wishlist → Wishlist Design → Wishlist Button)
The small "add to wishlist" heart icon shown on EACH product thumbnail/product page — distinct from Wishlist Access. Three separate global toggles:
- **Show on product details page** — below Add to Cart
- **Show on collection page** — on thumbnails in collection grids; requires backend setup by the team (not self-serve — has a "Contact us" link in-app)
- **Show on home page** — on home page product cards; self-serve checkbox

Each toggle is global (all products / all collection pages / all home sections) — none can be scoped to a single product or section without custom CSS/Liquid from the tech team. The button cannot be merged into the same block as Buy Now/Add to Cart (confirmed not feasible by dev).

### 4. Wishlist Page (Apps → Joy Wishlist → Wishlist Design → Wishlist Page)
Content type options: **Full page** (supports description), **Drawers** (slide-in panel), **Popup** (modal overlay) — only Full page supports Title/Description text. General settings control button text/colors shown on the wishlist page itself. A separate **Login modal** section (shown when a guest without an account tries to add to wishlist) has its own Modal title/description, Create account/Log in button text, and a **Custom login URL** field (self-serve, redirects login/sign-in links to a custom page).

### 5. Guest Wishlist & Login
By default, customers must be logged in / have a Shopify account for their wishlist to be tracked. Merchants can turn this off via **Settings → Configuration → "Allow guest add to wishlist"** (default OFF). Once on, an optional **"Show email capture prompt"** (default OFF) asks guests for their email so their wishlist can be recovered later — this does NOT create a Shopify customer account, and these guests won't appear in the Customers list until they actually sign in.

### 6. Customers & Export (Apps → Joy Wishlist → Customers)
Table tracks Name, Email, Wishlist items added, Total items paid, Revenue. Filter by "Has orders"/"No orders," search by name/email, sort by any metric. **Export CSV** gives per-product detail (title, variant, price, date added) — Variant SKU is NOT included in the export (logged as product feedback).

### 7. Settings (Apps → Joy Wishlist → Settings — separate tab from Wishlist Design)
- **Allow guest add to wishlist** / **Show email capture prompt** — see Guest Wishlist above
- **Allow share via public link** (default ON) — customers/guests can generate a public link to share their wishlist
- **Custom domain** — replace the default `.myshopify.com` domain on shared wishlist & recovery links (just the domain, no `https://`, no path)
- **Klaviyo event sync** — 4-step flow, requires a Joy Loyalty app installed and connected to Klaviyo first; no standalone Klaviyo connection exists

### 8. Translations
**Translatable:** Page title & description (Wishlist Design → Wishlist Page), and all Login modal button/title/description text (manual per-store text editing, not automatic multi-language).
**NOT translatable (hardcoded):** the empty-wishlist message, "Sign in" button, and "Share wishlist" text — a long-standing, unresolved product gap. A third-party translation app can sometimes override metafields and cause partial-translation issues.

### 9. Analytics
Dashboard totals only (Total Items Added, Unique Customers, Conversion Rate) — no per-product "most wishlisted" report exists (workaround: Customers → Export CSV). **Meta Pixel tracking IS available**: wishlist-add events publish via `shopify.analytics.publish` and can be picked up by a Custom Pixel (Shopify Admin → Settings → Customer Events → Add Custom Pixel, subscribe to `avada_wishlist:add`), no theme/collaborator access needed.

### 10. Integrations
- **Klaviyo** — only via a connected Joy Loyalty app forwarding events; no direct/standalone connection
- **Omnisend** — not available
- **Joy Loyalty** — separate apps, no product-level integration (no shared widget, no points for wishlist actions) beyond the Klaviyo forwarding path
- **Shopify Flow** — no trigger exists yet (roadmap)
- **Third-party wishlist app import** (e.g. Swym) — not available

### 11. Styling & CSS Limits
Color/icon/button-text are self-serve via General settings on the Access/Button/Page tabs. Anything beyond that (border-radius, precise spacing, font sizing, image cropping, matching another button's exact style) needs the team to apply custom CSS — collect the exact spec, **no collaborator code needed for styling requests**. **Background color fields only support solid colors, no transparent value** — setting it to white for an "outline" look makes the icon invisible instead. Custom CSS can be reverted by theme updates and may need re-applying; a CSS change to one element can sometimes have a knock-on effect on a nearby element.

Fixes that require editing the merchant's own theme (header icon positioning on custom-nav themes, scoping a toggle to one product/section, snippet placement on custom themes) DO need collaborator/Theme access.

### 12. Roadmap / Not Yet Available (do not promise dates)
Back-in-stock notifications (high internal priority, no confirmed date), price-drop notifications, multiple named/categorized wishlists, cart-abandon-to-wishlist prompt (any date given is merchant-specific, don't generalize), Shopify Flow trigger, "Notify me when available" instead of Add to Cart (explicitly declined, not feasible), lazy-loading of the widget (explicitly declined for technical reasons), third-party wishlist app import.

## Common Issues (Quick Reference)

| Issue | Root cause |
|---|---|
| Header icon not showing | App embed off, "Header icon" setting off, or (if both on) a code-level issue — often theme duplication/update not carrying the icon over |
| Header icon in wrong position | Default is left-of-profile/bag only — not a bug, a known limitation |
| Add-to-wishlist button missing on product/collection page | Setting off, block not added to that specific template (multi-template stores), or custom-theme code needing a manual snippet |
| Wishlist page blank | Page not in navigation, app embed off, or (rarer) default page template with content block hidden |
| Icon/button can't be scoped to one product/section | All display toggles are global — needs custom CSS/Liquid from the tech team |
| Background color looks wrong / icon disappears | Background color field is solid-only, no transparent option |
| Customers can't add to wishlist without an account | "Allow guest add to wishlist" is OFF by default — merchant can turn it on in Settings |
| Guest didn't appear in Customers list | Email-capture guests aren't full accounts — they only appear after actually signing in |
| Storefront text still in English | Empty-state, Sign in, and Share wishlist text are hardcoded, not translatable |
| No Klaviyo events reaching account | Requires a connected Joy Loyalty app — no standalone Klaviyo connection |
| Can't find per-product wishlist stats | No such report exists — closest workaround is Customers → Export CSV |

## Key Terms

| Term | Meaning |
|---|---|
| Wishlist Access | The one fixed header icon / floating button / menu page that opens the wishlist — not per-product |
| Wishlist Button | The per-product "add to wishlist" heart icon on product/collection/home thumbnails and product pages |
| Wishlist Page | The page where customers view their saved items (Full page / Drawers / Popup) |
| Guest wishlist | A wishlist tracked for a non-logged-in shopper via the optional email-capture flow (not a full account) |
| Conversion Rate | Total items paid / Total items added × 100%, shown on the Dashboard |
| Collaborator access | Shopify store/theme access the merchant grants so the tech team can apply theme-level fixes |

## CS Process Quick Reference

### Escalation Triggers
- Header icon / wishlist button not showing after both settings confirmed on → tech team (code-level issue)
- Any theme-level CSS/snippet fix (positioning, scoping to one section, custom style match) → escalate with collaborator access via `ref_collaborator-access`
- Complaint still unresolved after 2 attempts, legal threat, negative review threat, refund/compensation, VIP merchant → CS Leader
- Discount request → CS Leader / Sales — CS cannot approve independently
- Feature request not already covered as roadmap → log and forward to product, no promised timeline

### SLA Targets
- Complaint: < 2 hours first response, same day resolution
- Pre-sales: < 4 hours first response, same day resolution
- How-to (Regular): standard support queue
