# Screenshot checklist

In capture order. All app screenshots are taken by `python scripts/capture_screenshots.py` (laptop 1280 px wide unless stated) and saved in `docs/screenshots/`. Before capturing by hand, reset the demo accounts with `python scripts/seed_demo.py --demo-only`.

Demo logins (password `DemoPass2026!`): New Student `new.student@demo.example.com`, Active Student `active.student@demo.example.com`.

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 1 | Sign-up page | None (signed out) | Full name, email and password fields; link to sign in (FR1) | [`01-signup.png`](screenshots/01-signup.png) |
| 2 | Log-in page | None (signed out) | Email and password fields; link to create an account (FR1) | [`02-login.png`](screenshots/02-login.png) |
| 3 | Onboarding | New sign-up (Demo Student) | Department, level and learning-preference cards, two selected (FR1) | [`03-onboarding.png`](screenshots/03-onboarding.png) |
| 4 | Course list | New sign-up (Demo Student) | CSC 531 and CSC 574 with 'Take diagnostic quiz' buttons (FR2, FR5) | [`04-courses.png`](screenshots/04-courses.png) |
| 5 | Diagnostic quiz start | New sign-up (Demo Student) | 18 questions, 'Every topic', Start quiz button (FR2) | [`05-quiz-intro.png`](screenshots/05-quiz-intro.png) |
| 6 | Quiz question: single choice | New sign-up (Demo Student) | Progress bar, 'Single choice' label, one option selected (FR2) | [`06-quiz-single-choice.png`](screenshots/06-quiz-single-choice.png) |
| 7 | Quiz question: true or false | New sign-up (Demo Student) | Two large True/False buttons (FR2) | [`07-quiz-true-false.png`](screenshots/07-quiz-true-false.png) |
| 8 | Quiz question: multiple answers | New sign-up (Demo Student) | 'Select all that apply', two boxes ticked (FR2) | [`08-quiz-multi-select.png`](screenshots/08-quiz-multi-select.png) |
| 9 | Quiz question: odd one out | New sign-up (Demo Student) | 'Pick the one that does not belong' hint (FR2) | [`09-quiz-odd-one-out.png`](screenshots/09-quiz-odd-one-out.png) |
| 10 | Diagnostic results: score per topic | New sign-up (Demo Student) | Overall score, a coloured bar per topic, weakest topic called out (FR2) | [`10-results-summary.png`](screenshots/10-results-summary.png) |
| 11 | Diagnostic results: answer review | New sign-up (Demo Student) | Each question with your answer, the correct answer and the explanation (FR2) | [`11-results-answers.png`](screenshots/11-results-answers.png) |
| 12 | Topic page | New sign-up (Demo Student) | Summary, latest score, Take topic quiz, Log study session, resources grouped by type, subtopics (FR5) | [`12-topic.png`](screenshots/12-topic.png) |
| 13 | Study logger | New sign-up (Demo Student) | Topic, 30 min and Reading selected, 'Custom (minutes)', optional timer, 'Saved' confirmation, recent sessions (FR3) | [`13-log-study.png`](screenshots/13-log-study.png) |
| 14 | Dashboard, cold start | Kemi Balogun (new.student@demo.example.com) | 'Hi Kemi'; reminders to log study and take diagnostics; six 'Getting started' items (topic 1 note and lecture, topic 2 note, per course) with 'Not enough quiz history yet'; empty streak (FR4, NFR4) | [`14-dashboard-new.png`](screenshots/14-dashboard-new.png) |
| 15 | Dashboard, ML recommendations | Tolu Adeyemi (active.student@demo.example.com) | 'Hi Tolu'; bell with unread count; weekly summary; Cognitive Psychology and Fuzzy Logic 'Needs attention' with reason lines and 'Matched to your preference'; one 'Keep it up'; streak, 14-day strip, progress chart (FR1, FR4, FR6) | [`15-dashboard-active.png`](screenshots/15-dashboard-active.png) |
| 16 | 'Why this?' panel | Tolu Adeyemi | Logistic Regression and Random Forest probabilities, their average, and the factors that raise risk (FR4) | [`16-why-this.png`](screenshots/16-why-this.png) |
| 17 | Progress chart, CSC 574 tab | Tolu Adeyemi | Fuzzy Logic Systems bar in red below the 50% line; names on two lines (FR6) | [`17-progress-csc574.png`](screenshots/17-progress-csc574.png) |
| 18 | Dashboard on a phone (390 px) | Tolu Adeyemi | One column; menu button and bell stay in the header (NFR1) | [`18-phone-dashboard.png`](screenshots/18-phone-dashboard.png) |
| 19 | Quiz on a phone (390 px) | Tolu Adeyemi | Question and options fit the screen, Back/Next reachable (NFR1) | [`19-phone-quiz.png`](screenshots/19-phone-quiz.png) |

## Requirement screens (Phase 7)

Taken by `python scripts/phase7_check.py --shots docs/screenshots/phase7` (laptop 1280 px unless stated). Run `python scripts/seed_demo.py --demo-only` first.

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 20 | Knowledge Base | Tolu Adeyemi | Live counts, search box, topics with summaries and subtopics, resources grouped by type (FR5) | [`fr5-01-knowledge-base.png`](screenshots/phase7/fr5-01-knowledge-base.png) |
| 21 | Knowledge Base search | Tolu Adeyemi | 'fuzzy' filters to Fuzzy Logic Systems (FR5) | [`fr5-02-search.png`](screenshots/phase7/fr5-02-search.png) |
| 22 | Study note in the resource viewer | Tolu Adeyemi | Cognitive Psychology note rendered in the app, ending 'Source: Lecture 6' (FR5) | [`fr5-03-study-note.png`](screenshots/phase7/fr5-03-study-note.png) |
| 23 | Past questions in the resource viewer | Tolu Adeyemi | Data Gathering past questions grouped by paper, with the data table (FR5) | [`fr5-04-past-questions.png`](screenshots/phase7/fr5-04-past-questions.png) |
| 24 | Topic page | Tolu Adeyemi | Summary, resources grouped by type, quiz and log buttons (FR5) | [`fr5-05-topic.png`](screenshots/phase7/fr5-05-topic.png) |
| 25 | Knowledge Base on a phone (375 px) | Tolu Adeyemi | Menu button nav, no sideways scroll (FR5, NFR1) | [`fr5-06-phone-knowledge-base.png`](screenshots/phase7/fr5-06-phone-knowledge-base.png) |
| 26 | 'Why this?' panel | Tolu Adeyemi | Both model probabilities, their average, top factors (FR4) | [`fr4-01-why-this.png`](screenshots/phase7/fr4-01-why-this.png) |
| 27 | Cold-start items | Kemi Balogun | 'Getting started', 'Not enough quiz history yet', 'Take a few quizzes so we can personalise this for you' (FR4) | [`fr4-02-getting-started.png`](screenshots/phase7/fr4-02-getting-started.png) |
| 28 | Recommendation history | Kemi Balogun | Accepted and dismissed items under History (FR4) | [`fr4-03-history.png`](screenshots/phase7/fr4-03-history.png) |
| 29 | ML service unreachable | Kemi Balogun | Quiet notice 'Recommendations will update shortly', saved list still shown (FR4, NFR4) | [`fr4-04-service-down.png`](screenshots/phase7/fr4-04-service-down.png) |
| 30 | 'Why this?' on a phone | Tolu Adeyemi | Panel fits at 375 px (FR4, NFR1) | [`fr4-05-phone-why-this.png`](screenshots/phase7/fr4-05-phone-why-this.png) |
| 31 | Notifications bell | Tolu Adeyemi | Unread count and the list of reminders and feedback with times (FR6) | [`fr6-01-bell.png`](screenshots/phase7/fr6-01-bell.png) |
| 32 | Notifications page | Tolu Adeyemi | Full list, mark all read, link to reminder settings (FR6) | [`fr6-02-notifications-page.png`](screenshots/phase7/fr6-02-notifications-page.png) |
| 33 | Weekly summary | Tolu Adeyemi | Minutes vs last week, topics improved, next focus (FR6) | [`fr6-03-weekly-summary.png`](screenshots/phase7/fr6-03-weekly-summary.png) |
| 34 | Progress chart | Tolu Adeyemi | Long topic names on two lines (FR6) | [`fr6-04-progress-chart.png`](screenshots/phase7/fr6-04-progress-chart.png) |
| 35 | Reminder settings | Tolu Adeyemi | Study days, time, daily goal, browser notifications, 'saved' (FR6) | [`fr6-05-reminder-settings.png`](screenshots/phase7/fr6-05-reminder-settings.png) |
| 36 | Bell on a phone | Tolu Adeyemi | Bell visible beside the menu button, list fits (FR6, NFR1) | [`fr6-06-phone-bell.png`](screenshots/phase7/fr6-06-phone-bell.png) |
| 37 | Sign-up form | New sign-up (Ada Okoro) | Name, email, password (FR1) | [`fr1-01-signup.png`](screenshots/phase7/fr1-01-signup.png) |
| 38 | Onboarding | New sign-up (Ada Okoro) | The four study preferences, two selected (FR1) | [`fr1-02-onboarding.png`](screenshots/phase7/fr1-02-onboarding.png) |
| 39 | Matched to preference | Tolu Adeyemi | 'Hi Tolu', '✓ Matched to your preference: study notes' (FR1) | [`fr1-03-matched-preference.png`](screenshots/phase7/fr1-03-matched-preference.png) |
| 40 | Profile, before an edit | Tolu Adeyemi | Your details and reminder settings (FR1) | [`fr1-04-profile-before.png`](screenshots/phase7/fr1-04-profile-before.png) |
| 41 | Profile, after an edit | Tolu Adeyemi | New department and level, 'Profile saved.' (FR1) | [`fr1-05-profile-after.png`](screenshots/phase7/fr1-05-profile-after.png) |
| 42 | Kemi's dashboard | Kemi Balogun | 'Hi Kemi' with the introductory list (FR1, NFR4) | [`fr1-06-kemi-cold-start.png`](screenshots/phase7/fr1-06-kemi-cold-start.png) |
| 43 | Profile on a phone | Tolu Adeyemi | Fits at 375 px (FR1, NFR1) | [`fr1-07-phone-profile.png`](screenshots/phase7/fr1-07-phone-profile.png) |
| 44 | Results: change since last attempt | Temporary student | '0% to 20%, up 20 points' under the topic bar (FR2) | [`fr2-01-results-change.png`](screenshots/phase7/fr2-01-results-change.png) |
| 45 | Quiz history | Tolu Adeyemi | Date, quiz and score for every CSC 531 attempt (FR2) | [`fr2-02-quiz-history.png`](screenshots/phase7/fr2-02-quiz-history.png) |
| 46 | Study timer | Temporary student | Timer paused, ready to stop and use the time (FR3) | [`fr3-01-timer.png`](screenshots/phase7/fr3-01-timer.png) |
| 47 | Study logger | Temporary student | 'Custom (minutes)', timer, 'Saved' confirmation (FR3) | [`fr3-02-logger.png`](screenshots/phase7/fr3-02-logger.png) |
| 48 | Study logger on a phone | Tolu Adeyemi | Fits at 375 px, recent sessions stacked (FR3, NFR1) | [`fr3-03-phone-logger.png`](screenshots/phase7/fr3-03-phone-logger.png) |

## Figures from files and the terminal

| Source | What | Requirement |
| --- | --- | --- |
| ml/results/model_comparison_simulated_data.png | Rule baseline vs LR vs RF on four metrics (simulated data) | FR4 |
| ml/results/confusion_rule_baseline_simulated_data.png | Rule baseline confusion matrix (simulated data) | FR4 |
| ml/results/confusion_logistic_regression_simulated_data.png | LR confusion matrix (simulated data) | FR4 |
| ml/results/confusion_random_forest_simulated_data.png | RF confusion matrix (simulated data) | FR4 |
| ml/results/feature_weights_simulated_data.png | LR coefficients and RF importances (simulated data) | FR4 |
| ml/results/metrics_simulated_data.md | Three-row metrics table (simulated data) | FR4 |
| ml/results/simulation_rules.md | How the simulated students were generated | FR4 |
| terminal: python scripts/rls_check.py | Output ending '33/33 checks passed' | NFR3 |
| docs/results/performance.md | Response-time table (20 runs each) | NFR2 |
| docs/results/security.md | Row-level security check, 40 checks | NFR3 |
| ml/results/summary.md | Results in plain words, for Chapter Four (simulated data) | FR4 |
| Supabase dashboard: Authentication → Policies (taken by hand) | RLS enabled on every table, with its policies | NFR3 |

Charts and tables from `ml/results/` come from simulated students; keep "simulated data" in every caption.
