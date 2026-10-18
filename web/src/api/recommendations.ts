import { supabase } from './supabase'
import type { Resource } from './types'

export type RecommendationStatus = 'pending' | 'accepted' | 'dismissed'

export type Recommendation = {
  id: string
  rank: number
  priority_score: number | null
  source: 'ml' | 'cold_start'
  model_version: string | null
  status: RecommendationStatus
  created_at: string
  topic: { id: string; title: string; course: { id: string; code: string } }
  resource: Pick<Resource, 'id' | 'title' | 'type' | 'url'> | null
  quiz: { id: string; title: string } | null
  topic_quiz_id: string | null
}

/** Pending and accepted recommendations; dismissed ones are hidden. */
export async function listRecommendations(): Promise<Recommendation[]> {
  const { data, error } = await supabase
    .from('recommendations')
    .select(
      'id, rank, priority_score, source, model_version, status, created_at, ' +
        'topic:topics(id, title, course:courses(id, code), quizzes(id, kind)), ' +
        'resource:resources(id, title, type, url), quiz:quizzes(id, title)',
    )
    .in('status', ['pending', 'accepted'])
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
