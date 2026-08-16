# Lounge 3 — Write the Rulebook

**Tier:** Core build · **Uses:** AGENTS.md, opencode

Turn your Lounge 2 persona into a real agent by giving it a proper
rulebook file.

## Checklist
- [ ] Create `AGENTS.md` for your Lounge 2 persona.
- [ ] Fill in who it is, what it may do, and what it must never do.
- [ ] Add 2 example conversations that show the rules in action.
- [ ] Load `AGENTS.md` into opencode and chat with your agent.
- [ ] Try to break a rule on purpose — fix the wording if it slips through.

## Check your work
```bash
python harness/check.py lounge03 --file lounge-03-write-the-rulebook/template/AGENTS.md
```

## Debugging challenge
`broken/AGENTS.md` is missing a required section, contains a rule that
contradicts good persona practice, and its examples section has no
heading. Find and fix all three — the harness will confirm.
