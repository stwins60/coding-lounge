# Lounge 8 — Two Robots Talk

**Tier:** Advanced · **Uses:** Agents, AGENTS.md

Build a second agent with its own job and let the two negotiate a
conversation.

## Checklist
- [ ] Design Agent B with a different job (e.g. Quiz Master to Agent A's Player).
- [ ] Give each its own system prompt / `AGENTS.md`.
- [ ] Let them exchange messages, back and forth, 3 full rounds.
- [ ] Spot one moment they misunderstood each other.
- [ ] Fix one instruction to solve that mix-up.

## Check your work
```bash
python harness/check.py lounge08 --file lounge-08-two-robots-talk/template/duo_agents_template.py
```

**Heads up:** the harness only catches some of the bugs here. It can't
tell whether each agent is actually seeing the *right* conversation
history — that one you have to trace through by hand, or ask the
`coding-lounge-guide` skill to walk it with you.

## Debugging challenge
`broken/duo_agents_broken.py` has 3 bugs: a typo'd variable name, a
missing line that drops half the conversation, and a swapped condition
that mixes up whose turn it is. Only the first two will show up in the
harness — the third you have to read for.
