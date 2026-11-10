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
- `courses.level` (smallint, 100 to 500): set by `load.py` from the course file's `level`, or from the first digit of the course number. Groups the Courses page.
- `notifications` (new): id, student_id, kind, title, body, link, created_at, read_at. Students read their own and can set `read_at` only. Add a unique index on student_id, kind and the date part of created_at, so each kind fires at most once a day.
- `generate_reminders()` (new, security definer, uses `auth.uid()`): called by the dashboard on load. Inserts, at most once a day each:
  - `streak_at_risk`: today is one of the student's study days, it is past their preferred time, and nothing is logged today
  - `inactive_3_days`: no quiz or study log in 3 days
  - `daily_goal_reached`: today's minutes reached the daily goal
  - `score_improved`: the latest attempt on a topic beat the previous one by 20 points or more
- `knowledge_base_stats` (view): counts of courses, topics, resources by type, and approved questions, for the Knowledge Base page.

- `course_requests` (25 Oct): student_id, code, title, level, semester, lecturer, details, status (pending, added, declined), admin_note, course_id. Students read and create their own; a column grant lets them fill in only the request, so status and outcome are set by `scripts/course_requests.py` with the service role. Notification kind `course_added` tells them the course is ready.
- `resources.type` (25 Oct) also allows `textbook`: reading cards from `content/textbooks/`.
- `enrollments` (Phase 9): student_id, course_id, created_at. Students read, add and remove their own rows. A trigger on `profiles` enrols every new profile in the reviewed courses. The ML service only recommends for enrolled courses.

- `app_settings` (3 Nov): key, value (jsonb), description. Students can read it; nobody but the service role writes it. Holds `cold_start_threshold` (3), the one value for the recommendation stages.
- Stage functions (3 Nov): `recommendation_stages(student)` (each enrolled course's stage: 1 no diagnostic, 2 diagnostic below the threshold, 3 at or above), `diagnostic_recommendations(student)` (the Stage 2 list) and `cold_start_recommendations(student, course)`, for the service role only; `refresh_fallback_recommendations()` (security definer, `auth.uid()`), which the web app calls when the ML service is down; `cold_start_threshold()` for signed-in students. `recommendations.source` also allows `diagnostic`.
- Gamification (4 Nov): `student_badges` (student_id, badge, earned_at, seen_at); students read their own and never write it. `gamification_for(student, p_now)` computes the streak card (Lagos days, streak, freezes, XP, strip, badges) without writing anything, for the service role and tests; `sync_student_badges(student)` stores newly earned badges (service role); `my_gamification()` and `acknowledge_badges(badges)` for signed-in students. `study_logs.logged_at` is no longer insertable by students (defaults to now()). `generate_reminders()`'s streak-at-risk now counts quizzes too and says "keep your N-day streak".
- `resources.link_type` (4 Nov): `free`, `buy` or `preview` for a textbook's link (`url`); a check makes it need a url. `also_recommended()` returns it.
- Email reminders (4 Nov): `profiles.email_reminders` (default false), `email_streak`, `email_digest`, `email_weekly` (default true), all student-editable. `email_log` (student_id, kind, day, subject, status sent/dry_run/failed, error, to_self, sent_at): students read their own, only the service role writes; a unique index on student, kind and day (not failed, not to_self) makes each kind at most once a day. `email_recipients()` (opted-in, non-simulated students with their auth email) and `topic_progress_for(student)` are service role only.
- Course management (10 Nov): `profiles.role` (student, course_manager; no student grant). `is_course_manager()`. `course_requests.status` adds `in_progress`; students may insert the `id` so files can be uploaded under it; managers read every request. `course_request_files` (request_id, student_id, path, name, size_bytes, content_type; max 5 per request by trigger) with the private Storage bucket `course-request-files` (20 MB, PDF/DOCX/PPTX/images; students upload to `<uid>/...` and read their own; managers read all). `questions.status` adds `hidden`. Notification kinds `course_request_in_progress`, `course_request_declined`. `content_audit` (actor_id, action, table_name, row_id, summary, changes {field: {from, to}}): managers read, only functions write. Manager functions, each checking the role and auditing: `manage_requests`, `manage_set_request_status`, `manage_update_topic`, `manage_questions`, `manage_update_question` (shape checked by `question_shape_ok`), `manage_set_question_hidden`, `manage_save_resource`, `manage_set_course_reviewed`, `manage_audit`.

## Demo data

- The demo accounts get realistic names (Tolu Adeyemi for the active student, Kemi Balogun for the new student, Ngozi Eze for the Stage 2 student), department Computer Science, level 500, and reminder settings filled in.
- The three demo accounts have email reminders on (their addresses are on example.com, so they only ever get dry runs).
- Seed a few read and unread notifications for the active demo account so the bell shows a count in screenshots.
