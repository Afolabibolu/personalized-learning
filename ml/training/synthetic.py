"""Simulated students for training data (simulated data, not real students).

Each student has an ability, a diligence level and a hidden mastery per topic.
Studying raises mastery; time since the topic was last studied lowers the
mastery that shows up in a quiz (forgetting); taking a quiz adds a little
practice. Each question is answered correctly with probability
sigmoid(effective mastery). So a student's next score depends on study time,
past scores (through mastery) and days since last studied, plus noise.
"""

import math
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta

import numpy as np

SIM_DAYS = 42
STUDY_GAIN_PER_MINUTE = 0.006
FORGETTING_PER_DAY = 0.03
FORGETTING_CAP_DAYS = 30
QUIZ_PRACTICE_GAIN = 0.05
DAILY_STUDY_PROBABILITY = 0.12  # scaled by diligence
DAILY_QUIZ_PROBABILITY = 0.25
MIN_DAYS_BETWEEN_QUIZZES = 5
TOPIC_QUIZ_QUESTIONS = 5
DIAGNOSTIC_QUESTIONS_PER_TOPIC = 3
STUDY_MINUTES = [15, 20, 30, 45, 60, 90]
ACTIVITIES = ["reading", "video", "practice"]


@dataclass
class SimTopic:
    topic_id: str
    course_id: str
    quiz_id: str
    question_ids: list[str]
    difficulty: float


@dataclass
class SimCourse:
    course_id: str
    diagnostic_quiz_id: str
    topics: list[SimTopic]


@dataclass
class SimAttempt:
    id: str
    quiz_id: str
    started_at: datetime
    completed_at: datetime
    answers: list[tuple[str, bool]]  # (question_id, is_correct)

    @property
    def score(self) -> float:
        return round(100.0 * sum(ok for _, ok in self.answers) / len(self.answers), 2)


@dataclass
class SimStudyLog:
    topic_id: str
    duration_minutes: int
    activity_type: str
    logged_at: datetime


@dataclass
class SimStudent:
    attempts: list[SimAttempt] = field(default_factory=list)
    logs: list[SimStudyLog] = field(default_factory=list)


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def simulate_student(rng: np.random.Generator, courses: list[SimCourse], end: datetime) -> SimStudent:
    start = end - timedelta(days=SIM_DAYS)
    ability = rng.normal(0.0, 0.7)
    diligence = rng.beta(2, 2)
    topics = [t for c in courses for t in c.topics]
    mastery = {t.topic_id: ability - t.difficulty + rng.normal(0.0, 0.4) for t in topics}
    last_studied: dict[str, int | None] = {t.topic_id: None for t in topics}
    last_quiz: dict[str, int] = {}
    student = SimStudent()

    def moment(day: int) -> datetime:
        return start + timedelta(days=day, hours=float(rng.uniform(8, 22)))

    def effective(topic_id: str, day: int) -> float:
        studied = last_studied[topic_id]
        gap = FORGETTING_CAP_DAYS if studied is None else min(day - studied, FORGETTING_CAP_DAYS)
        return mastery[topic_id] - FORGETTING_PER_DAY * gap

    def answer(topic: SimTopic, n: int, day: int) -> list[tuple[str, bool]]:
        p = sigmoid(effective(topic.topic_id, day))
        chosen = rng.choice(topic.question_ids, size=min(n, len(topic.question_ids)), replace=False)
        return [(str(q), bool(rng.random() < p)) for q in chosen]

    def add_attempt(quiz_id: str, answers: list[tuple[str, bool]], day: int) -> None:
        started = moment(day)
        student.attempts.append(SimAttempt(
            id=str(uuid.UUID(bytes=rng.bytes(16), version=4)),
            quiz_id=quiz_id,
            started_at=started,
            completed_at=started + timedelta(minutes=float(rng.uniform(3, 15))),
            answers=answers,
        ))

    # Day 0: a diagnostic quiz on every course.
    for course in courses:
        answers = [a for t in course.topics for a in answer(t, DIAGNOSTIC_QUESTIONS_PER_TOPIC, 0)]
        add_attempt(course.diagnostic_quiz_id, answers, 0)
        for t in course.topics:
            last_quiz[t.topic_id] = 0

    for day in range(1, SIM_DAYS):
        for topic in topics:
            if rng.random() < DAILY_STUDY_PROBABILITY * diligence:
                minutes = int(rng.choice(STUDY_MINUTES))
                mastery[topic.topic_id] += STUDY_GAIN_PER_MINUTE * minutes
                last_studied[topic.topic_id] = day
                student.logs.append(SimStudyLog(topic.topic_id, minutes, str(rng.choice(ACTIVITIES)), moment(day)))

            if day - last_quiz[topic.topic_id] >= MIN_DAYS_BETWEEN_QUIZZES and rng.random() < DAILY_QUIZ_PROBABILITY:
                add_attempt(topic.quiz_id, answer(topic, TOPIC_QUIZ_QUESTIONS, day), day)
                mastery[topic.topic_id] += QUIZ_PRACTICE_GAIN
                last_quiz[topic.topic_id] = day

    # Events are generated per day, so keep each list in time order.
    student.attempts.sort(key=lambda a: a.started_at)
    student.logs.sort(key=lambda log: log.logged_at)
    return student


def topic_difficulties(rng: np.random.Generator, n: int) -> list[float]:
    return [float(d) for d in rng.normal(0.0, 0.5, size=n)]
