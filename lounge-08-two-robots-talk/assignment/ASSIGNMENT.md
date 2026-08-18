# Assignment: Inventor and Safety Tester

Build two agents that improve an invention together: an imaginative inventor
proposes ideas, and a careful safety tester challenges them.

Create `assignment/invention_team.py` from scratch. Do not edit the lounge
conversation template.

## Requirements

1. Ask the user for an invention problem to solve.
2. The inventor proposes one design.
3. The safety tester identifies one risk and asks one question.
4. The inventor revises the design using that feedback.
5. Run three review rounds and preserve the complete transcript.
6. Print a final summary containing the design and unresolved risks.

## Boundaries

- The agents must not suggest weapons or dangerous experiments.
- The tester must challenge ideas respectfully.
- Every transcript line must identify its speaker and round.

## Evidence

```bash
python lounge-08-two-robots-talk/assignment/invention_team.py
```

- [ ] The final design differs from the first design.
- [ ] Every tester message affects the next inventor message.
- [ ] The transcript has the expected order and speaker labels.
- [ ] `assignment/role-map.md` explains each role in each agent's history.
