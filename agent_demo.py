#!/usr/bin/env python3
"""
agent_demo.py — a tiny "executive decision-support agent" pattern.

Same idea as the tools on the visiting-card page, but in code:
an ambiguous business question comes in, the agent (1) classifies intent,
(2) picks the right internal tool, (3) drafts the step plan that tool would
run, and (4) — if an LLM key is present — asks the model to sharpen the plan.

Design goals it demonstrates:
  * Translate a fuzzy business problem into a concrete, tool-chained plan.
  * Keep AI where it helps and rules where they're more reliable.
  * Run with ZERO setup (rules mode) and light up with an LLM if available.

Run:
    py agent_demo.py "Which suppliers are hurting our margin this quarter?"
    py agent_demo.py                       # interactive mode
Optional LLM mode (auto-detected):
    set ANTHROPIC_API_KEY=...   (or OPENAI_API_KEY=...)   then run as above.

No dependencies required for rules mode.
"""
import os
import sys
import textwrap

# --- The internal "tools" this agent can route to (intent -> plan) ----------
TOOLS = {
    "margin": ("Margin & Unit-Economics agent", [
        "Pull orders + costs from CRM/ERP",
        "Compute per-order and per-supplier margin",
        "Rank margin leakage by supplier / SKU",
        "Draft an exec summary with the 3 biggest levers",
    ]),
    "contract": ("Contract-review agent", [
        "Ingest the contract",
        "Extract clauses and compare to our policy",
        "Produce a concede / negotiate / never-accept table",
        "Flag deal-breakers for sign-off",
    ]),
    "forecast": ("Forecasting agent", [
        "Assemble the historical time series",
        "Fit a seasonality-aware forecast",
        "Attach confidence bands",
        "Surface the assumptions worth challenging",
    ]),
    "pipeline": ("Pipeline / voice agent", [
        "Segment warm leads by intent",
        "Auto-call or auto-message the top segment",
        "Interpret replies and update the deal stage in CRM",
        "Report connect and conversion rates",
    ]),
    "competitor": ("Competitive-intelligence agent", [
        "Fire automated RFQs / collect competitor offers",
        "Compute market min / avg / max price",
        "Position us versus the market",
        "Recommend a discount-policy move",
    ]),
    "cash": ("Treasury / cash agent", [
        "Aggregate AR / AP and due dates",
        "Project the 13-week cash runway",
        "Flag overdue receivables",
        "Propose a payment-priority plan",
    ]),
}

# Keyword -> intent. Simple, transparent, and easy to extend.
KEYWORDS = {
    "margin": ["margin", "profit", "unit econom", "profitab"],
    "contract": ["contract", "legal", "terms", "clause"],
    "forecast": ["forecast", "predict", "demand", "trend", "next month", "next quarter"],
    "pipeline": ["lead", "pipeline", "call", "sales", "conversion", "outreach"],
    "competitor": ["competitor", "market price", "benchmark", "rival"],
    "cash": ["cash", "liquidity", "receivab", "payab", "treasury", "runway"],
}

FALLBACK = ("General decision-support agent", [
    "Clarify the decision and the precision it actually needs",
    "Gather the minimal data to answer it",
    "Compute the answer plus one sanity check",
    "Return a recommendation, not just a chart",
])


def classify(question: str):
    q = question.lower()
    for intent, words in KEYWORDS.items():
        if any(w in q for w in words):
            return intent
    return None


def plan(question: str):
    intent = classify(question)
    tool, steps = TOOLS.get(intent, FALLBACK)
    return intent, tool, steps


def maybe_llm_refine(question: str, tool: str, steps: list):
    """If an LLM key is present, ask it to tighten the plan. Otherwise skip."""
    prompt = (
        "You are an executive decision-support agent. A stakeholder asked:\n"
        f'  "{question}"\n\n'
        f"The routed tool is: {tool}\n"
        "Draft plan:\n" + "\n".join(f"  - {s}" for s in steps) +
        "\n\nReturn a tighter 4-step plan and name the single most important number to compute."
    )
    # Anthropic
    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            import anthropic
            client = anthropic.Anthropic()
            msg = client.messages.create(
                model="claude-sonnet-5", max_tokens=400,
                messages=[{"role": "user", "content": prompt}])
            return msg.content[0].text
        except Exception as e:
            return f"(LLM refine skipped: {e})"
    # OpenAI
    if os.getenv("OPENAI_API_KEY"):
        try:
            from openai import OpenAI
            client = OpenAI()
            r = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}])
            return r.choices[0].message.content
        except Exception as e:
            return f"(LLM refine skipped: {e})"
    return None


def answer(question: str):
    intent, tool, steps = plan(question)
    print("\n" + "=" * 60)
    print(f"Q: {question}")
    print("=" * 60)
    print(f"Intent   : {intent or 'general (fallback)'}")
    print(f"Routed to: {tool}\n")
    print("Plan the agent would run:")
    for i, s in enumerate(steps, 1):
        print(f"  {i}. {s}")
    refined = maybe_llm_refine(question, tool, steps)
    if refined:
        print("\nLLM-refined plan:")
        print(textwrap.indent(refined.strip(), "  "))
    else:
        print("\n(Tip: set ANTHROPIC_API_KEY or OPENAI_API_KEY to let an LLM sharpen the plan.)")


def main():
    if len(sys.argv) > 1:
        answer(" ".join(sys.argv[1:]))
        return
    print("Executive decision-support agent — type a question (blank to quit).")
    print("Examples: 'why is our margin down?', 'forecast Q3 demand', 'review this contract'")
    while True:
        try:
            q = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not q:
            break
        answer(q)


if __name__ == "__main__":
    main()
