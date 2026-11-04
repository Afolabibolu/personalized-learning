import { useEffect, useMemo, useRef } from 'react'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { getDashboardData } from '../api/dashboard'
import { getGamification } from '../api/gamification'
import { generateReminders, getTopicProgress } from '../api/notifications'
import { getProfile } from '../api/profile'
import { getColdStartThreshold, listRecommendations, refreshFallbackRecommendations } from '../api/recommendations'
import { ProgressCard } from '../components/dashboard/ProgressCard'
import { RecommendationsCard } from '../components/dashboard/RecommendationsCard'
import { RemindersCard } from '../components/dashboard/RemindersCard'
import { StreakCard } from '../components/dashboard/StreakCard'
import { WeeklySummaryCard } from '../components/dashboard/WeeklySummaryCard'
import { ErrorMessage, PageHeader, Spinner } from '../components/ui'
import { buildReminders } from '../lib/reminders'
import { weeklySummary } from '../lib/weekly'

export function DashboardPage() {
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const dashboard = useQuery({ queryKey: ['dashboard'], queryFn: getDashboardData, staleTime: 0 })
  const recommendations = useQuery({ queryKey: ['recommendations'], queryFn: listRecommendations, staleTime: 0 })
  const progress = useQuery({ queryKey: ['topicProgress'], queryFn: getTopicProgress, staleTime: 0 })
  const threshold = useQuery({ queryKey: ['coldStartThreshold'], queryFn: getColdStartThreshold, staleTime: Infinity })
  const gamification = useQuery({ queryKey: ['gamification'], queryFn: getGamification, staleTime: 30_000 })
  const queryClient = useQueryClient()

  // Never an empty list (NFR4): if nothing is pending (say the ML service was down when the
  // student signed up or finished a diagnostic), the database writes the Stage 1 or 2 lists.
  const fallbackTried = useRef(false)
  useEffect(() => {
    if (!recommendations.data || fallbackTried.current) return
    if (recommendations.data.some((r) => r.status === 'pending')) return
    fallbackTried.current = true
    refreshFallbackRecommendations()
      .then((written) => {
        if (written > 0) queryClient.invalidateQueries({ queryKey: ['recommendations'] })
      })
      .catch((e) => console.warn('Fallback recommendations not written:', e))
  }, [recommendations.data, queryClient])

  // Reminders are computed from stored dates each time the dashboard loads (at most one of each kind a day).
  useEffect(() => {
    generateReminders()
      .then(() => queryClient.invalidateQueries({ queryKey: ['notifications'] }))
      .catch((e) => console.warn('Reminders not generated:', e))
  }, [queryClient])

  const derived = useMemo(() => {
    if (!dashboard.data) return null
    const { studyLogs, topicScores, courses } = dashboard.data
    const now = new Date()
    const reminders = buildReminders({
      now,
      studyLogs,
      topicScores,
      topics: courses.flatMap((c) => c.topics),
    })
    // Stage 1 courses: the recommendations card asks for their diagnostic.
    const diagnosticPrompts = courses
      .filter((c) => !c.diagnostic_taken && c.diagnostic_quiz_id)
      .map((c) => ({ code: c.code, diagnostic_quiz_id: c.diagnostic_quiz_id as string }))
    const titles = new Map(courses.flatMap((c) => c.topics.map((t) => [t.id, t.title] as const)))
    const weekly = weeklySummary({ now, studyLogs, progress: progress.data ?? [], titles })
    return { reminders, weekly, diagnosticPrompts }
  }, [dashboard.data, progress.data])

  const firstName = profile.data?.full_name?.split(' ')[0]

  if (dashboard.isPending || recommendations.isPending) return <Spinner />
  if (dashboard.isError) return <ErrorMessage error={dashboard.error} />
  if (recommendations.isError) return <ErrorMessage error={recommendations.error} />

  return (
    <div className="grid gap-5">
      <PageHeader eyebrow="Dashboard" title={firstName ? `Hi ${firstName}` : 'Hi there'}>
        Here is where to focus next.
      </PageHeader>

      {derived && <RemindersCard reminders={derived.reminders} />}

      {derived && <WeeklySummaryCard summary={derived.weekly} recommendations={recommendations.data} />}

      <RecommendationsCard
        recommendations={recommendations.data}
        diagnosticPrompts={derived?.diagnosticPrompts}
        threshold={threshold.data}
      />

      <div className="grid gap-5 lg:grid-cols-5">
        <div className="lg:col-span-2">
          {gamification.data && <StreakCard g={gamification.data} />}
        </div>
        <div className="lg:col-span-3">
          <ProgressCard courses={dashboard.data.courses} />
        </div>
      </div>
    </div>
  )
}
