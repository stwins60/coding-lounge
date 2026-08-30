# Lounge 3 — Write the Rulebook

**Tier:** Core build · **Uses:** AGENTS.md, Python · **Time:** 60 minutes

Turn your Lounge 2 persona into a real agent by giving it a proper
rulebook file, then write code that tests it.

## 60-minute class plan
- **5 min:** Choose the agent's name, purpose, and voice.
- **15 min:** Complete the identity, abilities, restrictions, and examples.
- **20 min:** Complete `template/rulebook_tester_template.py`.
- **10 min:** Make one check fail on purpose, repair the rulebook, and rerun.
- **5 min:** Run the lounge harness.
- **5 min:** Explain one tester function.

## Checklist
- [ ] Fill in the **Who I Am** section: 2–3 sentences that describe your
      agent's identity, purpose, and personality.
- [ ] Fill in **What I Can Do**: at least **3** clear, specific abilities
      (not vague — "answer questions" is too vague; "answer trivia
      questions about space in a cheerful tone" is specific).
- [ ] Fill in **What I Must Never Do**: at least **3** clear rules.
      At least one rule should be about *how* it speaks, not just what
      topics it avoids.
- [ ] Add **2 example conversations** — one showing an ability and one
      showing a boundary.
- [ ] In `rulebook_tester_template.py`, implement `section_text`,
      `count_bullets`, and every check inside `check_rulebook`.
- [ ] Run the tester. Temporarily remove a heading or example from
      `AGENTS.md` and prove that the matching check fails. Restore it afterward.
- [ ] Run the harness:
      `python harness/check.py lounge03 --file lounge-03-write-the-rulebook/template/AGENTS.md`

## Check your work
```bash
python lounge-03-write-the-rulebook/template/rulebook_tester_template.py
python harness/check.py lounge03 --file lounge-03-write-the-rulebook/template/AGENTS.md
```

## Optional debugging challenge
`broken/AGENTS.md` has **4 bugs**. Read the whole file carefully before
touching anything.

1. **Bug 1 — missing required section:** One of the three required
   sections (Who I Am / What I Can Do / What I Must Never Do) is
   completely absent. The harness will catch this — find it, add it.
2. **Bug 2 — a rule that contradicts good practice:** One item in the
   "Can Do" list actively contradicts what a safe, trustworthy agent
   should do. Read each bullet and ask: "would this make the agent
   *less* trustworthy?" Fix the contradiction.
3. **Bug 3 — no heading on the examples section:** An example conversation
      exists but there's no `## Example Conversations` heading above it.
      Add the heading in the right place.
4. **Bug 4 — too few examples:** The checklist requires two example
      conversations, but the broken file has only one. Add a second example
      that demonstrates a different rule.

Fix all four, then re-run the harness to confirm.

## Go deeper
- **Try it live:** After Lounge 7, load your `AGENTS.md` into opencode.
      Ask three questions, including one designed to break a rule. Rewrite
      any rule the agent does not follow, then test it again.
- **Rule stress test:** Write a list of 5 tricky questions designed to
  make your agent break its own rules. Ask all 5, record which ones
  worked and which didn't, and fix the `AGENTS.md` until all 5 hold.
- **Version 2:** Copy your finished `AGENTS.md` to `AGENTS_v2.md`.
  Add a new skill section (`## Skills`) that lists one skill your agent
  can use — you'll fill in the actual skill file in Lounge 4.
- **Compare personas:** Swap `AGENTS.md` files with a classmate and try
  to break *their* rules. Write down which rule was easiest to break
  and why.

## Reflect
If you have time, discuss or write answers to these questions:

1. What's the difference between a rule like "be nice" and a rule like
   "never say the word 'can't' — always suggest what you *can* do
   instead"? Which one is easier for an agent to follow? Why?
2. Which of your "Must Never Do" rules was hardest to write clearly?
   What made it hard?
