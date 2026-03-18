"""
Customer Simulator — Web UI (Streamlit) for CS Live Chat Training (Chatty)

Setup:
1. pip install streamlit groq anthropic pyyaml pandas
2. export GROQ_API_KEY="your-key"
3. Optional: export ANTHROPIC_API_KEY="your-key" (for Claude grading)
4. streamlit run web_simulator.py

Features:
- Difficulty levels (Easy / Medium / Hard) with scenario categories
- Guided Mode — step-by-step coaching for new CS agents
- Scenario preview before starting + retry same scenario
- Agent name tracking for individual performance
- Response timer — tracks how fast you reply
- Dashboard: leaderboard, export CSV, filter by time, score trends
- Grading via Groq (free) or Claude (better quality)
- Results saved to JSON for persistence
"""

import os
import io
import json
import random
import re
import time
import yaml
import datetime
import streamlit as st
import pandas as pd
from pathlib import Path
from groq import Groq

# --- Config ---
BASE_DIR = Path(__file__).resolve().parent.parent  # app-chatty/
SHARED_DIR = BASE_DIR.parent / "shared"
RESULTS_DIR = BASE_DIR / "scripts" / "results"
def _get_secret(key: str) -> str:
    """Read from Streamlit secrets first, then env var."""
    try:
        return st.secrets[key]
    except Exception:
        return os.environ.get(key, "")

GROQ_API_KEY = _get_secret("GROQ_API_KEY")
ANTHROPIC_API_KEY = _get_secret("ANTHROPIC_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"
CLAUDE_MODEL = "claude-sonnet-4-20250514"

# --- 8-step livechat checklist (for Guided Mode) ---
LIVECHAT_STEPS = [
    {"key": "greeting", "label": "Step 1: Greeting",
     "tip": "Greet the customer and introduce yourself by name.\n\n> \"Hi [Name], this is [Your Name] from Avada Support. Thanks for reaching out!\""},
    {"key": "empathy", "label": "Step 2: Show Empathy",
     "tip": "Acknowledge the customer's situation before jumping to solutions.\n\n> \"I totally understand how frustrating this must be. Let's get this sorted out for you.\""},
    {"key": "probing", "label": "Step 3: Probing",
     "tip": "Ask specific questions to understand the root issue. Don't assume!\n\n> \"Could you share more details? When did this start? What page were you on?\""},
    {"key": "expectation", "label": "Step 4: Set Expectation",
     "tip": "Tell the customer what you'll do next and how long it might take.\n\n> \"Let me check this for you. It might take 2-3 minutes. Thanks for your patience!\""},
    {"key": "troubleshoot", "label": "Step 5: Troubleshoot",
     "tip": "Provide clear, step-by-step instructions. Use specific navigation paths.\n\n> \"Please go to Chatty Dashboard > AI Assistant > Data Sources and check if...\""},
    {"key": "followup", "label": "Step 6: Follow Up",
     "tip": "Confirm whether the issue is resolved. Ask them to double-check.\n\n> \"I've just updated the settings. Could you refresh and check if it works now?\""},
    {"key": "achieve_more", "label": "Step 7: Achieve More",
     "tip": "Offer additional help or suggest useful features they haven't tried.\n\n> \"By the way, have you tried our AI Smart Recommendations? It could help boost sales!\""},
    {"key": "farewell", "label": "Step 8: Farewell & Review",
     "tip": "Thank the customer and ask for a review. **This step is mandatory!**\n\n> \"Thank you for your time! If you're happy with the support, we'd really appreciate a quick review!\""},
]

# --- Difficulty & Category Definitions ---

PERSONAS_BY_DIFFICULTY = {
    "Easy": [
        {
            "name": "Friendly Newbie",
            "tone": "polite, a bit confused, asks basic questions, appreciative when helped",
            "patience": "high", "tech_level": "low", "emoji_use": "sometimes",
        },
        {
            "name": "Detail-Oriented Merchant",
            "tone": "asks many follow-up questions, wants to understand why not just how, methodical",
            "patience": "high", "tech_level": "high", "emoji_use": "no",
        },
    ],
    "Medium": [
        {
            "name": "Confused Non-Tech Merchant",
            "tone": "lost, doesn't understand technical terms, needs step-by-step hand-holding, asks 'what do you mean?' often",
            "patience": "medium", "tech_level": "very low", "emoji_use": "sometimes",
        },
        {
            "name": "Price-Sensitive Merchant",
            "tone": "always asks about cost, compares with competitors, wants discounts, hesitant to upgrade",
            "patience": "medium", "tech_level": "medium", "emoji_use": "rarely",
        },
        {
            "name": "Non-Native English Speaker",
            "tone": "simple English, occasional grammar mistakes, may mix languages, asks for clarification",
            "patience": "high", "tech_level": "low", "emoji_use": "often",
        },
    ],
    "Hard": [
        {
            "name": "Frustrated Merchant",
            "tone": "annoyed, short messages, expects quick resolution, may threaten to leave a bad review",
            "patience": "low", "tech_level": "medium", "emoji_use": "rarely",
        },
        {
            "name": "Angry Complainer",
            "tone": "very upset, uses caps sometimes, blames the app, mentions losing money/customers",
            "patience": "very low", "tech_level": "medium", "emoji_use": "no",
        },
        {
            "name": "Impatient Business Owner",
            "tone": "busy, wants instant answers, no small talk, sends short direct messages",
            "patience": "low", "tech_level": "high", "emoji_use": "no",
        },
    ],
}

INTENT_DIFFICULTY = {
    "howto": "Easy", "presales": "Easy", "integration": "Easy",
    "bug_report": "Medium", "billing": "Medium", "feature_request": "Medium", "common_issue": "Medium",
    "complaint": "Hard", "out_of_scope": "Hard", "ambiguous": "Hard", "multi_intent": "Hard",
}

INTENT_CATEGORY = {
    "howto": "How-to Questions", "presales": "Pre-sales", "integration": "Integration",
    "bug_report": "Bug Reports", "billing": "Billing", "feature_request": "Feature Requests",
    "common_issue": "Common Issues", "complaint": "Complaints", "out_of_scope": "Out of Scope",
    "ambiguous": "Edge Cases", "multi_intent": "Edge Cases",
}

INTENT_HINTS = {
    "howto": "Guide them step by step. Use specific navigation paths like 'Go to AI Assistant > ...'",
    "bug_report": "Ask for details first (store URL, screenshots). Then troubleshoot systematically.",
    "billing": "Understand the reason. Never approve refunds yourself — escalate to CSL.",
    "complaint": "Show empathy first! Acknowledge their frustration before troubleshooting.",
    "feature_request": "Acknowledge the request, log it, but don't promise it will be built.",
    "presales": "Highlight relevant features and plan options. Offer a demo call.",
    "common_issue": "Check the common issues guide for this topic.",
    "out_of_scope": "Politely redirect to the right team/product.",
    "ambiguous": "Ask clarifying questions. Don't assume what they need.",
    "multi_intent": "Address each question separately. Prioritize the urgent one.",
}


# --- Load scenarios ---
def load_scenarios() -> list[dict]:
    scenarios = []

    # From test-cases.yaml
    test_file = BASE_DIR / "eval" / "test-cases.yaml"
    if test_file.exists():
        with open(test_file, encoding="utf-8") as f:
            cases = yaml.safe_load(f)
        if cases:
            for c in cases:
                intent = c.get("intent", "general")
                scenarios.append({
                    "id": c.get("id", "unknown"),
                    "intent": intent,
                    "opening_message": c.get("input", ""),
                    "tags": c.get("tags", []),
                    "source": "test-cases",
                    "difficulty": INTENT_DIFFICULTY.get(intent, "Medium"),
                    "category": INTENT_CATEGORY.get(intent, "Other"),
                })

    # From common-issues/ markdown files
    issues_dir = BASE_DIR / "support-flow" / "common-issues"
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
                        "difficulty": "Medium",
                        "category": "Common Issues",
                    })

    return scenarios


# --- Load livechat process ---
def load_livechat_process() -> str:
    lc_file = SHARED_DIR / "support-flow" / "cs-process" / "livechat-process.md"
    if lc_file.exists():
        return lc_file.read_text(encoding="utf-8")
    return ""


# --- Build prompts ---
def build_customer_prompt(scenario: dict, persona: dict) -> str:
    reference = scenario.get("reference_answer", "")
    ref_section = ""
    if reference:
        ref_section = f"""
## Reference (what a good CS agent should do — use this to judge responses):
{reference}
"""

    return f"""You are a simulated Shopify merchant contacting Chatty app support via live chat.
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
- You run a Shopify store (pick a realistic niche: fashion, beauty, electronics, home decor, pet supplies, etc.)
- You may or may not know your current Chatty plan
- You may have 50-500 products

## Rules
1. Stay in character as the customer throughout the conversation.
2. Start with your opening message about your issue. Rephrase it naturally — don't copy it word-for-word.
3. React realistically to the CS agent's responses:
   - If they ask good probing questions → provide details gradually, don't dump everything at once.
   - If they give unclear instructions → ask for clarification (based on your tech level).
   - If they use jargon and you're non-technical → say you don't understand.
   - If they take too long or give generic answers → show impatience (based on your patience level).
   - If they solve your issue → show appropriate gratitude (based on your persona).
4. After 3-5 exchanges where the agent hasn't addressed your issue, escalate your frustration naturally.
5. If asked for store URL, screenshots, etc. → provide made-up but realistic info.
6. Keep messages short and natural (1-3 sentences typically). This is live chat, not email.
7. Do NOT reveal that you are a bot or break character.
8. Do NOT solve the issue yourself — let the CS agent guide you.
{ref_section}
## Important
- If the CS agent does something really well (empathy, probing, clear steps), subtly react positively.
- If the CS agent skips greeting, doesn't show empathy, or gives robotic responses, react accordingly.
- You can introduce small complications mid-conversation (e.g., "oh wait, I also noticed that..." or "actually I tried that but...").
"""


def build_grading_prompt(livechat_process: str) -> str:
    return f"""You are a CS Training Evaluator for Avada Support team.

Evaluate the CS agent's performance in this practice live chat session.

## Grading Criteria (based on Avada's 8-step live chat process):

{livechat_process}

## Scoring (0-10 for each, then overall):

1. **Greeting** (0-10): Did they greet properly and introduce themselves?
2. **Empathy** (0-10): Did they acknowledge the customer's situation?
3. **Probing** (0-10): Did they ask good questions to understand the root issue?
4. **Set Expectation** (0-10): Did they inform about next steps / handling time?
5. **Troubleshoot** (0-10): Was the solution correct, clear, and actionable?
6. **Follow-up** (0-10): Did they confirm resolution and check if it worked?
7. **Achieve More** (0-10): Did they offer additional help or suggest features?
8. **Farewell & Review** (0-10): Did they thank and ask for review?

Also evaluate:
9. **Tone & Professionalism** (0-10): Friendly, professional, appropriate?
10. **Response Quality** (0-10): Clear, concise, accurate information?

## Output Format

IMPORTANT: You MUST start your response with EXACTLY this line (with actual numbers):
SCORES: greeting=X, empathy=X, probing=X, expectation=X, troubleshoot=X, followup=X, achieve_more=X, farewell=X, tone=X, quality=X

Then give specific feedback for each criterion, and an overall summary with strengths and areas to improve. Be specific — quote exact messages where possible.

Overall score = average of all 10 criteria.
- 9-10: Excellent — ready for live chat
- 7-8: Good — minor improvements needed
- 5-6: Needs work — review training materials
- Below 5: Significant improvement needed — re-train

End with 3 specific, actionable tips for improvement.
"""


# --- API calls ---
def get_groq_client():
    return Groq(api_key=GROQ_API_KEY)


def _call_groq(client, system_prompt: str, messages: list, temperature: float = 0.7, max_tokens: int = 256) -> str:
    try:
        full_messages = [{"role": "system", "content": system_prompt}] + messages
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=full_messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content or ""
    except Exception as e:
        error_str = str(e)
        if "rate_limit" in error_str.lower() or "429" in error_str:
            return "⚠️ Rate limit — vui lòng đợi vài giây rồi thử lại."
        return f"⚠️ API error: {e}"


def get_opening_message(client, customer_prompt: str, fallback: str) -> str:
    result = _call_groq(
        client,
        system_prompt=customer_prompt,
        messages=[{"role": "user", "content": "Start the conversation. Send your opening message as the customer."}],
        temperature=0.8,
    )
    return result or fallback


def get_customer_response(client, history: list, customer_prompt: str, turn_count: int) -> str:
    turn_hint = ""
    if turn_count >= 8:
        turn_hint = "\n(The conversation has been going for a while. If the issue seems resolved, you can start wrapping up — express satisfaction or ask a final question.)"
    result = _call_groq(
        client,
        system_prompt=customer_prompt + turn_hint,
        messages=history,
        temperature=0.7,
    )
    return result or "..."


def grade_with_groq(client, conversation_text: str, grading_prompt: str, scenario: dict, persona: dict) -> str:
    return _call_groq(
        client,
        system_prompt=grading_prompt,
        messages=[{
            "role": "user",
            "content": (
                f"## Conversation to evaluate:\n\n{conversation_text}\n\n"
                f"## Scenario context:\n- Intent: {scenario['intent']}\n"
                f"- Tags: {', '.join(scenario.get('tags', []))}\n"
                f"- Customer persona: {persona['name']} ({persona['tone']})"
            ),
        }],
        temperature=0.3,
        max_tokens=2048,
    ) or "Grading failed."


def grade_with_claude(conversation_text: str, grading_prompt: str, scenario: dict, persona: dict) -> str:
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        response = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=2048,
            system=grading_prompt,
            messages=[{
                "role": "user",
                "content": (
                    f"## Conversation to evaluate:\n\n{conversation_text}\n\n"
                    f"## Scenario context:\n- Intent: {scenario['intent']}\n"
                    f"- Tags: {', '.join(scenario.get('tags', []))}\n"
                    f"- Customer persona: {persona['name']} ({persona['tone']})"
                ),
            }],
        )
        return response.content[0].text
    except ImportError:
        return "Error: `anthropic` package not installed. Run: pip install anthropic"
    except Exception as e:
        return f"Claude grading error: {e}"


# --- Results persistence ---
def _results_file() -> Path:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    return RESULTS_DIR / "training_results.json"


def load_results() -> list[dict]:
    f = _results_file()
    if f.exists():
        try:
            return json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, ValueError):
            return []
    return []


def save_result(entry: dict):
    results = load_results()
    results.append(entry)
    _results_file().write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")


def parse_scores(grading_text: str) -> dict:
    """Extract scores from grading output."""
    scores = {}
    match = re.search(r"SCORES:\s*(.+)", grading_text)
    if match:
        pairs = match.group(1)
        for pair in re.findall(r"(\w+)\s*=\s*(\d+(?:\.\d+)?)", pairs):
            scores[pair[0]] = float(pair[1])
    else:
        for m in re.finditer(r"\*?\*?(\w[\w\s&]*?)\*?\*?\s*[\(:]?\s*(\d+(?:\.\d+)?)\s*/?\s*10", grading_text):
            key = m.group(1).strip().lower().replace(" ", "_").replace("&", "and")
            scores[key] = float(m.group(2))
    return scores


# --- Streamlit UI ---
def init_session_state():
    if "scenarios" not in st.session_state:
        st.session_state.scenarios = load_scenarios()
    if "livechat_process" not in st.session_state:
        st.session_state.livechat_process = load_livechat_process()
    if "groq_client" not in st.session_state:
        st.session_state.groq_client = get_groq_client() if GROQ_API_KEY else None
    defaults = {
        "messages": [],
        "history": [],
        "scenario": None,
        "persona": None,
        "customer_prompt": "",
        "turn_count": 0,
        "session_active": False,
        "grading_result": None,
        "agent_name": "",
        "guided_mode": True,
        "guided_step": 0,
        "response_times": [],       # list of float (seconds per reply)
        "last_customer_time": None,  # timestamp when customer last messaged
        "last_scenario_key": None,   # for retry: (difficulty, category, scenario_id)
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def start_session_with_scenario(scenario: dict, difficulty: str):
    """Start session with a specific scenario."""
    personas = PERSONAS_BY_DIFFICULTY.get(difficulty, PERSONAS_BY_DIFFICULTY["Medium"])
    persona = random.choice(personas)

    st.session_state.scenario = scenario
    st.session_state.persona = persona
    st.session_state.customer_prompt = build_customer_prompt(scenario, persona)
    st.session_state.messages = []
    st.session_state.history = []
    st.session_state.turn_count = 0
    st.session_state.grading_result = None
    st.session_state.session_active = True
    st.session_state.guided_step = 0
    st.session_state.response_times = []
    st.session_state.last_customer_time = None
    st.session_state.last_scenario_key = (difficulty, scenario["id"])

    opening = get_opening_message(
        st.session_state.groq_client,
        st.session_state.customer_prompt,
        scenario["opening_message"],
    )

    st.session_state.messages.append({"role": "customer", "content": opening})
    st.session_state.history.append({"role": "assistant", "content": opening})
    st.session_state.last_customer_time = time.time()


def start_new_session(difficulty: str, category: str | None):
    """Start a new training session with selected difficulty + optional category."""
    scenarios = st.session_state.scenarios
    filtered = [s for s in scenarios if s.get("difficulty") == difficulty]
    if category and category != "All":
        filtered = [s for s in filtered if s.get("category") == category]
    if not filtered:
        filtered = [s for s in scenarios if s.get("difficulty") == difficulty]
    if not filtered:
        filtered = scenarios

    scenario = random.choice(filtered)
    start_session_with_scenario(scenario, difficulty)


def retry_session():
    """Retry the same scenario with a new persona."""
    if st.session_state.last_scenario_key:
        difficulty, scenario_id = st.session_state.last_scenario_key
        scenario = next(
            (s for s in st.session_state.scenarios if s["id"] == scenario_id),
            None,
        )
        if scenario:
            start_session_with_scenario(scenario, difficulty)
            return
    st.warning("No previous scenario to retry.")


def end_session(grader: str = "groq"):
    conversation_text = ""
    for msg in st.session_state.messages:
        role = "Customer" if msg["role"] == "customer" else "CS Agent"
        conversation_text += f"{role}: {msg['content']}\n\n"

    grading_prompt = build_grading_prompt(st.session_state.livechat_process)

    if grader == "claude" and ANTHROPIC_API_KEY:
        result = grade_with_claude(
            conversation_text, grading_prompt,
            st.session_state.scenario, st.session_state.persona,
        )
    else:
        result = grade_with_groq(
            st.session_state.groq_client,
            conversation_text, grading_prompt,
            st.session_state.scenario, st.session_state.persona,
        )

    st.session_state.grading_result = result
    st.session_state.session_active = False

    scores = parse_scores(result)
    overall = round(sum(scores.values()) / len(scores), 1) if scores else 0

    # Compute response time stats
    rt = st.session_state.response_times
    avg_rt = round(sum(rt) / len(rt), 1) if rt else 0
    max_rt = round(max(rt), 1) if rt else 0

    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "agent": st.session_state.agent_name or "Anonymous",
        "scenario_id": st.session_state.scenario["id"],
        "intent": st.session_state.scenario["intent"],
        "category": st.session_state.scenario.get("category", "Other"),
        "difficulty": st.session_state.scenario.get("difficulty", "Medium"),
        "persona": st.session_state.persona["name"],
        "turns": st.session_state.turn_count,
        "grader": grader,
        "scores": scores,
        "overall": overall,
        "avg_response_time": avg_rt,
        "max_response_time": max_rt,
        "conversation": st.session_state.messages,
    }
    save_result(entry)


# ------------------------------------------------------------------
# PAGE: Practice
# ------------------------------------------------------------------

def page_practice():
    st.title("💬 Chatty — CS Live Chat Training")
    st.caption("Practice handling customer conversations with AI-simulated merchants")

    if not GROQ_API_KEY:
        st.error("Missing `GROQ_API_KEY` environment variable.")
        st.code("export GROQ_API_KEY='your-key'\nstreamlit run web_simulator.py")
        return

    # --- Sidebar ---
    with st.sidebar:
        st.header("Agent")
        st.session_state.agent_name = st.text_input(
            "Your name", value=st.session_state.agent_name, placeholder="e.g. Linh"
        )

        st.divider()
        st.header("New Session")

        difficulty = st.radio(
            "Difficulty", ["Easy", "Medium", "Hard"], horizontal=True,
            help=(
                "**Easy**: Friendly customers, how-to & presales\n\n"
                "**Medium**: Confused/price-sensitive, bugs & billing\n\n"
                "**Hard**: Angry/impatient, complaints & edge cases"
            ),
        )

        all_scenarios = st.session_state.scenarios
        categories_for_diff = sorted(set(
            s.get("category", "Other")
            for s in all_scenarios if s.get("difficulty") == difficulty
        ))
        category = st.selectbox("Category", ["All"] + categories_for_diff)

        count = len([
            s for s in all_scenarios
            if s.get("difficulty") == difficulty and (category == "All" or s.get("category") == category)
        ])
        st.caption(f"{count} scenarios available")

        # Guided mode toggle
        st.session_state.guided_mode = st.toggle("Guided Mode (for new CS)", value=st.session_state.guided_mode)

        # --- Scenario preview ---
        preview_scenarios = [
            s for s in all_scenarios
            if s.get("difficulty") == difficulty and (category == "All" or s.get("category") == category)
        ]
        if preview_scenarios:
            with st.expander("Preview scenarios"):
                for s in preview_scenarios[:10]:
                    diff_emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}.get(s.get("difficulty"), "⚪")
                    st.markdown(f"{diff_emoji} **{s['intent']}** — _{s['opening_message'][:80]}..._")
                    if st.button(f"Start this one", key=f"preview_{s['id']}", use_container_width=True):
                        start_session_with_scenario(s, difficulty)
                        st.rerun()
                if len(preview_scenarios) > 10:
                    st.caption(f"... and {len(preview_scenarios) - 10} more")

        if st.button("🎲 Random Scenario", use_container_width=True, type="primary"):
            start_new_session(difficulty, category)
            st.rerun()

        # Active session controls
        if st.session_state.session_active:
            st.divider()
            st.subheader("Session Actions")

            grader = st.radio(
                "Grader", ["groq", "claude"],
                format_func=lambda x: "🤖 Groq (free)" if x == "groq" else "🧠 Claude (better)",
                horizontal=True,
            )
            if grader == "claude" and not ANTHROPIC_API_KEY:
                st.warning("Set `ANTHROPIC_API_KEY` for Claude grading.")

            if st.button("📝 End & Get Score", use_container_width=True):
                end_session(grader)
                st.rerun()

            if st.button("⏭️ Skip Scenario", use_container_width=True):
                start_new_session(difficulty, category)
                st.rerun()

            if st.button("💡 Hint", use_container_width=True):
                intent = st.session_state.scenario["intent"]
                st.info(INTENT_HINTS.get(intent, "Follow the 8-step livechat process."))

        # Retry button (after session ends)
        if st.session_state.grading_result and st.session_state.last_scenario_key:
            st.divider()
            if st.button("🔄 Retry Same Scenario", use_container_width=True):
                retry_session()
                st.rerun()

        # Current session info
        if st.session_state.scenario:
            st.divider()
            st.subheader("Current Session")
            diff = st.session_state.scenario.get("difficulty", "?")
            diff_emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}.get(diff, "⚪")
            st.markdown(f"**Difficulty:** {diff_emoji} {diff}")
            st.markdown(f"**Category:** {st.session_state.scenario.get('category', '?')}")
            st.markdown(f"**Customer:** {st.session_state.persona['name']}")
            st.markdown(f"**Turns:** {st.session_state.turn_count}")

            # Response time display
            if st.session_state.response_times:
                avg_rt = sum(st.session_state.response_times) / len(st.session_state.response_times)
                st.markdown(f"**Avg response:** {avg_rt:.0f}s")

    # --- Main chat area ---
    if not st.session_state.session_active and not st.session_state.grading_result:
        st.markdown("""
### How it works
1. Enter your **name** in the sidebar
2. Choose **difficulty** and **category**
3. **Preview** specific scenarios or click **🎲 Random Scenario**
4. Respond as a CS agent in the chat
5. Click **📝 End & Get Score** to get your evaluation

### Difficulty Levels

| Level | Customer Type | Scenario Type |
|-------|--------------|---------------|
| 🟢 Easy | Friendly, patient | How-to, presales |
| 🟡 Medium | Confused, price-sensitive | Bugs, billing, common issues |
| 🔴 Hard | Angry, impatient | Complaints, edge cases |

### Tips
- Toggle **Guided Mode** for step-by-step coaching
- Use **💡 Hint** if you're stuck
- Use **🔄 Retry** to improve your score on the same scenario
- Check **📊 Dashboard** to track your progress
        """)
        return

    # --- Guided mode: step tracker ---
    if st.session_state.guided_mode and st.session_state.session_active:
        step_idx = st.session_state.guided_step
        if step_idx < len(LIVECHAT_STEPS):
            current_step = LIVECHAT_STEPS[step_idx]
            st.info(f"**{current_step['label']}**\n\n{current_step['tip']}")
        else:
            st.success("All 8 steps covered! You can **End & Get Score** now, or keep chatting.")

    # --- Response timer banner ---
    if st.session_state.session_active and st.session_state.last_customer_time:
        elapsed = time.time() - st.session_state.last_customer_time
        if elapsed > 60:
            st.warning(f"⏱️ Customer waiting for {elapsed:.0f}s — try to reply within 30-60 seconds!")
        elif elapsed > 30:
            st.caption(f"⏱️ {elapsed:.0f}s since customer's last message")

    # Display chat messages
    for msg in st.session_state.messages:
        if msg["role"] == "customer":
            with st.chat_message("user", avatar="👤"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant", avatar="💬"):
                st.markdown(msg["content"])

    # Display grading result
    if st.session_state.grading_result:
        st.divider()
        st.subheader("📝 Session Evaluation")
        st.markdown(st.session_state.grading_result)

        scores = parse_scores(st.session_state.grading_result)
        if scores:
            overall = round(sum(scores.values()) / len(scores), 1)
            st.divider()
            label_map = {
                "greeting": "Greeting", "empathy": "Empathy", "probing": "Probing",
                "expectation": "Expectation", "troubleshoot": "Troubleshoot",
                "followup": "Follow-up", "achieve_more": "Achieve More",
                "farewell": "Farewell", "tone": "Tone", "quality": "Quality",
            }
            cols = st.columns(5)
            for i, (key, val) in enumerate(scores.items()):
                label = label_map.get(key, key.replace("_", " ").title())
                cols[i % 5].metric(label, f"{val}/10")
            st.metric("Overall Score", f"{overall}/10")

        # Response time summary
        rt = st.session_state.response_times
        if rt:
            st.divider()
            st.subheader("⏱️ Response Time")
            rc1, rc2, rc3 = st.columns(3)
            rc1.metric("Average", f"{sum(rt)/len(rt):.0f}s")
            rc2.metric("Fastest", f"{min(rt):.0f}s")
            rc3.metric("Slowest", f"{max(rt):.0f}s")
            if sum(rt) / len(rt) <= 30:
                st.success("Great speed! Your average response time is under 30 seconds.")
            elif sum(rt) / len(rt) <= 60:
                st.info("Good speed. Aim for under 30 seconds for better customer experience.")
            else:
                st.warning("Try to respond faster — customers expect replies within 30-60 seconds in live chat.")
        return

    # Chat input
    if st.session_state.session_active:
        if agent_input := st.chat_input("Type your response as CS agent..."):
            # Track response time
            if st.session_state.last_customer_time:
                rt = time.time() - st.session_state.last_customer_time
                st.session_state.response_times.append(rt)

            st.session_state.messages.append({"role": "agent", "content": agent_input})
            st.session_state.history.append({"role": "user", "content": agent_input})
            st.session_state.turn_count += 1

            # Advance guided step based on turn count
            if st.session_state.guided_mode:
                # Simple heuristic: advance step roughly with conversation flow
                turn = st.session_state.turn_count
                if turn <= 1:
                    st.session_state.guided_step = 1  # After greeting → empathy
                elif turn == 2:
                    st.session_state.guided_step = 2  # → probing
                elif turn == 3:
                    st.session_state.guided_step = 3  # → expectation
                elif turn <= 5:
                    st.session_state.guided_step = 4  # → troubleshoot
                elif turn == 6:
                    st.session_state.guided_step = 5  # → follow-up
                elif turn == 7:
                    st.session_state.guided_step = 6  # → achieve more
                elif turn >= 8:
                    st.session_state.guided_step = 7  # → farewell

            # Get customer response
            customer_reply = get_customer_response(
                st.session_state.groq_client,
                st.session_state.history,
                st.session_state.customer_prompt,
                st.session_state.turn_count,
            )

            st.session_state.messages.append({"role": "customer", "content": customer_reply})
            st.session_state.history.append({"role": "assistant", "content": customer_reply})
            st.session_state.last_customer_time = time.time()
            st.rerun()


# ------------------------------------------------------------------
# PAGE: Dashboard
# ------------------------------------------------------------------

def page_dashboard():
    st.title("📊 Training Dashboard")

    results = load_results()

    if not results:
        st.info("No training sessions yet. Go to **💬 Practice** to start!")
        return

    # --- Sidebar filters ---
    with st.sidebar:
        st.header("Filters")

        agents = sorted(set(r.get("agent", "Anonymous") for r in results))
        selected_agent = st.selectbox("Agent", ["All"] + agents)

        difficulties = sorted(set(r.get("difficulty", "?") for r in results))
        selected_diff = st.selectbox("Difficulty", ["All"] + difficulties)

        # Time filter
        time_filter = st.selectbox("Time Period", ["All Time", "Today", "This Week", "This Month"])

    # Apply filters
    filtered = results
    if selected_agent != "All":
        filtered = [r for r in filtered if r.get("agent") == selected_agent]
    if selected_diff != "All":
        filtered = [r for r in filtered if r.get("difficulty") == selected_diff]

    now = datetime.datetime.now()
    if time_filter == "Today":
        cutoff = now.replace(hour=0, minute=0, second=0, microsecond=0)
        filtered = [r for r in filtered if _parse_ts(r) and _parse_ts(r) >= cutoff]
    elif time_filter == "This Week":
        cutoff = now - datetime.timedelta(days=now.weekday())
        cutoff = cutoff.replace(hour=0, minute=0, second=0, microsecond=0)
        filtered = [r for r in filtered if _parse_ts(r) and _parse_ts(r) >= cutoff]
    elif time_filter == "This Month":
        cutoff = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        filtered = [r for r in filtered if _parse_ts(r) and _parse_ts(r) >= cutoff]

    if not filtered:
        st.warning("No results match your filters.")
        return

    # --- Summary metrics ---
    st.subheader("Summary")
    total = len(filtered)
    scores_with_data = [r for r in filtered if r.get("overall", 0) > 0]
    avg_overall = round(sum(r["overall"] for r in scores_with_data) / len(scores_with_data), 1) if scores_with_data else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sessions", total)
    col2.metric("Avg Score", f"{avg_overall}/10")

    if avg_overall >= 9:
        level = "🌟 Excellent"
    elif avg_overall >= 7:
        level = "✅ Good"
    elif avg_overall >= 5:
        level = "⚠️ Needs Work"
    else:
        level = "🔴 Re-train"
    col3.metric("Level", level)

    avg_rt_list = [r.get("avg_response_time", 0) for r in filtered if r.get("avg_response_time")]
    avg_rt = round(sum(avg_rt_list) / len(avg_rt_list), 0) if avg_rt_list else 0
    col4.metric("Avg Response Time", f"{avg_rt}s")

    # --- Leaderboard ---
    if len(agents) > 1 or selected_agent == "All":
        st.divider()
        st.subheader("🏆 Leaderboard")

        leaderboard = {}
        for r in filtered:
            agent = r.get("agent", "Anonymous")
            if agent not in leaderboard:
                leaderboard[agent] = {"sessions": 0, "total_score": 0, "scored_sessions": 0}
            leaderboard[agent]["sessions"] += 1
            if r.get("overall", 0) > 0:
                leaderboard[agent]["total_score"] += r["overall"]
                leaderboard[agent]["scored_sessions"] += 1

        lb_rows = []
        for agent, data in leaderboard.items():
            avg = round(data["total_score"] / data["scored_sessions"], 1) if data["scored_sessions"] > 0 else 0
            lb_rows.append({
                "Agent": agent,
                "Sessions": data["sessions"],
                "Avg Score": avg,
            })

        lb_df = pd.DataFrame(lb_rows).sort_values("Avg Score", ascending=False).reset_index(drop=True)
        lb_df.index = lb_df.index + 1  # rank starts at 1
        lb_df.index.name = "Rank"

        # Add medal emoji
        medals = {1: "🥇", 2: "🥈", 3: "🥉"}
        lb_df.insert(0, "", [medals.get(i, "") for i in lb_df.index])

        st.dataframe(lb_df, use_container_width=True)

    # --- Score breakdown ---
    if scores_with_data:
        st.divider()
        st.subheader("Score Breakdown (Average)")

        criteria_keys = ["greeting", "empathy", "probing", "expectation", "troubleshoot",
                         "followup", "achieve_more", "farewell", "tone", "quality"]
        criteria_labels = ["Greeting", "Empathy", "Probing", "Expectation", "Troubleshoot",
                           "Follow-up", "Achieve More", "Farewell", "Tone", "Quality"]

        avg_scores = {}
        for key in criteria_keys:
            vals = [r["scores"].get(key, 0) for r in scores_with_data if r.get("scores")]
            avg_scores[key] = round(sum(vals) / len(vals), 1) if vals else 0

        chart_data = {criteria_labels[i]: avg_scores[criteria_keys[i]] for i in range(len(criteria_keys))}
        st.bar_chart(chart_data)

        if avg_scores:
            weakest = sorted(avg_scores.items(), key=lambda x: x[1])[:3]
            st.markdown("**Areas to improve:**")
            for key, val in weakest:
                label = criteria_labels[criteria_keys.index(key)] if key in criteria_keys else key
                st.markdown(f"- {label}: **{val}/10**")

    # --- Score trend ---
    if len(scores_with_data) >= 2:
        st.divider()
        st.subheader("Score Trend")
        trend_data = []
        for r in scores_with_data:
            ts = _parse_ts(r)
            if ts:
                trend_data.append({"date": ts, "score": r["overall"]})
        if trend_data:
            df = pd.DataFrame(trend_data).set_index("date")
            st.line_chart(df)

    # --- Export CSV ---
    st.divider()
    st.subheader("Export")

    export_rows = []
    for r in filtered:
        row = {
            "Timestamp": r.get("timestamp", ""),
            "Agent": r.get("agent", ""),
            "Difficulty": r.get("difficulty", ""),
            "Category": r.get("category", ""),
            "Intent": r.get("intent", ""),
            "Persona": r.get("persona", ""),
            "Turns": r.get("turns", 0),
            "Overall Score": r.get("overall", 0),
            "Avg Response Time (s)": r.get("avg_response_time", 0),
            "Grader": r.get("grader", ""),
        }
        # Add individual score columns
        scores = r.get("scores", {})
        for key in ["greeting", "empathy", "probing", "expectation", "troubleshoot",
                     "followup", "achieve_more", "farewell", "tone", "quality"]:
            row[key.replace("_", " ").title()] = scores.get(key, "")
        export_rows.append(row)

    export_df = pd.DataFrame(export_rows)
    csv_buffer = io.StringIO()
    export_df.to_csv(csv_buffer, index=False)

    st.download_button(
        label="📥 Download CSV",
        data=csv_buffer.getvalue(),
        file_name=f"cs_training_results_{datetime.datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv",
        use_container_width=True,
    )

    # --- Session history ---
    st.divider()
    st.subheader("Session History")

    for i, r in enumerate(reversed(filtered)):
        ts_display = ""
        ts = _parse_ts(r)
        if ts:
            ts_display = ts.strftime("%Y-%m-%d %H:%M")
        else:
            ts_display = r.get("timestamp", "?")

        diff_emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}.get(r.get("difficulty", ""), "⚪")
        overall = r.get("overall", 0)
        avg_rt_val = r.get("avg_response_time", 0)

        with st.expander(
            f"{ts_display} | {diff_emoji} {r.get('difficulty', '?')} | "
            f"{r.get('category', '?')} | {r.get('persona', '?')} | "
            f"Score: {overall}/10 | {avg_rt_val}s avg | {r.get('agent', '?')}"
        ):
            conversation = r.get("conversation", [])
            if conversation:
                for msg in conversation:
                    role_label = "👤 Customer" if msg["role"] == "customer" else "💬 CS Agent"
                    st.markdown(f"**{role_label}:** {msg['content']}")
            else:
                st.caption("(Conversation not saved)")

            scores = r.get("scores", {})
            if scores:
                st.markdown("---")
                st.markdown("**Scores:** " + " | ".join(f"{k}: {v}" for k, v in scores.items()))


def _parse_ts(r: dict):
    """Parse timestamp from result entry."""
    try:
        return datetime.datetime.fromisoformat(r["timestamp"])
    except (KeyError, ValueError, TypeError):
        return None


# --- Main ---
def main():
    st.set_page_config(
        page_title="Chatty — CS Training",
        page_icon="💬",
        layout="wide",
    )

    init_session_state()

    page = st.sidebar.radio(
        "Navigation",
        ["💬 Practice", "📊 Dashboard"],
        label_visibility="collapsed",
    )

    if page == "💬 Practice":
        page_practice()
    elif page == "📊 Dashboard":
        page_dashboard()


if __name__ == "__main__":
    main()
