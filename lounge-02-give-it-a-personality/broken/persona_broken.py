"""
Lounge 2 — Give It a Personality (BROKEN)
Three bugs are hiding in here: one Python won't even let you run, one
that crashes partway through, and one that's silently wrong until you
run it for real with an API key. Fix them one at a time.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = (
    "You are Circuit, a friendly robot who just landed on Earth and is "
    "curious about everything humans do. Keep replies short and cheerful."
)


def ask_persona(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "sytem", "content": SYSTEM_PROMPT},   # bug: misspelled role name
            {"role": "user", "content": question},
        ],
    )
      return response.choices[0].message.content            # bug: bad indentation


if __name__ == "__main__":
    for q in ["What's your favorite Earth food?", "Why do humans sleep?"]:
        print(f"You: {q}")
        print(f"Circuit: {ask_persoan(q)}\n")                # bug: typo'd function name
