import { Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { listCourses, type CourseSummary } from '../api/courses'
import { getProfile } from '../api/profile'
import { CourseCard, useEnrolmentToggle } from '../components/CourseCard'
import { ButtonLink, Card, ErrorMessage, PageHeader, Spinner } from '../components/ui'
import { LEVELS } from '../lib/levels'

export function CoursesPage() {
  const courses = useQuery({ queryKey: ['courses'], queryFn: listCourses })
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const toggle = useEnrolmentToggle()

  const mine = courses.data?.filter((c) => c.enrolled) ?? []
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
                No courses yet. Browse a level below and add a course to get recommendations and reminders for it.
              </p>
            </Card>
          )}
        </section>
      )}

      {courses.data && (
        <section aria-labelledby="browse-courses" className="mt-10 grid gap-4">
          <div>
            <h2 id="browse-courses" className="text-lg font-semibold">Browse courses</h2>
            <p className="text-sm text-slate-500">
              Pick a level to see its courses by semester. Sample courses were built by the course ingestion pipeline and are
              waiting for a lecturer to review them.
            </p>
          </div>
          <ul className="grid grid-cols-2 gap-3 lg:grid-cols-3">
            {LEVELS.map((level) => {
              const count = courses.data.filter((c) => c.level === level).length
              const added = courses.data.filter((c) => c.level === level && c.enrolled).length
              const own = profile.data?.level === level
              const title = (
                <span className="flex flex-wrap items-center justify-between gap-x-2 gap-y-1">
                  <span id={`level-${level}`} className="text-lg font-semibold">{level} level</span>
                  {own && <span className="rounded-full bg-brand-50 px-2 py-0.5 text-xs font-semibold text-brand-700">Your level</span>}
                </span>
              )
              return (
                <li key={level} data-testid="level-card" data-level={level} data-count={count}>
                  {count > 0 ? (
                    <Link
                      to={`/courses/level/${level}`}
                      aria-labelledby={`level-${level}`}
                      className="block h-full rounded-2xl bg-white p-4 shadow-sm sm:p-5 ring-1 ring-slate-200 transition hover:ring-brand-500"
                    >
                      {title}
                      <span className="mt-1 block text-sm text-slate-500">
                        {count} {count === 1 ? 'course' : 'courses'}
                        {added > 0 && <span className="text-emerald-600"> · {added} added</span>}
                      </span>
                      <span className="mt-3 inline-flex items-center gap-1 text-sm font-semibold text-brand-600">
                        View courses
                        <svg viewBox="0 0 20 20" fill="currentColor" aria-hidden className="h-4 w-4">
                          <path d="M7.2 4.2a1 1 0 0 1 1.4 0l5.1 5.1a1 1 0 0 1 0 1.4l-5.1 5.1a1 1 0 1 1-1.4-1.4L11.6 10 7.2 5.6a1 1 0 0 1 0-1.4Z" />
                        </svg>
                      </span>
                    </Link>
                  ) : (
                    <div className="h-full rounded-2xl bg-slate-50 p-4 ring-1 sm:p-5 ring-slate-200">
                      {title}
                      <span className="mt-1 block text-sm text-slate-500">
                        No courses yet.{' '}
                        <Link to="/courses/request" className="font-semibold text-brand-600 hover:text-brand-700">
                          Request one.
                        </Link>
                      </span>
                    </div>
                  )}
                </li>
              )
            })}
          </ul>
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
