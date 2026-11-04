// Streaks, the 14-day strip, XP, freezes and badges are computed by the database
// (gamification_for, in Nigerian time), not here; see scripts/test_gamification.py.

/** Whole days between two moments (floor), never negative. */
export function daysBetween(earlier: Date, later: Date): number {
  return Math.max(0, Math.floor((later.getTime() - earlier.getTime()) / 86_400_000))
}
