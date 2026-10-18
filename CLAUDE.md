# Personalized Academic Recommendation and Learning Support System

Final-year Computer Science project, University of Ibadan. Author: Afolabi Boluwatife David (230881). Supervisor: Dr. Angela Makolo.

The system helps undergraduates find their weak topics before an exam result tells them. Students take quizzes and log study sessions. A Python service classifies each topic as "requires attention" or "adequately mastered" and recommends resources for the weakest ones. New students with too little data get an introductory sequence instead (the cold-start fallback).

The source of truth for requirements is the report, Chapters 1 to 3 (FR1 to FR6, NFR1 to NFR5).

## Goal and deadline

I present a working version to my supervisor on Tuesday for my results defence, and I have two days to build it. The goal is a demo that runs end to end on my laptop and gives me clear screenshots and a results table. It does not need deployment, a pilot or a usability survey.

Priorities when time is short, in order:

1. The full student journey works: sign up, onboarding, diagnostic quiz, results, study logging, dashboard with recommendations.
2. Cold start and ML recommendations both visibly work, on two demo accounts.
3. The model comparison runs and prints a results table.
4. Visual polish for screenshots.

If something will take long and is not on that list, skip it and note it in the phase report as future work.

## How to work with me

- Work through the phases below in order, one phase at a time.
- Phase 0 is a simple environment setup. Do it straight away with no plan, then show me the result of its check.
- From Phase 1 onward, implement the whole phase without stopping for approval. Write tests for the logic that matters (grading, features, cold start, ranking) and run them as you go. Skip tests for plain UI.
- When a phase is finished, run its check and stop. Then give me a short phase report:
  1. What you built, against the phase checklist.
  2. Test and check results, with the actual output.
  3. How I can try it myself.
  4. Anything you skipped or did differently, and why.
  5. Open questions.
- Do not start the next phase until I tell you to proceed.
- If something not covered here blocks the work, ask me. If it does not block, pick the simplest option that fits this file and list it in the phase report.
- Once I settle a decision, add it to this file.
- Commit at the end of a phase after I approve the report. Keep messages short.

## Stack

| Layer | Tools |
| --- | --- |
| Presentation (`web/`) | React, Vite, TypeScript, React Router, TanStack Query, supabase-js, Tailwind, Recharts |
| Application and data (`supabase/`) | Supabase: Postgres, Auth, row-level security, SQL functions |
| Machine learning (`ml/`) | Python, FastAPI, scikit-learn, pandas, joblib, matplotlib, pytest |
| Content (`content/`) | Python scripts that validate and load question files. Runs locally only |

Everything runs locally for the demo: Vite dev server, the hosted Supabase project, and the FastAPI service on localhost.

## Repository layout

```
recsys/
  CLAUDE.md
  web/                 React app (FR1, FR2, FR3, FR6)
    src/api/           every Supabase and ML call lives here; screens never touch tables directly
  supabase/
    migrations/        one SQL file per schema change
  ml/
    app/               FastAPI service (FR4)
    training/          features.py, synthetic.py, train.py
    models/            saved models, versioned (lr_v1.joblib, rf_v1.joblib)
    results/           metrics tables and charts for the results chapter
  content/
    sources/           outlines, lecture PDFs and past questions per course (not committed)
    courses/           one JSON file per course: topics and subtopics
    questions/         one JSON file per topic
    validate.py        schema and answer checks
    load.py            loads content into Supabase
  scripts/
    seed_demo.py       creates demo accounts and simulated students
  docs/
    test-cases.md      one row per FR and NFR, for Chapter Four
    screenshots.md     the screenshot checklist
```

## Hard rules

- The web app only holds the Supabase anon key (called the publishable key in newer projects). The service role key (the secret key in newer projects) lives only in `ml/.env`, `content/.env` and `scripts/.env`, and `.env` is in `.gitignore`. Commit `.env.example` files with key names only.
- Every table has row-level security. A student reads and writes only their own profile, attempts, answers, study logs and recommendations. Courses, topics, resources and quizzes are read-only for students.
- Students never touch `questions` directly, and never write scores themselves. Quizzes go through two SQL functions (security definer), and each one checks that `auth.uid()` owns the attempt:
  - `start_quiz(quiz_id)` creates the attempt, picks the questions (unseen first, then the oldest seen), stores their ids on the attempt, and returns the attempt id plus the questions without `correct_answer` or `explanation`.
  - `submit_quiz(attempt_id, responses)` grades only the questions stored on that attempt, writes `attempt_answers`, sets the score and `completed_at`, then returns the correct answers and explanations. A completed attempt cannot be submitted again.
- Students can only change the `status` column of their own recommendations. Enforce this with a column-level grant or a small SQL function, because RLS alone cannot limit columns.
- The ML service verifies the caller by passing their access token to Supabase (`auth.get_user`), not by decoding the JWT itself, and only recomputes recommendations for that user. It allows CORS from the Vite dev server.
- Every schema change is a new migration file. Never edit an applied migration.
- ML features use only data from before the moment being predicted. Never use the score that defines the label as a feature.
- Metrics from simulated students are always labelled "simulated data" in file names, table titles and chart titles. Never present them as results from real students.
- The UI works on a phone first, and also looks clean on a laptop for screenshots.
- Reminders are shown inside the app only. There is no SMS or email service.

## Design decisions

- Ten tables: the report's 8 entities plus `questions` and `attempt_answers`.
- Supabase Auth stores credentials. There is no `password_hash` column.
- Label rule: a topic "requires attention" when the student's next attempt on it scores below 50%. Rows with no next attempt are left out of training. The rule is fixed before any training.
- Model combination: average the predicted probabilities from Logistic Regression and Random Forest, and rank topics by that average.
- Cold-start threshold: fewer than 3 completed quiz attempts on a course means the student gets that course's introductory resources in order. Keep it in one config value. If no trained model file exists yet, every student gets the cold-start path instead of an error.
- Prototype scope: two 500-level courses, CSC 531 (Human-Computer Interaction) and CSC 574 (Intelligent Systems).
- Recommendation trigger: after a quiz is submitted or a study session is logged, the web app calls `POST /recommend` on the ML service without waiting for it. The dashboard also has a "Refresh recommendations" button. No webhooks or scheduled jobs for the demo.
- Training data: simulated students created by `scripts/seed_demo.py`, because there is no time for a pilot. The real-data comparison is future work.

## Database

| Table | Key columns | Students can |
| --- | --- | --- |
| profiles | id (= auth user id), full_name, department, level, learning_preferences, is_simulated | read and update own row (a trigger on `auth.users` creates the row at sign-up) |
| courses | id, code, title | read |
| topics | id, course_id, title, sequence_order | read |
| resources | id, topic_id, title, type, url, is_introductory, intro_order | read |
| quizzes | id, course_id, topic_id (null for diagnostic), kind (diagnostic or topic), question_count | read |
| questions | id, topic_id, format, stem, options, correct_answer, explanation, source, status (draft or approved) | no direct access |
| quiz_attempts | id, student_id, quiz_id, question_ids, score, started_at, completed_at | read own (created and graded only by the quiz functions) |
| attempt_answers | id, attempt_id, question_id, response, is_correct | read own (written only by `submit_quiz`) |
| study_logs | id, student_id, topic_id, duration_minutes, activity_type, logged_at | read and create own |
| recommendations | id, student_id, topic_id, resource_id, rank, priority_score, source (ml or cold_start), model_version, status, created_at | read own, update status only |

Question formats: `single_choice`, `true_false`, `multi_select`, `odd_one_out`.

Question shape (enforced by the schema and by `submit_quiz`): `options` is a list of `{"key", "text"}` with keys `a`, `b`, `c`, ...; true_false uses the keys `true` and `false`. `correct_answer` is always a list of keys: one for single_choice, true_false and odd_one_out (the odd option), two or more for multi_select. An answer is correct when the chosen keys equal the correct keys as a set, so a partial multi_select is wrong. Quiz responses are sent to `submit_quiz` as `{"<question id>": ["<key>", ...]}`.

Grants: new tables and functions give anon and authenticated no access by default (Phase 1 changed Supabase's default privileges). Every migration that adds one grants exactly what students need. anon has no table access at all.

A diagnostic quiz draws a few questions from every topic in a course. Each answer row points to a question, and each question to a topic, so one diagnostic attempt gives a score per topic.

## Build phases

Day 1 covers Phases 0 to 3. Day 2 covers Phases 4 to 6. Phase 2 only writes files until its last step, so it can run in a second Claude Code session at the same time as Phases 1 and 3.

### Phase 0: environment setup

- [x] In the Supabase dashboard, turn off email confirmation for sign-ups (Authentication settings), so demo accounts work without an email server. Tell me to do this; I will click it.
- [x] Supabase project linked with the CLI (`supabase init`, `supabase link`)
- [x] `web/` scaffolded with Vite (React + TypeScript) and Tailwind, with a page that reads one row from a test table
- [x] `ml/` with a virtual environment, FastAPI and `GET /health`
- [x] `.env.example` files and `.gitignore`

Check: the page shows the test row, `/health` returns OK, and `git status` tracks no `.env` file.

### Phase 1: schema and row-level security (FR5, NFR3)

- [x] Migrations for all ten tables, with foreign keys and indexes on student_id and topic_id
- [x] RLS policies for every table, matching the table above
- [x] The `auth.users` trigger that creates a profile row
- [x] `start_quiz` and `submit_quiz` functions, plus the column rule for recommendation status
- [x] `scripts/rls_check.py`: signs in as two test students with the anon key and tries to read and write each other's data

Check: `rls_check.py` shows student A gets zero rows for B's logs, attempts and recommendations, a direct select on `questions` returns nothing, and a direct insert into `quiz_attempts` with a made-up score is refused.

### Phase 2: content and question bank (FR5)

Easy mode: the sources are only each course's outline (or lecture list), topics and subtopics, and past questions. Do not try to extract full lecture content. You write the questions yourself in this session, so no API script is needed. The notes in `content/sources/` are student summaries, so where a note and a lecture slide disagree, follow the slide.

- [x] `content/courses/<code>.json`: the course, 5 or 6 topics in teaching order, and each topic's subtopics, built from the outline and lecture headings. Stop and show me both files before writing any questions.
- [x] `content/questions/<code>/<topic-slug>.json`: 10 questions per topic. Mix all four formats, with no format above half of a topic's questions. Each question has format, stem, options, correct_answer, explanation (one or two sentences) and source (the lecture or past question it is based on). Use the past questions to judge which subtopics matter most and how hard questions should be. Rewrite theory questions into the four objective formats. Never invent facts that are not in the sources.
- [x] `content/validate.py`: checks every file against the schema. single_choice has exactly one correct option, true_false has two options, multi_select has at least two correct options, odd_one_out has exactly one odd option, and there are no duplicate stems within a course. Prints counts per topic and per format.
- [x] `content/load.py`: inserts courses, topics, resources, quizzes (one diagnostic per course, one quiz per topic) and questions with status `approved` for the demo. Running it twice must not create duplicates.
- [x] Resources: the matching lecture PDF or Drive link for each topic. The first lecture of each course is the introductory resource.

This phase may run in a second Claude Code session. That session only touches files inside `content/` and does not commit; the main session commits its work after I approve the report.

Check: `validate.py` passes with zero errors, every topic has 10 questions in at least two formats, and every topic has a resource.

### Phase 3: React core (FR1, FR2, FR3)

- [ ] Sign up and log in with Supabase Auth, with protected routes
- [ ] Onboarding: department, level, learning preferences saved to `profiles`
- [ ] Course list, with "Take diagnostic quiz" on courses not yet started
- [ ] Quiz player: starts with `start_quiz`, one component per format, a progress bar, submits through `submit_quiz`
- [ ] Results: score per topic, then each question with its correct answer and explanation
- [ ] Topic page: resources, "Take topic quiz", "Log study session"
- [ ] Study logger: topic, duration, activity type (reading, video, practice)
- [ ] A consistent, clean visual style across screens, since these become screenshots

Check: a brand-new account can sign up, finish onboarding, take a diagnostic quiz, see per-topic results and log a 30-minute session, and every step lands in the right tables.

### Phase 4: ML service, simulated data and cold start (FR4, NFR4)

- [ ] `scripts/seed_demo.py`, using the service role key. It runs after `load.py`, because simulated answers point to real questions:
  - Create every simulated and demo user through the Supabase admin API (`auth.admin.create_user`), so each one has a real auth user and profile row.
  - About 80 simulated students (`is_simulated = true`) with several weeks of quiz attempts and study logs. Their next scores depend on study time, past scores and days since last studied, plus random noise, so the models have a pattern to learn.
  - Demo account "New Student" with no activity, to show cold start.
  - Demo account "Active Student" with a history that makes one or two topics clearly weak, to show ML recommendations.
  - Prints the demo logins at the end. Running it again resets the simulated data.
- [ ] `training/features.py`: one row per student per topic with mean_score, last_score, attempt_count, session_count, total_minutes, days_since_last_studied
- [ ] Labels from the label rule above
- [ ] `training/train.py`: Logistic Regression (StandardScaler in a pipeline) and Random Forest on the same stratified split, plus 5-fold cross-validation. Saves to `ml/results/`: a metrics table (accuracy, precision, recall, F1) as CSV and Markdown, a confusion matrix chart per model, a bar chart comparing the two, and Random Forest feature importances. All titled "simulated data".
- [ ] `POST /recommend`:
  1. Below the cold-start threshold on a course, write that course's introductory resources in order with source `cold_start`.
  2. Otherwise, build features per topic, average both models' probabilities, and rank the topics.
  3. For the top 3 topics, pick resources not already accepted or dismissed, and write them with rank, score, source `ml` and model_version. If a topic has no unused resource left, recommend its topic quiz instead.
  4. Each run first deletes that student's recommendations that are still pending, so the list never fills with duplicates.
- [ ] pytest for feature building, the cold-start branch and ranking

Run `train.py` before testing the route, so model files exist.

Check: "New Student" gets the introductory list, "Active Student" gets their weak topics ranked first, and `ml/results/` holds the metrics table and charts.

### Phase 5: dashboard, progress and reminders (FR4, FR6)

- [ ] Recommendations card with Accept and Dismiss (updates `status`); cold-start items labelled "Getting started"; a "Refresh recommendations" button
- [ ] Progress bar per topic (latest score), built with Recharts
- [ ] Consistency: streak count and a 14-day activity strip
- [ ] In-app reminders computed on load from stored dates (for example, no study in 3 days)

Check: logged in as "Active Student", the dashboard shows the streak, the weakest topic first and a reminder. Logged in as "New Student", it shows the introductory list.

### Phase 6: results capture (all requirements)

- [ ] `docs/test-cases.md`: one row per FR and NFR with steps, expected result, actual result, pass or fail. Include the cold-start case. Run every case and fill in the results.
- [ ] Response times for quiz submit and dashboard load, measured and recorded (NFR2)
- [ ] `docs/screenshots.md`: an ordered checklist of every screen to capture, with which account to use and what should be visible
- [ ] Final run of `train.py` so the results in `ml/results/` match the final code

Check: every test case has a recorded result, and every item in `screenshots.md` can be captured from the running app.

## Commands

Tools: Homebrew (`node`, `python@3.12`, `supabase/tap/supabase`). Python 3.12 lives in one venv at the repo root (`.venv`), shared by `ml/`, `content/` and `scripts/`; VS Code picks it up automatically. Activate it before any Python command: `source .venv/bin/activate`. Secrets go in `web/.env` (anon key only), `ml/.env`, `content/.env` and `scripts/.env`; copy from the matching `.env.example`.

```
# one-time setup
cd web && npm install
python3.12 -m venv .venv && .venv/bin/pip install -r ml/requirements.txt -r content/requirements.txt

# web (http://localhost:5173)
cd web && npm run dev
cd web && npm run build          # type-check and build

# ml (http://localhost:8000, GET /health)
cd ml && uvicorn app.main:app --reload
cd ml && pytest
cd ml && python -m training.train

# data (from the repo root)
python content/validate.py
python content/load.py
python scripts/seed_demo.py
python scripts/rls_check.py      # Phase 1 check; cleans up its test users and course
pytest scripts                   # quiz function tests against the linked project

# database (project already linked)
supabase migration new <name>    # creates supabase/migrations/<timestamp>_<name>.sql
supabase db push
```
