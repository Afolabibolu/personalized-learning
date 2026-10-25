import { Link } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { listCourses, setEnrolled, type CourseSummary } from '../api/courses'
import { Button, ButtonLink, Card, ErrorMessage, PageHeader, SampleBadge, Spinner } from '../components/ui'

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
  const toggle = useMutation({
    mutationFn: (c: CourseSummary) => setEnrolled(c.id, !c.enrolled),
    onSuccess: () => {
      for (const key of ['courses', 'dashboard', 'topicsByCourse', 'course']) queryClient.invalidateQueries({ queryKey: [key] })
    },
  })

  const mine = courses.data?.filter((c) => c.enrolled) ?? []
  const others = courses.data?.filter((c) => !c.enrolled) ?? []
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
          {levels(others).map(([level, list]) => (
            <div key={level} className="grid gap-4" aria-labelledby={`level-${level}`} role="group">
              <h3 id={`level-${level}`} className="mt-2 text-xs font-semibold tracking-wide text-slate-500 uppercase">
                {level ? `${level} level` : 'Other courses'}
              </h3>
              {list.map(card)}
            </div>
          ))}
        </section>
      )}

      <p className="mt-8 text-center text-sm text-slate-500">
        Studied something today?{' '}
        <Link to="/log" className="font-semibold text-brand-600 hover:text-brand-700">
          Log a study session
        </Link>
      </p>
    </>
  )
}
