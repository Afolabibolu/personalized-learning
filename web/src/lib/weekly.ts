const DAY_MS = 86_400_000

export type WeeklySummaryInput = {
  now: Date
  studyLogs: { logged_at: string; duration_minutes: number }[]
  progress: { topic_id: string; latest_score: number; previous_score: number | null; latest_completed_at: string }[]
  titles: Map<string, string>
}

export type WeeklySummary = {
  minutesThisWeek: number
  minutesLastWeek: number
  /** Topics whose latest attempt (within the last 7 days) beat the previous one, biggest gain first. */
  improved: { topic_id: string; title: string; from: number; to: number }[]
}

/** "This week" is the last 7 days; "last week" the 7 days before that. */
export function weeklySummary({ now, studyLogs, progress, titles }: WeeklySummaryInput): WeeklySummary {
  const age = (iso: string) => now.getTime() - new Date(iso).getTime()
  let minutesThisWeek = 0
  let minutesLastWeek = 0
  for (const log of studyLogs) {
    const a = age(log.logged_at)
    if (a < 0) continue
    if (a < 7 * DAY_MS) minutesThisWeek += log.duration_minutes
    else if (a < 14 * DAY_MS) minutesLastWeek += log.duration_minutes
  }
  const improved = progress
    .filter((p) => p.previous_score !== null && p.latest_score > p.previous_score && age(p.latest_completed_at) < 7 * DAY_MS)
    .sort((a, b) => b.latest_score - (b.previous_score ?? 0) - (a.latest_score - (a.previous_score ?? 0)))
    .map((p) => ({ topic_id: p.topic_id, title: titles.get(p.topic_id) ?? 'A topic', from: p.previous_score as number, to: p.latest_score }))
  return { minutesThisWeek, minutesLastWeek, improved }
}
