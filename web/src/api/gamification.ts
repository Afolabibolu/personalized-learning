import { supabase } from './supabase'

export type BadgeKey =
  | 'streak_3'
  | 'streak_7'
  | 'streak_14'
  | 'streak_30'
  | 'streak_50'
  | 'streak_100'
  | 'first_quiz'
  | 'first_perfect'
  | 'five_mastered'

/** The streak card, computed by the database (my_gamification) in Nigerian time. Days are "YYYY-MM-DD". */
export type Gamification = {
  student_id: string
  today: string
  streak: number
  today_active: boolean
  at_risk: boolean
  longest_streak: number
  first_activity_today: string | null
  freezes: number
  max_freezes: number
  next_freeze_in: number | null
  freezes_used_in_streak: string[]
  daily_goal_minutes: number
  minutes_today: number
  goal_met: boolean
  xp_today: number
  xp_week: number
  xp_total: number
  strip: { day: string; active: boolean; frozen: boolean }[]
  badges: { badge: BadgeKey; earned_at: string; seen: boolean }[]
  mastered_topics: number
}

/** Also stores any badge earned since the last call. */
export async function getGamification(): Promise<Gamification> {
  const { data, error } = await supabase.rpc('my_gamification')
  if (error) throw error
  return data as Gamification
}

export async function acknowledgeBadges(badges: BadgeKey[]): Promise<void> {
  const { error } = await supabase.rpc('acknowledge_badges', { p_badges: badges })
  if (error) throw error
}
