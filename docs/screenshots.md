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
| 12 | Topic page | New sign-up (Demo Student) | Latest score badge, Take topic quiz, Log study session, resources and subtopics (FR5) | [`12-topic.png`](screenshots/12-topic.png) |
| 13 | Study logger | New sign-up (Demo Student) | Topic, 30 min and Reading selected, 'Saved' confirmation, recent sessions (FR3) | [`13-log-study.png`](screenshots/13-log-study.png) |
| 14 | Dashboard, cold start | New Student | Reminders to log study and take diagnostics; six 'Getting started' lectures in order; empty streak (FR4, NFR4) | [`14-dashboard-new.png`](screenshots/14-dashboard-new.png) |
| 15 | Dashboard, ML recommendations | Active Student | Weak-topic reminders; Cognitive Psychology and Fuzzy Logic as 'Needs attention' first; one 'Keep it up' with a suggestion; streak, 14-day strip, progress chart (FR4, FR6) | [`15-dashboard-active.png`](screenshots/15-dashboard-active.png) |
| 16 | Recommendation accepted | Active Student | First recommendation shows '✓ Accepted' and 'Open resource' (FR4) | [`16-dashboard-accepted.png`](screenshots/16-dashboard-accepted.png) |
| 17 | Progress chart, CSC 574 tab | Active Student | Fuzzy Logic Systems bar in red below the 50% line (FR6) | [`17-progress-csc574.png`](screenshots/17-progress-csc574.png) |
| 18 | Dashboard on a phone (390 px) | Active Student | Same dashboard in one column, compact nav (NFR1) | [`18-phone-dashboard.png`](screenshots/18-phone-dashboard.png) |
| 19 | Quiz on a phone (390 px) | Active Student | Question and options fit the screen, Back/Next reachable (NFR1) | [`19-phone-quiz.png`](screenshots/19-phone-quiz.png) |

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
| docs/performance.md | Response-time table | NFR2 |

Charts and tables from `ml/results/` come from simulated students; keep "simulated data" in every caption.
