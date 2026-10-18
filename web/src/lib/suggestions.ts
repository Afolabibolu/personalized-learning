/** Below this averaged model probability a topic is not flagged: "Keep it up". */
export const ATTENTION_PROBABILITY = 0.5

export type SuggestionInput = {
  latestScore: number | null
  daysSinceStudied: number | null // null = never studied
  hasTopicQuiz: boolean
}

/** A short, concrete next step for a topic the models consider on track. */
export function keepItUpSuggestion({ latestScore, daysSinceStudied, hasTopicQuiz }: SuggestionInput): string {
  if (daysSinceStudied === null) {
    return 'Not studied yet. A quick read of this resource will lock in what you already know.'
  }
  if (daysSinceStudied >= 7) {
    return `Last studied ${daysSinceStudied} days ago. A 15-minute review keeps it fresh.`
  }
  if (latestScore !== null && latestScore >= 80 && hasTopicQuiz) {
    return `Scoring ${Math.round(latestScore)}%. Try the topic quiz: questions you haven't seen come first.`
  }
  return 'On track. One practice session this week keeps it that way.'
}
