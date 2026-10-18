import os

import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app import data
from app.recommender import recommend_course
from training.features import prediction_rows, to_frames

load_dotenv()

app = FastAPI(title="Recommendation service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_ORIGIN", "http://localhost:5173")],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


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
    courses = data.load_courses(db)
    attempts = data.completed_attempts_per_course(db, student_id)
    scores, logs = to_frames(*data.student_history(db, student_id))
    used = data.used_resource_ids(db, student_id)
    now = pd.Timestamp.now(tz="UTC")

    recs, summary = [], []
    for course in courses:
        features = prediction_rows(scores, logs, course.topic_ids, now)
        course_recs = recommend_course(course, attempts.get(course.course_id, 0), features, models, used)
        recs.extend(course_recs)
        summary.append({
            "course_id": course.course_id,
            "completed_attempts": attempts.get(course.course_id, 0),
            "source": course_recs[0].source if course_recs else None,
            "count": len(course_recs),
        })

    data.replace_pending(db, student_id, recs)
    return {
        "student_id": student_id,
        "model_version": models.version if models else None,
        "courses": summary,
    }
