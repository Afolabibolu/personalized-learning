import { Link, Navigate, useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { listCourses, type CourseSummary } from '../api/courses'
import { CourseCard, useEnrolmentToggle } from '../components/CourseCard'
import { Card, ErrorMessage, PageHeader, Spinner } from '../components/ui'
import { bySemester, isLevel, semesterName } from '../lib/levels'

/** One level's courses, split into first and second semester. */
export function CourseLevelPage() {
  const level = Number(useParams().level)
  const courses = useQuery({ queryKey: ['courses'], queryFn: listCourses })
  const toggle = useEnrolmentToggle()
  if (!isLevel(level)) return <Navigate to="/courses" replace />

  const list = courses.data?.filter((c) => c.level === level) ?? []
  const card = (c: CourseSummary) => (
    <CourseCard key={c.id} course={c} onToggle={() => toggle.mutate(c)} busy={toggle.isPending && toggle.variables?.id === c.id} />
  )

  return (
    <>
      <Link to="/courses" className="mb-4 inline-flex items-center gap-1 text-sm font-semibold text-brand-600 hover:text-brand-700">
        <svg viewBox="0 0 20 20" fill="currentColor" aria-hidden className="h-4 w-4 rotate-180">
          <path d="M7.2 4.2a1 1 0 0 1 1.4 0l5.1 5.1a1 1 0 0 1 0 1.4l-5.1 5.1a1 1 0 1 1-1.4-1.4L11.6 10 7.2 5.6a1 1 0 0 1 0-1.4Z" />
        </svg>
        Back to all levels
      </Link>
      <PageHeader eyebrow="Courses" title={`${level} level courses`}>
        {courses.data && `${list.length} ${list.length === 1 ? 'course' : 'courses'}. `}
        Add the ones you are taking, and recommendations and reminders will cover them.
      </PageHeader>

      {courses.isPending && <Spinner />}
      {courses.isError && <ErrorMessage error={courses.error} />}
      {toggle.isError && <ErrorMessage error={toggle.error} />}

      {courses.data && list.length === 0 && (
        <Card>
          <p className="text-sm text-slate-600">
            No courses yet.{' '}
            <Link to="/courses/request" className="font-semibold text-brand-600 hover:text-brand-700">
              Request one.
            </Link>
          </p>
        </Card>
      )}

      {bySemester(list).map(([semester, group]) => (
        <section key={semester ?? 'none'} aria-labelledby={`semester-${semester ?? 'none'}`} className="mb-8 grid gap-4">
          <h2 id={`semester-${semester ?? 'none'}`} className="text-sm font-semibold tracking-wide text-slate-500 uppercase">
            {semesterName(semester)} <span className="font-normal normal-case">· {group.length}</span>
          </h2>
          {group.map(card)}
        </section>
      ))}
    </>
  )
}
