export type Level = 100 | 200 | 300 | 400 | 500
/** Preferred ways to study: the four resource types (FR1). */
export type LearningPreference = 'note' | 'lecture' | 'past_questions' | 'video'
/** What a logged study session was. */
export type ActivityType = 'reading' | 'video' | 'practice'
export type QuestionFormat = 'single_choice' | 'true_false' | 'multi_select' | 'odd_one_out'

export type Weekday = 'mon' | 'tue' | 'wed' | 'thu' | 'fri' | 'sat' | 'sun'

export type Profile = {
  id: string
  full_name: string | null
  department: string | null
  level: Level | null
  learning_preferences: LearningPreference[]
  study_days: Weekday[]
  preferred_study_time: string // "18:00:00"
  daily_goal_minutes: number
  browser_notifications: boolean
}

export type Course = {
  id: string
  code: string
  title: string
  description: string | null
  /** false for sample courses added by the ingestion pipeline (Phase 9) */
  is_reviewed: boolean
  /** 100 to 500, from the course code; groups the Courses page */
  level: number | null
}

export type ResourceType = 'note' | 'lecture' | 'past_questions' | 'video' | 'textbook'

export type Resource = {
  id: string
  title: string
  type: ResourceType
  url: string | null // lecture and video: opens in a new tab
  source: string | null
  is_introductory: boolean
  intro_order: number | null
}

export type Quiz = {
  id: string
  course_id: string
  topic_id: string | null
  kind: 'diagnostic' | 'topic'
  title: string
  question_count: number
}

export type Topic = {
  id: string
  course_id: string
  slug: string
  title: string
  subtopics: string[]
  summary: string | null
  sequence_order: number
}

export type Option = { key: string; text: string }

export type QuizQuestion = {
  id: string
  topic_id: string
  format: QuestionFormat
  stem: string
  options: Option[]
}

export type StartedQuiz = {
  attempt_id: string
  quiz: Pick<Quiz, 'id' | 'title' | 'kind' | 'course_id' | 'topic_id'>
  questions: QuizQuestion[]
}

export type ReviewedQuestion = QuizQuestion & {
  response: string[]
  is_correct: boolean
  correct_answer: string[]
  explanation: string
}

export type TopicScore = {
  topic_id: string
  topic_title: string
  correct: number
  total: number
  score: number
  previous_score: number | null // this topic in the student's previous attempt that covered it
}

export type AttemptReview = {
  attempt_id: string
  quiz: StartedQuiz['quiz']
  score: number
  started_at: string
  completed_at: string
  topic_scores: TopicScore[]
  questions: ReviewedQuestion[]
}

export type StudyLog = {
  id: string
  topic_id: string
  duration_minutes: number
  activity_type: ActivityType
  logged_at: string
}
