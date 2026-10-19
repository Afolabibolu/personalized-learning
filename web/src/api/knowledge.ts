import { supabase } from './supabase'
import type { Course, Resource, ResourceType, Topic } from './types'

export type KnowledgeTopic = Topic & { resources: Resource[]; topic_quiz_id: string | null }
export type KnowledgeCourse = Course & { is_reviewed: boolean; topics: KnowledgeTopic[] }

export type KnowledgeStats = {
  courses: number
  topics: number
  resources: number
  notes: number
  lectures: number
  past_question_sets: number
  videos: number
  practice_questions: number
}

export const RESOURCE_ORDER: ResourceType[] = ['note', 'lecture', 'past_questions', 'video']

export function sortResources<T extends Pick<Resource, 'type' | 'title'>>(resources: T[]): T[] {
  return [...resources].sort(
    (a, b) => RESOURCE_ORDER.indexOf(a.type) - RESOURCE_ORDER.indexOf(b.type) || a.title.localeCompare(b.title),
  )
}

/** Every course with its topics (in teaching order) and their resources. */
export async function getKnowledgeBase(): Promise<KnowledgeCourse[]> {
  const { data, error } = await supabase
    .from('courses')
    .select(
      'id, code, title, description, is_reviewed, ' +
        'topics(id, course_id, slug, title, subtopics, summary, sequence_order, ' +
        'resources(id, title, type, url, source, is_introductory, intro_order), quizzes(id, kind))',
    )
    .order('code')
  if (error) throw error
  type Row = Omit<KnowledgeCourse, 'topics'> & {
    topics: (Topic & { resources: Resource[]; quizzes: { id: string; kind: string }[] })[]
  }
  return (data as unknown as Row[]).map((course) => ({
    ...course,
    topics: course.topics
      .sort((a, b) => a.sequence_order - b.sequence_order)
      .map(({ quizzes, resources, ...topic }) => ({
        ...topic,
        resources: sortResources(resources),
        topic_quiz_id: quizzes.find((q) => q.kind === 'topic')?.id ?? null,
      })),
  }))
}

/** Live counts from the knowledge_base_stats view. */
export async function getKnowledgeStats(): Promise<KnowledgeStats> {
  const { data, error } = await supabase.from('knowledge_base_stats').select('*').single()
  if (error) throw error
  return data as KnowledgeStats
}

export type ResourceDetail = Resource & {
  body: string | null
  topic: { id: string; title: string; course: { id: string; code: string; title: string } }
}

/** One resource with its Markdown body, for the in-app viewer. */
export async function getResource(id: string): Promise<ResourceDetail> {
  const { data, error } = await supabase
    .from('resources')
    .select(
      'id, title, type, url, body, source, is_introductory, intro_order, topic:topics(id, title, course:courses(id, code, title))',
    )
    .eq('id', id)
    .single()
  if (error) throw error
  return data as unknown as ResourceDetail
}
