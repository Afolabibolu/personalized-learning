import { formatDate } from './format'

/** "just now", "5 min ago", "3 hours ago", "yesterday", then "18 Oct 2026". */
export function timeAgo(value: string, now: Date = new Date()): string {
  const seconds = Math.max(0, (now.getTime() - new Date(value).getTime()) / 1000)
  if (seconds < 60) return 'just now'
  if (seconds < 3600) return `${Math.floor(seconds / 60)} min ago`
  if (seconds < 86_400) {
    const hours = Math.floor(seconds / 3600)
    return `${hours} hour${hours === 1 ? '' : 's'} ago`
  }
  if (seconds < 2 * 86_400) return 'yesterday'
  return formatDate(value)
}
