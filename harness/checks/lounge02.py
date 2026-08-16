"""Lounge 2 — Give It a Personality."""

from pathlib import Path

from harness.util import fake_openai, import_module_from_path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TARGET = ROOT / "lounge-02-give-it-a-personality" / "template" / "persona_template.py"


def run(path: Path):
    results = []

    try:
        with fake_openai():
            module = import_module_from_path("lounge02_target", path)
    except Exception as e:  # noqa: BLE001
        results.append(("File imports without errors", False, f"{type(e).__name__}: {e}"))
        return results
    results.append(("File imports without errors", True, ""))

    prompt = getattr(module, "SYSTEM_PROMPT", None)
    ok = isinstance(prompt, str) and len(prompt.strip()) >= 20
    results.append(
        ("SYSTEM_PROMPT is a real persona (20+ characters)", ok, "" if ok else f"got {prompt!r}")
    )

    fn = getattr(module, "ask_persona", None)
    if fn is None:
        results.append(("Defines ask_persona(question)", False, "function not found"))
        return results
    results.append(("Defines ask_persona(question)", True, ""))

    try:
        with fake_openai():
            reply = fn("What's your favorite Earth food?")
        ok = isinstance(reply, str) and len(reply) > 0
        results.append(("ask_persona returns real text back", ok, "" if ok else f"got {reply!r}"))
    except Exception as e:  # noqa: BLE001
        results.append(("ask_persona returns real text back", False, f"{type(e).__name__}: {e}"))

    return results
