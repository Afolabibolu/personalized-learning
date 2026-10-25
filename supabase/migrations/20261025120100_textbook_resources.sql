-- Recommended textbooks: a fifth resource type, shown in the app as a reading
-- card (book, edition, chapters to read) from content/textbooks/<code>.json.
-- Not a learning preference: preferences stay note, lecture, past_questions, video.
alter table public.resources drop constraint resources_type_check;
alter table public.resources add constraint resources_type_check
  check (type in ('note', 'lecture', 'past_questions', 'video', 'textbook'));
