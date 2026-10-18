/** Local calendar day as YYYY-MM-DD. */
export function dayKey(date: Date): string {
  const y = date.getFullYear()
  const m = String(date.getMonth() + 1).padStart(2, '0')
  const d = String(date.getDate()).padStart(2, '0')
  return `${y}-${m}-${d}`
}

function addDays(date: Date, days: number): Date {
  const next = new Date(date)
  next.setDate(next.getDate() + days)
  return next
}

/** Days with any activity (study log or completed quiz). */
export function activityDays(timestamps: string[]): Set<string> {
  return new Set(timestamps.map((t) => dayKey(new Date(t))))
}

/**
 * Consecutive active days ending today. If today has no activity yet, the
 * streak still counts up to yesterday, so it does not reset in the morning.
 */
export function currentStreak(days: Set<string>, today: Date): number {
  let cursor = days.has(dayKey(today)) ? today : addDays(today, -1)
  let streak = 0
  while (days.has(dayKey(cursor))) {
    streak += 1
    cursor = addDays(cursor, -1)
  }
  return streak
}

export type StripDay = { key: string; weekday: string; dayOfMonth: number; active: boolean; isToday: boolean }

/** The last n days, oldest first, ending today. */
export function activityStrip(days: Set<string>, today: Date, n = 14): StripDay[] {
  return Array.from({ length: n }, (_, i) => {
    const date = addDays(today, i - (n - 1))
    const key = dayKey(date)
    return {
      key,
      weekday: date.toLocaleDateString('en-GB', { weekday: 'narrow' }),
      dayOfMonth: date.getDate(),
      active: days.has(key),
      isToday: i === n - 1,
    }
  })
}

/** Whole days between two moments (floor), never negative. */
export function daysBetween(earlier: Date, later: Date): number {
  return Math.max(0, Math.floor((later.getTime() - earlier.getTime()) / 86_400_000))
}
