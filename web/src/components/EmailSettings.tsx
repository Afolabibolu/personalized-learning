export type EmailChoice = { email_reminders: boolean; email_streak: boolean; email_digest: boolean; email_weekly: boolean }

const EMAIL_KINDS: { key: keyof Omit<EmailChoice, 'email_reminders'>; label: string; hint: string }[] = [
  { key: 'email_streak', label: 'Streak at risk', hint: 'On your study days, at your study time, if nothing is logged yet' },
  { key: 'email_digest', label: 'Weak topics and new recommendations', hint: 'One email a day at most, after 19:00' },
  { key: 'email_weekly', label: 'Weekly summary', hint: 'Sunday evening: your minutes, topics improved, what to focus on' },
]

/** "Email me reminders", then one tick box per kind. Onboarding shows the switch only (compact). */
export function EmailSettings({ value, onChange, compact = false }: { value: EmailChoice; onChange: (v: EmailChoice) => void; compact?: boolean }) {
  return (
    <div className="rounded-xl bg-slate-50 p-3" data-testid="email-settings">
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-sm font-medium text-slate-800">Email me reminders</p>
          <p className="text-xs text-slate-500">Sent to the address you signed up with. Every email has a link to turn them off.</p>
        </div>
        <button
          type="button"
          role="switch"
          aria-checked={value.email_reminders}
          aria-label="Email me reminders"
          onClick={() => onChange({ ...value, email_reminders: !value.email_reminders })}
          className={`relative h-6 w-11 shrink-0 rounded-full transition ${value.email_reminders ? 'bg-brand-600' : 'bg-slate-300'}`}
        >
          <span className={`absolute top-0.5 left-0.5 h-5 w-5 rounded-full bg-white shadow transition ${value.email_reminders ? 'translate-x-5' : ''}`} />
        </button>
      </div>
      {value.email_reminders && !compact && (
        <fieldset className="mt-3 grid gap-2 border-t border-slate-200 pt-3">
          <legend className="sr-only">Which emails</legend>
          {EMAIL_KINDS.map((k) => (
            <label key={k.key} className="flex items-start gap-2.5">
              <input
                type="checkbox"
                className="mt-0.5 h-4 w-4 rounded border-slate-300 text-brand-600"
                checked={value[k.key]}
                onChange={() => onChange({ ...value, [k.key]: !value[k.key] })}
              />
              <span>
                <span className="block text-sm text-slate-800">{k.label}</span>
                <span className="block text-xs text-slate-500">{k.hint}</span>
              </span>
            </label>
          ))}
        </fieldset>
      )}
    </div>
  )
}
