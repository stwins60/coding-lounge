"""
Lounge 5 — Give It Hands (YOUR TURN)
Give the model a real function it can call.
"""

import json
import random

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def roll_dice(sides: int = 6) -> int:
    # TODO: return a random whole number between 1 and `sides`
    return ___


# TODO: describe roll_dice so the model knows it exists and how to call it
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "roll_dice",
            "description": "___",
            "parameters": {
                "type": "object",
                "properties": {"sides": {"type": "integer"}},
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
        return reply.content

    messages.append(reply)  # keep the assistant's tool request in the conversation
    for call in reply.tool_calls:
        function = AVAILABLE_FUNCTIONS[call.function.name]
        args = json.loads(call.function.arguments)
        result = function(**args)
        messages.append({"role": "tool", "tool_call_id": call.id, "content": str(result)})

    # TODO: ask the model again with the tool result included, and return its reply
    second = ___
    return ___


if __name__ == "__main__":
    print(handle_question("Roll a six-sided dice for me."))
    print(handle_question("What's the capital of France?"))
