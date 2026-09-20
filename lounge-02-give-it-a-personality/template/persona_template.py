"""
Lounge 2 — Give It a Personality (YOUR TURN)
Fill in the TODOs to give your agent a name and a job.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = (
    "You are Captain Calm Compass, a gentle and encouraging explorer who "
    "guides children through everyday questions. Speak with warm, simple "
    "words and use playful journey metaphors. Keep replies brief, practical, "
    "and suitable for children. Always end with: One small step!"
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
    questions = [
        "Why do socks seem to disappear?",
        "How can I welcome a new student?",
        "What do clouds dream about?",
        "How can I feel calmer before a test?",
        "What is one small way to tidy my desk?",
    ]

    for question in questions:
        print(f"You: {question}")
        print(f"Captain Calm Compass: {ask_persona(question)}\n")
