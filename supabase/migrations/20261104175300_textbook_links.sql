-- Textbook links (Prompt 5): every recommended textbook can carry a link, either a
-- legal free copy ("free") or where it can be bought or previewed ("buy", "preview").
-- Links come only from content/sources/textbook_links.csv, each opened and matched to
-- the book before it was added. The reading card still opens in the app; the link is
-- a separate button. Students already read resources (table grant), so no new grant.
alter table public.resources
  add column link_type text check (link_type in ('free', 'buy', 'preview')),
  add constraint resources_link_type_needs_url check (link_type is null or url is not null);

-- "Also recommended" now says what kind of link a textbook has.
create or replace function public.also_recommended(p_student uuid, p_topic uuid, p_main uuid)
returns jsonb
language sql
stable
security definer
set search_path = ''
as $$
  select coalesce(jsonb_agg(jsonb_build_object('resource_id', x.id, 'type', x.type, 'title', x.title, 'url', x.url,
                                               'link_type', x.link_type)
                            order by x.ord), '[]'::jsonb)
  from (
    select distinct on (r.type) r.id, r.type, r.title, r.url, r.link_type,
           case r.type when 'video' then 0 else 1 end as ord
    from public.resources r
    where r.topic_id = p_topic
      and r.type in ('video', 'textbook')
      and r.id is distinct from p_main
      and not exists (select 1 from public.recommendations u
                      where u.student_id = p_student and u.resource_id = r.id and u.status in ('accepted', 'dismissed'))
    order by r.type, r.title collate "C"
  ) x;
$$;

revoke execute on function public.also_recommended(uuid, uuid, uuid) from public, anon, authenticated;
grant execute on function public.also_recommended(uuid, uuid, uuid) to service_role;
