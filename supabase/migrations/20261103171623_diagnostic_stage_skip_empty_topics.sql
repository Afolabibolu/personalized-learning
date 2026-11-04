-- Stage 2 fix: a topic with no unused resource and no topic quiz has nothing to
-- recommend, so it is left out before ranking (a row needs a resource or a quiz).
-- Otherwise the same rules as 20261103171227_diagnostic_stage.sql.
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
  candidates as (
    select ts.*, res.id as resource_id, res.type as resource_type,
           case when res.id is null then
             (select q.id from public.quizzes q where q.topic_id = ts.topic_id and q.kind = 'topic' limit 1) end as quiz_id
    from topic_scores ts
    cross join prefs pr
    left join lateral (
      select r.id, r.type
      from public.resources r
      where r.topic_id = ts.topic_id
        and not exists (select 1 from public.recommendations u
                        where u.student_id = p_student and u.resource_id = r.id and u.status in ('accepted', 'dismissed'))
      order by r.type <> all (pr.types),
               array_position(array['note', 'past_questions', 'lecture', 'video', 'textbook'], r.type),
               not r.is_introductory,
               r.title collate "C"
      limit 1
    ) res on true
  ),
  ranked as (
    select c.*,
           row_number() over (partition by c.course_id
                              order by c.correct = c.total, c.correct::numeric / c.total, c.sequence_order) as rn,
           count(*) filter (where c.correct < c.total) over (partition by c.course_id) as not_full
    from candidates c
    where c.resource_id is not null or c.quiz_id is not null
  )
  select p.course_id,
         p.topic_id,
         p.rn::int,
         p.resource_id,
         p.quiz_id,
         jsonb_build_object(
           'reason', format('You got %s of %s right on this topic in the diagnostic.', p.correct, p.total),
           'probabilities', null,
           'top_factors', '[]'::jsonb,
           'matched_preference', case when p.resource_type = any (pr.types) then p.resource_type end,
           'also', public.also_recommended(p_student, p.topic_id, p.resource_id),
           'diagnostic', jsonb_build_object('correct', p.correct, 'total', p.total,
                                            'score', round(100.0 * p.correct / p.total)),
           'threshold', public.cold_start_threshold(),
           'completed_quizzes', p.completed_quizzes)
  from ranked p
  cross join prefs pr
  where p.rn <= 3 and (p.correct < p.total or p.not_full = 0);
$$;

revoke execute on function public.diagnostic_recommendations(uuid) from public, anon, authenticated;
grant execute on function public.diagnostic_recommendations(uuid) to service_role;
