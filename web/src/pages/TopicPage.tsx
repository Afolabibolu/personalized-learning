import { Link, useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { getTopic } from '../api/courses'
import { ResourceList } from '../components/ResourceList'
import { ButtonLink, Card, ErrorMessage, PageHeader, SampleBadge, ScoreBadge, Spinner } from '../components/ui'

export function TopicPage() {
  const { topicId = '' } = useParams()
  const topic = useQuery({ queryKey: ['topic', topicId], queryFn: () => getTopic(topicId) })

  if (topic.isPending) return <Spinner />
  if (topic.isError) return <ErrorMessage error={topic.error} />

  const { data } = topic

  return (
    <>
      <Link to={`/courses/${data.course.id}`} className="mb-4 inline-block text-sm text-slate-500 hover:text-slate-900">
        ← {data.course.code}: {data.course.title}
      </Link>
      <PageHeader eyebrow={`${data.course.code} · Topic ${data.sequence_order}`} title={data.title}>
        {data.latest_score !== null ? (
          <span className="flex items-center gap-2">
            Latest score <ScoreBadge score={data.latest_score} />
          </span>
        ) : (
          'No quiz attempts on this topic yet.'
        )}
      </PageHeader>

      {!data.course.is_reviewed && (
        <p className="-mt-3 mb-4">
          <SampleBadge />
        </p>
      )}

      {data.summary && <p className="-mt-2 mb-6 max-w-2xl text-sm leading-relaxed text-slate-700">{data.summary}</p>}

      <div className="mb-6 flex flex-col gap-2 sm:flex-row">
        {data.quiz && <ButtonLink to={`/quiz/${data.quiz.id}`}>Take topic quiz</ButtonLink>}
        <ButtonLink to={`/log?topic=${data.id}`} variant="secondary">
          Log study session
        </ButtonLink>
      </div>

      <div className="grid gap-4 sm:grid-cols-5">
        <Card className="sm:col-span-3">
          <h2 className="mb-3 font-semibold">Resources</h2>
          <ResourceList resources={data.resources} />
        </Card>
        <Card className="sm:col-span-2">
          <h2 className="mb-3 font-semibold">What this topic covers</h2>
          <ul className="space-y-2 text-sm text-slate-600">
            {data.subtopics.map((s) => (
              <li key={s} className="flex gap-2">
                <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-brand-500" />
                {s}
              </li>
            ))}
          </ul>
        </Card>
      </div>
    </>
  )
}
