-- The ten tables: the report's eight entities plus questions and attempt_answers.
-- Content tables cascade from course down; student data cascades from the profile.
-- Cross references (answers to questions, logs to topics, ...) are restricted.

create table public.profiles (
  id uuid primary key references auth.users (id) on delete cascade,
  full_name text,
  department text,
  level int check (level in (100, 200, 300, 400, 500)),
  learning_preferences text[] not null default '{}'
    check (learning_preferences <@ array['reading', 'video', 'practice']),
  is_simulated boolean not null default false,
  created_at timestamptz not null default now()
);

create table public.courses (
  id uuid primary key default gen_random_uuid(),
  code text not null unique,
  title text not null,
  description text,
  created_at timestamptz not null default now()
);

create table public.topics (
  id uuid primary key default gen_random_uuid(),
  course_id uuid not null references public.courses (id) on delete cascade,
  slug text not null,
  title text not null,
  subtopics text[] not null default '{}',
  sequence_order int not null check (sequence_order > 0),
  unique (course_id, slug)
);

create table public.resources (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid not null references public.topics (id) on delete cascade,
  title text not null,
  type text not null check (type in ('pdf', 'video', 'link')),
  url text not null,
  is_introductory boolean not null default false,
  intro_order int,
  check (not is_introductory or intro_order is not null),
  unique (topic_id, url)
);

create table public.quizzes (
  id uuid primary key default gen_random_uuid(),
  course_id uuid not null references public.courses (id) on delete cascade,
  topic_id uuid references public.topics (id) on delete cascade,
  kind text not null check (kind in ('diagnostic', 'topic')),
  title text not null,
  question_count int not null check (question_count between 1 and 50),
  check ((kind = 'diagnostic') = (topic_id is null))
);
create index quizzes_course_id_idx on public.quizzes (course_id);
create unique index quizzes_one_diagnostic_per_course on public.quizzes (course_id) where kind = 'diagnostic';
create unique index quizzes_one_quiz_per_topic on public.quizzes (topic_id) where kind = 'topic';

-- options: [{"key": "a", "text": "..."}, ...]
-- correct_answer: array of option keys, e.g. ["b"] or ["a", "c"] for multi_select
create table public.questions (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid not null references public.topics (id) on delete cascade,
  format text not null check (format in ('single_choice', 'true_false', 'multi_select', 'odd_one_out')),
  stem text not null,
  options jsonb not null check (jsonb_typeof(options) = 'array'),
  correct_answer jsonb not null check (jsonb_typeof(correct_answer) = 'array' and jsonb_array_length(correct_answer) >= 1),
  explanation text not null,
  source text not null,
  status text not null default 'draft' check (status in ('draft', 'approved')),
  created_at timestamptz not null default now(),
  unique (topic_id, stem)
);

create table public.quiz_attempts (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.profiles (id) on delete cascade,
  quiz_id uuid not null references public.quizzes (id),
  question_ids uuid[] not null,
  score numeric(5, 2) check (score between 0 and 100),
  started_at timestamptz not null default now(),
  completed_at timestamptz,
  check ((score is null) = (completed_at is null))
);
create index quiz_attempts_student_id_idx on public.quiz_attempts (student_id);
create index quiz_attempts_quiz_id_idx on public.quiz_attempts (quiz_id);

create table public.attempt_answers (
  id uuid primary key default gen_random_uuid(),
  attempt_id uuid not null references public.quiz_attempts (id) on delete cascade,
  question_id uuid not null references public.questions (id),
  response jsonb not null default '[]',
  is_correct boolean not null,
  unique (attempt_id, question_id)
);
create index attempt_answers_question_id_idx on public.attempt_answers (question_id);

create table public.study_logs (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.profiles (id) on delete cascade,
  topic_id uuid not null references public.topics (id),
  duration_minutes int not null check (duration_minutes between 1 and 600),
  activity_type text not null check (activity_type in ('reading', 'video', 'practice')),
  logged_at timestamptz not null default now()
);
create index study_logs_student_id_idx on public.study_logs (student_id);
create index study_logs_topic_id_idx on public.study_logs (topic_id);

-- A recommendation points at a resource, or at the topic quiz when no unused
-- resource is left for that topic.
create table public.recommendations (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.profiles (id) on delete cascade,
  topic_id uuid not null references public.topics (id),
  resource_id uuid references public.resources (id),
  quiz_id uuid references public.quizzes (id),
  rank int not null check (rank >= 1),
  priority_score double precision,
  source text not null check (source in ('ml', 'cold_start')),
  model_version text,
  status text not null default 'pending' check (status in ('pending', 'accepted', 'dismissed')),
  created_at timestamptz not null default now(),
  check (resource_id is not null or quiz_id is not null),
  check (source <> 'ml' or model_version is not null)
);
create index recommendations_student_id_idx on public.recommendations (student_id);
create index recommendations_topic_id_idx on public.recommendations (topic_id);
