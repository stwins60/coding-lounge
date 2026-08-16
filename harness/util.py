"""
Shared helpers for the Coding Lounge harness.

The big idea: lounge scripts call the real OpenAI API. Grading a whole
classroom of laptops shouldn't need 25 API keys and a network connection,
so `fake_openai()` swaps in a stand-in client that mimics the real
response shape closely enough to test the *logic* of a script offline.

Kids still run their scripts for real, with a real key, on their own —
this is only for the automated checker.
"""

from __future__ import annotations

import importlib.util
import json
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch


# --- Fake response objects, shaped like the real openai SDK's ----------

class FakeFunctionCall:
    def __init__(self, name: str, arguments: dict):
        self.name = name
        self.arguments = json.dumps(arguments)


class FakeToolCall:
    def __init__(self, call_id: str, name: str, arguments: dict):
        self.id = call_id
        self.function = FakeFunctionCall(name, arguments)


class FakeMessage:
    def __init__(self, content: str | None = None, tool_calls: list | None = None):
        self.content = content
        self.tool_calls = tool_calls or []


class FakeChoice:
    def __init__(self, message: FakeMessage):
        self.message = message


class FakeResponse:
    def __init__(self, message: FakeMessage):
        self.choices = [FakeChoice(message)]


class _FakeCompletions:
    def __init__(self, reply_fn):
        self._reply_fn = reply_fn

    def create(self, **kwargs):
        messages = kwargs.get("messages", [])
        for m in messages:
            # Mimic the real API's complaint about a malformed message dict,
            # so typo'd keys ("text" instead of "content") fail the same way.
            if isinstance(m, dict) and "role" in m and "content" not in m and "tool_call_id" not in m:
                raise KeyError("content")
        message = self._reply_fn(messages, kwargs)
        return FakeResponse(message)


class _FakeChat:
    def __init__(self, reply_fn):
        self.completions = _FakeCompletions(reply_fn)


class _FakeOpenAI:
    def __init__(self, reply_fn, *args, **kwargs):
        self.chat = _FakeChat(reply_fn)


def default_reply(messages, kwargs):
    last_user = next(
        (m.get("content") for m in reversed(messages) if isinstance(m, dict) and m.get("role") == "user"),
        "",
    )
    return FakeMessage(content=f"[fake reply to: {str(last_user)[:40]}]")


def tool_call_then_reply(tool_name: str, arguments: dict, final_text: str, trigger=None):
    """Reply strategy: offer a tool call once, then answer plainly once a
    tool result message shows up in the conversation. `trigger`, if given,
    is a function(messages) -> bool deciding whether this question even
    needs the tool (otherwise it answers directly, like the real model
    would for an unrelated question)."""

    def _reply(messages, kwargs):
        already_called = any(
            isinstance(m, dict) and m.get("role") == "tool" for m in messages
        )
        wants_tool = trigger(messages) if trigger else True
        if not already_called and kwargs.get("tools") and wants_tool:
            return FakeMessage(tool_calls=[FakeToolCall("call_1", tool_name, arguments)])
        if already_called:
            return FakeMessage(content=final_text)
        return FakeMessage(content="[fake direct reply, no tool needed]")

    return _reply


@contextmanager
def fake_openai(reply_fn=None):
    """Patch `openai.OpenAI` so a lounge script runs offline during grading."""
    fn = reply_fn or default_reply

    def _make(*args, **kwargs):
        return _FakeOpenAI(fn)

    with patch("openai.OpenAI", _make):
        yield


def import_module_from_path(name: str, path: Path):
    """Import a .py file the way the harness needs to: fresh, by path,
    without it needing to be on sys.path or be a package."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
