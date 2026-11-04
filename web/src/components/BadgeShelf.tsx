import type { BadgeKey, Gamification } from '../api/gamification'
import { BADGES, badgeInfo } from '../lib/badges'
import { formatDate } from '../lib/format'
import { Card } from './ui'

export function BadgeIcon({ badge, earned }: { badge: BadgeKey; earned: boolean }) {
  const kind = badgeInfo(badge).kind
  const tone = !earned
    ? 'bg-slate-100 text-slate-300'
    : kind === 'streak'
      ? 'bg-orange-100 text-orange-600'
      : kind === 'mastery'
        ? 'bg-green-100 text-green-700'
        : 'bg-brand-100 text-brand-700'
  const days = badge.startsWith('streak_') ? badge.slice(7) : null
  return (
    <span className={`relative grid h-12 w-12 shrink-0 place-items-center rounded-full ${tone}`} aria-hidden>
      {days ? (
        <>
          <svg viewBox="0 0 24 24" className="h-7 w-7" fill="currentColor">
            <path d="M12 2.5c.4 3-1.3 4.6-2.8 6.2C7.6 10.4 6 12.1 6 15a6 6 0 0 0 12 0c0-2.3-1-4.1-2.2-5.6-.3 1.4-1 2.4-2.1 2.9.4-3.6-.6-7.3-1.7-9.8Z" />
          </svg>
          <span className={`absolute -bottom-1 rounded-full px-1.5 text-[10px] font-bold ${earned ? 'bg-orange-500 text-white' : 'bg-slate-200 text-slate-500'}`}>
            {days}
          </span>
        </>
      ) : kind === 'mastery' ? (
        <svg viewBox="0 0 24 24" className="h-7 w-7" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M12 3 4 7l8 4 8-4-8-4ZM4 12l8 4 8-4M4 17l8 4 8-4" />
        </svg>
      ) : badge === 'first_perfect' ? (
        <svg viewBox="0 0 24 24" className="h-7 w-7" fill="currentColor">
          <path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9L12 3Z" />
        </svg>
      ) : (
        <svg viewBox="0 0 24 24" className="h-7 w-7" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M9 4h6v3H9zM9 5.5H6.5A1.5 1.5 0 0 0 5 7v12.5A1.5 1.5 0 0 0 6.5 21h11a1.5 1.5 0 0 0 1.5-1.5V7a1.5 1.5 0 0 0-1.5-1.5H15M8.5 13.5l2.5 2.5 4.5-5" />
        </svg>
      )}
    </span>
  )
}

/** Every badge, earned ones in colour with their date, the rest greyed out with how to earn them. */
export function BadgeShelf({ g }: { g: Gamification }) {
  const earned = new Map(g.badges.map((b) => [b.badge, b.earned_at]))
  return (
    <Card>
      <div className="flex items-baseline justify-between gap-2">
        <h2 className="font-semibold">Badges</h2>
        <p className="text-sm text-slate-500" data-testid="badge-count">
          {earned.size} of {BADGES.length} earned
        </p>
      </div>
      <p className="mt-1 text-sm text-slate-500">
        Longest streak: {g.longest_streak} {g.longest_streak === 1 ? 'day' : 'days'} · {g.xp_total} XP in total
      </p>
      <ul className="mt-4 grid gap-3 sm:grid-cols-2" data-testid="badge-shelf">
        {BADGES.map((b) => {
          const at = earned.get(b.key)
          return (
            <li
              key={b.key}
              className={`flex items-center gap-3 rounded-xl border px-3 py-2.5 ${at ? 'border-slate-200 bg-white' : 'border-dashed border-slate-200 bg-slate-50'}`}
              data-testid="badge"
              data-badge={b.key}
              data-earned={Boolean(at)}
            >
              <BadgeIcon badge={b.key} earned={Boolean(at)} />
              <div className="min-w-0">
                <p className={`text-sm font-semibold ${at ? 'text-slate-900' : 'text-slate-500'}`}>{b.title}</p>
                <p className="text-xs text-slate-500">{at ? `Earned ${formatDate(at)}` : b.howTo}</p>
              </div>
            </li>
          )
        })}
      </ul>
    </Card>
  )
}
