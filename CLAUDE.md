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

## Current status (Monday 19 October)

Phases 0 to 6 are built and working: sign-up, courses, diagnostic and topic quizzes, study logging, the ML recommendation service with probabilities and a rule baseline, a reminder banner, the consistency card, progress by topic, and the Phase 6 test cases and screenshots.

The results defence is on Tuesday. What remains is closing the requirement gaps listed in `docs/requirements.md` (Phase 7), capturing results again (Phase 8), and, as a stretch, the course ingestion pipeline (Phase 9, done 24 October: 9 sample courses added). The 19 October revision of this file widened the scope of Phases 2 to 5 (study notes, past questions, a Knowledge Base page, learning-preference matching, reasons on recommendations); those items are tracked as gaps in `docs/requirements.md`, not as unfinished boxes in the phases below.

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

## Where the detailed rules live

Claude Code reads a folder's own CLAUDE.md when working in that folder. Read the one for the area you are changing:

- `docs/requirements.md`: every FR and NFR, what is built, the open gaps with checkboxes, and the evidence needed. The source of truth for what to do next.
- `web/CLAUDE.md`: pages, navigation, components and UI rules.
- `ml/CLAUDE.md`: the recommendation output format, explanations, notifications from the service, training and results.
- `supabase/CLAUDE.md`: new columns, the notifications table, `generate_reminders()`, and demo data.
- `content/CLAUDE.md`: knowledge base content rules and the ingestion pipeline for adding any course.

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
      links.csv        lecture and video links I paste in: course, lecture, kind, title, url
    courses/           one JSON file per course: topics, subtopics, lectures covered, summaries
    notes/             one study note per topic (Markdown)
    past_questions/    past exam questions per course, tagged by topic
    resources/         every resource per topic
    questions/         one JSON file per topic
    apply_links.py     rebuilds lecture resources from sources/links.csv
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
- Metrics come from simulated students. Say so once, clearly: at the top of `ml/results/metrics.md` and `summary.md`, and in the report's methodology and at the start of its model results (26 Oct: no longer on every file name, chart and caption). Never present them as results from real students.
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
- Training data: simulated students created by `scripts/seed_demo.py`, because there is no time for a pilot. The simulation follows documented learning patterns (see Phase 4), so the results chapter can describe it as a simulation study. The real-data comparison is future work.
- Knowledge base (FR5): courses, topics with subtopics, and resources of four types. A `note` is a short in-app study note, a `lecture` links to the lecture PDF, `past_questions` lists past exam questions on that topic, and a `video` is a link I supply. Students can browse it all from a Knowledge Base page, not only through recommendations.
- Learning preferences: at onboarding a student picks how they prefer to study (reading notes, lecture slides, practising questions, or videos), stored as the resource types note, lecture, past_questions, video. When the engine picks a resource for a weak topic, it prefers the student's preferred type and the card says "Matched to your preference". This is what the learning preferences captured under FR1 are used for. Study-log activity types stay reading, video, practice.
- Cold-start sequence per course (FR5, 19 Oct): topic 1's study note, topic 1's lecture, then topic 2's note. For a weak topic the engine recommends, in order: study note, past questions, lecture, video (the student's preferred type will go first once FR1 lands).
- Past questions: transcribed as written from the papers in `content/sources/` into `content/past_questions/<code>.json`, tagged by year and topic. The 2020/21 and 2021/22 HCI papers are from the MSc course (CSC 777/MBC 738) and are labelled so.
- The Inter font is bundled with the app (`@fontsource-variable/inter`), not loaded from Google Fonts, so the demo never waits on an outside server.
- Reminders and notifications (FR6, 19 Oct): in the app only, under a bell with an unread count, plus optional browser notifications while the app is open (turned on from the Profile page). Email (for example to Gmail) is future work, because it needs an email service and a scheduler. Times use Nigerian time (Africa/Lagos). Each notification kind fires at most once a day.
- Baseline: a simple rule, "requires attention if the last score on the topic was below 50%", is evaluated next to both models. It answers "why use machine learning at all?" with numbers, whichever way the numbers fall.
- Simulation calibration: the practice-gain and forgetting parameters were set once so that about a third of student-topic rows need attention (label balance only), never tuned to make one model win. Final values are in the config block at the top of `ml/training/synthetic.py` and in `ml/results/simulation_rules.md`.
- Demo accounts (password `DemoPass2026!`): Kemi Balogun, `new.student@demo.example.com` (no activity, cold start, prefers lecture slides and videos) and Tolu Adeyemi, `active.student@demo.example.com` (weak topics: CSC 531 Cognitive Psychology, CSC 574 Fuzzy Logic; prefers reading notes and practising questions). Reset both with `python scripts/seed_demo.py --demo-only` before presenting. Simulated students use `sim-NNN@sim.example.com`. `seed_demo.py` sets `is_simulated` on the profile itself, because the admin API writes app_metadata after the sign-up trigger runs. Only `is_simulated` students are used for training.
- Resource links come only from `content/sources/links.csv`. Each topic lists the lectures it covers (`lectures` in the course file); `content/apply_links.py` gives a lecture its own row's link, or the course's `all` fallback row (a Drive folder for CSC 574, labelled "Open lecture folder" in the app). Supplementary readings with no row in `links.csv` (Shneiderman, Tadeusiewicz, Bidgoli, Knowledge Representation in AI) are left out. `load.py` matches resources by topic and title, then by link, so a change updates the row in place.
- Dashboard labels: ML recommendations with averaged probability of 0.5 or more show as "Needs attention"; below 0.5 they show as "Keep it up" with a suggestion (review if not studied for 7+ days, try the topic quiz if scoring 80%+, otherwise a light practice nudge). Cold-start items show as "Getting started".
- Reminders (in-app, computed on dashboard load): a weak topic (below 50%) not studied for 7+ days or never, no study logged for 3+ days, and courses whose diagnostic has not been taken. Streak and the 14-day strip count days with a study log or a completed quiz.
- Sample courses (24 Oct): every course added through the pipeline is `is_reviewed: false` and labelled "Sample content, pending lecturer review" in the app. Sample size: 4 to 7 topics, a 300 to 500-word note per topic, 8 practice questions per topic in at least three formats, every past question found, and no lecture links unless `links.csv` has them (their getting-started list is topic 1's note, topic 1's past questions, topic 2's note). Facts come only from the course's files, except where a course's files do not cover a topic it needs (25 Oct, confirmed): then the topic is written from general knowledge of the course, following its outline (or the NUC CCMAS outline when the folder has none, as for COS 102), and the note's Source line and `docs/results/courses.md` say so. Past questions are never written from general knowledge. A lecture error (CSC 552 says first-order logic is decidable) is left out rather than repeated. M.Sc. papers filed with a course are labelled M.Sc. I review the sample courses against their sources myself before presenting them as reviewed.
- My courses (24 Oct, confirmed): students choose their own courses (`enrollments`) rather than courses following their level, for flexibility. New profiles start on the reviewed courses; onboarding and the course list add or remove others. Recommendations, reminders, the progress chart and the study-log picker cover only the student's courses; the Knowledge Base shows every course, the student's first, with an All/My courses toggle. The demo accounts stay on CSC 531 and CSC 574.
- Videos and textbooks (25 Oct, confirmed): every recommendation also suggests its topic's video and textbook ("Also recommended", from `explanation.also`). Videos are YouTube links picked from YouTube's search results (university courses and established teaching channels first), confirmed through oEmbed, and added to `links.csv` with the topic slug in the lecture column; a topic with no clearly matching video gets none. Textbooks are reading cards from `content/textbooks/<code>.json`: the book in the course folder first, then a standard textbook, with chapter numbers only where they are known.
- Exam-style questions (25 Oct): GES 103 has no past papers (CSC 412 had none until its 2022/23 paper arrived on 26 Oct), so it has exam-style questions written for practice, titled "Exam-style questions" and labelled "not from a past paper". Invented questions are never shown as past questions.
- Course requests (25 Oct, for scalability): a student who cannot find a course fills in Request a course (code, title, level, semester, lecturer, details). I add the course through the pipeline, then `scripts/course_requests.py add` enrols them and sends a "course is ready" notification. Sample courses may have up to 7 topics (CSC 572).
- 400-level courses (26 Oct): CSC 412 (rebuilt as Microprocessor Interfacing from the Ojo course material), CSC 421, CSC 431, CSC 472, CSC 475 (Professional Ethics for Computer Science, from the DLC book filed as "CSC 476 Computer Ethics") and CSC 476 (Research Methods in Computer Science), 7 topics each, as sample courses. CSC 421 and CSC 475 have no past paper, so their course books' review questions are used, labelled "Review questions". Lecture links (27 Oct): each 400-level course's `all` row in `links.csv` points to the shared 400 Level Drive folder (one subfolder per course), shown as "Open lecture folder"; the connector cannot list the files inside, so there are no per-lecture links. `seed_demo.py` builds simulated and demo histories from reviewed courses only.
- Training rows: one per student per topic. The label is the student's last attempt on the topic; features come only from attempts and study logs before it. ML recommendations are the top 3 topics overall, across all of the student's courses (ranked 1 to 3 by averaged probability). Cold-start lists stay per course.

## Database

| Table | Key columns | Students can |
| --- | --- | --- |
| profiles | id (= auth user id), full_name, department, level, learning_preferences, is_simulated | read and update own row (a trigger on `auth.users` creates the row at sign-up) |
| courses | id, code, title, description, is_reviewed, level (100 to 500) | read |
| topics | id, course_id, title, sequence_order, subtopics (list), summary (Phase 7) | read |
| resources | id, topic_id, title, type (note, lecture, past_questions, video, textbook), url (for links), body (Markdown, for in-app content, Phase 7), source, is_introductory, intro_order | read |
| quizzes | id, course_id, topic_id (null for diagnostic), kind (diagnostic or topic), question_count | read |
| questions | id, topic_id, format, stem, options, correct_answer, explanation, source, status (draft or approved) | no direct access |
| quiz_attempts | id, student_id, quiz_id, question_ids, score, started_at, completed_at | read own (created and graded only by the quiz functions) |
| attempt_answers | id, attempt_id, question_id, response, is_correct | read own (written only by `submit_quiz`) |
| study_logs | id, student_id, topic_id, duration_minutes, activity_type, logged_at | read and create own |
| recommendations | id, student_id, topic_id, resource_id, rank, priority_score, source (ml or cold_start), model_version, status, created_at | read own, update status only |

Question formats: `single_choice`, `true_false`, `multi_select`, `odd_one_out`.

Question shape (enforced by the schema and by `submit_quiz`): `options` is a list of `{"key", "text"}` with keys `a`, `b`, `c`, ...; true_false uses the keys `true` and `false`. `correct_answer` is always a list of keys: one for single_choice, true_false and odd_one_out (the odd option), two or more for multi_select. An answer is correct when the chosen keys equal the correct keys as a set, so a partial multi_select is wrong. Quiz responses are sent to `submit_quiz` as `{"<question id>": ["<key>", ...]}`.

Other student-callable SQL functions: `get_attempt_review(attempt_id)` returns a completed attempt's score, per-topic scores and answered questions (used by the results page), and `get_topic_scores(topic_ids)` returns the student's latest score per topic (the most recent completed attempt that covered it, diagnostic included). Screens use these because students cannot read `questions`.

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
- [x] Resources: the matching lecture PDF or Drive link for each topic. The first three lectures of each course, in teaching order, are its introductory resources (intro_order 1 to 3); this is the cold-start sequence.

This phase may run in a second Claude Code session. That session only touches files inside `content/` and does not commit; the main session commits its work after I approve the report.

Check: `validate.py` passes with zero errors, every topic has 10 questions in at least two formats, and every topic has a resource.

### Phase 3: React core (FR1, FR2, FR3)

- [x] Sign up and log in with Supabase Auth, with protected routes
- [x] Onboarding: department, level, learning preferences saved to `profiles`
- [x] Course list, with "Take diagnostic quiz" on courses not yet started
- [x] Quiz player: starts with `start_quiz`, one component per format, a progress bar, submits through `submit_quiz`
- [x] Results: score per topic, then each question with its correct answer and explanation
- [x] Topic page: resources, "Take topic quiz", "Log study session"
- [x] Study logger: topic, duration, activity type (reading, video, practice)
- [x] A consistent, clean visual style across screens, since these become screenshots

Check: a brand-new account can sign up, finish onboarding, take a diagnostic quiz, see per-topic results and log a 30-minute session, and every step lands in the right tables.

### Phase 4: ML service, simulated data and cold start (FR4, NFR4)

- [x] `scripts/seed_demo.py`, using the service role key. It runs after `load.py`, because simulated answers point to real questions:
  - Create every simulated and demo user through the Supabase admin API (`auth.admin.create_user`), so each one has a real auth user and profile row.
  - About 80 simulated students (`is_simulated = true`) with several weeks of quiz attempts and study logs, following these rules:
    - Each student has a hidden ability level, and each topic has a hidden difficulty, both drawn at random.
    - Forgetting curve: the chance of answering correctly falls the longer a topic goes unstudied.
    - Practice effect: study minutes and earlier attempts on a topic raise the next score, with diminishing returns.
    - Study habits differ: some students study often in short sessions, some rarely, some cram before quizzes.
    - Every answer has random noise, so no single feature decides the outcome.
    - The 50% label rule is never used inside the simulation. Scores come from the rules above, and the label is applied afterwards.
  - All rule parameters live in one config block (at the top of `ml/training/synthetic.py`, which the script uses), with a fixed random seed so results can be reproduced.
  - It writes `ml/results/simulation_rules.md`: a plain description of every rule and parameter value, for Chapter Four.
  - Demo account "New Student" with no activity, to show cold start.
  - Demo account "Active Student" with a history that makes one or two topics clearly weak, to show ML recommendations.
  - Prints the demo logins at the end. Running it again resets the simulated data.
- [x] `training/features.py`: one row per student per topic with mean_score, last_score, attempt_count, session_count, total_minutes, days_since_last_studied
- [x] Labels from the label rule above
- [x] `training/train.py`: Logistic Regression (StandardScaler in a pipeline) and Random Forest on the same stratified split, plus 5-fold cross-validation. The rule baseline (last score below 50%) is scored on the same test rows and folds. Saves to `ml/results/`:
  - a metrics table with three rows (rule baseline, Logistic Regression, Random Forest) and columns for accuracy, precision, recall and F1, with the cross-validation mean and spread, as CSV and Markdown
  - a confusion matrix chart for each of the three
  - one bar chart comparing all three on the four metrics
  - Logistic Regression coefficients and Random Forest feature importances, as a table and a chart
  - `metrics.md` and `summary.md` say at the top that the data is simulated (file names and chart titles do not repeat it)
- [x] `train.py --real-test <file>` (optional, only if time allows): scores the already-trained models and the rule on a CSV of real student rows exported from the app (`scripts/export_real_rows.py`), and saves a separate table titled "real student data".
- [x] `POST /recommend`:
  1. Below the cold-start threshold on a course, write that course's introductory resources in order with source `cold_start`.
  2. Otherwise, build features per topic, average both models' probabilities, and rank the topics.
  3. For the top 3 topics, pick resources not already accepted or dismissed, and write them with rank, score, source `ml` and model_version. If a topic has no unused resource left, recommend its topic quiz instead.
  4. Each run first deletes that student's recommendations that are still pending, so the list never fills with duplicates.
- [x] pytest for feature building, the cold-start branch and ranking

Run `train.py` before testing the route, so model files exist.

Check: "New Student" gets the introductory list, "Active Student" gets their weak topics ranked first, and `ml/results/` holds the three-row metrics table, the charts and `simulation_rules.md`.

### Phase 5: dashboard, progress and reminders (FR4, FR6)

- [x] Recommendations card with Accept and Dismiss (updates `status`); cold-start items labelled "Getting started"; a "Refresh recommendations" button
- [x] Progress bar per topic (latest score), built with Recharts
- [x] Consistency: streak count and a 14-day activity strip
- [x] In-app reminders computed on load from stored dates (for example, no study in 3 days)

Check: logged in as "Active Student", the dashboard shows the streak, the weakest topic first and a reminder. Logged in as "New Student", it shows the introductory list.

### Phase 6: results capture (all requirements)

- [x] `docs/test-cases.md`: one row per FR and NFR with steps, expected result, actual result, pass or fail. Include the cold-start case. Run every case and fill in the results.
- [x] Response times for quiz submit and dashboard load, measured and recorded (NFR2)
- [x] `docs/screenshots.md`: an ordered checklist of every screen to capture, with which account to use and what should be visible
- [x] Final run of `train.py` so the results in `ml/results/` match the final code

Check: every test case has a recorded result, and every item in `screenshots.md` can be captured from the running app.

### Phase 7: requirement gaps

Work through the gaps in `docs/requirements.md` in its priority order (FR5, FR4, FR6, FR1, then FR2 and FR3). Tick each box as it is done. Report after each requirement, not only at the end of the phase, so I can screenshot as we go.

Check: every FR box in `docs/requirements.md` is ticked or listed in the report as skipped with a reason.

### Phase 8: results capture

This replaces Phase 6 if it has not run yet. (Phase 6 has run; Phase 8 reruns it on the final code and adds the files below.)

- [x] `docs/test-cases.md`: one row per FR and NFR with steps, expected, actual, pass or fail. Run every case.
- [x] `scripts/timing.py` output in `docs/results/performance.md` (NFR2)
- [x] `scripts/rls_check.py` output in `docs/results/security.md` (NFR3)
- [x] Final `python -m training.train`, so `ml/results/` and `summary.md` match the final code
- [x] `docs/screenshots.md`: an ordered list of every screenshot, with the account to use, the page, and what must be visible. Include phone-width shots for NFR1.

Check: every test case has a recorded result, and every screenshot in the list can be taken from the running app.

### Phase 9: course ingestion pipeline (stretch)

Build `inventory.py` and `extract.py` from `content/CLAUDE.md`, then add one extra course in the default mode (no API key). The point is to show that a course goes from files to the app without code changes.

- [x] `content/ingest/inventory.py` (generic code detection, hand fixes in `inventory_fixes.csv`) and `extract.py` (text, scanned and image status)
- [x] `content/ingest/publish.py`: links, validation, then loading, and nothing is loaded if validation fails
- [x] All 500-level courses in `sources/raw/` plus CSC 412 and GES 103 added as sample courses (`is_reviewed: false`), listed in `docs/results/courses.md`; COS 102 (Problem Solving) added on 25 Oct from the CCMAS outline, its reference textbook and general knowledge
- [x] "My courses" (`enrollments` table) so recommendations, reminders and progress cover only the courses a student chose
- [x] `scripts/phase9_check.py`, TC-22 in `docs/test-cases.md`, screenshots in `docs/screenshots/phase9/`

Check: one course not built by hand appears in the app with topics, a study note and a working quiz, using only the pipeline commands.

## Commands

Tools: Homebrew (`node`, `python@3.12`, `supabase/tap/supabase`). Python 3.12 lives in one venv at the repo root (`.venv`), shared by `ml/`, `content/` and `scripts/`; VS Code picks it up automatically. Activate it before any Python command: `source .venv/bin/activate`. Secrets go in `web/.env` (anon key only), `ml/.env`, `content/.env` and `scripts/.env`; copy from the matching `.env.example`.

```
# one-time setup
cd web && npm install
python3.12 -m venv .venv && .venv/bin/pip install -r ml/requirements.txt -r content/requirements.txt -r scripts/requirements.txt

# web (http://localhost:5173)
cd web && npm run dev
cd web && npm run build          # type-check and build
cd web && npm test               # dashboard logic tests (streak, reminders, suggestions)

# ml (http://localhost:8000, GET /health)
cd ml && uvicorn app.main:app --reload
cd ml && pytest
cd ml && python -m training.train
cd ml && python -m training.train --real-test ../real_rows.csv   # optional; rows from: python scripts/export_real_rows.py real_rows.csv

# data (from the repo root)
python content/apply_links.py     # lecture resources from content/sources/links.csv
python content/validate.py
python content/load.py            # --course "CSC 551" for one course
python content/ingest/inventory.py   # Phase 9: find and classify files in content/sources/raw/
python content/ingest/extract.py --course "CSC 551"   # or --all
python content/ingest/publish.py --course "CSC 551"   # links, validate, then load
python scripts/seed_demo.py           # resets and recreates simulated students + demo accounts
python scripts/seed_demo.py --demo-only   # resets only the two demo accounts (run before presenting)
python scripts/rls_check.py      # Phase 1 check; cleans up its test users and course; --out docs/results/security.md
pytest scripts                   # quiz function tests against the linked project
python scripts/phase3_check.py   # Phase 3 check in Chrome; needs npm run dev; --mobile, --shots DIR, --keep
python scripts/phase4_check.py   # Phase 4 check; needs seed_demo, training.train and the ML service running
python scripts/phase5_check.py   # Phase 5 dashboard check in Chrome; --mobile, --shots DIR
python scripts/phase7_check.py   # Phase 7 checks in Chrome; --only fr5|fr4|fr6|fr1|fr23, --shots DIR
python scripts/phase9_check.py   # Phase 9 pipeline check (commands, database, Chrome); --shots DIR
python scripts/phase10_check.py  # videos, textbooks, exam-style sets, course requests; --shots DIR
python scripts/course_requests.py   # list course requests; add <id> --course "CODE" | decline <id> --note "..."
python scripts/timing.py         # NFR2 response times, 20 runs each -> docs/results/performance.md
python scripts/capture_screenshots.py  # every screen in docs/screenshots.md -> docs/screenshots/
python scripts/run_test_cases.py       # all FR/NFR test cases -> docs/test-cases.md (--measure to re-time)

# database (project already linked)
supabase migration new <name>    # creates supabase/migrations/<timestamp>_<name>.sql
supabase db push
```
