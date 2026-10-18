import { useState, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { getProfile, updateProfile } from '../api/profile'
import type { LearningPreference, Level } from '../api/types'
import { Button, Card, ErrorMessage, Field, PageHeader, Spinner, inputClass } from '../components/ui'

const LEVELS: Level[] = [100, 200, 300, 400, 500]

const PREFERENCES: { value: LearningPreference; label: string; detail: string }[] = [
  { value: 'reading', label: 'Reading', detail: 'Lecture notes and slides' },
  { value: 'video', label: 'Video', detail: 'Recorded lectures and tutorials' },
  { value: 'practice', label: 'Practice', detail: 'Quizzes and past questions' },
]

export function OnboardingPage() {
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })

  const [department, setDepartment] = useState('Computer Science')
  const [level, setLevel] = useState<Level>(500)
  const [preferences, setPreferences] = useState<LearningPreference[]>([])

  const save = useMutation({
    mutationFn: () => updateProfile({ department: department.trim(), level, learning_preferences: preferences }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['profile'] })
      navigate('/')
    },
  })

  function togglePreference(value: LearningPreference) {
    setPreferences((prev) => (prev.includes(value) ? prev.filter((p) => p !== value) : [...prev, value]))
  }

  function handleSubmit(e: FormEvent) {
    e.preventDefault()
    save.mutate()
  }

  if (profile.isPending) return <Spinner />

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

          <fieldset>
            <legend className="mb-1.5 text-sm font-medium text-slate-700">How do you prefer to learn?</legend>
            <p className="mb-3 text-xs text-slate-500">Pick any that apply.</p>
            <div className="grid gap-2 sm:grid-cols-3">
              {PREFERENCES.map((p) => {
                const selected = preferences.includes(p.value)
                return (
                  <button
                    type="button"
                    key={p.value}
                    onClick={() => togglePreference(p.value)}
                    aria-pressed={selected}
                    className={`rounded-xl p-3 text-left ring-1 transition ${
                      selected ? 'bg-brand-50 ring-2 ring-brand-600' : 'bg-white ring-slate-300 hover:ring-slate-400'
                    }`}
                  >
                    <span className="block text-sm font-semibold">{p.label}</span>
                    <span className="block text-xs text-slate-500">{p.detail}</span>
                  </button>
                )
              })}
            </div>
          </fieldset>

          {save.isError && <ErrorMessage error={save.error} />}
          <Button type="submit" className="w-full" disabled={save.isPending}>
            {save.isPending ? 'Saving…' : 'Continue'}
          </Button>
        </form>
      </Card>
    </div>
  )
}
