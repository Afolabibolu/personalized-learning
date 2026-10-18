import { Link, useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { getCourse } from '../api/courses'
import { ButtonLink, Card, ErrorMessage, PageHeader, ScoreBadge, ScoreBar, Spinner } from '../components/ui'

export function CoursePage() {
  const { courseId = '' } = useParams()
  const course = useQuery({ queryKey: ['course', courseId], queryFn: () => getCourse(courseId) })

  if (course.isPending) return <Spinner />
  if (course.isError) return <ErrorMessage error={course.error} />

  const { data } = course
  const scored = data.topics.filter((t) => t.latest_score !== null)

  return (
    <>
      <Link to="/courses" className="mb-4 inline-block text-sm text-slate-500 hover:text-slate-900">
        ← All courses
      </Link>
      <PageHeader eyebrow={data.code} title={data.title}>
        {data.description}
      </PageHeader>

      {scored.length === 0 && data.diagnostic_quiz_id && (
        <Card className="mb-6 bg-brand-50 ring-brand-100">
          <h2 className="font-semibold">Start with the diagnostic quiz</h2>
          <p className="mt-1 text-sm text-slate-600">
            A few questions from every topic give you a score per topic, so you know where to focus.
          </p>
          <ButtonLink to={`/quiz/${data.diagnostic_quiz_id}`} className="mt-4">
            Take diagnostic quiz
          </ButtonLink>
        </Card>
      )}

      <h2 className="mb-3 text-sm font-semibold tracking-wide text-slate-500 uppercase">Topics</h2>
      <ol className="grid gap-3">
        {data.topics.map((topic) => (
          <li key={topic.id}>
            <Link to={`/topics/${topic.id}`} className="block rounded-2xl bg-white p-4 shadow-sm ring-1 ring-slate-200 transition hover:ring-brand-500">
              <div className="flex items-start justify-between gap-3">
                <div className="flex gap-3">
                  <span className="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-slate-100 text-xs font-semibold text-slate-600">
                    {topic.sequence_order}
                  </span>
                  <span className="font-medium">{topic.title}</span>
                </div>
                {topic.latest_score !== null && <ScoreBadge score={topic.latest_score} />}
              </div>
              {topic.latest_score !== null && (
                <div className="mt-3 pl-10">
                  <ScoreBar score={topic.latest_score} />
                </div>
              )}
            </Link>
          </li>
        ))}
      </ol>
    </>
  )
}
