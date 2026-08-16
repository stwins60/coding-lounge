"""
Lounge 9 — Capstone Showcase (BROKEN)
Three bugs, one borrowed from each of Lounges 5, 5, and 8's bug
families. If you've debugged those lounges already, you've seen each
of these before.
"""

import json
import random

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = (
    "You are Lounge Bot, the Coding Lounge's helper. Be encouraging and "
    "brief. You can roll dice and you know today's Coding Lounge note."
)

NOTES = {"today.txt": "Welcome to the Coding Lounge capstone. Good luck!"}


def roll_dice(sides: int = 6) -> int:
    return random.randint(1, sides)


def read_note(name: str) -> str:
    return NOTES[name]


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "roll_dice",
            "description": "Roll a dice with the given number of sides.",
            "parameters": {
                "type": "object",
                "properties": {"sides": {"type": "integer"}},
                "required": ["sides"],
            },
        },
    },
    # bug: read_note exists in AVAILABLE_FUNCTIONS below but was never
    # added here, so the model never learns it can ask for the note.
]

AVAILABLE_FUNCTIONS = {"roll_dice": roll_dice, "read_note": read_note}


def run_showcase(question: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
    first = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=TOOLS)
    reply = first.choices[0].message

    if not reply.tool_calls:
        return reply.content

    # bug: forgot `messages.append(reply)` here
    for call in reply.tool_calls:
        function = AVAILABLE_FUNCTIONS[call.function.Name]  # bug: wrong-case attribute
        args = json.loads(call.function.arguments)
        result = function(**args)
        messages.append({"role": "tool", "tool_call_id": call.id, "content": str(result)})

    second = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return second.choices[0].message.content


if __name__ == "__main__":
    print(run_showcase("Roll a dice for me."))
    print(run_showcase("What's today's note say?"))
    print(run_showcase("What's the capital of Japan?"))
