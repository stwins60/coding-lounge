"""
Lounge 9 — Capstone Showcase (YOUR TURN)
Combine a persona, a tool, and a mini-MCP resource read into one agent.
Make it your own — change the persona, the tool, and the note.
"""

import json
import random

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# TODO: write your own persona
SYSTEM_PROMPT = "___"

NOTES = {"today.txt": "___"}


def roll_dice(sides: int = 6) -> int:
    return random.randint(1, sides)


def read_note(name: str) -> str:
    return NOTES[name]


# TODO: advertise BOTH roll_dice and read_note here, like Lounge 5's TOOLS list
TOOLS = [
    ___,
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

    messages.append(reply)
    for call in reply.tool_calls:
        function = AVAILABLE_FUNCTIONS[call.function.name]
        args = json.loads(call.function.arguments)
        result = function(**args)
        messages.append({"role": "tool", "tool_call_id": call.id, "content": str(result)})

    # TODO: ask the model again with the tool result included, and return its reply
    second = ___
    return ___


if __name__ == "__main__":
    print(run_showcase("Roll a dice for me."))
    print(run_showcase("What's today's note say?"))
    print(run_showcase("What's the capital of Japan?"))
