import { currentUserId } from './auth'
import { supabase } from './supabase'
import type { ActivityType, StudyLog } from './types'

export async function logStudySession(input: {
  topicId: string
  durationMinutes: number
  activityType: ActivityType
}): Promise<StudyLog> {
  const studentId = await currentUserId()
  const { data, error } = await supabase
    .from('study_logs')
    .insert({
      student_id: studentId,
      topic_id: input.topicId,
      duration_minutes: input.durationMinutes,
      activity_type: input.activityType,
    })
    .select('id, topic_id, duration_minutes, activity_type, logged_at')
    .single()
  if (error) throw error
  return data
}

export async function listStudyLogs(limit = 20): Promise<(StudyLog & { topic_title: string })[]> {
  const { data, error } = await supabase
    .from('study_logs')
    .select('id, topic_id, duration_minutes, activity_type, logged_at, topic:topics(title)')
    .order('logged_at', { ascending: false })
    .limit(limit)
  if (error) throw error
  return data.map(({ topic, ...log }) => ({ ...log, topic_title: (topic as unknown as { title: string }).title }))
}
