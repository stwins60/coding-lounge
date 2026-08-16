---
name: code-reviewer
description: "Review code for bugs, regressions, risky behavior, unclear logic, and missing tests. Use when asked to review a file, change, patch, or project before sharing it."
compatibility: opencode
metadata:
  workflow: review
  output: findings
---

# Code Reviewer

## Steps

1. Understand the intended behavior and inspect the changed code.
2. Trace inputs, outputs, errors, and important state changes.
3. Check call sites and focused tests when needed.
4. Report findings first, ordered from most serious to least serious.
5. Give each finding a file, line, impact, and concrete reason.
6. Separate confirmed defects from questions or assumptions.
7. Mention missing test coverage and residual risk.

Do not fill the review with style preferences. If there are no findings, say so clearly and list any checks that were not run.