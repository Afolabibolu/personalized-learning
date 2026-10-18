-- The Phase 0 connection check is no longer needed.
drop table if exists public.healthcheck;

-- Supabase grants anon and authenticated full access to every new table and
-- function by default, leaving row-level security as the only guard. Turn that
-- off so each migration grants exactly what students need, column by column.
alter default privileges for role postgres in schema public
  revoke all on tables from anon, authenticated;
alter default privileges for role postgres in schema public
  revoke all on sequences from anon, authenticated;
alter default privileges for role postgres in schema public
  revoke execute on functions from anon, authenticated;
alter default privileges for role postgres
  revoke execute on functions from public;
