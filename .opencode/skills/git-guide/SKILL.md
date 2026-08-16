---
name: git-guide
description: "Guide safe everyday Git work. Use for status checks, diffs, branches, commits, merge conflicts, or explaining Git commands without losing work."
compatibility: opencode
metadata:
  workflow: version-control
  tool: git
---

# Git Guide

## Steps

1. Run `git status --short` before proposing a change.
2. Explain tracked, untracked, staged, and modified files in plain language.
3. Inspect the relevant diff before staging or committing.
4. Keep unrelated changes separate.
5. Use non-destructive commands by default.
6. Ask before commits, pushes, branch changes, resets, or deleting files.
7. After an operation, run status again and summarize the result.

Never discard changes with `reset --hard`, checkout restoration, or clean commands unless the user explicitly requests it and understands what will be lost.