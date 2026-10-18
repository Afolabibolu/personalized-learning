-- Phase 0 connection check. Phase 1 drops this table in its own migration.
create table public.healthcheck (
  id bigint generated always as identity primary key,
  message text not null,
  created_at timestamptz not null default now()
);

alter table public.healthcheck enable row level security;

create policy "healthcheck is readable by anyone"
  on public.healthcheck for select
  to anon, authenticated
  using (true);

grant select on public.healthcheck to anon, authenticated;

insert into public.healthcheck (message) values ('Hello from Supabase');
