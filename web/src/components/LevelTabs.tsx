/** A row of pill buttons that picks one option, such as one level at a time. */
export function LevelTabs<T extends string | number>({
  label,
  options,
  value,
  onChange,
}: {
  label: string
  options: { value: T; label: string; count?: number }[]
  value: T
  onChange: (value: T) => void
}) {
  return (
    <div className="flex flex-wrap gap-2" role="group" aria-label={label}>
      {options.map((o) => (
        <button
          key={o.value}
          type="button"
          aria-pressed={value === o.value}
          onClick={() => onChange(o.value)}
          className={`rounded-full px-3 py-1 text-xs font-semibold ring-1 transition ${
            value === o.value ? 'bg-brand-600 text-white ring-brand-600' : 'bg-white text-slate-600 ring-slate-300 hover:ring-brand-500'
          }`}
        >
          {o.label}
          {o.count !== undefined && <span className={value === o.value ? 'text-brand-100' : 'text-slate-400'}> · {o.count}</span>}
        </button>
      ))}
    </div>
  )
}
