"""Lounge 9 — Capstone Showcase."""

from pathlib import Path

from harness.util import FakeMessage, FakeToolCall, fake_openai, import_module_from_path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TARGET = ROOT / "lounge-09-capstone-showcase" / "template" / "showcase_agent_template.py"


def _reply(messages, kwargs):
    already_called = any(isinstance(m, dict) and m.get("role") == "tool" for m in messages)
    if already_called:
        return FakeMessage(content="Here you go!")
    last_user = next(
        (m.get("content", "") for m in reversed(messages) if isinstance(m, dict) and m.get("role") == "user"),
        "",
    )
    if kwargs.get("tools") and "roll" in last_user.lower():
        return FakeMessage(tool_calls=[FakeToolCall("call_1", "roll_dice", {"sides": 6})])
    if kwargs.get("tools") and "note" in last_user.lower():
        return FakeMessage(tool_calls=[FakeToolCall("call_1", "read_note", {"name": "today.txt"})])
    return FakeMessage(content="[fake direct reply, no tool needed]")


def run(path: Path):
    results = []

    try:
        with fake_openai(_reply):
            module = import_module_from_path("lounge09_target", path)
    except Exception as e:  # noqa: BLE001
        results.append(("File imports without errors", False, f"{type(e).__name__}: {e}"))
        return results
    results.append(("File imports without errors", True, ""))

    tools = getattr(module, "TOOLS", None)
    names = {t.get("function", {}).get("name") for t in tools} if isinstance(tools, list) else set()
    ok = "roll_dice" in names
    results.append(("TOOLS advertises roll_dice", ok, f"TOOLS has {names!r}" if not ok else ""))
    ok = "read_note" in names
    results.append(("TOOLS advertises read_note", ok, f"TOOLS has {names!r}" if not ok else ""))

    run_showcase = getattr(module, "run_showcase", None)
    if run_showcase is None:
        results.append(("Defines run_showcase(question)", False, "function not found"))
        return results
    results.append(("Defines run_showcase(question)", True, ""))

    try:
        with fake_openai(_reply):
            dice_answer = run_showcase("Roll a dice for me.")
        ok = isinstance(dice_answer, str) and len(dice_answer) > 0
        results.append(("run_showcase handles the dice tool", ok, "" if ok else f"got {dice_answer!r}"))
    except Exception as e:  # noqa: BLE001
        results.append(("run_showcase handles the dice tool", False, f"{type(e).__name__}: {e}"))

    try:
        with fake_openai(_reply):
            note_answer = run_showcase("What's today's note say?")
        ok = isinstance(note_answer, str) and len(note_answer) > 0
        results.append(("run_showcase handles the note tool", ok, "" if ok else f"got {note_answer!r}"))
    except Exception as e:  # noqa: BLE001
        results.append(("run_showcase handles the note tool", False, f"{type(e).__name__}: {e}"))

    return results
