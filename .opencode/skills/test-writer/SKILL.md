---
name: test-writer
description: "Design and write focused automated tests. Use when adding test coverage, reproducing a bug, checking edge cases, or teaching how tests prove behavior."
compatibility: opencode
metadata:
  workflow: testing
  scope: code
---

# Test Writer

## Steps

1. Write down the behavior to prove in plain language.
2. Find the repository's test framework and a nearby test example.
3. Add the smallest test that fails for the reported problem.
4. Keep setup short and make the expected result obvious.
5. Run only the new or nearest test first.
6. Fix the implementation separately from the expectation.
7. Rerun the focused test, then the relevant test group.

## Test Cases

Consider a normal input, an empty or boundary input, and one invalid input when each is meaningful. Avoid tests that only repeat implementation details.