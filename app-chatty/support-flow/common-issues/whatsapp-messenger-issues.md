---
category: Common Issues
topic: WhatsApp & Messenger Channel Issues
source: notion/Chatty FAQs
---

Q: What does a merchant need to connect WhatsApp to Chatty?
Q: WhatsApp connection requirements checklist.
A: The merchant needs all of the following:

**1. Meta Business Manager account**
- Must have a valid Meta Business Manager with **Business Admin** role.
- Employee role is NOT sufficient — admin access is required.
- Check at: business.facebook.com/settings/people

**2. Valid WhatsApp phone number**
- A phone number NOT currently registered on WhatsApp personal app.
- Or an existing WhatsApp Business number that has been migrated to Cloud API.
- OTP verification must be via SMS or phone call (not WhatsApp app).

**3. Valid business information**
- Business name, type, legal address, website domain.
- Meta may require Business Verification for full features.

**4. Permissions during OAuth**
- Must select their Business Manager, WhatsApp Business Account, and phone number.
- Must grant "AVADA group company limited" permission to manage the number.

**5. Correct Facebook login**
- Facebook account must be added to the Business Manager with proper permissions.
- Browser must not block popups or third-party cookies.

**6. No other WhatsApp API provider**
- If the number is currently connected to another provider (Twilio, 360dialog, etc.), it must be released/migrated first before connecting to Chatty.

---

Q: The merchant connected WhatsApp but it's not working.
Q: WhatsApp connection issues with Chatty.
A: Common WhatsApp connection issues:

1. **Insufficient permissions:** The person connecting must be a Business Admin (not Employee) in Meta Business Manager.
2. **Phone number already in use:** The number is active on WhatsApp personal app or connected to another API provider.
3. **Business verification pending:** Meta requires business verification for full features.
4. **Browser blocking popups:** The OAuth popup may be blocked — advise trying a different browser or disabling popup blockers.

For all WhatsApp issues, verify each item on the checklist above before escalating.

---

Q: Facebook Messenger is connected but new messages don't appear in Chatty.
Q: Messages from Facebook are not showing in Chatty inbox.
A: Check these common causes:

1. **Integration not complete:** Ensure the merchant has fully integrated Messenger with Chatty (all steps completed in the Channels section).
2. **Insufficient page permissions:** The person who connected must have "Manage and access Page messages" permission. Check Page Settings > Page Roles & Permissions.
3. **Permission deselection during setup:** If the merchant deselected items during the Facebook OAuth popup, permissions may be incomplete.
4. **Messages sent before connection:** Only messages sent AFTER Chatty is connected will sync. Old messages must be handled directly in Facebook Messenger.

---

Q: Messages from Meta (Facebook/Instagram) are not showing in Chatty.
Q: Instagram messages not appearing in the Chatty inbox.
A: Similar to Messenger issues — verify:

1. The channel (Messenger or Instagram) is properly connected in Chatty's Channel settings.
2. The connecting user has admin access to the Facebook page.
3. All permissions were granted during the OAuth connection process.
4. Only new messages (sent after connection) will appear in Chatty.

If all settings are correct but messages still don't sync, collect the details and escalate to the TS team.
