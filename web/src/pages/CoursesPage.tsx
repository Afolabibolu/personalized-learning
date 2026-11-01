import { useState } from 'react'
import { Link } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { listCourses, setEnrolled, type CourseSummary } from '../api/courses'
import { getProfile } from '../api/profile'
import { Button, ButtonLink, Card, ErrorMessage, PageHeader, SampleBadge, Spinner, inputClass } from '../components/ui'

function CourseCard({ course, onToggle, busy }: { course: CourseSummary; onToggle: () => void; busy: boolean }) {
  return (
    <Card className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between" >
      <div data-testid="course-card" data-code={course.code}>
        <div className="flex flex-wrap items-center gap-2">
          <p className="text-xs font-semibold tracking-wide text-brand-600 uppercase">{course.code}</p>
          {!course.is_reviewed && <SampleBadge />}
        </div>
        <h2 className="text-lg font-semibold">{course.title}</h2>
        <p className="mt-1 text-sm text-slate-500">
          {course.topic_count} topics
          {course.diagnostic_taken && <span className="text-emerald-600"> · Diagnostic done</span>}
        </p>
      </div>
      <div className="flex shrink-0 flex-wrap gap-2">
        {course.enrolled && !course.diagnostic_taken && course.diagnostic_quiz_id && (
          <ButtonLink to={`/quiz/${course.diagnostic_quiz_id}`}>Take diagnostic quiz</ButtonLink>
        )}
        <ButtonLink to={`/courses/${course.id}`} variant={course.enrolled && course.diagnostic_taken ? 'primary' : 'secondary'}>
          View course
        </ButtonLink>
        <Button variant={course.enrolled ? 'ghost' : 'primary'} onClick={onToggle} disabled={busy}>
          {course.enrolled ? 'Remove' : 'Add to my courses'}
        </Button>
      </div>
    </Card>
  )
}

/** Courses grouped by level, highest first (500, 400, ...); courses with no level go last. */
function levels(courses: CourseSummary[]): [number, CourseSummary[]][] {
  const groups = new Map<number, CourseSummary[]>()
  for (const c of courses) groups.set(c.level ?? 0, [...(groups.get(c.level ?? 0) ?? []), c])
  return [...groups].sort(([a], [b]) => (b || -1) - (a || -1))
}

export function CoursesPage() {
  const queryClient = useQueryClient()
  const courses = useQuery({ queryKey: ['courses'], queryFn: listCourses })
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const [search, setSearch] = useState('')
  const [levelFilter, setLevelFilter] = useState<number | null>(null)
  // Level groups the student opened or closed; the rest follow the default (only their own level open).
  const [toggled, setToggled] = useState<Record<number, boolean>>({})
  const toggle = useMutation({
    mutationFn: (c: CourseSummary) => setEnrolled(c.id, !c.enrolled),
    onSuccess: () => {
      for (const key of ['courses', 'dashboard', 'topicsByCourse', 'course']) queryClient.invalidateQueries({ queryKey: [key] })
    },
  })

  const mine = courses.data?.filter((c) => c.enrolled) ?? []
  const others = courses.data?.filter((c) => !c.enrolled) ?? []
  const query = search.trim().toLowerCase()
  const allGroups = levels(others)
  const groups = levels(
    others.filter(
      (c) =>
        (levelFilter === null || (c.level ?? 0) === levelFilter) &&
        (!query || c.code.toLowerCase().includes(query) || c.title.toLowerCase().includes(query)),
    ),
  )
  // A search or a chosen level opens every group shown.
  const isOpen = (level: number) => Boolean(query) || levelFilter !== null || (toggled[level] ?? level === profile.data?.level)
  const setAll = (open: boolean) => setToggled(Object.fromEntries(groups.map(([level]) => [level, open])))
  const pill = (active: boolean) =>
    `rounded-full px-3 py-1 text-xs font-semibold ring-1 transition ${
      active ? 'bg-brand-600 text-white ring-brand-600' : 'bg-white text-slate-600 ring-slate-300 hover:ring-brand-500'
    }`
  const card = (c: CourseSummary) => (
    <CourseCard key={c.id} course={c} onToggle={() => toggle.mutate(c)} busy={toggle.isPending && toggle.variables?.id === c.id} />
  )

  return (
    <>
      <PageHeader eyebrow="Courses" title="Your courses">
        Start with a diagnostic quiz on each course to see which topics need attention. Recommendations and reminders cover
        the courses you add here.
      </PageHeader>

      {courses.isPending && <Spinner />}
      {courses.isError && <ErrorMessage error={courses.error} />}
      {toggle.isError && <ErrorMessage error={toggle.error} />}

      {courses.data && (
        <section aria-labelledby="my-courses" className="grid gap-4">
          <h2 id="my-courses" className="sr-only">My courses</h2>
          {mine.map(card)}
          {mine.length === 0 && (
            <Card>
              <p className="text-sm text-slate-600" data-testid="no-courses">
                No courses yet. Add a course below to get recommendations and reminders for it.
              </p>
            </Card>
          )}
        </section>
      )}

      {others.length > 0 && (
        <section aria-labelledby="more-courses" className="mt-10 grid gap-4">
          <div>
            <h2 id="more-courses" className="text-lg font-semibold">More courses</h2>
            <p className="text-sm text-slate-500">
              Every course in the Knowledge Base. Sample courses were built by the course ingestion pipeline and are waiting
              for a lecturer to review them.
            </p>
          </div>
          <input
            type="search"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search by course code or title"
            aria-label="Search more courses"
            className={inputClass}
          />
          <div className="flex flex-wrap items-center justify-between gap-2">
            <div className="flex flex-wrap gap-2" role="group" aria-label="Which level to show">
              {[null, ...allGroups.map(([level]) => level)].map((level) => (
                <button
                  key={level ?? 'all'}
                  type="button"
                  aria-pressed={levelFilter === level}
                  onClick={() => setLevelFilter(level)}
                  className={pill(levelFilter === level)}
                >
                  {level === null ? 'All levels' : level ? `${level}` : 'Other'}
                </button>
              ))}
            </div>
            {!query && levelFilter === null && groups.length > 1 && (
              <div className="flex gap-3 text-xs font-semibold">
                <button type="button" onClick={() => setAll(true)} className="text-brand-600 hover:text-brand-700">
                  Expand all
                </button>
                <button type="button" onClick={() => setAll(false)} className="text-slate-500 hover:text-slate-800">
                  Collapse all
                </button>
              </div>
            )}
          </div>
          {groups.length === 0 && (
            <Card className="text-center">
              <p className="text-sm text-slate-600">No courses match “{search.trim()}”.</p>
              <button onClick={() => setSearch('')} className="mt-2 text-sm font-semibold text-brand-600 hover:text-brand-700">
                Clear the search
              </button>
            </Card>
          )}
          {groups.map(([level, list]) => {
            const open = isOpen(level)
            return (
              <div key={level} className="grid gap-4" aria-labelledby={`level-${level}`} role="group">
                <h3 className="mt-2">
                  <button
                    type="button"
                    aria-expanded={open}
                    aria-controls={`courses-level-${level}`}
                    disabled={Boolean(query) || levelFilter !== null}
                    onClick={() => setToggled((t) => ({ ...t, [level]: !open }))}
                    className="flex w-full items-center gap-2 rounded-xl bg-white px-4 py-3 text-left ring-1 ring-slate-200 hover:ring-brand-500 disabled:cursor-default disabled:hover:ring-slate-200"
                  >
                    <svg viewBox="0 0 20 20" fill="currentColor" aria-hidden className={`h-4 w-4 shrink-0 text-slate-400 transition ${open ? 'rotate-90' : ''}`}>
                      <path d="M7.2 4.2a1 1 0 0 1 1.4 0l5.1 5.1a1 1 0 0 1 0 1.4l-5.1 5.1a1 1 0 1 1-1.4-1.4L11.6 10 7.2 5.6a1 1 0 0 1 0-1.4Z" />
                    </svg>
                    <span id={`level-${level}`} className="text-sm font-semibold tracking-wide text-slate-700 uppercase">
                      {level ? `${level} level` : 'Other courses'}
                    </span>
                    <span className="ml-auto text-xs text-slate-500">
                      {list.length} {list.length === 1 ? 'course' : 'courses'}
                      {level !== 0 && level === profile.data?.level && ' · your level'}
                    </span>
                  </button>
                </h3>
                {open && (
                  <div id={`courses-level-${level}`} className="grid gap-4">
                    {list.map(card)}
                  </div>
                )}
              </div>
            )
          })}
        </section>
      )}

      <Card className="mt-10 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h2 className="font-semibold">Can't find your course?</h2>
          <p className="text-sm text-slate-500">Request it, and it will be added to your courses once its materials are in.</p>
        </div>
        <ButtonLink to="/courses/request" variant="secondary" className="shrink-0">
          Request a course
        </ButtonLink>
      </Card>

      <p className="mt-8 text-center text-sm text-slate-500">
        Studied something today?{' '}
        <Link to="/log" className="font-semibold text-brand-600 hover:text-brand-700">
          Log a study session
        </Link>
      </p>
    </>
  )
}
