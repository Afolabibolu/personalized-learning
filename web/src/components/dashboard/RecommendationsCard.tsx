import { Link } from 'react-router-dom'
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { refreshRecommendations } from '../../api/ml'
import { setRecommendationStatus, type Recommendation } from '../../api/recommendations'
import { daysBetween } from '../../lib/consistency'
import { ATTENTION_PROBABILITY, keepItUpSuggestion } from '../../lib/suggestions'
import { Button, Card, ErrorMessage } from '../ui'

type Kind = 'attention' | 'getting-started' | 'keep-it-up'

function kindOf(rec: Recommendation): Kind {
  if (rec.source === 'cold_start') return 'getting-started'
  return (rec.priority_score ?? 0) >= ATTENTION_PROBABILITY ? 'attention' : 'keep-it-up'
}

const KIND_STYLE: Record<Kind, { label: string; badge: string; accent: string }> = {
  attention: { label: 'Needs attention', badge: 'bg-red-50 text-red-700 ring-red-200', accent: 'bg-red-500' },
  'getting-started': { label: 'Getting started', badge: 'bg-brand-50 text-brand-700 ring-brand-100', accent: 'bg-brand-500' },
  'keep-it-up': { label: 'Keep it up', badge: 'bg-emerald-50 text-emerald-700 ring-emerald-200', accent: 'bg-emerald-500' },
}

/** Needs attention (highest probability first), then getting started in order, then keep it up. */
export function sortRecommendations(recs: Recommendation[]): Recommendation[] {
  const group: Record<Kind, number> = { attention: 0, 'getting-started': 1, 'keep-it-up': 2 }
  return [...recs].sort(
    (a, b) =>
      group[kindOf(a)] - group[kindOf(b)] ||
      (b.priority_score ?? 0) - (a.priority_score ?? 0) ||
      a.topic.course.code.localeCompare(b.topic.course.code) ||
      a.rank - b.rank,
  )
}

export function RecommendationsCard({
  recommendations,
  topicScores,
  lastStudied,
}: {
  recommendations: Recommendation[]
  topicScores: Map<string, number>
  lastStudied: Map<string, Date>
}) {
  const queryClient = useQueryClient()
  const refresh = useMutation({
    mutationFn: refreshRecommendations,
    onSettled: () => queryClient.invalidateQueries({ queryKey: ['recommendations'] }),
  })

  const sorted = sortRecommendations(recommendations)
  const now = new Date()

  return (
    <Card className="p-0">
      <div className="flex items-center justify-between gap-3 border-b border-slate-100 px-5 py-4">
        <div>
          <h2 className="font-semibold">Recommended for you</h2>
          <p className="text-xs text-slate-500">Based on your quiz scores and study history</p>
        </div>
        <Button variant="secondary" onClick={() => refresh.mutate()} disabled={refresh.isPending} className="shrink-0 px-3 py-2">
          <RefreshIcon spinning={refresh.isPending} />
          <span className="hidden sm:inline">{refresh.isPending ? 'Refreshing…' : 'Refresh recommendations'}</span>
          <span className="sm:hidden">Refresh</span>
        </Button>
      </div>

      {refresh.isError && (
        <div className="px-5 pt-4">
          <ErrorMessage error={new Error('Could not reach the recommendation service. Is it running on port 8000?')} />
        </div>
      )}

      {sorted.length === 0 ? (
        <p className="px-5 py-8 text-center text-sm text-slate-500">
          No recommendations yet. Take a diagnostic quiz, then press Refresh.
        </p>
      ) : (
        <ul className="divide-y divide-slate-100">
          {sorted.map((rec) => {
            const studied = lastStudied.get(rec.topic.id)
            return (
              <RecommendationRow
                key={rec.id}
                rec={rec}
                suggestion={
                  kindOf(rec) === 'keep-it-up'
                    ? keepItUpSuggestion({
                        latestScore: topicScores.get(rec.topic.id) ?? null,
                        daysSinceStudied: studied ? daysBetween(studied, now) : null,
                        hasTopicQuiz: Boolean(rec.topic_quiz_id),
                      })
                    : null
                }
              />
            )
          })}
        </ul>
      )}
    </Card>
  )
}

function RecommendationRow({ rec, suggestion }: { rec: Recommendation; suggestion: string | null }) {
  const queryClient = useQueryClient()
  const kind = kindOf(rec)
  const style = KIND_STYLE[kind]

  const update = useMutation({
    mutationFn: (status: 'accepted' | 'dismissed') => setRecommendationStatus(rec.id, status),
    onSuccess: (_data, status) =>
      queryClient.setQueryData<Recommendation[]>(['recommendations'], (prev) =>
        status === 'dismissed'
          ? prev?.filter((r) => r.id !== rec.id)
          : prev?.map((r) => (r.id === rec.id ? { ...r, status: 'accepted' } : r)),
      ),
  })

  const resourceAvailable = rec.resource && /^https?:\/\//.test(rec.resource.url)
  const accepted = rec.status === 'accepted'

  return (
    <li className="relative px-5 py-4" data-testid="recommendation" data-kind={kind}>
      <span className={`absolute top-4 bottom-4 left-0 w-1 rounded-r ${style.accent}`} />
      <div className="flex flex-wrap items-center gap-2">
        <span className={`rounded-full px-2.5 py-0.5 text-xs font-semibold ring-1 ${style.badge}`}>{style.label}</span>
        <span className="text-xs text-slate-500">
          {rec.topic.course.code}
          {kind === 'attention' && rec.priority_score !== null && ` · ${Math.round(rec.priority_score * 100)}% likely to need work`}
        </span>
      </div>
      <Link to={`/topics/${rec.topic.id}`} className="mt-1.5 block font-semibold hover:text-brand-700" data-testid="recommendation-topic">
        {rec.topic.title}
      </Link>
      <p className="mt-0.5 text-sm text-slate-600">
        {rec.resource ? rec.resource.title : rec.quiz ? `Take the ${rec.quiz.title}` : null}
      </p>
      {suggestion && <p className="mt-2 rounded-lg bg-emerald-50/60 px-3 py-2 text-sm text-emerald-900">{suggestion}</p>}

      <div className="mt-3 flex flex-wrap items-center gap-2">
        {accepted ? (
          <>
            <span className="text-sm font-medium text-emerald-700">✓ Accepted</span>
            {rec.resource && resourceAvailable && (
              <a href={rec.resource.url} target="_blank" rel="noreferrer" className="text-sm font-semibold text-brand-600 hover:text-brand-700">
                Open resource →
              </a>
            )}
            {rec.quiz && (
              <Link to={`/quiz/${rec.quiz.id}`} className="text-sm font-semibold text-brand-600 hover:text-brand-700">
                Start quiz →
              </Link>
            )}
            {rec.resource && !resourceAvailable && <span className="text-xs text-slate-500">Link coming soon</span>}
          </>
        ) : (
          <>
            <Button className="px-3 py-1.5" onClick={() => update.mutate('accepted')} disabled={update.isPending}>
              Accept
            </Button>
            <Button variant="ghost" className="px-3 py-1.5" onClick={() => update.mutate('dismissed')} disabled={update.isPending}>
              Dismiss
            </Button>
          </>
        )}
      </div>
      {update.isError && (
        <div className="mt-2">
          <ErrorMessage error={update.error} />
        </div>
      )}
    </li>
  )
}

function RefreshIcon({ spinning }: { spinning: boolean }) {
  return (
    <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.8" className={`h-4 w-4 ${spinning ? 'animate-spin' : ''}`} aria-hidden>
      <path d="M16 10a6 6 0 1 1-1.8-4.3M16 3.5v3.2h-3.2" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  )
}
