import { useState, type FormEvent } from 'react'
import { Link, NavLink, Outlet, useParams } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import type { CourseRequestStatus } from '../api/courseRequests'
import {
  getManagedCourse,
  listAllCourses,
  listAudit,
  listManagedRequests,
  listTopicQuestions,
  saveResource,
  setCourseReviewed,
  setQuestionHidden,
  setRequestStatus,
  updateQuestion,
  updateTopic,
  type ManagedCourse,
  type ManagedQuestion,
  type ManagedRequest,
} from '../api/manage'
import type { BookLinkType, ResourceType } from '../api/types'
import { RequireManager } from '../components/RequireManager'
import { FileButton, REQUEST_STATUS } from '../components/RequestFiles'
import { RESOURCE_LABEL, ResourceIcon } from '../components/ResourceList'
import { Button, Card, ErrorMessage, Field, PageHeader, SampleBadge, Spinner, inputClass } from '../components/ui'
import { formatDate } from '../lib/format'
import { LEVELS } from '../lib/levels'
import { timeAgo } from '../lib/time'

const tabClass = ({ isActive }: { isActive: boolean }) =>
  `rounded-lg px-3 py-2 text-sm font-medium whitespace-nowrap transition ${
    isActive ? 'bg-brand-50 text-brand-700' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
  }`

/** /manage: requests, courses and the edit history, for course managers only. */
export function ManageLayout() {
  return (
    <RequireManager>
      {/* min-w-0 on grid children: a long link or name truncates instead of widening the page */}
      <div className="grid gap-5 [&>*]:min-w-0">
        <PageHeader eyebrow="Course management" title="Manage courses">
          Handle course requests and fix course content. Every change is recorded with your name.
        </PageHeader>
        <nav className="-mx-1 flex gap-1 overflow-x-auto px-1" aria-label="Course management">
          <NavLink to="/manage" end className={tabClass}>Requests</NavLink>
          <NavLink to="/manage/courses" className={tabClass}>Courses</NavLink>
          <NavLink to="/manage/history" className={tabClass}>Edit history</NavLink>
        </nav>
        <Outlet />
      </div>
    </RequireManager>
  )
}

function StatusBadge({ status }: { status: CourseRequestStatus }) {
  return (
    <span className={`rounded-full px-2.5 py-0.5 text-xs font-semibold whitespace-nowrap ring-1 ${REQUEST_STATUS[status].className}`} data-testid="request-status">
      {REQUEST_STATUS[status].label}
    </span>
  )
}

// -- Requests ------------------------------------------------------------------------------

export function ManageRequestsPage() {
  const requests = useQuery({ queryKey: ['manage', 'requests'], queryFn: listManagedRequests })
  const [show, setShow] = useState<'open' | 'all'>('open')
  if (requests.isPending) return <Spinner />
  if (requests.isError) return <ErrorMessage error={requests.error} />
  const open = requests.data.filter((r) => r.status === 'pending' || r.status === 'in_progress')
  const shown = show === 'open' ? open : requests.data
  return (
    <section className="grid gap-3 [&>*]:min-w-0" aria-label="Course requests">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <p className="text-sm text-slate-600">
          {open.length} open · {requests.data.length} in total. Add a course through the pipeline
          (<code className="text-xs">docs/how-to-add-a-course.md</code>), then mark its request added.
        </p>
        <div className="flex gap-1 rounded-xl bg-slate-100 p-1 text-sm">
          {(['open', 'all'] as const).map((v) => (
            <button key={v} type="button" onClick={() => setShow(v)} aria-pressed={show === v}
              className={`rounded-lg px-3 py-1 font-medium ${show === v ? 'bg-white shadow-sm' : 'text-slate-600'}`}>
              {v === 'open' ? 'Open' : 'All'}
            </button>
          ))}
        </div>
      </div>
      {shown.length === 0 && (
        <Card><p className="text-sm text-slate-600">No {show === 'open' ? 'open ' : ''}requests. New ones appear here as students send them.</p></Card>
      )}
      <ul className="grid gap-3 [&>*]:min-w-0">
        {shown.map((r) => <RequestCard key={r.id} request={r} />)}
      </ul>
    </section>
  )
}

function RequestCard({ request: r }: { request: ManagedRequest }) {
  const queryClient = useQueryClient()
  const [mode, setMode] = useState<'added' | 'declined' | null>(null)
  const [code, setCode] = useState(r.code)
  const [note, setNote] = useState('')
  const change = useMutation({
    mutationFn: (status: 'in_progress' | 'added' | 'declined') =>
      setRequestStatus(r.id, status, status === 'in_progress' ? undefined : note.trim() || undefined, status === 'added' ? code.trim() : undefined),
    onSuccess: () => {
      setMode(null)
      setNote('')
      queryClient.invalidateQueries({ queryKey: ['manage'] })
    },
  })
  function submit(e: FormEvent) {
    e.preventDefault()
    if (mode) change.mutate(mode)
  }
  return (
    <li data-testid="manage-request" data-status={r.status}>
      <Card className="p-4">
        <div className="flex flex-wrap items-start justify-between gap-2">
          <div className="min-w-0">
            <p className="font-semibold"><span className="text-brand-600">{r.code}</span> · {r.title}</p>
            <p className="mt-0.5 text-xs text-slate-500">
              {r.student.name ?? 'A student'}{r.student.email ? ` (${r.student.email})` : ''} · sent {formatDate(r.created_at)}
              {r.level ? ` · ${r.level} level` : ''}{r.semester ? ` · ${r.semester === 1 ? 'first' : 'second'} semester` : ''}
            </p>
          </div>
          <StatusBadge status={r.status} />
        </div>
        {r.lecturer && <p className="mt-2 text-sm text-slate-700"><span className="text-slate-500">Lecturer:</span> {r.lecturer}</p>}
        {r.details && <p className="mt-1 text-sm whitespace-pre-line text-slate-700">{r.details}</p>}
        {r.files.length > 0 ? (
          <ul className="mt-3 grid gap-1.5 sm:grid-cols-2" aria-label="Files">
            {r.files.map((f) => <FileButton key={f.id} path={f.path} name={f.name} size={f.size_bytes} type={f.content_type} />)}
          </ul>
        ) : (
          <p className="mt-2 text-xs text-slate-500">No files attached.</p>
        )}
        {r.admin_note && <p className="mt-3 rounded-lg bg-slate-50 px-3 py-2 text-sm text-slate-700">Note to student: {r.admin_note}</p>}

        {r.status !== 'added' && r.status !== 'declined' && (
          <div className="mt-3 flex flex-wrap gap-2">
            {r.status === 'pending' && (
              <Button variant="secondary" className="px-3 py-1.5" onClick={() => change.mutate('in_progress')} disabled={change.isPending}>
                Mark in progress
              </Button>
            )}
            <Button variant="secondary" className="px-3 py-1.5" onClick={() => setMode(mode === 'added' ? null : 'added')}>Mark added</Button>
            <Button variant="ghost" className="px-3 py-1.5" onClick={() => setMode(mode === 'declined' ? null : 'declined')}>Decline</Button>
          </div>
        )}
        {mode && (
          <form onSubmit={submit} className="mt-3 grid gap-3 rounded-xl bg-slate-50 p-3">
            {mode === 'added' ? (
              <Field label="Course code in the app" hint="The course you added through the pipeline. The student is enrolled in it and notified.">
                <input className={inputClass} value={code} onChange={(e) => setCode(e.target.value)} required />
              </Field>
            ) : (
              <Field label="Reason (the student sees this)">
                <textarea className={`${inputClass} min-h-20`} value={note} onChange={(e) => setNote(e.target.value)} required maxLength={500} />
              </Field>
            )}
            {change.isError && <ErrorMessage error={change.error} />}
            <div className="flex gap-2">
              <Button type="submit" disabled={change.isPending || (mode === 'declined' && !note.trim())} className="px-3 py-1.5">
                {mode === 'added' ? 'Mark added and notify' : 'Decline and notify'}
              </Button>
              <Button type="button" variant="ghost" className="px-3 py-1.5" onClick={() => setMode(null)}>Cancel</Button>
            </div>
          </form>
        )}
      </Card>
    </li>
  )
}

// -- Courses -------------------------------------------------------------------------------

export function ManageCoursesPage() {
  const courses = useQuery({ queryKey: ['manage', 'courses'], queryFn: listAllCourses })
  if (courses.isPending) return <Spinner />
  if (courses.isError) return <ErrorMessage error={courses.error} />
  const sample = courses.data.filter((c) => !c.is_reviewed).length
  return (
    <section className="grid gap-5" aria-label="Courses">
      <p className="text-sm text-slate-600">
        {courses.data.length} courses, {sample} still sample content. Open a course to fix a topic, a question or a link, or to mark it reviewed.
      </p>
      {LEVELS.map((level) => {
        const atLevel = courses.data.filter((c) => c.level === level)
        if (atLevel.length === 0) return null
        return (
          <div key={level}>
            <h2 className="mb-2 text-sm font-semibold tracking-wide text-slate-500 uppercase">{level} level · {atLevel.length}</h2>
            <ul className="grid gap-2 sm:grid-cols-2">
              {atLevel.map((c) => (
                <li key={c.id}>
                  <Link to={`/manage/courses/${encodeURIComponent(c.code)}`} data-testid="manage-course" data-reviewed={c.is_reviewed}
                    className="flex h-full items-start justify-between gap-2 rounded-xl bg-white p-3 ring-1 ring-slate-200 transition hover:ring-brand-300">
                    <span className="min-w-0 text-sm">
                      <span className="font-semibold">{c.code}</span> <span className="text-slate-700">{c.title}</span>
                    </span>
                    {c.is_reviewed ? (
                      <span className="shrink-0 rounded-full bg-emerald-50 px-2 py-0.5 text-xs font-semibold text-emerald-700 ring-1 ring-emerald-200">Reviewed</span>
                    ) : (
                      <span className="shrink-0 rounded-full bg-amber-50 px-2 py-0.5 text-xs font-semibold text-amber-700 ring-1 ring-amber-200">Sample</span>
                    )}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        )
      })}
    </section>
  )
}

export function ManageCoursePage() {
  const { code = '' } = useParams()
  const queryClient = useQueryClient()
  const course = useQuery({ queryKey: ['manage', 'course', code], queryFn: () => getManagedCourse(code) })
  const review = useMutation({
    mutationFn: (reviewed: boolean) => setCourseReviewed(course.data!.id, reviewed),
    onSuccess: () => queryClient.invalidateQueries(),
  })
  if (course.isPending) return <Spinner />
  if (course.isError) return <ErrorMessage error={course.error} />
  const c = course.data
  return (
    <section className="grid gap-4 [&>*]:min-w-0" aria-label={c.code}>
      <Link to="/manage/courses" className="text-sm text-slate-500 hover:text-slate-900">← All courses</Link>
      <Card>
        <div className="flex flex-wrap items-start justify-between gap-3">
          <div>
            <h2 className="text-lg font-semibold"><span className="text-brand-600">{c.code}</span> · {c.title}</h2>
            <p className="mt-1 text-sm text-slate-500">{c.level ? `${c.level} level · ` : ''}{c.topics.length} topics</p>
            <div className="mt-2">{c.is_reviewed ? (
              <span className="rounded-full bg-emerald-50 px-2.5 py-0.5 text-xs font-semibold text-emerald-700 ring-1 ring-emerald-200" data-testid="course-reviewed">Reviewed</span>
            ) : <SampleBadge />}</div>
          </div>
          <Button variant={c.is_reviewed ? 'secondary' : 'primary'} onClick={() => review.mutate(!c.is_reviewed)} disabled={review.isPending} data-testid="toggle-reviewed">
            {c.is_reviewed ? 'Mark as sample content' : 'Mark as reviewed'}
          </Button>
        </div>
        {!c.is_reviewed && (
          <p className="mt-3 text-xs text-slate-500">Marking it reviewed removes the "Sample content" badge for students. Check the topics, notes and questions against the course files first.</p>
        )}
        {review.isError && <ErrorMessage error={review.error} />}
      </Card>
      <ol className="grid gap-3 [&>*]:min-w-0">
        {c.topics.map((t, i) => <TopicEditor key={t.id} topic={t} number={i + 1} courseCode={c.code} />)}
      </ol>
    </section>
  )
}

function Saved({ when }: { when: boolean }) {
  return when ? <span className="text-xs font-medium text-emerald-700" role="status">Saved</span> : null
}

function TopicEditor({ topic, number, courseCode }: { topic: ManagedCourse['topics'][number]; number: number; courseCode: string }) {
  const queryClient = useQueryClient()
  const [open, setOpen] = useState(false)
  const [title, setTitle] = useState(topic.title)
  const [summary, setSummary] = useState(topic.summary ?? '')
  const save = useMutation({
    mutationFn: () => updateTopic(topic.id, title, summary),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['manage', 'course', courseCode] }),
  })
  return (
    <li data-testid="manage-topic">
      <Card className="p-0">
        <button type="button" onClick={() => setOpen(!open)} aria-expanded={open}
          className="flex w-full items-center gap-3 px-4 py-3 text-left">
          <span className="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-slate-100 text-xs font-semibold text-slate-600">{number}</span>
          <span className="min-w-0 flex-1 font-medium">{topic.title}</span>
          <span className="text-xs text-slate-500">{open ? 'Close' : 'Edit'}</span>
        </button>
        {open && (
          <div className="grid gap-5 border-t border-slate-100 px-4 pt-4 pb-5 [&>*]:min-w-0">
            <form className="grid gap-3" onSubmit={(e) => (e.preventDefault(), save.mutate())}>
              <Field label="Topic title">
                <input className={inputClass} value={title} onChange={(e) => (save.reset(), setTitle(e.target.value))} required maxLength={200} />
              </Field>
              <Field label="Summary" hint="Two sentences shown on the topic page and in the Knowledge Base.">
                <textarea className={`${inputClass} min-h-20`} value={summary} onChange={(e) => (save.reset(), setSummary(e.target.value))} maxLength={1000} />
              </Field>
              {save.isError && <ErrorMessage error={save.error} />}
              <div className="flex items-center gap-3">
                <Button type="submit" className="px-3 py-1.5" disabled={save.isPending}>Save topic</Button>
                <Saved when={save.isSuccess} />
              </div>
            </form>
            <ResourceEditor topic={topic} courseCode={courseCode} />
            <QuestionEditor topicId={topic.id} />
          </div>
        )}
      </Card>
    </li>
  )
}

const LINK_TYPES: ResourceType[] = ['lecture', 'video', 'textbook', 'past_questions']

function ResourceEditor({ topic, courseCode }: { topic: ManagedCourse['topics'][number]; courseCode: string }) {
  const links = topic.resources.filter((r) => r.url || r.type === 'textbook' || r.type === 'lecture' || r.type === 'video')
  return (
    <div>
      <h3 className="mb-2 text-sm font-semibold">Links</h3>
      <ul className="grid gap-2 [&>*]:min-w-0">
        {links.map((r) => <ResourceRow key={r.id} resource={r} topicId={topic.id} courseCode={courseCode} />)}
      </ul>
      <ResourceRow topicId={topic.id} courseCode={courseCode} />
    </div>
  )
}

function ResourceRow({ resource, topicId, courseCode }: {
  resource?: ManagedCourse['topics'][number]['resources'][number]; topicId: string; courseCode: string
}) {
  const queryClient = useQueryClient()
  const [editing, setEditing] = useState(false)
  const [adding, setAdding] = useState(false)
  const [title, setTitle] = useState(resource?.title ?? '')
  const [url, setUrl] = useState(resource?.url ?? '')
  const [type, setType] = useState<ResourceType>(resource?.type ?? 'video')
  const [linkType, setLinkType] = useState<BookLinkType>(resource?.link_type ?? 'buy')
  const save = useMutation({
    mutationFn: () => saveResource({ id: resource?.id ?? null, topicId, title, type, url, linkType: type === 'textbook' ? linkType : null }),
    onSuccess: () => {
      setEditing(false)
      setAdding(false)
      if (!resource) { setTitle(''); setUrl('') }
      queryClient.invalidateQueries({ queryKey: ['manage', 'course', courseCode] })
    },
  })
  const form = (
    <form className="mt-2 grid gap-2 rounded-xl bg-slate-50 p-3" onSubmit={(e) => (e.preventDefault(), save.mutate())} data-testid="resource-form">
      <div className="grid gap-2 sm:grid-cols-[2fr_1fr]">
        <input className={inputClass} value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title, e.g. Video: Fuzzy sets explained" aria-label="Title" required />
        <select className={inputClass} value={type} onChange={(e) => setType(e.target.value as ResourceType)} aria-label="Type" disabled={Boolean(resource)}>
          {LINK_TYPES.map((t) => <option key={t} value={t}>{RESOURCE_LABEL[t]}</option>)}
        </select>
      </div>
      <input className={inputClass} value={url} onChange={(e) => setUrl(e.target.value)} placeholder="https://…" aria-label="Link" type="url" required={!resource || resource.type !== 'textbook'} />
      {type === 'textbook' && (
        <select className={inputClass} value={linkType} onChange={(e) => setLinkType(e.target.value as BookLinkType)} aria-label="Link type">
          <option value="free">Read free online (a legal free copy)</option>
          <option value="buy">Buy or preview: publisher</option>
          <option value="preview">Buy or preview: Google Books</option>
        </select>
      )}
      {save.isError && <ErrorMessage error={save.error} />}
      <div className="flex gap-2">
        <Button type="submit" className="px-3 py-1.5" disabled={save.isPending}>{resource ? 'Save link' : 'Add link'}</Button>
        <Button type="button" variant="ghost" className="px-3 py-1.5" onClick={() => (setEditing(false), setAdding(false))}>Cancel</Button>
      </div>
    </form>
  )
  if (!resource) {
    return adding ? form : (
      <Button variant="secondary" className="mt-2 px-3 py-1.5" onClick={() => setAdding(true)}>Add a link</Button>
    )
  }
  return (
    <li className="rounded-xl ring-1 ring-slate-200" data-testid="manage-resource">
      <div className="flex items-center gap-2.5 p-2">
        <ResourceIcon type={resource.type} className="h-8 w-8" />
        <span className="min-w-0 flex-1 text-sm">
          <span className="block font-medium">{resource.title}</span>
          <span className="block truncate text-xs text-slate-500">{resource.url ?? 'No link (reading card only)'}</span>
        </span>
        <Button variant="ghost" className="px-2.5 py-1" onClick={() => setEditing(!editing)}>Fix</Button>
      </div>
      {editing && <div className="px-2 pb-2">{form}</div>}
    </li>
  )
}

function QuestionEditor({ topicId }: { topicId: string }) {
  const questions = useQuery({ queryKey: ['manage', 'questions', topicId], queryFn: () => listTopicQuestions(topicId) })
  return (
    <div>
      <h3 className="mb-2 text-sm font-semibold">Practice questions</h3>
      {questions.isPending && <Spinner />}
      {questions.isError && <ErrorMessage error={questions.error} />}
      {questions.data && (
        <ol className="grid gap-2 [&>*]:min-w-0">
          {questions.data.map((q) => <QuestionRow key={q.id} question={q} topicId={topicId} />)}
        </ol>
      )}
    </div>
  )
}

const FORMAT_LABEL: Record<ManagedQuestion['format'], string> = {
  single_choice: 'Single choice', true_false: 'True or false', multi_select: 'Select all that apply', odd_one_out: 'Odd one out',
}

function QuestionRow({ question: q, topicId }: { question: ManagedQuestion; topicId: string }) {
  const queryClient = useQueryClient()
  const [editing, setEditing] = useState(false)
  const [draft, setDraft] = useState(q)
  const refresh = () => queryClient.invalidateQueries({ queryKey: ['manage', 'questions', topicId] })
  const save = useMutation({ mutationFn: () => updateQuestion(draft), onSuccess: () => (setEditing(false), refresh()) })
  const hide = useMutation({ mutationFn: () => setQuestionHidden(q.id, q.status !== 'hidden'), onSuccess: refresh })
  const multi = q.format === 'multi_select'
  function toggleAnswer(key: string) {
    setDraft((d) => ({
      ...d,
      correct_answer: multi
        ? (d.correct_answer.includes(key) ? d.correct_answer.filter((k) => k !== key) : [...d.correct_answer, key])
        : [key],
    }))
  }
  return (
    <li className={`rounded-xl p-3 ring-1 ${q.status === 'hidden' ? 'bg-slate-50 ring-dashed ring-slate-300' : 'ring-slate-200'}`}
      data-testid="manage-question" data-status={q.status}>
      <div className="flex flex-wrap items-start justify-between gap-2">
        <p className="min-w-0 flex-1 text-sm font-medium">{q.stem}</p>
        <span className="text-[11px] font-semibold tracking-wide text-slate-500 uppercase">{FORMAT_LABEL[q.format]}{q.status === 'hidden' ? ' · hidden' : ''}</span>
      </div>
      {!editing ? (
        <>
          <ul className="mt-2 grid gap-1 text-sm">
            {q.options.map((o) => (
              <li key={o.key} className={q.correct_answer.includes(o.key) ? 'font-medium text-emerald-700' : 'text-slate-600'}>
                {q.correct_answer.includes(o.key) ? '✓ ' : '• '}{o.text}
              </li>
            ))}
          </ul>
          <p className="mt-2 text-xs text-slate-500">{q.explanation}</p>
          <div className="mt-2 flex gap-2">
            <Button variant="secondary" className="px-2.5 py-1" onClick={() => (setDraft(q), setEditing(true))}>Edit</Button>
            <Button variant="ghost" className="px-2.5 py-1" onClick={() => hide.mutate()} disabled={hide.isPending} data-testid="toggle-hidden">
              {q.status === 'hidden' ? 'Show in quizzes' : 'Hide from quizzes'}
            </Button>
          </div>
          {hide.isError && <ErrorMessage error={hide.error} />}
        </>
      ) : (
        <form className="mt-2 grid gap-2" onSubmit={(e) => (e.preventDefault(), save.mutate())}>
          <textarea className={`${inputClass} min-h-16`} value={draft.stem} onChange={(e) => setDraft({ ...draft, stem: e.target.value })} aria-label="Question" required />
          {draft.options.map((o, i) => (
            <label key={o.key} className="flex items-center gap-2">
              <input type={multi ? 'checkbox' : 'radio'} name={`answer-${q.id}`} checked={draft.correct_answer.includes(o.key)}
                onChange={() => toggleAnswer(o.key)} aria-label={`Option ${o.key} is correct`} />
              <input className={inputClass} value={o.text} disabled={q.format === 'true_false'} aria-label={`Option ${o.key}`}
                onChange={(e) => setDraft({ ...draft, options: draft.options.map((x, j) => (j === i ? { ...x, text: e.target.value } : x)) })} />
            </label>
          ))}
          <textarea className={`${inputClass} min-h-14`} value={draft.explanation} onChange={(e) => setDraft({ ...draft, explanation: e.target.value })} aria-label="Explanation" required />
          {save.isError && <ErrorMessage error={save.error} />}
          <div className="flex gap-2">
            <Button type="submit" className="px-3 py-1.5" disabled={save.isPending}>Save question</Button>
            <Button type="button" variant="ghost" className="px-3 py-1.5" onClick={() => setEditing(false)}>Cancel</Button>
          </div>
        </form>
      )}
    </li>
  )
}

// -- Edit history --------------------------------------------------------------------------

function show(value: unknown): string {
  if (value === null || value === undefined || value === '') return '(empty)'
  const text = typeof value === 'string' ? value : JSON.stringify(value)
  return text.length > 120 ? text.slice(0, 117) + '…' : text
}

export function ManageHistoryPage() {
  const audit = useQuery({ queryKey: ['manage', 'audit'], queryFn: () => listAudit(100) })
  if (audit.isPending) return <Spinner />
  if (audit.isError) return <ErrorMessage error={audit.error} />
  if (audit.data.length === 0) return <Card><p className="text-sm text-slate-600">No edits yet. Changes made in Requests and Courses appear here.</p></Card>
  return (
    <ul className="grid gap-2 [&>*]:min-w-0" aria-label="Edit history">
      {audit.data.map((a) => (
        <li key={a.id} data-testid="audit-entry">
          <Card className="p-3">
            <div className="flex flex-wrap items-baseline justify-between gap-2">
              <p className="text-sm font-medium">{a.summary}</p>
              <p className="text-xs text-slate-500">{a.actor ?? 'Unknown'} · {timeAgo(a.created_at)}</p>
            </div>
            <ul className="mt-1.5 grid gap-0.5 text-xs text-slate-600">
              {Object.entries(a.changes).map(([field, c]) => (
                <li key={field} className="break-words"><span className="font-semibold">{field}</span>: {show(c.from)} → {show(c.to)}</li>
              ))}
            </ul>
          </Card>
        </li>
      ))}
    </ul>
  )
}

