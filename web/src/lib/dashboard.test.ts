import { describe, expect, it } from 'vitest'
import { activityDays, activityStrip, currentStreak, dayKey } from './consistency'
import { buildReminders, type ReminderInput } from './reminders'

const today = new Date(2026, 9, 18, 15, 0) // 18 Oct 2026, local time

function daysAgo(n: number, hour = 12): string {
  const d = new Date(today)
  d.setDate(d.getDate() - n)
  d.setHours(hour)
  return d.toISOString()
}

describe('streak', () => {
  it('counts consecutive days ending today', () => {
    expect(currentStreak(activityDays([daysAgo(0), daysAgo(1), daysAgo(2), daysAgo(4)]), today)).toBe(3)
  })

  it('still counts up to yesterday when nothing is logged today yet', () => {
    expect(currentStreak(activityDays([daysAgo(1), daysAgo(2)]), today)).toBe(2)
  })

  it('is zero after a missed day', () => {
    expect(currentStreak(activityDays([daysAgo(2), daysAgo(3)]), today)).toBe(0)
  })

  it('counts several events on one day once', () => {
    expect(currentStreak(activityDays([daysAgo(0, 9), daysAgo(0, 18)]), today)).toBe(1)
  })
})

describe('activity strip', () => {
  it('covers 14 days, oldest first, ending today', () => {
    const strip = activityStrip(activityDays([daysAgo(0), daysAgo(13), daysAgo(20)]), today)
    expect(strip).toHaveLength(14)
    expect(strip[13]).toMatchObject({ key: dayKey(today), isToday: true, active: true })
    expect(strip[0].active).toBe(true)
    expect(strip.filter((d) => d.active)).toHaveLength(2)
  })
})

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
    coursesWithoutDiagnostic: [],
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

  it('asks new students to log study and take diagnostics', () => {
    const reminders = buildReminders({
      ...base,
      coursesWithoutDiagnostic: [{ code: 'CSC 531', diagnostic_quiz_id: 'q1' }],
    })
    expect(reminders.map((r) => r.id)).toEqual(['no-study', 'diagnostic-CSC 531'])
    expect(reminders[1].action?.to).toBe('/quiz/q1')
  })
})
