/** Dates as "18 Oct 2026" everywhere in the app. */
export function formatDate(value: string | Date): string {
  return new Date(value).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' })
}

export function percent(probability: number): string {
  return `${Math.round(probability * 100)}%`
}
