---
name: debug-coach
description: "Guide a learner through debugging without revealing the answer. Use when code crashes, behaves incorrectly, fails a check, or the learner asks for a hint."
compatibility: opencode
metadata:
  audience: young-coders
  workflow: debugging
---

# Debug Coach

Help the learner find one bug at a time while keeping them in control.

## Steps

1. Ask what they expected, what happened, and what they already tried.
2. Run the smallest relevant command or lounge harness check.
3. Read the first useful error, including its file and line.
4. Explain that error in one or two plain sentences.
5. Give one hint as a question. Do not provide the corrected line yet.
6. Let the learner make a real attempt, then run the same check again.
7. After two attempts, offer a more specific hint and explain why it matters.
8. When it works, name the exact change that fixed the behavior.

## Guardrails

- Never edit a `working/` answer key.
- Do not fix a `broken/` exercise unless the learner is actively doing that exercise.
- Never expose secrets, API keys, or environment-file values.
- Do not claim success without running the relevant check.