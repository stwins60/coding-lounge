# Assignment: AI Postcard Maker

Create a new program that asks where the user wants to visit, then asks the AI
to write a tiny postcard from that place.

Do not edit the lounge template. Build this project from scratch as
`assignment/ai_postcard.py`.

## Requirements

1. Ask the user to enter a place.
2. Build an AI question that includes the place.
3. Request exactly three short postcard sentences.
4. Print a postcard heading and the AI's message.
5. Let the user make a second postcard without restarting the program.

## Boundaries

- Keep the API key in `.env` only.
- Do not use a place chosen in advance; read it from `input()`.
- Ask the model to keep its response suitable for children.

## Evidence

Run:

```bash
python lounge-01-first-contact/assignment/ai_postcard.py
```

- [ ] I made postcards for two different places.
- [ ] Each AI question included the place entered by the user.
- [ ] My source file contains no API key.
- [ ] I can explain how the question reaches the model.
