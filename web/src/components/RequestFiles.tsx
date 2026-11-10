import { useState } from 'react'
import { ALLOWED_TYPES, requestFileUrl, type CourseRequestStatus } from '../api/courseRequests'

export const REQUEST_STATUS: Record<CourseRequestStatus, { label: string; className: string }> = {
  pending: { label: 'Pending', className: 'bg-amber-50 text-amber-800 ring-amber-200' },
  in_progress: { label: 'In progress', className: 'bg-sky-50 text-sky-800 ring-sky-200' },
  added: { label: 'Added', className: 'bg-emerald-50 text-emerald-700 ring-emerald-200' },
  declined: { label: 'Declined', className: 'bg-slate-100 text-slate-600 ring-slate-200' },
}

export function fileSize(bytes: number): string {
  return bytes >= 1024 * 1024 ? `${(bytes / 1024 / 1024).toFixed(1)} MB` : `${Math.max(1, Math.round(bytes / 1024))} KB`
}

export function FileButton({ path, name, size, type }: { path: string; name: string; size: number; type: string }) {
  const [error, setError] = useState<string | null>(null)
  async function open() {
    setError(null)
    try {
      window.open(await requestFileUrl(path), '_blank', 'noopener')
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Could not open the file')
    }
  }
  return (
    <li>
      <button
        type="button"
        onClick={open}
        className="flex w-full items-center gap-2 rounded-lg px-2 py-1.5 text-left text-sm ring-1 ring-slate-200 hover:bg-slate-50"
        data-testid="request-file"
      >
        <span className="rounded bg-slate-100 px-1.5 py-0.5 text-[10px] font-bold text-slate-600">{ALLOWED_TYPES[type] ?? 'FILE'}</span>
        <span className="min-w-0 flex-1 truncate">{name}</span>
        <span className="text-xs text-slate-500">{fileSize(size)}</span>
      </button>
      {error && <p className="mt-1 text-xs text-red-600">{error}</p>}
    </li>
  )
}
