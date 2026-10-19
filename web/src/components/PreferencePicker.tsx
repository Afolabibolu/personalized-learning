import type { LearningPreference } from '../api/types'

export const PREFERENCES: { value: LearningPreference; label: string; detail: string }[] = [
  { value: 'note', label: 'Reading notes', detail: 'Short study notes in the app' },
  { value: 'lecture', label: 'Lecture slides', detail: "The lecturer's slides" },
  { value: 'past_questions', label: 'Practising questions', detail: 'Past exam questions' },
  { value: 'video', label: 'Videos', detail: 'Recorded lectures and tutorials' },
]

/** How the matched line names a preference: "Matched to your preference: study notes". */
export const PREFERENCE_PHRASE: Record<LearningPreference, string> = {
  note: 'study notes',
  lecture: 'lecture slides',
  past_questions: 'practising questions',
  video: 'videos',
}

export function PreferencePicker({
  value,
  onChange,
}: {
  value: LearningPreference[]
  onChange: (value: LearningPreference[]) => void
}) {
  function toggle(pref: LearningPreference) {
    onChange(value.includes(pref) ? value.filter((p) => p !== pref) : [...value, pref])
  }
  return (
    <fieldset>
      <legend className="mb-1.5 text-sm font-medium text-slate-700">How do you prefer to study?</legend>
      <p className="mb-3 text-xs text-slate-500">Pick any that apply. Recommendations use these first.</p>
      <div className="grid gap-2 sm:grid-cols-2">
        {PREFERENCES.map((p) => {
          const selected = value.includes(p.value)
          return (
            <button
              type="button"
              key={p.value}
              onClick={() => toggle(p.value)}
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
  )
}
