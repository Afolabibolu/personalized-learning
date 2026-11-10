-- The "course is ready" notification links to the course page, which is addressed by id, not code.

-- Mark a request in progress, added (optionally linking the course and enrolling the student)
-- or declined (a reason is required). The student is notified each time.
create or replace function public.manage_set_request_status(
  p_request uuid, p_status text, p_note text default null, p_course_code text default null)
returns void
language plpgsql
security definer
set search_path = ''
as $$
declare
  v_req public.course_requests;
  v_course public.courses;
begin
  perform public.require_course_manager();
  if p_status not in ('in_progress', 'added', 'declined') then
    raise exception 'status must be in_progress, added or declined' using errcode = '22023';
  end if;
  if p_status = 'declined' and coalesce(trim(p_note), '') = '' then
    raise exception 'a reason is required to decline a request' using errcode = '22023';
  end if;
  select * into v_req from public.course_requests where id = p_request for update;
  if not found then
    raise exception 'request not found' using errcode = 'P0002';
  end if;
  if p_course_code is not null then
    select * into v_course from public.courses where upper(code) = upper(trim(p_course_code));
    if not found then
      raise exception 'no course %', p_course_code using errcode = 'P0002';
    end if;
  end if;

  update public.course_requests
  set status = p_status,
      admin_note = case when p_note is not null then trim(p_note) else admin_note end,
      course_id = coalesce(v_course.id, course_id),
      updated_at = now()
  where id = p_request;

  if p_status = 'added' and v_course.id is not null then
    insert into public.enrollments (student_id, course_id) values (v_req.student_id, v_course.id)
    on conflict do nothing;
  end if;

  insert into public.notifications (student_id, kind, title, body, link)
  values (
    v_req.student_id,
    case p_status when 'added' then 'course_added' when 'declined' then 'course_request_declined'
                  else 'course_request_in_progress' end,
    case p_status when 'added' then format('%s is ready', coalesce(v_course.code, v_req.code))
                  when 'declined' then format('Your request for %s was declined', v_req.code)
                  else format('We are working on %s', v_req.code) end,
    case p_status
      when 'added' then format('%s: %s is now in the app%s.', coalesce(v_course.code, v_req.code),
                               coalesce(v_course.title, v_req.title),
                               case when v_course.id is not null then ' and in your courses' else '' end)
      when 'declined' then format('Reason: %s', trim(p_note))
      else format('Your request for %s: %s is in progress.', v_req.code, v_req.title) end,
    case p_status when 'added' then coalesce('/courses/' || v_course.id::text, '/courses') else '/courses/request' end
  )
  on conflict do nothing;

  perform public.write_audit('request.status', 'course_requests', p_request,
    format('Request %s: %s', v_req.code, p_status),
    public.audit_changes(jsonb_build_object('status', v_req.status, 'admin_note', v_req.admin_note, 'course_id', v_req.course_id),
                         jsonb_build_object('status', p_status,
                                            'admin_note', case when p_note is not null then trim(p_note) else v_req.admin_note end,
                                            'course_id', coalesce(v_course.id, v_req.course_id))));
end;
$$;
