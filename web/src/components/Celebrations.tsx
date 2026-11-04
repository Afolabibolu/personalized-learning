import { useEffect, useState } from 'react'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { acknowledgeBadges, getGamification, type BadgeKey } from '../api/gamification'
import { badgeInfo } from '../lib/badges'
import { BadgeIcon } from './BadgeShelf'
import { Flame } from './dashboard/StreakCard'

// The "streak extended" moment shows when today's first activity was this recent.
const FRESH_MS = 15 * 60_000
const SHOW_MS = 4_000

function seenKey(studentId: string, day: string) {
  return `streak-celebrated:${studentId}:${day}`
}

function alreadyShown(key: string): boolean {
  try {
    return localStorage.getItem(key) !== null
  } catch {
    return false
  }
}

function markShown(key: string) {
  try {
    localStorage.setItem(key, '1')
  } catch {
    // Private mode: the moment may show again, which is harmless.
  }
}

/**
 * Short celebrations after an activity: "Streak extended to N days" after the first
 * activity of the day, and a pop-up for each new badge. Mounted once in the layout,
 * so it also shows on the quiz results page. Animations are motion-safe only.
 */
export function Celebrations() {
  const queryClient = useQueryClient()
  const g = useQuery({ queryKey: ['gamification'], queryFn: getGamification, staleTime: 30_000 })
  const [streakMoment, setStreakMoment] = useState<number | null>(null)
  const [badge, setBadge] = useState<BadgeKey | null>(null)

  useEffect(() => {
    const data = g.data
    if (!data || !data.today_active || !data.first_activity_today) return
    const key = seenKey(data.student_id, data.today)
    if (alreadyShown(key)) return
    if (Date.now() - new Date(data.first_activity_today).getTime() > FRESH_MS) return
    markShown(key)
    setStreakMoment(data.streak)
    const t = setTimeout(() => setStreakMoment(null), SHOW_MS)
    return () => clearTimeout(t)
  }, [g.data])

  useEffect(() => {
    if (badge || !g.data) return
    const next = g.data.badges.find((b) => !b.seen)
    if (!next) return
    setBadge(next.badge)
    acknowledgeBadges([next.badge])
      .then(() => queryClient.invalidateQueries({ queryKey: ['gamification'] }))
      .catch((e) => console.warn('Badge not acknowledged:', e))
  }, [g.data, badge, queryClient])

  useEffect(() => {
    if (!badge) return
    const t = setTimeout(() => setBadge(null), 6_000)
    return () => clearTimeout(t)
  }, [badge])

  return (
    <div className="pointer-events-none fixed inset-x-0 bottom-4 z-30 flex flex-col items-center gap-2 px-4" aria-live="polite">
      {streakMoment !== null && (
        <div
          className="pointer-events-auto flex items-center gap-3 rounded-2xl bg-orange-500 px-4 py-3 text-white shadow-lg motion-safe:animate-[pop_400ms_ease-out]"
          role="status"
          data-testid="streak-celebration"
        >
          <span className="grid h-10 w-10 place-items-center rounded-full bg-white/20">
            <Flame lit className="h-7 w-7 [&_path:first-child]:fill-white [&_path:last-child]:fill-amber-200" />
          </span>
          <div>
            <p className="font-semibold">
              {streakMoment === 1 ? 'Streak started: day 1' : `Streak extended to ${streakMoment} days`}
            </p>
            <p className="text-sm text-orange-50">Come back tomorrow to keep it going.</p>
          </div>
        </div>
      )}
      {badge && (
        <div
          className="pointer-events-auto flex items-center gap-3 rounded-2xl border border-slate-200 bg-white px-4 py-3 shadow-lg motion-safe:animate-[pop_400ms_ease-out]"
          role="status"
          data-testid="badge-popup"
          data-badge={badge}
        >
          <BadgeIcon badge={badge} earned />
          <div>
            <p className="text-xs font-semibold uppercase tracking-wide text-brand-600">Badge earned</p>
            <p className="font-semibold text-slate-900">{badgeInfo(badge).title}</p>
            <p className="text-sm text-slate-500">See all your badges on your profile.</p>
          </div>
          <button
            className="ml-2 rounded-lg p-1.5 text-slate-400 hover:bg-slate-100 hover:text-slate-700"
            aria-label="Close"
            onClick={() => setBadge(null)}
          >
            <svg viewBox="0 0 20 20" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden>
              <path d="M5 5l10 10M15 5L5 15" strokeLinecap="round" />
            </svg>
          </button>
        </div>
      )}
    </div>
  )
}
