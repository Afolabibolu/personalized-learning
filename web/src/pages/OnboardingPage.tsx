import { useState, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { listCourses, setEnrolled } from '../api/courses'
import { getProfile, updateProfile } from '../api/profile'
import type { LearningPreference, Level } from '../api/types'
import { LevelTabs } from '../components/LevelTabs'
import { PreferencePicker } from '../components/PreferencePicker'
import { EmailSettings } from '../components/EmailSettings'
import { Button, Card, ErrorMessage, Field, PageHeader, Spinner, inputClass } from '../components/ui'

const LEVELS: Level[] = [100, 200, 300, 400, 500]

export function OnboardingPage() {
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const courses = useQuery({ queryKey: ['courses'], queryFn: listCourses })

  const [department, setDepartment] = useState('Computer Science')
  const [level, setLevel] = useState<Level>(500)
  const [preferences, setPreferences] = useState<LearningPreference[]>([])
  // Asked once here; existing students start with email off. All three kinds are on if they say yes.
  const [email, setEmail] = useState({ email_reminders: false, email_streak: true, email_digest: true, email_weekly: true })
  // The course list opens on the student's level; null until they pick another tab.
  const [shownLevel, setShownLevel] = useState<Level | null>(null)
  // Starts as the courses every new account gets (the reviewed ones); null until changed.
  const [chosen, setChosen] = useState<Set<string> | null>(null)
  const selected = chosen ?? new Set(courses.data?.filter((c) => c.enrolled).map((c) => c.id))

  function toggleCourse(id: string) {
    const next = new Set(selected)
    if (next.has(id)) next.delete(id)
    else next.add(id)
    setChosen(next)
  }

  const save = useMutation({
    mutationFn: async () => {
      await updateProfile({ department: department.trim(), level, learning_preferences: preferences, ...email })
      const changes = (courses.data ?? []).filter((c) => c.enrolled !== selected.has(c.id))
      await Promise.all(changes.map((c) => setEnrolled(c.id, selected.has(c.id))))
    },
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['profile'] })
      await queryClient.invalidateQueries({ queryKey: ['courses'] })
      navigate('/')
    },
  })

  function handleSubmit(e: FormEvent) {
    e.preventDefault()
    save.mutate()
  }

  if (profile.isPending || courses.isPending) return <Spinner />

  const firstName = profile.data?.full_name?.split(' ')[0]
  const showing = shownLevel ?? level
  const shown = (courses.data ?? []).filter((c) => c.level === showing)
  const picked = (courses.data ?? []).filter((c) => selected.has(c.id))

  return (
    <div className="mx-auto max-w-lg">
      <PageHeader eyebrow="Step 1 of 2" title={firstName ? `Welcome, ${firstName}` : 'Welcome'}>
        Tell us a little about yourself. Next, a short diagnostic quiz shows which topics need attention.
      </PageHeader>
      <Card>
        <form onSubmit={handleSubmit} className="space-y-5">
          <Field label="Department">
            <input required className={inputClass} value={department} onChange={(e) => setDepartment(e.target.value)} />
          </Field>

          <Field label="Level">
            <select className={inputClass} value={level} onChange={(e) => {
                setLevel(Number(e.target.value) as Level)
                setShownLevel(null)
              }}>
              {LEVELS.map((l) => (
                <option key={l} value={l}>
                  {l} level
                </option>
              ))}
            </select>
          </Field>

          <PreferencePicker value={preferences} onChange={setPreferences} />

          {courses.data && courses.data.length > 0 && (
            <fieldset>
              <legend className="mb-1.5 text-sm font-medium text-slate-700">Your courses</legend>
              <p className="mb-2 text-xs text-slate-500">Recommendations and reminders cover these. You can change them later on the Courses page.</p>
              <div className="mb-2">
                <LevelTabs
                  label="Show courses for"
                  value={showing}
                  onChange={setShownLevel}
                  options={LEVELS.map((l) => ({
                    value: l,
                    label: `${l}`,
                    count: courses.data.filter((c) => c.level === l).length,
                  }))}
                />
              </div>
              <div className="grid max-h-64 gap-1.5 overflow-y-auto rounded-xl p-0.5">
                {shown.map((c) => (
                  <label key={c.id} className="flex cursor-pointer items-start gap-3 rounded-xl px-3 py-2 ring-1 ring-slate-200 has-[:checked]:bg-brand-50 has-[:checked]:ring-brand-500">
                    <input type="checkbox" className="mt-0.5 accent-brand-600" checked={selected.has(c.id)} onChange={() => toggleCourse(c.id)} />
                    <span className="text-sm">
                      <span className="font-semibold">{c.code}</span> {c.title}
                      {!c.is_reviewed && <span className="block text-xs text-amber-700">Sample content, pending lecturer review</span>}
                    </span>
                  </label>
                ))}
                {shown.length === 0 && <p className="px-1 py-2 text-sm text-slate-500">No {showing} level courses yet.</p>}
              </div>
              <p className="mt-2 text-xs text-slate-500" data-testid="picked-courses">
                {picked.length === 0
                  ? 'No courses chosen yet.'
                  : `${picked.length} chosen: ${picked.map((c) => c.code).join(', ')}`}
              </p>
            </fieldset>
          )}

          <div>
            <EmailSettings value={email} onChange={setEmail} compact />
            <p className="mt-1.5 text-xs text-slate-500">Reminders like a streak at risk or your weekly summary. You can pick which ones on your Profile page.</p>
          </div>

          {save.isError && <ErrorMessage error={save.error} />}
          <Button type="submit" className="w-full" disabled={save.isPending}>
            {save.isPending ? 'Saving…' : 'Continue'}
          </Button>
        </form>
      </Card>
    </div>
  )
}
