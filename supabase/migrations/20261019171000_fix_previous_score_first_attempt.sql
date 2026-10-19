-- Fix for 20261019170000: with no earlier attempt on a topic, previous_score divided by zero.
-- nullif makes it null instead (the first attempt on a topic has no previous score).
create or replace function public.get_attempt_review(p_attempt_id uuid)
returns jsonb
language plpgsql
stable
security definer
set search_path = ''
as $$
declare
  v_attempt public.quiz_attempts;
  v_quiz public.quizzes;
begin
  select * into v_attempt from public.quiz_attempts where id = p_attempt_id;
  if not found or v_attempt.student_id is distinct from auth.uid() then
    raise exception 'attempt not found' using errcode = 'P0002';
  end if;
  if v_attempt.completed_at is null then
    raise exception 'attempt has not been submitted' using errcode = 'P0001';
  end if;

  select * into v_quiz from public.quizzes where id = v_attempt.quiz_id;

  return jsonb_build_object(
    'attempt_id', v_attempt.id,
    'quiz', jsonb_build_object(
      'id', v_quiz.id, 'title', v_quiz.title, 'kind', v_quiz.kind,
      'course_id', v_quiz.course_id, 'topic_id', v_quiz.topic_id
    ),
    'score', v_attempt.score,
    'started_at', v_attempt.started_at,
    'completed_at', v_attempt.completed_at,
    'topic_scores', (
      select coalesce(jsonb_agg(jsonb_build_object(
        'topic_id', t.id,
        'topic_title', t.title,
        'correct', s.correct,
        'total', s.total,
        'score', round(100.0 * s.correct / s.total, 2),
        'previous_score', (
          -- The student's score on this topic in their most recent earlier attempt that covered it.
          select round(100.0 * count(*) filter (where pa.is_correct) / nullif(count(*), 0), 2)
          from public.attempt_answers pa
          join public.questions pq on pq.id = pa.question_id
          where pq.topic_id = s.topic_id
            and pa.attempt_id = (
              select a2.id
              from public.quiz_attempts a2
              join public.attempt_answers aa2 on aa2.attempt_id = a2.id
              join public.questions q2 on q2.id = aa2.question_id
              where a2.student_id = v_attempt.student_id
                and a2.completed_at < v_attempt.completed_at
                and q2.topic_id = s.topic_id
              order by a2.completed_at desc
              limit 1
            )
        )
      ) order by t.sequence_order), '[]')
      from (
        select q.topic_id, count(*) as total, count(*) filter (where aa.is_correct) as correct
        from public.attempt_answers aa
        join public.questions q on q.id = aa.question_id
        where aa.attempt_id = v_attempt.id
        group by q.topic_id
      ) s
      join public.topics t on t.id = s.topic_id
    ),
    'questions', (
      select coalesce(jsonb_agg(jsonb_build_object(
        'id', q.id,
        'topic_id', q.topic_id,
        'format', q.format,
        'stem', q.stem,
        'options', q.options,
        'response', aa.response,
        'is_correct', aa.is_correct,
        'correct_answer', q.correct_answer,
        'explanation', q.explanation
      ) order by u.ord), '[]')
      from unnest(v_attempt.question_ids) with ordinality as u(id, ord)
      join public.attempt_answers aa on aa.attempt_id = v_attempt.id and aa.question_id = u.id
      join public.questions q on q.id = u.id
    )
  );
end;
$$;
