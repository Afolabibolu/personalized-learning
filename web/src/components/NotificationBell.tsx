import { useEffect, useRef, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { listNotifications, markNotificationsRead, type AppNotification, type NotificationKind } from '../api/notifications'
import { getProfile } from '../api/profile'
import { timeAgo } from '../lib/time'

const KIND_DOT: Record<NotificationKind, string> = {
  streak_at_risk: 'bg-amber-500',
  inactive_3_days: 'bg-amber-500',
  weak_topic_unstudied: 'bg-red-500',
  daily_goal_reached: 'bg-emerald-500',
  score_improved: 'bg-emerald-500',
  new_recommendations: 'bg-brand-600',
}

export function useNotifications() {
  return useQuery({ queryKey: ['notifications'], queryFn: () => listNotifications(), refetchInterval: 60_000 })
}

/** Marks a notification read and follows its link. */
export function useOpenNotification() {
  const queryClient = useQueryClient()
  const navigate = useNavigate()
  const markRead = useMutation({
    mutationFn: markNotificationsRead,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['notifications'] }),
  })
  return (n: AppNotification) => {
    if (!n.read_at) markRead.mutate([n.id])
    if (n.link) navigate(n.link)
  }
}

export function NotificationItem({ n, onOpen }: { n: AppNotification; onOpen: (n: AppNotification) => void }) {
  return (
    <button
      onClick={() => onOpen(n)}
      className={`flex w-full gap-3 rounded-xl px-3 py-2.5 text-left transition hover:bg-slate-50 ${n.read_at ? '' : 'bg-brand-50/50'}`}
      data-testid="notification"
      data-unread={!n.read_at}
    >
      <span className={`mt-1.5 h-2 w-2 shrink-0 rounded-full ${n.read_at ? 'bg-slate-300' : KIND_DOT[n.kind]}`} aria-hidden />
      <span className="min-w-0 flex-1">
        <span className={`block text-sm ${n.read_at ? 'text-slate-700' : 'font-semibold text-slate-900'}`}>{n.title}</span>
        <span className="block text-sm text-slate-600">{n.body}</span>
        <span className="mt-0.5 block text-xs text-slate-400">{timeAgo(n.created_at)}</span>
      </span>
    </button>
  )
}

export function NotificationBell() {
  const notifications = useNotifications()
  const queryClient = useQueryClient()
  const open = useOpenNotification()
  const [panelOpen, setPanelOpen] = useState(false)
  const ref = useRef<HTMLDivElement>(null)
  useBrowserNotifications(notifications.data)

  const items = notifications.data ?? []
  const unread = items.filter((n) => !n.read_at)

  const markAll = useMutation({
    mutationFn: () => markNotificationsRead(unread.map((n) => n.id)),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['notifications'] }),
  })

  // Close the panel on an outside click.
  useEffect(() => {
    if (!panelOpen) return
    const close = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setPanelOpen(false)
    }
    document.addEventListener('mousedown', close)
    return () => document.removeEventListener('mousedown', close)
  }, [panelOpen])

  return (
    <div className="relative" ref={ref}>
      <button
        onClick={() => setPanelOpen((v) => !v)}
        aria-label={unread.length ? `Notifications, ${unread.length} unread` : 'Notifications'}
        aria-expanded={panelOpen}
        className="relative rounded-lg p-2 text-slate-600 hover:bg-slate-100 hover:text-slate-900"
        data-testid="notification-bell"
      >
        <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" className="h-5 w-5" aria-hidden>
          <path d="M10 3a4.5 4.5 0 0 0-4.5 4.5c0 4-1.5 5.5-1.5 5.5h12s-1.5-1.5-1.5-5.5A4.5 4.5 0 0 0 10 3ZM8.5 16a1.5 1.5 0 0 0 3 0" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        {unread.length > 0 && (
          <span className="absolute -top-0.5 -right-0.5 grid h-5 min-w-5 place-items-center rounded-full bg-red-500 px-1 text-[11px] font-bold text-white" data-testid="unread-count">
            {unread.length > 9 ? '9+' : unread.length}
          </span>
        )}
      </button>

      {panelOpen && (
        <div className="absolute right-0 z-20 mt-2 w-[min(22rem,calc(100vw-2rem))] rounded-2xl bg-white p-2 shadow-lg ring-1 ring-slate-200" data-testid="notification-panel">
          <div className="flex items-center justify-between px-3 py-2">
            <p className="text-sm font-semibold">Notifications</p>
            {unread.length > 0 && (
              <button onClick={() => markAll.mutate()} className="text-xs font-semibold text-brand-600 hover:text-brand-700">
                Mark all read
              </button>
            )}
          </div>
          {items.length === 0 ? (
            <p className="px-3 py-6 text-center text-sm text-slate-500">No notifications yet. Reminders and feedback will appear here.</p>
          ) : (
            <div className="grid gap-0.5">
              {items.slice(0, 5).map((n) => (
                <NotificationItem
                  key={n.id}
                  n={n}
                  onOpen={(item) => {
                    setPanelOpen(false)
                    open(item)
                  }}
                />
              ))}
            </div>
          )}
          <Link to="/notifications" onClick={() => setPanelOpen(false)} className="mt-1 block rounded-xl px-3 py-2 text-center text-sm font-semibold text-brand-600 hover:bg-slate-50">
            See all notifications
          </Link>
        </div>
      )}
    </div>
  )
}

const SHOWN_KEY = 'ls-browser-notified'

/**
 * Shows new unread notifications as browser notifications while the app is
 * open, if the student turned them on in Profile and the browser allows it.
 * Reminders always stay in the bell either way.
 */
function useBrowserNotifications(items: AppNotification[] | undefined) {
  const profile = useQuery({ queryKey: ['profile'], queryFn: getProfile })
  const enabled = profile.data?.browser_notifications

  useEffect(() => {
    if (!enabled || !items || typeof Notification === 'undefined' || Notification.permission !== 'granted') return
    let shown: string[] = []
    try {
      shown = JSON.parse(localStorage.getItem(SHOWN_KEY) ?? '[]')
    } catch {
      shown = []
    }
    const fresh = items.filter((n) => !n.read_at && !shown.includes(n.id))
    for (const n of fresh.slice(0, 3)) new Notification(n.title, { body: n.body, tag: n.id })
    try {
      localStorage.setItem(SHOWN_KEY, JSON.stringify([...shown, ...fresh.map((n) => n.id)].slice(-200)))
    } catch {
      // Storage blocked: at worst a notification shows again later.
    }
  }, [enabled, items])
}
