# Day 10 — Personal Agent: Yoyo

## Goal
Record the user's daily tasks, remind them, and carry unfinished ones to the next day.

## MVP scope (now)
- Store tasks in a local file (JSON) — real Google Calendar / push later
- Commands: add, list, done, snooze, delete, remind
- Short-term: today's list (session)
- Long-term: weekly tasks + leftovers from yesterday (file)

## Tools (MVP)
- `add_task(title, day)`
- `list_tasks(day?)`
- `complete_task(id)`
- `snooze_task(id)` → move to tomorrow
- `delete_task(id)`
- `remind_today()` → today + carried over from yesterday


## Memory
- Short-term: which commands ran in this chat / today's view
- Long-term: `tasks.json` (weekly + snoozed tasks)

## Success criteria
1. A task not completed yesterday shows up again today via `remind` / `list`
2. After `snooze`, the task is on tomorrow's list; after `delete`, it is gone

## Showcase (30 sec)
"Yoyo keeps my weekly tasks. Demo: I added a task → listed it → snoozed one I didn't do → next day the remind showed that task again. Memory is in a file; notifications/calendar come in the next version."
