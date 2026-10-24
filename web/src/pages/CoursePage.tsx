import { Link, useParams } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { getCourse, listEnrolledCourseIds, listQuizHistory, setEnrolled } from '../api/courses'
import { formatDate } from '../lib/format'
import { Button, ButtonLink, Card, ErrorMessage, PageHeader, SampleBadge, ScoreBadge, ScoreBar, Spinner } from '../components/ui'

export function CoursePage() {
  const { courseId = '' } = useParams()
  const course = useQuery({ queryKey: ['course', courseId], queryFn: () => getCourse(courseId) })
  const history = useQuery({ queryKey: ['quizHistory', courseId], queryFn: () => listQuizHistory(courseId) })
  const enrolled = useQuery({ queryKey: ['course', 'enrolled'], queryFn: listEnrolledCourseIds })
  const queryClient = useQueryClient()
  const isMine = enrolled.data?.has(courseId) ?? false
  const toggle = useMutation({
    mutationFn: () => setEnrolled(courseId, !isMine),
    onSuccess: () => {
      for (const key of ['courses', 'dashboard', 'topicsByCourse', 'course']) queryClient.invalidateQueries({ queryKey: [key] })
    },
  })

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
        {!data.is_reviewed && (
          <span className="mb-2 block">
            <SampleBadge />
          </span>
        )}
        {data.description}
      </PageHeader>

      {enrolled.data && (
        <div className="-mt-3 mb-6 flex flex-wrap items-center gap-3 text-sm text-slate-600">
          <span>{isMine ? 'In your courses.' : 'Not in your courses yet.'}</span>
          <Button variant={isMine ? 'ghost' : 'secondary'} className="px-3 py-1.5" onClick={() => toggle.mutate()} disabled={toggle.isPending}>
            {isMine ? 'Remove from my courses' : 'Add to my courses'}
          </Button>
        </div>
      )}

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

      <h2 className="mt-8 mb-3 text-sm font-semibold tracking-wide text-slate-500 uppercase">Quiz history</h2>
      <Card className="p-0" >
        {history.isPending ? (
          <Spinner />
        ) : !history.data || history.data.length === 0 ? (
          <div className="px-5 py-6 text-center text-sm text-slate-500">
            No quizzes yet.{' '}
            {data.diagnostic_quiz_id && (
              <Link to={`/quiz/${data.diagnostic_quiz_id}`} className="font-semibold text-brand-600 hover:text-brand-700">
                Take the diagnostic quiz
              </Link>
            )}
          </div>
        ) : (
          <table className="w-full text-sm" data-testid="quiz-history">
            <thead>
              <tr className="border-b border-slate-100 text-left text-xs text-slate-500">
                <th className="px-5 py-2.5 font-medium">Date</th>
                <th className="px-2 py-2.5 font-medium">Quiz</th>
                <th className="px-5 py-2.5 text-right font-medium">Score</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {history.data.map((h) => (
                <tr key={h.attempt_id} className="hover:bg-slate-50">
                  <td className="px-5 py-2.5 whitespace-nowrap text-slate-500">{formatDate(h.completed_at)}</td>
                  <td className="px-2 py-2.5">
                    <Link to={`/attempts/${h.attempt_id}`} className="font-medium hover:text-brand-700">
                      {h.quiz_title}
                    </Link>
                  </td>
                  <td className="px-5 py-2.5 text-right">
                    <ScoreBadge score={h.score} />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </Card>
    </>
  )
}
