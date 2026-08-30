# Lounge 4 — Teach It a Trick

**Tier:** Core build · **Uses:** SKILL.md, Python · **Time:** 60 minutes

Package one skill as a file your agent can look up and follow, step by
step — the same shape as [`.opencode/skill/coding-lounge-guide/SKILL.md`](../.opencode/skill/coding-lounge-guide/SKILL.md), which is a real one this repo actually uses.

## 60-minute class plan
- **5 min:** Choose the skill and its input.
- **15 min:** Complete `template/SKILL.md` with four ordered steps.
- **20 min:** Complete `template/skill_tester_template.py`.
- **10 min:** Break one skill check on purpose, repair it, and rerun.
- **5 min:** Run the lounge harness.
- **5 min:** Explain why one test matters.

## Checklist
- [ ] Read the working example at `working/SKILL.md` and the real skill
      at `.opencode/skill/coding-lounge-guide/SKILL.md`. Notice what
      every section is for before writing your own.
- [ ] Pick a skill your agent doesn't already have. Good options:
      flip a coin, translate one word to another language, pick a random
      colour, tell a joke in a specific format, or invent your own.
- [ ] Fill in the frontmatter (`name` and `description`) in the
      template. The name should be a short slug like `flip-coin`.
- [ ] Write **at least 4 numbered steps** that are clear enough for
      someone who has never heard of your skill to follow exactly.
      Order matters — plan before acting, act before reporting.
- [ ] Add a complete `## Example` block: the ask, what to do, and the
      exact reply format.
- [ ] Complete `skill_tester_template.py` so it checks the frontmatter,
      four numbered steps, the example, and leftover blanks.
- [ ] Temporarily remove one step and prove your tester reports a failure.
      Restore the step before continuing.
- [ ] Run the harness:
      `python harness/check.py lounge04 --file lounge-04-teach-it-a-trick/template/SKILL.md`
- [ ] Link your new skill from your Lounge 3 `AGENTS.md` by adding a
      `## Skills` section that names the skill and its file path.
- [ ] Ask your agent (in opencode) to use the skill **by name** — e.g.
      "use the flip-coin skill". Check it follows your exact steps in
      order.
- [ ] Get a classmate to trigger the skill without coaching — just by
      asking for the thing the skill does. Watch whether the agent
      follows the steps or shortcuts.

## Check your work
```bash
python lounge-04-teach-it-a-trick/template/skill_tester_template.py
python harness/check.py lounge04 --file lounge-04-teach-it-a-trick/template/SKILL.md
```

## Debugging challenge
`broken/SKILL.md` has **2 bugs**. Read the whole file before editing.

1. **Bug 1 — missing frontmatter field:** The `---` block at the top is
   incomplete. Compare it to the working example to see what's missing.
   The harness will fail until this is added.
2. **Bug 2 — steps in the wrong order:** The numbered steps describe
   the skill, but they're in a logically broken order — the result is
   announced before it's even been calculated. Reading the steps aloud
   in order should make sense; right now it doesn't. Reorder them.

Fix both, re-run the harness to confirm.

## Go deeper
- **Two skills:** Write a second `SKILL.md` for a different trick and
  link both from your `AGENTS.md`. Ask your agent to use each one and
  confirm it picks the right skill for the right request.
- **Edge cases in steps:** Add a step to your original skill that
  handles an unusual input — e.g. "if the user asks to flip 0 coins,
  say that doesn't make sense and ask again." Test it.
- **Skill vs guessing:** Ask your agent the same question twice: once
  telling it to use the skill, and once without mentioning the skill.
  Are the replies different? Why might they be?

## Reflect
Write your answers in a `skill-notes.md` file next to your template:

1. A skill file is just text. Why would an AI follow it instead of
   making up its own steps?
2. If your skill has 4 steps but the AI only follows 3 of them, what
   would you change in the file to make it more likely to follow all 4?
