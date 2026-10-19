import { Link } from 'react-router-dom'
import { RESOURCE_ORDER } from '../api/knowledge'
import type { Resource, ResourceType } from '../api/types'

export const RESOURCE_LABEL: Record<ResourceType, string> = {
  note: 'Study note',
  lecture: 'Lecture slides',
  past_questions: 'Past questions',
  video: 'Video',
}

const GROUP_LABEL: Record<ResourceType, string> = {
  note: 'Study notes',
  lecture: 'Lecture slides',
  past_questions: 'Past questions',
  video: 'Videos',
}

const ICON_STYLE: Record<ResourceType, string> = {
  note: 'bg-brand-50 text-brand-700',
  lecture: 'bg-sky-50 text-sky-700',
  past_questions: 'bg-amber-50 text-amber-700',
  video: 'bg-rose-50 text-rose-700',
}

export function ResourceIcon({ type, className = 'h-10 w-10' }: { type: ResourceType; className?: string }) {
  const paths: Record<ResourceType, string> = {
    note: 'M6 3h7l5 5v13H6zM13 3v5h5M9 13h6M9 17h6',
    lecture: 'M4 5h16v11H4zM8 20h8M12 16v4',
    past_questions: 'M9 9a3 3 0 1 1 4 2.8c-.8.4-1 1-1 1.7V14M12 17.5v.5M5 3h14v18H5z',
    video: 'M4 6h12v12H4zM16 10l4-2v8l-4-2',
  }
  return (
    <span className={`grid shrink-0 place-items-center rounded-xl ${ICON_STYLE[type]} ${className}`} aria-hidden>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" className="h-5 w-5">
        <path d={paths[type]} strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    </span>
  )
}

/** Where a resource opens: notes and past questions in the app, links in a new tab. */
export function resourceHint(resource: Pick<Resource, 'type' | 'url'>): string {
  if (!resource.url) return 'Read in the app'
  if (resource.url.includes('/drive/folders/')) return 'Open lecture folder'
  return 'Opens in a new tab'
}

export function ResourceLink({ resource, compact = false }: { resource: Resource; compact?: boolean }) {
  const body = (
    <>
      <ResourceIcon type={resource.type} className={compact ? 'h-8 w-8' : 'h-10 w-10'} />
      <span className="min-w-0 flex-1">
        <span className="block text-sm leading-snug font-medium">{resource.title}</span>
        <span className="block text-xs text-slate-500">
          {resource.is_introductory ? 'Getting started · ' : ''}
          {resourceHint(resource)}
        </span>
      </span>
    </>
  )
  const style = 'flex items-center gap-3 rounded-xl p-2 transition hover:bg-slate-50'
  return resource.url ? (
    <a href={resource.url} target="_blank" rel="noreferrer" className={style} data-testid="resource-link">
      {body}
    </a>
  ) : (
    <Link to={`/resources/${resource.id}`} className={style} data-testid="resource-link">
      {body}
    </Link>
  )
}

/** Resources grouped by type, in the order: notes, lecture slides, past questions, videos. */
export function ResourceList({ resources, compact = false }: { resources: Resource[]; compact?: boolean }) {
  if (resources.length === 0) {
    return <p className="text-sm text-slate-500">No resources for this topic yet.</p>
  }
  return (
    <div className="grid gap-3">
      {RESOURCE_ORDER.filter((type) => resources.some((r) => r.type === type)).map((type) => (
        <div key={type}>
          <p className="mb-1 text-xs font-semibold tracking-wide text-slate-500 uppercase">{GROUP_LABEL[type]}</p>
          <div className="-mx-2 grid gap-0.5">
            {resources
              .filter((r) => r.type === type)
              .map((r) => (
                <ResourceLink key={r.id} resource={r} compact={compact} />
              ))}
          </div>
        </div>
      ))}
    </div>
  )
}
