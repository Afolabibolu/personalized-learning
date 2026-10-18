-- One row per completed attempt per topic it covered, with the percentage
-- correct on that topic. Feeds the ML features (training and /recommend).
-- Only the service role reads it: anon and authenticated get no grant.
create view public.ml_attempt_topic_scores
with (security_invoker = true)
as
select
  a.student_id,
  q.topic_id,
  a.id as attempt_id,
  a.completed_at,
  round(100.0 * count(*) filter (where aa.is_correct) / count(*), 2) as score
from public.quiz_attempts a
join public.attempt_answers aa on aa.attempt_id = a.id
join public.questions q on q.id = aa.question_id
where a.completed_at is not null
group by a.student_id, q.topic_id, a.id, a.completed_at;

revoke all on public.ml_attempt_topic_scores from anon, authenticated;
grant select on public.ml_attempt_topic_scores to service_role;
