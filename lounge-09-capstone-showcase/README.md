# Lounge 9 — Capstone Showcase

**Tier:** Capstone · **Uses:** OpenAI API, MCP, Agents, AGENTS.md, SKILL.md, opencode · **Time:** 60 minutes

One agent, everything you've learned, presented live to the lounge.

## 60-minute class plan
- **5 min:** Pick a project and map the starter.
- **10 min:** Write the persona and resource data.
- **15 min:** Advertise both provided tools.
- **10 min:** Complete the second model call.
- **10 min:** Code and register one original tool.
- **5 min:** Run the harness and test questions.
- **5 min:** Present the working agent.

## Capstone project ideas

Pick one (or invent your own — these are just starting points):

| # | Project | Persona | Tool | MCP resource |
|---|---|---|---|---|
| 1 | **Weather Wizard** | A dramatic meteorologist who speaks in prophecy | `get_weather(city)` returning a fake forecast | `locations.txt` listing cities the wizard knows |
| 2 | **Quiz Champion** | An enthusiastic game show host | `roll_dice(sides)` for score bonuses | `questions.txt` with trivia questions to read |
| 3 | **Space Explorer** | A calm, curious astronaut on a long mission | `flip_coin()` to decide which planet to visit | `mission_log.txt` to read and update |
| 4 | **Chef's Assistant** | A cheerful chef who never gives up on bad recipes | `random_ingredient()` returning a surprise item | `recipes.txt` listing dishes to look up |
| 5 | **Story Generator** | A storyteller who speaks in riddles | `pick_word(category)` returning a random noun/verb | `story_starts.txt` with opening lines to read |
| 6 | **Daily Planner** | A hyper-organised assistant who loves bullet points | `flip_coin()` to randomly prioritise tasks | `tasks.txt` to read today's task list from |
| 7 | **Trivia Machine** | A know-it-all robot who admits when it guesses | `roll_dice(sides)` to pick a random question number | `trivia.txt` with questions and answers |
| 8 | **Fortune Teller** | A mysterious oracle who speaks in riddles | `random_number(max)` for fortune numbers | `fortunes.txt` to read prophecies from |

**Not sure which to pick?** Choose the one whose *persona* sounds most fun to you — the tools and MCP part are almost the same for all of them.

## Checklist
- [ ] Read `working/showcase_agent.py` carefully — it is your map.
      Identify which lines come from Lounge 2 (persona), which from
      Lounge 5 (tool), and which from Lounge 6 (MCP read). Mark them
      with a comment if it helps.
- [ ] In the template, write your own `SYSTEM_PROMPT` — a persona that
      is *different* from `working/`'s "Lounge Bot". Give it a name,
      a job, and at least 2 personality traits.
- [ ] Update `NOTES` with a note that fits your persona — not the
      default "Welcome" text.
- [ ] Fill in the `TOOLS` list to advertise both `roll_dice` and
      `read_note` so the model knows about them.
- [ ] Fill in the second API call and the return value at the bottom of
      `run_showcase`.
- [ ] Run the harness:
      `python harness/check.py lounge09 --file lounge-09-capstone-showcase/template/showcase_agent_template.py`
- [ ] Run the template with a real key. Check all 3 test questions in
      `__main__` produce sensible output that fits your persona's voice.
- [ ] Add a **third tool** of your own invention to the template (any
      small Python function — generate a random colour, pick a random
      word, calculate something). Register it in `TOOLS` and
      `AVAILABLE_FUNCTIONS`, then add a 4th test question that uses it.
- [ ] Write an `AGENTS.md` for your capstone agent (at least Who/Can/Never
      + 2 examples).
- [ ] Present your finished agent to the lounge: show what it does,
      name the Lounges it uses, and share one thing that surprised you
      while building it.

## Check your work
```bash
python harness/check.py lounge09 --file lounge-09-capstone-showcase/template/showcase_agent_template.py
```

## Debugging challenge
`broken/showcase_agent_broken.py` has **3 bugs**, one from each
earlier lounge's bug family. If you've done those lounges already,
you've seen each of these once before.

1. **Bug 1 — tool never registered (Lounge 5 style):** `read_note` is
   in `AVAILABLE_FUNCTIONS` but is *not* in `TOOLS`. The model will
   never call it because it doesn't know it exists. Add the missing
   tool description.
2. **Bug 2 — crash from wrong-case attribute (Lounge 5 style):** When
   the code dispatches a tool call, it reads an attribute name with the
   wrong capitalisation. Python will raise `AttributeError`. Find
   `.Name` and correct it to `.name`.
3. **Bug 3 — missing message append (Lounge 8 style):** After all tool
   calls complete, the assistant's original reply message is never
   appended to `messages` before the second API call, so the model
   doesn't see its own tool request. Add the missing append.

Fix them in order. Re-run after each one.

## Go deeper
- **Full integration run:** Open your capstone agent in opencode and
  have a real conversation with it — at least 5 back-and-forth turns.
  Include at least one tool-triggering question and one note-reading
  question.
- **Skill link:** Write a `SKILL.md` for your third tool and link it
  from your `AGENTS.md`. Ask opencode to use the skill by name.
- **Capstone remix:** Take a classmate's Lounge 2 persona and swap it
  into your showcase agent in place of your own. Does the persona
  change feel natural? What breaks?

## Reflect
Write your answers in a `capstone-notes.md` file:

1. You built this agent across 8 lounges, one piece at a time. Which
   single piece — persona, tool, or MCP read — makes the biggest
   difference to what the agent can do? Why?
2. What would you add to your capstone agent if you had one more hour?
   Be specific: what feature, what file, what function?
