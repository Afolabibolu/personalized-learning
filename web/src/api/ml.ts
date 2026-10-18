import { supabase } from './supabase'

const ML_URL = import.meta.env.VITE_ML_URL ?? 'http://localhost:8000'

/** Asks the ML service to recompute the signed-in student's recommendations. */
export async function refreshRecommendations(): Promise<void> {
  const { data } = await supabase.auth.getSession()
  const token = data.session?.access_token
  if (!token) throw new Error('Not signed in')
  const response = await fetch(`${ML_URL}/recommend`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}` },
  })
  if (!response.ok) throw new Error(`Recommendation service returned ${response.status}`)
}

/**
 * Fire-and-forget trigger after a quiz submit or study log. The student's
 * action has already been saved, so a failure here is only logged.
 */
export function triggerRecommendations(): void {
  refreshRecommendations().catch((e) => console.warn('Recommendations not refreshed:', e))
}
