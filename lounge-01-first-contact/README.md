# Lounge 1 — First Contact

**Tier:** Warm-up · **Uses:** OpenAI API

Send your very first message to a real AI model and get a real reply back.

## Folders
- `working/` — a finished, correct version. Read it *after* you've tried.
- `broken/` — the same idea with 3 bugs hiding in it. Run it, read the
  error, fix one bug at a time.
- `template/` — start here. Fill in the `___` blanks.

## Checklist
- [ ] Put your API key in `.env` — never paste it in chat or code.
- [ ] Send the message "Hello, I'm a Coding Lounge builder!" to the model.
- [ ] Print the AI's reply in the terminal.
- [ ] Swap the message and run it two more times with new questions.
- [ ] Write one sentence in `notes.md`: what surprised you?

## Check your work
```bash
python harness/check.py lounge01 --file lounge-01-first-contact/template/first_contact_template.py
```

## Debugging challenge
`broken/first_contact_broken.py` has 3 bugs, each a different kind:
a broken bracket, a wrong dictionary key, and a typo'd attribute name.
Fix them one at a time — run it, read the error, fix just that one, run
it again.
