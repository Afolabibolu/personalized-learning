import { supabase } from './supabase'
import type { AttemptReview, Quiz, StartedQuiz } from './types'

export async function getQuiz(quizId: string): Promise<Quiz & { course_code: string; topic_title: string | null }> {
  const { data, error } = await supabase
    .from('quizzes')
    .select('id, course_id, topic_id, kind, title, question_count, course:courses(code), topic:topics(title)')
    .eq('id', quizId)
    .single()
  if (error) throw error
  const { course, topic, ...quiz } = data
  return {
    ...quiz,
    course_code: (course as unknown as { code: string }).code,
    topic_title: (topic as unknown as { title: string } | null)?.title ?? null,
  }
}

export async function startQuiz(quizId: string): Promise<StartedQuiz> {
  const { data, error } = await supabase.rpc('start_quiz', { p_quiz_id: quizId })
  if (error) throw error
  return data as StartedQuiz
}

/** responses: question id -> chosen option keys */
export async function submitQuiz(attemptId: string, responses: Record<string, string[]>): Promise<AttemptReview> {
  const { data, error } = await supabase.rpc('submit_quiz', { p_attempt_id: attemptId, p_responses: responses })
  if (error) throw error
  return data as AttemptReview
}

export async function getAttemptReview(attemptId: string): Promise<AttemptReview> {
  const { data, error } = await supabase.rpc('get_attempt_review', { p_attempt_id: attemptId })
  if (error) throw error
  return data as AttemptReview
}
