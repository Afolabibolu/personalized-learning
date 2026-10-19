-- FR1: a student's preferred ways to study are the four resource types, so the
-- recommendation engine can prefer them: note (reading notes), lecture (lecture
-- slides), past_questions (practising questions), video (videos).
-- Study-log activity types (reading, video, practice) are unchanged.
alter table public.profiles drop constraint profiles_learning_preferences_check;

update public.profiles
set learning_preferences = array(
  select distinct case p when 'reading' then 'note' when 'practice' then 'past_questions' else p end
  from unnest(learning_preferences) as p
);

alter table public.profiles
  add constraint profiles_learning_preferences_check
  check (learning_preferences <@ array['note', 'lecture', 'past_questions', 'video']);
