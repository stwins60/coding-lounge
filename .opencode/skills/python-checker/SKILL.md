---
name: python-checker
description: "Check Python code with syntax checks, focused tests, and runtime evidence. Use for Python errors, validation, imports, type problems, or checking whether a change works."
compatibility: opencode
metadata:
  language: python
  workflow: validation
---

# Python Checker

## Steps

1. Identify the file and expected behavior.
2. Check syntax with `python -m py_compile <file>` when the file should parse.
3. Run the narrowest available test or Coding Lounge harness command.
4. Report the first actionable failure with its file and line.
5. Make or suggest one focused correction.
6. Rerun the same check before using a broader test command.
7. Report exactly which commands passed and which could not run.

## Safety

- Do not run unknown scripts before reading them.
- Do not print `.env` values or API keys.
- Do not install packages unless the project requires them and the learner agrees.