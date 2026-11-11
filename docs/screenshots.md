# Screenshot checklist

In capture order. All app screenshots are taken by `python scripts/capture_screenshots.py` (laptop 1280 px wide unless stated) and saved in `docs/screenshots/`. Before capturing by hand, reset the demo accounts with `python scripts/seed_demo.py --demo-only`.

Demo logins (password `DemoPass2026!`): New Student `new.student@demo.example.com`, Stage 2 student `diagnostic.student@demo.example.com`, Active Student `active.student@demo.example.com`, 200-level student Bisi Adewale `bisi.student@demo.example.com`.

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
| 14 | Dashboard, cold start | Kemi Balogun (new.student@demo.example.com) | 'Hi Kemi'; a reminder to log study; 'Take the CSC 531/CSC 574 diagnostic' cards at the top of the list; six 'Getting started' items (topic 1 note and lecture, topic 2 note, per course) with 'Not enough quiz history yet'; empty streak (FR4, NFR4) | [`14-dashboard-new.png`](screenshots/14-dashboard-new.png) |
| 15 | Dashboard, ML recommendations | Tolu Adeyemi (active.student@demo.example.com) | 'Hi Tolu'; bell with unread count; weekly summary; Cognitive Psychology and Fuzzy Logic 'Needs attention' with reason lines and 'Matched to your preference'; one 'Keep it up'; streak, 14-day strip, progress chart (FR1, FR4, FR6) | [`15-dashboard-active.png`](screenshots/15-dashboard-active.png) |
| 16 | 'Why this?' panel | Tolu Adeyemi | Logistic Regression and Random Forest probabilities, their average, and the factors that raise risk (FR4) | [`16-why-this.png`](screenshots/16-why-this.png) |
| 17 | Progress chart, CSC 574 picked in the course dropdown | Tolu Adeyemi | Fuzzy Logic Systems bar in red below the 50% line; names on two lines (FR6) | [`17-progress-csc574.png`](screenshots/17-progress-csc574.png) |
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

## Course ingestion pipeline (Phase 9)

Taken by `python scripts/phase9_check.py --shots docs/screenshots/phase9` with a temporary student, which is deleted afterwards.

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 49 | Onboarding with course choice | New sign-up (Phase Nine Student) | Opens on 500 level with level tabs, CSC 531 and CSC 574 ticked, CSC 551 added, sample courses labelled, the chosen courses listed (NFR5) | [`p9-01-onboarding-courses.png`](screenshots/phase9/p9-01-onboarding-courses.png) |
| 50 | Course list: my courses and level cards | New sign-up | My courses with Remove; Browse courses with one card per level (100 to 500) and its course count (NFR5) | [`p9-02-courses.png`](screenshots/phase9/p9-02-courses.png) |
| 51 | A level page | New sign-up | 500 level courses split into First semester and Second semester, 'Back to all levels', sample badges and Add to my courses (NFR5) | [`p9-02b-level-page.png`](screenshots/phase9/p9-02b-level-page.png) |
| 52 | Knowledge Base with a sample course | New sign-up | CSC 551 section with the sample badge, topics, study notes and past questions (FR5, NFR5) | [`p9-03-knowledge-base.png`](screenshots/phase9/p9-03-knowledge-base.png) |
| 53 | Knowledge Base, one level, collapsed | New sign-up | The 400 level picked; one header per course with its level, topic count and sample badge; Expand all and Collapse all (FR5, NFR5) | [`p9-03b-knowledge-base-collapsed.png`](screenshots/phase9/p9-03b-knowledge-base-collapsed.png) |
| 54 | Sample course study note | New sign-up | Divide and Conquer note ending 'Source: CSC 551 Design and Analysis of Algorithms.pdf, Study Session 2' (NFR5) | [`p9-04-study-note.png`](screenshots/phase9/p9-04-study-note.png) |
| 55 | Sample course past questions | New sign-up | CSC 551 Graphs past questions grouped by paper (2024/25, 2023/24) (NFR5) | [`p9-05-past-questions.png`](screenshots/phase9/p9-05-past-questions.png) |
| 56 | Sample course topic page | New sign-up | Badge, summary, Take topic quiz (NFR5) | [`p9-06-topic.png`](screenshots/phase9/p9-06-topic.png) |
| 57 | Sample course topic quiz | New sign-up | A CSC 551 question in the quiz player (NFR5) | [`p9-07-quiz.png`](screenshots/phase9/p9-07-quiz.png) |
| 58 | Sample course quiz results | New sign-up | Score per topic for the CSC 551 quiz (NFR5) | [`p9-08-results.png`](screenshots/phase9/p9-08-results.png) |
| 59 | Dashboard with a sample course | New sign-up | Getting started items for CSC 531, CSC 551 and CSC 574; a 'Take the diagnostic' card for each (FR4, NFR5) | [`p9-09-dashboard.png`](screenshots/phase9/p9-09-dashboard.png) |
| 60 | Course page after removing | New sign-up | 'Not in your courses yet' with Add to my courses (NFR5) | [`p9-10-course-page.png`](screenshots/phase9/p9-10-course-page.png) |
| 61 | Course list on a phone (375 px) | New sign-up | Fits without sideways scroll (NFR1, NFR5) | [`p9-11-phone-courses.png`](screenshots/phase9/p9-11-phone-courses.png) |

## Videos, textbooks and course requests (25 October)

Taken by `python scripts/phase10_check.py --shots docs/screenshots/phase10`, with a temporary student for the course request, which is deleted afterwards.

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 62 | Recommendation with a video and a textbook | Tolu Adeyemi | 'Also recommended': a YouTube video and a textbook chapter for Cognitive Psychology (FR4, FR5) | [`p10-01-also-recommended.png`](screenshots/phase10/p10-01-also-recommended.png) |
| 63 | Recommended textbook card | Tolu Adeyemi | Interaction Design (5th ed.), Chapter 4: what to read and why, source: in the course folder (FR5) | [`p10-02-textbook.png`](screenshots/phase10/p10-02-textbook.png) |
| 64 | Topic page with every resource type | Tolu Adeyemi | Fuzzy Logic: study note, lecture, past questions, video, recommended textbook (FR5) | [`p10-03-topic-resources.png`](screenshots/phase10/p10-03-topic-resources.png) |
| 65 | Request a course | New student (Request Tester) | The form, 'Request sent', and the request listed as pending (NFR5) | [`p10-04-request-form.png`](screenshots/phase10/p10-04-request-form.png) |
| 66 | Request a course on a phone (375 px) | New student | The form fits; the request now shows 'Added to your courses' (NFR1, NFR5) | [`p10-05-phone-request.png`](screenshots/phase10/p10-05-phone-request.png) |

## Recommendation stages (3 November)

Taken by `python scripts/stage_check.py --shots docs/screenshots/stages` (and `--mobile --shots docs/screenshots/stages/mobile` for phone width). Run `python scripts/seed_demo.py --demo-only` first.

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 67 | Stage 1: no diagnostic yet | Kemi Balogun (new.student@demo.example.com) | 'Take the CSC 531 diagnostic…' and 'Take the CSC 574 diagnostic…' cards with Start diagnostic, mentioning ML after 3 quizzes; six 'Getting started' items (FR4, NFR4) | [`stage1-dashboard.png`](screenshots/stages/stage1-dashboard.png) |
| 68 | Stage 2: based on the diagnostic | Ngozi Eze (diagnostic.student@demo.example.com) | CSC 531: Cognitive Psychology (0 of 3), Conceptual Models (1 of 3), Problem Space and User-Centred Design (2 of 3), each 'Based on your diagnostic'; the first 'Why this?' open, saying it comes from the diagnostic score, not the models, and ML starts after 3 quizzes; a CSC 574 diagnostic card and its 'Getting started' items (FR4, NFR4) | [`stage2-dashboard.png`](screenshots/stages/stage2-dashboard.png) |
| 69 | Stage 3: machine learning | Tolu Adeyemi (active.student@demo.example.com) | 'Needs attention' and 'Keep it up' items with both models' probabilities in 'Why this?'; no diagnostic cards (FR4) | [`stage3-dashboard.png`](screenshots/stages/stage3-dashboard.png) |

## Streaks, XP and badges (4 November)

Taken by `python scripts/streak_check.py --shots docs/screenshots/streaks` (and `--mobile --shots docs/screenshots/streaks/mobile` for phone width), with temporary students for the at-risk, freeze and celebration states, which are deleted afterwards. Run `python scripts/seed_demo.py --demo-only` first.

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 70 | Streak card: today done | Tolu Adeyemi (active.student@demo.example.com) | Lit flame with a 7-day streak, 'Today counts', the daily goal ring at 20/30 min, today's and this week's XP, 1 of 2 freezes, the 14-day strip in orange (FR6). Card alone: streak-done-today-card.png | [`streak-done-today.png`](screenshots/streaks/streak-done-today.png) |
| 71 | Streak card: at risk | temporary student (active the 3 days before today) | Grey flame, 3-day streak (not 0), 'Do a quiz or log study today to keep your 3-day streak', today empty on the strip; the bell holds the streak-at-risk notification (FR6). Card alone: streak-at-risk-card.png | [`streak-at-risk.png`](screenshots/streaks/streak-at-risk.png) |
| 72 | Streak card: a freeze used | temporary student (7 days, yesterday missed, today) | 8-day streak, 'A streak freeze kept your streak alive on <yesterday>', a snowflake on yesterday's square, 0 of 2 freezes (FR6). Card alone: streak-freeze-used-card.png | [`streak-freeze-used.png`](screenshots/streaks/streak-freeze-used.png) |
| 73 | Badge shelf on the Profile page | Tolu Adeyemi | 5 of 9 earned with dates (first quiz, perfect score, 5 topics mastered, 3- and 7-day streak); 14 to 100 days greyed with how to earn them; longest streak and total XP (FR6) | [`badge-shelf.png`](screenshots/streaks/badge-shelf.png) |
| 74 | Celebration: streak started | temporary student, just after logging 30 minutes | Orange 'Streak started: day 1' moment at the bottom of the study log page (FR6) | [`celebration-streak.png`](screenshots/streaks/celebration-streak.png) |
| 75 | Celebration: badge earned | the same student, after their first quiz | 'Badge earned: First quiz' pop-up on the results page (FR6) | [`celebration-badge.png`](screenshots/streaks/celebration-badge.png) |

## Textbook links (4 November)

Taken by `python scripts/textbook_links_check.py --shots docs/screenshots/textbooks` (and `--mobile --shots docs/screenshots/textbooks/mobile` for phone width).

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 76 | Recommendation card with a textbook link | Tolu Adeyemi (active.student@demo.example.com) | A recommendation's 'Also recommended' with the topic's video and its textbook, and a 'Buy or preview' or 'Read free online' button beside the textbook (FR5) | [`recommendation-card-book-link.png`](screenshots/textbooks/recommendation-card-book-link.png) |
| 77 | Knowledge Base textbooks with links | Tolu Adeyemi | A search for 'Interaction Design': the CSC 531 topics' recommended textbooks, each with its button (FR5) | [`knowledge-base-book-link.png`](screenshots/textbooks/knowledge-base-book-link.png) |
| 78 | Textbook reading card with its link | Tolu Adeyemi | The reading card (book, what to read, why), then the button and a line saying what the link is (FR5) | [`reading-card-book-link.png`](screenshots/textbooks/reading-card-book-link.png) |

## Email reminders (4 November)

Taken by `python scripts/email_check.py --shots docs/screenshots/emails` (the dry-run emails, rendered from `ml/outbox/`). Screenshots of the same emails as they arrive in the inbox, from the real test send to TEST_EMAIL_TO, go in `docs/screenshots/emails/inbox/`.

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 79 | Email: streak at risk (dry run) | Kemi Balogun, nothing done today | 'A few minutes today starts a streak': the study time, one 'Log a study session' button, the unsubscribe link (FR6) | [`dry-run-streak-at-risk.png`](screenshots/emails/dry-run-streak-at-risk.png) |
| 80 | Email: daily digest (dry run) | Tolu Adeyemi, after /recommend | Today's unread 'new recommendations' and 'needs attention' notifications in one email, one 'See your recommendations' button (FR6) | [`dry-run-digest.png`](screenshots/emails/dry-run-digest.png) |
| 81 | Email: weekly summary (dry run) | Tolu Adeyemi | Minutes this week against last week, topics improved with their scores, the next topic to focus on, one button (FR6) | [`dry-run-weekly-summary.png`](screenshots/emails/dry-run-weekly-summary.png) |
| 82 | Email settings on the Profile page | Tolu Adeyemi | Reminder settings with 'Email me reminders' on and a tick box for each kind (FR6) | [`profile-email-settings.png`](screenshots/emails/profile-email-settings.png) |

## Course management (10 November)

Taken by `python scripts/manage_check.py --shots docs/screenshots/manage` (and `--mobile --shots docs/screenshots/manage/mobile` for phone width), with a temporary student, a temporary course manager and the throwaway test course, all removed afterwards.

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 83 | Request a course with files | temporary student (manage_check.py) | The request form filled in, two files chosen (an outline PDF and a past-question photo) with Remove, before sending (NFR5) | [`request-form-with-files.png`](screenshots/manage/request-form-with-files.png) |
| 84 | The student's request, pending | the same student | 'Request sent', and the request listed as Pending with its two files (NFR5) | [`request-sent.png`](screenshots/manage/request-sent.png) |
| 85 | Manage: Requests | temporary course manager | The request with the student's name, the details, both files to open, status In progress, and Mark added / Decline (NFR5) | [`manage-requests.png`](screenshots/manage/manage-requests.png) |
| 86 | Manage: Courses | the course manager | Every course grouped by level (100 to 500), each marked Sample or Reviewed (NFR5) | [`manage-courses.png`](screenshots/manage/manage-courses.png) |
| 87 | Manage: fixing a course | the course manager | The test course marked Reviewed; a topic open with its title and summary saved, its links (one just added) and its practice questions, one hidden (NFR5) | [`manage-course-editing.png`](screenshots/manage/manage-course-editing.png) |
| 88 | Manage: Edit history | the course manager | Each edit with the manager's name and time and what changed, from and to (NFR3, NFR5) | [`manage-history.png`](screenshots/manage/manage-history.png) |
| 89 | A declined request | the student | A second request marked Declined, with the reason the manager gave (NFR5) | [`request-declined.png`](screenshots/manage/request-declined.png) |

## Courses below 500 level (11 November)

Taken by `python scripts/levels_check.py` (saves to `docs/screenshots/levels/`, laptop 1280 px unless stated) as Bisi Adewale, 200 level, on COS 103, CSC 236, CSC 351 and CSC 472. Run `python scripts/seed_demo.py --demo-only` first.

| # | Screen | Account | What should be visible | File |
| --- | --- | --- | --- | --- |
| 90 | Knowledge Base, 100 level | Bisi Adewale | The 100 level picked; COS 103 Introduction to Programming expanded with its topics, subtopics and resources (FR5) | [`kb-100-level.png`](screenshots/levels/kb-100-level.png) |
| 91 | A 100-level topic page | Bisi Adewale | COS 103 Loops: summary, sample badge, Take topic quiz, Log study session, its note, past questions, video and textbook (FR5) | [`topic-cos103.png`](screenshots/levels/topic-cos103.png) |
| 92 | A 300-level study note | Bisi Adewale | CSC 351 Deterministic Finite Automata study note in the resource viewer (FR5) | [`note-csc351.png`](screenshots/levels/note-csc351.png) |
| 93 | 400-level past questions | Bisi Adewale | CSC 472 SQL past questions from the 2022/23 paper, with its source line (FR5) | [`pastq-csc472.png`](screenshots/levels/pastq-csc472.png) |
| 94 | A 200-level diagnostic result | Bisi Adewale | CSC 236 diagnostic: 14 of 21, and a score per topic, Recurrences and the Master Theorem 0/3 (FR2) | [`diagnostic-csc236.png`](screenshots/levels/diagnostic-csc236.png) |
| 95 | A 400-level quiz question | Bisi Adewale | CSC 472 SQL topic quiz, a multiple-answer question with the progress bar (FR2) | [`quiz-csc472.png`](screenshots/levels/quiz-csc472.png) |
| 96 | Dashboard with all three stages | Bisi Adewale | Take-the-diagnostic cards for COS 103 and CSC 351; CSC 236 ML items (Needs attention, Keep it up); CSC 472 'Based on your diagnostic'; COS 103 and CSC 351 'Getting started' (FR4) | [`dashboard-bisi.png`](screenshots/levels/dashboard-bisi.png) |
| 97 | Why this? on a 200-level ML card | Bisi Adewale | Recurrences and the Master Theorem: Logistic Regression 95%, Random Forest 86%, average 91%, and what drove it (FR4) | [`why-this-csc236.png`](screenshots/levels/why-this-csc236.png) |
| 98 | Progress chart, CSC 236 | Bisi Adewale | CSC 236 picked in the course dropdown; Recurrences in red at 20%, Quicksort and Merge Sort at 80% (FR6) | [`progress-csc236.png`](screenshots/levels/progress-csc236.png) |
| 99 | Bisi's dashboard on a phone (390 px) | Bisi Adewale | The same dashboard at phone width, no sideways scroll (NFR1) | [`phone-dashboard-bisi.png`](screenshots/levels/phone-dashboard-bisi.png) |

## Figures from files and the terminal

| Source | What | Requirement |
| --- | --- | --- |
| ml/results/model_comparison.png | Rule baseline vs LR vs RF on four metrics | FR4 |
| ml/results/confusion_rule_baseline.png | Rule baseline confusion matrix | FR4 |
| ml/results/confusion_logistic_regression.png | LR confusion matrix | FR4 |
| ml/results/confusion_random_forest.png | RF confusion matrix | FR4 |
| ml/results/feature_weights.png | LR coefficients and RF importances | FR4 |
| ml/results/metrics.md | Three-row metrics table | FR4 |
| ml/results/simulation_rules.md | How the simulated students were generated | FR4 |
| terminal: python scripts/rls_check.py | Output ending '46/46 checks passed' | NFR3 |
| docs/results/performance.md | Response-time table (20 runs each) | NFR2 |
| docs/results/security.md | Row-level security check, 52 checks | NFR3 |
| docs/results/courses.md | Every course in the knowledge base, with files used and skipped | NFR5 |
| ml/results/summary.md | Results in plain words, for Chapter Four | FR4 |
| Supabase dashboard: Authentication → Policies (taken by hand) | RLS enabled on every table, with its policies | NFR3 |

Charts and tables from `ml/results/` come from simulated students. Say so once in the report (in the methodology and at the start of the model results), not on every caption.
