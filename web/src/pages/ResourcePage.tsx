import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { Link, useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { getResource } from '../api/knowledge'
import { RESOURCE_LABEL, ResourceIcon } from '../components/ResourceList'
import { ButtonLink, Card, ErrorMessage, Spinner } from '../components/ui'

/** In-app viewer for study notes and past questions (Markdown). */
export function ResourcePage() {
  const { resourceId = '' } = useParams()
  const resource = useQuery({ queryKey: ['resource', resourceId], queryFn: () => getResource(resourceId) })

  if (resource.isPending) return <Spinner />
  if (resource.isError) return <ErrorMessage error={resource.error} />

  const { data } = resource
  const { topic } = data

  return (
    <article className="mx-auto max-w-2xl">
      <Link to={`/topics/${topic.id}`} className="mb-4 inline-block text-sm text-slate-500 hover:text-slate-900">
        ← {topic.course.code}: {topic.title}
      </Link>
      <div className="mb-4 flex items-center gap-3">
        <ResourceIcon type={data.type} />
        <div>
          <p className="text-xs font-semibold tracking-wide text-brand-600 uppercase">{RESOURCE_LABEL[data.type]}</p>
          <p className="text-sm text-slate-500">{topic.course.code} · {topic.course.title}</p>
        </div>
      </div>

      {data.body ? (
        <Card className="px-5 py-6 sm:px-8">
          <div className="prose prose-slate prose-sm sm:prose-base max-w-none prose-headings:tracking-tight prose-h1:text-2xl prose-h2:text-lg prose-table:text-xs prose-th:px-2 prose-td:px-2 [&_table]:block [&_table]:overflow-x-auto">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{data.body}</ReactMarkdown>
          </div>
        </Card>
      ) : data.url ? (
        <Card>
          <h1 className="text-lg font-semibold">{data.title}</h1>
          <p className="mt-2 text-sm text-slate-600">This resource opens outside the app.</p>
          <a href={data.url} target="_blank" rel="noreferrer" className="mt-4 inline-block font-semibold text-brand-600 hover:text-brand-700">
            Open it in a new tab →
          </a>
        </Card>
      ) : null}

      {data.source && data.type === 'past_questions' && (
        <p className="mt-3 text-xs text-slate-500">From: {data.source}</p>
      )}

      <div className="mt-6 flex flex-col gap-2 sm:flex-row">
        <ButtonLink to={`/topics/${topic.id}`} variant="secondary">
          Back to topic
        </ButtonLink>
        <ButtonLink to={`/log?topic=${topic.id}`}>Log this study session</ButtonLink>
      </div>
    </article>
  )
}
