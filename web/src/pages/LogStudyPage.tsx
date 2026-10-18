import { useState, type FormEvent, type ReactNode } from 'react'
import { useSearchParams } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { listTopicsByCourse } from '../api/courses'
import { triggerRecommendations } from '../api/ml'
import { listStudyLogs, logStudySession } from '../api/studyLogs'
import type { ActivityType } from '../api/types'
import { Button, Card, ErrorMessage, Field, PageHeader, Spinner, inputClass } from '../components/ui'

const DURATIONS = [15, 30, 45, 60, 90]

const ACTIVITIES: { value: ActivityType; label: string }[] = [
  { value: 'reading', label: 'Reading' },
  { value: 'video', label: 'Video' },
  { value: 'practice', label: 'Practice' },
]

export function LogStudyPage() {
  const [params] = useSearchParams()
  const queryClient = useQueryClient()
  const courses = useQuery({ queryKey: ['topicsByCourse'], queryFn: listTopicsByCourse })
  const logs = useQuery({ queryKey: ['studyLogs'], queryFn: () => listStudyLogs(5) })

  const [topicId, setTopicId] = useState(params.get('topic') ?? '')
  const [duration, setDuration] = useState(30)
  const [activity, setActivity] = useState<ActivityType>('reading')

  const save = useMutation({
    mutationFn: () => logStudySession({ topicId, durationMinutes: duration, activityType: activity }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['studyLogs'] })
      queryClient.invalidateQueries({ queryKey: ['dashboard'] })
      triggerRecommendations()
    },
  })

  function handleSubmit(e: FormEvent) {
    e.preventDefault()
    save.mutate()
  }

  if (courses.isPending) return <Spinner />
  if (courses.isError) return <ErrorMessage error={courses.error} />

  return (
    <div className="mx-auto max-w-lg">
      <PageHeader eyebrow="Study log" title="Log a study session">
        Logging your study time helps the system spot topics you may be neglecting.
      </PageHeader>

      <Card>
        <form onSubmit={handleSubmit} className="space-y-5">
          <Field label="Topic">
            <select required className={inputClass} value={topicId} onChange={(e) => setTopicId(e.target.value)}>
              <option value="" disabled>
                Choose a topic
              </option>
              {courses.data.map((c) => (
                <optgroup key={c.id} label={`${c.code}: ${c.title}`}>
                  {c.topics.map((t) => (
                    <option key={t.id} value={t.id}>
                      {t.title}
                    </option>
                  ))}
                </optgroup>
              ))}
            </select>
          </Field>

          <fieldset>
            <legend className="mb-1.5 text-sm font-medium text-slate-700">Duration</legend>
            <div className="flex flex-wrap gap-2">
              {DURATIONS.map((d) => (
                <Chip key={d} selected={duration === d} onClick={() => setDuration(d)}>
                  {d} min
                </Chip>
              ))}
              <input
                type="number"
                min={1}
                max={600}
                aria-label="Minutes"
                className={inputClass.replace('w-full', 'w-24')}
                value={duration}
                onChange={(e) => setDuration(Number(e.target.value))}
              />
            </div>
          </fieldset>

          <fieldset>
            <legend className="mb-1.5 text-sm font-medium text-slate-700">Activity</legend>
            <div className="grid grid-cols-3 gap-2">
              {ACTIVITIES.map((a) => (
                <Chip key={a.value} selected={activity === a.value} onClick={() => setActivity(a.value)}>
                  {a.label}
                </Chip>
              ))}
            </div>
          </fieldset>

          {save.isError && <ErrorMessage error={save.error} />}
          {save.isSuccess && (
            <div className="rounded-xl bg-emerald-50 px-4 py-3 text-sm text-emerald-800 ring-1 ring-emerald-200" role="status">
              Saved: {save.data.duration_minutes} minutes of {save.data.activity_type}.
            </div>
          )}
          <Button type="submit" className="w-full" disabled={save.isPending || !topicId || duration < 1}>
            {save.isPending ? 'Saving…' : 'Save session'}
          </Button>
        </form>
      </Card>

      {logs.data && logs.data.length > 0 && (
        <section className="mt-8">
          <h2 className="mb-3 text-sm font-semibold tracking-wide text-slate-500 uppercase">Recent sessions</h2>
          <ul className="grid gap-2">
            {logs.data.map((log) => (
              <li key={log.id} className="flex items-center justify-between gap-3 rounded-xl bg-white px-4 py-3 text-sm ring-1 ring-slate-200">
                <span className="min-w-0 truncate font-medium">{log.topic_title}</span>
                <span className="shrink-0 text-slate-500">
                  {log.duration_minutes} min · {log.activity_type} · {new Date(log.logged_at).toLocaleDateString()}
                </span>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  )
}

function Chip({ selected, onClick, children }: { selected: boolean; onClick: () => void; children: ReactNode }) {
  return (
    <button
      type="button"
      aria-pressed={selected}
      onClick={onClick}
      className={`rounded-xl px-3.5 py-2 text-sm font-medium ring-1 transition ${
        selected ? 'bg-brand-50 text-brand-700 ring-2 ring-brand-600' : 'bg-white text-slate-700 ring-slate-300 hover:ring-slate-400'
      }`}
    >
      {children}
    </button>
  )
}
