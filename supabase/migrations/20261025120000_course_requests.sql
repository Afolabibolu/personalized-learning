-- Course requests (scalability): a student who cannot find a course asks for it.
-- The course is then added through the ingestion pipeline (content/CLAUDE.md), and
-- scripts/course_requests.py marks the request added, enrols the student and
-- sends them a notification. Students read and create their own requests only;
-- the status is set by the admin script (service role), never by students.

create table public.course_requests (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.profiles (id) on delete cascade,
  code text not null check (length(trim(code)) between 2 and 20),
  title text not null check (length(trim(title)) between 2 and 200),
  level smallint check (level in (100, 200, 300, 400, 500)),
  semester smallint check (semester in (1, 2)),
  lecturer text check (length(lecturer) <= 200),
  details text check (length(details) <= 2000),
  status text not null default 'pending' check (status in ('pending', 'added', 'declined')),
  admin_note text,
  course_id uuid references public.courses (id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index course_requests_student_id_idx on public.course_requests (student_id, created_at desc);

alter table public.course_requests enable row level security;

create policy "course_requests: read own" on public.course_requests
  for select to authenticated using (student_id = (select auth.uid()));
create policy "course_requests: create own" on public.course_requests
  for insert to authenticated with check (student_id = (select auth.uid()) and status = 'pending');

grant select on public.course_requests to authenticated;
-- Students can only fill in the request itself, never its status or outcome.
grant insert (student_id, code, title, level, semester, lecturer, details) on public.course_requests to authenticated;

-- Tells the student when their course is ready.
alter table public.notifications drop constraint notifications_kind_check;
alter table public.notifications add constraint notifications_kind_check check (kind in (
  'streak_at_risk', 'inactive_3_days', 'daily_goal_reached', 'score_improved',
  'new_recommendations', 'weak_topic_unstudied', 'course_added'
));
