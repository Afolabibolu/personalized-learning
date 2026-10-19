"""Simulated students for training data (simulated data, not real students).

Every rule and parameter is in CONFIG below, with a fixed random seed, and
describe_rules() writes them out in plain words for Chapter Four
(ml/results/simulation_rules.md, written by scripts/seed_demo.py).

The model, per student and topic, in log-odds of answering a question right:

    ability - difficulty + prior + learned * retention + attempt noise

  - ability (student) and difficulty (topic) are drawn at random.
  - learned is the practice effect: it grows with study minutes and earlier
    attempts, with diminishing returns (max_gain * (1 - exp(-minutes / scale))).
  - retention is the forgetting curve: exp(-days since last practice / stability),
    so what was learned fades the longer a topic goes unstudied.
  - attempt noise varies from attempt to attempt, and each answer is a random
    draw on top, so no single feature decides the outcome.

The 50% label rule is never used here. Scores come from these rules; the label
is applied afterwards by features.training_rows().
"""

import math
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta

import numpy as np


# --- Simulation config: every rule parameter lives here ---------------------

@dataclass(frozen=True)
class Habit:
    name: str
    share: float  # proportion of students with this habit
    daily_study_probability: float  # chance of a session on a given topic on an ordinary day
    session_minutes: tuple[int, int]  # range of minutes per session
    cram_probability: float  # chance of a session on a topic in the 2 days before its quiz


@dataclass(frozen=True)
class SimConfig:
    seed: int = 2026
    students: int = 80
    days: int = 42  # six weeks of activity

    # Student ability and topic difficulty (log-odds), drawn once
    ability_sd: float = 0.8
    difficulty_sd: float = 0.6
    prior_sd: float = 0.3  # extra per student-topic variation (prior exposure)

    # Practice effect, with diminishing returns
    # Calibrated once so that about a third of topics end up needing attention
    # (label balance only; never tuned to make one model win).
    max_learning_gain: float = 1.2  # log-odds gained when a topic is fully practised
    practice_scale_minutes: float = 240.0  # minutes of practice for about 63% of the maximum gain
    quiz_practice_minutes: float = 20.0  # each quiz attempt counts as this much practice

    # Forgetting curve
    memory_stability_days: float = 7.0  # retention = exp(-days since last practice / stability)

    # Noise
    attempt_noise_sd: float = 0.5  # attempt-to-attempt variation ("form on the day")

    # Quizzes
    topic_quiz_questions: int = 5
    diagnostic_questions_per_topic: int = 3
    first_quiz_day: tuple[int, int] = (4, 9)  # first topic quiz falls in this day range
    days_between_quizzes: tuple[int, int] = (5, 10)
    quiz_attendance: float = 0.85  # chance a student takes a scheduled quiz

    habits: tuple[Habit, ...] = (
        Habit("steady: studies often in short sessions", 0.40, 0.16, (15, 30), 0.30),
        Habit("crammer: studies little, then hard just before quizzes", 0.35, 0.02, (45, 120), 0.75),
        Habit("rare: studies seldom", 0.25, 0.04, (20, 60), 0.15),
    )


CONFIG = SimConfig()
ACTIVITIES = ["reading", "video", "practice"]

# -----------------------------------------------------------------------------


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
    habit: str = ""
    attempts: list[SimAttempt] = field(default_factory=list)
    logs: list[SimStudyLog] = field(default_factory=list)


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def learned(practice_minutes: float, cfg: SimConfig = CONFIG) -> float:
    """Practice effect with diminishing returns."""
    return cfg.max_learning_gain * (1.0 - math.exp(-practice_minutes / cfg.practice_scale_minutes))


def retention(days_since_practice: float | None, cfg: SimConfig = CONFIG) -> float:
    """Forgetting curve. Nothing learned yet means nothing to retain."""
    if days_since_practice is None:
        return 0.0
    return math.exp(-days_since_practice / cfg.memory_stability_days)


def topic_difficulties(rng: np.random.Generator, n: int, cfg: SimConfig = CONFIG) -> list[float]:
    return [float(d) for d in rng.normal(0.0, cfg.difficulty_sd, size=n)]


def pick_habit(rng: np.random.Generator, cfg: SimConfig = CONFIG) -> Habit:
    shares = np.array([h.share for h in cfg.habits])
    return cfg.habits[int(rng.choice(len(cfg.habits), p=shares / shares.sum()))]


def quiz_schedule(rng: np.random.Generator, cfg: SimConfig = CONFIG) -> list[int]:
    days, day = [], int(rng.integers(cfg.first_quiz_day[0], cfg.first_quiz_day[1] + 1))
    while day < cfg.days:
        days.append(day)
        day += int(rng.integers(cfg.days_between_quizzes[0], cfg.days_between_quizzes[1] + 1))
    return days


def simulate_student(rng: np.random.Generator, courses: list[SimCourse], end: datetime,
                     cfg: SimConfig = CONFIG) -> SimStudent:
    start = end - timedelta(days=cfg.days)
    ability = rng.normal(0.0, cfg.ability_sd)
    habit = pick_habit(rng, cfg)
    topics = [t for c in courses for t in c.topics]
    base = {t.topic_id: ability - t.difficulty + rng.normal(0.0, cfg.prior_sd) for t in topics}
    practice = {t.topic_id: 0.0 for t in topics}  # minutes of practice so far
    last_practice: dict[str, int | None] = {t.topic_id: None for t in topics}
    schedule = {t.topic_id: quiz_schedule(rng, cfg) for t in topics}
    student = SimStudent(habit=habit.name)

    def moment(day: int, earliest: float = 8, latest: float = 22) -> datetime:
        return start + timedelta(days=day, hours=float(rng.uniform(earliest, latest)))

    def answer(topic: SimTopic, n: int, day: int) -> list[tuple[str, bool]]:
        last = last_practice[topic.topic_id]
        log_odds = (base[topic.topic_id]
                    + learned(practice[topic.topic_id], cfg) * retention(None if last is None else day - last, cfg)
                    + rng.normal(0.0, cfg.attempt_noise_sd))
        p = sigmoid(log_odds)
        chosen = rng.choice(topic.question_ids, size=min(n, len(topic.question_ids)), replace=False)
        return [(str(q), bool(rng.random() < p)) for q in chosen]

    def add_attempt(quiz_id: str, answers: list[tuple[str, bool]], day: int) -> None:
        # Quizzes happen in the evening, after that day's study sessions.
        started = moment(day, 18, 22)
        student.attempts.append(SimAttempt(
            id=str(uuid.UUID(bytes=rng.bytes(16), version=4)),
            quiz_id=quiz_id,
            started_at=started,
            completed_at=started + timedelta(minutes=float(rng.uniform(3, 15))),
            answers=answers,
        ))

    # Day 0: a diagnostic on every course, before any study.
    for course in courses:
        answers = [a for t in course.topics for a in answer(t, cfg.diagnostic_questions_per_topic, 0)]
        add_attempt(course.diagnostic_quiz_id, answers, 0)
        for t in course.topics:
            practice[t.topic_id] += cfg.quiz_practice_minutes * cfg.diagnostic_questions_per_topic / cfg.topic_quiz_questions
            last_practice[t.topic_id] = 0

    for day in range(1, cfg.days):
        for topic in topics:
            tid = topic.topic_id
            quiz_soon = any(0 < q - day <= 2 for q in schedule[tid])
            chance = habit.cram_probability if quiz_soon else habit.daily_study_probability
            if rng.random() < chance:
                minutes = int(rng.integers(habit.session_minutes[0], habit.session_minutes[1] + 1))
                practice[tid] += minutes
                last_practice[tid] = day
                student.logs.append(SimStudyLog(tid, minutes, str(rng.choice(ACTIVITIES)), moment(day, 8, 17)))

            if day in schedule[tid] and rng.random() < cfg.quiz_attendance:
                add_attempt(topic.quiz_id, answer(topic, cfg.topic_quiz_questions, day), day)
                practice[tid] += cfg.quiz_practice_minutes
                last_practice[tid] = day

    student.attempts.sort(key=lambda a: a.started_at)
    student.logs.sort(key=lambda log: log.logged_at)
    return student


def describe_rules(cfg: SimConfig = CONFIG) -> str:
    """The simulation in plain words, with every parameter value, for Chapter Four."""
    habits = "\n".join(
        f"| {h.name} | {h.share:.0%} | {h.daily_study_probability:.0%} | {h.session_minutes[0]}–{h.session_minutes[1]} min "
        f"| {h.cram_probability:.0%} |" for h in cfg.habits)
    half_gain = cfg.practice_scale_minutes * math.log(2)
    half_life = cfg.memory_stability_days * math.log(2)
    return f"""# Simulation rules (simulated data)

The training data for the models comes from simulated students, not real students. This file is
written by `scripts/seed_demo.py` from the config block at the top of `ml/training/synthetic.py`,
so it always matches the data in the database.

## Population and time span

- {cfg.students} simulated students, each active for {cfg.days} days (six weeks), on the two prototype courses
  (CSC 531 and CSC 574, 12 topics in all).
- Random seed {cfg.seed}: running `python scripts/seed_demo.py` again produces the same students.

## How a student answers a question

For a student and a topic, the chance of answering a question correctly is

    P(correct) = sigmoid( ability − difficulty + prior + learned × retention + noise )

on the log-odds scale, where:

| Term | Rule | Parameter values |
| --- | --- | --- |
| ability | Each student has a hidden ability level, drawn once at random. | Normal(0, {cfg.ability_sd}) |
| difficulty | Each topic has a hidden difficulty, drawn once at random. | Normal(0, {cfg.difficulty_sd}) |
| prior | Extra variation per student and topic (for example, prior exposure). | Normal(0, {cfg.prior_sd}) |
| learned | **Practice effect with diminishing returns.** Grows with study minutes and earlier quiz attempts on the topic: {cfg.max_learning_gain} × (1 − e^(−minutes / {cfg.practice_scale_minutes:g})). Each quiz attempt counts as {cfg.quiz_practice_minutes:g} minutes of practice. | Half of the maximum gain after about {half_gain:.0f} minutes; the next hour adds less than the first. |
| retention | **Forgetting curve.** What was learned fades with days since the topic was last studied or quizzed: e^(−days / {cfg.memory_stability_days:g}). Nothing learned yet means nothing to retain. | Half-life of about {half_life:.1f} days. |
| noise | Attempt-to-attempt variation ("form on the day"). | Normal(0, {cfg.attempt_noise_sd}) per attempt |

Each answer is then a random draw with that probability, so the same student can score differently on
two attempts at the same level of preparation. No single feature decides the outcome.

## Study habits

Each student has one habit, assigned at random in these proportions:

| Habit | Share | Chance of a session on a topic on an ordinary day | Session length | Chance of a session in the 2 days before that topic's quiz |
| --- | --- | --- | --- | --- |
{habits}

## Quizzes

- Day 0: a diagnostic quiz on each course, {cfg.diagnostic_questions_per_topic} questions per topic, before any study.
- Each topic then has its own quiz schedule: the first quiz between days {cfg.first_quiz_day[0]} and {cfg.first_quiz_day[1]},
  then one every {cfg.days_between_quizzes[0]}–{cfg.days_between_quizzes[1]} days. A student takes each scheduled quiz
  with probability {cfg.quiz_attendance:.0%}.
- A topic quiz has {cfg.topic_quiz_questions} questions drawn from the topic's 10. Quizzes happen in the evening,
  after that day's study sessions.

## What the simulation does not do

- **It never uses the 50% label rule.** Scores come only from the rules above. The label ("requires attention"
  when the next attempt scores below 50%) is applied afterwards, when the training rows are built.
- It does not copy any real student's data, and its results are not evidence about real students. It shows
  that the pipeline (features, labels, models, ranking) works on data with known, documented learning patterns.
"""
