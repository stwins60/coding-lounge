# Bonus Challenge: Robot Interviewer

Turn your program into a robot interviewer that creates a special builder
nickname for you.

## Your Mission

Update `first_contact_template.py` so it:

1. Asks the user for their name.
2. Asks what they enjoy building.
3. Sends both answers to the AI in one question.
4. Asks the AI to invent a short, funny robot-builder nickname.
5. Prints the nickname in the terminal.

## Rules

- Store each answer in a variable.
- Use an f-string to put both answers into the AI question.
- Never put an API key in the Python file.
- Keep the AI's reply friendly and suitable for children.

## Small Hints

Ask the user a question with:

```python
answer = input("Your question: ")
```

Start an f-string by placing `f` before the opening quote:

```python
message = f"My answer is {answer}."
```

## Success Check

Run the program twice with different names and projects.

- [ ] The program waits for both answers.
- [ ] Both answers are included in the message sent to the AI.
- [ ] A nickname is printed each time.
- [ ] Different answers can produce different nicknames.
- [ ] The API key remains only in `.env`.

## Extra Bonus

After receiving the nickname, ask the AI one more question:

> What should a robot builder with this nickname create next?

Print the new project idea underneath the nickname.
