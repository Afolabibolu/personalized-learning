import type { Gamification } from '../../api/gamification'
import { formatDay } from '../../lib/format'
import { Card } from '../ui'

/** Streak, daily goal, XP, freezes and the 14-day strip. Every number comes from the database. */
export function StreakCard({ g }: { g: Gamification }) {
  const lit = g.today_active
  const lastFreeze = g.freezes_used_in_streak.at(-1)

  return (
    <Card>
      <div className="flex items-center justify-between gap-2">
        <h2 className="font-semibold">Streak</h2>
        <FreezeChips held={g.freezes} max={g.max_freezes} />
      </div>

      <div className="mt-3 grid grid-cols-3 gap-2 sm:gap-3">
        <div className="flex flex-col items-center rounded-xl bg-slate-50 px-2 py-2.5 text-center" data-testid="streak-flame" data-lit={lit}>
          <Flame lit={lit} />
          <p className="text-2xl font-bold leading-tight text-slate-900" data-testid="streak">
            {g.streak}
          </p>
          <p className="text-[11px] leading-tight text-slate-500">day streak</p>
        </div>

        <GoalRing minutes={g.minutes_today} goal={g.daily_goal_minutes} met={g.goal_met} />

        <div className="flex flex-col items-center justify-center rounded-xl bg-slate-50 px-2 py-2.5 text-center" data-testid="xp">
          <p className="text-2xl font-bold leading-tight text-slate-900">
            <span data-testid="xp-today">{g.xp_today}</span>
            <span className="ml-0.5 text-xs font-semibold text-slate-500">XP</span>
          </p>
          <p className="text-[11px] leading-tight text-slate-500">today</p>
          <p className="mt-1.5 text-sm font-semibold text-slate-700" data-testid="xp-week">
            {g.xp_week} XP
          </p>
          <p className="text-[11px] leading-tight text-slate-500">this week</p>
        </div>
      </div>

      <p
        className={`mt-3 rounded-lg px-3 py-2 text-sm ${lit ? 'bg-orange-50 text-orange-800' : 'bg-slate-100 text-slate-700'}`}
        data-testid="streak-message"
      >
        {lit
          ? g.streak === 1
            ? 'Today counts. Day 1 of a new streak.'
            : `Today counts. Your streak is ${g.streak} days.`
          : g.at_risk
            ? `Do a quiz or log study today to keep your ${g.streak}-day streak`
            : 'Do a quiz or log study today to start a streak.'}
      </p>

      {lastFreeze ? (
        <p className="mt-2 flex items-center gap-1.5 text-xs text-sky-800" data-testid="freeze-used">
          <Snowflake className="h-3.5 w-3.5 text-sky-500" />
          A streak freeze kept your streak alive on {formatDay(lastFreeze)}
          {g.freezes_used_in_streak.length > 1 ? ` (${g.freezes_used_in_streak.length} used in this streak)` : ''}.
        </p>
      ) : (
        <p className="mt-2 text-xs text-slate-500" data-testid="freeze-info">
          {g.next_freeze_in === null
            ? `You hold the most freezes (${g.max_freezes}). One is used automatically if you miss a day.`
            : `Every 7 days in a row earns a streak freeze (next in ${g.next_freeze_in} ${g.next_freeze_in === 1 ? 'day' : 'days'}). It saves your streak on a missed day.`}
        </p>
      )}

      <div className="mt-4">
        <p className="mb-2 text-xs text-slate-500">Last 14 days (quizzes and study sessions, Nigerian time)</p>
        <ol className="grid grid-cols-14 gap-1" data-testid="activity-strip">
          {g.strip.map((d, i) => (
            <li
              key={d.day}
              className="flex flex-col items-center gap-1"
              title={`${formatDay(d.day)}${d.active ? ': active' : d.frozen ? ': streak freeze used' : ''}`}
            >
              <span
                className={`grid aspect-square w-full place-items-center rounded-md ${
                  d.active ? 'bg-orange-500' : d.frozen ? 'bg-sky-200' : 'bg-slate-200'
                } ${i === g.strip.length - 1 ? 'ring-2 ring-orange-300 ring-offset-1' : ''}`}
                data-active={d.active}
                data-frozen={d.frozen}
              >
                {d.frozen && <Snowflake className="h-3 w-3 text-sky-700" />}
              </span>
              <span className="text-[10px] text-slate-400">{weekday(d.day)}</span>
            </li>
          ))}
        </ol>
      </div>
    </Card>
  )
}

function weekday(day: string): string {
  const [y, m, d] = day.split('-').map(Number)
  return 'SMTWTFS'[new Date(y, m - 1, d).getDay()]
}

export function Flame({ lit, className = 'h-8 w-8' }: { lit: boolean; className?: string }) {
  return (
    <svg viewBox="0 0 24 24" className={className} aria-label={lit ? 'Streak lit for today' : 'Streak not yet lit today'} role="img">
      <path
        d="M12 2.5c.4 3-1.3 4.6-2.8 6.2C7.6 10.4 6 12.1 6 15a6 6 0 0 0 12 0c0-2.3-1-4.1-2.2-5.6-.3 1.4-1 2.4-2.1 2.9.4-3.6-.6-7.3-1.7-9.8Z"
        className={lit ? 'fill-orange-500' : 'fill-slate-300'}
      />
      <path
        d="M12 13.2c-1.4 1.2-2.4 2.3-2.4 3.8a2.4 2.4 0 0 0 4.8 0c0-1.5-1-2.6-2.4-3.8Z"
        className={lit ? 'fill-amber-300' : 'fill-slate-200'}
      />
    </svg>
  )
}

export function Snowflake({ className = '' }: { className?: string }) {
  return (
    <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" className={className} aria-hidden>
      <path d="M10 2v16M3.1 6l13.8 8M3.1 14l13.8-8M7.5 3.5 10 5l2.5-1.5M7.5 16.5 10 15l2.5 1.5" />
    </svg>
  )
}

function FreezeChips({ held, max }: { held: number; max: number }) {
  return (
    <span
      className="flex items-center gap-1 rounded-full bg-sky-50 px-2 py-1 text-xs font-medium text-sky-800"
      title="Streak freezes: one for every 7 days in a row, at most 2"
      data-testid="freezes"
      data-held={held}
    >
      {Array.from({ length: max }, (_, i) => (
        <Snowflake key={i} className={`h-3.5 w-3.5 ${i < held ? 'text-sky-500' : 'text-slate-300'}`} />
      ))}
      {held} of {max} freezes
    </span>
  )
}

function GoalRing({ minutes, goal, met }: { minutes: number; goal: number; met: boolean }) {
  const r = 22
  const circumference = 2 * Math.PI * r
  const share = Math.min(1, minutes / goal)
  return (
    <div className="flex flex-col items-center rounded-xl bg-slate-50 px-2 py-2.5 text-center" data-testid="goal-ring" data-met={met}>
      <div className="relative h-14 w-14">
        <svg viewBox="0 0 56 56" className="h-14 w-14 -rotate-90" role="img" aria-label={`${minutes} of ${goal} minutes today`}>
          <circle cx="28" cy="28" r={r} fill="none" strokeWidth="6" className="stroke-slate-200" />
          {share > 0 && (
            <circle
              cx="28"
              cy="28"
              r={r}
              fill="none"
              strokeWidth="6"
              strokeLinecap="round"
              strokeDasharray={`${share * circumference} ${circumference}`}
              className={met ? 'stroke-green-500' : 'stroke-brand-600'}
            />
          )}
        </svg>
        <span className="absolute inset-0 grid place-items-center">
          {met ? (
            <svg viewBox="0 0 20 20" className="h-6 w-6 text-green-600" fill="none" stroke="currentColor" strokeWidth="2.5" aria-label="Goal met" role="img" data-testid="goal-tick">
              <path d="m5 10.5 3.2 3.2L15 7" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          ) : (
            <span className="text-xs font-semibold text-slate-700">{Math.round(share * 100)}%</span>
          )}
        </span>
      </div>
      <p className="mt-1 text-sm font-semibold text-slate-700" data-testid="goal-minutes">
        {minutes}/{goal}
      </p>
      <p className="text-[11px] leading-tight text-slate-500">min daily goal</p>
    </div>
  )
}
