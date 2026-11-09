import asyncio
import logging
import os
from contextlib import asynccontextmanager

import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from app import data, emails, notify
from app.recommender import recommend_course, top_overall
from training.features import prediction_rows, to_frames

load_dotenv()
log = logging.getLogger("emails")


async def email_loop() -> None:
    """Email reminders: one check every 15 minutes while the service runs (EMAIL_SCHEDULER=off to stop it)."""
    while True:
        try:
            results = await asyncio.to_thread(emails.run_once, data.service_client())
            if results:
                log.warning("email check: %s", ", ".join(f"{r['kind']} {r['status']}" for r in results))
        except Exception:  # a failed check must never stop the service; the next one retries
            log.exception("email check failed")
        await asyncio.sleep(emails.CHECK_EVERY_SECONDS)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    task = asyncio.create_task(email_loop()) if os.getenv("EMAIL_SCHEDULER", "on").lower() != "off" else None
    yield
    if task:
        task.cancel()


app = FastAPI(title="Recommendation service", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_ORIGIN", "http://localhost:5173")],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/email/unsubscribe", response_class=HTMLResponse)
def unsubscribe(token: str = ""):
    """Turns email reminders off for the student in the signed token, without logging in."""
    student_id = emails.verify_token(token)
    if not student_id:
        return HTMLResponse(page("This link is not valid", "Turn email reminders off from your Profile page instead."), 400)
    data.service_client().table("profiles").update({"email_reminders": False}).eq("id", student_id).execute()
    return page("Email reminders are off",
                "You will not get reminder emails any more. Reminders still appear in the app, and you can turn "
                "emails back on from your Profile page.")


def page(title: str, text: str) -> str:
    app_url = os.getenv("APP_URL", "http://localhost:5173")
    return (f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">'
            f'<title>{title}</title></head><body style="font-family:Inter,Arial,sans-serif;background:#f8fafc;color:#0f172a">'
            f'<div style="max-width:480px;margin:48px auto;padding:24px;background:#fff;border:1px solid #e2e8f0;border-radius:16px">'
            f'<p style="font-weight:700;color:#4f46e5;margin:0 0 12px">Learning Support</p><h1 style="font-size:20px">{title}</h1>'
            f'<p>{text}</p><p><a href="{app_url}/profile" style="color:#4f46e5">Open your Profile</a></p></div></body></html>')


def authenticated_user_id(authorization: str | None) -> str:
    """Verifies the caller's access token with Supabase Auth (no local JWT decoding)."""
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    token = authorization.split(" ", 1)[1]
    try:
        response = data.service_client().auth.get_user(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    if not response or not response.user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return response.user.id


@app.post("/recommend")
def recommend(authorization: str | None = Header(default=None)):
    student_id = authenticated_user_id(authorization)
    db = data.service_client()

    models = data.load_models()
    enrolled = data.enrolled_course_ids(db, student_id)
    courses = [c for c in data.load_courses(db) if c.course_id in enrolled]
    attempts = data.completed_attempts_per_course(db, student_id)
    scores, logs = to_frames(*data.student_history(db, student_id))
    used = data.used_resource_ids(db, student_id)
    preferred = data.learning_preferences(db, student_id)
    previous_top = data.previous_top_topic(db, student_id)
    threshold = data.cold_start_threshold(db)
    diagnostic = data.diagnostic_recommendations(db, student_id)
    now = pd.Timestamp.now(tz="UTC")

    candidates, days_since = [], {}
    for course in courses:
        features = prediction_rows(scores, logs, course.topic_ids, now)
        days_since.update(dict(zip(features["topic_id"], features["days_since_last_studied"])))
        candidates.extend(recommend_course(course, attempts.get(course.course_id, 0), features, models, used, preferred,
                                           threshold=threshold, diagnostic=diagnostic.get(course.course_id)))
    # Getting started and diagnostic lists per course; ML recommendations only for the top topics overall.
    recs = top_overall(candidates)

    course_of_topic = {t: c.course_id for c in courses for t in c.topic_ids}
    summary = []
    for course in courses:
        course_recs = [r for r in recs if course_of_topic[r.topic_id] == course.course_id]
        summary.append({
            "course_id": course.course_id,
            "completed_attempts": attempts.get(course.course_id, 0),
            "source": course_recs[0].source if course_recs else None,
            "count": len(course_recs),
        })

    data.replace_pending(db, student_id, recs)
    sent = data.insert_notifications(db, student_id, notify.decide(previous_top, recs, days_since, data.topic_titles(db)))
    return {
        "notifications_sent": sent,
        "student_id": student_id,
        "model_version": models.version if models else None,
        "threshold": threshold,
        "courses": summary,
    }
