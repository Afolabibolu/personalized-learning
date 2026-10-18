import { useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { triggerRecommendations } from '../api/ml'
import { getQuiz, startQuiz, submitQuiz } from '../api/quiz'
import type { StartedQuiz } from '../api/types'
import { FORMAT_LABEL, QuestionInput } from '../components/QuestionInputs'
import { Button, Card, ErrorMessage, PageHeader, ProgressBar, Spinner } from '../components/ui'

export function QuizPage() {
  const { quizId = '' } = useParams()
  const quiz = useQuery({ queryKey: ['quiz', quizId], queryFn: () => getQuiz(quizId) })
  // start_quiz creates an attempt, so it runs on a button press, never on mount.
  const start = useMutation({ mutationFn: () => startQuiz(quizId) })

  if (quiz.isPending) return <Spinner />
  if (quiz.isError) return <ErrorMessage error={quiz.error} />

  if (start.data) return <QuizPlayer started={start.data} />

  const { data } = quiz
  const isDiagnostic = data.kind === 'diagnostic'

  return (
    <div className="mx-auto max-w-lg">
      <PageHeader eyebrow={`${data.course_code} · ${isDiagnostic ? 'Diagnostic quiz' : 'Topic quiz'}`} title={data.title} />
      <Card>
        <dl className="grid grid-cols-2 gap-4 text-sm">
          <div>
            <dt className="text-slate-500">Questions</dt>
            <dd className="text-lg font-semibold">{data.question_count}</dd>
          </div>
          <div>
            <dt className="text-slate-500">Covers</dt>
            <dd className="text-lg font-semibold">{isDiagnostic ? 'Every topic' : data.topic_title}</dd>
          </div>
        </dl>
        <p className="mt-4 text-sm text-slate-600">
          {isDiagnostic
            ? 'A few questions from each topic. Your results show a score per topic, so you can see which ones need attention.'
            : "Questions you haven't seen come first. You'll see the correct answers and explanations at the end."}
        </p>
        {start.isError && (
          <div className="mt-4">
            <ErrorMessage error={start.error} />
          </div>
        )}
        <Button className="mt-5 w-full" onClick={() => start.mutate()} disabled={start.isPending}>
          {start.isPending ? 'Preparing questions…' : 'Start quiz'}
        </Button>
      </Card>
    </div>
  )
}

function QuizPlayer({ started }: { started: StartedQuiz }) {
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const [index, setIndex] = useState(0)
  const [responses, setResponses] = useState<Record<string, string[]>>({})

  const questions = started.questions
  const question = questions[index]
  const answered = questions.filter((q) => (responses[q.id] ?? []).length > 0).length
  const isLast = index === questions.length - 1

  const submit = useMutation({
    mutationFn: () => submitQuiz(started.attempt_id, responses),
    onSuccess: (review) => {
      queryClient.setQueryData(['review', review.attempt_id], review)
      // Scores changed everywhere they are shown.
      queryClient.invalidateQueries({ queryKey: ['courses'] })
      queryClient.invalidateQueries({ queryKey: ['course'] })
      queryClient.invalidateQueries({ queryKey: ['topic'] })
      queryClient.invalidateQueries({ queryKey: ['dashboard'] })
      triggerRecommendations()
      navigate(`/attempts/${review.attempt_id}`, { replace: true })
    },
  })

  function handleSubmit() {
    const missing = questions.length - answered
    if (missing > 0 && !window.confirm(`You have ${missing} unanswered question${missing > 1 ? 's' : ''}. Submit anyway?`)) return
    submit.mutate()
  }

  return (
    <div className="mx-auto max-w-xl">
      <div className="mb-5">
        <div className="mb-2 flex items-center justify-between text-sm">
          <Link to="/" className="text-slate-500 hover:text-slate-900">
            {started.quiz.title}
          </Link>
          <span className="font-medium text-slate-700">
            {index + 1} / {questions.length}
          </span>
        </div>
        <ProgressBar value={((index + 1) / questions.length) * 100} />
      </div>

      <Card>
        <p className="mb-2 text-xs font-semibold tracking-wide text-brand-600 uppercase">{FORMAT_LABEL[question.format]}</p>
        <h1 className="mb-5 text-lg leading-snug font-semibold">{question.stem}</h1>
        <QuestionInput
          key={question.id}
          question={question}
          value={responses[question.id] ?? []}
          onChange={(value) => setResponses((prev) => ({ ...prev, [question.id]: value }))}
        />
      </Card>

      {submit.isError && (
        <div className="mt-4">
          <ErrorMessage error={submit.error} />
        </div>
      )}

      <div className="mt-5 flex items-center justify-between gap-3">
        <Button variant="secondary" onClick={() => setIndex((i) => i - 1)} disabled={index === 0}>
          Back
        </Button>
        <span className="text-xs text-slate-500">
          {answered} of {questions.length} answered
        </span>
        {isLast ? (
          <Button onClick={handleSubmit} disabled={submit.isPending}>
            {submit.isPending ? 'Submitting…' : 'Submit'}
          </Button>
        ) : (
          <Button onClick={() => setIndex((i) => i + 1)}>Next</Button>
        )}
      </div>
    </div>
  )
}
