import { useState, type FormEvent } from 'react'
import { Link } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { listCourseRequests, requestCourse, type CourseRequestStatus } from '../api/courseRequests'
import { formatDate } from '../lib/format'
import { Button, Card, ErrorMessage, Field, PageHeader, Spinner, inputClass } from '../components/ui'

const STATUS: Record<CourseRequestStatus, { label: string; className: string }> = {
  pending: { label: 'Pending', className: 'bg-amber-50 text-amber-800 ring-amber-200' },
  added: { label: 'Added to your courses', className: 'bg-emerald-50 text-emerald-700 ring-emerald-200' },
  declined: { label: 'Not added', className: 'bg-slate-100 text-slate-600 ring-slate-200' },
}

const EMPTY = { code: '', title: '', level: '', semester: '', lecturer: '', details: '' }

export function RequestCoursePage() {
  const queryClient = useQueryClient()
  const requests = useQuery({ queryKey: ['courseRequests'], queryFn: listCourseRequests })
  const [form, setForm] = useState(EMPTY)
  const set = (key: keyof typeof EMPTY) => (e: { target: { value: string } }) => setForm((f) => ({ ...f, [key]: e.target.value }))

  const send = useMutation({
    mutationFn: () =>
      requestCourse({
        code: form.code.trim().toUpperCase(),
        title: form.title.trim(),
        level: form.level ? Number(form.level) : null,
        semester: form.semester ? Number(form.semester) : null,
        lecturer: form.lecturer.trim() || null,
        details: form.details.trim() || null,
      }),
    onSuccess: () => {
      setForm(EMPTY)
      queryClient.invalidateQueries({ queryKey: ['courseRequests'] })
    },
  })

  function handleSubmit(e: FormEvent) {
    e.preventDefault()
    send.mutate()
  }

  const valid = form.code.trim().length >= 2 && form.title.trim().length >= 2

  return (
    <div className="mx-auto max-w-lg">
      <PageHeader eyebrow="Courses" title="Request a course">
        Can't find a course you are taking? Tell us about it. New courses are added through the course ingestion pipeline,
        then appear in your courses with their topics, study notes and quizzes.
      </PageHeader>

      <Card>
        <form onSubmit={handleSubmit} className="space-y-5">
          <div className="grid gap-4 sm:grid-cols-[1fr_2fr]">
            <Field label="Course code">
              <input className={inputClass} value={form.code} onChange={set('code')} placeholder="e.g. CSC 563" maxLength={20} required />
            </Field>
            <Field label="Course title">
              <input className={inputClass} value={form.title} onChange={set('title')} placeholder="e.g. Computer Graphics" maxLength={200} required />
            </Field>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <Field label="Level">
              <select className={inputClass} value={form.level} onChange={set('level')}>
                <option value="">Not sure</option>
                {[100, 200, 300, 400, 500].map((l) => (
                  <option key={l} value={l}>{l} level</option>
                ))}
              </select>
            </Field>
            <Field label="Semester">
              <select className={inputClass} value={form.semester} onChange={set('semester')}>
                <option value="">Not sure</option>
                <option value="1">First</option>
                <option value="2">Second</option>
              </select>
            </Field>
          </div>
          <Field label="Lecturer (optional)">
            <input className={inputClass} value={form.lecturer} onChange={set('lecturer')} maxLength={200} />
          </Field>
          <Field label="Details (optional)" hint="Topics covered, or where the lecture notes and past questions can be found.">
            <textarea className={`${inputClass} min-h-28`} value={form.details} onChange={set('details')} maxLength={2000} />
          </Field>
          {send.isError && <ErrorMessage error={send.error} />}
          {send.isSuccess && (
            <p className="rounded-xl bg-emerald-50 px-3.5 py-2.5 text-sm text-emerald-800" role="status">
              Request sent. You will get a notification when the course is added.
            </p>
          )}
          <Button type="submit" disabled={!valid || send.isPending} className="w-full">
            {send.isPending ? 'Sending…' : 'Send request'}
          </Button>
        </form>
      </Card>

      <section aria-labelledby="my-requests" className="mt-8">
        <h2 id="my-requests" className="mb-3 font-semibold">Your requests</h2>
        {requests.isPending && <Spinner />}
        {requests.isError && <ErrorMessage error={requests.error} />}
        {requests.data?.length === 0 && (
          <Card>
            <p className="text-sm text-slate-600">No requests yet. Use the form above when a course is missing.</p>
          </Card>
        )}
        <ul className="grid gap-3">
          {requests.data?.map((r) => (
            <li key={r.id} data-testid="course-request">
              <Card className="p-4">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <p className="font-semibold">
                    <span className="text-brand-600">{r.code}</span> · {r.title}
                  </p>
                  <span className={`rounded-full px-2.5 py-0.5 text-xs font-semibold ring-1 ${STATUS[r.status].className}`}>
                    {STATUS[r.status].label}
                  </span>
                </div>
                <p className="mt-1 text-xs text-slate-500">
                  Sent {formatDate(r.created_at)}
                  {r.level && ` · ${r.level} level`}
                  {r.semester && ` · ${r.semester === 1 ? 'first' : 'second'} semester`}
                </p>
                {r.admin_note && <p className="mt-2 text-sm text-slate-600">{r.admin_note}</p>}
                {r.status === 'added' && r.course_id && (
                  <Link to={`/courses/${r.course_id}`} className="mt-2 inline-block text-sm font-semibold text-brand-600 hover:text-brand-700">
                    Open the course
                  </Link>
                )}
              </Card>
            </li>
          ))}
        </ul>
      </section>
    </div>
  )
}
