# Simulation rules (simulated data)

The training data for the models comes from simulated students, not real students. This file is
written by `scripts/seed_demo.py` from the config block at the top of `ml/training/synthetic.py`,
so it always matches the data in the database.

## Population and time span

- 80 simulated students, each active for 42 days (six weeks), on the two prototype courses
  (CSC 531 and CSC 574, 12 topics in all).
- Random seed 2026: running `python scripts/seed_demo.py` again produces the same students.

## How a student answers a question

For a student and a topic, the chance of answering a question correctly is

    P(correct) = sigmoid( ability − difficulty + prior + learned × retention + noise )

on the log-odds scale, where:

| Term | Rule | Parameter values |
| --- | --- | --- |
| ability | Each student has a hidden ability level, drawn once at random. | Normal(0, 0.8) |
| difficulty | Each topic has a hidden difficulty, drawn once at random. | Normal(0, 0.6) |
| prior | Extra variation per student and topic (for example, prior exposure). | Normal(0, 0.3) |
| learned | **Practice effect with diminishing returns.** Grows with study minutes and earlier quiz attempts on the topic: 1.2 × (1 − e^(−minutes / 240)). Each quiz attempt counts as 20 minutes of practice. | Half of the maximum gain after about 166 minutes; the next hour adds less than the first. |
| retention | **Forgetting curve.** What was learned fades with days since the topic was last studied or quizzed: e^(−days / 7). Nothing learned yet means nothing to retain. | Half-life of about 4.9 days. |
| noise | Attempt-to-attempt variation ("form on the day"). | Normal(0, 0.5) per attempt |

Each answer is then a random draw with that probability, so the same student can score differently on
two attempts at the same level of preparation. No single feature decides the outcome.

## Study habits

Each student has one habit, assigned at random in these proportions:

| Habit | Share | Chance of a session on a topic on an ordinary day | Session length | Chance of a session in the 2 days before that topic's quiz |
| --- | --- | --- | --- | --- |
| steady: studies often in short sessions | 40% | 16% | 15–30 min | 30% |
| crammer: studies little, then hard just before quizzes | 35% | 2% | 45–120 min | 75% |
| rare: studies seldom | 25% | 4% | 20–60 min | 15% |

## Quizzes

- Day 0: a diagnostic quiz on each course, 3 questions per topic, before any study.
- Each topic then has its own quiz schedule: the first quiz between days 4 and 9,
  then one every 5–10 days. A student takes each scheduled quiz
  with probability 85%.
- A topic quiz has 5 questions drawn from the topic's 10. Quizzes happen in the evening,
  after that day's study sessions.

## What the simulation does not do

- **It never uses the 50% label rule.** Scores come only from the rules above. The label ("requires attention"
  when the next attempt scores below 50%) is applied afterwards, when the training rows are built.
- It does not copy any real student's data, and its results are not evidence about real students. It shows
  that the pipeline (features, labels, models, ranking) works on data with known, documented learning patterns.
