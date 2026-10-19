-- FR6: reminder settings, a notifications centre, reminders generated from
-- stored dates, and per-topic progress (latest vs previous score).
-- "Today" and the preferred study time are in Nigerian time (Africa/Lagos).

-- Reminder settings, editable by the student (column grant, like the other profile fields).
alter table public.profiles
  add column study_days text[] not null default array['mon', 'tue', 'wed', 'thu', 'fri']
    check (study_days <@ array['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']),
  add column preferred_study_time time not null default '18:00',
  add column daily_goal_minutes int not null default 30 check (daily_goal_minutes between 5 and 600),
  add column browser_notifications boolean not null default false;

grant update (study_days, preferred_study_time, daily_goal_minutes, browser_notifications)
  on public.profiles to authenticated;

-- Notifications: students read their own and can only set read_at.
create table public.notifications (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.profiles (id) on delete cascade,
  kind text not null check (kind in (
    'streak_at_risk', 'inactive_3_days', 'daily_goal_reached', 'score_improved',
    'new_recommendations', 'weak_topic_unstudied'
  )),
  title text not null,
  body text not null,
  link text,
  created_at timestamptz not null default now(),
  read_at timestamptz
);
create index notifications_student_id_idx on public.notifications (student_id, created_at desc);
-- Each kind fires at most once a day per student.
create unique index notifications_once_per_day
  on public.notifications (student_id, kind, ((created_at at time zone 'Africa/Lagos')::date));

alter table public.notifications enable row level security;
grant select on public.notifications to authenticated;
grant update (read_at) on public.notifications to authenticated;

create policy "notifications: read own" on public.notifications
  for select to authenticated using (student_id = (select auth.uid()));
create policy "notifications: mark own read" on public.notifications
  for update to authenticated
  using (student_id = (select auth.uid())) with check (student_id = (select auth.uid()));

-- Latest and previous score per topic for the signed-in student.
create or replace function public.get_topic_progress()
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
    where a.student_id = auth.uid() and a.completed_at is not null
    group by q.topic_id, a.id, a.completed_at
  ),
  ranked as (
    select *, row_number() over (partition by topic_id order by completed_at desc) as n
    from per_attempt
  )
  select l.topic_id, l.score, p.score, l.completed_at
  from ranked l
  left join ranked p on p.topic_id = l.topic_id and p.n = 2
  where l.n = 1;
$$;

revoke execute on function public.get_topic_progress() from public, anon;
grant execute on function public.get_topic_progress() to authenticated;

-- Reminders computed from stored dates; called by the dashboard on load.
-- Inserts at most one of each kind per day and returns the unread count.
create or replace function public.generate_reminders()
returns int
language plpgsql
volatile
security definer
set search_path = ''
as $$
declare
  v_uid uuid := auth.uid();
  v_profile public.profiles;
  v_now timestamp := now() at time zone 'Africa/Lagos';
  v_today date := (now() at time zone 'Africa/Lagos')::date;
  v_last_activity timestamptz;
  v_today_minutes int;
  v_logged_today boolean;
  v_best record;
  v_days int;
begin
  if v_uid is null then
    raise exception 'not signed in' using errcode = '42501';
  end if;
  select * into v_profile from public.profiles where id = v_uid;

  select greatest(
    (select max(logged_at) from public.study_logs where student_id = v_uid),
    (select max(completed_at) from public.quiz_attempts where student_id = v_uid)
  ) into v_last_activity;

  select coalesce(sum(duration_minutes), 0)::int, count(*) > 0
  into v_today_minutes, v_logged_today
  from public.study_logs
  where student_id = v_uid and (logged_at at time zone 'Africa/Lagos')::date = v_today;

  -- Streak at risk: a study day, past the preferred time, nothing logged today.
  if lower(to_char(v_today, 'dy')) = any (v_profile.study_days)
     and v_now::time >= v_profile.preferred_study_time
     and not v_logged_today then
    insert into public.notifications (student_id, kind, title, body, link)
    values (v_uid, 'streak_at_risk', 'Keep your streak going',
            format('You planned to study today at %s. A short session keeps your streak alive.',
                   to_char(v_profile.preferred_study_time, 'HH24:MI')),
            '/log')
    on conflict do nothing;
  end if;

  -- No quiz or study log in 3 days (or none at all, 3 days after joining).
  v_days := floor(extract(epoch from now() - coalesce(v_last_activity, v_profile.created_at)) / 86400);
  if v_days >= 3 then
    insert into public.notifications (student_id, kind, title, body, link)
    values (v_uid, 'inactive_3_days', 'Time to get back to it',
            case when v_last_activity is null
              then 'You have not taken a quiz or logged a study session yet. The diagnostic quiz is a good start.'
              else format('No quiz or study session in %s days. Pick up where you left off.', v_days) end,
            case when v_last_activity is null then '/courses' else '/' end)
    on conflict do nothing;
  end if;

  -- Daily goal reached.
  if v_today_minutes >= v_profile.daily_goal_minutes then
    insert into public.notifications (student_id, kind, title, body, link)
    values (v_uid, 'daily_goal_reached', 'Daily goal reached',
            format('You studied %s minutes today (goal: %s). Nice work.', v_today_minutes, v_profile.daily_goal_minutes),
            '/')
    on conflict do nothing;
  end if;

  -- Score improved by 20 points or more on today's latest attempt.
  select t.title, p.topic_id, p.previous_score, p.latest_score
  into v_best
  from public.get_topic_progress() p
  join public.topics t on t.id = p.topic_id
  where p.previous_score is not null
    and p.latest_score - p.previous_score >= 20
    and (p.latest_completed_at at time zone 'Africa/Lagos')::date = v_today
  order by p.latest_score - p.previous_score desc
  limit 1;
  if found then
    insert into public.notifications (student_id, kind, title, body, link)
    values (v_uid, 'score_improved', 'Score improved',
            format('%s: %s%% to %s%%, up %s points.', v_best.title, round(v_best.previous_score),
                   round(v_best.latest_score), round(v_best.latest_score - v_best.previous_score)),
            '/topics/' || v_best.topic_id)
    on conflict do nothing;
  end if;

  return (select count(*) from public.notifications where student_id = v_uid and read_at is null);
end;
$$;

revoke execute on function public.generate_reminders() from public, anon;
grant execute on function public.generate_reminders() to authenticated;
