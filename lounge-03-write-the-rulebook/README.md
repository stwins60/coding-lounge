# Lounge 3 — Write the Rulebook

**Tier:** Core build · **Uses:** AGENTS.md, opencode · **Time:** ~1 hour

Turn your Lounge 2 persona into a real agent by giving it a proper
rulebook file.

## Checklist
- [ ] Read the working example at `working/AGENTS.md` and the template
      at `template/AGENTS.md` — understand every section before you
      write a single word of your own.
- [ ] Fill in the **Who I Am** section: 2–3 sentences that describe your
      Lounge 2 persona's identity and personality.
- [ ] Fill in **What I Can Do**: at least **4** clear, specific abilities
      (not vague — "answer questions" is too vague; "answer trivia
      questions about space in a cheerful tone" is specific).
- [ ] Fill in **What I Must Never Do**: at least **4** clear rules.
      At least one rule should be about *how* it speaks, not just what
      topics it avoids.
- [ ] Add **3 example conversations** (not 2) — each should demonstrate
      a different rule in action.
- [ ] Run the harness:
      `python harness/check.py lounge03 --file lounge-03-write-the-rulebook/template/AGENTS.md`
- [ ] Load your `AGENTS.md` into opencode and have a conversation with
      your agent. Ask it at least 3 questions.
- [ ] Deliberately try to **break one rule** — e.g. if a rule says
      "never pretend to be human", ask "are you human?". Did it hold?
- [ ] If the agent slipped through the rule, rewrite that rule to be
      clearer, reload, and test again until it holds.

## Check your work
```bash
python harness/check.py lounge03 --file lounge-03-write-the-rulebook/template/AGENTS.md
```

## Debugging challenge
`broken/AGENTS.md` has **3 bugs**. Read the whole file carefully before
touching anything.

1. **Bug 1 — missing required section:** One of the three required
   sections (Who I Am / What I Can Do / What I Must Never Do) is
   completely absent. The harness will catch this — find it, add it.
2. **Bug 2 — a rule that contradicts good practice:** One item in the
   "Can Do" list actively contradicts what a safe, trustworthy agent
   should do. Read each bullet and ask: "would this make the agent
   *less* trustworthy?" Fix the contradiction.
3. **Bug 3 — no heading on the examples section:** The example
   conversations exist but there's no `## Example Conversations`
   heading above them. Without the heading, opencode and other tools
   won't find them. Add the heading in the right place.

Fix all three, then re-run the harness to confirm.

## Go deeper
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
Write your answers at the bottom of your `AGENTS.md` as an HTML
comment (`<!-- like this -->`), so they don't affect the agent:

1. What's the difference between a rule like "be nice" and a rule like
   "never say the word 'can't' — always suggest what you *can* do
   instead"? Which one is easier for an agent to follow? Why?
2. Which of your "Must Never Do" rules was hardest to write clearly?
   What made it hard?
