---
category: Common Issues
topic: Widget Display Issues (Header Icon, Floating Button, Wishlist Button)
source: KB (cs2.avada.net wishlist-agent) + weekly FAQ mines
---

Q: The wishlist icon isn't showing in the header even though I enabled it.
Q: I turned on the header icon setting but nothing appears on my store.
A: Check two things in order:

**Step 1: App embed enabled?**
- Go to **Online Store → Themes → Customize → App embeds** and confirm Joy Wishlist is toggled ON, then Save.

**Step 2: Header icon setting enabled?**
- Go to **Apps → Joy Wishlist → Wishlist Design → Wishlist Access** and confirm "Header icon" is toggled ON.

If either was off, turn it on and ask the merchant to hard refresh or check in incognito.

**If both are already on and it still doesn't show:** this is a code-level issue, not a settings issue. Collect the store's theme name(s) and escalate to the tech team — do not keep repeating the same toggle instructions.

**Common trigger:** merchant duplicated or majorly updated their theme (e.g. "Actions → Duplicate," a redesign). A manually-added/customized icon on the old theme does not automatically carry over to the new theme copy, even with app embed and Header icon both already enabled on the new theme — the customization lives in the old theme's code, not in app settings. Ask which theme is affected (old vs. new) and escalate for the tech team to add it to the new theme's code.

---

Q: Can I move the header wishlist icon to the right side of the logo/cart icon?
Q: I want the header icon positioned differently than where it currently shows.
A: By default, the header icon can only sit **left of the profile/bag icon** — there's no setting to place it on the right or elsewhere. This is a known limitation, not a bug. Positioning is also theme-dependent — multi-menu or custom-nav themes may need the tech team to add custom CSS/selectors (requires Theme access).

---

Q: The Add to Wishlist button isn't showing on my product page.
Q: The wishlist button works on some products but not others.
A: Ask which page (product/collection/home) and whether it's missing everywhere on that page type or only on specific products — multiple product templates is the #1 cause of "button disappeared on this one product page" tickets.

Check:
1. Is **Wishlist Design → Wishlist Button → Show on [product details / collection / home] page** turned ON?
2. Has the **Wishlist Button block** been added via **Theme Editor** on that specific page template? The block must be added to each template individually, not just the default one.

**If both are already enabled/added and the button still isn't showing:**
- On a custom/non-standard theme, or if Theme Editor shows the error `"wishlist-button" not added. Liquid templates don't support sections and blocks` — the app injects the button automatically via a script instead. Go to **Online Store → Customize → App embeds**, turn ON Joy Wishlist (and turn off any conflicting wishlist app). The button will show correctly on the live storefront even though it won't appear inside the Theme Editor preview — disregard the dashboard error.
- If a manual snippet is still needed for a custom theme, the guide is: `avadagroup.gitbook.io/joy-wishlist/getting-started/publish-your-docs/wishlist-button/add-snippet-code-to-theme-code`. There's no single snippet that works for every theme — it needs tech-team adjustment per store.
- Otherwise, collect the store's theme name/domain and affected page/template and escalate to the tech team.

**Note:** the button cannot be merged into the same row/block as Buy Now/Add to Cart (confirmed not feasible by dev). A CSS-based width/padding adjustment can make it sit visually close instead.

---

Q: How do I turn on the wishlist button on collection page or home page thumbnails?
Q: I want the heart icon to show on product cards in my collection grid.
A: **"Show on collection page"** requires a quick backend setup from the team, not fully self-serve — share your store URL and preferred button position on the thumbnail, and the team will configure it and follow up.

**"Show on home page"** is self-serve — go to **Wishlist Design → Wishlist Button** and turn on "Show on home page."

---

Q: I want the wishlist icon hidden, but I'm not sure which one the merchant means.
Q: Merchant says "hide the wishlist icon" without specifying where.
A: Never guess — there are at least 4 different things a "wishlist icon" could mean (header icon, floating button, the per-product button on thumbnails, or the button on a single product page), each under a different setting.

**Ask first:** "Could you share a screenshot with the icon you'd like to hide, or describe exactly where it appears (e.g. which page, section, what it's next to)?"

Then classify:
| Where it is | What it is | Fix |
|---|---|---|
| Fixed at top of every page near logo/cart | Header icon | Wishlist Access → toggle off Header icon |
| Floats as you scroll, any page | Floating button | Wishlist Access → toggle off Floating button |
| On every product thumbnail across all collections/home | Wishlist Button global toggle | Wishlist Button → toggle off "Show on home/collection page" |
| Below Add to Cart on all product pages | Wishlist Button global toggle | Wishlist Button → toggle off "Show on product details page" |
| Only in ONE section/collection, keep elsewhere | Same global toggle, but scoped | Not self-serve — needs custom CSS from the tech team |
| Only on ONE product, keep on others | Same global toggle, but scoped | Not self-serve — needs custom Liquid/CSS from the tech team |

Confirm the classification back with the merchant before acting, then execute the fix (direct navigation path for global toggles, or escalate for scoped requests).

---

Q: My theme has its own built-in wishlist and now I'm seeing duplicate heart icons.
Q: The wishlist icon conflicts with another wishlist app/feature on my store.
A: This is common with themes that have a native wishlist (e.g. MINIMOG) or another installed wishlist app. The team can sometimes apply a temporary CSS fix to hide the conflicting icon, but the permanent, correct fix is disabling the other wishlist app/feature so only Joy Wishlist is active. Matching a theme's native icon set/positions exactly is not currently supported.

---

Q: The wishlist button/icon disappeared after a theme update.
A: Common causes: (1) custom CSS previously applied gets wiped by a theme update — needs to be re-applied by the tech team; (2) app settings reset after certain theme changes and need re-toggling; (3) app embed gets disabled when switching themes. If it's intermittent with no clear trigger, escalate to dev for investigation rather than repeating the same fix.
