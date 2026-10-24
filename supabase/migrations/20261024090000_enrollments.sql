-- Phase 9: "my courses". With every course in the Knowledge Base, recommendations,
-- reminders and progress cover only the courses a student has chosen.
-- New profiles start with the reviewed courses (CSC 531, CSC 574); students add
-- or remove courses from onboarding and the course list.

create table public.enrollments (
  student_id uuid not null references public.profiles (id) on delete cascade,
  course_id uuid not null references public.courses (id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (student_id, course_id)
);
create index enrollments_course_id_idx on public.enrollments (course_id);

alter table public.enrollments enable row level security;

create policy "enrollments: read own" on public.enrollments
  for select to authenticated using (student_id = (select auth.uid()));
create policy "enrollments: add own" on public.enrollments
  for insert to authenticated with check (student_id = (select auth.uid()));
create policy "enrollments: remove own" on public.enrollments
  for delete to authenticated using (student_id = (select auth.uid()));

grant select, insert, delete on public.enrollments to authenticated;

-- Every new profile starts on the reviewed courses.
create or replace function public.enroll_in_reviewed_courses()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
begin
  insert into public.enrollments (student_id, course_id)
  select new.id, c.id from public.courses c where c.is_reviewed
  on conflict do nothing;
  return new;
end;
$$;
revoke all on function public.enroll_in_reviewed_courses() from public, anon, authenticated;

create trigger on_profile_created_enroll
  after insert on public.profiles
  for each row execute function public.enroll_in_reviewed_courses();

-- Existing students keep what they had: the reviewed courses.
insert into public.enrollments (student_id, course_id)
select p.id, c.id from public.profiles p cross join public.courses c where c.is_reviewed
on conflict do nothing;
