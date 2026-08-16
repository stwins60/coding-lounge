"""
Lounge 1 — First Contact
Send a message to a real AI model and get a real reply back.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads OPENAI_API_KEY from a .env file next to this script
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

    # Checklist step 4: try two more questions of your own below.
    print(ask_the_model("What is one fun fact about robots?"))
    print(ask_the_model("Can you rhyme with the word 'lounge'?"))
