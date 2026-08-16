"""
Lounge 2 — Give It a Personality
Add a system prompt so the model plays a consistent character.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# Checklist step 1: name your persona and its job right here.
SYSTEM_PROMPT = (
    "You are Circuit, a friendly robot who just landed on Earth and is "
    "curious about everything humans do. Keep replies short, cheerful, "
    "and always ask one question back."
)


def ask_persona(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    for q in [
        "What's your favorite Earth food?",
        "Why do humans sleep?",
        "Can you keep a secret?",
    ]:
        print(f"You: {q}")
        print(f"Circuit: {ask_persona(q)}\n")
