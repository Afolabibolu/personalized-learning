import { Link } from 'react-router-dom'
import type { Recommendation } from '../../api/recommendations'
import { ATTENTION_PROBABILITY } from '../../lib/suggestions'
import type { WeeklySummary } from '../../lib/weekly'
import { Card } from '../ui'

/** The topic to work on next: the most likely "needs attention", else the first getting-started item. */
function nextTopic(recs: Recommendation[]): Recommendation | null {
  const pending = recs.filter((r) => r.status === 'pending')
  const attention = pending
    .filter((r) => r.source === 'ml' && (r.priority_score ?? 0) >= ATTENTION_PROBABILITY)
    .sort((a, b) => (b.priority_score ?? 0) - (a.priority_score ?? 0))
  return attention[0] ?? pending.find((r) => r.source === 'cold_start') ?? null
}

export function WeeklySummaryCard({ summary, recommendations }: { summary: WeeklySummary; recommendations: Recommendation[] }) {
  const { minutesThisWeek: now, minutesLastWeek: before, improved } = summary
  const diff = now - before
  const next = nextTopic(recommendations)

  return (
    <Card className="grid gap-4 sm:grid-cols-3" >
      <div data-testid="weekly-minutes">
        <p className="text-xs font-semibold tracking-wide text-slate-500 uppercase">This week</p>
        <p className="mt-1 text-2xl font-bold">
          {now} <span className="text-base font-medium text-slate-500">min</span>
        </p>
        <p className={`text-xs font-medium ${diff > 0 ? 'text-emerald-600' : diff < 0 ? 'text-amber-600' : 'text-slate-500'}`}>
          {before === 0 && now === 0
            ? 'No study logged in the last two weeks'
            : diff === 0
              ? `Same as last week (${before} min)`
              : `${diff > 0 ? '▲' : '▼'} ${Math.abs(diff)} min vs last week (${before} min)`}
        </p>
      </div>

      <div data-testid="weekly-improved">
        <p className="text-xs font-semibold tracking-wide text-slate-500 uppercase">Topics improved</p>
        {improved.length === 0 ? (
          <p className="mt-1 text-sm text-slate-500">None this week yet. Retake a topic quiz to see your progress.</p>
        ) : (
          <ul className="mt-1 grid gap-0.5">
            {improved.slice(0, 2).map((t) => (
              <li key={t.topic_id} className="text-sm">
                <Link to={`/topics/${t.topic_id}`} className="font-medium hover:text-brand-700">
                  {t.title}
                </Link>
                <span className="text-emerald-600">
                  {' '}
                  {Math.round(t.from)}% → {Math.round(t.to)}%
                </span>
              </li>
            ))}
            {improved.length > 2 && <li className="text-xs text-slate-500">and {improved.length - 2} more</li>}
          </ul>
        )}
      </div>

      <div data-testid="weekly-next">
        <p className="text-xs font-semibold tracking-wide text-slate-500 uppercase">Focus next</p>
        {next ? (
          <>
            <Link to={`/topics/${next.topic.id}`} className="mt-1 block text-sm font-semibold hover:text-brand-700">
              {next.topic.title}
            </Link>
            <p className="text-xs text-slate-500">
              {next.topic.course.code}
              {next.source === 'ml' && next.priority_score !== null ? ` · ${Math.round(next.priority_score * 100)}% likely to need work` : ' · Getting started'}
            </p>
          </>
        ) : (
          <p className="mt-1 text-sm text-slate-500">Take a diagnostic quiz to get a focus topic.</p>
        )}
      </div>
    </Card>
  )
}
