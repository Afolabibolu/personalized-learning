-- Create a profile row for every new auth user. full_name comes from the
-- sign-up metadata; is_simulated comes from app_metadata, which only the
-- admin API (seed_demo.py) can set.
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
begin
  insert into public.profiles (id, full_name, is_simulated)
  values (
    new.id,
    nullif(trim(new.raw_user_meta_data ->> 'full_name'), ''),
    coalesce((new.raw_app_meta_data ->> 'is_simulated')::boolean, false)
  );
  return new;
end;
$$;

revoke execute on function public.handle_new_user() from public, anon, authenticated;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- Users created before this migration.
insert into public.profiles (id, full_name)
select id, nullif(trim(raw_user_meta_data ->> 'full_name'), '')
from auth.users
on conflict (id) do nothing;
