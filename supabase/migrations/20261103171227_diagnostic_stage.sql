-- Three recommendation stages per course (3 Nov):
--   Stage 1: no diagnostic yet                     -> "Getting started" list (source cold_start)
--   Stage 2: diagnostic taken, below the threshold  -> weakest diagnostic topics (source diagnostic)
--   Stage 3: at or above the threshold              -> Logistic Regression + Random Forest (source ml)
-- "Completed quizzes" counts every completed attempt on the course's quizzes, the diagnostic included.
--
-- Stage 2 is computed here, in one place: the ML service reads it through
-- diagnostic_recommendations(), and the web app calls refresh_fallback_recommendations()
-- when the ML service is down, so Stage 2 never depends on the Python service (NFR4).

-- One config value for the threshold, read by the web app, the ML service and the functions below.
create table public.app_settings (
  key text primary key,
  value jsonb not null,
  description text
);
alter table public.app_settings enable row level security;
create policy "Anyone signed in can read settings" on public.app_settings
  for select to authenticated using (true);
grant select on public.app_settings to authenticated, service_role;

insert into public.app_settings (key, value, description) values
  ('cold_start_threshold', '3',
   'Completed quizzes on a course (diagnostic included) before the ML models rank its topics.');

create or replace function public.cold_start_threshold()
returns int
language sql
stable
security definer
set search_path = ''
as $$
  select (value #>> '{}')::int from public.app_settings where key = 'cold_start_threshold';
$$;
revoke execute on function public.cold_start_threshold() from public, anon;
grant execute on function public.cold_start_threshold() to authenticated, service_role;

alter table public.recommendations drop constraint recommendations_source_check;
alter table public.recommendations
  add constraint recommendations_source_check check (source in ('ml', 'cold_start', 'diagnostic'));

-- Each of the student's courses with its stage.
create or replace function public.recommendation_stages(p_student uuid)
returns table (course_id uuid, completed_quizzes int, diagnostic_attempt_id uuid, stage int)
language sql
stable
security definer
set search_path = ''
as $$
  with completed as (
    select q.course_id, count(*)::int as n
    from public.quiz_attempts a
    join public.quizzes q on q.id = a.quiz_id
    where a.student_id = p_student and a.completed_at is not null
    group by q.course_id
  ),
  last_diagnostic as (
    select distinct on (q.course_id) q.course_id, a.id as attempt_id
    from public.quiz_attempts a
    join public.quizzes q on q.id = a.quiz_id
    where a.student_id = p_student and a.completed_at is not null and q.kind = 'diagnostic'
    order by q.course_id, a.completed_at desc
  )
  select e.course_id,
         coalesce(c.n, 0),
         d.attempt_id,
         case when coalesce(c.n, 0) >= public.cold_start_threshold() then 3
              when d.attempt_id is not null then 2
              else 1 end
  from public.enrollments e
  left join completed c on c.course_id = e.course_id
  left join last_diagnostic d on d.course_id = e.course_id
  where e.student_id = p_student;
$$;

-- The topic's first unused video and textbook other than the main resource ("Also recommended").
create or replace function public.also_recommended(p_student uuid, p_topic uuid, p_main uuid)
returns jsonb
language sql
stable
security definer
set search_path = ''
as $$
  select coalesce(jsonb_agg(jsonb_build_object('resource_id', x.id, 'type', x.type, 'title', x.title, 'url', x.url)
                            order by x.ord), '[]'::jsonb)
  from (
    select distinct on (r.type) r.id, r.type, r.title, r.url, case r.type when 'video' then 0 else 1 end as ord
    from public.resources r
    where r.topic_id = p_topic
      and r.type in ('video', 'textbook')
      and r.id is distinct from p_main
      and not exists (select 1 from public.recommendations u
                      where u.student_id = p_student and u.resource_id = r.id and u.status in ('accepted', 'dismissed'))
    order by r.type, r.title collate "C"
  ) x;
$$;

-- Stage 2: for each course in Stage 2, up to 3 topics from the latest diagnostic, lowest
-- score first, ties broken by teaching order. Fully right topics are left out unless every
-- topic was fully right. Each gets its first unused resource (the student's preferred types
-- first, then note, past questions, lecture, video, textbook), or the topic quiz.
create or replace function public.diagnostic_recommendations(p_student uuid)
returns table (course_id uuid, topic_id uuid, rank int, resource_id uuid, quiz_id uuid, explanation jsonb)
language sql
stable
security definer
set search_path = ''
as $$
  with prefs as (
    select coalesce(learning_preferences, '{}') as types from public.profiles where id = p_student
  ),
  stage2 as (
    select s.course_id, s.diagnostic_attempt_id, s.completed_quizzes
    from public.recommendation_stages(p_student) s
    where s.stage = 2
  ),
  topic_scores as (
    select s.course_id, t.id as topic_id, t.sequence_order, s.completed_quizzes,
           count(*) filter (where aa.is_correct)::int as correct, count(*)::int as total
    from stage2 s
    join public.attempt_answers aa on aa.attempt_id = s.diagnostic_attempt_id
    join public.questions qn on qn.id = aa.question_id
    join public.topics t on t.id = qn.topic_id
    group by s.course_id, t.id, t.sequence_order, s.completed_quizzes
  ),
  ranked as (
    select ts.*,
           row_number() over (partition by ts.course_id
                              order by ts.correct = ts.total, ts.correct::numeric / ts.total, ts.sequence_order) as rn,
           count(*) filter (where ts.correct < ts.total) over (partition by ts.course_id) as not_full
    from topic_scores ts
  ),
  picked as (
    select * from ranked where rn <= 3 and (correct < total or not_full = 0)
  )
  select p.course_id,
         p.topic_id,
         p.rn::int,
         res.id,
         case when res.id is null then
           (select q.id from public.quizzes q where q.topic_id = p.topic_id and q.kind = 'topic' limit 1) end,
         jsonb_build_object(
           'reason', format('You got %s of %s right on this topic in the diagnostic.', p.correct, p.total),
           'probabilities', null,
           'top_factors', '[]'::jsonb,
           'matched_preference', case when res.type = any (pr.types) then res.type end,
           'also', public.also_recommended(p_student, p.topic_id, res.id),
           'diagnostic', jsonb_build_object('correct', p.correct, 'total', p.total,
                                            'score', round(100.0 * p.correct / p.total)),
           'threshold', public.cold_start_threshold(),
           'completed_quizzes', p.completed_quizzes)
  from picked p
  cross join prefs pr
  left join lateral (
    select r.id, r.type
    from public.resources r
    where r.topic_id = p.topic_id
      and not exists (select 1 from public.recommendations u
                      where u.student_id = p_student and u.resource_id = r.id and u.status in ('accepted', 'dismissed'))
    order by r.type <> all (pr.types),
             array_position(array['note', 'past_questions', 'lecture', 'video', 'textbook'], r.type),
             not r.is_introductory,
             r.title collate "C"
    limit 1
  ) res on true;
$$;

-- Stage 1 (used by the fallback): the course's unused introductory resources, in order.
create or replace function public.cold_start_recommendations(p_student uuid, p_course uuid)
returns table (topic_id uuid, rank int, resource_id uuid, explanation jsonb)
language sql
stable
security definer
set search_path = ''
as $$
  select r.topic_id,
         (row_number() over (order by r.intro_order nulls last, r.id))::int,
         r.id,
         jsonb_build_object('reason', 'Not enough quiz history yet for this course.', 'probabilities', null,
                            'top_factors', '[]'::jsonb, 'matched_preference', null,
                            'also', public.also_recommended(p_student, r.topic_id, r.id))
  from public.resources r
  join public.topics t on t.id = r.topic_id
  where t.course_id = p_course
    and r.is_introductory
    and not exists (select 1 from public.recommendations u
                    where u.student_id = p_student and u.resource_id = r.id and u.status in ('accepted', 'dismissed'));
$$;

-- Called by the web app when the ML service cannot be reached. For the signed-in student:
-- Stage 2 courses get their diagnostic list (replacing that course's pending rows), and
-- Stage 1 courses with nothing pending get their introductory list. Stage 3 courses keep
-- their last saved ML list. Returns the number of rows written.
create or replace function public.refresh_fallback_recommendations()
returns int
language plpgsql
security definer
set search_path = ''
as $$
declare
  v_student uuid := auth.uid();
  v_written int := 0;
  v_rows int;
  v_course record;
begin
  if v_student is null then
    raise exception 'not signed in';
  end if;

  for v_course in select * from public.recommendation_stages(v_student) loop
    if v_course.stage = 2 then
      delete from public.recommendations r
      using public.topics t
      where r.topic_id = t.id and t.course_id = v_course.course_id
        and r.student_id = v_student and r.status = 'pending';
      insert into public.recommendations (student_id, topic_id, resource_id, quiz_id, rank, source, explanation)
      select v_student, d.topic_id, d.resource_id, d.quiz_id, d.rank, 'diagnostic', d.explanation
      from public.diagnostic_recommendations(v_student) d
      where d.course_id = v_course.course_id;
      get diagnostics v_rows = row_count;
      v_written := v_written + v_rows;
    elsif v_course.stage = 1 and not exists (
      select 1 from public.recommendations r join public.topics t on t.id = r.topic_id
      where r.student_id = v_student and r.status = 'pending' and t.course_id = v_course.course_id
    ) then
      insert into public.recommendations (student_id, topic_id, resource_id, rank, source, explanation)
      select v_student, c.topic_id, c.resource_id, c.rank, 'cold_start', c.explanation
      from public.cold_start_recommendations(v_student, v_course.course_id) c;
      get diagnostics v_rows = row_count;
      v_written := v_written + v_rows;
    end if;
  end loop;
  return v_written;
end;
$$;

revoke execute on function public.recommendation_stages(uuid) from public, anon, authenticated;
revoke execute on function public.also_recommended(uuid, uuid, uuid) from public, anon, authenticated;
revoke execute on function public.diagnostic_recommendations(uuid) from public, anon, authenticated;
revoke execute on function public.cold_start_recommendations(uuid, uuid) from public, anon, authenticated;
grant execute on function public.recommendation_stages(uuid) to service_role;
grant execute on function public.also_recommended(uuid, uuid, uuid) to service_role;
grant execute on function public.diagnostic_recommendations(uuid) to service_role;
grant execute on function public.cold_start_recommendations(uuid, uuid) to service_role;

revoke execute on function public.refresh_fallback_recommendations() from public, anon;
grant execute on function public.refresh_fallback_recommendations() to authenticated;
