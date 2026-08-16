"""
Lounge 8 — Two Robots Talk
Two agents with different jobs have a conversation with each other.
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
    """Ask one agent to reply, given the conversation so far as plain text."""
    messages = [{"role": "system", "content": system_prompt}]
    for i, line in enumerate(conversation):
        # The agent's own past lines look like its own turns; the other
        # agent's lines look like the human/user turns to it.
        role = "assistant" if i % 2 == 0 else "user"
        messages.append({"role": role, "content": line})
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response.choices[0].message.content


def run_conversation(rounds: int = 3) -> list[str]:
    """Alternate turns between Quiz Master and Player for `rounds` exchanges."""
    conversation: list[str] = []
    for _ in range(rounds):
        question = ask(QUIZ_MASTER_PROMPT, conversation)
        conversation.append(question)
        answer = ask(PLAYER_PROMPT, conversation)
        conversation.append(answer)
    return conversation


if __name__ == "__main__":
    transcript = run_conversation(3)
    for i, line in enumerate(transcript):
        speaker = "Quiz Master" if i % 2 == 0 else "Player"
        print(f"{speaker}: {line}")
