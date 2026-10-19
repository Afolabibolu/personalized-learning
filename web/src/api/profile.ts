import { currentUserId } from './auth'
import { supabase } from './supabase'
import type { Profile } from './types'

export async function getProfile(): Promise<Profile> {
  const id = await currentUserId()
  const { data, error } = await supabase
    .from('profiles')
    .select('id, full_name, department, level, learning_preferences, study_days, preferred_study_time, daily_goal_minutes, browser_notifications')
    .eq('id', id)
    .single()
  if (error) throw error
  return data
}

export function isOnboarded(profile: Profile): boolean {
  return Boolean(profile.department && profile.level)
}

export async function updateProfile(
  changes: Partial<
    Pick<
      Profile,
      | 'full_name'
      | 'department'
      | 'level'
      | 'learning_preferences'
      | 'study_days'
      | 'preferred_study_time'
      | 'daily_goal_minutes'
      | 'browser_notifications'
    >
  >,
): Promise<void> {
  const id = await currentUserId()
  const { error } = await supabase.from('profiles').update(changes).eq('id', id)
  if (error) throw error
}
