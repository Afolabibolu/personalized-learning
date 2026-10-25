import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { refreshRecommendations } from '../../api/ml'
import { setRecommendationStatus, type Explanation, type Recommendation } from '../../api/recommendations'
import { formatDate, percent } from '../../lib/format'
import { ATTENTION_PROBABILITY } from '../../lib/suggestions'
import { PREFERENCE_PHRASE } from '../PreferencePicker'
import { RESOURCE_LABEL, ResourceIcon } from '../ResourceList'
import { Button, Card } from '../ui'

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
function sortRecommendations(recs: Recommendation[]): Recommendation[] {
  const group: Record<Kind, number> = { attention: 0, 'getting-started': 1, 'keep-it-up': 2 }
  return [...recs].sort(
    (a, b) =>
      group[kindOf(a)] - group[kindOf(b)] ||
      (b.priority_score ?? 0) - (a.priority_score ?? 0) ||
      a.topic.course.code.localeCompare(b.topic.course.code) ||
      a.rank - b.rank,
  )
}

function targetLabel(rec: Recommendation): string | null {
  if (rec.resource) {
    const label = RESOURCE_LABEL[rec.resource.type]
    return rec.resource.title.startsWith(label) ? rec.resource.title : `${label}: ${rec.resource.title}`
  }
  if (rec.quiz) return `Take the ${rec.quiz.title}`
  return null
}

export function RecommendationsCard({ recommendations }: { recommendations: Recommendation[] }) {
  const queryClient = useQueryClient()
  const refresh = useMutation({
    mutationFn: refreshRecommendations,
    onSettled: () => queryClient.invalidateQueries({ queryKey: ['recommendations'] }),
  })

  const pending = sortRecommendations(recommendations.filter((r) => r.status === 'pending'))
  const history = recommendations.filter((r) => r.status !== 'pending')

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
        // The saved list below stays usable; this is a quiet notice, not an error screen (NFR4).
        <p className="border-b border-amber-100 bg-amber-50 px-5 py-2 text-xs text-amber-800" role="status" data-testid="ml-offline-notice">
          Recommendations will update shortly. Showing your last saved list.
        </p>
      )}

      {pending.length === 0 ? (
        <p className="px-5 py-8 text-center text-sm text-slate-500">
          Nothing to work on right now. Take a quiz or log a study session, then press Refresh.
        </p>
      ) : (
        <ul className="divide-y divide-slate-100">
          {pending.map((rec) => (
            <RecommendationRow key={rec.id} rec={rec} />
          ))}
        </ul>
      )}

      {history.length > 0 && <History items={history} />}
    </Card>
  )
}

function RecommendationRow({ rec }: { rec: Recommendation }) {
  const queryClient = useQueryClient()
  const navigate = useNavigate()
  const [showWhy, setShowWhy] = useState(false)
  const kind = kindOf(rec)
  const style = KIND_STYLE[kind]
  const explanation = rec.explanation

  const update = useMutation({
    mutationFn: (status: 'accepted' | 'dismissed') => setRecommendationStatus(rec.id, status),
    onSuccess: (_data, status) => {
      queryClient.setQueryData<Recommendation[]>(['recommendations'], (prev) =>
        prev?.map((r) => (r.id === rec.id ? { ...r, status } : r)),
      )
      if (status === 'accepted') {
        if (rec.resource && !rec.resource.url) navigate(`/resources/${rec.resource.id}`)
        else if (!rec.resource && rec.quiz) navigate(`/quiz/${rec.quiz.id}`)
      }
    },
  })

  function accept() {
    // Open external links straight from the click, so the browser does not block the new tab.
    if (rec.resource?.url) window.open(rec.resource.url, '_blank', 'noopener')
    update.mutate('accepted')
  }

  return (
    <li className="relative px-5 py-4" data-testid="recommendation" data-kind={kind} data-id={rec.id}>
      <span className={`absolute top-4 bottom-4 left-0 w-1 rounded-r ${style.accent}`} />
      <div className="flex flex-wrap items-center gap-2">
        <span className={`rounded-full px-2.5 py-0.5 text-xs font-semibold ring-1 ${style.badge}`}>{style.label}</span>
        <span className="text-xs text-slate-500">
          {rec.topic.course.code}
          {kind === 'attention' && rec.priority_score !== null && ` · ${percent(rec.priority_score)} likely to need work`}
        </span>
      </div>
      <Link to={`/topics/${rec.topic.id}`} className="mt-1.5 block font-semibold hover:text-brand-700" data-testid="recommendation-topic">
        {rec.topic.title}
      </Link>
      <p className="mt-0.5 text-sm text-slate-600">{targetLabel(rec)}</p>
      {explanation?.matched_preference && explanation.matched_preference in PREFERENCE_PHRASE && (
        <p className="mt-1 flex items-center gap-1 text-xs font-medium text-brand-700" data-testid="matched-preference">
          <span aria-hidden>✓</span> Matched to your preference: {PREFERENCE_PHRASE[explanation.matched_preference as keyof typeof PREFERENCE_PHRASE]}
        </p>
      )}

      {explanation && (
        <p
          className={`mt-2 rounded-lg px-3 py-2 text-sm ${
            kind === 'keep-it-up' ? 'bg-emerald-50/60 text-emerald-900' : kind === 'attention' ? 'bg-red-50/60 text-red-900' : 'bg-brand-50/60 text-brand-900'
          }`}
          data-testid="recommendation-reason"
        >
          {explanation.reason}
          {kind === 'getting-started' && <span className="block text-xs opacity-80">Take a few quizzes so we can personalise this for you.</span>}
        </p>
      )}

      {explanation?.also && explanation.also.length > 0 && <AlsoRecommended items={explanation.also} />}

      <div className="mt-3 flex flex-wrap items-center gap-2">
        <Button className="px-3 py-1.5" onClick={accept} disabled={update.isPending}>
          Accept and open
        </Button>
        <Button variant="ghost" className="px-3 py-1.5" onClick={() => update.mutate('dismissed')} disabled={update.isPending}>
          Dismiss
        </Button>
        {explanation?.probabilities && (
          <button
            onClick={() => setShowWhy((v) => !v)}
            aria-expanded={showWhy}
            className="ml-auto text-sm font-semibold text-brand-600 hover:text-brand-700"
          >
            {showWhy ? 'Hide details' : 'Why this?'}
          </button>
        )}
      </div>
      {update.isError && <p className="mt-2 text-xs text-red-600">Could not save that. Try again.</p>}
      {showWhy && explanation?.probabilities && <WhyPanel explanation={explanation} />}
    </li>
  )
}

function WhyPanel({ explanation }: { explanation: Explanation }) {
  const p = explanation.probabilities!
  const rows = [
    { label: 'Logistic Regression', value: p.logistic_regression },
    { label: 'Random Forest', value: p.random_forest },
    { label: 'Average (used to rank)', value: p.average, strong: true },
  ]
  return (
    <div className="mt-3 rounded-xl bg-slate-50 p-4 text-sm" data-testid="why-panel">
      <p className="mb-2 text-xs font-semibold tracking-wide text-slate-500 uppercase">Chance this topic needs attention</p>
      <div className="grid gap-2">
        {rows.map((r) => (
          <div key={r.label} className="grid grid-cols-[7.5rem_1fr_2.5rem] sm:grid-cols-[11rem_1fr_3rem] items-center gap-2">
            <span className={r.strong ? 'font-semibold' : 'text-slate-600'}>{r.label}</span>
            <span className="h-2 overflow-hidden rounded-full bg-slate-200">
              <span className={`block h-full rounded-full ${r.strong ? 'bg-brand-600' : 'bg-slate-400'}`} style={{ width: `${r.value * 100}%` }} />
            </span>
            <span className={`text-right tabular-nums ${r.strong ? 'font-semibold' : 'text-slate-600'}`}>{percent(r.value)}</span>
          </div>
        ))}
      </div>
      {explanation.top_factors.length > 0 && (
        <>
          <p className="mt-4 mb-2 text-xs font-semibold tracking-wide text-slate-500 uppercase">What drove it</p>
          <ul className="grid gap-1">
            {explanation.top_factors.map((f) => (
              <li key={f.feature} className="flex items-center justify-between gap-3">
                <span>
                  {f.label}: <span className="font-medium">{factorValue(f.feature, f.value)}</span>
                </span>
                <span className={`text-xs font-semibold ${f.direction === 'raises risk' ? 'text-red-600' : 'text-emerald-600'}`}>
                  {f.direction === 'raises risk' ? '▲ raises risk' : '▼ lowers risk'}
                </span>
              </li>
            ))}
          </ul>
        </>
      )}
      <p className="mt-3 text-xs text-slate-500">Models trained on simulated students; factors from the Logistic Regression model.</p>
    </div>
  )
}

function factorValue(feature: string, value: number): string {
  if (feature.endsWith('_score')) return `${Math.round(value)}%`
  if (feature === 'days_since_last_studied') return value >= 60 ? 'never studied' : `${Math.round(value)} days`
  if (feature === 'total_minutes') return `${Math.round(value)} min`
  return String(Math.round(value))
}

function History({ items }: { items: Recommendation[] }) {
  const [open, setOpen] = useState(false)
  return (
    <div className="border-t border-slate-100">
      <button
        onClick={() => setOpen((v) => !v)}
        aria-expanded={open}
        className="flex w-full items-center justify-between px-5 py-3 text-sm font-semibold text-slate-600 hover:bg-slate-50"
      >
        History ({items.length})
        <span aria-hidden>{open ? '▴' : '▾'}</span>
      </button>
      {open && (
        <ul className="divide-y divide-slate-100 pb-2" data-testid="recommendation-history">
          {items.map((rec) => (
            <li key={rec.id} className="flex items-center justify-between gap-3 px-5 py-2.5 text-sm">
              <span className="min-w-0">
                <span className="block truncate font-medium">{rec.topic.title}</span>
                <span className="block truncate text-xs text-slate-500">
                  {targetLabel(rec)} · {formatDate(rec.created_at)}
                </span>
              </span>
              <span
                className={`shrink-0 rounded-full px-2 py-0.5 text-xs font-semibold ${
                  rec.status === 'accepted' ? 'bg-emerald-50 text-emerald-700' : 'bg-slate-100 text-slate-500'
                }`}
              >
                {rec.status === 'accepted' ? 'Accepted' : 'Dismissed'}
              </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

function RefreshIcon({ spinning }: { spinning: boolean }) {
  return (
    <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.8" className={`h-4 w-4 ${spinning ? 'animate-spin' : ''}`} aria-hidden>
      <path d="M16 10a6 6 0 1 1-1.8-4.3M16 3.5v3.2h-3.2" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  )
}

/** A video and a textbook for the same topic: videos open on YouTube, textbooks as a reading card. */
function AlsoRecommended({ items }: { items: NonNullable<Explanation['also']> }) {
  return (
    <div className="mt-2" data-testid="also-recommended">
      <p className="text-xs font-semibold tracking-wide text-slate-500 uppercase">Also recommended</p>
      <ul className="-mx-2 mt-1 grid gap-0.5">
        {items.map((item) => {
          const body = (
            <>
              <ResourceIcon type={item.type} className="h-7 w-7" />
              <span className="min-w-0 flex-1 text-sm leading-snug">
                <span className="font-medium">{item.type === 'video' ? 'Video' : 'Textbook'}:</span>{' '}
                {item.title.replace(/^(Video|Textbook): /, '')}
              </span>
            </>
          )
          const style = 'flex items-center gap-2.5 rounded-lg p-1.5 transition hover:bg-slate-50'
          return (
            <li key={item.resource_id}>
              {item.url ? (
                <a href={item.url} target="_blank" rel="noreferrer" className={style} data-testid="also-link">
                  {body}
                </a>
              ) : (
                <Link to={`/resources/${item.resource_id}`} className={style} data-testid="also-link">
                  {body}
                </Link>
              )}
            </li>
          )
        })}
      </ul>
    </div>
  )
}
