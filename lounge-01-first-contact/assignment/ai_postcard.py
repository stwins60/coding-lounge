"""Create a child-friendly AI postcard from a place chosen by the user."""

import sys

from dotenv import load_dotenv
from openai import OpenAI


sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()
client = OpenAI()


def ask_the_model(question: str) -> str:
    """Send a question to the AI and return its answer."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    while True:
        place = input("Enter a place (or type quit): ").strip()
        if place.lower() == "quit":
            break

        question = (
            f"Write a tiny postcard from {place}. "
            "Use exactly three short sentences and make it suitable for children."
        )
        message = ask_the_model(question)

        print(f"\n--- Postcard from {place} ---")
        print(message)
