"""
Lounge 5 — Give It Hands
Give the model a real function it can call instead of guessing.
"""

import json
import random

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def roll_dice(sides: int = 6) -> int:
    """The actual Python function the model is allowed to call."""
    return random.randint(1, sides)


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "roll_dice",
            "description": "Roll a fair dice and return the result.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sides": {"type": "integer", "description": "Number of sides on the dice"},
                },
                "required": ["sides"],
            },
        },
    }
]

AVAILABLE_FUNCTIONS = {"roll_dice": roll_dice}


def handle_question(question: str) -> str:
    messages = [{"role": "user", "content": question}]

    first = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=TOOLS)
    reply = first.choices[0].message

    if not reply.tool_calls:
        # The model answered directly — no tool was needed.
        return reply.content

    # The model wants to call a tool. Run it for real and hand the result back.
    messages.append(reply)
    for call in reply.tool_calls:
        function = AVAILABLE_FUNCTIONS[call.function.name]
        args = json.loads(call.function.arguments)
        result = function(**args)
        messages.append(
            {
                "role": "tool",
                "tool_call_id": call.id,
                "content": str(result),
            }
        )

    second = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return second.choices[0].message.content


if __name__ == "__main__":
    print(handle_question("Roll a six-sided dice for me."))
    print(handle_question("What's the capital of France?"))
