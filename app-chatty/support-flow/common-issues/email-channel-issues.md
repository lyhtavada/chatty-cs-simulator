---
category: Common Issues
topic: Email Channel Issues
source: notion/Chatty FAQs
---

Q: Emails from Hotmail and Outlook are not being forwarded to Chatty.
Q: Outlook/Hotmail email forwarding doesn't work with Chatty.
A: This is a known compatibility issue between Cloudflare and Microsoft's mail system.

**Workarounds:**
1. **Use an intermediate mailbox:** Set up a Gmail or other domain email to receive from Outlook/Hotmail, then forward to Chatty.
2. **Switch email hosting:** Consider Google Workspace or Zoho Mail for the domain email, then forward to Chatty.
3. **Enable alternative notifications:** Turn on email notifications via Gmail or install the Chatty mobile app to avoid missing messages.

Use shortcut `!outlook-hotmail-fw` to respond. Guide the merchant to test after setting up the workaround.

---

Q: Email forwarding is not getting verified even after adding the forwarding address.
Q: The merchant set up email forwarding but verification fails.
A: Common causes include incorrect forwarding address, email provider blocking automatic forwarding, or verification email going to spam.

**Support flow:**
1. Verify the forwarding address is entered correctly.
2. Ask the merchant to check spam/junk folder for the verification email.
3. If using Outlook/Hotmail, note the Cloudflare compatibility issue and suggest alternative email providers.
4. If the issue persists, check if the email sender configuration is blocking forwarding.

---

Q: The merchant can't verify email forwarding because of email sender issues.
Q: Email sender verification is failing in Chatty.
A: Check if the email provider requires SPF record configuration.

**Solution:**
1. Verify the merchant's email provider settings.
2. If SPF records need updating, guide the merchant to add the SPF record to their DNS settings.
3. Use shortcut for SPF record setup guidance if applicable.
4. Test again after DNS changes propagate (may take up to 48 hours).

---

Q: The merchant didn't receive the verification email when setting up email channel.
Q: Verification email for Chatty email setup never arrived.
A: Check these common causes:

1. **Spam/junk folder:** Ask the merchant to check spam and junk folders.
2. **Email provider blocking:** Some corporate email providers block automated verification emails.
3. **Incorrect email address:** Verify the email was entered correctly in settings.
4. If none of the above, try resending the verification email or use an alternative email address.

---

Q: Email notifications from Chatty are going to the spam box.
Q: Merchant's customers say Chatty emails land in spam.
A: This is typically caused by missing or incorrect email authentication records.

**Solution:**
1. Guide the merchant to add SPF records to their DNS settings for their email provider.
2. Verify DKIM and DMARC records are properly configured.
3. Recommend using a custom sender domain instead of the default noreply@chattyemail.com.
4. If the merchant uses a custom domain, verify the domain in Chatty settings.

---

Q: How do I add SPF records for Chatty email?
Q: Merchant needs to configure SPF for email delivery.
A: Guide the merchant to add SPF records in their DNS provider settings. This ensures emails sent through Chatty are authenticated and less likely to be flagged as spam.

The specific SPF record values depend on the merchant's email hosting provider. Refer to the email provider's documentation for exact configuration steps.

---

Q: The merchant wants to add alias emails to channels.
Q: Can I use multiple email addresses with Chatty?
A: Chatty supports connecting one email to the channel. For additional email addresses, the merchant can set up email forwarding from alias addresses to the connected Chatty email.

---

Q: Clicking the email icon in the Contact Us widget opens the wrong email client.
Q: The email button in the chatbox doesn't work correctly.
A: The email contact button behavior depends on the merchant's chatbox configuration and the customer's device default email client settings. Verify the email address is correctly set in the Contact Us block settings.

---

Q: Merchant gets "Fail to deliver" error emails.
Q: The merchant keeps receiving delivery failure notifications.
A: These errors typically occur when the recipient email is invalid or the email provider rejects the message. Verify the recipient email addresses and check email forwarding configuration for any issues.

---

Q: The merchant wants to transfer the admin email to a different address.
Q: How do I change the admin email for a Chatty account?
A: The admin email is tied to the Shopify store owner account. To change it:

1. Go to the Chatty app settings.
2. Check Team settings for the current admin email.
3. If the merchant needs to change the primary admin, they may need to update their Shopify store owner email first, then re-access Chatty.
