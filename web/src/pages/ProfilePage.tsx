import { useEffect, useState, type FormEvent } from 'react'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { getProfile, updateProfile } from '../api/profile'
import type { LearningPreference, Level, Weekday } from '../api/types'
import { PreferencePicker } from '../components/PreferencePicker'
import { Button, Card, ErrorMessage, Field, PageHeader, Spinner, inputClass } from '../components/ui'

const DAYS: { value: Weekday; label: string }[] = [
  { value: 'mon', label: 'Mon' },
  { value: 'tue', label: 'Tue' },
  { value: 'wed', label: 'Wed' },
  { value: 'thu', label: 'Thu' },
  { value: 'fri', label: 'Fri' },
  { value: 'sat', label: 'Sat' },
  { value: 'sun', label: 'Sun' },
]

export function ProfilePage() {
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })

  if (profile.isPending) return <Spinner />
  if (profile.isError) return <ErrorMessage error={profile.error} />

  return (
    <div className="mx-auto grid max-w-xl gap-6">
      <PageHeader eyebrow="Profile" title={profile.data.full_name ?? 'Your profile'}>
        {[profile.data.department, profile.data.level ? `${profile.data.level} level` : null].filter(Boolean).join(' · ')}
      </PageHeader>
      <YourDetails />
      <ReminderSettings />
    </div>
  )
}

const LEVELS: Level[] = [100, 200, 300, 400, 500]

function YourDetails() {
  const queryClient = useQueryClient()
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const [fullName, setFullName] = useState('')
  const [department, setDepartment] = useState('')
  const [level, setLevel] = useState<Level>(500)
  const [preferences, setPreferences] = useState<LearningPreference[]>([])

  useEffect(() => {
    if (!profile.data) return
    setFullName(profile.data.full_name ?? '')
    setDepartment(profile.data.department ?? '')
    setLevel(profile.data.level ?? 500)
    setPreferences(profile.data.learning_preferences)
  }, [profile.data])

  const save = useMutation({
    mutationFn: () =>
      updateProfile({ full_name: fullName.trim(), department: department.trim(), level, learning_preferences: preferences }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['profile'] }),
  })

  function changed<T>(setter: (value: T) => void) {
    return (value: T) => {
      save.reset()
      setter(value)
    }
  }

  function handleSubmit(e: FormEvent) {
    e.preventDefault()
    save.mutate()
  }

  return (
    <Card>
      <h2 className="font-semibold">Your details</h2>
      <form onSubmit={handleSubmit} className="mt-4 space-y-5">
        <Field label="Full name">
          <input required autoComplete="name" className={inputClass} value={fullName} onChange={(e) => changed(setFullName)(e.target.value)} />
        </Field>
        <div className="grid gap-4 sm:grid-cols-2">
          <Field label="Department">
            <input required className={inputClass} value={department} onChange={(e) => changed(setDepartment)(e.target.value)} />
          </Field>
          <Field label="Level">
            <select className={inputClass} value={level} onChange={(e) => changed(setLevel)(Number(e.target.value) as Level)}>
              {LEVELS.map((l) => (
                <option key={l} value={l}>
                  {l} level
                </option>
              ))}
            </select>
          </Field>
        </div>
        <PreferencePicker value={preferences} onChange={changed(setPreferences)} />
        {save.isError && <ErrorMessage error={save.error} />}
        {save.isSuccess && (
          <p className="rounded-xl bg-emerald-50 px-4 py-3 text-sm text-emerald-800 ring-1 ring-emerald-200" role="status">
            Profile saved. New recommendations will use your study preferences.
          </p>
        )}
        <Button type="submit" className="w-full sm:w-auto" disabled={save.isPending || !fullName.trim() || !department.trim()}>
          {save.isPending ? 'Saving…' : 'Save profile'}
        </Button>
      </form>
    </Card>
  )
}

function ReminderSettings() {
  const queryClient = useQueryClient()
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const [days, setDays] = useState<Weekday[]>([])
  const [time, setTime] = useState('18:00')
  const [goal, setGoal] = useState(30)
  const [browser, setBrowser] = useState(false)
  const [permissionNote, setPermissionNote] = useState<string | null>(null)

  useEffect(() => {
    if (!profile.data) return
    setDays(profile.data.study_days)
    setTime(profile.data.preferred_study_time.slice(0, 5))
    setGoal(profile.data.daily_goal_minutes)
    setBrowser(profile.data.browser_notifications)
  }, [profile.data])

  const save = useMutation({
    mutationFn: () =>
      updateProfile({ study_days: days, preferred_study_time: time, daily_goal_minutes: goal, browser_notifications: browser }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['profile'] }),
  })

  function toggleDay(day: Weekday) {
    save.reset()
    setDays((prev) => (prev.includes(day) ? prev.filter((d) => d !== day) : [...prev, day]))
  }

  async function toggleBrowser() {
    save.reset()
    if (browser) {
      setBrowser(false)
      return
    }
    // Permission is asked for here only, never on page load.
    if (typeof Notification === 'undefined') {
      setPermissionNote('This browser does not support notifications. Reminders still appear under the bell.')
      return
    }
    const permission = Notification.permission === 'granted' ? 'granted' : await Notification.requestPermission()
    if (permission === 'granted') {
      setBrowser(true)
      setPermissionNote(null)
    } else {
      setPermissionNote('The browser blocked notifications. Reminders still appear under the bell in the app.')
    }
  }

  function handleSubmit(e: FormEvent) {
    e.preventDefault()
    save.mutate()
  }

  return (
    <Card>
      <h2 className="font-semibold">Reminder settings</h2>
      <p className="mt-1 text-sm text-slate-600">Reminders appear under the bell in the app. They use these settings.</p>
      <form onSubmit={handleSubmit} className="mt-5 space-y-5">
        <fieldset>
          <legend className="mb-1.5 text-sm font-medium text-slate-700">Study days</legend>
          <div className="flex flex-wrap gap-2">
            {DAYS.map((d) => {
              const selected = days.includes(d.value)
              return (
                <button
                  type="button"
                  key={d.value}
                  aria-pressed={selected}
                  onClick={() => toggleDay(d.value)}
                  className={`w-12 rounded-xl py-2 text-sm font-medium ring-1 transition ${
                    selected ? 'bg-brand-50 text-brand-700 ring-2 ring-brand-600' : 'bg-white text-slate-600 ring-slate-300 hover:ring-slate-400'
                  }`}
                >
                  {d.label}
                </button>
              )
            })}
          </div>
          <p className="mt-1.5 text-xs text-slate-500">On these days you get a "keep your streak going" reminder if nothing is logged by your study time.</p>
        </fieldset>

        <div className="grid gap-4 sm:grid-cols-2">
          <Field label="Preferred study time">
            <input type="time" required className={inputClass} value={time} onChange={(e) => (save.reset(), setTime(e.target.value))} />
          </Field>
          <Field label="Daily goal (minutes)" hint="5 to 600 minutes">
            <input
              type="number"
              min={5}
              max={600}
              required
              className={inputClass}
              value={goal}
              onChange={(e) => (save.reset(), setGoal(Number(e.target.value)))}
            />
          </Field>
        </div>

        <div className="flex items-start justify-between gap-4 rounded-xl bg-slate-50 p-3">
          <div>
            <p className="text-sm font-medium text-slate-800">Browser notifications</p>
            <p className="text-xs text-slate-500">Also pop up reminders while the app is open in a tab. Optional.</p>
            {permissionNote && <p className="mt-1 text-xs text-amber-700">{permissionNote}</p>}
          </div>
          <button
            type="button"
            role="switch"
            aria-checked={browser}
            aria-label="Browser notifications"
            onClick={toggleBrowser}
            className={`relative h-6 w-11 shrink-0 rounded-full transition ${browser ? 'bg-brand-600' : 'bg-slate-300'}`}
          >
            <span className={`absolute top-0.5 left-0.5 h-5 w-5 rounded-full bg-white shadow transition ${browser ? 'translate-x-5' : ''}`} />
          </button>
        </div>

        {save.isError && <ErrorMessage error={save.error} />}
        {save.isSuccess && (
          <p className="rounded-xl bg-emerald-50 px-4 py-3 text-sm text-emerald-800 ring-1 ring-emerald-200" role="status">
            Reminder settings saved.
          </p>
        )}
        <Button type="submit" className="w-full sm:w-auto" disabled={save.isPending || days.length === 0 || goal < 5 || goal > 600}>
          {save.isPending ? 'Saving…' : 'Save reminder settings'}
        </Button>
      </form>
    </Card>
  )
}
