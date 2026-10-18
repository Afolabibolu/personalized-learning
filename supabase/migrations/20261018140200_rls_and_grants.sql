-- Row-level security on every table, plus table and column grants.
-- Grants decide which operations and columns a role may use at all;
-- policies decide which rows. anon gets nothing: every screen needs a login.

alter table public.profiles enable row level security;
alter table public.courses enable row level security;
alter table public.topics enable row level security;
alter table public.resources enable row level security;
alter table public.quizzes enable row level security;
alter table public.questions enable row level security;
alter table public.quiz_attempts enable row level security;
alter table public.attempt_answers enable row level security;
alter table public.study_logs enable row level security;
alter table public.recommendations enable row level security;

revoke all on all tables in schema public from anon, authenticated;

-- profiles: read and update own row. The row itself comes from the auth trigger,
-- and is_simulated is only set by the admin API.
grant select on public.profiles to authenticated;
grant update (full_name, department, level, learning_preferences) on public.profiles to authenticated;

create policy "profiles: read own" on public.profiles
  for select to authenticated using (id = (select auth.uid()));
create policy "profiles: update own" on public.profiles
  for update to authenticated
  using (id = (select auth.uid())) with check (id = (select auth.uid()));

-- Content is read-only for students.
grant select on public.courses, public.topics, public.resources, public.quizzes to authenticated;

create policy "courses: read all" on public.courses for select to authenticated using (true);
create policy "topics: read all" on public.topics for select to authenticated using (true);
create policy "resources: read all" on public.resources for select to authenticated using (true);
create policy "quizzes: read all" on public.quizzes for select to authenticated using (true);

-- questions: no grant and no policy. Students only see questions through
-- start_quiz (without answers) and the review after submit_quiz.

-- quiz_attempts and attempt_answers: read own. Only the quiz functions write.
grant select on public.quiz_attempts, public.attempt_answers to authenticated;

create policy "quiz_attempts: read own" on public.quiz_attempts
  for select to authenticated using (student_id = (select auth.uid()));
create policy "attempt_answers: read own" on public.attempt_answers
  for select to authenticated using (
    exists (
      select 1 from public.quiz_attempts a
      where a.id = attempt_id and a.student_id = (select auth.uid())
    )
  );

-- study_logs: read and create own.
grant select on public.study_logs to authenticated;
grant insert (student_id, topic_id, duration_minutes, activity_type, logged_at) on public.study_logs to authenticated;

create policy "study_logs: read own" on public.study_logs
  for select to authenticated using (student_id = (select auth.uid()));
create policy "study_logs: create own" on public.study_logs
  for insert to authenticated
  with check (student_id = (select auth.uid()) and logged_at <= now());

-- recommendations: read own, and change only the status column.
-- RLS cannot limit columns, so the column-level grant does that part.
grant select on public.recommendations to authenticated;
grant update (status) on public.recommendations to authenticated;

create policy "recommendations: read own" on public.recommendations
  for select to authenticated using (student_id = (select auth.uid()));
create policy "recommendations: update own status" on public.recommendations
  for update to authenticated
  using (student_id = (select auth.uid())) with check (student_id = (select auth.uid()));
