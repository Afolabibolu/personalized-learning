"""Tests for course management (Prompt 7), as real signed-in users on the linked project:
roles, request files in private storage, and every /manage action with its audit row.

    pytest scripts/test_course_management.py
"""

import uuid

import pytest
from postgrest.exceptions import APIError

import testkit

BUCKET = "course-request-files"
PDF = b"%PDF-1.4\n% test file\n"


@pytest.fixture(scope="module")
def db():
    return testkit.admin()


@pytest.fixture(scope="module")
def fx(db):
    fixture = testkit.setup(db)
    yield fixture
    # Uploaded files are not deleted with their users: remove the test users' folders first.
    for u in db.auth.admin.list_users(page=1, per_page=1000):
        if (u.email or "").endswith("@" + testkit.EMAIL_DOMAIN):
            store = db.storage.from_(BUCKET)
            paths = [f"{u.id}/{d['name']}/{f['name']}" for d in store.list(u.id) for f in store.list(f"{u.id}/{d['name']}")]
            if paths:
                store.remove(paths)
    testkit.cleanup(db)


def user(db, name: str, role: str = "student"):
    uid, email = testkit.create_student(db, f"Manage {name} {uuid.uuid4().hex[:6]}")
    db.table("profiles").update({"role": role, "department": "Computer Science", "level": 500}).eq("id", uid).execute()
    return uid, testkit.sign_in(email)


@pytest.fixture
def student(db, fx):
    return user(db, "student")


@pytest.fixture
def other(db, fx):
    return user(db, "other")


@pytest.fixture
def manager(db, fx):
    return user(db, "manager", "course_manager")


def request_with_file(client, uid: str, code: str = "TST 101") -> tuple[str, str]:
    """A request made the way the app does it (id chosen first), with one uploaded PDF."""
    rid = str(uuid.uuid4())
    client.table("course_requests").insert({"id": rid, "student_id": uid, "code": code, "title": "Test request"}).execute()
    path = f"{uid}/{rid}/outline.pdf"
    client.storage.from_(BUCKET).upload(path, PDF, {"content-type": "application/pdf"})
    client.table("course_request_files").insert({"request_id": rid, "student_id": uid, "path": path, "name": "outline.pdf",
                                                 "size_bytes": len(PDF), "content_type": "application/pdf"}).execute()
    return rid, path


def audit_rows(db, row_id: str) -> list[dict]:
    return db.table("content_audit").select("action, actor_id, changes").eq("row_id", row_id).order("created_at").execute().data


def raises_42501(action) -> bool:
    try:
        action()
    except APIError as e:
        return e.code == "42501"
    return False


# -- roles ---------------------------------------------------------------------------------

def test_a_student_cannot_change_their_own_role(student, db):
    uid, client = student
    with pytest.raises(APIError):
        client.table("profiles").update({"role": "course_manager"}).eq("id", uid).execute()
    assert db.table("profiles").select("role").eq("id", uid).single().execute().data["role"] == "student"


def test_new_profiles_are_students(student, db):
    uid, client = student
    assert client.rpc("is_course_manager").execute().data is False


# -- students are blocked from /manage by the database --------------------------------------

def test_a_student_cannot_use_any_manage_function(student, fx):
    _, client = student
    calls = [
        lambda: client.rpc("manage_requests").execute(),
        lambda: client.rpc("manage_set_request_status", {"p_request": str(uuid.uuid4()), "p_status": "added"}).execute(),
        lambda: client.rpc("manage_update_topic", {"p_topic": fx.topic_ids["alpha"], "p_title": "x", "p_summary": "x"}).execute(),
        lambda: client.rpc("manage_questions", {"p_topic": fx.topic_ids["alpha"]}).execute(),
        lambda: client.rpc("manage_set_question_hidden", {"p_question": next(iter(fx.correct)), "p_hidden": True}).execute(),
        lambda: client.rpc("manage_save_resource", {"p_resource": None, "p_topic": fx.topic_ids["alpha"], "p_title": "x",
                                                    "p_type": "video", "p_url": "https://example.org"}).execute(),
        lambda: client.rpc("manage_set_course_reviewed", {"p_course": fx.course_id, "p_reviewed": True}).execute(),
        lambda: client.rpc("manage_audit").execute(),
    ]
    assert all(raises_42501(c) for c in calls)
    assert client.table("content_audit").select("id").execute().data == []


# -- request files -------------------------------------------------------------------------

def test_files_are_private_to_the_requester_and_managers(student, other, manager):
    uid, client = student
    rid, path = request_with_file(client, uid)
    assert client.storage.from_(BUCKET).download(path) == PDF
    _, other_client = other
    assert other_client.table("course_request_files").select("id").eq("request_id", rid).execute().data == []
    assert other_client.table("course_requests").select("id").eq("id", rid).execute().data == []
    with pytest.raises(Exception):
        other_client.storage.from_(BUCKET).download(path)
    _, mgr = manager
    assert mgr.storage.from_(BUCKET).download(path) == PDF
    listed = next(r for r in mgr.rpc("manage_requests").execute().data if r["id"] == rid)
    assert [f["name"] for f in listed["files"]] == ["outline.pdf"] and listed["student"]["email"]


def test_a_student_cannot_upload_into_someone_elses_folder(student, other):
    uid, client = student
    other_id, _ = other
    with pytest.raises(Exception):
        client.storage.from_(BUCKET).upload(f"{other_id}/{uuid.uuid4()}/x.pdf", PDF, {"content-type": "application/pdf"})


def test_only_allowed_file_types(student):
    uid, client = student
    with pytest.raises(Exception):
        client.storage.from_(BUCKET).upload(f"{uid}/{uuid.uuid4()}/notes.txt", b"plain text", {"content-type": "text/plain"})


def test_at_most_five_files_per_request(student):
    uid, client = student
    rid, _ = request_with_file(client, uid)
    for i in range(4):
        client.table("course_request_files").insert({"request_id": rid, "student_id": uid, "path": f"{uid}/{rid}/f{i}.pdf",
                                                     "name": f"f{i}.pdf", "size_bytes": 10, "content_type": "application/pdf"}).execute()
    with pytest.raises(APIError):
        client.table("course_request_files").insert({"request_id": rid, "student_id": uid, "path": f"{uid}/{rid}/f9.pdf",
                                                     "name": "f9.pdf", "size_bytes": 10, "content_type": "application/pdf"}).execute()


def test_the_bucket_limits_size_and_type(db):
    bucket = db.storage.get_bucket(BUCKET)
    assert bucket.public is False and bucket.file_size_limit == 20 * 1024 * 1024
    assert "application/pdf" in bucket.allowed_mime_types and "text/plain" not in bucket.allowed_mime_types


def test_a_student_cannot_set_their_own_request_status(student):
    uid, client = student
    rid, _ = request_with_file(client, uid)
    with pytest.raises(APIError):
        client.table("course_requests").update({"status": "added"}).eq("id", rid).execute()


# -- manager actions, each audited -----------------------------------------------------------

def notes_for(client) -> list[str]:
    return sorted(n["kind"] for n in client.table("notifications").select("kind").like("kind", "course%").execute().data)


def test_request_status_changes_notify_the_student_and_are_audited(db, fx, student, manager):
    uid, client = student
    mgr_id, mgr = manager
    rid, _ = request_with_file(client, uid, code="TEST 000")
    mgr.rpc("manage_set_request_status", {"p_request": rid, "p_status": "in_progress"}).execute()
    with pytest.raises(APIError):  # a reason is required to decline
        mgr.rpc("manage_set_request_status", {"p_request": rid, "p_status": "declined", "p_note": " "}).execute()
    mgr.rpc("manage_set_request_status", {"p_request": rid, "p_status": "added", "p_course_code": "TEST 000"}).execute()
    row = client.table("course_requests").select("status, course_id").eq("id", rid).single().execute().data
    assert row == {"status": "added", "course_id": fx.course_id}
    assert client.table("enrollments").select("course_id").eq("course_id", fx.course_id).execute().data
    assert notes_for(client) == ["course_added", "course_request_in_progress"]
    link = client.table("notifications").select("link").eq("kind", "course_added").execute().data[0]["link"]
    assert link == f"/courses/{fx.course_id}"  # the course page is addressed by id
    audit = audit_rows(db, rid)
    assert [a["action"] for a in audit] == ["request.status", "request.status"] and all(a["actor_id"] == mgr_id for a in audit)
    assert audit[1]["changes"]["status"] == {"from": "in_progress", "to": "added"}


def test_declining_needs_and_shows_a_reason(db, student, manager):
    uid, client = student
    _, mgr = manager
    rid, _ = request_with_file(client, uid, code="XYZ 999")
    mgr.rpc("manage_set_request_status", {"p_request": rid, "p_status": "declined",
                                          "p_note": "No course files were found for this code."}).execute()
    assert client.table("course_requests").select("status, admin_note").eq("id", rid).single().execute().data == {
        "status": "declined", "admin_note": "No course files were found for this code."}
    body = client.table("notifications").select("body").eq("kind", "course_request_declined").execute().data[0]["body"]
    assert body == "Reason: No course files were found for this code."


def test_edit_a_topic(db, fx, manager):
    mgr_id, mgr = manager
    tid = fx.topic_ids["beta"]
    mgr.rpc("manage_update_topic", {"p_topic": tid, "p_title": "Beta, renamed", "p_summary": "A short summary."}).execute()
    assert db.table("topics").select("title, summary").eq("id", tid).single().execute().data == {
        "title": "Beta, renamed", "summary": "A short summary."}
    a = audit_rows(db, tid)[-1]
    assert a["action"] == "topic.update" and a["changes"]["title"]["to"] == "Beta, renamed" and a["actor_id"] == mgr_id


def test_edit_a_question_and_reject_a_bad_shape(db, fx, manager):
    _, mgr = manager
    qs = mgr.rpc("manage_questions", {"p_topic": fx.topic_ids["alpha"]}).execute().data
    q = next(x for x in qs if x["format"] == "single_choice")
    assert q["correct_answer"]  # managers see answers
    with pytest.raises(APIError):  # two answers for a single-choice question
        mgr.rpc("manage_update_question", {"p_question": q["id"], "p_stem": q["stem"], "p_options": q["options"],
                                           "p_correct": [o["key"] for o in q["options"][:2]], "p_explanation": "x"}).execute()
    mgr.rpc("manage_update_question", {"p_question": q["id"], "p_stem": q["stem"] + " (edited)", "p_options": q["options"],
                                       "p_correct": q["correct_answer"], "p_explanation": "A clearer explanation."}).execute()
    row = db.table("questions").select("stem, explanation").eq("id", q["id"]).single().execute().data
    assert row["stem"].endswith("(edited)") and row["explanation"] == "A clearer explanation."
    assert audit_rows(db, q["id"])[-1]["action"] == "question.update"


def test_hide_a_question_from_quizzes(db, fx, manager, student):
    _, mgr = manager
    qs = mgr.rpc("manage_questions", {"p_topic": fx.topic_ids["alpha"]}).execute().data
    hidden = qs[0]["id"]
    mgr.rpc("manage_set_question_hidden", {"p_question": hidden, "p_hidden": True}).execute()
    _, client = student
    for _ in range(3):  # the topic quiz never serves it
        started = client.rpc("start_quiz", {"p_quiz_id": fx.topic_quiz_id}).execute().data
        assert hidden not in {q["id"] for q in started["questions"]}
    mgr.rpc("manage_set_question_hidden", {"p_question": hidden, "p_hidden": False}).execute()
    assert [a["action"] for a in audit_rows(db, hidden)][-2:] == ["question.hide", "question.show"]


def test_add_and_fix_a_resource_link(db, fx, manager):
    _, mgr = manager
    rid = mgr.rpc("manage_save_resource", {"p_resource": None, "p_topic": fx.topic_ids["alpha"], "p_title": "Video: Alpha",
                                           "p_type": "video", "p_url": "https://www.youtube.com/watch?v=abc"}).execute().data
    with pytest.raises(APIError):
        mgr.rpc("manage_save_resource", {"p_resource": rid, "p_topic": fx.topic_ids["alpha"], "p_title": "Video: Alpha",
                                         "p_type": "video", "p_url": "javascript:alert(1)"}).execute()
    mgr.rpc("manage_save_resource", {"p_resource": rid, "p_topic": fx.topic_ids["alpha"], "p_title": "Video: Alpha (fixed)",
                                     "p_type": "video", "p_url": "https://www.youtube.com/watch?v=def"}).execute()
    assert db.table("resources").select("title, url").eq("id", rid).single().execute().data == {
        "title": "Video: Alpha (fixed)", "url": "https://www.youtube.com/watch?v=def"}
    assert [a["action"] for a in audit_rows(db, rid)] == ["resource.add", "resource.update"]


def test_mark_a_course_reviewed(db, fx, manager):
    _, mgr = manager
    db.table("courses").update({"is_reviewed": False}).eq("id", fx.course_id).execute()
    mgr.rpc("manage_set_course_reviewed", {"p_course": fx.course_id, "p_reviewed": True}).execute()
    assert db.table("courses").select("is_reviewed").eq("id", fx.course_id).single().execute().data["is_reviewed"] is True
    a = audit_rows(db, fx.course_id)[-1]
    assert a["action"] == "course.review" and a["changes"] == {"is_reviewed": {"from": False, "to": True}}


def test_managers_read_the_audit_trail_with_names(manager):
    _, mgr = manager
    trail = mgr.rpc("manage_audit", {"p_limit": 20}).execute().data
    assert trail and all({"action", "summary", "changes", "created_at", "actor"} <= set(t) for t in trail)
