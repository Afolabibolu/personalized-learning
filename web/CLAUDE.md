# web/: React frontend

Read the root CLAUDE.md and `docs/requirements.md` first. This file adds the rules for the frontend only.

## Navigation

Top nav, in this order: Dashboard, Courses, Knowledge Base, Log study, then on the right a notifications bell with an unread count and a profile menu (Profile, Sign out). On phone width the links collapse into a menu button, and the bell stays visible.

## Pages

| Route | Page | Requirement |
| --- | --- | --- |
| `/` | Dashboard: weekly summary, recommendations, consistency, progress by topic | FR4, FR6 |
| `/courses` | My courses (with diagnostic status and Remove), then More courses grouped by level (500 first) with Add to my courses | FR2, NFR5 |
| `/courses/request` | Request a course: form (code, title, level, semester, lecturer, details) and the student's requests with their status | NFR5 |
| `/courses/:code` | Course page: topics with latest score, quiz history, "Take topic quiz" | FR2 |
| `/knowledge` | Knowledge Base: search, collapsible course sections (own courses open; a search opens every match; Expand all, Collapse all), topics with subtopics, resources grouped by type, live counts | FR5 |
| `/topics/:id` | Topic page: summary, subtopics, resources, latest score, "Take topic quiz", "Log study session" | FR5 |
| `/resources/:id` | Resource viewer: notes and past questions rendered with react-markdown | FR5 |
| `/quiz/:attemptId` | Quiz player | FR2 |
| `/quiz/:attemptId/results` | Results with per-topic scores, change since last attempt, explanations | FR2, FR6 |
| `/log` | Study logger, with `?topic=` to preselect | FR3 |
| `/notifications` | Full notifications list, mark as read | FR6 |
| `/profile` | Profile and reminder settings | FR1, FR6 |

## Components to build or fix

- `RecommendationCard`: label (Needs attention, Getting started, Keep it up), course code, probability, topic, resource title and type, the reason line, a "Matched to your preference" line when it applies, "Also recommended" (the topic's video and textbook, from `explanation.also`), Accept (opens the resource) and Dismiss. A "Why this?" toggle shows both model probabilities, their average and the top factors. The reason and factors come from the `explanation` field the ML service writes; do not compute them in the browser.
- `NotificationBell` and `NotificationList`: unread count from `notifications` where `read_at` is null. Clicking an item marks it read and follows its link.
- `WeeklySummary`: minutes this week against last week, topics whose latest score went up, and the top recommended topic.
- `ProgressByTopic`: a course dropdown (the student's courses), not tabs, so it scales to many courses. Wrap long topic names onto two lines; show the full name in a tooltip. Keep the 50% line and the colour legend.
- `StudyLogger`: label the custom box "Custom (minutes)", accept 1 to 300, and add an optional timer.
- `KnowledgeBase`: a search box that filters as you type, course sections, and a resource type icon for each resource.
- Sample courses (`is_reviewed = false`) carry the `SampleBadge` ("Sample content, pending lecturer review") on the course list, course page, topic page, Knowledge Base and onboarding.
- Empty states on every list, each with one clear next step (for example, "No quizzes yet. Take the diagnostic quiz.").

## Rules

- Every Supabase and ML call lives in `src/api/`. Pages never name tables directly.
- After a quiz submit or a study log, call the ML service in the background and refetch recommendations when it returns. If it fails, keep the saved list and show a small notice: "Recommendations will update shortly."
- Browser notifications are optional. Ask for permission from the Profile page only, never on page load.
- Keep the current visual style: white cards, indigo primary, red for needs attention, amber for 50 to 69%, green for 70% and above.
- Check every page at 375 px wide and at laptop width before reporting a task done.
- Dates show as "18 Oct 2026", not "10/18/2026".
