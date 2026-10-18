import { daysBetween } from './consistency'

export type Reminder = {
  id: string
  tone: 'warning' | 'info'
  text: string
  action?: { label: string; to: string }
}

export type ReminderInput = {
  now: Date
  studyLogs: { topic_id: string; logged_at: string }[]
  topicScores: Map<string, number>
  topics: { id: string; title: string }[]
  coursesWithoutDiagnostic: { code: string; diagnostic_quiz_id: string }[]
}

export const INACTIVE_DAYS = 3
export const NEGLECTED_WEAK_TOPIC_DAYS = 7
const MAX_REMINDERS = 4

/** In-app reminders, computed from stored dates every time the dashboard loads. */
export function buildReminders(input: ReminderInput): Reminder[] {
  const { now, studyLogs, topicScores, topics, coursesWithoutDiagnostic } = input
  const reminders: Reminder[] = []

  const lastStudied = new Map<string, Date>()
  for (const log of studyLogs) {
    const at = new Date(log.logged_at)
    const prev = lastStudied.get(log.topic_id)
    if (!prev || at > prev) lastStudied.set(log.topic_id, at)
  }

  // Weak topics (below 50%) that have not been studied for a week, weakest first.
  const weak = topics
    .filter((t) => (topicScores.get(t.id) ?? 100) < 50)
    .sort((a, b) => (topicScores.get(a.id) ?? 0) - (topicScores.get(b.id) ?? 0))
  for (const topic of weak) {
    const studied = lastStudied.get(topic.id)
    const idle = studied ? daysBetween(studied, now) : null
    if (idle !== null && idle < NEGLECTED_WEAK_TOPIC_DAYS) continue
    const score = Math.round(topicScores.get(topic.id) ?? 0)
    reminders.push({
      id: `weak-${topic.id}`,
      tone: 'warning',
      text:
        idle === null
          ? `${topic.title} scored ${score}% and you haven't studied it yet.`
          : `${topic.title} scored ${score}% and you last studied it ${idle} days ago.`,
      action: { label: 'Open topic', to: `/topics/${topic.id}` },
    })
  }

  const latest = studyLogs.reduce<Date | null>((max, l) => {
    const at = new Date(l.logged_at)
    return !max || at > max ? at : max
  }, null)
  if (!latest) {
    reminders.push({
      id: 'no-study',
      tone: 'info',
      text: "You haven't logged a study session yet. Logging helps the system spot neglected topics.",
      action: { label: 'Log study', to: '/log' },
    })
  } else if (daysBetween(latest, now) >= INACTIVE_DAYS) {
    reminders.push({
      id: 'inactive',
      tone: 'warning',
      text: `No study logged in ${daysBetween(latest, now)} days. A short session keeps your streak going.`,
      action: { label: 'Log study', to: '/log' },
    })
  }

  for (const course of coursesWithoutDiagnostic) {
    reminders.push({
      id: `diagnostic-${course.code}`,
      tone: 'info',
      text: `Take the ${course.code} diagnostic quiz so your recommendations can be personalised.`,
      action: { label: 'Start quiz', to: `/quiz/${course.diagnostic_quiz_id}` },
    })
  }

  return reminders.slice(0, MAX_REMINDERS)
}
