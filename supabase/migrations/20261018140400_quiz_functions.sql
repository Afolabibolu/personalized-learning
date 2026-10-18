-- Quizzes go through these functions only. Students cannot read questions or
-- write attempts and answers directly; each function checks auth.uid() owns
-- the attempt.

-- An answer is correct when the set of chosen option keys equals the set of
-- correct keys. Order and duplicates do not matter; a partial multi_select is wrong.
create or replace function public.answer_is_correct(p_response jsonb, p_correct jsonb)
returns boolean
language sql
immutable
set search_path = ''
as $$
  select coalesce(
    (select array_agg(distinct x order by x) from jsonb_array_elements_text(p_response) as x)
      = (select array_agg(distinct x order by x) from jsonb_array_elements_text(p_correct) as x),
    false
  );
$$;

-- The review of a completed attempt: score, score per topic, and every question
-- with the student's response, the correct answer and the explanation.
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
        'score', round(100.0 * s.correct / s.total, 2)
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

-- Creates an attempt and picks its questions: per topic, unseen questions first,
-- then the ones seen longest ago. A diagnostic quiz takes them round-robin across
-- the course's topics so every topic is covered. Returns the questions without
-- correct_answer or explanation.
create or replace function public.start_quiz(p_quiz_id uuid)
returns jsonb
language plpgsql
volatile
security definer
set search_path = ''
as $$
declare
  v_uid uuid := auth.uid();
  v_quiz public.quizzes;
  v_question_ids uuid[];
  v_attempt_id uuid;
begin
  if v_uid is null then
    raise exception 'not signed in' using errcode = '42501';
  end if;

  select * into v_quiz from public.quizzes where id = p_quiz_id;
  if not found then
    raise exception 'quiz not found' using errcode = 'P0002';
  end if;

  with seen as (
    select u.question_id, max(a.started_at) as last_seen
    from public.quiz_attempts a
    cross join unnest(a.question_ids) as u(question_id)
    where a.student_id = v_uid
    group by u.question_id
  ),
  candidates as (
    select
      q.id,
      t.sequence_order,
      row_number() over (
        partition by q.topic_id
        order by s.last_seen asc nulls first, random()
      ) as rn
    from public.questions q
    join public.topics t on t.id = q.topic_id
    left join seen s on s.question_id = q.id
    where q.status = 'approved'
      and t.course_id = v_quiz.course_id
      and (v_quiz.topic_id is null or q.topic_id = v_quiz.topic_id)
  ),
  picked as (
    select id, sequence_order, rn
    from candidates
    order by rn, sequence_order
    limit v_quiz.question_count
  )
  select array_agg(id order by sequence_order, rn) into v_question_ids from picked;

  if v_question_ids is null then
    raise exception 'quiz has no approved questions' using errcode = 'P0001';
  end if;

  insert into public.quiz_attempts (student_id, quiz_id, question_ids)
  values (v_uid, p_quiz_id, v_question_ids)
  returning id into v_attempt_id;

  return jsonb_build_object(
    'attempt_id', v_attempt_id,
    'quiz', jsonb_build_object(
      'id', v_quiz.id, 'title', v_quiz.title, 'kind', v_quiz.kind,
      'course_id', v_quiz.course_id, 'topic_id', v_quiz.topic_id
    ),
    'questions', (
      select jsonb_agg(jsonb_build_object(
        'id', q.id,
        'topic_id', q.topic_id,
        'format', q.format,
        'stem', q.stem,
        'options', q.options
      ) order by u.ord)
      from unnest(v_question_ids) with ordinality as u(id, ord)
      join public.questions q on q.id = u.id
    )
  );
end;
$$;

-- Grades only the questions stored on the attempt. p_responses is an object
-- keyed by question id, each value an array of option keys (a single key as a
-- string is accepted too). Missing responses count as wrong; responses for
-- questions not on the attempt are ignored. A completed attempt cannot be
-- submitted again.
create or replace function public.submit_quiz(p_attempt_id uuid, p_responses jsonb)
returns jsonb
language plpgsql
volatile
security definer
set search_path = ''
as $$
declare
  v_uid uuid := auth.uid();
  v_attempt public.quiz_attempts;
  v_total int;
  v_correct int;
begin
  if v_uid is null then
    raise exception 'not signed in' using errcode = '42501';
  end if;
  if p_responses is null or jsonb_typeof(p_responses) <> 'object' then
    raise exception 'responses must be an object keyed by question id' using errcode = '22023';
  end if;

  select * into v_attempt from public.quiz_attempts where id = p_attempt_id for update;
  if not found or v_attempt.student_id <> v_uid then
    raise exception 'attempt not found' using errcode = 'P0002';
  end if;
  if v_attempt.completed_at is not null then
    raise exception 'attempt already submitted' using errcode = 'P0001';
  end if;

  insert into public.attempt_answers (attempt_id, question_id, response, is_correct)
  select p_attempt_id, q.id, r.response, public.answer_is_correct(r.response, q.correct_answer)
  from unnest(v_attempt.question_ids) as u(id)
  join public.questions q on q.id = u.id
  cross join lateral (
    select case jsonb_typeof(p_responses -> q.id::text)
      when 'array' then p_responses -> q.id::text
      when 'string' then jsonb_build_array(p_responses -> q.id::text)
      else '[]'::jsonb
    end as response
  ) r;

  select count(*), count(*) filter (where is_correct)
  into v_total, v_correct
  from public.attempt_answers
  where attempt_id = p_attempt_id;

  update public.quiz_attempts
  set score = round(100.0 * v_correct / greatest(v_total, 1), 2),
      completed_at = now()
  where id = p_attempt_id;

  return public.get_attempt_review(p_attempt_id);
end;
$$;

revoke execute on function public.answer_is_correct(jsonb, jsonb) from public, anon, authenticated;
revoke execute on function public.get_attempt_review(uuid) from public, anon;
revoke execute on function public.start_quiz(uuid) from public, anon;
revoke execute on function public.submit_quiz(uuid, jsonb) from public, anon;
grant execute on function public.get_attempt_review(uuid) to authenticated;
grant execute on function public.start_quiz(uuid) to authenticated;
grant execute on function public.submit_quiz(uuid, jsonb) to authenticated;
