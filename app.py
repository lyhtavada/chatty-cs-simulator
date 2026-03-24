from __future__ import annotations

"""
CS Training Simulator — Flask Backend
Serves the HTML frontend and provides API endpoints for:
- Scenario listing
- Customer simulation (Groq LLM)
- Session grading
- Results persistence (Supabase)
"""

import os
import json
import random
import re
import time
import yaml
import datetime
from pathlib import Path
from flask import Flask, render_template, request, jsonify, session
from groq import Groq
from supabase import create_client

# --- App ---
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "cs-simulator-secret-2024")

# --- Config ---
DATA_DIR = Path(__file__).resolve().parent / "data"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")
LEADER_PASSWORD = os.environ.get("LEADER_PASSWORD", "avada2024")
GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_FALLBACK_MODEL = "llama-3.1-8b-instant"

# --- Clients ---
groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


def groq_create(**kwargs):
    """Call Groq API with automatic fallback to a secondary model on rate limit."""
    try:
        return groq_client.chat.completions.create(model=GROQ_MODEL, **kwargs)
    except Exception as e:
        err_str = str(e)
        if "429" in err_str or "rate_limit_exceeded" in err_str:
            # Fallback to lighter model
            return groq_client.chat.completions.create(model=GROQ_FALLBACK_MODEL, **kwargs)
        raise
supabase = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL and SUPABASE_KEY else None

# --- In-memory chat session store (avoids cookie size limit) ---
chat_sessions: dict[str, dict] = {}

# --- Personas by difficulty ---
PERSONAS_BY_DIFFICULTY = {
    "easy": [
        {"name": "Friendly Newbie", "tone": "polite, a bit confused, asks basic questions, appreciative when helped",
         "patience": "high", "tech_level": "low", "emoji_use": "sometimes"},
        {"name": "Detail-Oriented Merchant", "tone": "asks many follow-up questions, wants to understand why not just how, methodical",
         "patience": "high", "tech_level": "high", "emoji_use": "no"},
    ],
    "medium": [
        {"name": "Confused Non-Tech Merchant", "tone": "lost, doesn't understand technical terms, needs step-by-step hand-holding",
         "patience": "medium", "tech_level": "very low", "emoji_use": "sometimes"},
        {"name": "Price-Sensitive Merchant", "tone": "always asks about cost, compares with competitors, wants discounts",
         "patience": "medium", "tech_level": "medium", "emoji_use": "rarely"},
        {"name": "Non-Native English Speaker", "tone": "simple English, occasional grammar mistakes, may mix languages",
         "patience": "high", "tech_level": "low", "emoji_use": "often"},
    ],
    "hard": [
        {"name": "Frustrated Merchant", "tone": "annoyed, short messages, expects quick resolution, may threaten bad review",
         "patience": "low", "tech_level": "medium", "emoji_use": "rarely"},
        {"name": "Angry Complainer", "tone": "very upset, uses caps sometimes, blames the app, mentions losing money",
         "patience": "very low", "tech_level": "medium", "emoji_use": "no"},
        {"name": "Impatient Business Owner", "tone": "busy, wants instant answers, no small talk, short direct messages",
         "patience": "low", "tech_level": "high", "emoji_use": "no"},
    ],
}

INTENT_DIFFICULTY = {
    "howto": "easy", "presales": "easy", "integration": "easy",
    "bug_report": "medium", "billing": "medium", "feature_request": "medium", "common_issue": "medium",
    "complaint": "hard", "out_of_scope": "hard", "ambiguous": "hard", "multi_intent": "hard",
}

INTENT_CATEGORY = {
    "howto": "How-to", "presales": "Pre-sales", "integration": "Integration",
    "bug_report": "Bug Report", "billing": "Billing", "feature_request": "Feature Request",
    "complaint": "Complaint", "out_of_scope": "Edge Case", "common_issue": "Common Issue",
    "ambiguous": "Edge Case", "multi_intent": "Edge Case",
}

INTENT_HINTS = {
    "howto": "Guide them step by step. Use specific navigation paths.",
    "bug_report": "Ask for details first (store URL, screenshots). Then troubleshoot systematically.",
    "billing": "Understand the reason. Never approve refunds yourself — escalate to CSL.",
    "complaint": "Show empathy first! Acknowledge their frustration before troubleshooting.",
    "feature_request": "Acknowledge the request, log it, but don't promise it will be built.",
    "presales": "Highlight relevant features and plan options. Offer a demo call.",
    "common_issue": "Check the common issues guide for this topic.",
    "integration": "Confirm the integration exists, guide through setup steps.",
}

LIVECHAT_STEPS = [
    {"key": "greeting", "label": "Step 1: Greeting",
     "tip": 'Greet the customer and introduce yourself by name.'},
    {"key": "empathy", "label": "Step 2: Show Empathy",
     "tip": "Acknowledge the customer's situation before jumping to solutions."},
    {"key": "probing", "label": "Step 3: Probing",
     "tip": "Ask specific questions to understand the root issue. Don't assume."},
    {"key": "expectation", "label": "Step 4: Set Expectation",
     "tip": "Tell the customer what you'll do next and how long it might take."},
    {"key": "troubleshoot", "label": "Step 5: Troubleshoot",
     "tip": "Provide clear, step-by-step solution. Use screenshots/links if needed."},
    {"key": "followup", "label": "Step 6: Follow Up",
     "tip": "Confirm the issue is resolved. Ask the customer to verify."},
    {"key": "achieve_more", "label": "Step 7: Achieve More",
     "tip": "Offer additional help or suggest useful features proactively."},
    {"key": "farewell", "label": "Step 8: Farewell & Review",
     "tip": "Thank the customer and ask for a review. This step is mandatory!"},
]


# --- Load scenarios ---
def load_scenarios(app_name: str = "chatty") -> list[dict]:
    scenarios = []
    app_dir = DATA_DIR / app_name

    # From test-cases.yaml
    test_file = app_dir / "eval" / "test-cases.yaml"
    if test_file.exists():
        with open(test_file, encoding="utf-8") as f:
            cases = yaml.safe_load(f) or []
        for c in cases:
            intent = c.get("intent", "general")
            scenarios.append({
                "id": c.get("id", "unknown"),
                "intent": intent,
                "opening_message": c.get("input", ""),
                "tags": c.get("tags", []),
                "source": "test-cases",
                "difficulty": INTENT_DIFFICULTY.get(intent, "medium"),
                "category": INTENT_CATEGORY.get(intent, "Other"),
            })

    # From common-issues/*.md
    issues_dir = app_dir / "common-issues"
    if issues_dir.exists():
        for md_file in sorted(issues_dir.glob("*.md")):
            content = md_file.read_text(encoding="utf-8")
            blocks = content.split("---")
            for block in blocks:
                lines = block.strip().split("\n")
                questions = []
                answer_lines = []
                in_answer = False
                for line in lines:
                    if line.startswith("Q: "):
                        questions.append(line[3:].strip())
                        in_answer = False
                    elif line.startswith("A: "):
                        answer_lines.append(line[3:].strip())
                        in_answer = True
                    elif in_answer:
                        answer_lines.append(line)
                if questions:
                    scenarios.append({
                        "id": md_file.stem,
                        "intent": "common_issue",
                        "opening_message": random.choice(questions),
                        "tags": [md_file.stem],
                        "source": f"common-issues/{md_file.name}",
                        "reference_answer": "\n".join(answer_lines),
                        "difficulty": "medium",
                        "category": "Common Issue",
                    })

    return scenarios


def load_livechat_process() -> str:
    lc_file = DATA_DIR / "shared" / "livechat-process.md"
    if lc_file.exists():
        return lc_file.read_text(encoding="utf-8")
    return ""


# --- LLM Prompts ---
def build_customer_prompt(scenario: dict, persona: dict) -> str:
    reference = scenario.get("reference_answer", "")
    ref_section = ""
    if reference:
        ref_section = f"\n## Reference (what a good CS agent should do):\n{reference}\n"

    return f"""You are a simulated Shopify merchant contacting support via live chat.
You are role-playing as a customer for CS training purposes.

## Your Persona
- Type: {persona['name']}
- Tone: {persona['tone']}
- Patience level: {persona['patience']}
- Tech knowledge: {persona['tech_level']}
- Emoji usage: {persona['emoji_use']}

## Your Scenario
- Issue/Question: {scenario['opening_message']}
- Intent type: {scenario['intent']}
- Category: {', '.join(scenario.get('tags', []))}

## Your Store Context (make up realistic details as needed)
- You run a Shopify store (pick a realistic niche)
- You may or may not know your current plan
- You may have 50-500 products
{ref_section}
## Rules
1. Stay in character throughout.
2. Your issue is EXACTLY what is described in "Issue/Question" above — do NOT change the topic or intent.
3. Start with your opening message about that specific issue. Rephrase it naturally but keep the same topic.
4. React realistically to the CS agent's responses.
5. After 3-5 exchanges where the agent hasn't addressed your issue, escalate frustration.
6. Keep messages short (1-3 sentences). This is live chat, not email.
7. Do NOT reveal you are a bot.
8. Do NOT solve the issue yourself.
9. Emoji usage "{persona['emoji_use']}" means: "no"=never use emojis, "rarely"=max 1 emoji per 3 messages, "sometimes"=max 1 emoji per message, "often"=1-2 emojis per message max.
"""


def build_grading_prompt(livechat_process: str) -> str:
    return f"""You are a CS Training Evaluator for Avada Support team.

Evaluate the CS agent's performance in this practice live chat session.

## Grading Criteria (8-step live chat process):

{livechat_process}

## Scoring (0-10 for each):

1. **Communication** (0-10): Greeting, empathy, farewell — was the agent polite, warm, and professional in opening and closing the conversation? Did they acknowledge the customer's situation?
2. **Problem Understanding** (0-10): Did the agent ask the right questions to understand the root issue? Did they set clear expectations about next steps and handling time?
3. **Troubleshooting** (0-10): Was the solution correct, clear, step-by-step, and actionable? Did they guide the customer effectively?
4. **Product Knowledge** (0-10): SCORE THIS STRICTLY. Was the information about the app, features, settings, and plans accurate and specific? Did they reference correct feature names, navigation paths, and limitations? Deduct points for vague or generic answers.
5. **Language & Tone** (0-10): SCORE THIS STRICTLY. Grammar, spelling, punctuation correctness. Natural and professional writing style — not robotic, not overly casual. Appropriate tone for the situation.
6. **Response Quality** (0-10): SCORE THIS STRICTLY. Were responses concise, well-structured, and to the point? Did they avoid unnecessary filler? Were they easy for the customer to follow?
7. **Proactiveness** (0-10): Did the agent follow up to confirm resolution, offer additional help, or suggest useful features? Did they ask for a review?
8. **Process Compliance** (0-10): Did the agent follow CS process correctly? Did they escalate when needed instead of handling out of scope? Did they avoid making unauthorized promises (refunds, feature commitments)? Did they avoid sharing incorrect policies?

## IMPORTANT: Output format
At the END of your evaluation, add this exact line:
SCORES: communication=X, problem_understanding=X, troubleshooting=X, product_knowledge=X, language_tone=X, response_quality=X, proactiveness=X, process_compliance=X

## IMPORTANT: Context-aware scoring
Not every conversation requires all 8 steps to be perfect. Score based on what's appropriate for the specific scenario:
- A simple how-to question may not need deep empathy — don't penalize for that
- If the issue is resolved in 3 turns, skipping "Achieve More" is acceptable
- Focus on whether the agent resolved the customer's issue effectively
- Only penalize for steps that were clearly needed but missing

Overall: 9-10 Excellent, 7-8 Good, 5-6 Needs Work, <5 Re-train.

## MANDATORY Output Structure
You MUST output ALL 3 sections below in this EXACT order and format. Do NOT skip any section.

### Section 1: SCORES (one line, this exact format)
SCORES: communication=X, problem_understanding=X, troubleshooting=X, product_knowledge=X, language_tone=X, response_quality=X, proactiveness=X, process_compliance=X

### Section 2: TIPS (exactly 3 lines)
TIP_1: <first actionable improvement tip>
TIP_2: <second actionable improvement tip>
TIP_3: <third actionable improvement tip>

### Section 3: SUGGESTED better responses (one line per CS agent message)
SUGGESTED_1: <better version of agent's 1st message>
SUGGESTED_2: <better version of agent's 2nd message>
SUGGESTED_3: <better version of agent's 3rd message>
(continue for ALL agent messages in the conversation)

CRITICAL: You MUST include ALL 3 sections. Do NOT use bullet points or other formats — use the exact prefixes shown (SCORES:, TIP_1:, SUGGESTED_1: etc).
"""


def parse_scores(grading_text: str) -> dict:
    scores = {}
    match = re.search(r"SCORES:\s*(.+)", grading_text)
    if match:
        for pair in re.findall(r"(\w+)\s*=\s*(\d+(?:\.\d+)?)", match.group(1)):
            scores[pair[0]] = float(pair[1])
    else:
        for m in re.finditer(r"\*?\*?(\w[\w\s&]*?)\*?\*?\s*[\(:]?\s*(\d+(?:\.\d+)?)\s*/?\s*10", grading_text):
            key = m.group(1).strip().lower().replace(" ", "_").replace("&", "and")
            scores[key] = float(m.group(2))
    return scores


def parse_suggestions(grading_text: str) -> list[str]:
    """Parse SUGGESTED_N: lines from grading output."""
    suggestions = []
    for m in re.finditer(r"SUGGESTED[_\s]*\d+\s*[:\.]\s*(.+)", grading_text, re.IGNORECASE):
        text = m.group(1).strip().strip('"').strip("'")
        if text:
            suggestions.append(text)
    return suggestions


def parse_tips(grading_text: str) -> list[str]:
    """Parse TIP_N: lines from grading output."""
    tips = []
    for m in re.finditer(r"TIP[_\s]*\d+\s*[:\.]\s*(.+)", grading_text, re.IGNORECASE):
        text = m.group(1).strip().strip('"').strip("'")
        if text:
            tips.append(text)
    return tips


# --- Cache scenarios ---
_scenarios_cache = {}
_cache_ts = {}

def get_scenarios(app_name: str = "chatty") -> list[dict]:
    # Refresh cache every 60s to pick up new custom scenarios
    now = time.time()
    if app_name not in _scenarios_cache or now - _cache_ts.get(app_name, 0) > 60:
        base = load_scenarios(app_name)
        custom = load_custom_scenarios(app_name)
        _scenarios_cache[app_name] = base + custom
        _cache_ts[app_name] = now
    return _scenarios_cache[app_name]


def invalidate_cache(app_name: str = "chatty"):
    _scenarios_cache.pop(app_name, None)
    _cache_ts.pop(app_name, None)


def load_custom_scenarios(app_name: str = "chatty") -> list[dict]:
    """Load custom scenarios from Supabase."""
    if not supabase:
        return []
    try:
        data = supabase.table("custom_scenarios") \
            .select("*") \
            .eq("app_name", app_name) \
            .eq("active", True) \
            .order("created_at", desc=True) \
            .execute().data or []
        scenarios = []
        for row in data:
            scenarios.append({
                "id": f"custom_{row['id']}",
                "intent": row.get("intent", "general"),
                "opening_message": row.get("opening_message", ""),
                "tags": row.get("tags", []),
                "source": "custom",
                "difficulty": row.get("difficulty", "medium"),
                "category": row.get("category", "Other"),
                "reference_answer": row.get("reference_answer", ""),
            })
        return scenarios
    except Exception as e:
        print(f"Error loading custom scenarios: {e}")
        return []


# --- Product Knowledge for Generator ---
_product_knowledge_cache: str = ""

def load_product_knowledge(app_name: str = "chatty") -> str:
    global _product_knowledge_cache
    if _product_knowledge_cache:
        return _product_knowledge_cache
    pk_file = DATA_DIR / app_name / "product-knowledge.md"
    if pk_file.exists():
        _product_knowledge_cache = pk_file.read_text(encoding="utf-8")
    return _product_knowledge_cache


# --- Scenario Generation Prompt ---
def build_gen_prompt(topic: str, count: int, app_name: str, difficulty: str | None = None) -> str:
    diff_guide = ""
    if difficulty:
        diff_map = {
            "easy": "Simple how-to questions, presales inquiries. Customer is friendly and patient.",
            "medium": "Bug reports, billing questions, setup issues. Customer may be confused or price-sensitive.",
            "hard": "Angry complaints, edge cases, multi-intent issues. Customer is frustrated or impatient.",
        }
        diff_guide = f"\nDifficulty: {difficulty} — {diff_map.get(difficulty, '')}"

    product_knowledge = load_product_knowledge(app_name)
    pk_section = ""
    if product_knowledge:
        pk_section = f"""
## Product Knowledge (use this to create accurate scenarios)
{product_knowledge}
"""

    return f"""You are a CS training scenario generator for a Shopify app called {app_name.title()}.

Generate exactly {count} realistic customer support scenarios based on this topic: "{topic}"
{diff_guide}
{pk_section}

## Examples of good scenarios

Example 1 (easy — howto):
{{
  "intent": "howto",
  "opening_message": "Hi, I just installed Chatty and I'm trying to set up the AI assistant. Where do I start?",
  "difficulty": "easy",
  "category": "How-to",
  "tags": ["ai", "setup", "new_user"],
  "reference_answer": "Guide the merchant to AI Assistant section, help them add data sources (products auto-sync, add custom Q&As), configure AI instructions, and test using the built-in Test feature."
}}

Example 2 (medium — bug_report):
{{
  "intent": "bug_report",
  "opening_message": "The AI is showing $29.99 for a product that costs $39.99 on my French market domain. Customers are complaining about the wrong price.",
  "difficulty": "medium",
  "category": "Bug Report",
  "tags": ["ai", "pricing", "markets"],
  "reference_answer": "Check if Shopify Markets is set up and 'Sync Markets' is enabled in AI settings. Reproduce by visiting the market domain. If Markets configured correctly but issue persists, request staff access and escalate to dev team."
}}

Example 3 (hard — complaint):
{{
  "intent": "complaint",
  "opening_message": "I've been paying $68.99/month for Pro and the AI STILL gives wrong answers after 3 months. I've contacted support 4 times and nobody fixed it. I want a full refund NOW or I'm leaving a 1-star review.",
  "difficulty": "hard",
  "category": "Complaint",
  "tags": ["complaint", "refund", "ai", "sensitive"],
  "reference_answer": "Apologize sincerely, acknowledge the repeated frustration. Ask for specific chat IDs where AI was wrong. Review AI data sources and instructions. NEVER approve refund without CSL approval. Escalate to CS Leader with full context. Offer to personally follow up until resolved."
}}

## Output format

For each scenario, output EXACTLY this JSON format (as a JSON array):
[
  {{
    "intent": "howto|bug_report|billing|complaint|presales|feature_request|common_issue|out_of_scope|ambiguous|multi_intent",
    "opening_message": "The customer's first message (realistic, 1-3 sentences)",
    "difficulty": "easy|medium|hard",
    "category": "How-to|Bug Report|Billing|Complaint|Pre-sales|Feature Request|Common Issue|Edge Case|Integration",
    "tags": ["tag1", "tag2"],
    "reference_answer": "Brief guide for CS agent on how to handle this (2-4 sentences). Include specific steps, feature names, and when to escalate."
  }}
]

## Rules
- Make opening messages realistic — how a real Shopify merchant would type in live chat (casual, sometimes with typos or urgency)
- Vary the tone based on difficulty (easy=friendly/curious, medium=confused/concerned, hard=angry/frustrated/threatening)
- Use REAL feature names, plan names, and pricing from the product knowledge above
- Include specific details: error messages, feature paths (e.g., "AI Assistant > Data Source"), plan names (Free/Basic/Pro/Plus), pricing ($19.99/$68.99/$199.99)
- reference_answer must include actionable steps for CS agents, mention specific tools (DevZone, shortcuts), and note when to escalate
- Do NOT create generic scenarios — each must reference a specific Chatty feature or workflow
- For billing scenarios: mention real plan prices and limits
- For bug reports: include realistic symptoms the merchant would describe
- For complaints: include emotional language and specific grievances
- Return ONLY valid JSON array, no markdown or extra text
"""


# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.json
    name = data.get("name", "").strip()
    role = data.get("role", "agent")
    password = data.get("password", "")
    restore = data.get("restore", False)

    if not name:
        return jsonify({"error": "Name required"}), 400
    # Skip password check on session restore (user already authenticated before)
    if role == "leader" and not restore and password != LEADER_PASSWORD:
        return jsonify({"error": "Wrong password"}), 403

    session["agent_name"] = name
    session["user_role"] = role
    return jsonify({"ok": True, "name": name, "role": role})


@app.route("/api/scenarios")
def api_scenarios():
    app_name = request.args.get("app", "chatty")
    scenarios = get_scenarios(app_name)
    # Return without reference_answer (keep it server-side)
    safe = []
    for s in scenarios:
        safe.append({
            "id": s["id"],
            "intent": s["intent"],
            "opening_message": s["opening_message"],
            "tags": s.get("tags", []),
            "difficulty": s.get("difficulty", "medium"),
            "category": s.get("category", "Other"),
        })
    return jsonify(safe)


@app.route("/api/session/start", methods=["POST"])
def api_start_session():
    """Start a new chat session. Returns opening customer message."""
    data = request.json
    app_name = data.get("app", "chatty")
    scenario_id = data.get("scenario_id")
    difficulty = data.get("difficulty", "medium")

    scenarios = get_scenarios(app_name)

    # Find scenario
    if scenario_id:
        scenario = next((s for s in scenarios if s["id"] == scenario_id), None)
        if not scenario:
            return jsonify({"error": "Scenario not found"}), 404
    else:
        # Random from difficulty
        filtered = [s for s in scenarios if s.get("difficulty") == difficulty]
        if not filtered:
            filtered = scenarios
        scenario = random.choice(filtered)

    # Pick persona
    diff_key = scenario.get("difficulty", "medium")
    personas = PERSONAS_BY_DIFFICULTY.get(diff_key, PERSONAS_BY_DIFFICULTY["medium"])
    persona = random.choice(personas)

    # Build customer prompt
    customer_prompt = build_customer_prompt(scenario, persona)

    # Get opening message from LLM
    opening = scenario["opening_message"]
    if groq_client:
        try:
            response = groq_create(
                messages=[
                    {"role": "system", "content": customer_prompt},
                    {"role": "user", "content": f"Start the conversation. Send your opening message as the customer about this specific issue: '{scenario['opening_message']}'. Keep it short (1-2 sentences). Do NOT change the topic."},
                ],
                temperature=0.8,
                max_tokens=256,
            )
            opening = response.choices[0].message.content or opening
        except Exception:
            pass

    # Store session data in memory
    session_id = f"{int(time.time())}_{random.randint(1000,9999)}"
    chat_sessions[session_id] = {
        "scenario": scenario,
        "persona": persona,
        "customer_prompt": customer_prompt,
        "history": [{"role": "assistant", "content": opening}],
        "turn_count": 0,
        "started_at": time.time(),
    }

    return jsonify({
        "session_id": session_id,
        "opening_message": opening,
        "scenario": {
            "id": scenario["id"],
            "intent": scenario["intent"],
            "difficulty": scenario.get("difficulty", "medium"),
            "category": scenario.get("category", "Other"),
            "opening_message": scenario["opening_message"],
        },
        "persona": {"name": persona["name"]},
        "guided_steps": LIVECHAT_STEPS,
    })


@app.route("/api/session/message", methods=["POST"])
def api_send_message():
    """Send agent message, get customer reply."""
    data = request.json
    session_id = data.get("session_id")
    agent_message = data.get("message", "").strip()

    sess = chat_sessions.get(session_id)
    if not sess:
        return jsonify({"error": "Session not found"}), 404
    if not agent_message:
        return jsonify({"error": "Empty message"}), 400

    # Update history
    sess["history"].append({"role": "user", "content": agent_message})
    sess["turn_count"] += 1

    # Get customer response
    customer_reply = "Sorry, can you say that again?"
    if groq_client:
        try:
            turn_hint = ""
            if sess["turn_count"] >= 8:
                turn_hint = "\n(The conversation has been going for a while. If the issue seems resolved, start wrapping up.)"

            messages = [{"role": "system", "content": sess["customer_prompt"] + turn_hint}]
            messages.extend(sess["history"])

            response = groq_create(
                messages=messages,
                temperature=0.7,
                max_tokens=256,
            )
            customer_reply = response.choices[0].message.content or customer_reply
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "rate_limit_exceeded" in err_str:
                customer_reply = "Xin lỗi, hệ thống đang bận. Vui lòng thử lại sau ít phút nhé!"
            else:
                customer_reply = "Xin lỗi, có lỗi kết nối. Vui lòng thử lại!"

    sess["history"].append({"role": "assistant", "content": customer_reply})

    # Detect customer satisfaction signals
    satisfaction_keywords = [
        "thank", "thanks", "that works", "that helped", "solved", "perfect",
        "great", "awesome", "got it", "understood", "appreciate", "you're the best",
        "issue is resolved", "working now", "fixed", "no more questions",
        "that's all", "nothing else", "all good", "no problem now",
    ]
    reply_lower = customer_reply.lower()
    customer_satisfied = any(kw in reply_lower for kw in satisfaction_keywords)

    # Max turns limit
    max_turns = 15
    force_end = sess["turn_count"] >= max_turns

    # Guided step hint
    turn = sess["turn_count"]
    guided_step = min(turn, len(LIVECHAT_STEPS) - 1)
    if turn <= 1:
        guided_step = 1
    elif turn == 2:
        guided_step = 2
    elif turn == 3:
        guided_step = 3
    elif turn <= 5:
        guided_step = 4
    elif turn == 6:
        guided_step = 5
    elif turn == 7:
        guided_step = 6
    elif turn >= 8:
        guided_step = 7

    return jsonify({
        "customer_reply": customer_reply,
        "turn_count": sess["turn_count"],
        "guided_step": guided_step,
        "customer_satisfied": customer_satisfied,
        "force_end": force_end,
    })


@app.route("/api/session/end", methods=["POST"])
def api_end_session():
    """End session and grade the conversation."""
    data = request.json
    session_id = data.get("session_id")
    agent_name = data.get("agent_name", session.get("agent_name", "Anonymous"))

    sess = chat_sessions.get(session_id)
    if not sess:
        return jsonify({"error": "Session not found"}), 404

    scenario = sess["scenario"]
    persona = sess["persona"]

    # Build conversation text
    conversation_text = ""
    messages_for_save = []
    for msg in sess["history"]:
        role = "Customer" if msg["role"] == "assistant" else "CS Agent"
        conversation_text += f"{role}: {msg['content']}\n\n"
        messages_for_save.append({
            "role": "customer" if msg["role"] == "assistant" else "agent",
            "content": msg["content"],
        })

    # Grade
    livechat_process = load_livechat_process()
    grading_prompt = build_grading_prompt(livechat_process)
    grading_text = "Grading unavailable."

    if groq_client:
        try:
            response = groq_create(
                messages=[
                    {"role": "system", "content": grading_prompt},
                    {"role": "user", "content": (
                        f"## Conversation to evaluate:\n\n{conversation_text}\n\n"
                        f"## Scenario context:\n- Intent: {scenario['intent']}\n"
                        f"- Tags: {', '.join(scenario.get('tags', []))}\n"
                        f"- Customer persona: {persona['name']} ({persona['tone']})"
                    )},
                ],
                temperature=0.3,
                max_tokens=4096,
            )
            grading_text = response.choices[0].message.content or grading_text
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "rate_limit_exceeded" in err_str:
                grading_text = "Chấm điểm tạm thời không khả dụng do giới hạn API. Vui lòng thử lại sau ít phút!"
            else:
                grading_text = f"Grading error: {e}"

    scores = parse_scores(grading_text)
    suggestions = parse_suggestions(grading_text)
    tips = parse_tips(grading_text)
    overall = round(sum(scores.values()) / len(scores), 1) if scores else 0

    # Save to Supabase
    if supabase:
        try:
            row = {
                "agent_name": agent_name,
                "scenario_id": scenario["id"],
                "intent": scenario["intent"],
                "category": scenario.get("category", "Other"),
                "difficulty": scenario.get("difficulty", "medium"),
                "persona": persona["name"],
                "turns": sess["turn_count"],
                "grader": "groq",
                "score_greeting": scores.get("communication"),
                "score_empathy": scores.get("problem_understanding"),
                "score_probing": scores.get("troubleshooting"),
                "score_expectation": scores.get("product_knowledge"),
                "score_troubleshoot": scores.get("language_tone"),
                "score_followup": scores.get("response_quality"),
                "score_achieve_more": scores.get("proactiveness"),
                "score_farewell": scores.get("process_compliance"),
                "score_tone": None,
                "score_quality": None,
                "overall_score": overall,
                "conversation": messages_for_save,
                "feedback": grading_text,
            }
            supabase.table("training_results").insert(row).execute()
        except Exception as e:
            print(f"Supabase save error: {e}")

    # Clean up session
    chat_sessions.pop(session_id, None)

    return jsonify({
        "grading_text": grading_text,
        "scores": scores,
        "overall": overall,
        "turns": sess["turn_count"],
        "conversation": messages_for_save,
        "suggestions": suggestions,
        "tips": tips,
    })


@app.route("/api/session/hint", methods=["POST"])
def api_hint():
    data = request.json
    session_id = data.get("session_id")
    sess = chat_sessions.get(session_id)
    if not sess:
        return jsonify({"hint": "Follow the 8-step livechat process."})
    intent = sess["scenario"]["intent"]
    hint = INTENT_HINTS.get(intent, "Follow the 8-step livechat process. Start with greeting and empathy.")
    return jsonify({"hint": hint, "tags": sess["scenario"].get("tags", [])})


@app.route("/api/results")
def api_results():
    """Get training results. Leaders see all, agents see own."""
    if not supabase:
        return jsonify([])

    agent_name = request.args.get("agent")
    role = session.get("user_role", "agent")

    try:
        query = supabase.table("training_results").select("*").order("created_at", desc=True).limit(200)
        if role != "leader" and agent_name:
            query = query.eq("agent_name", agent_name)
        data = query.execute().data or []

        # Column-to-criteria mapping (reusing existing DB columns)
        col_to_criteria = {
            "greeting": "communication",
            "empathy": "problem_understanding",
            "probing": "troubleshooting",
            "expectation": "product_knowledge",
            "troubleshoot": "language_tone",
            "followup": "response_quality",
            "achieve_more": "proactiveness",
            "farewell": "process_compliance",
        }
        results = []
        for row in data:
            scores = {}
            for col, criteria_key in col_to_criteria.items():
                val = row.get(f"score_{col}")
                if val is not None:
                    scores[criteria_key] = val
            results.append({
                "timestamp": row.get("created_at", ""),
                "agent": row.get("agent_name", "Anonymous"),
                "scenario_id": row.get("scenario_id", ""),
                "intent": row.get("intent", ""),
                "category": row.get("category", ""),
                "difficulty": row.get("difficulty", ""),
                "persona": row.get("persona", ""),
                "turns": row.get("turns", 0),
                "scores": scores,
                "overall": row.get("overall_score", 0),
                "conversation": row.get("conversation", []),
                "feedback": row.get("feedback", ""),
            })
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/guided-steps")
def api_guided_steps():
    return jsonify(LIVECHAT_STEPS)


# ------------------------------------------------------------------
# SCENARIO GENERATOR (Leader only)
# ------------------------------------------------------------------

@app.route("/api/scenarios/generate", methods=["POST"])
def api_generate_scenarios():
    """Generate scenarios using AI. Leader only."""
    if session.get("user_role") != "leader":
        return jsonify({"error": "Leader access required"}), 403
    if not groq_client:
        return jsonify({"error": "Groq API not configured"}), 500

    data = request.json
    topic = data.get("topic", "").strip()
    count = min(int(data.get("count", 5)), 20)  # Max 20 at a time
    difficulty = data.get("difficulty")  # optional filter
    app_name = data.get("app", "chatty")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    prompt = build_gen_prompt(topic, count, app_name, difficulty)

    try:
        response = groq_create(
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Generate {count} scenarios about: {topic}"},
            ],
            temperature=0.8,
            max_tokens=4096,
        )
        raw = response.choices[0].message.content or "[]"

        # Extract JSON from response (handle markdown code blocks)
        json_match = re.search(r'\[[\s\S]*\]', raw)
        if json_match:
            scenarios = json.loads(json_match.group())
        else:
            return jsonify({"error": "Failed to parse AI response", "raw": raw}), 500

        # Validate and clean
        valid = []
        for s in scenarios:
            if not s.get("opening_message"):
                continue
            valid.append({
                "intent": s.get("intent", "general"),
                "opening_message": s["opening_message"],
                "difficulty": s.get("difficulty", "medium"),
                "category": s.get("category", "Other"),
                "tags": s.get("tags", []),
                "reference_answer": s.get("reference_answer", ""),
            })

        return jsonify({"scenarios": valid})

    except json.JSONDecodeError:
        return jsonify({"error": "AI returned invalid JSON", "raw": raw}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/scenarios/save", methods=["POST"])
def api_save_scenarios():
    """Save generated scenarios to Supabase. Leader only."""
    if session.get("user_role") != "leader":
        return jsonify({"error": "Leader access required"}), 403
    if not supabase:
        return jsonify({"error": "Supabase not configured"}), 500

    data = request.json
    scenarios = data.get("scenarios", [])
    app_name = data.get("app", "chatty")
    created_by = session.get("agent_name", "unknown")

    saved = 0
    for s in scenarios:
        if not s.get("opening_message"):
            continue
        try:
            row = {
                "app_name": app_name,
                "scenario_id": f"gen_{int(time.time())}_{random.randint(100,999)}",
                "intent": s.get("intent", "general"),
                "opening_message": s["opening_message"],
                "difficulty": s.get("difficulty", "medium"),
                "category": s.get("category", "Other"),
                "tags": s.get("tags", []),
                "reference_answer": s.get("reference_answer", ""),
                "created_by": created_by,
            }
            supabase.table("custom_scenarios").insert(row).execute()
            saved += 1
        except Exception as e:
            print(f"Save scenario error: {e}")

    invalidate_cache(app_name)
    return jsonify({"saved": saved})


@app.route("/api/scenarios/custom")
def api_list_custom():
    """List custom scenarios. Leader only."""
    if session.get("user_role") != "leader":
        return jsonify({"error": "Leader access required"}), 403
    if not supabase:
        return jsonify([])

    app_name = request.args.get("app", "chatty")
    try:
        data = supabase.table("custom_scenarios") \
            .select("*") \
            .eq("app_name", app_name) \
            .order("created_at", desc=True) \
            .execute().data or []
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/scenarios/custom/<int:scenario_id>", methods=["DELETE"])
def api_delete_custom(scenario_id):
    """Delete a custom scenario. Leader only."""
    if session.get("user_role") != "leader":
        return jsonify({"error": "Leader access required"}), 403
    if not supabase:
        return jsonify({"error": "Supabase not configured"}), 500

    try:
        supabase.table("custom_scenarios").delete().eq("id", scenario_id).execute()
        invalidate_cache()
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/scenarios/custom/<int:scenario_id>/toggle", methods=["POST"])
def api_toggle_custom(scenario_id):
    """Toggle active/inactive for a custom scenario. Leader only."""
    if session.get("user_role") != "leader":
        return jsonify({"error": "Leader access required"}), 403
    if not supabase:
        return jsonify({"error": "Supabase not configured"}), 500

    data = request.json
    active = data.get("active", True)
    try:
        supabase.table("custom_scenarios").update({"active": active}).eq("id", scenario_id).execute()
        invalidate_cache()
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/scenarios/from-transcript", methods=["POST"])
def api_scenarios_from_transcript():
    """Generate scenarios from a Crisp chat transcript. Leader only."""
    if session.get("user_role") != "leader":
        return jsonify({"error": "Leader access required"}), 403
    if not groq_client:
        return jsonify({"error": "Groq API not configured"}), 500

    data = request.json
    transcript = (data.get("transcript") or "").strip()
    count = min(int(data.get("count", 3)), 10)
    app_name = data.get("app", "chatty")

    if not transcript:
        return jsonify({"error": "Transcript is required"}), 400

    product_knowledge = ""
    pk_file = DATA_DIR / app_name / "product-knowledge.md"
    if pk_file.exists():
        product_knowledge = pk_file.read_text(encoding="utf-8")[:3000]

    pk_section = f"\n## Product Knowledge:\n{product_knowledge}\n" if product_knowledge else ""

    prompt = f"""You are a CS training scenario generator for a Shopify app called {app_name.title()}.
Analyze the following real customer support transcript and generate {count} training scenarios inspired by it.
Extract the core issues, customer type, and tone from the transcript to create realistic practice scenarios.
{pk_section}
## Output format — return ONLY a JSON array:
[
  {{
    "intent": "howto|bug_report|billing|complaint|presales|feature_request|common_issue",
    "opening_message": "The customer's first message (realistic, 1-3 sentences)",
    "difficulty": "easy|medium|hard",
    "category": "How-to|Bug Report|Billing|Complaint|Pre-sales|Feature Request|Common Issue",
    "tags": ["tag1", "tag2"],
    "reference_answer": "What a good CS agent should do (2-4 sentences)"
  }}
]

Rules:
- Base scenarios on the real issues found in the transcript
- Vary difficulty and phrasing — don't copy verbatim from transcript
- reference_answer must be actionable for a CS agent
- Return ONLY valid JSON array, no markdown or extra text"""

    try:
        response = groq_create(
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Here is the transcript:\n\n{transcript}\n\nGenerate {count} scenarios from this."},
            ],
            temperature=0.7,
            max_tokens=4096,
        )
        raw = response.choices[0].message.content or "[]"
        json_match = re.search(r'\[[\s\S]*\]', raw)
        if not json_match:
            return jsonify({"error": "Failed to parse AI response", "raw": raw}), 500

        scenarios = json.loads(json_match.group())
        valid = []
        for s in scenarios:
            if not s.get("opening_message"):
                continue
            valid.append({
                "intent": s.get("intent", "general"),
                "opening_message": s["opening_message"],
                "difficulty": s.get("difficulty", "medium"),
                "category": s.get("category", "Other"),
                "tags": s.get("tags", []),
                "reference_answer": s.get("reference_answer", ""),
            })
        return jsonify({"scenarios": valid})

    except json.JSONDecodeError:
        return jsonify({"error": "AI returned invalid JSON", "raw": raw}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/dashboard/feedback", methods=["POST"])
def api_dashboard_feedback():
    """Generate AI performance feedback from session results."""
    role = session.get("user_role", "agent")
    data = request.json
    agent_filter = data.get("agent")  # None = all agents (leader only)
    app_name = data.get("app", "chatty")

    # Agents can only get their own feedback
    if role != "leader":
        agent_filter = session.get("agent_name")
        if not agent_filter:
            return jsonify({"error": "Not logged in"}), 403

    if not groq_client:
        return jsonify({"error": "Groq API not configured"}), 500
    if not supabase:
        return jsonify({"error": "Supabase not configured"}), 500

    try:
        query = supabase.table("training_results").select("*").order("created_at", desc=True).limit(100)
        if agent_filter:
            query = query.eq("agent_name", agent_filter)
        rows = query.execute().data or []
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if not rows:
        return jsonify({"error": "No session data found"}), 404

    # Summarize data for the prompt
    col_map = {
        "score_greeting": "Communication",
        "score_empathy": "Problem Understanding",
        "score_probing": "Troubleshooting",
        "score_expectation": "Product Knowledge",
        "score_troubleshoot": "Language & Tone",
        "score_followup": "Response Quality",
        "score_achieve_more": "Proactiveness",
        "score_farewell": "Process Compliance",
    }
    criteria_totals = {v: [] for v in col_map.values()}
    overall_scores = []
    agents_seen = set()
    categories_seen = []

    for row in rows:
        if row.get("overall_score"):
            overall_scores.append(row["overall_score"])
        if row.get("agent_name"):
            agents_seen.add(row["agent_name"])
        if row.get("category"):
            categories_seen.append(row["category"])
        for col, label in col_map.items():
            v = row.get(col)
            if v is not None:
                criteria_totals[label].append(v)

    criteria_avgs = {k: (sum(v)/len(v) if v else None) for k, v in criteria_totals.items()}
    overall_avg = sum(overall_scores)/len(overall_scores) if overall_scores else None

    sorted_criteria = sorted([(k, v) for k, v in criteria_avgs.items() if v is not None], key=lambda x: x[1])
    weakest = sorted_criteria[:3]
    strongest = sorted_criteria[-2:]

    summary = f"""Sessions analyzed: {len(rows)}
Overall average score: {overall_avg:.1f}/10 if overall_avg else 'N/A'
Agents: {', '.join(sorted(agents_seen)) if not agent_filter else agent_filter}
Common categories: {', '.join(set(categories_seen[:20]))}

Criteria averages:
""" + "\n".join(f"- {k}: {v:.1f}/10" for k, v in sorted_criteria)

    scope = f"agent '{agent_filter}'" if agent_filter else "all agents combined"
    is_leader_all = role == "leader" and not agent_filter

    prompt = f"""You are a CS team performance coach reviewing training simulator results for {scope}.

Here is the performance summary:
{summary}

Write a detailed, actionable performance feedback report. Structure it as:
1. **Overall Assessment** (2-3 sentences on general performance level)
2. **Strengths** (top performing areas with specific praise)
3. **Areas for Improvement** (weakest areas with concrete, specific coaching tips)
4. **Action Plan** (3-5 bullet points of specific things to practice or focus on)
{"5. **Team Patterns** (cross-agent observations, consistency notes)" if is_leader_all else ""}

Tone: direct, coaching, constructive. Use specific score numbers. Max 400 words."""

    try:
        response = groq_create(
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Generate the feedback report now."},
            ],
            temperature=0.5,
            max_tokens=1024,
        )
        feedback_text = response.choices[0].message.content or ""
        return jsonify({"feedback": feedback_text, "sessions": len(rows), "scope": scope})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("DEBUG", "0") == "1")
