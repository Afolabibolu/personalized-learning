import { Link } from 'react-router-dom'
import type { Reminder } from '../../lib/reminders'

export function RemindersCard({ reminders }: { reminders: Reminder[] }) {
  if (reminders.length === 0) return null
  return (
    <section aria-label="Reminders" className="grid gap-2">
      {reminders.map((r) => (
        <div
          key={r.id}
          data-testid="reminder"
          className={`flex flex-col gap-2 rounded-2xl px-4 py-3 text-sm ring-1 sm:flex-row sm:items-center sm:justify-between ${
            r.tone === 'warning' ? 'bg-amber-50 text-amber-900 ring-amber-200' : 'bg-brand-50 text-brand-900 ring-brand-100'
          }`}
        >
          <span className="flex items-start gap-2">
            <BellIcon />
            {r.text}
          </span>
          {r.action && (
            <Link to={r.action.to} className="shrink-0 pl-6 font-semibold underline-offset-2 hover:underline sm:pl-0">
              {r.action.label} →
            </Link>
          )}
        </div>
      ))}
    </section>
  )
}

function BellIcon() {
  return (
    <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" className="mt-0.5 h-4 w-4 shrink-0" aria-hidden>
      <path d="M10 3a4.5 4.5 0 0 0-4.5 4.5c0 4-1.5 5.5-1.5 5.5h12s-1.5-1.5-1.5-5.5A4.5 4.5 0 0 0 10 3ZM8.5 16a1.5 1.5 0 0 0 3 0" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  )
}
