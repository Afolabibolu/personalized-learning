-- Email reminders (Prompt 6): sent by the Python service through Gmail SMTP to the
-- address a student signed up with, only if they opt in. Off for everyone already
-- signed up; new students are asked once during onboarding.

alter table public.profiles
  add column email_reminders boolean not null default false,
  add column email_streak boolean not null default true,   -- streak at risk
  add column email_digest boolean not null default true,   -- weak topics and new recommendations, one a day
  add column email_weekly boolean not null default true;   -- Sunday-evening summary

grant update (email_reminders, email_streak, email_digest, email_weekly) on public.profiles to authenticated;

-- Every email, sent or not. Students read their own; only the service role writes.
create table public.email_log (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.profiles (id) on delete cascade,
  kind text not null check (kind in ('streak_at_risk', 'digest', 'weekly_summary')),
  day date not null,                     -- the Nigerian (Africa/Lagos) day it belongs to
  subject text not null,
  status text not null check (status in ('sent', 'dry_run', 'failed')),
  error text,
  to_self boolean not null default false, -- test sends to SMTP_USER instead of the student
  sent_at timestamptz not null default now()
);
create index email_log_student_id_idx on public.email_log (student_id, sent_at desc);
-- Never the same kind to the same student twice on the same day (failed attempts do not count).
create unique index email_log_once_per_day on public.email_log (student_id, kind, day) where status <> 'failed';

alter table public.email_log enable row level security;
grant select on public.email_log to authenticated;
create policy "email_log: read own" on public.email_log
  for select to authenticated using (student_id = (select auth.uid()));

-- Students who opted in, with the address they signed up with. Service role only.
create or replace function public.email_recipients()
returns table (
  student_id uuid, email text, full_name text, study_days text[], preferred_study_time time,
  email_streak boolean, email_digest boolean, email_weekly boolean
)
language sql
stable
security definer
set search_path = ''
as $$
  select p.id, u.email::text, p.full_name, p.study_days, p.preferred_study_time,
         p.email_streak, p.email_digest, p.email_weekly
  from public.profiles p
  join auth.users u on u.id = p.id
  where p.email_reminders and not p.is_simulated and u.email is not null;
$$;

-- Latest and previous score per topic for one student (get_topic_progress, for the service role).
create or replace function public.topic_progress_for(p_student uuid)
returns table (topic_id uuid, latest_score numeric, previous_score numeric, latest_completed_at timestamptz)
language sql
stable
security definer
set search_path = ''
as $$
  with per_attempt as (
    select q.topic_id, a.completed_at,
           round(100.0 * count(*) filter (where aa.is_correct) / count(*), 2) as score
    from public.quiz_attempts a
    join public.attempt_answers aa on aa.attempt_id = a.id
    join public.questions q on q.id = aa.question_id
    where a.student_id = p_student and a.completed_at is not null
    group by q.topic_id, a.id, a.completed_at
  ),
  ranked as (
    select *, row_number() over (partition by topic_id order by completed_at desc) as n from per_attempt
  )
  select l.topic_id, l.score, p.score, l.completed_at
  from ranked l
  left join ranked p on p.topic_id = l.topic_id and p.n = 2
  where l.n = 1;
$$;

revoke execute on function public.email_recipients() from public, anon, authenticated;
revoke execute on function public.topic_progress_for(uuid) from public, anon, authenticated;
grant execute on function public.email_recipients() to service_role;
grant execute on function public.topic_progress_for(uuid) to service_role;
