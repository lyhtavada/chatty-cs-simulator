---
category: Common Issues
topic: Notification Issues
source: notion/Chatty FAQs
---

Q: The merchant is not receiving push notifications on desktop when new messages arrive.
Q: Desktop push notifications don't work for Chatty.
A: Check these settings in order:

**Step 1: Verify app notification settings**
- Go to **Settings → Notifications**. Under **Web push**, if the label shows "Not subscribe," click **Subscribe** first, then click **Manage**. Ensure the relevant notification triggers are toggled on.

**Step 2: Verify browser and device settings**
- Browser must have notifications allowed for Chatty/app.chatty.net.
- PC/laptop system settings must allow notifications (not in Silent/Do Not Disturb mode).
- Device must not be in presentation mode or screen recording mode.

**Step 3: If settings are correct but still no notifications**
- Clear browser cache and cookies.
- Restart the computer.
- Open browser DevTools (F12) > Application > Service Workers > Update the firebase-messaging-sw.js service worker.

**Step 4: If still not resolved**
- Offer to use TeamViewer/AnyDesk to directly check the merchant's settings (shortcut `!teamview-check`).
- If the issue persists, forward to dev team with detailed info.

**Meanwhile:** Recommend email notifications or installing the Chatty mobile app as alternatives.

---

Q: Notification banners show up but there's no sound when a new message arrives.
Q: The merchant says notification sound stopped working, even though the settings look correct.
A: This is a different problem from "no notifications at all" — the visual banner is arriving, only the sound is missing.

**Step 1: Check the sound settings in Chatty**
- Go to **Settings → Notifications** → confirm the relevant triggers have Web/desktop notifications on (click **Subscribe** if it shows "Not subscribe").
- Under **Sound settings**, confirm the sound toggle is on and a sound option is selected (Only first message, or All messages).

**Step 2: Check the browser and OS**
- The browser tab must not be muted (right-click the tab → Unmute site).
- Do Not Disturb / Focus must be off.
- On macOS: System Settings → Notifications → [browser] → Allow notifications + Play sound for notifications.

**Step 3: Known compatibility limitation (macOS + Chrome)**
- On **macOS with Google Chrome** (and other Chromium browsers), push-notification **sound** is a documented Chrome/macOS compatibility issue — not a Chatty bug. Visual banners work; the sound does not play.
- Recommend **Safari** to resolve it — Chatty can be installed as a desktop app in Safari (Share icon → Add to Dock), and notification sound works there.

**If sound still fails across multiple devices and multiple browsers** after all of the above, escalate with: device model, OS version, browser + version, and confirmation of which steps were already checked.

---

Q: The merchant is not receiving mobile app notifications.
Q: Chatty mobile app push notifications are not working.
A: Check these items:

1. Verify the mobile app is installed and the merchant is logged in.
2. Check device notification settings — Chatty must be allowed to send notifications.
3. Ensure the phone is not in Do Not Disturb mode.
4. Try uninstalling and reinstalling the mobile app.
5. If the issue persists, collect device model, OS version, and app version, then escalate to dev team.

---

Q: The merchant is not receiving email notifications when new messages arrive.
Q: Email alerts for new chat messages are not being sent.
A: Verify these settings:

1. Email notifications must be enabled in Chatty's notification settings.
2. Check the merchant's email spam/junk folder.
3. Verify the notification email address is correct.
4. If using a corporate email, the organization may be blocking automated emails.

---

Q: Chatty is not showing in the device's notification settings.
Q: I can't find Chatty in my phone/computer notification settings to enable it.
A: This can happen if:

1. The app was never opened after installation (notifications permission was never requested).
2. The notification permission was denied on first prompt and needs to be manually re-enabled.

**Solution:** Guide the merchant to manually find and enable Chatty notifications in their device settings, or clear app data and reopen to trigger the permission prompt again.

---

Q: How do I trigger the push notification permission popup again on mobile?
Q: The notification popup never appeared or was dismissed.
A: If the notification permission popup was dismissed or denied:

1. Go to device Settings > Apps > Chatty > Notifications > Enable notifications.
2. Alternatively, uninstall and reinstall the app to trigger the permission prompt again.

---

Q: Chatty is disconnected in Customer Events (App Pixel).
Q: The Chatty app pixel shows as disconnected in Shopify.
A: The App Pixel may become disconnected due to theme changes or Shopify updates.

**Solution:**
1. Go to Shopify Admin > Settings > Customer Events.
2. Find Chatty in the list and reconnect/re-enable it.
3. Verify the connection is active.
4. If the merchant cannot reconnect, collect details and escalate to TS team.
