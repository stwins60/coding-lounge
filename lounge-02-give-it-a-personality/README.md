# Lounge 2 — Give It a Personality

**Tier:** Warm-up · **Uses:** OpenAI API · **Time:** 60 minutes

Use a system prompt to turn the model into a character with a name and
a job.

## 60-minute class plan
- **5 min:** Read the starter and choose a character idea.
- **15 min:** Write the system prompt.
- **15 min:** Complete `ask_persona`.
- **10 min:** Code a list-and-loop test for five questions.
- **10 min:** Improve the prompt after reading the replies.
- **5 min:** Run the harness.

## Checklist
- [ ] Open `template/persona_template.py` and read through the whole file
      before changing anything. Understand what each `TODO` is asking.
- [ ] Write a `SYSTEM_PROMPT` that gives your agent a name, a job, and
      at least two personality traits (e.g. always curious, speaks in
      rhymes, loves puns).
- [ ] Fill in the `ask_persona` function so it sends your system prompt
      and the user's question to the model and returns the reply.
- [ ] Run the harness to check your code is wired up correctly:
      `python harness/check.py lounge02 --file lounge-02-give-it-a-personality/template/persona_template.py`
- [ ] Store at least **5 different questions** in a list, then use a loop in
      `__main__` to ask and print each one. Include at least one silly
      question and one serious question.
- [ ] Check that all 5 replies feel like the *same* character — not just
      the same job, but the same voice and personality.
- [ ] Tweak the `SYSTEM_PROMPT` to make the personality stronger or
      stranger, then re-run and compare the before and after replies.
- [ ] Write a `persona-notes.md` file (next to the template) explaining
      your persona in plain English: who they are, what makes them
      unique, and one rule you'd never want them to break.
- [ ] Show a partner only **2 replies** and see if they can guess the
      persona's name and job from those alone. If they can't, update
      the system prompt until they can.

## Check your work
```bash
python harness/check.py lounge02 --file lounge-02-give-it-a-personality/template/persona_template.py
```

## Debugging challenge
`broken/persona_broken.py` has **3 bugs**. Open the file and read it
carefully before running anything.

1. **Bug 1 — Python won't even start:** There is a bad indentation
   somewhere in the file. Find it by reading the code top to bottom;
   `IndentationError` will name the line number once you try to run it.
2. **Bug 2 — crashes mid-run:** A function is called by a name that
   doesn't match any defined function. Read the `if __name__` block
   and compare with the actual function definition above it.
3. **Bug 3 — silent wrong output:** The role name in one message dict
   has a typo. The code runs without crashing but the model doesn't
   behave like a persona at all. You'll only spot this by running it
   with a real key **or** reading the string very carefully.

Fix them one at a time. Run the file after each fix to confirm you
haven't introduced a new problem.

## Go deeper
Once all checklist items are green, try these stretch challenges:

- **Mood dial:** Add an optional `mood` parameter to `ask_persona` so
  you can call `ask_persona("Hello", mood="grumpy")` and the system
  prompt includes the mood. Test it with at least 3 moods.
- **Memory stub:** After each call, append the question and reply to a
  Python list called `history`. Print the whole history at the end of
  `__main__`. (Real memory comes later — this is just a list for now.)
- **Two personas, one fight:** Create a second `SYSTEM_PROMPT_B` for a
  persona that disagrees with your first one. Ask them both the same
  question and print both replies side by side.

## Reflect
Write your answers to these questions at the bottom of `persona-notes.md`:

1. What one word in your system prompt most changes how the persona
   sounds? How do you know?
2. If you removed the persona's name from the prompt entirely, would
   the replies feel different? Try it and describe what changed.
