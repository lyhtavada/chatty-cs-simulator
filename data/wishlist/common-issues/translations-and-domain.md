---
category: Common Issues
topic: Translations & Custom Domain
source: KB (cs2.avada.net wishlist-agent) + weekly FAQ mines
---

Q: Can I translate the wishlist page text into another language?
Q: The empty wishlist message or "Sign in" button still shows in English on my non-English store.
A: Be precise about what is and isn't translatable:

**Translatable (self-serve):**
- Page title & description on the Wishlist page — **Wishlist Design → Wishlist Page**, edit the text directly.
- Login modal text — Modal title, Modal description, Create account button text, Log in button text — **Wishlist Design → Wishlist Page → Login modal**. This is manual per-store text editing (one value at a time), not automatic multi-language translation.

**NOT translatable (hardcoded in the widget):**
- The empty-wishlist message ("Your wishlist is empty," "Continue shopping")
- The "Sign in" button
- The "Share wishlist" text

This has been a repeated, unresolved request — log it as product feedback rather than promising a date/ETA.

If a translation app is installed, note it can sometimes override metafields and cause unexpected partial-translation behavior — worth checking before assuming it's an app bug, though the hardcoded strings above stay untranslatable regardless.

---

Q: Does the "App's language" setting translate the storefront for customers?
A: No — the app's language setting (English, French, German, Italian, Spanish, Japanese) only changes the **admin dashboard** language for the merchant, not any storefront-facing customer text.

---

Q: Can the shared wishlist link use my own custom domain instead of myshopify.com?
A: Yes — **Settings → Custom domain**. Enter just the domain (e.g. `shop.com`, no `https://`, no trailing path) to replace the default `.myshopify.com` domain on shared wishlist & recovery links. Leave blank to keep the default.
