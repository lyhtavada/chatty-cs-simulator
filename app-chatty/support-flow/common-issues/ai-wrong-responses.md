---
category: Common Issues
topic: AI Giving Wrong Responses
source: notion/Chatty FAQs
---

Q: The AI assistant is giving wrong answers to customer questions. What should I do?
Q: AI is answering incorrectly. How do I fix it?
Q: A merchant says the AI chatbot responded with wrong information.
A: When the AI provides incorrect answers, follow this process:

**Step 1: Identify the issue**
- Ask the merchant for the specific chat link/ID where the AI responded incorrectly.
- Determine what information was wrong (product details, pricing, policy, etc.).

**Step 2: Review the AI's data sources**
- For live conversations: open the conversation and click "Review Sources" under each AI reply to see which data sources and instructions the AI used.
- For test conversations: go to Dev Zone to review test conversation history, check context, data sources, and instructions.

**Step 3: Diagnose the root cause**
- **(a) Source data is wrong or incomplete:** Recommend the merchant update or correct the source content. CS can assist with edits.
- **(b) Source is correct but AI misinterprets:** Confirm the source is accurate but AI inferred incorrectly. Report to dev team. Suggest rephrasing questions or adding more detailed documentation.
- **(c) Instructions are inappropriate:** Review App, Custom, and Scenario Instructions. Identify what causes the AI to misunderstand. Propose instruction edits and test.

**Step 4: Follow up**
- If the issue persists after corrections, escalate to the product/dev team.
- Continue following up with the merchant until resolved.

---

Q: The AI is showing wrong product prices. It doesn't match the customer's market.
Q: AI suggests wrong price — not matching the market the customer is visiting.
A: This happens when the AI pulls pricing from the main domain instead of the market-specific pricing.

**Step 1: Check Markets setup**
- Ask the merchant if they have set up Markets in Shopify Admin.
- Check if "Sync Markets" is enabled in AI Assistant settings.

**Step 2: CS reproduces the issue**
- Visit the merchant's market domain and test the same question.

**Step 3: Handle by scenario**
- **If Markets are NOT set up:** Guide the merchant to set up Markets in Shopify Admin and enable "Sync Markets" in AI Assistant settings. Test again afterward.
- **If Markets ARE set up but issue persists:** Request staff access to inspect Markets and Product settings. Report the issue to dev team with screenshots, reproduction steps, Market config, and product pricing per Market.

---

Q: The AI sends wrong product links — they lead to 404 pages or wrong products.
Q: AI product links are broken or incorrect.
A: This is a known bug that the dev team has acknowledged.

**Support flow:**
1. Ask the merchant for the specific chat with the incorrect link.
2. Go to the merchant's store and test in the AI Test section to confirm the issue.
3. Report the store URL and chat link in the internal Slack bug thread for dev team follow-up.
4. Reply to the merchant using shortcut `!ai-wrong-link`:
   - Inform them the dev team has acknowledged the bug and is investigating.
   - Suggest manually copying correct product links as a workaround.
   - Apologize for the inconvenience and promise to keep them updated.
5. Follow up when the fix is deployed.

---

Q: The AI suggests wrong domain for product URLs when customer visits a market-specific domain.
Q: Customer visits abc.fr but AI shows links to abc.com.
A: This is a current technical limitation — the app only stores product data for the main domain. Multi-domain support per Shopify Market is being developed.

**Support flow:**
1. Confirm which market domain the customer visited and what URL the AI returned.
2. Check the merchant's Shopify Markets setup: verify country is in Market setup and domain mapping is correct.
3. Reproduce the issue by visiting the market domain and testing the same question.
4. Notify the merchant using shortcut `!AI-suggest-wrong-market-link` — explain this is a known limitation and a fix is planned.
5. Create a tracking card and follow up with the merchant.

---

Q: The AI does not return variant-specific product links.
Q: AI only sends generic product links, not links for specific variants (size, color).
A: This is a feature limitation — variant-level links have not been fully implemented yet. The AI's data source does not store variant-specific URLs.

A feature is currently in development to support variant-specific links. In the meantime, inform the merchant that the AI can describe variants but cannot link directly to them.

---

Q: AI responses are duplicated — the same answer appears twice.
Q: The AI sends duplicate messages in the chat.
A: Duplicate AI responses can happen due to:
- Customer sending the same question multiple times (re-clicking or network lag).
- Slow or unstable network causing duplicate signals to the server.
- Temporary system-side processing error.

**Support flow:**
1. Request the chat ID and review the conversation to determine if it was user error or system error.
2. If system error: create a card for TS to investigate with conversation link, timestamp, and merchant name.
3. Suggest the merchant try "refresh chat" or switch to manual chat if duplication continues.
4. Follow up when the technical team responds.

---

Q: AI recommends products that don't belong to the merchant's store.
Q: The AI is suggesting products from other websites.
A: This can happen when AI training data is incomplete or not synced properly.

**Support flow:**
1. Request the chat ID of the incorrect response.
2. Check AI assistant settings: ensure AI product recommendation is enabled and sync is complete.
3. If settings are correct: reproduce the issue on the storefront. If confirmed, forward to dev team with full details.
4. If settings are incomplete: guide the merchant to enable and sync, then test again.
5. Monitor and update the merchant on progress.
