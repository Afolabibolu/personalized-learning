import type { ReactNode } from 'react'
import { Navigate, useLocation } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { useSession } from '../api/auth'
import { getProfile, isOnboarded } from '../api/profile'
import { ErrorMessage, Spinner } from './ui'

/**
 * Lets signed-in students through. Students who have not finished onboarding
 * are sent to /onboarding first (unless they are already there).
 */
export function RequireAuth({ children }: { children: ReactNode }) {
  const session = useSession()
  const location = useLocation()
  const profile = useQuery({
    queryKey: ['profile', session?.user.id],
    queryFn: getProfile,
    enabled: Boolean(session),
  })

  if (session === undefined) return <Spinner />
  if (session === null) return <Navigate to="/login" replace />
  if (profile.isPending) return <Spinner />
  if (profile.isError) return <div className="p-4"><ErrorMessage error={profile.error} /></div>

  const onOnboarding = location.pathname === '/onboarding'
  if (!isOnboarded(profile.data) && !onOnboarding) return <Navigate to="/onboarding" replace />
  return children
}
