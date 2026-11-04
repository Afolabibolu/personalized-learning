import { refreshFallbackRecommendations } from './recommendations'
import { supabase } from './supabase'

const ML_URL = import.meta.env.VITE_ML_URL ?? 'http://localhost:8000'

/** Asks the ML service to recompute the signed-in student's recommendations. */
async function callMlService(): Promise<void> {
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
 * Recomputes the student's recommendations. If the ML service is down, the
 * database still writes the Stage 2 (diagnostic) lists, then the error is
 * rethrown so the dashboard can show its quiet notice.
 */
export async function refreshRecommendations(): Promise<void> {
  try {
    await callMlService()
  } catch (e) {
    await refreshFallbackRecommendations().catch((fallbackError) => console.warn('Fallback not written:', fallbackError))
    throw e
  }
}

/**
 * Fire-and-forget trigger after a quiz submit or study log. The student's
 * action has already been saved, so a failure here is only logged.
 */
export function triggerRecommendations(onDone?: () => void): void {
  refreshRecommendations()
    .catch((e) => console.warn('Recommendations not refreshed by the ML service:', e))
    .finally(() => onDone?.())
}
