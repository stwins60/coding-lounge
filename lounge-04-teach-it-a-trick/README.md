# Lounge 4 — Teach It a Trick

**Tier:** Core build · **Uses:** SKILLS.md

Package one skill as a file your agent can look up and follow, step by
step — the same shape as [`.opencode/skill/coding-lounge-guide/SKILL.md`](../.opencode/skill/coding-lounge-guide/SKILL.md), which is a real one this repo actually uses.

## Checklist
- [ ] Pick a skill your agent doesn't have yet (dice roll, translate a
      word, tell a joke).
- [ ] Write a `SKILL.md` entry: name, description, exact steps.
- [ ] Link the skill file from your Lounge 3 `AGENTS.md`.
- [ ] Ask your agent to use the skill by name and check it follows your steps.
- [ ] Get a classmate to trigger the skill without your help.

## Check your work
```bash
python harness/check.py lounge04 --file lounge-04-teach-it-a-trick/template/SKILL.md
```

## Debugging challenge
`broken/SKILL.md` is missing a required frontmatter field, and its
steps are in the wrong order — it tells the result before it's even
been picked. Reading a skill file top to bottom should make sense; if
it doesn't, that's the bug.
