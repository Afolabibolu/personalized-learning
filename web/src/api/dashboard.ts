import { latestTopicScores, listCourses, listTopicsByCourse } from './courses'
import { supabase } from './supabase'

export type DashboardData = {
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
  const [logs, courseSummaries, topicsByCourse] = await Promise.all([
    // All logs (not just recent ones): reminders need each topic's last study date.
    supabase.from('study_logs').select('topic_id, logged_at, duration_minutes'),
    listCourses(),
    listTopicsByCourse(),
  ])
  if (logs.error) throw logs.error

  const allTopicIds = topicsByCourse.filter((c) => c.enrolled).flatMap((c) => c.topics.map((t) => t.id))
  const topicScores = await latestTopicScores(allTopicIds)
  const summaryById = new Map(courseSummaries.map((c) => [c.id, c]))

  return {
    studyLogs: logs.data,
    topicScores,
    // Only the student's own courses feed reminders and progress.
    courses: topicsByCourse.filter((c) => c.enrolled).map((c) => ({
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
