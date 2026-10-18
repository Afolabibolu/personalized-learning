import { Link, useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { getAttemptReview } from '../api/quiz'
import type { ReviewedQuestion } from '../api/types'
import { ButtonLink, Card, ErrorMessage, PageHeader, ScoreBar, Spinner, scoreTone } from '../components/ui'

export function ResultsPage() {
  const { attemptId = '' } = useParams()
  const review = useQuery({ queryKey: ['review', attemptId], queryFn: () => getAttemptReview(attemptId) })

  if (review.isPending) return <Spinner />
  if (review.isError) return <ErrorMessage error={review.error} />

  const { data } = review
  const correct = data.questions.filter((q) => q.is_correct).length
  const tone = scoreTone(Number(data.score))
  const weakest = [...data.topic_scores].sort((a, b) => a.score - b.score)[0]

  return (
    <>
      <PageHeader eyebrow={data.quiz.kind === 'diagnostic' ? 'Diagnostic results' : 'Quiz results'} title={data.quiz.title} />

      <Card className="mb-6 flex flex-col items-center gap-1 py-8 text-center">
        <p className={`text-5xl font-bold ${tone.text}`}>{Math.round(Number(data.score))}%</p>
        <p className="text-sm text-slate-600">
          {correct} of {data.questions.length} correct
        </p>
      </Card>

      <section className="mb-8">
        <h2 className="mb-3 text-sm font-semibold tracking-wide text-slate-500 uppercase">Score per topic</h2>
        <Card className="grid gap-4">
          {data.topic_scores.map((t) => (
            <Link key={t.topic_id} to={`/topics/${t.topic_id}`} className="group block">
              <div className="mb-1.5 flex items-center justify-between gap-3 text-sm">
                <span className="font-medium group-hover:text-brand-700">{t.topic_title}</span>
                <span className="shrink-0 text-slate-500">
                  {t.correct}/{t.total}
                </span>
              </div>
              <ScoreBar score={Number(t.score)} />
            </Link>
          ))}
        </Card>
        {weakest && Number(weakest.score) < 50 && (
          <p className="mt-3 text-sm text-slate-600">
            <span className="font-semibold text-red-600">{weakest.topic_title}</span> needs attention.{' '}
            <Link to={`/topics/${weakest.topic_id}`} className="font-semibold text-brand-600 hover:text-brand-700">
              Go to topic →
            </Link>
          </p>
        )}
      </section>

      <section>
        <h2 className="mb-3 text-sm font-semibold tracking-wide text-slate-500 uppercase">Answers</h2>
        <ol className="grid gap-3">
          {data.questions.map((q, i) => (
            <AnswerCard key={q.id} question={q} number={i + 1} />
          ))}
        </ol>
      </section>

      <div className="mt-8 flex flex-col gap-2 sm:flex-row">
        <ButtonLink to={`/courses/${data.quiz.course_id}`}>Back to course</ButtonLink>
        <ButtonLink to="/log" variant="secondary">
          Log a study session
        </ButtonLink>
      </div>
    </>
  )
}

function AnswerCard({ question, number }: { question: ReviewedQuestion; number: number }) {
  const chosen = new Set(question.response)
  const correct = new Set(question.correct_answer)

  return (
    <li className="rounded-2xl bg-white p-5 shadow-sm ring-1 ring-slate-200">
      <div className="mb-3 flex items-start justify-between gap-3">
        <p className="font-medium">
          <span className="mr-1 text-slate-400">{number}.</span> {question.stem}
        </p>
        <ScoreBadgeMini correct={question.is_correct} />
      </div>
      <ul className="grid gap-1.5 text-sm">
        {question.options.map((o) => {
          const isCorrect = correct.has(o.key)
          const isChosen = chosen.has(o.key)
          const style = isCorrect
            ? 'bg-emerald-50 text-emerald-800 ring-emerald-200'
            : isChosen
              ? 'bg-red-50 text-red-800 ring-red-200'
              : 'text-slate-600 ring-transparent'
          return (
            <li key={o.key} className={`flex items-center justify-between gap-2 rounded-lg px-3 py-2 ring-1 ${style}`}>
              <span>{o.text}</span>
              <span className="shrink-0 text-xs font-semibold">
                {isCorrect && isChosen && 'Your answer ✓'}
                {isCorrect && !isChosen && 'Correct answer'}
                {!isCorrect && isChosen && 'Your answer ✗'}
              </span>
            </li>
          )
        })}
      </ul>
      {question.response.length === 0 && <p className="mt-2 text-xs text-slate-500">Not answered.</p>}
      <p className="mt-3 rounded-lg bg-slate-50 px-3 py-2 text-sm text-slate-700">{question.explanation}</p>
    </li>
  )
}

function ScoreBadgeMini({ correct }: { correct: boolean }) {
  return correct ? (
    <span className="shrink-0 rounded-full bg-emerald-50 px-2.5 py-0.5 text-xs font-semibold text-emerald-700 ring-1 ring-emerald-200">Correct</span>
  ) : (
    <span className="shrink-0 rounded-full bg-red-50 px-2.5 py-0.5 text-xs font-semibold text-red-700 ring-1 ring-red-200">Incorrect</span>
  )
}
