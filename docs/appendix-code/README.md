# Code excerpts for the report appendix

Syntax-highlighted excerpts of the key code, each under 40 lines, with the file and real line numbers in the header. Lines left out are marked "lines N–M not shown". Regenerate with `python scripts/render_appendix_code.py` after changing any of these files.

| File | What it shows |
| --- | --- |
| [`01-start-quiz-picks-unseen-questions-first.png`](01-start-quiz-picks-unseen-questions-first.png) | The security-definer SQL function that starts a quiz for the signed-in student and picks each topic's questions, unseen ones first and then the longest unseen, so answers never reach the browser. |
| [`02-start-quiz-returns-questions-without-answers.png`](02-start-quiz-returns-questions-without-answers.png) | The second half of start_quiz: it stores the chosen question ids on a new attempt and returns the questions without their correct answers or explanations. |
| [`03-submit-quiz-grades-only-stored-questions.png`](03-submit-quiz-grades-only-stored-questions.png) | The SQL function that grades only the questions stored on the student's own attempt, refuses a second submission, and writes the answers and score itself, so students can never write their own scores. |
| [`04-recommender-cold-start-and-fallback.png`](04-recommender-cold-start-and-fallback.png) | The cold-start rule (fewer than three completed quizzes on a course, or no trained model) and the introductory list it returns, including the fallback that keeps a student on that list if ML ranking ever fails. |
| [`05-recommender-ranking-by-averaged-probability.png`](05-recommender-ranking-by-averaged-probability.png) | How topics are ranked by the average of the Logistic Regression and Random Forest probabilities, and how each top topic gets its resource (the student's preferred type first) or its topic quiz. |
| [`06-explain-reason-and-explanation.png`](06-explain-reason-and-explanation.png) | The reason line shown on every card (last score, days since studied, minutes studied) and the explanation object the ML service stores with each recommendation. |
| [`07-explain-top-factors.png`](07-explain-top-factors.png) | How the "Why this?" panel's top factors are computed: each feature's Logistic Regression coefficient times its standardised value, keeping the factors that push towards the verdict shown. |
| [`08-simulation-config-block.png`](08-simulation-config-block.png) | The single config block at the top of the simulation, with the fixed random seed and every parameter of the forgetting curve, practice effect, noise and study habits used to generate the training data. |
| [`09-rls-study-logs-policies.png`](09-rls-study-logs-policies.png) | Row-level security and grants on study_logs: a student can read and create only their own study sessions, and cannot log one with a future date. |
