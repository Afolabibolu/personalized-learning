import { useEffect, useState } from 'react'
import { NavLink, Outlet, useLocation, useNavigate } from 'react-router-dom'
import { useQueryClient } from '@tanstack/react-query'
import { signOut } from '../api/auth'

const LINKS = [
  { to: '/', label: 'Dashboard', end: true },
  { to: '/courses', label: 'Courses', end: false },
  { to: '/knowledge', label: 'Knowledge Base', end: false },
  { to: '/log', label: 'Log study', end: false },
]

const navClass = ({ isActive }: { isActive: boolean }) =>
  `whitespace-nowrap rounded-lg px-3 py-2 text-sm font-medium transition ${
    isActive ? 'bg-brand-50 text-brand-700' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
  }`

export function AppLayout() {
  const navigate = useNavigate()
  const location = useLocation()
  const queryClient = useQueryClient()
  const [menuOpen, setMenuOpen] = useState(false)

  // Close the phone menu whenever the page changes.
  useEffect(() => setMenuOpen(false), [location.pathname])

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
            <span>Learning Support</span>
          </NavLink>

          <nav className="hidden items-center gap-0.5 md:flex" aria-label="Main">
            {LINKS.map((l) => (
              <NavLink key={l.to} to={l.to} end={l.end} className={navClass}>
                {l.label}
              </NavLink>
            ))}
            <button onClick={handleSignOut} className="rounded-lg px-3 py-2 text-sm font-medium whitespace-nowrap text-slate-500 hover:bg-slate-100 hover:text-slate-900">
              Sign out
            </button>
          </nav>

          <button
            className="rounded-lg p-2 text-slate-600 hover:bg-slate-100 md:hidden"
            aria-label={menuOpen ? 'Close menu' : 'Open menu'}
            aria-expanded={menuOpen}
            onClick={() => setMenuOpen((open) => !open)}
          >
            <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.8" className="h-5 w-5" aria-hidden>
              {menuOpen ? <path d="M5 5l10 10M15 5L5 15" strokeLinecap="round" /> : <path d="M3 6h14M3 10h14M3 14h14" strokeLinecap="round" />}
            </svg>
          </button>
        </div>

        {menuOpen && (
          <nav className="border-t border-slate-100 px-4 pt-2 pb-3 md:hidden" aria-label="Main">
            <div className="mx-auto grid max-w-3xl gap-1">
              {LINKS.map((l) => (
                <NavLink key={l.to} to={l.to} end={l.end} className={navClass}>
                  {l.label}
                </NavLink>
              ))}
              <button onClick={handleSignOut} className="rounded-lg px-3 py-2 text-left text-sm font-medium text-slate-500 hover:bg-slate-100">
                Sign out
              </button>
            </div>
          </nav>
        )}
      </header>
      <main className="mx-auto max-w-3xl px-4 py-6 sm:py-8">
        <Outlet />
      </main>
    </div>
  )
}
