# Lounge 8 — Two Robots Talk

**Tier:** Advanced · **Uses:** Agents, AGENTS.md · **Time:** 60 minutes

Build a second agent with its own job and let the two negotiate a
conversation.

## 60-minute class plan
- **5 min:** Trace how the conversation list grows.
- **15 min:** Write both prompts and role logic.
- **15 min:** Complete the conversation loop.
- **10 min:** Run the harness and a three-round conversation.
- **10 min:** Test five rounds and fix one misunderstanding.
- **5 min:** Record the roles and fix in `duo-notes.md`.

## Checklist
- [ ] Read `working/duo_agents.py` all the way through. Trace how
      `run_conversation` builds the `conversation` list and how `ask`
      figures out which lines are "user" vs "assistant" for each agent.
- [ ] In the template, write `AGENT_A_PROMPT` — a clear system prompt
      for an agent with a specific job (e.g. Quiz Master, Storyteller,
      Detective, Coach).
- [ ] Write `AGENT_B_PROMPT` for a second agent whose job creates an
      interesting dynamic with Agent A (e.g. Player, Co-author, Suspect,
      Athlete).
- [ ] Fill in the `role` assignment inside `ask` so Agent A's own past
      lines are `"assistant"` and the other agent's lines are `"user"`.
- [ ] Fill in the missing line in `run_conversation` so Agent B's reply
      is added to `conversation` after each round.
- [ ] Run the harness:
      `python harness/check.py lounge08 --file lounge-08-two-robots-talk/template/duo_agents_template.py`
- [ ] Run the script with a real key. Read all 6 lines of the printed
      transcript. Does it feel like a real back-and-forth, or does one
      agent seem confused?
- [ ] Increase `rounds` to **5** and run again. Find **one specific
      moment** in the transcript where the agents seemed to
      misunderstand each other or repeat themselves.
- [ ] Change one word in one of the system prompts to fix that
      misunderstanding and run again to confirm it improved.
- [ ] Write a `duo-notes.md` file documenting: your two agent roles,
      the misunderstanding you found, and the fix you made.

## Check your work
```bash
python harness/check.py lounge08 --file lounge-08-two-robots-talk/template/duo_agents_template.py
```

**Heads up:** the harness only catches some of the bugs here. It can't
tell whether each agent is actually seeing the *right* conversation
history — that one you have to trace through by hand, or ask the
`coding-lounge-guide` skill to walk it with you.

## Debugging challenge
`broken/duo_agents_broken.py` has **3 bugs**. Form a theory about
each bug *before* making any change.

1. **Bug 1 — crash on the first run:** A variable is referenced in one
   function but its name is misspelled. Python will raise `NameError`.
   Find the misspelled name and correct it. (The harness catches this.)
2. **Bug 2 — half the conversation disappears:** `run_conversation`
   gets Agent A's reply and appends it, then gets Agent B's reply —
   but forgets to append Agent B's reply to `conversation`. The list
   is half the size it should be. Add the missing append. (The harness
   catches this.)
3. **Bug 3 — swapped roles:** The `role` logic in `ask` has been
   flipped — even-indexed lines are marked `"user"` and odd-indexed
   lines are marked `"assistant"`, but it should be the *other way
   around*. The code runs without crashing and produces output, but
   each agent thinks the other agent's lines are its own past turns.
   The harness can't detect this — you have to read the logic. Fix it.

## Go deeper
- **Three-way conversation:** Add a third agent (a referee, a narrator,
  or a judge) that speaks once after every two Agent A/B exchanges and
  comments on the conversation. This requires changing `run_conversation`.
- **Topic pivot:** After round 3, inject a new `"user"` message into
  the conversation from outside the loop that changes the topic. See
  how both agents adapt.
- **AGENTS.md for both:** Write a short `AGENTS.md` for each agent in
  your duo and load one of them into opencode. Does it still behave the
  same way as when it was just a system prompt?

## Reflect
Write your answers in `duo-notes.md` under a **Reflect** heading:

1. Each agent only sees the `conversation` list — it has no idea the
   other agent is also an AI. Does that matter? Could it cause
   problems in a longer conversation?
2. In `ask`, why does the first item in the conversation get role
   `"assistant"` for Agent A but role `"user"` for Agent B, even
   though it's the exact same message?
