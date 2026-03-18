---
category: Common Issues
topic: AI Training & Setup
source: notion/Chatty FAQs
---

Q: How do I help a merchant set up and train the AI assistant?
Q: What should I check when a merchant needs help with AI training?
A: When helping merchants with AI training:

**Step 1: Check the merchant's plan first**
- Store Instruction, Scenarios, QnA, and Data Source expansion only apply to paid plans.
- Install Store Lead Chrome Extension to check the store's yearly revenue (ARR).

**Step 2: Prioritize support based on plan and revenue**
- Prioritize paid plan customers for faster, more detailed support.
- For stores with ARR > $200K on a paid plan, proactively help with initial setup.
- For qualifying merchants (ARR > $200K), offer a call with PM using shortcut `!chatty-demo-call`.

**Step 3: Help with Custom Instructions or Scenarios**
- Send the template file using shortcut `!AI_scenario_template_link`.
- If the merchant fills it out: request edit access and add team members (tungqt@avada.io, phuongnt@avadagroup.com).
- Create a card and post to `#chatty-support` Slack channel.

---

Q: The merchant accidentally deleted their AI Instructions. How do I recover them?
Q: How to restore AI instructions that were deleted by mistake?
A: To recover deleted AI Instructions:

1. Go to Dashboard > Tools > Trace Logs (OpenAI platform).
2. Find an old conversation from the store (from when the AI was working correctly).
3. Open the trace details and locate the AI Instruction used at that time.
4. Copy the full instruction content and paste it back into the AI Instructions section in Chatty.

**Important notes:**
- Choose a conversation date as close as possible to before the deletion.
- If the store uses multi-language, verify the trace matches the correct language.
- After recovery, the merchant should review and edit the instructions as needed.

---

Q: How do I test the AI assistant without activating it for customers?
Q: Can I test AI responses without using the merchant's AI reply quota?
A: Use the built-in Test feature:

1. Go to the app > AI Assistant section > use the **Test** feature.
2. In the Test interface, enter questions and check AI responses.
3. This does NOT count against the merchant's AI replies quota.

**Important:** Under the new pricing policy, each plan (except Plus) has limited AI Replies. Do not test directly on the merchant's live chat without permission.

---

Q: The merchant doesn't want the AI to share the support email in chat.
Q: How do I stop the AI from providing the store's email address?
A: Add a custom instruction to prevent this:

1. Go to AI Instructions.
2. Add: `Do not provide Store Support Email addresses to customers.`
3. Save the changes.
4. Test by simulating scenarios like "How can I contact support?" to confirm the email is no longer shown.

---

Q: The merchant wants to disable AI follow-up questions.
Q: AI keeps asking unnecessary follow-up questions after answering.
A: To disable follow-up questions:

1. Confirm the merchant wants the AI to answer directly without follow-ups.
2. Disable the feature in DevZone: toggle off the follow-up questions option.
3. Explain the impact: responses may be shorter and less personalized after disabling.
4. Ask the merchant to test again and confirm the behavior matches expectations.

---

Q: How do I add bonus AI conversations for a merchant?
Q: Merchant ran out of AI conversations, how to add more?
A: To add AI conversation bonus:

1. Go to DevZone > Testing.
2. Enter the number of conversations to add in the "Limit" field.
3. Click "Set."

---

Q: The AI sends the wrong support email address to customers.
Q: AI is showing an incorrect contact email in chat.
A: The AI pulls the support email from **Transfer (AI Settings) > Contact Support Email**.

**Solution:**
1. Check which email the AI sent to the customer.
2. Go to Chatty > AI Assistant > Transfer, check the Contact Support Email field.
3. If the wrong email was entered, guide the merchant to update it with the correct one.
4. After updating, the AI will automatically use the new email.

---

Q: The AI is not replying to emails forwarded to the inbox.
Q: AI doesn't respond to email conversations.
A: Check these items:

1. **Verify AI email channel is enabled:** Go to AI Assistant Settings > AI Channels > Email.
2. **Understand the reply logic:** When enabled, AI auto-replies after 5 minutes if no agent responds. AI only replies to genuine customer inquiries about sales or support (products, orders, policies). Spam, marketing, or system notifications are skipped.
3. If everything is configured correctly but AI still doesn't reply, escalate to the dev team.

---

Q: AI does not automatically transfer conversations to agents.
Q: The AI detected "talk to human" intent but didn't assign to any agent.
A: Check the assignment settings:

- **Manual Assignment:** The system does not auto-assign. The merchant must manually assign conversations to team members. Recommend switching to Automatic Assignment if they want auto-transfer.
- **Automatic Assignment (round-robin):** Check "Reassign conversations" settings. If configured correctly but conversations still show "Unassigned," collect the conversation details and escalate to TS/dev team.

---

Q: How do I hide the product preview card in AI chat?
Q: Merchant doesn't want the product card showing in chat conversations.
A: There is currently no dedicated app setting to disable product preview cards. The preview card shares CSS with the "Reply to" element, so hiding via CSS would hide both.

**Handle based on the merchant's reason:**
- If they don't want AI to sell: suggest adjusting AI to focus on support skills instead.
- If concerned about cluttered UI: explain the CSS limitation.
- If they need more control: log the feedback and escalate to the product team.

---

Q: Merchant enabled pre-chat form but customers still get AI responses before filling it out.
Q: Why does AI respond before the pre-chat form appears?
A: This happens when customers interact via the AI Product Assistant on the product page. The AI Product Assistant works like an FAQ — it prioritizes quick answers without requiring customer info first.

If the merchant's priority is collecting customer information before any response, they should hide the AI Product Assistant on the storefront and rely solely on the pre-chat form.
