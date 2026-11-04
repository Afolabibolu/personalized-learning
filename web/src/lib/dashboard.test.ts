import { describe, expect, it } from 'vitest'
import { buildReminders, type ReminderInput } from './reminders'
import { weeklySummary } from './weekly'

const today = new Date(2026, 9, 18, 15, 0) // 18 Oct 2026, local time

function daysAgo(n: number, hour = 12): string {
  const d = new Date(today)
  d.setDate(d.getDate() - n)
  d.setHours(hour)
  return d.toISOString()
}

describe('reminders', () => {
  const base: ReminderInput = {
    now: today,
    studyLogs: [],
    topicScores: new Map(),
    topics: [
      { id: 'fuzzy', title: 'Fuzzy Logic' },
      { id: 'search', title: 'Search' },
      { id: 'expert', title: 'Expert Systems' },
    ],
  }

  it('flags weak topics never studied, weakest first', () => {
    const reminders = buildReminders({
      ...base,
      studyLogs: [{ topic_id: 'expert', logged_at: daysAgo(1) }],
      topicScores: new Map([['fuzzy', 30], ['search', 45], ['expert', 90]]),
    })
    expect(reminders.map((r) => r.id)).toEqual(['weak-fuzzy', 'weak-search'])
    expect(reminders[0].text).toContain("haven't studied it yet")
  })

  it('skips weak topics studied within the last week', () => {
    const reminders = buildReminders({
      ...base,
      studyLogs: [{ topic_id: 'fuzzy', logged_at: daysAgo(2) }],
      topicScores: new Map([['fuzzy', 30]]),
    })
    expect(reminders.map((r) => r.id)).not.toContain('weak-fuzzy')
  })

  it('reminds after three days without study', () => {
    const reminders = buildReminders({ ...base, studyLogs: [{ topic_id: 'search', logged_at: daysAgo(3) }] })
    expect(reminders).toEqual([expect.objectContaining({ id: 'inactive', text: expect.stringContaining('3 days') })])
  })

  it('does not nag the day after studying', () => {
    expect(buildReminders({ ...base, studyLogs: [{ topic_id: 'search', logged_at: daysAgo(1) }] })).toEqual([])
  })

  it('asks new students to log study (diagnostics are prompted in the recommendations card)', () => {
    expect(buildReminders(base).map((r) => r.id)).toEqual(['no-study'])
  })
})

describe('weekly summary', () => {
  const titles = new Map([['fuzzy', 'Fuzzy Logic'], ['search', 'Search'], ['old', 'Old topic']])

  it('compares minutes this week with last week', () => {
    const s = weeklySummary({
      now: today,
      studyLogs: [
        { logged_at: daysAgo(0), duration_minutes: 30 },
        { logged_at: daysAgo(6), duration_minutes: 15 },
        { logged_at: daysAgo(8), duration_minutes: 60 },
        { logged_at: daysAgo(20), duration_minutes: 90 },
      ],
      progress: [],
      titles,
    })
    expect([s.minutesThisWeek, s.minutesLastWeek]).toEqual([45, 60])
  })

  it('lists topics that improved this week, biggest gain first', () => {
    const s = weeklySummary({
      now: today,
      studyLogs: [],
      progress: [
        { topic_id: 'search', latest_score: 60, previous_score: 50, latest_completed_at: daysAgo(1) },
        { topic_id: 'fuzzy', latest_score: 70, previous_score: 40, latest_completed_at: daysAgo(2) },
        { topic_id: 'old', latest_score: 90, previous_score: 10, latest_completed_at: daysAgo(10) },
      ],
      titles,
    })
    expect(s.improved.map((t) => [t.title, t.from, t.to])).toEqual([['Fuzzy Logic', 40, 70], ['Search', 50, 60]])
  })
})

describe('dates', () => {
  it('reads like "18 Oct 2026", with three-letter months', async () => {
    const { formatDate } = await import('./format')
    expect(formatDate(new Date(2026, 9, 18))).toBe('18 Oct 2026')
    expect(formatDate(new Date(2026, 8, 28))).toBe('28 Sep 2026')
  })
})
