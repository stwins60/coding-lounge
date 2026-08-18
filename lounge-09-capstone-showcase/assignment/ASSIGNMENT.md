# Assignment: Escape Room Director

Build a complete agent that hosts a safe, text-based escape room for a team.

Create the project from scratch inside `assignment/escape-room/`. Do not edit
or copy the capstone template.

## Components

- `director.py`: the agent and tool-calling loop.
- `AGENTS.md`: the director's identity, abilities, and safety rules.
- `puzzles.md`: at least three original puzzles and their hints.
- `demo-notes.md`: test evidence and presentation notes.

## Requirements

1. Give the director a mysterious but encouraging persona.
2. Expose a tool that checks an answer without revealing it first.
3. Expose a tool that selects a puzzle by difficulty.
4. Read puzzle text and hints from the resource file.
5. Track solved puzzle IDs during the running program.
6. Offer a hint after two incorrect attempts.
7. Finish with a short team celebration and score summary.

## Boundaries

- Do not use real locks, locations, personal information, or dangerous tasks.
- Normalize answers before comparing them.
- Never print all puzzle answers during normal play.
- Keep API keys in `.env` only.

## Evidence

- [ ] Easy and hard puzzle requests select suitable resources.
- [ ] Correct and incorrect answers follow different paths.
- [ ] A hint appears only after two incorrect attempts.
- [ ] Solved puzzles remain solved during the session.
- [ ] The presentation demonstrates persona, tools, resources, and state.
