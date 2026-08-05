---
category: Common Issues
topic: Integrations, Analytics & Data Export
source: KB (cs2.avada.net wishlist-agent) + weekly FAQ mines
---

Q: Does Joy Wishlist integrate with Klaviyo?
Q: How do I send wishlist events to Klaviyo?
A: There's no direct/standalone Klaviyo connection inside Joy Wishlist — wishlist events only reach Klaviyo through an installed, Klaviyo-connected **Joy Loyalty** app forwarding them. Setup is a 4-step flow shown on the Wishlist **Settings** page:
1. Connect Joy Loyalty (must be installed and connected to Klaviyo, with triggers enabled)
2. Pick which wishlist events to forward, inside Joy Loyalty's Klaviyo per-event list
3. Enable wishlist event sync on the Joy Loyalty side (tick at least one wishlist event)
4. Enable wishlist event sync on this Wishlist Settings page — only unlocks after steps 1–3

If the merchant completed steps elsewhere and it's still not showing, have them press "Refresh status" before assuming something's broken.

If a merchant wants Klaviyo without installing Joy Loyalty, this isn't possible today.

---

Q: Does Joy Wishlist integrate with Omnisend?
A: No — no Omnisend integration exists for Joy Wishlist today.

---

Q: Can wishlisted products show up inside the Joy Loyalty widget, or can customers earn loyalty points for wishlist actions?
A: No — beyond the Klaviyo event-forwarding path, Joy Wishlist and Joy Loyalty are separate apps with no product-level integration. A customer's wishlist doesn't surface inside the Joy Loyalty widget or vice versa, and there's no way to reward loyalty points for wishlist actions today. This is logged as a future roadmap idea, not a current capability.

---

Q: Can I track "Add to Wishlist" events for Meta/Facebook ads?
A: Yes — wishlist-add events are published via `shopify.analytics.publish` and can be picked up by a Custom Pixel:
1. **Shopify Admin → Settings → Customer Events → Add Custom Pixel**
2. Subscribe to the `avada_wishlist:add` event.

For Meta specifically, the merchant also needs a matching Custom Event ("add to wishlist") created in Meta Events Manager for it to register correctly. This is configured entirely in Shopify Admin and Meta Events Manager — no theme or collaborator access needed. If a merchant needs help, offer to set up the Custom Pixel via Theme access.

---

Q: Is there a back-in-stock or price-drop notification for wishlisted products?
A: Not yet — these are on the roadmap (back-in-stock is confirmed high internal priority) but there's no confirmed public release date. Don't promise a timeline unless the merchant already received one directly from support.

---

Q: Can I import wishlist data from another app (e.g. Swym, Wishlist Club)?
A: No import feature exists from third-party wishlist apps today. Log this as product feedback.

---

Q: Is there a Shopify Flow trigger for wishlist events?
A: Not yet — this is logged as a requested roadmap item, no Shopify Flow trigger exists today.

---

Q: How do I see which specific products a customer has wishlisted?
Q: Can I export wishlist data, and does it include Variant SKU?
A: The Customers table (**Apps → Joy Wishlist → Customers**) shows aggregate counts (items added, items paid, revenue) per customer, not individual products. Use **Export CSV** on that page for per-product detail — it includes product title, variant, price, and the date each item was added, covering customers whether or not they've purchased yet.

Variant SKU is NOT included in the export (only title/variant/price/date) — this has been requested and forwarded to the dev team. Treat as logged product feedback, not an available feature; don't promise a timeline.

---

Q: Can I see which products are wishlisted the most across my store?
A: There's currently no dedicated report for this — the Dashboard only shows store-wide totals (Total Items Added, Unique Customers, Conversion Rate). The closest workaround is Customers → Export CSV, which lists individual product entries per customer. A "most-wishlisted products" report has been requested repeatedly and forwarded to product — treat as roadmap, not available.
