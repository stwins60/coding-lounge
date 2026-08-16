"""Lounge 8 — Two Robots Talk.

Note: this harness can only catch some of the bugs. It replies based on
call order, not on what's actually in each agent's conversation history,
so it can't tell whether that history was threaded through correctly
turn to turn — that one needs a human (or the coding-lounge-guide skill)
reading the code with the learner. Say so if everything here passes but
the transcript still looks wrong when run for real.
"""

from pathlib import Path

from harness.util import FakeMessage, fake_openai, import_module_from_path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TARGET = ROOT / "lounge-08-two-robots-talk" / "template" / "duo_agents_template.py"


def _make_reply():
    """Alternate Q:/A: replies by call order, independent of persona names."""
    state = {"n": 0}

    def _reply(messages, kwargs):
        n = state["n"]
        state["n"] += 1
        return FakeMessage(content=f"Q: line {n}" if n % 2 == 0 else f"A: line {n}")

    return _reply


def run(path: Path):
    results = []

    try:
        with fake_openai(_make_reply()):
            module = import_module_from_path("lounge08_target", path)
    except Exception as e:  # noqa: BLE001
        results.append(("File imports without errors", False, f"{type(e).__name__}: {e}"))
        return results
    results.append(("File imports without errors", True, ""))

    run_conversation = getattr(module, "run_conversation", None)
    if run_conversation is None:
        results.append(("Defines run_conversation(rounds)", False, "function not found"))
        return results
    results.append(("Defines run_conversation(rounds)", True, ""))

    try:
        with fake_openai(_make_reply()):
            transcript = run_conversation(2)
        ok = isinstance(transcript, list) and len(transcript) == 4
        results.append(
            ("run_conversation(2) returns 4 lines (2 rounds x 2 speakers)", ok,
             f"got {len(transcript) if isinstance(transcript, list) else type(transcript)} item(s)" if not ok else "")
        )
        if ok:
            alternates = all(
                (transcript[i].startswith("Q:") if i % 2 == 0 else transcript[i].startswith("A:"))
                for i in range(4)
            )
            results.append(
                ("Both agents take turns in order", alternates,
                 "" if alternates else f"got {transcript!r}")
            )
    except Exception as e:  # noqa: BLE001
        results.append(("run_conversation(2) returns 4 lines (2 rounds x 2 speakers)", False, f"{type(e).__name__}: {e}"))

    return results
