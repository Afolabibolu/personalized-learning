-- Streaks, daily goal, XP, streak freezes and badges (Prompt 4).
-- Everything is computed here from quiz attempts and study logs, never in the
-- browser, so a student cannot fake it. Day boundaries are Nigerian time (Africa/Lagos).
--
-- Rules:
--   active day   a Lagos calendar day with a completed quiz or a logged study session
--   streak       consecutive active days ending today; if today has nothing yet, the run
--                ending yesterday still counts and is "at risk" (not 0)
--   freeze       one earned for every 7 active days in a run (7, 14, 21, ...), at most 2 held;
--                a missed day (before today) uses one automatically and the streak survives
--                (the frozen day keeps the run going but does not add to it)
--   XP           10 per completed quiz + 1 per correct answer; 1 per 5 minutes logged;
--                10 bonus on each day the daily goal (profiles.daily_goal_minutes) is met
--   badges       streak of 3, 7, 14, 30, 50, 100 days; first quiz; first 100% score;
--                5 topics mastered (latest score 70% or more)

-- Study logs are stamped by the database, so a missed day cannot be filled in later.
revoke insert on public.study_logs from authenticated;
grant insert (student_id, topic_id, duration_minutes, activity_type) on public.study_logs to authenticated;

-- Earned badges. Students read their own; only the functions below write them.
create table public.student_badges (
  student_id uuid not null references public.profiles (id) on delete cascade,
  badge text not null check (badge in (
    'streak_3', 'streak_7', 'streak_14', 'streak_30', 'streak_50', 'streak_100',
    'first_quiz', 'first_perfect', 'five_mastered'
  )),
  earned_at timestamptz not null,
  seen_at timestamptz,
  primary key (student_id, badge)
);

alter table public.student_badges enable row level security;
grant select on public.student_badges to authenticated;

create policy "student_badges: read own" on public.student_badges
  for select to authenticated using (student_id = (select auth.uid()));

-- The whole streak card for one student, as of p_now. Pure: writes nothing, so
-- tests can call it with any moment. Service role only.
create or replace function public.gamification_for(p_student uuid, p_now timestamptz default now())
returns jsonb
language plpgsql
stable
security definer
set search_path = ''
as $$
declare
  v_today date := (p_now at time zone 'Africa/Lagos')::date;
  v_goal int;
  v_first date;
  r record;
  v_run int := 0;
  v_longest int := 0;
  v_freezes int := 0;
  v_frozen date[] := '{}';       -- freezes used inside the current streak
  v_freezes_used int := 0;        -- all time
  v_day_xp int;
  v_xp_today int := 0;
  v_xp_week int := 0;
  v_xp_total int := 0;
  v_minutes_today int := 0;
  v_today_active boolean := false;
  v_first_today timestamptz;
  v_strip jsonb := '[]';
  v_badges jsonb := '[]';
  v_when timestamptz;
  v_mastered int;
begin
  select daily_goal_minutes into v_goal from public.profiles where id = p_student;
  v_goal := coalesce(v_goal, 30);

  v_first := least(
    (select min((logged_at at time zone 'Africa/Lagos')::date) from public.study_logs
     where student_id = p_student and logged_at <= p_now),
    (select min((completed_at at time zone 'Africa/Lagos')::date) from public.quiz_attempts
     where student_id = p_student and completed_at is not null and completed_at <= p_now));

  for r in
    with ev as (
      select (l.logged_at at time zone 'Africa/Lagos')::date as day, l.logged_at as at,
             l.duration_minutes as minutes, l.duration_minutes / 5 as xp
      from public.study_logs l
      where l.student_id = p_student and l.logged_at <= p_now
      union all
      select (a.completed_at at time zone 'Africa/Lagos')::date, a.completed_at, 0,
             10 + (select count(*) from public.attempt_answers aa where aa.attempt_id = a.id and aa.is_correct)::int
      from public.quiz_attempts a
      where a.student_id = p_student and a.completed_at is not null and a.completed_at <= p_now
    ),
    days as (
      select day, min(at) as first_at, sum(minutes)::int as minutes, sum(xp)::int as xp from ev group by day
    )
    select g::date as day, d.first_at, coalesce(d.minutes, 0) as minutes, coalesce(d.xp, 0) as xp,
           d.day is not null as active
    from generate_series(least(coalesce(v_first, v_today), v_today - 13), v_today, interval '1 day') g
    left join days d on d.day = g::date
    order by 1
  loop
    if r.active then
      v_run := v_run + 1;
      if v_run > v_longest then
        v_longest := v_run;
        if v_run in (3, 7, 14, 30, 50, 100) then
          v_badges := v_badges || jsonb_build_object('badge', 'streak_' || v_run, 'earned_at', r.first_at);
        end if;
      end if;
      if v_run % 7 = 0 and v_freezes < 2 then
        v_freezes := v_freezes + 1;
      end if;
    elsif r.day < v_today then
      if v_run > 0 and v_freezes > 0 then
        v_freezes := v_freezes - 1;
        v_freezes_used := v_freezes_used + 1;
        v_frozen := v_frozen || r.day;
      else
        v_run := 0;
        v_frozen := '{}';
      end if;
    end if;

    v_day_xp := r.xp + case when r.minutes >= v_goal then 10 else 0 end;
    v_xp_total := v_xp_total + v_day_xp;
    if r.day > v_today - 7 then
      v_xp_week := v_xp_week + v_day_xp;
    end if;
    if r.day = v_today then
      v_xp_today := v_day_xp;
      v_minutes_today := r.minutes;
      v_today_active := r.active;
      v_first_today := r.first_at;
    end if;
    if r.day > v_today - 14 then
      v_strip := v_strip || jsonb_build_object('day', r.day, 'active', r.active, 'frozen', r.day = any (v_frozen));
    end if;
  end loop;

  -- First quiz and first 100%.
  select min(completed_at) into v_when
  from public.quiz_attempts where student_id = p_student and completed_at is not null and completed_at <= p_now;
  if v_when is not null then
    v_badges := v_badges || jsonb_build_object('badge', 'first_quiz', 'earned_at', v_when);
  end if;
  select min(completed_at) into v_when
  from public.quiz_attempts
  where student_id = p_student and completed_at is not null and completed_at <= p_now and score >= 100;
  if v_when is not null then
    v_badges := v_badges || jsonb_build_object('badge', 'first_perfect', 'earned_at', v_when);
  end if;

  -- Five topics whose latest score is 70% or more; earned when the fifth of them was taken.
  with per_attempt as (
    select q.topic_id, a.completed_at,
           100.0 * count(*) filter (where aa.is_correct) / count(*) as score
    from public.quiz_attempts a
    join public.attempt_answers aa on aa.attempt_id = a.id
    join public.questions q on q.id = aa.question_id
    where a.student_id = p_student and a.completed_at is not null and a.completed_at <= p_now
    group by q.topic_id, a.id, a.completed_at
  ),
  latest as (
    select distinct on (topic_id) topic_id, completed_at, score
    from per_attempt order by topic_id, completed_at desc
  )
  select count(*), (array_agg(completed_at order by completed_at))[5]
  into v_mastered, v_when
  from latest where score >= 70;
  if v_mastered >= 5 then
    v_badges := v_badges || jsonb_build_object('badge', 'five_mastered', 'earned_at', v_when);
  end if;

  return jsonb_build_object(
    'student_id', p_student,
    'timezone', 'Africa/Lagos',
    'today', v_today,
    'streak', v_run,
    'today_active', v_today_active,
    'at_risk', v_run > 0 and not v_today_active,
    'longest_streak', v_longest,
    'first_activity_today', v_first_today,
    'freezes', v_freezes,
    'max_freezes', 2,
    'next_freeze_in', case when v_freezes < 2 then 7 - v_run % 7 end,
    'freezes_used_in_streak', to_jsonb(v_frozen),
    'freezes_used_total', v_freezes_used,
    'daily_goal_minutes', v_goal,
    'minutes_today', v_minutes_today,
    'goal_met', v_minutes_today >= v_goal,
    'xp_today', v_xp_today,
    'xp_week', v_xp_week,
    'xp_total', v_xp_total,
    'strip', v_strip,
    'badges', v_badges,
    'mastered_topics', v_mastered
  );
end;
$$;

-- Computes the card as of now and stores any newly earned badges (kept even if,
-- say, a mastered topic later drops below 70%). Returns the card with the stored badges.
create or replace function public.sync_student_badges(p_student uuid)
returns jsonb
language plpgsql
volatile
security definer
set search_path = ''
as $$
declare
  v jsonb := public.gamification_for(p_student, now());
begin
  insert into public.student_badges (student_id, badge, earned_at)
  select p_student, b ->> 'badge', (b ->> 'earned_at')::timestamptz
  from jsonb_array_elements(v -> 'badges') b
  on conflict do nothing;

  return v || jsonb_build_object('badges', (
    select coalesce(jsonb_agg(jsonb_build_object('badge', badge, 'earned_at', earned_at, 'seen', seen_at is not null)
                              order by earned_at), '[]')
    from public.student_badges where student_id = p_student));
end;
$$;

-- The signed-in student's card (the dashboard and the badge pop-ups use this).
create or replace function public.my_gamification()
returns jsonb
language plpgsql
volatile
security definer
set search_path = ''
as $$
begin
  if auth.uid() is null then
    raise exception 'not signed in' using errcode = '42501';
  end if;
  return public.sync_student_badges(auth.uid());
end;
$$;

-- Marks the signed-in student's badges as seen once their pop-up has shown.
create or replace function public.acknowledge_badges(p_badges text[])
returns void
language sql
volatile
security definer
set search_path = ''
as $$
  update public.student_badges set seen_at = now()
  where student_id = auth.uid() and badge = any (p_badges) and seen_at is null;
$$;

revoke execute on function public.gamification_for(uuid, timestamptz) from public, anon, authenticated;
revoke execute on function public.sync_student_badges(uuid) from public, anon, authenticated;
grant execute on function public.gamification_for(uuid, timestamptz) to service_role;
grant execute on function public.sync_student_badges(uuid) to service_role;
revoke execute on function public.my_gamification() from public, anon;
revoke execute on function public.acknowledge_badges(text[]) from public, anon;
grant execute on function public.my_gamification() to authenticated;
grant execute on function public.acknowledge_badges(text[]) to authenticated;

-- Reminders: streak at risk now counts quizzes as well as study logs, and names the streak.
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
  v_active_today boolean;
  v_streak int;
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

  select coalesce(sum(duration_minutes), 0)::int
  into v_today_minutes
  from public.study_logs
  where student_id = v_uid and (logged_at at time zone 'Africa/Lagos')::date = v_today;

  v_active_today := (v_last_activity at time zone 'Africa/Lagos')::date = v_today;

  -- Streak at risk: a study day, past the preferred time, no quiz or study session today.
  if lower(to_char(v_today, 'dy')) = any (v_profile.study_days)
     and v_now::time >= v_profile.preferred_study_time
     and not coalesce(v_active_today, false) then
    v_streak := (public.gamification_for(v_uid, now()) ->> 'streak')::int;
    insert into public.notifications (student_id, kind, title, body, link)
    values (v_uid, 'streak_at_risk', 'Keep your streak going',
            case when v_streak > 0
              then format('Do a quiz or log study today to keep your %s-day streak.', v_streak)
              else format('You planned to study today at %s. A short session starts a new streak.',
                          to_char(v_profile.preferred_study_time, 'HH24:MI')) end,
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
