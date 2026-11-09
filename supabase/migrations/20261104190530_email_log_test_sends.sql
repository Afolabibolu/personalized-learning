-- Test sends to SMTP_USER (to_self) do not count towards "once per kind per day",
-- so testing never stops a student's real reminder.
drop index public.email_log_once_per_day;
create unique index email_log_once_per_day on public.email_log (student_id, kind, day)
  where status <> 'failed' and not to_self;
