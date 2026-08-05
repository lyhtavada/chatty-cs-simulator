# Chatty — Product Knowledge Reference
# Used by the scenario generator to create realistic, product-accurate scenarios.

## What Chatty Does
Chatty is a Shopify live chat + AI chatbot app. It helps merchants:
- Talk to store visitors in real time (live chat)
- Automate support 24/7 with an AI assistant trained on store data
- Build a self-serve FAQ help center on their storefront

Shopify "Built for Shopify" badge. 4.9★ / 1,700+ reviews.

## Plans

| | Free | Basic ($19.99/mo) | Pro ($68.99/mo) | Plus ($199.99/mo) |
|---|---|---|---|---|
| AI conversations | 50/month (resets monthly) | 100/month | 500/month | 1,000/month |
| Extra conversations | — | $0.40 each | $0.40 each | $0.40 each |
| Products for AI | 200 | 500 | 8,000 | Unlimited |
| Team members | 1 | 5 | 10 | Unlimited |
| Auto-translation | 1 language | 2 | 9 | Unlimited |
| Chat history | 90 days | 12 months | Unlimited | Unlimited |
| Smart recommendations | ✗ | ✗ | ✓ | ✓ |
| CSAT survey | ✗ | ✗ | ✓ | ✓ |
| Cart booster | ✗ | ✗ | ✓ | ✓ |
| Dedicated AI consultant | ✗ | ✗ | ✗ | ✓ |

Annual billing: ~15% savings. 7-day free trial. 30-day money-back guarantee.

## Core Features

### 1. Live Chat
- Inbox: Unified inbox for all conversations
- Channels: Email, Facebook Messenger, Instagram, WhatsApp — all in one inbox
- Contacts: Customer profiles with tags, notes, conversation history
- Team: Invite members, assign roles, assign conversations
- Quick Replies: Pre-saved templates for faster responses
- Proactive Chat: Auto-triggered messages based on visitor behavior
- Real-time Translation: Auto-translate between merchant and customer languages

### 2. AI Assistant
- Handles conversations 24/7, appears as assignee in inbox
- Chat Summary: AI summarizes conversation with issue highlights + response suggestions when transferring to human
- Data Sources: Products (auto-synced daily at 00:00 UTC), discounts, markets, FAQs, policies, manual Q&As, URLs, files
- AI Skills: Smart product recommendations, size guide, inventory status, transfer to human, refund/return form, order tracking
- Settings: Bot name, avatar, welcome message, custom instructions, AI availability, AI channels
- Test & Optimize: Test zone to preview AI responses

### 3. Chatbox (Widget)
- General: On/off toggle, focus mode, header, blocks (Live chat, Contact us, Order tracking, FAQs, Categories)
- Appearance: Brand colors, button style (icon, size, position), chatbox style
- Advanced: Deep links, display rules (devices, pages), custom CSS
- Contact Button: 11 methods — WhatsApp, Messenger, Phone, Email, Instagram, Telegram, Skype, Line, Zalo, TikTok, SMS
- Embedded Chatbox: Embed directly into page content

### 4. FAQ Builder
- Categories with icons and descriptions
- Questions with rich text answers
- FAQ page with customizable theme + FAQ block inside chatbox
- Analytics: views, clicks, search queries
- Export as CSV, multi-language translation

### 5. Order Tracking
- Customers track orders directly in the chatbox
- Supports Shopify native + third-party tracking

### 6. Integrations
- Klaviyo: Sync contacts, tags, conversation data
- Zendesk: Unified helpdesk
- Joy Loyalty: Show loyalty points/tier in conversations
- Air Reviews: Turns positive support conversations into product reviews (helps prevent negative reviews by resolving issues in chat first)
- Powerful Contact Form: Form submissions become conversations in the Chatty inbox

## Common Issues (Quick Reference)

| Issue | Root cause |
|---|---|
| Chatbox not showing | App embed off in theme editor, or display rules excluding the page |
| AI not responding | AI assistant off, live chat block disabled, or insufficient training data |
| Email not connecting (Outlook) | Org Outlook blocks auto-forwarding — IT admin needs to allow |
| WhatsApp not connecting | Missing Business FB page, or WA Business not linked |
| Translation not showing | Language not added/published in Shopify Admin |
| AI recommending wrong products | Check Smart Recommendations collections |
| Products missing from AI | Only published + in-stock products train. Check plan limit. |
| Order tracking not working | Order Tracking block must be enabled in chatbox |

## Key Terms

| Term | Meaning |
|---|---|
| AI conversation | A customer chat handled by the AI assistant |
| Transfer | AI hands off to a human agent |
| Data source | Info used to train AI (products, FAQs, custom data) |
| AI skill | Specialized AI capability (recommendations, size guide, etc.) |
| Chatbox | The chat widget on the storefront |
| Deep link | URL that opens a specific chatbox section |
| Proactive chat | Auto-triggered message based on visitor behavior |
| Quick reply | Pre-saved response template |
| CSAT | Customer Satisfaction survey (Pro+ only) |
| Smart recommendations | AI product suggestions from collections |

## CS Process Quick Reference

### Escalation Triggers
- Technical bug after CS troubleshooting → TS team
- Refund request → CS Leader (NEVER approve without CSL approval)
- Angry merchant after 2 attempts → CS Leader
- Critical bug (app down, data loss) → PM + TS Leader immediately
- VIP merchant → CS Leader FYI immediately
- Discount/pricing negotiation → PM / Sales Manager

### SLA Targets
- P0 Critical: < 1 hour first response, 4-24 hours resolution
- Complaint: < 2 hours first response, same day resolution
- Pre-sales: < 4 hours first response, same day resolution
- How-to (Regular): < 24 hours first response, < 48 hours resolution
- Refund: < 2 hours first response, < 24 hours resolution
