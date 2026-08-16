"""Lounge 1 — First Contact."""

from pathlib import Path

from harness.util import fake_openai, import_module_from_path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TARGET = ROOT / "lounge-01-first-contact" / "template" / "first_contact_template.py"


def run(path: Path):
    results = []

    try:
        with fake_openai():
            module = import_module_from_path("lounge01_target", path)
    except Exception as e:  # noqa: BLE001
        results.append(("File imports without errors", False, f"{type(e).__name__}: {e}"))
        return results
    results.append(("File imports without errors", True, ""))

    fn = getattr(module, "ask_the_model", None)
    if fn is None:
        results.append(("Defines ask_the_model(question)", False, "function not found"))
        return results
    results.append(("Defines ask_the_model(question)", True, ""))

    try:
        with fake_openai():
            reply = fn("Hello, I'm a Coding Lounge builder!")
        ok = isinstance(reply, str) and len(reply) > 0
        results.append(("ask_the_model returns real text back", ok, "" if ok else f"got {reply!r}"))
    except Exception as e:  # noqa: BLE001
        results.append(("ask_the_model returns real text back", False, f"{type(e).__name__}: {e}"))

    return results
