from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from training.features import training_rows
from training.synthetic import CONFIG, SimCourse, SimTopic, simulate_student

END = datetime(2026, 10, 1, tzinfo=timezone.utc)


def courses():
    return [
        SimCourse(f"c{c}", f"diag{c}", [
            SimTopic(f"t{c}{i}", f"c{c}", f"quiz{c}{i}", [f"q{c}{i}-{k}" for k in range(10)], 0.0)
            for i in range(6)
        ])
        for c in range(2)
    ]


def population(seed: int, n: int = 60):
    rng = np.random.default_rng(seed)
    cs = courses()
    topic_of = {q: t.topic_id for c in cs for t in c.topics for q in t.question_ids}
    scores, logs = [], []
    for s in range(n):
        student = simulate_student(rng, cs, END)
        for a in student.attempts:
            per_topic: dict[str, list[bool]] = {}
            for q, ok in a.answers:
                per_topic.setdefault(topic_of[q], []).append(ok)
            for t, oks in per_topic.items():
                scores.append({"student_id": s, "topic_id": t, "completed_at": a.completed_at, "score": 100 * sum(oks) / len(oks)})
        for log in student.logs:
            logs.append({"student_id": s, "topic_id": log.topic_id, "logged_at": log.logged_at, "duration_minutes": log.duration_minutes})
    s, l = pd.DataFrame(scores), pd.DataFrame(logs)
    s["completed_at"] = pd.to_datetime(s["completed_at"], utc=True)
    l["logged_at"] = pd.to_datetime(l["logged_at"], utc=True)
    return s, l


def test_same_seed_gives_same_students():
    a = simulate_student(np.random.default_rng(7), courses(), END)
    b = simulate_student(np.random.default_rng(7), courses(), END)
    assert [x.answers for x in a.attempts] == [x.answers for x in b.attempts]
    assert [x.id for x in a.attempts] == [x.id for x in b.attempts]


def test_events_stay_inside_the_simulated_window():
    student = simulate_student(np.random.default_rng(1), courses(), END)
    times = [a.completed_at for a in student.attempts] + [log.logged_at for log in student.logs]
    assert min(times) >= END - pd.Timedelta(days=CONFIG.days)
    assert max(times) < END


def test_every_student_takes_one_diagnostic_per_course():
    student = simulate_student(np.random.default_rng(3), courses(), END)
    diagnostics = [a for a in student.attempts if a.quiz_id.startswith("diag")]
    assert sorted(a.quiz_id for a in diagnostics) == ["diag0", "diag1"]
    assert all(len(a.answers) == 18 for a in diagnostics)


def test_labels_are_balanced_enough_to_learn():
    rows = training_rows(*population(2026))
    assert 0.2 < rows["requires_attention"].mean() < 0.6


def test_studying_and_recency_relate_to_the_label_as_designed():
    rows = training_rows(*population(2026))
    corr = rows.corr(numeric_only=True)["requires_attention"]
    assert corr["total_minutes"] < -0.1
    assert corr["last_score"] < -0.1
    assert corr["days_since_last_studied"] > 0.1


def test_forgetting_curve_decays_with_time_since_practice():
    from training.synthetic import retention
    assert retention(None) == 0.0
    assert retention(0) == 1.0
    assert 1.0 > retention(3) > retention(10) > retention(30) > 0.0


def test_practice_effect_has_diminishing_returns():
    from training.synthetic import CONFIG, learned
    first_hour = learned(60) - learned(0)
    fifth_hour = learned(300) - learned(240)
    assert first_hour > fifth_hour > 0
    assert learned(10_000) <= CONFIG.max_learning_gain


def test_every_study_habit_appears_in_the_population():
    from training.synthetic import CONFIG
    rng = np.random.default_rng(2026)
    habits = {simulate_student(rng, courses(), END).habit for _ in range(60)}
    assert habits == {h.name for h in CONFIG.habits}


def test_simulation_never_uses_the_label_rule():
    source = (Path(__file__).resolve().parent.parent / "training" / "synthetic.py").read_text()
    assert "ATTENTION_THRESHOLD" not in source
    assert "requires_attention" not in source


def test_rules_file_lists_the_parameter_values():
    from training.synthetic import CONFIG, describe_rules
    text = describe_rules()
    assert "simulated students, not real students" in text
    for value in [CONFIG.seed, CONFIG.max_learning_gain, CONFIG.memory_stability_days, CONFIG.attempt_noise_sd]:
        assert f"{value:g}" in text
    assert "never uses the 50% label rule" in text
