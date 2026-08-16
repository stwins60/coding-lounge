"""
Lounge 5 — Give It Hands (BROKEN)
Three bugs, three different kinds: a tool that's registered nowhere,
a missing step that only breaks things when you run it for real, and a
crash. Fix them one at a time, in order, and re-run after each fix.
"""

import json
import random

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def roll_dice(sides: int = 6) -> int:
    return random.randint(1, sides)


TOOLS = []  # bug: roll_dice exists but was never added here, so the model can't see it

AVAILABLE_FUNCTIONS = {"roll_dice": roll_dice}


def handle_question(question: str) -> str:
    messages = [{"role": "user", "content": question}]

    first = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=TOOLS)
    reply = first.choices[0].message

    if not reply.tool_calls:
        return reply.content

    # bug: forgot `messages.append(reply)` here — the tool result below
    # ends up with no assistant turn in front of it.
    for call in reply.tool_calls:
        function = AVAILABLE_FUNCTIONS[call.function.Name]  # bug: wrong-case attribute
        args = json.loads(call.function.arguments)
        result = function(**args)
        messages.append({"role": "tool", "tool_call_id": call.id, "content": str(result)})

    second = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return second.choices[0].message.content


if __name__ == "__main__":
    print(handle_question("Roll a six-sided dice for me."))
    print(handle_question("What's the capital of France?"))
