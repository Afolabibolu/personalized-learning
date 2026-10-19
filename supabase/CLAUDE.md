# supabase/: schema, security and SQL functions

Read the root CLAUDE.md first. This file adds the rules for the database only.

## Rules

- Every change is a new file in `supabase/migrations/`. Never edit an applied migration.
- Every new table gets RLS in the same migration. Students only read and write their own rows.
- After any change to policies, run `scripts/rls_check.py` and extend it to cover the new table.

## Additions for the requirement gaps

- `profiles`: add `study_days` (list of weekdays), `preferred_study_time` (time), `daily_goal_minutes` (integer, default 30), `browser_notifications` (boolean, default false). Students update their own row.
- `recommendations`: add `explanation` (jsonb), written by the ML service only.
- `courses`: add `is_reviewed` (boolean, default true). Courses added by the ingestion pipeline are false.
- `notifications` (new): id, student_id, kind, title, body, link, created_at, read_at. Students read their own and can set `read_at` only. Add a unique index on student_id, kind and the date part of created_at, so each kind fires at most once a day.
- `generate_reminders()` (new, security definer, uses `auth.uid()`): called by the dashboard on load. Inserts, at most once a day each:
  - `streak_at_risk`: today is one of the student's study days, it is past their preferred time, and nothing is logged today
  - `inactive_3_days`: no quiz or study log in 3 days
  - `daily_goal_reached`: today's minutes reached the daily goal
  - `score_improved`: the latest attempt on a topic beat the previous one by 20 points or more
- `knowledge_base_stats` (view): counts of courses, topics, resources by type, and approved questions, for the Knowledge Base page.

## Demo data

- The demo accounts get realistic names (for example Tolu Adeyemi for the active student, Kemi Balogun for the new student), department Computer Science, level 500, and reminder settings filled in.
- Seed a few read and unread notifications for the active demo account so the bell shows a count in screenshots.
