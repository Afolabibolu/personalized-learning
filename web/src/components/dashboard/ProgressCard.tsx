import { useState } from 'react'
import { Bar, BarChart, Cell, LabelList, ReferenceLine, ResponsiveContainer, XAxis, YAxis } from 'recharts'
import type { DashboardData } from '../../api/dashboard'
import { Card } from '../ui'

const BAR_COLOURS = { weak: '#ef4444', middle: '#f59e0b', strong: '#10b981', none: '#cbd5e1' }

function colour(score: number | null): string {
  if (score === null) return BAR_COLOURS.none
  if (score < 50) return BAR_COLOURS.weak
  if (score < 70) return BAR_COLOURS.middle
  return BAR_COLOURS.strong
}

/** Splits a topic name into at most two lines of about `width` characters; the rest is cut with "…". */
export function wrapTitle(title: string, width = 22): [string, string?] {
  if (title.length <= width) return [title]
  const words = title.split(' ')
  let first = ''
  while (words.length && (first + ' ' + words[0]).trim().length <= width) first = (first + ' ' + words.shift()).trim()
  if (!first) first = words.shift() ?? ''
  let second = words.join(' ')
  if (second.length > width) second = `${second.slice(0, width - 1).trimEnd()}…`
  return second ? [first, second] : [first]
}

/** Topic name on up to two lines, with the full name as a hover tooltip. */
function TopicTick({ x, y, payload }: { x?: number; y?: number; payload?: { value: string } }) {
  const full = payload?.value ?? ''
  const [first, second] = wrapTitle(full)
  return (
    <text x={x} y={y} textAnchor="end" fontSize={11} fill="#475569">
      <title>{full}</title>
      <tspan x={x} dy={second ? -2 : 4}>{first}</tspan>
      {second && <tspan x={x} dy={13}>{second}</tspan>}
    </text>
  )
}

/** Latest score per topic, one course at a time. */
export function ProgressCard({ courses }: { courses: DashboardData['courses'] }) {
  const [courseId, setCourseId] = useState(courses[0]?.id)
  const course = courses.find((c) => c.id === courseId) ?? courses[0]
  if (!course) return null

  const data = course.topics.map((t) => ({
    name: t.title,
    // Unattempted topics get a sliver so the row is visible.
    value: t.score ?? 2,
    label: t.score === null ? 'Not attempted' : `${Math.round(t.score)}%`,
    score: t.score,
  }))

  return (
    <Card>
      <div className="mb-4 flex flex-wrap items-center justify-between gap-2">
        <div>
          <h2 className="font-semibold">Progress by topic</h2>
          <p className="text-xs text-slate-500">Latest quiz score on each topic</p>
        </div>
        <div className="flex rounded-xl bg-slate-100 p-1" role="tablist">
          {courses.map((c) => (
            <button
              key={c.id}
              role="tab"
              aria-selected={c.id === course.id}
              onClick={() => setCourseId(c.id)}
              className={`rounded-lg px-3 py-1 text-xs font-semibold transition ${
                c.id === course.id ? 'bg-white text-slate-900 shadow-sm' : 'text-slate-500 hover:text-slate-800'
              }`}
            >
              {c.code}
            </button>
          ))}
        </div>
      </div>

      <div style={{ height: data.length * 48 + 28 }} data-testid="progress-chart">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data} layout="vertical" margin={{ top: 0, right: 64, bottom: 0, left: 0 }}>
            <XAxis type="number" domain={[0, 100]} ticks={[0, 50, 100]} tickFormatter={(v) => `${v}%`} fontSize={11} stroke="#94a3b8" />
            <YAxis type="category" dataKey="name" width={156} tick={<TopicTick />} tickLine={false} axisLine={false} />
            <ReferenceLine x={50} stroke="#94a3b8" strokeDasharray="4 4" />
            <Bar dataKey="value" radius={[0, 6, 6, 0]} barSize={18} isAnimationActive={false}>
              {data.map((d) => (
                <Cell key={d.name} fill={colour(d.score)} />
              ))}
              <LabelList dataKey="label" position="right" fontSize={11} fill="#334155" />
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
      <p className="mt-2 flex flex-wrap gap-x-4 gap-y-1 text-xs text-slate-500">
        <Legend colour={BAR_COLOURS.weak} label="Below 50%: needs attention" />
        <Legend colour={BAR_COLOURS.middle} label="50–69%" />
        <Legend colour={BAR_COLOURS.strong} label="70%+" />
      </p>
    </Card>
  )
}

function Legend({ colour, label }: { colour: string; label: string }) {
  return (
    <span className="inline-flex items-center gap-1.5">
      <span className="h-2.5 w-2.5 rounded-sm" style={{ background: colour }} />
      {label}
    </span>
  )
}
