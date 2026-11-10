import type { CourseRequest, RequestFile } from './courseRequests'
import { supabase } from './supabase'
import type { BookLinkType, QuestionFormat, ResourceType } from './types'

// Course manager actions. Each is a database function that checks the caller's role
// (students get "course managers only") and records the change in content_audit.

export type ManagedRequest = Omit<CourseRequest, 'files'> & {
  updated_at: string
  student: { id: string; name: string | null; email: string | null }
  files: Omit<RequestFile, 'request_id'>[]
}

export type ManagedQuestion = {
  id: string
  format: QuestionFormat
  stem: string
  options: { key: string; text: string }[]
  correct_answer: string[]
  explanation: string
  source: string | null
  status: 'approved' | 'hidden'
}

export type AuditEntry = {
  id: string
  action: string
  summary: string
  changes: Record<string, { from: unknown; to: unknown }>
  created_at: string
  actor: string | null
}

export type ManagedCourse = {
  id: string
  code: string
  title: string
  level: number | null
  semester: number | null
  is_reviewed: boolean
  topics: {
    id: string
    title: string
    summary: string | null
    sequence_order: number
    resources: { id: string; title: string; type: ResourceType; url: string | null; link_type: BookLinkType | null; source: string | null }[]
  }[]
}

async function call<T>(fn: string, args?: Record<string, unknown>): Promise<T> {
  const { data, error } = await supabase.rpc(fn, args)
  if (error) throw error
  return data as T
}

export async function isCourseManager(): Promise<boolean> {
  return call<boolean>('is_course_manager')
}

export const listManagedRequests = () => call<ManagedRequest[]>('manage_requests')

export function setRequestStatus(requestId: string, status: 'in_progress' | 'added' | 'declined', note?: string, courseCode?: string) {
  return call<void>('manage_set_request_status', {
    p_request: requestId, p_status: status, p_note: note ?? null, p_course_code: courseCode || null,
  })
}

/** Every course, for the Courses tab (courses are readable by everyone). */
export async function listAllCourses(): Promise<Omit<ManagedCourse, 'topics'>[]> {
  const { data, error } = await supabase
    .from('courses')
    .select('id, code, title, level, semester, is_reviewed')
    .order('code')
  if (error) throw error
  return data
}

export async function getManagedCourse(code: string): Promise<ManagedCourse> {
  const { data, error } = await supabase
    .from('courses')
    .select('id, code, title, level, semester, is_reviewed, topics(id, title, summary, sequence_order, resources(id, title, type, url, link_type, source))')
    .eq('code', code)
    .single()
  if (error) throw error
  const course = data as unknown as ManagedCourse
  course.topics.sort((a, b) => a.sequence_order - b.sequence_order)
  return course
}

export const updateTopic = (topicId: string, title: string, summary: string) =>
  call<void>('manage_update_topic', { p_topic: topicId, p_title: title, p_summary: summary })

export const listTopicQuestions = (topicId: string) => call<ManagedQuestion[]>('manage_questions', { p_topic: topicId })

export const updateQuestion = (q: Pick<ManagedQuestion, 'id' | 'stem' | 'options' | 'correct_answer' | 'explanation'>) =>
  call<void>('manage_update_question', {
    p_question: q.id, p_stem: q.stem, p_options: q.options, p_correct: q.correct_answer, p_explanation: q.explanation,
  })

export const setQuestionHidden = (questionId: string, hidden: boolean) =>
  call<void>('manage_set_question_hidden', { p_question: questionId, p_hidden: hidden })

export const saveResource = (r: { id: string | null; topicId: string; title: string; type: ResourceType; url: string; linkType?: BookLinkType | null }) =>
  call<string>('manage_save_resource', {
    p_resource: r.id, p_topic: r.topicId, p_title: r.title, p_type: r.type, p_url: r.url, p_link_type: r.linkType ?? null,
  })

export const setCourseReviewed = (courseId: string, reviewed: boolean) =>
  call<void>('manage_set_course_reviewed', { p_course: courseId, p_reviewed: reviewed })

export const listAudit = (limit = 100) => call<AuditEntry[]>('manage_audit', { p_limit: limit })
