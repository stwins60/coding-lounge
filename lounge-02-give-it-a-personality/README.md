# Lounge 2 — Give It a Personality

**Tier:** Warm-up · **Uses:** OpenAI API

Use a system prompt to turn the model into a character with a name and
a job.

## Checklist
- [ ] Add a `system` message naming your persona and its job.
- [ ] Ask it 3 questions — check the personality stays consistent.
- [ ] Turn the personality up: make it funnier or stranger, then retest.
- [ ] Save the persona's rules in plain English in `persona-notes.md`.
- [ ] Have a partner guess your persona from just 2 replies.

## Check your work
```bash
python harness/check.py lounge02 --file lounge-02-give-it-a-personality/template/persona_template.py
```

## Debugging challenge
`broken/persona_broken.py` has 3 bugs: a misspelled role name (only
shows up when you run it for real with a key), a bad indentation, and
a typo'd function name. Fix them one at a time.
