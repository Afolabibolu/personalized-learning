import { Link, useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { getTopic } from '../api/courses'
import type { Resource } from '../api/types'
import { ButtonLink, Card, ErrorMessage, PageHeader, ScoreBadge, Spinner } from '../components/ui'

const TYPE_LABEL: Record<Resource['type'], string> = { pdf: 'PDF', video: 'Video', link: 'Link' }

function ResourceRow({ resource }: { resource: Resource }) {
  // Placeholder URLs ("todo:<file>") are kept until real Drive links are added.
  const available = /^https?:\/\//.test(resource.url)
  const body = (
    <>
      <span className="grid h-10 w-10 shrink-0 place-items-center rounded-xl bg-brand-50 text-xs font-bold text-brand-700">
        {TYPE_LABEL[resource.type]}
      </span>
      <span className="min-w-0 flex-1">
        <span className="block truncate text-sm font-medium">{resource.title}</span>
        <span className="block text-xs text-slate-500">
          {resource.is_introductory ? 'Getting started · ' : ''}
          {!available ? 'Link coming soon' : resource.url.includes('/drive/folders/') ? 'Opens its Google Drive folder' : 'Opens in a new tab'}
        </span>
      </span>
    </>
  )
  return available ? (
    <a href={resource.url} target="_blank" rel="noreferrer" className="flex items-center gap-3 rounded-xl p-2 transition hover:bg-slate-50">
      {body}
    </a>
  ) : (
    <div className="flex items-center gap-3 rounded-xl p-2 opacity-70">{body}</div>
  )
}

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

      <div className="mb-6 flex flex-col gap-2 sm:flex-row">
        {data.quiz && <ButtonLink to={`/quiz/${data.quiz.id}`}>Take topic quiz</ButtonLink>}
        <ButtonLink to={`/log?topic=${data.id}`} variant="secondary">
          Log study session
        </ButtonLink>
      </div>

      <div className="grid gap-4 sm:grid-cols-5">
        <Card className="sm:col-span-3">
          <h2 className="mb-3 font-semibold">Resources</h2>
          <div className="-mx-2 grid gap-1">
            {data.resources.map((r) => (
              <ResourceRow key={r.id} resource={r} />
            ))}
          </div>
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
