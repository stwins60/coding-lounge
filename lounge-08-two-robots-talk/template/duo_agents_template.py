"""
Lounge 8 — Two Robots Talk (YOUR TURN)
Build two agents with different jobs and let them talk to each other.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# TODO: give each agent a name and a job
AGENT_A_PROMPT = "___"
AGENT_B_PROMPT = "___"


def ask(system_prompt: str, conversation: list[str]) -> str:
    messages = [{"role": "system", "content": system_prompt}]
    for i, line in enumerate(conversation):
        # TODO: figure out which lines are this agent's own past turns
        # ("assistant") and which are the other agent's ("user")
        role = ___
        messages.append({"role": role, "content": line})
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response.choices[0].message.content


def run_conversation(rounds: int = 3) -> list[str]:
    conversation: list[str] = []
    for _ in range(rounds):
        line_a = ask(AGENT_A_PROMPT, conversation)
        conversation.append(line_a)
        # TODO: get Agent B's reply and add it to `conversation` too
        ___
    return conversation


if __name__ == "__main__":
    transcript = run_conversation(3)
    for i, line in enumerate(transcript):
        speaker = "Agent A" if i % 2 == 0 else "Agent B"
        print(f"{speaker}: {line}")
