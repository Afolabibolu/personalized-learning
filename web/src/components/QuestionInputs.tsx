import type { QuizQuestion } from '../api/types'

type InputProps = {
  question: QuizQuestion
  value: string[]
  onChange: (value: string[]) => void
}

const optionBase = 'flex w-full items-center gap-3 rounded-xl px-4 py-3 text-left text-sm ring-1 transition'
const optionIdle = 'bg-white ring-slate-300 hover:ring-slate-400'
const optionSelected = 'bg-brand-50 ring-2 ring-brand-600'

function Marker({ selected, shape }: { selected: boolean; shape: 'circle' | 'square' }) {
  return (
    <span
      className={`grid h-5 w-5 shrink-0 place-items-center border-2 ${shape === 'circle' ? 'rounded-full' : 'rounded-md'} ${
        selected ? 'border-brand-600 bg-brand-600' : 'border-slate-300 bg-white'
      }`}
    >
      {selected && (shape === 'circle' ? <span className="h-2 w-2 rounded-full bg-white" /> : <Tick />)}
    </span>
  )
}

function Tick() {
  return (
    <svg viewBox="0 0 16 16" className="h-3 w-3 text-white" fill="none" stroke="currentColor" strokeWidth="2.5">
      <path d="M3 8.5l3 3 7-7" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  )
}

function SingleChoice({ question, value, onChange, hint }: InputProps & { hint?: string }) {
  return (
    <div role="radiogroup" className="grid gap-2">
      {hint && <p className="mb-1 text-xs font-medium text-slate-500">{hint}</p>}
      {question.options.map((o) => {
        const selected = value[0] === o.key
        return (
          <button
            type="button"
            role="radio"
            aria-checked={selected}
            key={o.key}
            onClick={() => onChange([o.key])}
            className={`${optionBase} ${selected ? optionSelected : optionIdle}`}
          >
            <Marker selected={selected} shape="circle" />
            {o.text}
          </button>
        )
      })}
    </div>
  )
}

function TrueFalse({ question, value, onChange }: InputProps) {
  return (
    <div role="radiogroup" className="grid grid-cols-2 gap-3">
      {question.options.map((o) => {
        const selected = value[0] === o.key
        return (
          <button
            type="button"
            role="radio"
            aria-checked={selected}
            key={o.key}
            onClick={() => onChange([o.key])}
            className={`rounded-xl px-4 py-5 text-base font-semibold ring-1 transition ${selected ? optionSelected : optionIdle}`}
          >
            {o.text}
          </button>
        )
      })}
    </div>
  )
}

function MultiSelect({ question, value, onChange }: InputProps) {
  function toggle(key: string) {
    onChange(value.includes(key) ? value.filter((k) => k !== key) : [...value, key])
  }
  return (
    <div className="grid gap-2">
      <p className="mb-1 text-xs font-medium text-slate-500">Select all that apply.</p>
      {question.options.map((o) => {
        const selected = value.includes(o.key)
        return (
          <button
            type="button"
            role="checkbox"
            aria-checked={selected}
            key={o.key}
            onClick={() => toggle(o.key)}
            className={`${optionBase} ${selected ? optionSelected : optionIdle}`}
          >
            <Marker selected={selected} shape="square" />
            {o.text}
          </button>
        )
      })}
    </div>
  )
}

export function QuestionInput(props: InputProps) {
  switch (props.question.format) {
    case 'single_choice':
      return <SingleChoice {...props} />
    case 'true_false':
      return <TrueFalse {...props} />
    case 'multi_select':
      return <MultiSelect {...props} />
    case 'odd_one_out':
      return <SingleChoice {...props} hint="Pick the one that does not belong." />
  }
}

export const FORMAT_LABEL: Record<QuizQuestion['format'], string> = {
  single_choice: 'Single choice',
  true_false: 'True or false',
  multi_select: 'Multiple answers',
  odd_one_out: 'Odd one out',
}
