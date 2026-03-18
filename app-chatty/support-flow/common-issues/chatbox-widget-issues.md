---
category: Common Issues
topic: Chatbox & Widget Issues
source: notion/Chatty FAQs
---

Q: The live chat button is not showing on the store.
Q: Chatbox widget doesn't appear on the merchant's website.
A: Common causes and solutions:

**Cause 1: App Embed not enabled**
- Go to Shopify Admin > Online Store > Themes > Customize > App Embeds.
- Ensure Chatty is toggled ON.
- Ask the merchant for a screenshot to verify.

**Cause 2: Live chat not turned on in app settings**
- Go to Chatbox > General > Blocks > ensure "Live chat" is enabled.

**Cause 3: Theme conflict**
- If App Embed is enabled but the button still doesn't show, ask the merchant for their theme name.
- Create a card for the TS team to investigate the technical issue.
- Follow up with the merchant on progress.

---

Q: The FAQ page is not showing on the store.
Q: Merchant can't see the FAQ page on their website.
A: Common causes:

1. **FAQ page not enabled in app:** Guide the merchant to Settings > Pages > Enable FAQ page.
2. **FAQ page URL not added to menu:** Help the merchant get the FAQ page URL from the app and add it to their store's navigation menu.
3. CS can request access to Themes and Pages to assist directly.

Reference: https://help.chatty.net/build-faqs/faqs-page

**Tip:** Suggest adding the FAQ URL to the main navigation menu for better visibility.

---

Q: The Chatty FAQ page is overwriting other page templates.
Q: Other pages (About Us, Contact) look wrong after installing Chatty FAQ.
A: The Chatty app assigns FAQ content to the default page template, which can affect other pages.

**Solution:** (use shortcut `!faq_overwrite_fix`)
1. In Shopify theme editor > Theme Templates, create a new template (e.g., `chatty-faq`).
2. Go to Shopify Admin > Online Store > Pages.
3. Select the FAQ page created by Chatty (usually "Frequently Asked Questions").
4. Assign the new template to this FAQ page only.
5. In the Chatty app, set the correct FAQ page URL.
6. Verify other content pages are no longer affected.

---

Q: The merchant wants to move the live chat button to a different position.
Q: How to change the position of the chat widget on the store.
A: The chatbox button position can be adjusted in Chatbox > Appearance > Set chatbox button > Select button alignment.

If the merchant needs more specific positioning:
1. Ask the merchant for their desired position.
2. For basic alignment changes, use the built-in button alignment settings.
3. For custom positioning, suggest CSS customization (if the merchant has coding knowledge).
4. If the merchant can't do it themselves, create a ticket for the TS team.

---

Q: How do I remove Chatty branding from the widget?
Q: Merchant wants to remove the "Powered by Chatty" watermark.
A: To remove branding:

1. Go to DevZone > General > Enable "Remove branding."
2. Notify the merchant to check.
3. Communicate: "Normally, this option is only available for paid plans. However, we've helped remove the branding for you this time as a special support."
4. After removing branding, proactively offer to help with other features.

**Important:** Do NOT ask for a review immediately after offering branding removal — Shopify considers this "exchange for review." First help with an additional task, then request a review based on the support experience.

---

Q: How do I use JavaScript to open or close the Chatty widget programmatically?
Q: Can I trigger the chatbox to open via code?
A: Chatty provides JavaScript functions for widget control:

- **Toggle open/close:** `avadaFaqTrigger()`
- **Close widget:** `ChattyJS.closeWidget()`
- **Open widget (general):** `ChattyJS.openWidget()`
- **Open to specific page:**
  - `ChattyJS.openWidget('#chatty-home')` — Home
  - `ChattyJS.openWidget('#chatty-chat')` — Message/Live Chat
  - `ChattyJS.openWidget('#chatty-tracking')` — Order Tracking
  - `ChattyJS.openWidget('#chatty-help')` — Help/FAQ

Use these when deep links cannot be used or the trigger element is not a standard link.

---

Q: How do I enable FAQ category icons for a merchant?
Q: The "View more" icons option in FAQ categories is locked.
A: For newly installed apps, the category icons feature is locked by default.

**Solution:**
1. Get the merchant's Store URL.
2. Go to DevZone and enable the category icons feature.
3. Notify the merchant to check if icons are now available.
