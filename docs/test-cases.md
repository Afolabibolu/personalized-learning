# Test cases (Chapter Four)

Run 2026-10-26 23:49 with `python scripts/run_test_cases.py`. One or more cases per functional (FR1–FR6) and non-functional (NFR1–NFR5) requirement from Chapter Three, including the cold-start case (Section 3.14). Every case was run against the live system; the evidence lines are the actual output.

**Summary:** 23 pass, 1 partial, 0 fail.

| ID | Requirement | Test | Expected result | Actual result | Pass/Fail |
| --- | --- | --- | --- | --- | --- |
| TC-01 | FR1 | Register and create a profile | Account created without email confirmation; onboarding saves department, level and preferences to the student's own profile row | 3 of 3 checks passed | **Pass** |
| TC-02 | FR1 | Sign in, protected pages, sign out, update profile | Signed-out visits redirect to /login; sign-in lands on the dashboard; a student can update their own profile but not is_simulated | 8 of 8 checks passed | **Pass** |
| TC-03 | FR2 | Diagnostic quiz with per-topic results | Three questions from every topic; graded server-side; results show a score per topic and each answer with explanation | 5 of 5 checks passed | **Pass** |
| TC-04 | FR2 | Topic quiz grading and question selection | All four formats graded correctly (partial multi-select is wrong); unseen questions first; a submitted attempt cannot be resubmitted; latest score per topic is correct | 3 of 3 checks passed | **Pass** |
| TC-05 | FR3 | Log a study session | Session saved with topic, duration and activity type; logging for someone else is refused | 3 of 3 checks passed | **Pass** |
| TC-06 | FR4 | ML recommendations rank weak topics first | Top 3 overall from the models; the two weak topics ranked 1 and 2; re-running does not duplicate pending recommendations | 4 of 4 checks passed | **Pass** |
| TC-07 | FR4 / NFR4 | Cold-start fallback for a new student | For each course: topic 1's study note and lecture, then topic 2's note, labelled 'Getting started'; not empty, no ML scores | 4 of 4 checks passed | **Pass** |
| TC-08 | FR4 | Model training and comparison with a rule baseline | Rule baseline, Logistic Regression and Random Forest scored on the same split and 5-fold CV; three-row metrics table, confusion matrices, comparison chart, LR coefficients and RF importances and simulation rules saved, all labelled simulated data | 3 of 3 checks passed | **Pass** |
| TC-09 | FR5 | Academic knowledge base | Validation passes; the reviewed courses have 12 topics and 120 approved questions; every topic in every course has a resource and a topic quiz | 6 of 6 checks passed | **Pass** |
| TC-10 | FR6 | Progress tracking and consistency | Streak, 14-day activity strip and per-topic progress chart shown; logic tests pass | 5 of 5 checks passed | **Pass** |
| TC-11 | FR6 | Reminders and recommendation feedback | Weak-topic and diagnostic reminders shown; Accept and Dismiss change only the status column | 7 of 7 checks passed | **Pass** |
| TC-12 | NFR1 | Usability: core tasks without assistance | Every core task completes at both widths; SUS score above 68 | 3 of 3 checks passed; 1 not run | **Partial** |
| TC-13 | NFR2 | Response times | p95 within target: quiz submit ≤ 2 s (browser), dashboard load ≤ 3 s, background recommendation update ≤ 5 s | 4 of 4 checks passed | **Pass** |
| TC-14 | NFR3 | Security: row-level security | A student gets zero rows of another student's data, cannot read questions, cannot write scores or answers, and can change only the status of their own recommendations | 7 of 7 checks passed | **Pass** |
| TC-15 | NFR4 | Reliability: predictable behaviour with limited data | Cold-start list instead of an error or empty result, including when the model files are missing | 11 of 11 checks passed | **Pass** |
| TC-16 | NFR5 | Portability: add a course without code changes | The new course validates and loads with no code change | 3 of 3 checks passed | **Pass** |
| TC-17 | FR1 | Profile page, realistic demo names and learning preferences | Name, department, level and preferred resource types saved; recommendations that use the preferred type say 'Matched to your preference'; profile edits confirmed | 6 of 6 checks passed | **Pass** |
| TC-18 | FR2 / FR3 | Score change, quiz history, custom minutes and study timer | First attempt says so; second shows the change since last time; course page lists the quiz history; 400 rejected, 45 accepted; timer fills in the duration | 8 of 8 checks passed | **Pass** |
| TC-19 | FR4 | Explained recommendations, accept and history | Every item has a reason from the features; 'Why this?' shows both probabilities, the average and the top factors; accepted items open the resource and move to History; a quiet notice when the ML service is down | 10 of 10 checks passed | **Pass** |
| TC-20 | FR5 | Knowledge Base: notes, past questions and lecture links | Live counts, topics with summaries, resources grouped by type, search as you type; notes and past questions render in the app; lectures open in a new tab; every topic has a note, a lecture and a quiz | 11 of 11 checks passed | **Pass** |
| TC-21 | FR6 | Notifications, reminders and weekly summary | Unread count; clicking marks read and follows the link; weekly summary and two-line chart labels; settings saved; each reminder kind fires at most once a day and stays private | 11 of 11 checks passed | **Pass** |
| TC-22 | NFR5 | Course ingestion pipeline: raw files to the app | Every sample course validates and loads as is_reviewed = false; it appears in the Knowledge Base with the sample badge, its study note, past questions and topic quiz work, it gets its own getting-started list, and the demo accounts are unchanged | 22 of 22 checks passed | **Pass** |
| TC-23 | FR4 / FR5 | Videos and textbooks in the recommendations | Each ML recommendation also suggests the topic's video and textbook; every video is a YouTube link that still exists; textbooks open as reading cards; courses with no past papers show labelled exam-style questions | 10 of 10 checks passed | **Pass** |
| TC-24 | NFR5 | Course requests (scalability) | The request shows as pending, the admin script lists it and adds it, and the student sees it added, is notified and has the course in their courses; the form fits a phone | 7 of 7 checks passed | **Pass** |

Notes

- TC-12 is partial by design: the automated walkthrough shows the core tasks complete without assistance, but the SUS questionnaire with student participants (Section 3.14.3) was not run for this demo and is future work.
- TC-08 metrics come from the simulated students described in `ml/results/simulation_rules.md`, not from real students.
- TC-13 targets were set for this test; see docs/results/performance.md for all samples and caveats.
- First Phase 8 run (19 Oct 2026): 18 pass, 1 partial, 2 fail. TC-02 failed because the test still looked for a Sign out button in the top bar, which Phase 7 moved into the profile menu. TC-16 failed because its test course used the old file layout (resources inside the course file, no study notes). Both were faults in the test script, not the app; the script was updated and every case was run again.
- First Phase 9 run (24 Oct 2026): 20 pass, 2 fail. TC-10 and TC-12 failed on 'dashboard shows a streak' (0-day streak) because the demo accounts had last been reset on 19 October, so the seeded study days were no longer consecutive up to today. After `python scripts/seed_demo.py --demo-only` the streak check passed, and every case was run again for the table above. Reset the demo accounts on the day of the demo.

- Runs on 25 Oct 2026 (12 courses): one run had TC-10 fail because npm was not on the PATH of the shell running this script (not an app fault). A later run had TC-17 and TC-18 fail with no check output, and TC-22 fail on Kemi's dashboard: `seed_demo.py --demo-only` leaves no recommendations, and phase9_check.py relied on an earlier check having refreshed them, so it now presses Refresh first. The TC-17/TC-18 crash did not happen again in the full phase7 run or in the rerun of every case for the table above. Later the same day `timing.py` failed for the same reason (no saved recommendations after a reset); it now refreshes them once before the timed dashboard loads. One run had TC-24 with no check output (phase10_check.py stopped before its course-request section, cause not found; it passed in every later run, and a crash in either section is now reported as a failed check with the error).

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
    PASS  profiles: name, department, level and preferences saved  (Phase Three Student, Computer Science, 500, ['note', 'past_questions'])
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
    PASS  pytest: diagnostic covers every topic and scores each one (25 passed in 46.47s)
```

### TC-04 · FR2 · Topic quiz grading and question selection

**Steps**

1. Run pytest scripts (signed-in students against the live database)

**Expected:** All four formats graded correctly (partial multi-select is wrong); unseen questions first; a submitted attempt cannot be resubmitted; latest score per topic is correct

**Actual:** 3 of 3 checks passed. **Result: Pass**

```
    PASS  pytest scripts: 25 passed in 46.47s
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

**Expected:** For each course: topic 1's study note and lecture, then topic 2's note, labelled 'Getting started'; not empty, no ML scores

**Actual:** 4 of 4 checks passed. **Result: Pass**

```
    PASS  every recommendation is cold start  (6 recommendation(s))
    PASS  one introductory list per course
    PASS  every recommendation is 'Getting started'  (6 items)
    PASS  introductory list: topic 1's note and lecture, then topic 2's note, for each course  (6 items)
```

### TC-08 · FR4 · Model training and comparison with a rule baseline

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
    PASS  pytest ml (features, simulator, cold start, ranking): 45 passed in 2.00s
```

### TC-09 · FR5 · Academic knowledge base

**Steps**

1. python content/validate.py
2. Count courses, topics, approved questions, resources and quizzes in Supabase

**Expected:** Validation passes; the reviewed courses have 12 topics and 120 approved questions; every topic in every course has a resource and a topic quiz

**Actual:** 6 of 6 checks passed. **Result: Pass**

```
    PASS  validate.py: 0 error(s)
    PASS  reviewed courses: CSC 531, CSC 574
    PASS  12 topics in the reviewed courses
    PASS  120 approved questions in the reviewed courses
    INFO  15 sample courses from the ingestion pipeline: COS 102, CSC 412, CSC 421, CSC 431, CSC 472, CSC 475, CSC 476, CSC 551, CSC 552, CSC 554, CSC 572, CSC 582, CSC 583, CSC 584, GES 103
    PASS  every topic (103) has at least one resource
    PASS  every topic has a topic quiz; 17 diagnostic quizzes for 17 courses
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
    PASS  the third says 'Keep it up' with a suggestion  (Scoring 100%. Try the topic quiz: questions you haven't seen come first.)
    PASS  at least one reminder  (Cognitive Psychology and Perception scored 40% and you haven't studied it yet.)
    PASS  new student is reminded to take a diagnostic
    PASS  Accept sets status to accepted and opens the resource  (HCI, Interactive Systems and Usability)
    PASS  Dismiss sets status to dismissed and moves it to History  (HCI, Interactive Systems and Usability)
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

1. python scripts/timing.py --runs 20

**Expected:** p95 within target: quiz submit ≤ 2 s (browser), dashboard load ≤ 3 s, background recommendation update ≤ 5 s

**Actual:** 4 of 4 checks passed. **Result: Pass**

```
    PASS  quiz_submit_api: median 0.19 s, p95 0.22 s, target 1.0 s (20 runs, 2026-10-26 23:35)
    PASS  quiz_submit_ui: median 0.33 s, p95 0.35 s, target 2.0 s (20 runs, 2026-10-26 23:35)
    PASS  dashboard_load_ui: median 0.84 s, p95 0.88 s, target 3.0 s (20 runs, 2026-10-26 23:35)
    PASS  recommend_api: median 2.90 s, p95 3.04 s, target 5.0 s (20 runs, 2026-10-26 23:35)
```

### TC-14 · NFR3 · Security: row-level security

**Steps**

1. python scripts/rls_check.py (two students with the anon key)

**Expected:** A student gets zero rows of another student's data, cannot read questions, cannot write scores or answers, and can change only the status of their own recommendations

**Actual:** 7 of 7 checks passed. **Result: Pass**

```
    PASS  rls_check.py: 52/52 checks passed
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

**Actual:** 11 of 11 checks passed. **Result: Pass**

```
    PASS  unit test test_cold_start_rows_explain_why_and_have_no_probabilities
    PASS  unit test test_a_failing_model_falls_back_to_cold_start_instead_of_an_error
    PASS  unit test test_corrupt_model_files_mean_cold_start
    PASS  unit test test_cold_start_runs_send_nothing
    PASS  unit test test_below_threshold_gets_introductory_resources_in_order
    PASS  unit test test_missing_model_files_means_cold_start_even_with_history
    PASS  unit test test_at_threshold_ranks_topics_by_averaged_probability
    PASS  unit test test_cold_start_skips_resources_already_accepted_or_dismissed
    PASS  unit test test_top_three_are_chosen_across_courses_and_cold_start_lists_are_kept
    PASS  unit test test_cold_start_items_also_suggest_a_video_and_textbook
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

### TC-17 · FR1 · Profile page, realistic demo names and learning preferences

**Steps**

1. Sign up and onboard a new student
2. Open the dashboard as Tolu Adeyemi
3. Edit department and level on /profile

**Expected:** Name, department, level and preferred resource types saved; recommendations that use the preferred type say 'Matched to your preference'; profile edits confirmed

**Actual:** 6 of 6 checks passed. **Result: Pass**

```
    PASS  sign up and onboarding save name, department, level and study preferences  ({'full_name': 'Ada Okoro', 'department': 'Computer Science', 'level': 500, 'learning_preferences': ['note', 'video']})
    PASS  demo account has a realistic name  (Tolu Adeyemi)
    PASS  recommendations that matched the preference say so  (✓
    PASS  Profile page edits are saved with a confirmation  ({'department': 'Computer Science (Data Science option)', 'level': 400, 'learning_preferences': ['note', 'past_questions', 'video']})
    PASS  cold-start demo account is Kemi Balogun
    PASS  phone width: Profile page fits
```

### TC-18 · FR2 / FR3 · Score change, quiz history, custom minutes and study timer

**Steps**

1. Take the same topic quiz twice
2. Open the course page
3. Log study with 400, then 45 custom minutes, then with the timer

**Expected:** First attempt says so; second shows the change since last time; course page lists the quiz history; 400 rejected, 45 accepted; timer fills in the duration

**Actual:** 8 of 8 checks passed. **Result: Pass**

```
    PASS  results: first attempt on a topic says so
    PASS  results: change since the last attempt, e.g. '40% to 70%, up 30 points'  (0% to 0%, no change)
    PASS  'Custom (minutes)' is labelled and rejects 400
    PASS  'Custom (minutes)' accepts 45
    PASS  study timer: start, pause, stop fills in the duration  (stopped at 00:01, duration 1 min)
    PASS  after saving: confirmation, and recommendations refresh in the background
    PASS  course page: quiz history with date, quiz and score  (22 Oct 2026 Cognitive Psychology and Perception quiz 40% · Needs attention)
    PASS  phone width: logger with timer fits
```

### TC-19 · FR4 · Explained recommendations, accept and history

**Steps**

1. Open the dashboard as Tolu
2. Open 'Why this?'
3. Accept and Dismiss items
4. Block the ML service and log a session

**Expected:** Every item has a reason from the features; 'Why this?' shows both probabilities, the average and the top factors; accepted items open the resource and move to History; a quiet notice when the ML service is down

**Actual:** 10 of 10 checks passed. **Result: Pass**

```
    PASS  a reason line on every recommendation  (Last score 40%. Not studied yet. 0 minutes studied in total.)
    PASS  reason built from the features
    PASS  'Why this?' shows both model probabilities, their average and the factors  (92% | 85% | 89% | Average score: 20%)
    PASS  'Keep it up' item says why
    PASS  cold-start items look different, with the personalise line
    PASS  Accept opens a study note inside the app  (HCI, Interactive Systems and Usability)
    PASS  Accept opens lecture slides in a new tab  (https://drive.google.com/file/d/1-PORIEFbqnm4Hco1wyvZdOhVWWo)
    PASS  accepted and dismissed items leave the list and appear under History
    PASS  ML service down: quiet notice, saved recommendations still shown  (Recommendations will update shortly. Showing your last saved list.)
    PASS  phone width: reason and 'Why this?' fit without sideways scroll
```

### TC-20 · FR5 · Knowledge Base: notes, past questions and lecture links

**Steps**

1. Open Knowledge Base
2. Search 'fuzzy'
3. Open a study note, a past-questions page and a lecture link
4. Open a topic page

**Expected:** Live counts, topics with summaries, resources grouped by type, search as you type; notes and past questions render in the app; lectures open in a new tab; every topic has a note, a lecture and a quiz

**Actual:** 11 of 11 checks passed. **Result: Pass**

```
    PASS  Knowledge Base page in the nav with live counts  (17 courses 103 topics 409 resources 848 practice questions)
    PASS  courses, then topics in order with summaries and subtopics  (103 topics; first: HCI, Interactive Systems and Usability)
    PASS  resources grouped by type  (Study notes, Lecture slides, Past questions)
    PASS  search filters topics as you type  ('fuzzy' -> 1 topic(s))
    PASS  empty search shows a clear next step
    PASS  study note opens inside the app, rendered from Markdown  (sections ['What the topic is', 'Subtopics', 'Key terms', 'Exam-style point']; 'Source: Lecture 6')
    PASS  past questions open inside the app, grouped by year (tables rendered)  (4 papers, 2 table(s))
    PASS  lecture links open in a new tab, folders labelled 'Open lecture folder'
    PASS  topic page: summary, subtopics, resources by type, quiz and log buttons
    PASS  every topic has a study note and a topic quiz (and a lecture link in reviewed courses)  (103 of 103)
    PASS  phone width (375 px): menu button opens the nav; no sideways scroll
```

### TC-21 · FR6 · Notifications, reminders and weekly summary

**Steps**

1. Open the bell as Tolu
2. Click a notification
3. Check the weekly summary and progress chart
4. Save reminder settings
5. pytest scripts/test_reminders.py

**Expected:** Unread count; clicking marks read and follows the link; weekly summary and two-line chart labels; settings saved; each reminder kind fires at most once a day and stays private

**Actual:** 11 of 11 checks passed. **Result: Pass**

```
    PASS  lecture links open in a new tab, folders labelled 'Open lecture folder'
    PASS  bell in the nav with an unread count  (3 unread; kinds: daily_goal_reached, new_recommendations, score_improved, streak_at_risk, weak_topic_unstudied)
    PASS  bell opens a list of reminders and feedback, each with a time  (5 shown)
    PASS  clicking a notification marks it read and follows its link  (3 -> 2 unread, now at /log)
    PASS  full notifications page
    PASS  weekly summary: minutes vs last week, topics improved, next focus  (THIS WEEK 825 min ▲ 330 min vs last week (495 min) | TOPICS IMPROVED Knowledge Representation and Reasoning 80% → 100% Fuzzy Logic Systems 20% → 40% and 1 more )
    PASS  progress chart: long names on two lines, full name on hover  (6 wrapped)
    PASS  reminder settings saved on the profile  ({'study_days': ['mon', 'tue', 'wed', 'thu', 'fri', 'sat'], 'preferred_study_time': '17:30:00', 'daily_goal_minutes': 45})
    PASS  phone width: bell stays visible and its list fits
    PASS  'Custom (minutes)' is labelled and rejects 400
    PASS  pytest test_reminders.py: 6 passed in 19.43s
```

### TC-22 · NFR5 · Course ingestion pipeline: raw files to the app

**Steps**

1. python content/ingest/inventory.py
2. python content/ingest/extract.py --course "CSC 551"
3. Write the course files from the extracted text, then python content/ingest/publish.py --course "CSC 551"
4. In Chrome: pick the course at onboarding, open it in the Knowledge Base, take a topic quiz, remove it again

**Expected:** Every sample course validates and loads as is_reviewed = false; it appears in the Knowledge Base with the sample badge, its study note, past questions and topic quiz work, it gets its own getting-started list, and the demo accounts are unchanged

**Actual:** 22 of 22 checks passed. **Result: Pass**

```
    PASS  inventory.py finds the courses in sources/raw/ and writes inventory.csv  (114 files, 17 courses: COS 102, CSC 412, CSC 421, CSC 431, CSC 472, CSC 475, CSC 476, CSC 531, CSC 551, CSC 552, CSC 554, CSC 572, CSC 574, CSC 582, CSC 583, CSC 584, GES 103)
    PASS  extract.py extracts CSC 551 and marks scanned PDFs  (5 files: scanned, text)
    PASS  validate.py passes for every sample course  (15 sample courses)
    PASS  every sample course is loaded with is_reviewed = false  (15 of 15)
    PASS  each topic has a study note, a topic quiz and at least 8 practice questions  (91 topics)
    PASS  the reviewed courses are unchanged
    PASS  onboarding lists every course, with the two reviewed courses ticked and sample courses labelled  (17 courses, 2 ticked)
    PASS  choosing CSC 551 at onboarding enrols the student  (CSC 531, CSC 551, CSC 574)
    PASS  course list shows my courses, then more courses with the sample badge  (17 course cards)
    PASS  more courses are grouped by level, highest first  (500 LEVEL | 400 LEVEL | 200 LEVEL | 100 LEVEL)
    PASS  Knowledge Base shows the sample course with the 'Sample content' badge
    PASS  Knowledge Base: other courses start collapsed; a header, Expand all and Collapse all toggle them
    PASS  'My courses' filter shows only the student's courses  (CSC 531 · Human-Computer Interaction | CSC 551 · Design and Analysis of Algorithms | CSC 574 · Intelligent Systems)
    PASS  a sample course's study note opens in the app  (Source: CSC 551 Design and Analysis of Algorithms.pdf, Study Session 2)
    PASS  its past questions open in the app, grouped by paper  (2024/2025 · B.Sc. Degree Examinations, First Semester (CSC 551: Design and Analysis of Algorithms); 2023/2024 · B.Sc. Degree Examinations, First Semester (CSC 551: Design and Analysis of Algorithms))
    PASS  topic page shows the badge and the topic quiz button
    PASS  a sample course's topic quiz is graded and shows results  (2b6d227a)
    PASS  CSC 551 gets its own getting-started list (fewer than 3 attempts)  (Study note: Algorithm Fundamentals and Analysis; Past questions: Algorithm Fundamentals and Analysis; Study note: Divide and Conquer)
    PASS  progress chart: a course dropdown lists only my courses and switches the chart  (CSC 531 · Human-Computer Interaction | CSC 551 · Design and Analysis of Algorithms | CSC 574 · Intelligent Systems)
    PASS  a course can be removed from my courses
    PASS  phone width: course list with more courses fits
    PASS  Kemi's dashboard is unchanged: six getting-started items for CSC 531 and CSC 574  (6 items)
```

### TC-23 · FR4 / FR5 · Videos and textbooks in the recommendations

**Steps**

1. Sign in as Active Student and refresh recommendations
2. Open a recommendation's video and textbook
3. Open a topic page
4. Search the Knowledge Base for a course with no past papers

**Expected:** Each ML recommendation also suggests the topic's video and textbook; every video is a YouTube link that still exists; textbooks open as reading cards; courses with no past papers show labelled exam-style questions

**Actual:** 10 of 10 checks passed. **Result: Pass**

```
    PASS  every topic has a recommended textbook card  (103 topics)
    PASS  every video is a YouTube link that oEmbed confirms exists  (101 videos for 103 topics)
    PASS  exam-style and review-question sets are labelled as not from a past paper  (18 sets in CSC 421, CSC 475, GES 103)
    PASS  CSC 572 has 7 topics, including Decision Trees and Random Forests  (7 topics)
    PASS  each ML recommendation also suggests a video and a textbook for its topic  (3 of 3 cards)
    PASS  the video opens on YouTube in a new tab
    PASS  the textbook opens as a reading card: what to read and why  (What to read for Cognitive Psychology and Perception; Why this book)
    PASS  the topic page lists videos and recommended textbooks
    PASS  a course with no past papers shows 'Exam-style questions', not 'Past questions'
    PASS  a course book's own review questions show as 'Review questions', not 'Past questions'
```

### TC-24 · NFR5 · Course requests (scalability)

**Steps**

1. As a new student, open Courses, then Request a course, and send the form
2. python scripts/course_requests.py, then add <id> --course "CSC 412"
3. Reload the request page, notifications and Courses

**Expected:** The request shows as pending, the admin script lists it and adds it, and the student sees it added, is notified and has the course in their courses; the form fits a phone

**Actual:** 7 of 7 checks passed. **Result: Pass**

```
    PASS  a student can request a missing course from the Courses page; it shows as pending  (CSC 412 · Microprocessor Interfacing Pending Sent 26 Oct 2026 · 400 level · first semester)
    PASS  scripts/course_requests.py lists the pending request  (fd017818  pending   2026-10-26  CSC 412 · Microprocessor Interfacing  (Request Tester))
    PASS  adding it enrols the student and notifies them  (Added: CSC 412 · Microprocessor Interfacing is now in the student's courses, and they have been notified.)
    PASS  the student sees the request as added, with a link to the course
    PASS  the student gets a 'course is ready' notification
    PASS  the course is now in the student's courses  (CSC 412, CSC 531, CSC 574)
    PASS  phone width: the request form fits
```
