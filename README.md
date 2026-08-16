# Coding Lounge

Nine hands-on stations recapping classes 1–13: the OpenAI API, agents,
tools, MCP, `AGENTS.md`, `SKILL.md`, and opencode. Built for coders aged
7–12, one lounge at a time.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env        # macOS/Linux: cp .env.example .env
```

Open `.env` and paste in a real `OPENAI_API_KEY`. Never commit `.env`,
never paste a key into chat or code — `.gitignore` already excludes it.

## Deploy the interface

The static site in `interface/` is configured as a Cloudflare Workers
assets-only project. Install dependencies and preview it locally:

```bash
npm install
npm run dev
```

For Cloudflare Builds, leave **Build command** empty, use
`npx wrangler deploy` as the **Deploy command**, and use `/` as the path.
The deployment reads `wrangler.jsonc` and publishes only `interface/`.

## The map

| # | Lounge | Tier | Uses |
|---|---|---|---|
| 1 | [First Contact](lounge-01-first-contact/) | Warm-up | OpenAI API |
| 2 | [Give It a Personality](lounge-02-give-it-a-personality/) | Warm-up | OpenAI API |
| 3 | [Write the Rulebook](lounge-03-write-the-rulebook/) | Core build | AGENTS.md |
| 4 | [Teach It a Trick](lounge-04-teach-it-a-trick/) | Core build | SKILL.md |
| 5 | [Give It Hands](lounge-05-give-it-hands/) | Core build | OpenAI API, Agents |
| 6 | [Plug Into MCP](lounge-06-plug-into-mcp/) | Advanced | MCP, Agents |
| 7 | [Run It With Opencode](lounge-07-run-it-with-opencode/) | Advanced | opencode |
| 8 | [Two Robots Talk](lounge-08-two-robots-talk/) | Advanced | Agents |
| 9 | [Capstone Showcase](lounge-09-capstone-showcase/) | Capstone | All of the above |

## How each lounge is laid out

```
lounge-0N-name/
  README.md    <- the checklist for that lounge
  working/     <- a finished, correct reference (read-only — no peeking first!)
  broken/      <- the same idea with a few real bugs planted on purpose
  template/    <- start here: fill in the ___ blanks
```

The pattern repeats but the content escalates — Lounge 5's tool-calling
mistakes show up again, on purpose, inside Lounge 9's capstone.

## The harness

`harness/check.py` grades a file against that lounge's checklist
without needing a real API key — it patches in a fake AI so the *logic*
gets tested offline.

```bash
python harness/check.py list
python harness/check.py lounge01
python harness/check.py lounge01 --file lounge-01-first-contact/template/first_contact_template.py
python harness/check.py all
```

**The harness isn't the whole grade.** A few lounges plant bugs on
purpose that only show up when you actually run the script with a real
key, or that never throw an error at all — they just quietly do the
wrong thing. Each lounge's README says which. That's intentional: a
green checkmark is a start, not proof of understanding.

## Install the tutor skill

`.opencode/skill/coding-lounge-guide/SKILL.md` is a skill for opencode:
a co-teacher that gives hints instead of answers, runs the harness
before guessing, and won't touch `working/` or `broken/` files. It
lives inside this repo, so opencode picks it up automatically when run
from here. If your opencode build reads skills from a different,
version-specific location, copy that folder there instead.

The root [`AGENTS.md`](AGENTS.md) sets the same ground rules for any
agent working in this repo generally — the skill is the same idea, made
explicitly callable.

## Tracker

Print this and check a box per finished lounge, left to right across
the term:

| Lounge | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Done | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
