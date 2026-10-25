import { currentUserId } from './auth'
import { supabase } from './supabase'

export type CourseRequestStatus = 'pending' | 'added' | 'declined'

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
}

export type CourseRequestInput = Pick<CourseRequest, 'code' | 'title' | 'level' | 'semester' | 'lecturer' | 'details'>

/** A course the student cannot find; it is added later through the ingestion pipeline. */
export async function requestCourse(input: CourseRequestInput): Promise<void> {
  const studentId = await currentUserId()
  // No .select() after the insert: students may insert only the request columns.
  const { error } = await supabase.from('course_requests').insert({ student_id: studentId, ...input })
  if (error) throw error
}

export async function listCourseRequests(): Promise<CourseRequest[]> {
  const { data, error } = await supabase
    .from('course_requests')
    .select('id, code, title, level, semester, lecturer, details, status, admin_note, course_id, created_at')
    .order('created_at', { ascending: false })
  if (error) throw error
  return data
}
