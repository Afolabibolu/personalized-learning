import { Link } from 'react-router-dom'
import { RESOURCE_ORDER } from '../api/knowledge'
import type { BookLinkType, Resource, ResourceType } from '../api/types'

export const RESOURCE_LABEL: Record<ResourceType, string> = {
  note: 'Study note',
  lecture: 'Lecture slides',
  past_questions: 'Past questions',
  video: 'Video',
  textbook: 'Recommended textbook',
}

const GROUP_LABEL: Record<ResourceType, string> = {
  note: 'Study notes',
  lecture: 'Lecture slides',
  past_questions: 'Past questions',
  video: 'Videos',
  textbook: 'Recommended textbooks',
}

const ICON_STYLE: Record<ResourceType, string> = {
  note: 'bg-brand-50 text-brand-700',
  lecture: 'bg-sky-50 text-sky-700',
  past_questions: 'bg-amber-50 text-amber-700',
  video: 'bg-rose-50 text-rose-700',
  textbook: 'bg-emerald-50 text-emerald-700',
}

export function ResourceIcon({ type, className = 'h-10 w-10' }: { type: ResourceType; className?: string }) {
  const paths: Record<ResourceType, string> = {
    note: 'M6 3h7l5 5v13H6zM13 3v5h5M9 13h6M9 17h6',
    lecture: 'M4 5h16v11H4zM8 20h8M12 16v4',
    past_questions: 'M9 9a3 3 0 1 1 4 2.8c-.8.4-1 1-1 1.7V14M12 17.5v.5M5 3h14v18H5z',
    video: 'M4 6h12v12H4zM16 10l4-2v8l-4-2',
    textbook: 'M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2zM4 19V5M8 7h7',
  }
  return (
    <span className={`grid shrink-0 place-items-center rounded-xl ${ICON_STYLE[type]} ${className}`} aria-hidden>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" className="h-5 w-5">
        <path d={paths[type]} strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    </span>
  )
}

/** Question sets that are not from past papers (exam-style or course-book review questions) are never labelled past questions. */
export function isExamStyle(resource: Pick<Resource, 'type' | 'title'>): boolean {
  return resource.type === 'past_questions' && /^(Exam-style|Review) questions/.test(resource.title)
}

/** The label for a question set that is not from past papers: "Review questions" or "Exam-style questions". */
export function practiceLabel(resource: Pick<Resource, 'title'>): string {
  return resource.title.startsWith('Review questions') ? 'Review questions' : 'Exam-style questions'
}

/** Notes, past questions and textbook reading cards open in the app; lectures and videos in a new tab. */
export function opensOutside(resource: Pick<Resource, 'type' | 'url'>): boolean {
  return Boolean(resource.url) && resource.type !== 'textbook'
}

const BOOK_LINK_LABEL: Record<BookLinkType, string> = {
  free: 'Read free online',
  buy: 'Buy or preview',
  preview: 'Buy or preview',
}

/** A textbook's own link, beside its reading card: a legal free copy, or where to buy or preview it. */
export function BookLinkButton({ url, linkType, className = '' }: { url: string; linkType: BookLinkType; className?: string }) {
  const free = linkType === 'free'
  return (
    <a
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      className={`inline-flex shrink-0 items-center gap-1 rounded-lg px-2.5 py-1.5 text-xs font-semibold whitespace-nowrap ring-1 transition ${
        free ? 'bg-emerald-50 text-emerald-800 ring-emerald-200 hover:bg-emerald-100' : 'bg-white text-slate-700 ring-slate-300 hover:bg-slate-50'
      } ${className}`}
      data-testid="book-link"
      data-link-type={linkType}
    >
      {BOOK_LINK_LABEL[linkType]}
      <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.8" className="h-3.5 w-3.5" aria-hidden>
        <path d="M8 4H4v12h12v-4M11 4h5v5M16 4l-7 7" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
      <span className="sr-only">(opens in a new tab)</span>
    </a>
  )
}

/** Where a resource opens: notes and past questions in the app, links in a new tab. */
export function resourceHint(resource: Pick<Resource, 'type' | 'url'>): string {
  if (!opensOutside(resource)) return 'Read in the app'
  if (resource.url?.includes('/drive/folders/')) return resource.type === 'lecture' ? 'Open lecture folder' : 'Open folder'
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
  if (resource.type === 'textbook') {
    // The reading card opens in the app; the book's own link is a separate button.
    return (
      // Phone: the button sits under the title, lined up with the text; wider screens: beside it.
      <div className="flex flex-col items-start sm:flex-row sm:items-center sm:gap-2">
        <Link to={`/resources/${resource.id}`} className={`${style} w-full min-w-0 flex-1`} data-testid="resource-link">
          {body}
        </Link>
        {resource.url && resource.link_type && (
          <BookLinkButton url={resource.url} linkType={resource.link_type} className={`mb-1.5 sm:mr-2 sm:mb-0 sm:ml-0 ${compact ? 'ml-13' : 'ml-15'}`} />
        )}
      </div>
    )
  }
  return opensOutside(resource) ? (
    <a href={resource.url ?? undefined} target="_blank" rel="noreferrer" className={style} data-testid="resource-link">
      {body}
    </a>
  ) : (
    <Link to={`/resources/${resource.id}`} className={style} data-testid="resource-link">
      {body}
    </Link>
  )
}

/** Resources grouped by type, in the order: notes, lecture slides, past questions, videos, textbooks. */
export function ResourceList({ resources, compact = false }: { resources: Resource[]; compact?: boolean }) {
  if (resources.length === 0) {
    return <p className="text-sm text-slate-500">No resources for this topic yet.</p>
  }
  return (
    <div className="grid gap-3">
      {RESOURCE_ORDER.filter((type) => resources.some((r) => r.type === type)).map((type) => (
        <div key={type}>
          <p className="mb-1 text-xs font-semibold tracking-wide text-slate-500 uppercase">
            {type === 'past_questions' && resources.filter((r) => r.type === type).every(isExamStyle)
              ? practiceLabel(resources.find((r) => r.type === type)!)
              : GROUP_LABEL[type]}
          </p>
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
