# Aleksandr Borisov — AI Solutions Builder (visiting card)

A tiny, self-contained prototype I built to go with my application for the **AI Solutions Builder** role at SmartCat. It shows — rather than tells — how I turn business problems into working AI tools.

**▶ Live demo:** `https://<your-github-username>.github.io/smartcat-visiting-card/`
*(fill in after publishing — steps below)*

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

---

## How to publish (≈3 minutes)

1. Create a new **public** repo on GitHub named `smartcat-visiting-card`.
2. Upload the three files in this folder (`index.html`, `agent_demo.py`, `README.md`) — either drag-and-drop in the GitHub web UI, or:
   ```bash
   git init
   git add index.html agent_demo.py README.md
   git commit -m "AI Solutions Builder visiting card"
   git branch -M main
   git remote add origin https://github.com/<your-username>/smartcat-visiting-card.git
   git push -u origin main
   ```
3. In the repo: **Settings → Pages → Source: `main` / root → Save.**
4. Wait ~1 minute; your live link is `https://<your-username>.github.io/smartcat-visiting-card/`.
5. Paste that link into the "Live demo" line above and into your application / cover letter.

> Note: publishing requires signing in to your own GitHub account, so that last step is yours to do — everything here is ready to upload as-is.
