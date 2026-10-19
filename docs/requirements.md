# Requirements coverage

This file maps every requirement in the report (Chapter 3) to what the app must show, the gap as of Monday 19 October, and the evidence for the results chapter. Work through the gaps in the priority order at the bottom. When a gap is closed, tick it and write where the evidence is.

## Functional requirements

### FR1: Registration and profile management

The report says: a student can register, authenticate, and create and update an academic profile with department, level and learning preferences.

Built: sign up, log in, sign out, onboarding.

Gaps:
- [x] No Profile page. Add one to the nav: full name, department, level, preferred way to study, and reminder settings (FR6). Saving shows a confirmation.
  _Done: `web/src/pages/ProfilePage.tsx` ("Your details": name, department, level, preferred way to study; "Reminder settings"), reached from the profile menu; saving shows "Profile saved."; screenshots `docs/screenshots/phase7/fr1-04-profile-before.png` and `fr1-05-profile-after.png`._
- [x] The learning preference is not visibly used. On each recommendation that matched it, show a small line such as "Matched to your preference: study notes".
  _Done: preferences are the four resource types (migration `20261019150000_learning_preferences_as_resource_types.sql`); the engine picks the preferred type first and records `matched_preference` (`ml/app/recommender.py`, test in `ml/tests/test_recommender.py`); cards show "✓ Matched to your preference: study notes"; screenshot `fr1-03-matched-preference.png`._
- [x] Demo accounts are named "Active" and "New". Rename them to realistic names, for example "Tolu Adeyemi" and "Kemi Balogun", with department Computer Science and level 500.
  _Done: `scripts/seed_demo.py` creates Tolu Adeyemi (active, prefers notes and practising questions) and Kemi Balogun (new, prefers lecture slides and videos), Computer Science, 500 level, default reminder settings; logins unchanged; screenshot `fr1-06-kemi-cold-start.png`._

Evidence: screenshots of sign-up, onboarding and the Profile page before and after an edit.

### FR2: Diagnostic and topic-based assessment

The report says: a diagnostic quiz when a student first engages with a course, topic quizzes afterwards, and scores recorded against the profile.

Built: diagnostic status on the course list.

Gaps:
- [x] Check that all four formats appear in a real quiz (single choice, true or false, select all, odd one out). Each needs a screenshot.
  _Done: `web/src/components/QuestionInputs.tsx` (one component per format); screenshots `docs/screenshots/06`–`09`, taken from a real diagnostic by `scripts/capture_screenshots.py`._
- [x] Results page: per-topic scores from the diagnostic, then each question with the correct answer and the explanation.
  _Done: `web/src/pages/ResultsPage.tsx` (data from `get_attempt_review`); screenshots `docs/screenshots/10-results-summary.png` and `11-results-answers.png`._
- [ ] Feedback against the last attempt on the results page, for example "Fuzzy Logic Systems: 40% to 70%, up 30 points".
- [ ] A Quiz history list on the course page: date, quiz, score.

Evidence: screenshots of each question format, the results page and quiz history.

### FR3: Study activity logging

Built: topic, duration chips, activity type, recent sessions.

Gaps:
- [ ] The free number box under the duration chips has no label. Label it "Custom (minutes)" and validate it (1 to 300).
  _Partly done: it has only an `aria-label` and accepts 1 to 600 (`LogStudyPage.tsx`)._
- [ ] Optional study timer: start, pause, stop, then the duration fills in.
- [x] "Log study session" on the topic page opens the logger with that topic already chosen.
  _Done: `web/src/pages/TopicPage.tsx` links to `/log?topic=<id>`; `web/src/pages/LogStudyPage.tsx` reads `?topic`._
- [x] After saving, show a confirmation and refresh recommendations in the background.
  _Done: `web/src/pages/LogStudyPage.tsx` shows "Saved: 30 minutes of reading" and calls `triggerRecommendations()` from `web/src/api/ml.ts`; screenshot `docs/screenshots/13-log-study.png`._

Evidence: screenshots of the logger and the recent sessions list.

### FR4: Machine learning recommendation engine

Built: ranked recommendations with "Needs attention" and a probability, refresh button, Accept and Dismiss.

Gaps:
- [x] A reason line on every item, built from the features: "Last score 40%. Not studied for 9 days. 20 minutes studied in total."
  _Done: written by the ML service into `recommendations.explanation` (`ml/app/explain.py`), shown by `web/src/components/dashboard/RecommendationsCard.tsx`; tests in `ml/tests/test_explain.py`._
- [x] A "Why this?" toggle that shows the Logistic Regression probability, the Random Forest probability, their average, and the top factors behind it.
  _Done: LR and RF probabilities, their average, and the LR factors that pushed toward the verdict (coefficient × scaled value); screenshot `docs/screenshots/phase7/fr4-01-why-this.png`._
- [x] Cold-start items look different: a "Getting started" label and the line "Take a few quizzes so we can personalise this for you."
  _Done: "Getting started" label, reason "Not enough quiz history yet for this course." and "Take a few quizzes so we can personalise this for you."; screenshot `fr4-02-getting-started.png`._
- [x] Accepting opens the resource. Accepted and dismissed items leave the list and appear under "History".
  _Done: "Accept and open" opens study notes in the app and lecture slides in a new tab; accepted and dismissed items move to a History section; screenshot `fr4-03-history.png`._
- [x] If the ML service is down, the dashboard keeps showing the last saved recommendations with a quiet notice, never an error screen (NFR4).
  _Done: a failed refresh shows "Recommendations will update shortly. Showing your last saved list." and keeps the list; the service falls back to cold start if a model is missing, corrupt or fails (`ml/app/data.py`, `ml/app/recommender.py`); screenshot `fr4-04-service-down.png`._

Evidence: dashboard screenshots for both demo accounts, the "Why this?" panel open, and the results table from `ml/results/`.

### FR5: Academic knowledge base

The report says: a structured repository of courses, topics, learning resources and practice questions, organised so the engine can retrieve resources for a weak topic.

Built: course list, topics, lecture resources.

Gaps:
- [x] A Knowledge Base page in the nav: courses, then topics in order with subtopics and a short summary, then resources grouped by type (study note, lecture slides, past questions, video).
  _Done: `web/src/pages/KnowledgeBasePage.tsx`, `web/src/components/ResourceList.tsx`; screenshot `docs/screenshots/phase7/fr5-01-knowledge-base.png`._
- [x] Study notes and past questions open inside the app in a resource viewer. Lecture and video links open in a new tab.
  _Done: `web/src/pages/ResourcePage.tsx` (react-markdown + remark-gfm); screenshots `fr5-03-study-note.png`, `fr5-04-past-questions.png`._
- [x] A search box on the Knowledge Base page that filters topics and resources by name.
  _Done: `KnowledgeBasePage.tsx` (filters as you type, empty state with "Clear the search"); screenshot `fr5-02-search.png`._
- [x] Every topic has at least a study note, a lecture link and a topic quiz.
  _Done: 12 notes in `content/notes/` (checked by `content/validate.py`: 300–500 words, source line), lecture links from `content/sources/links.csv`, topic quizzes from `content/load.py`; verified by `scripts/phase7_check.py --only fr5`._
- [x] A small count on the page: "2 courses, 12 topics, N resources, N practice questions", read live from the database.
  _Done: `knowledge_base_stats` view (`supabase/migrations/20261019090000_knowledge_base.sql`), shown by `KnowledgeBasePage.tsx`: 2 courses, 12 topics, 40 resources, 120 practice questions._

Evidence: screenshots of the Knowledge Base page, a topic page, a study note and a past-questions set.

### FR6: Progress tracking and engagement

The report says: track study consistency over time and give feedback and study reminders that encourage regular engagement.

Built: streak, active days, minutes, 14-day strip, progress by topic, one reminder banner.

Gaps:
- [x] A notifications centre: a bell in the nav with an unread count, and a list of reminders and feedback with time and a link. Kinds: weak topic not studied, streak at risk, no activity for 3 days, new recommendations ready, score improved.
  _Done: `notifications` table with RLS (`supabase/migrations/20261019130000_notifications_and_reminders.sql`); bell with unread count and list in `web/src/components/NotificationBell.tsx`, full list at `/notifications`. Kinds: streak at risk, 3 days inactive, daily goal reached and score improved from `generate_reminders()`; weak topic not studied and new recommendations from the ML service (`ml/app/notify.py`). Tests: `scripts/test_reminders.py`, `ml/tests/test_notify.py`; screenshots `fr6-01-bell.png`, `fr6-02-notifications-page.png`._
- [x] Reminder settings on the Profile page: study days, preferred study time, daily goal in minutes. The "streak at risk" and "daily goal" reminders use them.
  _Done: `web/src/pages/ProfilePage.tsx` (study days, preferred time, daily goal, browser notifications), used by `generate_reminders()`; screenshot `fr6-05-reminder-settings.png`._
- [x] Optional browser notification while the app is open, after the student allows it. Reminders still appear in the app if they do not.
  _Done: turned on from the Profile page only (asks the browser's permission there); `useBrowserNotifications` in `NotificationBell.tsx` pops up new unread reminders while the app is open; reminders stay in the bell either way. Email is out of scope (CLAUDE.md: in-app only) and listed as future work._
- [x] A weekly summary card: minutes this week against last week, topics improved, and the next topic to focus on.
  _Done: `web/src/components/dashboard/WeeklySummaryCard.tsx` with `web/src/lib/weekly.ts` (tested) and `get_topic_progress()`; screenshot `fr6-03-weekly-summary.png`._
- [x] Progress chart: long topic names are cut off. Wrap them onto two lines or show the full name on hover.
  _Done: names wrap onto two lines with the full name as a hover tooltip (`ProgressCard.tsx`); screenshot `fr6-04-progress-chart.png`._

Evidence: screenshots of the bell with unread count, the notifications list, reminder settings, and the weekly summary.

## Non-functional requirements

| Requirement | What proves it | Gap |
| --- | --- | --- |
| NFR1 Usability | Every core task works without help, on a phone and a laptop | [ ] Phone-width screenshots of the dashboard, quiz and logger (_partly: dashboard and quiz exist, `docs/screenshots/18`, `19`; logger missing_). [ ] Empty states with a clear next step on every page (_partly: dashboard and course list have them_) |
| NFR2 Performance | Measured response times | [ ] `scripts/timing.py`: times quiz submit, dashboard load and `/recommend` 20 times each and writes median and slowest to `docs/results/performance.md` (_partly: `scripts/measure_performance.py` does this 10 times each into `docs/performance.md`_) |
| NFR3 Security | Students only see their own data | [ ] Run `scripts/rls_check.py` and save its output to `docs/results/security.md` (_partly: 33/33 pass, excerpt in TC-14 of `docs/test-cases.md`_). [ ] Screenshot of the RLS policies in the Supabase dashboard (you take this one) |
| NFR4 Reliability | New students get a sensible result, and failures degrade quietly | [ ] "Kemi" screenshot with the cold-start list (_partly: `docs/screenshots/14-dashboard-new.png`, still named "New"_). [ ] ML service stopped: dashboard still loads with saved recommendations |
| NFR5 Portability | A new course can be added without code changes | [ ] The course ingestion pipeline in `content/CLAUDE.md`, run on at least one extra course, with a screenshot of it appearing in the app (_partly: TC-16 adds a course from JSON files with no code change; no inventory or extraction yet_) |

## Priority order for Monday

1. FR5 Knowledge Base page, resource viewer and study notes.
2. FR4 reason line, "Why this?" panel and cold-start styling.
3. FR6 notifications centre, reminder settings and weekly summary.
4. FR1 Profile page and demo account names.
5. FR2 and FR3 small gaps.
6. Results capture: NFR2 timing, NFR3 security output, model results table, test cases, screenshots.
7. NFR5 course ingestion pipeline (stretch, but it answers "can it scale to all courses?").
