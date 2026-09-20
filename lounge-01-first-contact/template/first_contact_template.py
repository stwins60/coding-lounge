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
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    reply = ask_the_model("Hello, I'm a Coding Lounge builder!")
    print("AI said:", reply)

    while True:
        question = input("Ask the AI a question (or type quit): ")
        if question.lower() == "quit":
            break
        print("AI said:", ask_the_model(question))
