---
category: Common Issues
topic: Inbox & Conversation Issues
source: notion/Chatty FAQs
---

Q: The merchant wants to export conversations from the Inbox.
Q: Can I download or export chat history from Chatty?
A: Chatty currently supports exporting **individual conversations only** — open the conversation, click the **⋮ menu** (top right), then **Export transcript**.

Bulk export with a date range filter is not available in the app UI on any plan. If the merchant needs multiple conversations exported, collect the date range and escalate to the team, who can export the data and send it to the merchant's email. The **Zendesk integration** is also an option for ongoing chat history storage (all resolved conversations sync as Zendesk tickets).

---

Q: The merchant set up "Chat as guest" but still sees Anonymous conversations.
Q: Why are there Anonymous conversations when pre-chat form is enabled?
A: Two features can bypass the pre-chat form:

1. **AI Product Page Assistant:** When embedded on product pages, customers can chat immediately without providing email. The system prioritizes fast support.

2. **Proactive Chat:** When enabled, customers can reply to the proactive chat bubble without filling the pre-chat form first.

**Solution:** If the merchant wants to enforce info collection for all conversations, they should disable the AI Product Page Assistant embed and/or Proactive Chat features.

---

Q: How is "Last activity" time calculated in the Inbox?
Q: What does Last Activity mean in conversation list?
A: Last Activity shows the timestamp of the most recent message or action in a conversation. This includes messages from both the customer and the agent/AI, as well as system events like transfers.

---

Q: The merchant wants to manage chats from multiple stores on one account.
Q: Can I see all my stores' conversations in one place?
A: This depends on the plan. On **Free, Basic, and Pro**, each Shopify store has its own separate Chatty installation and inbox — conversations from different stores cannot be merged. On **Plus**, a unified inbox across stores exists: a member can connect up to 10 additional stores (the main store isn't counted) and work all conversations from one inbox.

Team members who work across multiple stores can be invited to each store's Chatty and switch between them via Shopify Admin or app.chatty.net using the store switcher in the top-left corner of the web app. Note: each connected store still keeps its own separate plan, and on mobile, notifications only arrive for the currently active store.

---

Q: The merchant says they get a "404 / page not found / technical problem with Avada app" error when opening a conversation, or the inbox behaves erratically (old conversations reappearing as unread, new chats landing in Resolved instead of Open, two customers' messages mixed in one thread).
Q: Conversations won't open, disappear, or reopen themselves in the inbox.
A: This is a **recognized, active system-side defect** affecting the inbox — it is not a merchant setting, and reinstalling the app does not help.

**Step 1 — First line:** ask the merchant to hard-refresh/reload the page (this resolves it for some) and try an incognito window.

**Step 2 — If it persists, or if any of these symptoms are present, treat it as the same incident and escalate immediately:**
- 404 or "technical problem with Avada app" when opening a conversation, a tab, or any chat record
- Old/resolved conversations reappearing as unread
- New chats landing in Resolved instead of Open
- The Resolve button showing "Reopen" on an already-**Open** conversation and refusing to close it
- The inbox crashing mid-conversation
- Two different customers' messages mixed in one thread — treat this as urgent, since it's a data-integrity issue

Collect: conversation/session IDs, affected customer emails, a screenshot or screen recording, the store URL, and timestamps, then escalate to the dev team. Tell the merchant: "Thanks for flagging — this is a system-side issue our team is investigating; I've logged your details so they can trace it."

**Do not confuse this with normal behavior:** a Reopen button on an already-**Resolved** conversation is expected — conversations auto-resolve after 60 minutes of no team message by default (Settings → Automation → Automatic resolution). Only treat the Reopen button as this defect if it appears on an Open conversation and won't close.
