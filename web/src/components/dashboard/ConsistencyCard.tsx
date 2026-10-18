import { activityDays, activityStrip, currentStreak } from '../../lib/consistency'
import { Card } from '../ui'

export function ConsistencyCard({ timestamps, minutesThisWeek }: { timestamps: string[]; minutesThisWeek: number }) {
  const today = new Date()
  const days = activityDays(timestamps)
  const streak = currentStreak(days, today)
  const strip = activityStrip(days, today)
  const activeDays = strip.filter((d) => d.active).length

  return (
    <Card>
      <h2 className="font-semibold">Consistency</h2>
      <div className="mt-3 grid grid-cols-3 gap-3">
        <Stat value={streak} label="day streak" testId="streak" />
        <Stat value={activeDays} label="active days (14)" />
        <Stat value={minutesThisWeek} label="minutes, 7 days" />
      </div>
      <div className="mt-5">
        <p className="mb-2 text-xs text-slate-500">Last 14 days (quizzes and study sessions)</p>
        <ol className="grid grid-cols-14 gap-1" data-testid="activity-strip">
          {strip.map((d) => (
            <li key={d.key} className="flex flex-col items-center gap-1" title={`${d.key}${d.active ? ': active' : ''}`}>
              <span
                className={`aspect-square w-full rounded-md ${d.active ? 'bg-brand-600' : 'bg-slate-200'} ${
                  d.isToday ? 'ring-2 ring-brand-300 ring-offset-1' : ''
                }`}
                data-active={d.active}
              />
              <span className="text-[10px] text-slate-400">{d.weekday}</span>
            </li>
          ))}
        </ol>
      </div>
    </Card>
  )
}

function Stat({ value, label, testId }: { value: number; label: string; testId?: string }) {
  return (
    <div className="rounded-xl bg-slate-50 px-3 py-2.5 text-center">
      <p className="text-2xl font-bold text-slate-900" data-testid={testId}>
        {value}
      </p>
      <p className="text-[11px] leading-tight text-slate-500">{label}</p>
    </div>
  )
}
