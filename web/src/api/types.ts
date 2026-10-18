export type Level = 100 | 200 | 300 | 400 | 500
export type LearningPreference = 'reading' | 'video' | 'practice'
export type ActivityType = LearningPreference
export type QuestionFormat = 'single_choice' | 'true_false' | 'multi_select' | 'odd_one_out'

export type Profile = {
  id: string
  full_name: string | null
  department: string | null
  level: Level | null
  learning_preferences: LearningPreference[]
}

export type Course = {
  id: string
  code: string
  title: string
  description: string | null
}

export type Resource = {
  id: string
  title: string
  type: 'pdf' | 'video' | 'link'
  url: string
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
