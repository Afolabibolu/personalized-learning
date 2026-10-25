-- Level of each course (100 to 500), so the Courses page can group many courses.
-- Filled from the first digit of the course number; content/load.py keeps it in
-- step with the course file ("level", or the same rule when it is missing).
alter table public.courses add column level smallint
  check (level in (100, 200, 300, 400, 500));

update public.courses
set level = (substring(code from '[0-9]')::int) * 100
where substring(code from '[0-9]') between '1' and '5';
