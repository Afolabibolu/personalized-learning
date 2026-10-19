# Test cases (Chapter Four)

Run 2026-10-19 17:14 with `python scripts/run_test_cases.py`. One or more cases per functional (FR1–FR6) and non-functional (NFR1–NFR5) requirement from Chapter Three, including the cold-start case (Section 3.14). Every case was run against the live system; the evidence lines are the actual output.

**Summary:** 15 pass, 1 partial, 0 fail.

| ID | Requirement | Test | Expected result | Actual result | Pass/Fail |
| --- | --- | --- | --- | --- | --- |
| TC-01 | FR1 | Register and create a profile | Account created without email confirmation; onboarding saves department, level and preferences to the student's own profile row | 3 of 3 checks passed | **Pass** |
| TC-02 | FR1 | Sign in, protected pages, sign out, update profile | Signed-out visits redirect to /login; sign-in lands on the dashboard; a student can update their own profile but not is_simulated | 8 of 8 checks passed | **Pass** |
| TC-03 | FR2 | Diagnostic quiz with per-topic results | Three questions from every topic; graded server-side; results show a score per topic and each answer with explanation | 5 of 5 checks passed | **Pass** |
| TC-04 | FR2 | Topic quiz grading and question selection | All four formats graded correctly (partial multi-select is wrong); unseen questions first; a submitted attempt cannot be resubmitted; latest score per topic is correct | 3 of 3 checks passed | **Pass** |
| TC-05 | FR3 | Log a study session | Session saved with topic, duration and activity type; logging for someone else is refused | 3 of 3 checks passed | **Pass** |
| TC-06 | FR4 | ML recommendations rank weak topics first | Top 3 overall from the models; the two weak topics ranked 1 and 2; re-running does not duplicate pending recommendations | 4 of 4 checks passed | **Pass** |
| TC-07 | FR4 / NFR4 | Cold-start fallback for a new student | Introductory resources for each course in order, labelled 'Getting started'; not empty, no ML scores | 4 of 4 checks passed | **Pass** |
| TC-08 | FR4 | Model training and comparison with a rule baseline (simulated data) | Rule baseline, Logistic Regression and Random Forest scored on the same split and 5-fold CV; three-row metrics table, confusion matrices, comparison chart, LR coefficients and RF importances and simulation rules saved, all labelled simulated data | 3 of 3 checks passed | **Pass** |
| TC-09 | FR5 | Academic knowledge base | Validation passes; 2 courses, 12 topics, 120 approved questions; every topic has a resource and a topic quiz | 6 of 6 checks passed | **Pass** |
| TC-10 | FR6 | Progress tracking and consistency | Streak, 14-day activity strip and per-topic progress chart shown; logic tests pass | 5 of 5 checks passed | **Pass** |
| TC-11 | FR6 | Reminders and recommendation feedback | Weak-topic and diagnostic reminders shown; Accept and Dismiss change only the status column | 7 of 7 checks passed | **Pass** |
| TC-12 | NFR1 | Usability: core tasks without assistance | Every core task completes at both widths; SUS score above 68 | 3 of 3 checks passed; 1 not run | **Partial** |
| TC-13 | NFR2 | Response times | p95 within target: quiz submit ≤ 2 s (browser), dashboard load ≤ 3 s, background recommendation update ≤ 5 s | 4 of 4 checks passed | **Pass** |
| TC-14 | NFR3 | Security: row-level security | A student gets zero rows of another student's data, cannot read questions, cannot write scores or answers, and can change only the status of their own recommendations | 7 of 7 checks passed | **Pass** |
| TC-15 | NFR4 | Reliability: predictable behaviour with limited data | Cold-start list instead of an error or empty result, including when the model files are missing | 6 of 6 checks passed | **Pass** |
| TC-16 | NFR5 | Portability: add a course without code changes | The new course validates and loads with no code change | 3 of 3 checks passed | **Pass** |

Notes

- TC-12 is partial by design: the automated walkthrough shows the core tasks complete without assistance, but the SUS questionnaire with student participants (Section 3.14.3) was not run for this demo and is future work.
- TC-08 metrics come from simulated students, not real students (simulated data).
- TC-13 targets were set for this test; see docs/performance.md for all samples and caveats.

## Details

### TC-01 · FR1 · Register and create a profile

**Steps**

1. Open /signup and create an account
2. Fill in department, level and learning preferences
3. Check the profiles table

**Expected:** Account created without email confirmation; onboarding saves department, level and preferences to the student's own profile row

**Actual:** 3 of 3 checks passed. **Result: Pass**

```
    PASS  sign up lands on onboarding  (http://localhost:5173/onboarding)
    PASS  onboarding saves, opens the dashboard, and the course list loads
    PASS  profiles: name, department, level and preferences saved  (Phase Three Student, Computer Science, 500, ['reading', 'practice'])
```

### TC-02 · FR1 · Sign in, protected pages, sign out, update profile

**Steps**

1. Visit /, /courses and /log signed out
2. Sign in as New Student
3. Sign out
4. Update own department and level through the API

**Expected:** Signed-out visits redirect to /login; sign-in lands on the dashboard; a student can update their own profile but not is_simulated

**Actual:** 8 of 8 checks passed. **Result: Pass**

```
    PASS  signed-out visit to / redirects to /login
    PASS  signed-out visit to /courses redirects to /login
    PASS  signed-out visit to /log redirects to /login
    PASS  New Student signs in and lands on the dashboard
    PASS  sign out returns to /login
    PASS  A reads B's profile  (0 rows)
    PASS  A sets is_simulated on own profile  (refused: 42501 permission denied for table profiles)
    PASS  A updates own department and level  (1 row(s))
```

### TC-03 · FR2 · Diagnostic quiz with per-topic results

**Steps**

1. New student takes the CSC 531 diagnostic (18 questions)
2. Submit
3. Open the results page

**Expected:** Three questions from every topic; graded server-side; results show a score per topic and each answer with explanation

**Actual:** 5 of 5 checks passed. **Result: Pass**

```
    PASS  results show a score per topic  (6 topic rows)
    PASS  results show each question with its correct answer and explanation  (18 questions, 18 explanations)
    PASS  quiz_attempts: one completed diagnostic attempt with a score  (1 attempt(s), score 22.22)
    PASS  attempt_answers: 18 graded answers across all 6 topics  (18 answers, 6 topics)
    PASS  pytest: diagnostic covers every topic and scores each one (18 passed in 28.96s)
```

### TC-04 · FR2 · Topic quiz grading and question selection

**Steps**

1. Run pytest scripts (signed-in students against the live database)

**Expected:** All four formats graded correctly (partial multi-select is wrong); unseen questions first; a submitted attempt cannot be resubmitted; latest score per topic is correct

**Actual:** 3 of 3 checks passed. **Result: Pass**

```
    PASS  pytest scripts: 18 passed in 28.96s
    PASS  start_quiz returns no correct_answer or explanation  (4 questions, keys: ['format', 'id', 'options', 'stem', 'topic_id'])
    PASS  B submits own completed attempt again  (refused: P0001 attempt already submitted)
```

### TC-05 · FR3 · Log a study session

**Steps**

1. Open Log study, choose a topic, 30 min, Reading, Save
2. Check the study_logs table
3. Try to log a session as another student

**Expected:** Session saved with topic, duration and activity type; logging for someone else is refused

**Actual:** 3 of 3 checks passed. **Result: Pass**

```
    PASS  study logger saves a 30-minute session
    PASS  study_logs: one 30-minute reading session  (1 log(s))
    PASS  A logs a study session as B  (refused: 42501 new row violates row-level security policy for table "study_logs")
```

### TC-06 · FR4 · ML recommendations rank weak topics first

**Steps**

1. Sign in as Active Student (weak: Cognitive Psychology, Fuzzy Logic)
2. POST /recommend with the student's token
3. Read the recommendations

**Expected:** Top 3 overall from the models; the two weak topics ranked 1 and 2; re-running does not duplicate pending recommendations

**Actual:** 4 of 4 checks passed. **Result: Pass**

```
    PASS  every recommendation comes from the models  (model v1)
    PASS  top 3 overall across both courses  (3 recommendation(s))
    PASS  both weak topics ranked first and second  (Cognitive Psychology and Perception, Fuzzy Logic Systems)
    PASS  same number of pending recommendations after a second run  (3)
```

### TC-07 · FR4 / NFR4 · Cold-start fallback for a new student

**Steps**

1. Sign in as New Student (no quiz attempts or study logs)
2. POST /recommend
3. Open the dashboard

**Expected:** Introductory resources for each course in order, labelled 'Getting started'; not empty, no ML scores

**Actual:** 4 of 4 checks passed. **Result: Pass**

```
    PASS  every recommendation is cold start  (6 recommendation(s))
    PASS  one introductory list per course
    PASS  every recommendation is 'Getting started'  (6 items)
    PASS  introductory list is the first three lectures of each course
```

### TC-08 · FR4 · Model training and comparison with a rule baseline (simulated data)

**Steps**

1. python scripts/seed_demo.py (writes simulation_rules.md)
2. cd ml && python -m training.train
3. Inspect ml/results/

**Expected:** Rule baseline, Logistic Regression and Random Forest scored on the same split and 5-fold CV; three-row metrics table, confusion matrices, comparison chart, LR coefficients and RF importances and simulation rules saved, all labelled simulated data

**Actual:** 3 of 3 checks passed. **Result: Pass**

```
    PASS  metrics table compares the rule baseline with both models
    PASS  ml/results holds the three-row metrics table, the charts and simulation_rules.md  (9 files)
    INFO  5-fold CV | Rule baseline (last score < 50%) | 0.684 ± 0.023 | 0.488 ± 0.037 | 0.541 ± 0.047 | 0.512 ± 0.031 |
    INFO  5-fold CV | Logistic Regression | 0.770 ± 0.009 | 0.678 ± 0.029 | 0.476 ± 0.029 | 0.559 ± 0.021 |
    INFO  5-fold CV | Random Forest | 0.752 ± 0.011 | 0.633 ± 0.020 | 0.452 ± 0.035 | 0.527 ± 0.029 |
    PASS  pytest ml (features, simulator, cold start, ranking): 26 passed in 2.12s
```

### TC-09 · FR5 · Academic knowledge base

**Steps**

1. python content/validate.py
2. Count courses, topics, approved questions, resources and quizzes in Supabase

**Expected:** Validation passes; 2 courses, 12 topics, 120 approved questions; every topic has a resource and a topic quiz

**Actual:** 6 of 6 checks passed. **Result: Pass**

```
    PASS  validate.py: 0 error(s)
    PASS  2 courses loaded (CSC 531, CSC 574)
    PASS  12 topics
    PASS  120 approved questions
    PASS  every topic has at least one resource
    PASS  every topic has a topic quiz; 2 diagnostic quizzes
```

### TC-10 · FR6 · Progress tracking and consistency

**Steps**

1. Sign in as Active Student and open the dashboard
2. Run npm test (streak and strip logic)

**Expected:** Streak, 14-day activity strip and per-topic progress chart shown; logic tests pass

**Actual:** 5 of 5 checks passed. **Result: Pass**

```
    PASS  dashboard shows a streak  (2-day streak)
    PASS  14-day activity strip  (7 active days)
    PASS  progress chart has a bar per topic  (6 bars)
    PASS  no streak yet
    PASS  npm test: Tests  13 passed (13)
```

### TC-11 · FR6 · Reminders and recommendation feedback

**Steps**

1. Open the dashboard as Active Student and as New Student
2. Press Accept and Dismiss
3. Run npm test (reminder rules)

**Expected:** Weak-topic and diagnostic reminders shown; Accept and Dismiss change only the status column

**Actual:** 7 of 7 checks passed. **Result: Pass**

```
    PASS  the third says 'Keep it up' with a suggestion
    PASS  at least one reminder  (Cognitive Psychology and Perception scored 40% and you haven't studied it yet.)
    PASS  new student is reminded to take a diagnostic
    PASS  Accept sets status to accepted  (HCI, Interactive Systems and Usability)
    PASS  Dismiss sets status to dismissed and hides it  (Understanding the Problem Space and User-Centred Design)
    PASS  A changes priority_score of own recommendation  (refused: 42501 permission denied for table recommendations)
    PASS  A accepts own recommendation  (1 row(s))
```

### TC-12 · NFR1 · Usability: core tasks without assistance

**Steps**

1. Complete registration, a quiz, a study log and reading a recommendation at laptop and phone width (automated walkthrough)
2. SUS questionnaire with student participants (Section 3.14.3)

**Expected:** Every core task completes at both widths; SUS score above 68

**Actual:** 3 of 3 checks passed; 1 not run. **Result: Partial**

```
    PASS  core tasks at laptop width: 10/10 checks passed
    PASS  core tasks at phone width (390 px): 10/10 checks passed
    PASS  reading recommendations at phone width: 14/14 checks passed
    NOT RUN  SUS questionnaire with student participants (out of scope for this demo; future work)
```

### TC-13 · NFR2 · Response times

**Steps**

1. python scripts/measure_performance.py --runs 10

**Expected:** p95 within target: quiz submit ≤ 2 s (browser), dashboard load ≤ 3 s, background recommendation update ≤ 5 s

**Actual:** 4 of 4 checks passed. **Result: Pass**

```
    PASS  quiz_submit_api: median 0.22 s, p95 0.27 s, target 1.0 s (10 runs, 2026-10-19 17:11)
    PASS  quiz_submit_ui: median 0.33 s, p95 0.83 s, target 2.0 s (10 runs, 2026-10-19 17:11)
    PASS  dashboard_load_ui: median 1.35 s, p95 1.38 s, target 3.0 s (10 runs, 2026-10-19 17:11)
    PASS  recommend_api: median 2.28 s, p95 4.49 s, target 5.0 s (10 runs, 2026-10-19 17:11)
```

### TC-14 · NFR3 · Security: row-level security

**Steps**

1. python scripts/rls_check.py (two students with the anon key)

**Expected:** A student gets zero rows of another student's data, cannot read questions, cannot write scores or answers, and can change only the status of their own recommendations

**Actual:** 7 of 7 checks passed. **Result: Pass**

```
    PASS  rls_check.py: 33/33 checks passed
    PASS  A reads B's study logs  (0 rows)
    PASS  A reads B's quiz attempts  (0 rows)
    PASS  A reads B's recommendations  (0 rows)
    PASS  A selects from questions  (refused: 42501 permission denied for table questions)
    PASS  B selects from questions (after taking a quiz)  (refused: 42501 permission denied for table questions)
    PASS  A inserts a quiz attempt with a made-up score  (refused: 42501 permission denied for table quiz_attempts)
```

### TC-15 · NFR4 · Reliability: predictable behaviour with limited data

**Steps**

1. Unit tests: below the threshold and with no model files
2. New Student via /recommend

**Expected:** Cold-start list instead of an error or empty result, including when the model files are missing

**Actual:** 6 of 6 checks passed. **Result: Pass**

```
    PASS  unit test test_below_threshold_gets_introductory_resources_in_order
    PASS  unit test test_missing_model_files_means_cold_start_even_with_history
    PASS  unit test test_at_threshold_ranks_topics_by_averaged_probability
    PASS  unit test test_cold_start_skips_resources_already_accepted_or_dismissed
    PASS  unit test test_top_three_are_chosen_across_courses_and_cold_start_lists_are_kept
    PASS  every recommendation is cold start  (6 recommendation(s))
```

### TC-16 · NFR5 · Portability: add a course without code changes

**Steps**

1. Write a third course as JSON files only
2. Run validate.py and load.py on it
3. Remove it

**Expected:** The new course validates and loads with no code change

**Actual:** 3 of 3 checks passed. **Result: Pass**

```
    PASS  validate.py accepts a new course: 0 error(s)
    PASS  load.py loads it with no code change: TST 999: 5 topics, 50 questions, diagnostic of 15
    PASS  test course removed afterwards
```
