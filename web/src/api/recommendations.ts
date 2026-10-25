import { supabase } from './supabase'
import type { Resource } from './types'

export type RecommendationStatus = 'pending' | 'accepted' | 'dismissed'

/** Why a recommendation was made. Written by the ML service; the app only displays it. */
export type Explanation = {
  reason: string
  probabilities: { logistic_regression: number; random_forest: number; average: number } | null
  top_factors: { feature: string; label: string; value: number; direction: 'raises risk' | 'lowers risk' }[]
  matched_preference: string | null
  /** The topic's video and textbook, picked by the ML service alongside the main resource. */
  also?: { resource_id: string; type: 'video' | 'textbook'; title: string; url: string | null }[]
}

export type Recommendation = {
  id: string
  rank: number
  priority_score: number | null
  source: 'ml' | 'cold_start'
  model_version: string | null
  status: RecommendationStatus
  created_at: string
  explanation: Explanation | null
  topic: { id: string; title: string; course: { id: string; code: string } }
  resource: Pick<Resource, 'id' | 'title' | 'type' | 'url'> | null
  quiz: { id: string; title: string } | null
  topic_quiz_id: string | null
}

/** All of the student's recommendations: pending ones for the list, accepted and dismissed for History. */
export async function listRecommendations(): Promise<Recommendation[]> {
  const { data, error } = await supabase
    .from('recommendations')
    .select(
      'id, rank, priority_score, source, model_version, status, created_at, explanation, ' +
        'topic:topics(id, title, course:courses(id, code), quizzes(id, kind)), ' +
        'resource:resources(id, title, type, url), quiz:quizzes(id, title)',
    )
    .order('created_at', { ascending: false })
  if (error) throw error
  return (data as unknown as (Omit<Recommendation, 'topic_quiz_id'> & {
    topic: Recommendation['topic'] & { quizzes: { id: string; kind: string }[] }
  })[]).map(({ topic: { quizzes, ...topic }, ...rec }) => ({
    ...rec,
    topic,
    topic_quiz_id: quizzes.find((q) => q.kind === 'topic')?.id ?? null,
  }))
}

/** Students may change only the status column (enforced by a column grant). */
export async function setRecommendationStatus(id: string, status: Exclude<RecommendationStatus, 'pending'>): Promise<void> {
  const { error } = await supabase.from('recommendations').update({ status }).eq('id', id)
  if (error) throw error
}
