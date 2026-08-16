# Lounge 5 — Give It Hands

**Tier:** Core build · **Uses:** OpenAI API, Agents

Wire up a real function the model can call instead of guessing the
answer.

## Checklist
- [ ] Write one small function (`roll_dice()`, `flip_coin()`, …).
- [ ] Register it as a tool the model is allowed to call.
- [ ] Ask a question only the tool can answer correctly.
- [ ] Check the terminal log to prove the tool was actually called, not guessed.
- [ ] Add a second tool and watch the agent pick the right one.

## Check your work
```bash
python harness/check.py lounge05 --file lounge-05-give-it-hands/template/tool_agent_template.py
```

## Debugging challenge
`broken/tool_agent_broken.py` has 3 bugs: a tool that's never actually
registered, a missing conversation entry, and a typo'd attribute name.
Fix them one at a time.
