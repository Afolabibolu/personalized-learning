const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

/** Dates as "18 Oct 2026" everywhere in the app (three-letter months, whatever the browser locale). */
export function formatDate(value: string | Date): string {
  const d = new Date(value)
  return `${d.getDate()} ${MONTHS[d.getMonth()]} ${d.getFullYear()}`
}

export function percent(probability: number): string {
  return `${Math.round(probability * 100)}%`
}
