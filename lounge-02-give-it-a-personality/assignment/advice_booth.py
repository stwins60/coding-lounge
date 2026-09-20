"""An advice booth run by Captain Calm Compass."""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

CATCHPHRASE = "One small step!"
SYSTEM_PROMPT = """
You are Captain Calm Compass, a gentle explorer who helps children navigate
small everyday problems. Sound calm, kind, and encouraging. Use simple words
and a light exploration theme. Give exactly one kind suggestion followed by
one tiny action the user can try now. Never give medical, legal, dangerous, or
other professional advice. For safety concerns or problems too big for a
child, clearly recommend asking a trusted adult for help. Keep every response
under 80 words and always end with the exact catchphrase: "One small step!"
""".strip()


def ask_persona(problem: str) -> str:
    """Ask Captain Calm Compass for safe, child-friendly advice."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": problem},
        ],
    )

    reply = response.choices[0].message.content or ""
    if reply.endswith(CATCHPHRASE):
        reply = reply[: -len(CATCHPHRASE)].rstrip()

    # Reserve three of the allowed 99 words for the catchphrase.
    reply_words = reply.split()[:96]
    return " ".join([*reply_words, CATCHPHRASE])


if __name__ == "__main__":
    print("Captain Calm Compass's Advice Booth")
    while True:
        problem = input("Describe a small problem (or type quit): ").strip()
        if problem.lower() == "quit":
            break
        if not problem:
            print("Please describe a problem or type quit.")
            continue
        print("Captain Calm Compass:", ask_persona(problem))
