"""
Lounge 2 — Give It a Personality (YOUR TURN)
Fill in the TODOs to give your agent a name and a job.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# TODO (checklist step 1): name your persona and describe its job/personality.
SYSTEM_PROMPT = "___"


def ask_persona(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": ___},  # TODO
            {"role": "user", "content": ___},     # TODO
        ],
    )
    return ___  # TODO: pull the reply text out of `response`


if __name__ == "__main__":
    # TODO: make a list of 5 questions, then use a loop to ask and print them.
    pass
