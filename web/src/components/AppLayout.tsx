import { NavLink, Outlet, useNavigate } from 'react-router-dom'
import { useQueryClient } from '@tanstack/react-query'
import { signOut } from '../api/auth'

const navClass = ({ isActive }: { isActive: boolean }) =>
  `whitespace-nowrap rounded-lg px-2.5 py-2 text-sm font-medium transition sm:px-3 ${
    isActive ? 'bg-brand-50 text-brand-700' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
  }`

export function AppLayout() {
  const navigate = useNavigate()
  const queryClient = useQueryClient()

  async function handleSignOut() {
    await signOut()
    queryClient.clear()
    navigate('/login')
  }

  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-10 border-b border-slate-200 bg-white/90 backdrop-blur">
        <div className="mx-auto flex max-w-3xl items-center justify-between gap-2 px-4 py-3">
          <NavLink to="/" className="flex items-center gap-2 font-bold text-slate-900">
            <span className="grid h-8 w-8 place-items-center rounded-lg bg-brand-600 text-sm text-white">LS</span>
            <span className="hidden sm:inline">Learning Support</span>
          </NavLink>
          <nav className="flex items-center gap-0.5 sm:gap-1">
            <NavLink to="/" end className={navClass}>
              Dashboard
            </NavLink>
            <NavLink to="/courses" className={navClass}>
              Courses
            </NavLink>
            <NavLink to="/log" className={navClass}>
              Log study
            </NavLink>
            <button
              onClick={handleSignOut}
              aria-label="Sign out"
              className="rounded-lg px-2.5 py-2 text-sm font-medium whitespace-nowrap text-slate-500 hover:bg-slate-100 hover:text-slate-900 sm:px-3"
            >
              <span className="hidden sm:inline">Sign out</span>
              <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.7" className="h-4 w-4 sm:hidden" aria-hidden>
                <path d="M8 4H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3M12 6l4 4-4 4M16 10H8" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </button>
          </nav>
        </div>
      </header>
      <main className="mx-auto max-w-3xl px-4 py-6 sm:py-8">
        <Outlet />
      </main>
    </div>
  )
}
