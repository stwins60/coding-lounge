# Assignment: Break-Time Planner Agent

Build an agent that uses Python tools to choose a short classroom break
activity based on the available time.

Create `assignment/break_planner.py` from scratch. Do not edit the lounge
template or reuse its dice and coin tools.

## Tools to Build

1. `pick_brain_break(minutes)` returns an activity that fits the time limit.
2. `pick_team_size(student_count)` returns fair group sizes.

Register both functions as model tools and dispatch calls by tool name.

## Requirements

- Reject zero or negative numbers with a helpful message.
- Print a short signal whenever a real Python tool runs.
- Let the model answer directly when no calculation or choice is needed.
- Test one request that requires both tools.

## Evidence

```bash
python lounge-05-give-it-hands/assignment/break_planner.py
```

- [ ] A two-minute request gets a suitably short activity.
- [ ] Seventeen students receive a sensible grouping suggestion.
- [ ] A combined request calls both tools.
- [ ] A greeting calls neither tool.
