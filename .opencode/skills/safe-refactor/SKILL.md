---
name: safe-refactor
description: "Improve code structure without changing behavior. Use for renaming, extracting functions, reducing duplication, simplifying control flow, or organizing code safely."
compatibility: opencode
metadata:
  workflow: refactoring
  priority: behavior
---

# Safe Refactor

## Steps

1. State the behavior that must stay unchanged.
2. Run the narrowest existing check to establish a baseline.
3. Choose one small structural change.
4. Preserve public names and data formats unless changing them is required.
5. Make the edit without mixing in unrelated fixes.
6. Rerun the same check immediately.
7. Continue one small step at a time, validating after each step.

Stop and explain the blocker when there is no reliable way to verify preserved behavior.