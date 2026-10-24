import { useState, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { listCourses, setEnrolled } from '../api/courses'
import { getProfile, updateProfile } from '../api/profile'
import type { LearningPreference, Level } from '../api/types'
import { PreferencePicker } from '../components/PreferencePicker'
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
      await updateProfile({ department: department.trim(), level, learning_preferences: preferences })
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
            <select className={inputClass} value={level} onChange={(e) => setLevel(Number(e.target.value) as Level)}>
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
              <div className="grid max-h-64 gap-1.5 overflow-y-auto rounded-xl p-0.5">
                {courses.data.map((c) => (
                  <label key={c.id} className="flex cursor-pointer items-start gap-3 rounded-xl px-3 py-2 ring-1 ring-slate-200 has-[:checked]:bg-brand-50 has-[:checked]:ring-brand-500">
                    <input type="checkbox" className="mt-0.5 accent-brand-600" checked={selected.has(c.id)} onChange={() => toggleCourse(c.id)} />
                    <span className="text-sm">
                      <span className="font-semibold">{c.code}</span> {c.title}
                      {!c.is_reviewed && <span className="block text-xs text-amber-700">Sample content, pending lecturer review</span>}
                    </span>
                  </label>
                ))}
              </div>
            </fieldset>
          )}

          {save.isError && <ErrorMessage error={save.error} />}
          <Button type="submit" className="w-full" disabled={save.isPending}>
            {save.isPending ? 'Saving…' : 'Continue'}
          </Button>
        </form>
      </Card>
    </div>
  )
}
