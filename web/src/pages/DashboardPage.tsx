import { useEffect, useMemo } from 'react'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { getDashboardData } from '../api/dashboard'
import { generateReminders, getTopicProgress } from '../api/notifications'
import { getProfile } from '../api/profile'
import { listRecommendations } from '../api/recommendations'
import { ConsistencyCard } from '../components/dashboard/ConsistencyCard'
import { ProgressCard } from '../components/dashboard/ProgressCard'
import { RecommendationsCard } from '../components/dashboard/RecommendationsCard'
import { RemindersCard } from '../components/dashboard/RemindersCard'
import { WeeklySummaryCard } from '../components/dashboard/WeeklySummaryCard'
import { ErrorMessage, PageHeader, Spinner } from '../components/ui'
import { buildReminders } from '../lib/reminders'
import { weeklySummary } from '../lib/weekly'

const WEEK_MS = 7 * 86_400_000

export function DashboardPage() {
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const dashboard = useQuery({ queryKey: ['dashboard'], queryFn: getDashboardData, staleTime: 0 })
  const recommendations = useQuery({ queryKey: ['recommendations'], queryFn: listRecommendations, staleTime: 0 })
  const progress = useQuery({ queryKey: ['topicProgress'], queryFn: getTopicProgress, staleTime: 0 })
  const queryClient = useQueryClient()

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
    const minutesThisWeek = studyLogs
      .filter((l) => now.getTime() - new Date(l.logged_at).getTime() < WEEK_MS)
      .reduce((sum, l) => sum + l.duration_minutes, 0)
    const reminders = buildReminders({
      now,
      studyLogs,
      topicScores,
      topics: courses.flatMap((c) => c.topics),
      coursesWithoutDiagnostic: courses
        .filter((c) => !c.diagnostic_taken && c.diagnostic_quiz_id)
        .map((c) => ({ code: c.code, diagnostic_quiz_id: c.diagnostic_quiz_id as string })),
    })
    const titles = new Map(courses.flatMap((c) => c.topics.map((t) => [t.id, t.title] as const)))
    const weekly = weeklySummary({ now, studyLogs, progress: progress.data ?? [], titles })
    return { minutesThisWeek, reminders, weekly }
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

      <RecommendationsCard recommendations={recommendations.data} />

      <div className="grid gap-5 lg:grid-cols-5">
        <div className="lg:col-span-2">
          <ConsistencyCard timestamps={dashboard.data.activityTimestamps} minutesThisWeek={derived?.minutesThisWeek ?? 0} />
        </div>
        <div className="lg:col-span-3">
          <ProgressCard courses={dashboard.data.courses} />
        </div>
      </div>
    </div>
  )
}
