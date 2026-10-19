-- FR5 knowledge base: topic summaries, four resource types with in-app
-- Markdown content, reviewed flag for pipeline courses, and live counts.

alter table public.topics add column summary text;

alter table public.courses add column is_reviewed boolean not null default true;

-- Resources: note and past_questions carry Markdown in body (shown in the app);
-- lecture and video carry a url (opened in a new tab).
alter table public.resources drop constraint resources_type_check;
update public.resources set type = 'lecture' where type in ('pdf', 'link');
alter table public.resources
  add constraint resources_type_check check (type in ('note', 'lecture', 'past_questions', 'video'));

alter table public.resources alter column url drop not null;
alter table public.resources add column body text;
alter table public.resources add column source text;
alter table public.resources
  add constraint resources_url_or_body check (url is not null or body is not null);

-- Live counts for the Knowledge Base page. security_invoker, so students
-- count only what RLS lets them read (all content is readable; questions
-- are counted through a definer function because students cannot read them).
create or replace function public.approved_question_count()
returns bigint
language sql
stable
security definer
set search_path = ''
as $$
  select count(*) from public.questions where status = 'approved';
$$;

revoke execute on function public.approved_question_count() from public, anon;
grant execute on function public.approved_question_count() to authenticated;

create view public.knowledge_base_stats
with (security_invoker = true)
as
select
  (select count(*) from public.courses) as courses,
  (select count(*) from public.topics) as topics,
  (select count(*) from public.resources) as resources,
  (select count(*) from public.resources where type = 'note') as notes,
  (select count(*) from public.resources where type = 'lecture') as lectures,
  (select count(*) from public.resources where type = 'past_questions') as past_question_sets,
  (select count(*) from public.resources where type = 'video') as videos,
  public.approved_question_count() as practice_questions;

revoke all on public.knowledge_base_stats from anon;
grant select on public.knowledge_base_stats to authenticated;
