import type { BadgeKey } from '../api/gamification'

export type BadgeInfo = { key: BadgeKey; title: string; howTo: string; kind: 'streak' | 'quiz' | 'mastery' }

/** Shelf order. The rules themselves live in the database (gamification_for). */
export const BADGES: BadgeInfo[] = [
  { key: 'first_quiz', title: 'First quiz', howTo: 'Complete any quiz.', kind: 'quiz' },
  { key: 'first_perfect', title: 'Perfect score', howTo: 'Score 100% on a quiz.', kind: 'quiz' },
  { key: 'five_mastered', title: '5 topics mastered', howTo: 'Reach 70% or more as your latest score on 5 topics.', kind: 'mastery' },
  ...([3, 7, 14, 30, 50, 100] as const).map((n) => ({
    key: `streak_${n}` as BadgeKey,
    title: `${n}-day streak`,
    howTo: `Do a quiz or log study ${n} days in a row.`,
    kind: 'streak' as const,
  })),
]

export function badgeInfo(key: BadgeKey): BadgeInfo {
  return BADGES.find((b) => b.key === key) as BadgeInfo
}
