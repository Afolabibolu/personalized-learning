import { supabase } from './supabase'
import type { Course, Quiz, Resource, Topic } from './types'

export type CourseSummary = Course & {
  topic_count: number
  diagnostic_quiz_id: string | null
  diagnostic_taken: boolean
}

export async function listCourses(): Promise<CourseSummary[]> {
  const [courses, attempts] = await Promise.all([
    supabase
      .from('courses')
      .select('id, code, title, description, topics(count), quizzes(id, kind)')
      .order('code'),
    supabase
      .from('quiz_attempts')
      .select('quizzes!inner(course_id, kind)')
      .not('completed_at', 'is', null)
      .eq('quizzes.kind', 'diagnostic'),
  ])
  if (courses.error) throw courses.error
  if (attempts.error) throw attempts.error

  const taken = new Set(
    attempts.data.map((a) => (a.quizzes as unknown as { course_id: string }).course_id),
  )
  return courses.data.map(({ topics, quizzes, ...course }) => ({
    ...course,
    topic_count: (topics as unknown as { count: number }[])[0]?.count ?? 0,
    diagnostic_quiz_id: (quizzes as { id: string; kind: string }[]).find((q) => q.kind === 'diagnostic')?.id ?? null,
    diagnostic_taken: taken.has(course.id),
  }))
}

export type TopicWithScore = Topic & { latest_score: number | null }

export type CourseDetail = Course & {
  topics: TopicWithScore[]
  diagnostic_quiz_id: string | null
}

export async function getCourse(courseId: string): Promise<CourseDetail> {
  const { data, error } = await supabase
    .from('courses')
    .select('id, code, title, description, topics(id, course_id, slug, title, subtopics, sequence_order), quizzes(id, kind)')
    .eq('id', courseId)
    .single()
  if (error) throw error

  const { topics, quizzes, ...course } = data
  const scores = await latestTopicScores(topics.map((t) => t.id))
  return {
    ...course,
    topics: topics
      .sort((a, b) => a.sequence_order - b.sequence_order)
      .map((t) => ({ ...t, latest_score: scores.get(t.id) ?? null })),
    diagnostic_quiz_id: quizzes.find((q) => q.kind === 'diagnostic')?.id ?? null,
  }
}

export type TopicDetail = Topic & {
  course: Pick<Course, 'id' | 'code' | 'title'>
  resources: Resource[]
  quiz: Quiz | null
  latest_score: number | null
}

export async function getTopic(topicId: string): Promise<TopicDetail> {
  const { data, error } = await supabase
    .from('topics')
    .select(
      'id, course_id, slug, title, subtopics, sequence_order, course:courses(id, code, title), resources(id, title, type, url, is_introductory, intro_order), quizzes(id, course_id, topic_id, kind, title, question_count)',
    )
    .eq('id', topicId)
    .single()
  if (error) throw error

  const { quizzes, course, resources, ...topic } = data
  const scores = await latestTopicScores([topic.id])
  return {
    ...topic,
    course: course as unknown as TopicDetail['course'],
    resources: [...resources].sort((a, b) => Number(b.is_introductory) - Number(a.is_introductory)),
    quiz: (quizzes as Quiz[])[0] ?? null,
    latest_score: scores.get(topic.id) ?? null,
  }
}

/** Topics of every course, for pickers such as the study logger. */
export async function listTopicsByCourse(): Promise<(Course & { topics: Topic[] })[]> {
  const { data, error } = await supabase
    .from('courses')
    .select('id, code, title, description, topics(id, course_id, slug, title, subtopics, sequence_order)')
    .order('code')
  if (error) throw error
  return data.map((c) => ({ ...c, topics: c.topics.sort((a, b) => a.sequence_order - b.sequence_order) }))
}

/**
 * The student's percentage on each topic in their most recent completed
 * attempt that included it. Diagnostic attempts count for every topic they
 * cover. Goes through a SQL function because students cannot read questions.
 */
export async function latestTopicScores(topicIds: string[]): Promise<Map<string, number>> {
  if (topicIds.length === 0) return new Map()
  const { data, error } = await supabase.rpc('get_topic_scores', { p_topic_ids: topicIds })
  if (error) throw error
  return new Map((data as { topic_id: string; score: number }[]).map((r) => [r.topic_id, Number(r.score)]))
}
