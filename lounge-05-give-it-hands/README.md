# Lounge 5 — Give It Hands

**Tier:** Core build · **Uses:** OpenAI API, Agents · **Time:** 60 minutes

Wire up a real function the model can call instead of guessing the
answer.

## 60-minute class plan
- **5 min:** Trace the two-call tool flow.
- **15 min:** Implement and advertise `roll_dice`.
- **15 min:** Complete the second model call.
- **10 min:** Code and register `flip_coin`.
- **10 min:** Test tool and no-tool questions.
- **5 min:** Run the harness.

## Checklist
- [ ] Read `working/tool_agent.py` from top to bottom. Trace the flow:
      first API call → tool call detected → function runs → result
      added to messages → second API call → final reply. Understand each
      step before you open the template.
- [ ] In the template, implement `roll_dice(sides)` so it returns a
      real random integer between 1 and `sides` (inclusive).
- [ ] Fill in the `"description"` field inside `TOOLS` so the model
      knows when to use the tool (what it does, what the argument means).
- [ ] Fill in the second API call in `handle_question` and return the
      final reply.
- [ ] Run the harness:
      `python harness/check.py lounge05 --file lounge-05-give-it-hands/template/tool_agent_template.py`
- [ ] Run the template with a real key. Check the terminal output proves
      the tool was actually called (not just the model guessing a number).
      *Hint: add a `print("🎲 rolling…")` inside `roll_dice` as a signal.*
- [ ] Ask the same dice-roll question **5 times in a row**. Confirm the
      number is different each time — if it's always the same, the tool
      isn't being called.
- [ ] Add a **second tool** called `flip_coin()` that returns `"heads"`
      or `"tails"` randomly. Register it in `TOOLS` and `AVAILABLE_FUNCTIONS`.
- [ ] Ask a question that should use `flip_coin` and confirm the right
      tool was chosen (not `roll_dice`).
- [ ] Ask a question that needs neither tool (e.g. "What's the capital
      of France?") and confirm the model answers directly without calling
      any tool.

## Check your work
```bash
python harness/check.py lounge05 --file lounge-05-give-it-hands/template/tool_agent_template.py
```

## Debugging challenge
`broken/tool_agent_broken.py` has **3 bugs**. Read the whole file and
form a theory about each bug before making any change.

1. **Bug 1 — tool never registered:** `TOOLS` is an empty list. The
   model will never call `roll_dice` because it doesn't know the tool
   exists. Add the correct tool description.
2. **Bug 2 — crash on attribute access:** When a tool call comes back,
   the code reads an attribute name using the wrong case. Python
   attribute names are case-sensitive. Find the wrong-case name and
   fix it. (The harness catches this one.)
3. **Bug 3 — missing message append:** After the tool call completes,
   something is missing from the `messages` list before the second API
   call. The model won't have the full context it needs. Compare with
   the working version to spot what's absent.

Fix them one at a time and re-run after each fix.

## Go deeper
- **Tool registry helper:** Instead of manually maintaining
  `AVAILABLE_FUNCTIONS`, write a helper function or decorator that
  auto-registers a Python function as a tool when you define it.
- **Three tools, one question:** Add a third tool (e.g. `random_colour()`
  returning a colour name). Then craft a single user question that
  makes the model call all three tools in sequence.
- **No tool fallback message:** If the model answers directly (no tool
  calls), print a different prefix: `"(No tool used) "` before the
  reply. Confirm it appears for the France question but not for the
  dice question.

## Reflect
Write your answers in a `tool-notes.md` file next to your template:

1. Why does the code make **two** API calls instead of one when a tool
   is used? Draw or describe the message flow.
2. What would happen if you forgot to add the tool result to `messages`
   before the second call? What would the model say?
