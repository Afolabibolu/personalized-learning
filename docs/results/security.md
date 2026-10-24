# Security: row-level security check (NFR3)

Run 2026-10-24 21:53 with `python scripts/rls_check.py --out docs/results/security.md` against the live Supabase project. Two test students (A and B) sign in with the public anon key, the same key the web app uses, and try to read and change each other's data. A signed-out visitor is also tried. The test accounts and test course are deleted at the end.

**Result: 46 of 46 checks passed.** "Refused" means the database rejected the request (42501 is Postgres' permission-denied code); "0 rows" means row-level security hid the other student's rows.

### Sign-up trigger

| Result | Check | Detail |
| --- | --- | --- |
| Pass | profile row created for each new user | RLS Student A is_simulated=False, RLS Student B is_simulated=False |

### Student B reading own data (control)

| Result | Check | Detail |
| --- | --- | --- |
| Pass | B reads own profile | 1 row(s |
| Pass | B reads own study logs | 1 row(s |
| Pass | B reads own quiz attempts | 1 row(s |
| Pass | B reads own attempt answers | 4 row(s |
| Pass | B reads own recommendations | 1 row(s |

### Student A reading student B's data

| Result | Check | Detail |
| --- | --- | --- |
| Pass | A reads B's profile | 0 rows |
| Pass | A reads B's study logs | 0 rows |
| Pass | A reads B's quiz attempts | 0 rows |
| Pass | A reads B's attempt answers | 0 rows |
| Pass | A reads B's recommendations | 0 rows |
| Pass | A opens B's quiz review | refused: P0002 attempt not found |

### Questions are hidden

| Result | Check | Detail |
| --- | --- | --- |
| Pass | A selects from questions | refused: 42501 permission denied for table questions |
| Pass | B selects from questions (after taking a quiz) | refused: 42501 permission denied for table questions |
| Pass | start_quiz returns no correct_answer or explanation | 4 questions, keys: ['format', 'id', 'options', 'stem', 'topic_id'] |

### Writing scores and answers directly

| Result | Check | Detail |
| --- | --- | --- |
| Pass | A inserts a quiz attempt with a made-up score | refused: 42501 permission denied for table quiz_attempts |
| Pass | A sets the score on own open attempt | refused: 42501 permission denied for table quiz_attempts |
| Pass | A inserts an attempt answer | refused: 42501 permission denied for table attempt_answers |
| Pass | A submits B's attempt | refused: P0002 attempt not found |
| Pass | B submits own completed attempt again | refused: P0001 attempt already submitted |

### Study logs

| Result | Check | Detail |
| --- | --- | --- |
| Pass | A logs a study session as B | refused: 42501 new row violates row-level security policy for table "study_logs" |
| Pass | A logs own study session | 1 row(s |

### Recommendations: status column only

| Result | Check | Detail |
| --- | --- | --- |
| Pass | A changes status of B's recommendation | 0 rows |
| Pass | B's recommendation still pending | pending |
| Pass | A changes priority_score of own recommendation | refused: 42501 permission denied for table recommendations |
| Pass | A inserts a recommendation | refused: 42501 permission denied for table recommendations |
| Pass | A accepts own recommendation | 1 row(s |

### Notifications

| Result | Check | Detail |
| --- | --- | --- |
| Pass | B has notifications to protect | 1 |
| Pass | A reads B's notifications | 0 rows |
| Pass | A marks B's notification read | 0 rows |
| Pass | A inserts a notification | refused: 42501 permission denied for table notifications |
| Pass | B changes the text of own notification | refused: 42501 permission denied for table notifications |
| Pass | B marks own notification read | 1 row(s |
| Pass | A updates B's reminder settings | 0 rows |

### Enrollments (my courses)

| Result | Check | Detail |
| --- | --- | --- |
| Pass | B adds a course to own courses | 1 row(s |
| Pass | A reads B's enrollments | 0 rows |
| Pass | A enrols B in a course | refused: 42501 new row violates row-level security policy for table "enrollments" |
| Pass | A removes B's enrollment | 0 rows |
| Pass | B's enrollment is still there |  |
| Pass | B removes own enrollment | 1 row(s |

### Profiles and content

| Result | Check | Detail |
| --- | --- | --- |
| Pass | A sets is_simulated on own profile | refused: 42501 permission denied for table profiles |
| Pass | A updates own department and level | 1 row(s |
| Pass | A reads courses | 1 row(s |
| Pass | A inserts a course | refused: 42501 permission denied for table courses |
| Pass | A edits a topic | refused: 42501 permission denied for table topics |
| Pass | Signed-out visitor reads courses | refused: 42501 permission denied for table courses |
