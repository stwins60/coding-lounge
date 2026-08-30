"""
Lounge 1 — First Contact (YOUR TURN)
Fill in the TODOs below to send your first message to a real AI model.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def ask_the_model(question: str) -> str:
    """Send `question` to the model and return its reply as a string."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": ___},   # TODO: put `question` here
        ],
    )
    return ___  # TODO: pull the reply text out of `response`


if __name__ == "__main__":
    # TODO: ask "Hello, I'm a Coding Lounge builder!" and print the reply.
    # TODO: replace `pass` with a loop that:
    #   1. reads a question with input()
    #   2. stops when the question is "quit"
    #   3. calls ask_the_model() and prints the reply
    pass
