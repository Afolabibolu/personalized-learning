-- Semester of each course (1 = first, 2 = second), so a level page can split its
-- courses by semester. Filled by content/load.py from the course file's "semester",
-- which is taken from the course's source folder or its exam papers.
alter table public.courses add column semester smallint
  check (semester in (1, 2));
