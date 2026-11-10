import type { ReactNode } from 'react'
import { useQuery } from '@tanstack/react-query'
import { getProfile } from '../api/profile'
import { ButtonLink, Card, ErrorMessage, PageHeader, Spinner } from './ui'

/**
 * The /manage pages for course managers. This only decides what to show: the database
 * refuses every manager action from a student whatever the browser does.
 */
export function RequireManager({ children }: { children: ReactNode }) {
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  if (profile.isPending) return <Spinner />
  if (profile.isError) return <ErrorMessage error={profile.error} />
  if (profile.data.role !== 'course_manager') {
    return (
      <div className="mx-auto max-w-lg" data-testid="manage-forbidden">
        <PageHeader eyebrow="Course management" title="Course managers only">
          This area is for the people who add and check courses. If a course is missing, you can request it.
        </PageHeader>
        <Card>
          <ButtonLink to="/courses/request">Request a course</ButtonLink>
        </Card>
      </div>
    )
  }
  return children
}
