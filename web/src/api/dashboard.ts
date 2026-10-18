import { latestTopicScores, listCourses, listTopicsByCourse } from './courses'
import { supabase } from './supabase'

const HISTORY_DAYS = 60

export type DashboardData = {
  activityTimestamps: string[]
  studyLogs: { topic_id: string; logged_at: string; duration_minutes: number }[]
  courses: {
    id: string
    code: string
    title: string
    diagnostic_quiz_id: string | null
    diagnostic_taken: boolean
    topics: { id: string; title: string; sequence_order: number; score: number | null }[]
  }[]
  topicScores: Map<string, number>
}

export async function getDashboardData(): Promise<DashboardData> {
  const since = new Date(Date.now() - HISTORY_DAYS * 86_400_000).toISOString()
  const [logs, attempts, courseSummaries, topicsByCourse] = await Promise.all([
    // All logs (not just recent ones): reminders need each topic's last study date.
    supabase.from('study_logs').select('topic_id, logged_at, duration_minutes'),
    supabase.from('quiz_attempts').select('completed_at').not('completed_at', 'is', null).gte('completed_at', since),
    listCourses(),
    listTopicsByCourse(),
  ])
  if (logs.error) throw logs.error
  if (attempts.error) throw attempts.error

  const allTopicIds = topicsByCourse.flatMap((c) => c.topics.map((t) => t.id))
  const topicScores = await latestTopicScores(allTopicIds)
  const summaryById = new Map(courseSummaries.map((c) => [c.id, c]))

  return {
    activityTimestamps: [
      ...logs.data.map((l) => l.logged_at),
      ...attempts.data.map((a) => a.completed_at as string),
    ],
    studyLogs: logs.data,
    topicScores,
    courses: topicsByCourse.map((c) => ({
      id: c.id,
      code: c.code,
      title: c.title,
      diagnostic_quiz_id: summaryById.get(c.id)?.diagnostic_quiz_id ?? null,
      diagnostic_taken: summaryById.get(c.id)?.diagnostic_taken ?? false,
      topics: c.topics.map((t) => ({
        id: t.id,
        title: t.title,
        sequence_order: t.sequence_order,
        score: topicScores.get(t.id) ?? null,
      })),
    })),
  }
}
