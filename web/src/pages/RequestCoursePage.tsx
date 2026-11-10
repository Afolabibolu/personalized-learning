import { useState, type FormEvent } from 'react'
import { Link } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { MAX_FILES, fileProblem, listCourseRequests, requestCourse } from '../api/courseRequests'
import { FileButton, REQUEST_STATUS, fileSize } from '../components/RequestFiles'
import { formatDate } from '../lib/format'
import { Button, Card, ErrorMessage, Field, PageHeader, Spinner, inputClass } from '../components/ui'

// The student's words for each status (managers see the short ones).
const STATUS_TEXT = { pending: 'Pending', in_progress: 'In progress', added: 'Added to your courses', declined: 'Declined' } as const

const EMPTY = { code: '', title: '', level: '', semester: '', lecturer: '', details: '' }

export function RequestCoursePage() {
  const queryClient = useQueryClient()
  const requests = useQuery({ queryKey: ['courseRequests'], queryFn: listCourseRequests })
  const [form, setForm] = useState(EMPTY)
  const [files, setFiles] = useState<File[]>([])
  const [fileError, setFileError] = useState<string | null>(null)

  function addFiles(list: FileList | null) {
    const picked = Array.from(list ?? [])
    const problems = picked.map(fileProblem).filter(Boolean)
    const ok = picked.filter((f) => !fileProblem(f))
    const next = [...files, ...ok].slice(0, MAX_FILES)
    setFiles(next)
    setFileError(
      problems.length ? problems.join('. ') + '.' : files.length + ok.length > MAX_FILES ? `At most ${MAX_FILES} files.` : null,
    )
  }
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
      }, files),
    onSuccess: () => {
      setForm(EMPTY)
      setFiles([])
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
          <div>
            <p className="mb-1.5 text-sm font-medium text-slate-700">Course files (optional)</p>
            <p className="mb-2 text-xs text-slate-500">
              The outline, lecture notes or past questions: PDF, DOCX, PPTX or photos, up to {MAX_FILES} files of 20 MB each.
              Only you and the course managers can open them.
            </p>
            <label className="flex cursor-pointer items-center justify-center gap-2 rounded-xl border-2 border-dashed border-slate-300 px-4 py-4 text-sm font-medium text-slate-600 hover:border-brand-400 hover:text-brand-700">
              <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.8" className="h-5 w-5" aria-hidden>
                <path d="M10 13V3m0 0L6 7m4-4 4 4M4 13v3h12v-3" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              {files.length >= MAX_FILES ? 'Five files attached' : 'Choose files'}
              <input
                type="file"
                multiple
                className="sr-only"
                accept=".pdf,.docx,.pptx,image/*"
                disabled={files.length >= MAX_FILES}
                onChange={(e) => (addFiles(e.target.files), (e.target.value = ''))}
                data-testid="request-files"
              />
            </label>
            {fileError && <p className="mt-1.5 text-xs font-medium text-red-600">{fileError}</p>}
            {files.length > 0 && (
              <ul className="mt-2 grid gap-1.5" data-testid="chosen-files">
                {files.map((f, i) => (
                  <li key={`${f.name}-${i}`} className="flex items-center gap-2 rounded-lg px-2 py-1.5 text-sm ring-1 ring-slate-200">
                    <span className="min-w-0 flex-1 truncate">{f.name}</span>
                    <span className="text-xs text-slate-500">{fileSize(f.size)}</span>
                    <button type="button" className="text-xs font-semibold text-slate-500 hover:text-red-600" onClick={() => setFiles(files.filter((_, j) => j !== i))}>
                      Remove
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </div>

          {send.isError && <ErrorMessage error={send.error} />}
          {send.isSuccess && (
            <p className="rounded-xl bg-emerald-50 px-3.5 py-2.5 text-sm text-emerald-800" role="status">
              Request sent. You will get a notification when the course is added.
            </p>
          )}
          <Button type="submit" disabled={!valid || send.isPending} className="w-full">
            {send.isPending ? (files.length ? 'Uploading…' : 'Sending…') : 'Send request'}
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
                  <span className={`rounded-full px-2.5 py-0.5 text-xs font-semibold ring-1 ${REQUEST_STATUS[r.status].className}`} data-testid="request-status">
                    {STATUS_TEXT[r.status]}
                  </span>
                </div>
                <p className="mt-1 text-xs text-slate-500">
                  Sent {formatDate(r.created_at)}
                  {r.level && ` · ${r.level} level`}
                  {r.semester && ` · ${r.semester === 1 ? 'first' : 'second'} semester`}
                </p>
                {r.files && r.files.length > 0 && (
                  <ul className="mt-2 grid gap-1.5" aria-label="Your files">
                    {r.files.map((f) => <FileButton key={f.id} path={f.path} name={f.name} size={f.size_bytes} type={f.content_type} />)}
                  </ul>
                )}
                {r.admin_note && (
                  <p className="mt-2 text-sm text-slate-600">
                    {r.status === 'declined' ? <span className="font-medium">Reason: </span> : null}
                    {r.admin_note}
                  </p>
                )}
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
