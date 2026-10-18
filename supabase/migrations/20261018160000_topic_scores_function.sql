-- The student's latest score per topic: for each topic, the percentage correct
-- in their most recent completed attempt that included questions on it.
-- A diagnostic attempt gives a score for every topic it covered. Security
-- definer because students cannot read questions (which hold topic_id).
create or replace function public.get_topic_scores(p_topic_ids uuid[] default null)
returns table (topic_id uuid, score numeric, completed_at timestamptz)
language sql
stable
security definer
set search_path = ''
as $$
  with per_attempt as (
    select
      q.topic_id,
      a.completed_at,
      round(100.0 * count(*) filter (where aa.is_correct) / count(*), 2) as score
    from public.quiz_attempts a
    join public.attempt_answers aa on aa.attempt_id = a.id
    join public.questions q on q.id = aa.question_id
    where a.student_id = auth.uid()
      and a.completed_at is not null
      and (p_topic_ids is null or q.topic_id = any(p_topic_ids))
    group by q.topic_id, a.id, a.completed_at
  )
  select distinct on (p.topic_id) p.topic_id, p.score, p.completed_at
  from per_attempt p
  order by p.topic_id, p.completed_at desc;
$$;

revoke execute on function public.get_topic_scores(uuid[]) from public, anon;
grant execute on function public.get_topic_scores(uuid[]) to authenticated;
