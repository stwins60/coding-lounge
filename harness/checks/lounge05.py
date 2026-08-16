"""Lounge 5 — Give It Hands (tool calling)."""

from pathlib import Path

from harness.util import fake_openai, import_module_from_path, tool_call_then_reply

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TARGET = ROOT / "lounge-05-give-it-hands" / "template" / "tool_agent_template.py"


def run(path: Path):
    results = []

    try:
        with fake_openai():
            module = import_module_from_path("lounge05_target", path)
    except Exception as e:  # noqa: BLE001
        results.append(("File imports without errors", False, f"{type(e).__name__}: {e}"))
        return results
    results.append(("File imports without errors", True, ""))

    roll_dice = getattr(module, "roll_dice", None)
    if roll_dice is None:
        results.append(("Defines roll_dice(sides)", False, "function not found"))
    else:
        results.append(("Defines roll_dice(sides)", True, ""))
        try:
            value = roll_dice(sides=6)
            ok = isinstance(value, int) and 1 <= value <= 6
            results.append(("roll_dice(sides=6) returns 1-6", ok, "" if ok else f"got {value!r}"))
        except Exception as e:  # noqa: BLE001
            results.append(("roll_dice(sides=6) returns 1-6", False, f"{type(e).__name__}: {e}"))

    tools = getattr(module, "TOOLS", None)
    ok = isinstance(tools, list) and any(
        isinstance(t, dict) and t.get("function", {}).get("name") == "roll_dice" for t in tools
    )
    results.append(("TOOLS advertises roll_dice to the model", ok, "" if ok else "roll_dice missing from TOOLS"))

    handle_question = getattr(module, "handle_question", None)
    if handle_question is None:
        results.append(("Defines handle_question(question)", False, "function not found"))
        return results
    results.append(("Defines handle_question(question)", True, ""))

    reply_fn = tool_call_then_reply(
        tool_name="roll_dice",
        arguments={"sides": 6},
        final_text="You rolled a 4!",
    )
    try:
        with fake_openai(reply_fn):
            answer = handle_question("Roll a six-sided dice for me.")
        ok = isinstance(answer, str) and len(answer) > 0
        results.append(
            ("handle_question actually calls the tool and answers", ok, "" if ok else f"got {answer!r}")
        )
    except Exception as e:  # noqa: BLE001
        results.append(("handle_question actually calls the tool and answers", False, f"{type(e).__name__}: {e}"))

    return results
