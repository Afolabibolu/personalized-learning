import { currentUserId } from './auth'
import { supabase } from './supabase'

export type CourseRequestStatus = 'pending' | 'in_progress' | 'added' | 'declined'

export type CourseRequest = {
  id: string
  code: string
  title: string
  level: number | null
  semester: number | null
  lecturer: string | null
  details: string | null
  status: CourseRequestStatus
  admin_note: string | null
  course_id: string | null
  created_at: string
  files?: RequestFile[]
}

export type CourseRequestInput = Pick<CourseRequest, 'code' | 'title' | 'level' | 'semester' | 'lecturer' | 'details'>

export type RequestFile = { id: string; request_id: string; path: string; name: string; size_bytes: number; content_type: string }

/** Private bucket: the requester and course managers can read a file, nobody else. */
export const REQUEST_FILES_BUCKET = 'course-request-files'
export const MAX_FILES = 5
export const MAX_FILE_BYTES = 20 * 1024 * 1024
export const ALLOWED_TYPES: Record<string, string> = {
  'application/pdf': 'PDF',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'DOCX',
  'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'PPTX',
  'image/png': 'image',
  'image/jpeg': 'image',
  'image/webp': 'image',
  'image/heic': 'image',
}

/** Why a file cannot be attached, or null if it can. */
export function fileProblem(file: File): string | null {
  if (!ALLOWED_TYPES[file.type]) return `${file.name}: only PDF, DOCX, PPTX or image files`
  if (file.size > MAX_FILE_BYTES) return `${file.name}: larger than 20 MB`
  if (file.size === 0) return `${file.name}: the file is empty`
  return null
}

function safeName(name: string): string {
  return name.normalize('NFKD').replace(/[^\w.\- ]+/g, '').replace(/\s+/g, '_').slice(-120) || 'file'
}

/** A course the student cannot find, with optional files (outline, notes, past questions); it is added later
 *  through the ingestion pipeline. The id is chosen here so the files can be uploaded under it. */
export async function requestCourse(input: CourseRequestInput, files: File[] = []): Promise<void> {
  const studentId = await currentUserId()
  const id = crypto.randomUUID()
  // No .select() after the insert: students may insert only the request columns.
  const { error } = await supabase.from('course_requests').insert({ id, student_id: studentId, ...input })
  if (error) throw error
  for (const [i, file] of files.slice(0, MAX_FILES).entries()) {
    const path = `${studentId}/${id}/${i + 1}-${safeName(file.name)}`
    const upload = await supabase.storage.from(REQUEST_FILES_BUCKET).upload(path, file, { contentType: file.type })
    if (upload.error) throw new Error(`${file.name} could not be uploaded: ${upload.error.message}`)
    const row = await supabase.from('course_request_files').insert({
      request_id: id, student_id: studentId, path, name: file.name, size_bytes: file.size, content_type: file.type,
    })
    if (row.error) throw row.error
  }
}

/** A short-lived link to download a request file (RLS on storage decides who may). */
export async function requestFileUrl(path: string): Promise<string> {
  const { data, error } = await supabase.storage.from(REQUEST_FILES_BUCKET).createSignedUrl(path, 600, { download: true })
  if (error) throw error
  return data.signedUrl
}

/** The signed-in student's own requests (a course manager can read everyone's, so filter). */
export async function listCourseRequests(): Promise<CourseRequest[]> {
  const studentId = await currentUserId()
  const { data, error } = await supabase
    .from('course_requests')
    .select('id, code, title, level, semester, lecturer, details, status, admin_note, course_id, created_at, files:course_request_files(id, request_id, path, name, size_bytes, content_type)')
    .eq('student_id', studentId)
    .order('created_at', { ascending: false })
  if (error) throw error
  return data
}
