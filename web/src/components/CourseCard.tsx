import { useMutation, useQueryClient } from '@tanstack/react-query'
import { setEnrolled, type CourseSummary } from '../api/courses'
import { Button, ButtonLink, Card, SampleBadge } from './ui'

/** Adds a course to, or removes it from, the student's courses, and refreshes everything that depends on them. */
export function useEnrolmentToggle() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (c: CourseSummary) => setEnrolled(c.id, !c.enrolled),
    onSuccess: () => {
      for (const key of ['courses', 'dashboard', 'topicsByCourse', 'course']) queryClient.invalidateQueries({ queryKey: [key] })
    },
  })
}

export function CourseCard({ course, onToggle, busy }: { course: CourseSummary; onToggle: () => void; busy: boolean }) {
  return (
    <Card className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between" >
      <div data-testid="course-card" data-code={course.code}>
        <div className="flex flex-wrap items-center gap-2">
          <p className="text-xs font-semibold tracking-wide text-brand-600 uppercase">{course.code}</p>
          {!course.is_reviewed && <SampleBadge />}
        </div>
        <h2 className="text-lg font-semibold">{course.title}</h2>
        <p className="mt-1 text-sm text-slate-500">
          {course.topic_count} topics
          {course.diagnostic_taken && <span className="text-emerald-600"> · Diagnostic done</span>}
        </p>
      </div>
      <div className="flex shrink-0 flex-wrap gap-2">
        {course.enrolled && !course.diagnostic_taken && course.diagnostic_quiz_id && (
          <ButtonLink to={`/quiz/${course.diagnostic_quiz_id}`}>Take diagnostic quiz</ButtonLink>
        )}
        <ButtonLink to={`/courses/${course.id}`} variant={course.enrolled && course.diagnostic_taken ? 'primary' : 'secondary'}>
          View course
        </ButtonLink>
        <Button variant={course.enrolled ? 'ghost' : 'primary'} onClick={onToggle} disabled={busy}>
          {course.enrolled ? 'Remove' : 'Add to my courses'}
        </Button>
      </div>
    </Card>
  )
}
