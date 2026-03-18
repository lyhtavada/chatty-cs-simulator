---
category: Common Issues
topic: AI Product Sync Issues
source: notion/Chatty FAQs
---

Q: The AI product sync is stuck and not making progress.
Q: Product synchronization for AI data source is hanging.
A: When the product sync gets stuck:

**Step 1: Confirm the sync start time**
- Go to AI Assistant > Data Source and check the timestamp of the most recent sync.

**Step 2: If sync has been running too long with no progress**
- Go to DevZone > Testing and click "Start Auto Resync" to reset and restart the sync process.
- Warning: this restarts the sync from scratch.

**Step 3: Monitor and confirm**
- After resync, update the merchant. When products are fully displayed in the data source, notify them.
- Advise the merchant not to make changes in the app (editing product tags, etc.) during resync to avoid data conflicts.

---

Q: AI is not syncing all products from the store.
Q: The product count in AI data source doesn't match the Shopify product count.
A: Only published, in-stock products are synced to the AI. Products sync daily at 12:00 AM PST.

**Common causes:**
- Products are in draft status or out of stock.
- The merchant has hit their plan's product limit (Free: 100, Basic: 500, Pro: 8,000, Plus: 20,000).
- Sync hasn't run yet after recent product changes.

**Support flow:**
1. Check the merchant's plan and product count against the plan limit.
2. Verify products are published and in stock in Shopify.
3. If needed, wait for the next daily sync or trigger a manual resync.
4. If the issue persists, escalate to the dev team.

---

Q: The merchant deleted all products in Shopify but old products still show in AI sync.
Q: Products were removed from Shopify but AI still answers questions about them.
A: The sync may not immediately reflect product deletions.

**Solution:**
1. Suggest the merchant turn off product synchronization entirely.
2. When they add products back later, they can re-enable sync.
3. Advise the merchant not to sync repeatedly — either sync manually once or rely on the daily auto-sync at 7 AM.

---

Q: Merchant wants to extend the number of products, URLs, or files for AI training.
Q: The merchant has hit the AI training data limit on their plan.
A: Plan limits restrict the number of products/URLs/files for AI training.

**Support flow:**
1. Check the merchant's current plan and what data type they need more of (Products/URLs/Files).
2. Explain plan limits and recommend an appropriate upgrade.
3. If the merchant is not ready to upgrade (testing, small budget): escalate to `#sales-cs-success` tagging PM + CSL.
4. For small increases (100-200 products, 10-20 URLs/Files): CS can proactively extend limits in DevZone without requiring an upgrade.
5. For stores with > 10,000 products: use shortcut `!ai_sync_over_10k` to offer a call with the sales lead.
6. Never promise beyond your authority — always say "I'll check internally" before confirming extensions.
