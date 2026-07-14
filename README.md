# Aleksandr Borisov — AI Solutions Builder (visiting card)

A tiny, self-contained prototype I built to go with my application for the **AI Solutions Builder** role at SmartCat. It shows — rather than tells — how I turn business problems into working AI tools.

**▶ Live demo:** ` https://aleksandrborisovds.github.io/smartcat-visiting-card/`


## What's inside

- **`index.html`** — a one-page interactive card that runs entirely in the browser (no server, no API key):
  - **Supplier & Cost Engine** — pick a priority (lowest price / fastest delivery), quantity and a client target price; it selects the optimal supplier and computes final cost, route, ETA, and margin. This is the same selection logic I shipped in production at EDELWEISS (order processing 2 weeks → 30 min, margin +~80%), reimplemented client-side.
  - **Ops Question Router** — type a business question; a transparent rule-based router classifies intent and drafts the tool-chain an AI agent would run. Swap the rules for an LLM and each step becomes an executed action.
- **`agent_demo.py`** — a runnable "executive decision-support agent" pattern in ~150 lines. Runs with **zero setup** (rules mode) and automatically uses an LLM if `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` is set.

```bash
py agent_demo.py "Which suppliers are hurting our margin this quarter?"
py agent_demo.py            # interactive
```

## Why it maps to the role
The brief asks for someone who builds AI-powered internal tools for **sales-pipeline analysis, operational reporting, and executive decision support**, end-to-end, in the Office of the CEO. These two mini-tools are honest, miniature versions of exactly that — and I've shipped their full-scale counterparts (a voice agent, an order-automation engine, and an AI contract reviewer) solo, from scratch.

## Tech
Vanilla HTML/CSS/JS (no build step, GitHub-Pages-ready) · Python 3 (standard library only for rules mode).

## Contact
✉ aleandr.g@gmail.com · ✈ Telegram [@Aleksandr_G_Borisov](https://t.me/Aleksandr_G_Borisov) · 💻 [GitHub](https://github.com/AleksandrBorisovDS/projects_yandex_practicum) · Russian (native) / English (B2) / Spanish (B1) · full remote (UTC−3)


