---
category: Common Issues
topic: Notifications & Email Issues
source: reports/weekly-faqs/joy + cs2 KB
---

Q: My new store's Notifications feature is disabled and I can't turn it on.
A: Stores under 7 days old (installed after 2025-01-13) have Notifications disabled by default as an anti-phishing precaution — this is temporary and lifts automatically once the store passes 7 days, or the team can verify and enable it sooner on request. This is expected behavior, not a bug or a plan restriction — don't disclose the exact "under 7 days" rule to the merchant. Collect the store URL and let the merchant know the team will review and enable it, usually within 1-2 business days, `<escalate_human>`.

---

Q: My customers received point/loyalty emails they never signed up for — this feels like a privacy issue.
A: Treat this as high priority, not a routine deliverability ticket. Immediate step: turn the **global notification toggle off** (Joy Admin → Notifications) to stop all Joy emails at once, then re-enable only the specific enrolled-member events actually wanted. Check for a Sandbox-mode leak or notification-config cause. For any privacy/GDPR angle, escalate to the team immediately, confirm what was sent and to whom, and address the merchant's data-handling concern directly, `<escalate_human>`.

---

Q: How do I stop or limit the notification emails Joy sends to customers?
A: Notifications are available on **All plans** at **Joy Admin → Notifications**, with two layers: a **global toggle** (master switch) and per-program toggles underneath it (Birthday rewards, Earn points, POS redemption, Redeem points, Referral coupons/points, Referral invite, VIP tier reach, Points expiry). Turn off the specific program(s) the merchant doesn't want emailing customers, rather than the global toggle, if some emails should keep sending.

---

Q: My custom sender emails aren't delivering / are landing in spam.
A: Check in order:
1. Confirm the sender email status shows **Verified** in Joy.
2. Check for an **SPF record** including `mailgun.org` (Joy's Simple Custom Sender uses Avada's shared domain `send.avada.io`) — only one SPF record is allowed per domain; inspect with a tool like mxtoolbox.com.
3. Check the domain's **DMARC policy** — a `reject` policy will block Simple Custom Sender; recommend setting it to `none` only if the merchant understands the impact of relaxing DMARC.
4. For 100% deliverability on Advanced/Ultimate, recommend **Custom SMTP** setup instead of the shared sender.
5. Send a test email (**Email Notification → select template → Send test email**) and check Spam/Promotions folders; a mail-testing tool can help diagnose further.

---

Q: The verification email for my sender address never arrived, or I can't get verified.
A: Validate the sender email address is real and not typo'd. If valid, resend the verification email and ask the merchant to check Inbox/Spam and click the link. Recheck status in Joy after a few minutes; retry once or twice. If still unverified after that, escalate with the details, `<escalate_human>`.

---

Q: I edited an email template but my changes didn't save.
A: Confirm the merchant actually clicked **Save changes** after editing (a common miss). Suggest copying the edited content to a separate file as a backup before retrying, then log out/back into the app and re-edit the template — after clicking Save, wait 3-5 seconds before reloading the page (a fast reload can race the save). If it persists, escalate with the merchant's store link, the template name, and the latest error timestamp, `<escalate_human>`.
