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
    # TODO (checklist step 2): ask "Hello, I'm a Coding Lounge builder!"
    # TODO (checklist step 4): ask two more questions of your own
    pass
