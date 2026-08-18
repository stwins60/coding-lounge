# Assignment: Character Advice Booth

Invent an advice-giving character that helps with small everyday problems while
keeping a recognizable voice.

Build it from scratch as `assignment/advice_booth.py`. Do not copy or edit the
lounge template.

## Requirements

1. Create a system prompt for a character with an original name and theme.
2. Give the character one speaking habit, such as ending with a catchphrase.
3. Ask the user to describe a small problem.
4. Return one kind suggestion and one tiny action the user can try.
5. Continue accepting problems until the user enters `quit`.

## Boundaries

- The character must not give medical, legal, or dangerous advice.
- The character must admit when an adult should help.
- Every reply should stay under 100 words.

## Evidence

```bash
python lounge-02-give-it-a-personality/assignment/advice_booth.py
```

- [ ] I tested three different problems.
- [ ] Every reply used the character's speaking habit.
- [ ] A safety-related question suggested asking a trusted adult.
- [ ] `assignment/design-notes.md` explains which prompt words shape the voice.
