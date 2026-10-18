import { Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { listCourses } from '../api/courses'
import { getProfile } from '../api/profile'
import { ButtonLink, Card, ErrorMessage, PageHeader, Spinner } from '../components/ui'

export function HomePage() {
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const courses = useQuery({ queryKey: ['courses'], queryFn: listCourses })

  const firstName = profile.data?.full_name?.split(' ')[0]

  return (
    <>
      <PageHeader eyebrow="Your courses" title={firstName ? `Hi ${firstName}` : 'Hi there'}>
        Start with a diagnostic quiz on each course to see which topics need attention.
      </PageHeader>

      {courses.isPending && <Spinner />}
      {courses.isError && <ErrorMessage error={courses.error} />}

      <div className="grid gap-4">
        {courses.data?.map((course) => (
          <Card key={course.id} className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <p className="text-xs font-semibold tracking-wide text-brand-600 uppercase">{course.code}</p>
              <h2 className="text-lg font-semibold">{course.title}</h2>
              <p className="mt-1 text-sm text-slate-500">
                {course.topic_count} topics
                {course.diagnostic_taken && <span className="text-emerald-600"> · Diagnostic done</span>}
              </p>
            </div>
            <div className="flex shrink-0 gap-2">
              {!course.diagnostic_taken && course.diagnostic_quiz_id && (
                <ButtonLink to={`/quiz/${course.diagnostic_quiz_id}`}>Take diagnostic quiz</ButtonLink>
              )}
              <ButtonLink to={`/courses/${course.id}`} variant={course.diagnostic_taken ? 'primary' : 'secondary'}>
                View course
              </ButtonLink>
            </div>
          </Card>
        ))}
      </div>

      {courses.data?.length === 0 && (
        <Card>
          <p className="text-sm text-slate-600">
            No courses yet. Load content with <code>python content/load.py</code>.
          </p>
        </Card>
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
