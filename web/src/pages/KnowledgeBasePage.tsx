import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { listEnrolledCourseIds } from '../api/courses'
import { getKnowledgeBase, getKnowledgeStats, type KnowledgeTopic } from '../api/knowledge'
import { ResourceList } from '../components/ResourceList'
import { ButtonLink, Card, ErrorMessage, PageHeader, SampleBadge, Spinner, inputClass } from '../components/ui'

function matches(text: string | null | undefined, query: string): boolean {
  return Boolean(text && text.toLowerCase().includes(query))
}

/** Topics that match the search; a topic matched only by its resources shows just those resources. */
function filterTopic(topic: KnowledgeTopic, query: string): KnowledgeTopic | null {
  if (!query) return topic
  const topicMatch =
    matches(topic.title, query) || matches(topic.summary, query) || topic.subtopics.some((s) => matches(s, query))
  if (topicMatch) return topic
  const resources = topic.resources.filter((r) => matches(r.title, query))
  return resources.length ? { ...topic, resources } : null
}

export function KnowledgeBasePage() {
  const courses = useQuery({ queryKey: ['knowledgeBase'], queryFn: getKnowledgeBase })
  const stats = useQuery({ queryKey: ['knowledgeStats'], queryFn: getKnowledgeStats })
  const enrolled = useQuery({ queryKey: ['course', 'enrolled'], queryFn: listEnrolledCourseIds })
  const [search, setSearch] = useState('')
  const [onlyMine, setOnlyMine] = useState(false)
  // Sections the student opened or closed; the rest follow the default (own courses open).
  const [toggled, setToggled] = useState<Record<string, boolean>>({})
  const query = search.trim().toLowerCase()
  const mine = useMemo(() => enrolled.data ?? new Set<string>(), [enrolled.data])
  // A search opens every course with a match.
  const isOpen = (id: string) => Boolean(query) || (toggled[id] ?? mine.has(id))
  const setAll = (open: boolean) => setToggled(Object.fromEntries(filtered.map((c) => [c.id, open])))

  // The student's own courses first, then the rest by code.
  const filtered = useMemo(() => {
    return (courses.data ?? [])
      .filter((c) => !onlyMine || mine.has(c.id))
      .map((c) => ({ ...c, topics: c.topics.map((t) => filterTopic(t, query)).filter((t): t is KnowledgeTopic => t !== null) }))
      .filter((c) => c.topics.length > 0)
      .sort((a, b) => Number(mine.has(b.id)) - Number(mine.has(a.id)) || a.code.localeCompare(b.code))
  }, [courses.data, mine, query, onlyMine])

  return (
    <>
      <PageHeader eyebrow="Knowledge Base" title="Everything to study, by topic">
        Study notes, lecture slides and past questions for each topic, in teaching order.
      </PageHeader>

      {stats.data && (
        <p className="mb-4 flex flex-wrap gap-x-4 gap-y-1 text-sm text-slate-600" data-testid="kb-stats">
          <Stat value={stats.data.courses} label="courses" />
          <Stat value={stats.data.topics} label="topics" />
          <Stat value={stats.data.resources} label="resources" />
          <Stat value={stats.data.practice_questions} label="practice questions" />
        </p>
      )}

      <div className="relative mb-6">
        <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.8" className="pointer-events-none absolute top-1/2 left-3.5 h-4 w-4 -translate-y-1/2 text-slate-400" aria-hidden>
          <circle cx="9" cy="9" r="5.5" />
          <path d="M13.5 13.5 17 17" strokeLinecap="round" />
        </svg>
        <input
          type="search"
          aria-label="Search topics and resources"
          placeholder="Search topics and resources, e.g. fuzzy, heuristics, personas"
          className={`${inputClass} pl-10`}
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>

      <div className="-mt-3 mb-6 flex flex-wrap items-center justify-between gap-2">
      <div className="flex gap-2" role="group" aria-label="Which courses to show">
        {[
          { mine: false, label: 'All courses' },
          { mine: true, label: 'My courses' },
        ].map((o) => (
          <button
            key={o.label}
            type="button"
            aria-pressed={onlyMine === o.mine}
            onClick={() => setOnlyMine(o.mine)}
            className={`rounded-full px-3 py-1 text-xs font-semibold ring-1 transition ${
              onlyMine === o.mine ? 'bg-brand-600 text-white ring-brand-600' : 'bg-white text-slate-600 ring-slate-300 hover:ring-brand-500'
            }`}
          >
            {o.label}
          </button>
        ))}
      </div>
        {!query && filtered.length > 1 && (
          <div className="flex gap-3 text-xs font-semibold">
            <button type="button" onClick={() => setAll(true)} className="text-brand-600 hover:text-brand-700">
              Expand all
            </button>
            <button type="button" onClick={() => setAll(false)} className="text-slate-500 hover:text-slate-800">
              Collapse all
            </button>
          </div>
        )}
      </div>

      {courses.isPending && <Spinner />}
      {courses.isError && <ErrorMessage error={courses.error} />}

      {courses.data && filtered.length === 0 && (
        <Card className="text-center">
          <p className="text-sm text-slate-600">No topics or resources match “{search.trim()}”.</p>
          <button onClick={() => setSearch('')} className="mt-2 text-sm font-semibold text-brand-600 hover:text-brand-700">
            Clear the search
          </button>
        </Card>
      )}

      <div className="grid gap-4">
        {filtered.map((course) => {
          const open = isOpen(course.id)
          return (
          <section key={course.id} aria-labelledby={`course-${course.id}`} className={open ? 'pb-4' : ''}>
            <div className="mb-3 flex flex-wrap items-center gap-2">
              <h2 id={`course-${course.id}`} className="text-lg font-semibold">
                <button
                  type="button"
                  aria-expanded={open}
                  aria-controls={`topics-${course.id}`}
                  disabled={Boolean(query)}
                  onClick={() => setToggled((t) => ({ ...t, [course.id]: !open }))}
                  className="flex items-center gap-2 text-left hover:text-brand-700 disabled:cursor-default disabled:hover:text-inherit"
                >
                  <svg viewBox="0 0 20 20" fill="currentColor" aria-hidden className={`h-4 w-4 shrink-0 text-slate-400 transition ${open ? 'rotate-90' : ''}`}>
                    <path d="M7.2 4.2a1 1 0 0 1 1.4 0l5.1 5.1a1 1 0 0 1 0 1.4l-5.1 5.1a1 1 0 1 1-1.4-1.4L11.6 10 7.2 5.6a1 1 0 0 1 0-1.4Z" />
                  </svg>
                  <span>
                    <span className="text-brand-600">{course.code}</span> · {course.title}
                  </span>
                </button>
              </h2>
              {!open && <span className="text-xs text-slate-500">{course.topics.length} topics</span>}
              {!course.is_reviewed && <SampleBadge />}
            </div>
            {open && (
            <ol className="grid gap-3" id={`topics-${course.id}`}>
              {course.topics.map((topic) => (
                <li key={topic.id}>
                  <Card className="p-4 sm:p-5" >
                    <div className="flex items-start gap-3">
                      <span className="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-slate-100 text-xs font-semibold text-slate-600">
                        {topic.sequence_order}
                      </span>
                      <div className="min-w-0 flex-1">
                        <Link to={`/topics/${topic.id}`} className="font-semibold hover:text-brand-700" data-testid="kb-topic">
                          {topic.title}
                        </Link>
                        {topic.summary && <p className="mt-1 text-sm text-slate-600">{topic.summary}</p>}
                        {topic.subtopics.length > 0 && (
                          <ul className="mt-2 flex flex-wrap gap-1.5">
                            {topic.subtopics.map((s) => (
                              <li key={s} className="rounded-lg bg-slate-100 px-2 py-0.5 text-xs text-slate-600">
                                {s}
                              </li>
                            ))}
                          </ul>
                        )}
                        <div className="mt-4">
                          <ResourceList resources={topic.resources} compact />
                        </div>
                        <div className="mt-3 flex flex-wrap gap-2">
                          {topic.topic_quiz_id && (
                            <ButtonLink to={`/quiz/${topic.topic_quiz_id}`} variant="secondary" className="px-3 py-1.5">
                              Practice: topic quiz
                            </ButtonLink>
                          )}
                        </div>
                      </div>
                    </div>
                  </Card>
                </li>
              ))}
            </ol>
            )}
          </section>
          )
        })}
      </div>
    </>
  )
}

function Stat({ value, label }: { value: number; label: string }) {
  return (
    <span>
      <span className="font-semibold text-slate-900">{value}</span> {label}
    </span>
  )
}
