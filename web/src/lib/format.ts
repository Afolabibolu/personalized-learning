const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

/** Dates as "18 Oct 2026" everywhere in the app (three-letter months, whatever the browser locale). */
export function formatDate(value: string | Date): string {
  const d = new Date(value)
  return `${d.getDate()} ${MONTHS[d.getMonth()]} ${d.getFullYear()}`
}

/** A calendar day from the database ("2026-11-02") as "2 Nov 2026", with no timezone shift. */
export function formatDay(day: string): string {
  const [y, m, d] = day.split('-').map(Number)
  return `${d} ${MONTHS[m - 1]} ${y}`
}

export function percent(probability: number): string {
  return `${Math.round(probability * 100)}%`
}
