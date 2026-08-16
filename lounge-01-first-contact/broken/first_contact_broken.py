"""
Lounge 1 — First Contact (BROKEN)
This is supposed to work exactly like working/first_contact.py, but
three bugs are hiding inside it. Run it, read the error message, fix
ONE bug, run it again — repeat until it works.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def ask_the_model(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "text": question},   # bug: wrong dictionary key
        ],
    )
    return response.choice[0].message.content      # bug: typo'd attribute name


if __name__ == "__main__":
    reply = ask_the_model("Hello, I'm a Coding Lounge builder!")
    print("AI said:", reply)
    print(ask_the_model("What is one fun fact about robots?")
    print(ask_the_model("Can you rhyme with the word 'lounge'?"))
