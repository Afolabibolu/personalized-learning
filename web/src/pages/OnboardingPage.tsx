import { useState, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { getProfile, updateProfile } from '../api/profile'
import type { LearningPreference, Level } from '../api/types'
import { PreferencePicker } from '../components/PreferencePicker'
import { Button, Card, ErrorMessage, Field, PageHeader, Spinner, inputClass } from '../components/ui'

const LEVELS: Level[] = [100, 200, 300, 400, 500]

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

          <PreferencePicker value={preferences} onChange={setPreferences} />

          {save.isError && <ErrorMessage error={save.error} />}
          <Button type="submit" className="w-full" disabled={save.isPending}>
            {save.isPending ? 'Saving…' : 'Continue'}
          </Button>
        </form>
      </Card>
    </div>
  )
}
