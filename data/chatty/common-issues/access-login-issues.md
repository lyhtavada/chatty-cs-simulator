---
category: Common Issues
topic: Access & Login Issues
source: notion/Chatty FAQs
---

Q: The merchant sees "Account not activated" when logging into app.meetchatty.com.
Q: Merchant can't log in — account not activated error.
A: Common causes:

1. The merchant has never opened Chatty from Shopify Admin after installing — no internal account was created.
2. The app was uninstalled and reinstalled but the old account wasn't reactivated.
3. The merchant is trying to log in directly via the external link instead of through Shopify Admin.
4. Browser has cached old data.

**Solution:**
- Guide the merchant to open Chatty from Shopify Admin first (Apps > Chatty) to activate the account.
- After activation, they can use app.meetchatty.com.
- If the issue persists, suggest clearing browser cache and trying again.

---

Q: The merchant or team member gets "Incorrect email or password" on app.meetchatty.com.
Q: Agent can't log in to the Chatty web app.
A: This depends on the sign-up method used:

1. **If they used "Create account" (custom password):**
   - Log in with email + the password they created during sign-up.
   - If forgotten, click "Forgot password" to reset.

2. **If they used "Sign up with Google":**
   - Click "Sign in with Google" and use the same Gmail account they originally signed up with.

Ask the merchant/agent which method they used to sign up, then guide accordingly.

---

Q: A development store is blocked from using Chatty.
Q: The app shows "Not Found" on a development store.
A: Chatty automatically blocks access from development stores with emails from blacklisted domains (competitors and known testing accounts).

**Blacklisted domains include:** @tidio.com, @intercom.com, @firegroup.io, @flowio.app, @beae.com, @fireapps.vn, @channelwill.cn, @bsscommerce.com, @amasty.com, @secomus.com, @appsfinal.com, @omegatheme.com, @loox.io, @samita.io.

If the merchant's email belongs to a blacklisted domain, CS does not need to continue support — resolve the conversation.

---

Q: A Chinese merchant can't access Chatty — the screen is blank/white.
Q: Merchant from China sees white screen and console errors.
A: Chatty is hosted on Google Cloud, which is commonly blocked by China's Great Firewall.

**Solution:**
1. Confirm the merchant is located in China.
2. If not using a VPN: guide them to use a reputable VPN that works in China.
3. If already using a VPN: suggest trying a different VPN or network.
4. Send the standalone link: `https://app.meetchatty.com` and instruct them to try with VPN enabled.
5. If other apps work fine, explain Chatty's Google Cloud hosting limitation.
6. Escalate to dev only if VPN + standalone link still doesn't work.

---

Q: How does a merchant manage multiple stores from one account?
Q: Can I use one Chatty account for multiple Shopify stores?
A: Each Shopify store requires its own Chatty installation. The merchant can access each store's Chatty separately through their Shopify Admin.

For team members who work across multiple stores, they can be invited as team members on each store's Chatty installation and switch between them.
