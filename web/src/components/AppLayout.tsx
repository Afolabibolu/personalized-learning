import { useEffect, useRef, useState } from 'react'
import { Link, NavLink, Outlet, useLocation, useNavigate } from 'react-router-dom'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { signOut } from '../api/auth'
import { getProfile } from '../api/profile'
import { NotificationBell } from './NotificationBell'

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

function initials(name: string | null | undefined): string {
  const parts = (name ?? '').trim().split(/\s+/).filter(Boolean)
  return (parts[0]?.[0] ?? '?').toUpperCase() + (parts[1]?.[0] ?? '').toUpperCase()
}

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
        <div className="mx-auto flex max-w-4xl items-center justify-between gap-2 px-4 py-3">
          <NavLink to="/" className="flex items-center gap-2 font-bold text-slate-900">
            <span className="grid h-8 w-8 place-items-center rounded-lg bg-brand-600 text-sm text-white">LS</span>
            <span className="hidden sm:inline">Learning Support</span>
          </NavLink>

          <nav className="hidden items-center gap-0.5 md:flex" aria-label="Main">
            {LINKS.map((l) => (
              <NavLink key={l.to} to={l.to} end={l.end} className={navClass}>
                {l.label}
              </NavLink>
            ))}
          </nav>

          <div className="flex items-center gap-1">
            <NotificationBell />
            <div className="hidden md:block">
              <ProfileMenu onSignOut={handleSignOut} />
            </div>
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
        </div>

        {menuOpen && (
          <nav className="border-t border-slate-100 px-4 pt-2 pb-3 md:hidden" aria-label="Main">
            <div className="mx-auto grid max-w-4xl gap-1">
              {LINKS.map((l) => (
                <NavLink key={l.to} to={l.to} end={l.end} className={navClass}>
                  {l.label}
                </NavLink>
              ))}
              <NavLink to="/profile" className={navClass}>
                Profile
              </NavLink>
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

function ProfileMenu({ onSignOut }: { onSignOut: () => void }) {
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const [open, setOpen] = useState(false)
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!open) return
    const close = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false)
    }
    document.addEventListener('mousedown', close)
    return () => document.removeEventListener('mousedown', close)
  }, [open])

  const item = 'block w-full rounded-lg px-3 py-2 text-left text-sm text-slate-700 hover:bg-slate-50'
  return (
    <div className="relative" ref={ref}>
      <button
        onClick={() => setOpen((v) => !v)}
        aria-label="Profile menu"
        aria-expanded={open}
        className="grid h-9 w-9 place-items-center rounded-full bg-brand-50 text-xs font-bold text-brand-700 ring-1 ring-brand-100 hover:ring-brand-500"
      >
        {initials(profile.data?.full_name)}
      </button>
      {open && (
        <div className="absolute right-0 z-20 mt-2 w-52 rounded-2xl bg-white p-1.5 shadow-lg ring-1 ring-slate-200">
          <p className="truncate px-3 pt-1.5 pb-2 text-xs text-slate-500">{profile.data?.full_name}</p>
          <Link to="/profile" className={item} onClick={() => setOpen(false)}>
            Profile and reminders
          </Link>
          <Link to="/notifications" className={item} onClick={() => setOpen(false)}>
            Notifications
          </Link>
          <button onClick={onSignOut} className={`${item} text-slate-500`}>
            Sign out
          </button>
        </div>
      )}
    </div>
  )
}
