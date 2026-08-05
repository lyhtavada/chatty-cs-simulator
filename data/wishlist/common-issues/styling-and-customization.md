---
category: Common Issues
topic: Styling & CSS Customization
source: KB (cs2.avada.net wishlist-agent) + weekly FAQ mines
---

Q: Can you change the wishlist icon/button color, size, or border-radius?
Q: I want to customize how the wishlist button looks on my store.
A: Basic color and icon customization is self-serve via **Wishlist Design → Wishlist Access/Button → General settings** (icon color, background color, border color, icon type). Button text is under its own **Button text** section on the Wishlist Button tab.

For anything beyond that — border-radius, precise px alignment, matching another button's exact style, uppercase text, icon/image size, image cropping — collect the exact spec and pass it to the team; they apply it as custom CSS. **No collaborator code is needed for styling requests.**

Note: custom CSS can get reverted by theme updates or re-editing in Theme Editor — if a previously-fixed style reverts, it usually needs to be re-applied.

---

Q: I set the background color to white to get a transparent/outline look, but now the icon is invisible.
Q: Can the icon background be transparent?
A: The Background color field only supports solid colors, no transparent value — setting it to white against a white page makes the icon disappear (white-on-white) rather than giving a transparent background. For a genuinely transparent background, share the exact spec and the team will apply it via custom CSS — no collaborator code needed.

---

Q: What image size/format should I use for a custom wishlist icon upload?
A: There's no hard app-enforced spec, but the practical recommendation is a **1:1 (square) ratio image under 200kb** for best display and load performance.

---

Q: After resizing the wishlist icon via custom CSS, another button on the page looks broken.
A: A custom CSS change to one element can occasionally have a knock-on layout effect on a nearby unrelated element. After any custom CSS fix is applied, ask the merchant to check the whole page/section, not just the element that was changed, and report back if anything else shifted.

---

Q: Can I change the color/hover effect of the "Sign In" or "Create account" button on the wishlist login modal?
A: There's currently no self-serve color/hover-state setting for the Login modal's Create account/Log in buttons — they're separate from the "Button color" fields that only style the per-item add-to-cart button on the wishlist page. This needs custom CSS from the tech team: collect the exact spec, no collaborator code needed.

The Login modal's **text** (Modal title, Modal description, Create account button text, Log in button text) IS self-serve and editable under **Wishlist Design → Wishlist Page → Login modal**.

---

Q: Can the wishlist button match my "Buy it now" / Add to Cart button's exact style?
A: There's no self-serve "Add Custom CSS" field for this in the app. Share what you'd like it to match (e.g. same shape/style as the Buy button) and the team will apply the styling from the backend.

---

Q: Can the wishlist button be merged into the same row/block as Add to Cart?
A: Not reliably possible — confirmed not feasible by the dev team, since the Wishlist button is its own separate theme section/block. The workaround is CSS-adjusting the button's width/padding/alignment so it visually sits close to the Add to Cart row, not literally merged into it.

---

Q: I want to hide the wishlist icon in just one section/collection, not everywhere.
A: All the display toggles (Show on collection page, Show on home page, Show on product details page) are global — none can be scoped to a single section, collection, or product. If the merchant only wants it hidden in one specific place while keeping it elsewhere, don't default to the global toggle — confirm scope first, then this needs custom CSS/Liquid scoped to that section from the tech team (Theme access required).
