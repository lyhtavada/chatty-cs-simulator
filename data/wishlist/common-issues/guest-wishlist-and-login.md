---
category: Common Issues
topic: Guest Wishlist, Login Requirement & Account Access
source: KB (cs2.avada.net wishlist-agent) + weekly FAQ mines
---

Q: Why do my customers have to create an account or log in to use the wishlist?
Q: Can customers add items to their wishlist without logging in?
A: By default, customers must be logged in / have a Shopify account for items to be added to their wishlist and tracked — the app identifies wishlists by account.

This is configurable: go to **Settings → Configuration → "Allow guest add to wishlist"** (default OFF). Once turned ON, customers can add products to their wishlist without logging in.

---

Q: What does the "email capture" popup do, and does that count as a real customer account?
A: This is only relevant once "Allow guest add to wishlist" is ON. **Settings → Configuration → "Show email capture prompt"** (default OFF) shows a form for non-logged-in guests to leave their email, so their wishlist can be recovered later or on another device. This does NOT create a Shopify customer account — these guests will NOT appear in the Customers list until they actually sign in to a real account.

If enabled, a "When should the prompt appear?" dropdown controls timing:
- After N wishlist adds (default, "Show after this many wishlist adds" field, default 1)
- After N seconds on page
- When the user is about to leave (exit-intent)

This can be disabled in Settings if unwanted.

---

Q: A customer got a login/register error on the wishlist page after clicking "Log in" or "Create account."
A: If the store uses Shopify's **New Customer Accounts**, the Login/Create Account buttons on the Wishlist page redirect to Shopify's native registration/login page. This can fail to open correctly **inside the Theme Editor preview** (Shopify manages these pages outside theme editor control) but works normally on the live/published site — check the live site before assuming it's broken. The redirect destination itself can't be changed by the app; it's a Shopify-level setting under **Settings → Checkout**.

---

Q: Can I redirect the wishlist's login/sign-in link to a custom account page (e.g. a Kwik Pass page)?
A: Yes — **Wishlist Design → Wishlist Page → Login modal → Custom login URL**. Accepts a relative path (e.g. `/pages/kp-account`) or a full https URL. Leave empty to use the default Shopify login. This is self-serve, no theme access needed.
