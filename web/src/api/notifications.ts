import { supabase } from './supabase'

export type NotificationKind =
  | 'streak_at_risk'
  | 'inactive_3_days'
  | 'daily_goal_reached'
  | 'score_improved'
  | 'new_recommendations'
  | 'weak_topic_unstudied'
  | 'course_added'

export type AppNotification = {
  id: string
  kind: NotificationKind
  title: string
  body: string
  link: string | null
  created_at: string
  read_at: string | null
}

export async function listNotifications(limit = 50): Promise<AppNotification[]> {
  const { data, error } = await supabase
    .from('notifications')
    .select('id, kind, title, body, link, created_at, read_at')
    .order('created_at', { ascending: false })
    .limit(limit)
  if (error) throw error
  return data as AppNotification[]
}

/** Creates today's reminders from stored dates (once per kind per day) and returns the unread count. */
export async function generateReminders(): Promise<number> {
  const { data, error } = await supabase.rpc('generate_reminders')
  if (error) throw error
  return data as number
}

/** Students can change only read_at on their own notifications. */
export async function markNotificationsRead(ids: string[]): Promise<void> {
  if (ids.length === 0) return
  const { error } = await supabase.from('notifications').update({ read_at: new Date().toISOString() }).in('id', ids)
  if (error) throw error
}

export type TopicProgress = {
  topic_id: string
  latest_score: number
  previous_score: number | null
  latest_completed_at: string
}

/** Latest and previous score on each topic the student has attempted. */
export async function getTopicProgress(): Promise<TopicProgress[]> {
  const { data, error } = await supabase.rpc('get_topic_progress')
  if (error) throw error
  return (data as TopicProgress[]).map((r) => ({
    ...r,
    latest_score: Number(r.latest_score),
    previous_score: r.previous_score === null ? null : Number(r.previous_score),
  }))
}
