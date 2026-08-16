"""
Lounge 8 — Two Robots Talk (BROKEN)
Three bugs. The first crashes right away. The second silently drops
half the conversation. The third mixes up whose line is whose — it
never crashes, and the harness can't see it either. Read the code.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

QUIZ_MASTER_PROMPT = (
    "You are Quiz Master. Ask one short trivia question at a time about "
    "space. Do not reveal the answer yet."
)
PLAYER_PROMPT = (
    "You are Player. Answer the trivia question in one short sentence. "
    "If unsure, guess anyway."
)


def ask(system_prompt: str, conversation: list[str]) -> str:
    messages = [{"role": "system", "content": system_prompt}]
    for i, line in enumerate(conversation):
        role = "user" if i % 2 == 0 else "assistant"
        messages.append({"role": role, "content": line})
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return respones.choices[0].message.content


def run_conversation(rounds: int = 3) -> list[str]:
    conversation: list[str] = []
    for _ in range(rounds):
        question = ask(QUIZ_MASTER_PROMPT, conversation)
        conversation.append(question)
        answer = ask(PLAYER_PROMPT, conversation)
    return conversation


if __name__ == "__main__":
    transcript = run_conversation(3)
    for i, line in enumerate(transcript):
        speaker = "Quiz Master" if i % 2 == 0 else "Player"
        print(f"{speaker}: {line}")
