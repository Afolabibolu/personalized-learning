import type { Course } from '../api/types'

/** Every level the app groups courses by, in the order the browse cards and tabs show them. */
export const LEVELS = [100, 200, 300, 400, 500] as const

export function isLevel(value: number): boolean {
  return (LEVELS as readonly number[]).includes(value)
}

export function semesterName(semester: number | null): string {
  return semester === 1 ? 'First semester' : semester === 2 ? 'Second semester' : 'Semester not set'
}

/** Courses split by semester (first, second, then any without one), dropping empty groups. */
export function bySemester<T extends Pick<Course, 'semester' | 'code'>>(courses: T[]): [number | null, T[]][] {
  return ([1, 2, null] as const)
    .map((s): [number | null, T[]] => [
      s,
      courses.filter((c) => (c.semester ?? null) === s).sort((a, b) => a.code.localeCompare(b.code)),
    ])
    .filter(([, list]) => list.length > 0)
}
