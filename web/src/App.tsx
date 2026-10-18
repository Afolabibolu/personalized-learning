import { useEffect, useState } from 'react'
import { fetchHealthcheckRow, type HealthcheckRow } from './api/healthcheck'

export default function App() {
  const [row, setRow] = useState<HealthcheckRow | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchHealthcheckRow()
      .then(setRow)
      .catch((e: Error) => setError(e.message))
  }, [])

  return (
    <main className="min-h-screen bg-slate-50 px-4 py-10 text-slate-900">
      <div className="mx-auto max-w-md rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200">
        <h1 className="text-lg font-semibold">Supabase connection check</h1>
        {error && <p className="mt-3 text-sm text-red-600">Error: {error}</p>}
        {!error && !row && <p className="mt-3 text-sm text-slate-500">Loading…</p>}
        {row && (
          <p className="mt-3 text-sm" data-testid="healthcheck-row">
            Row {row.id}: <span className="font-medium">{row.message}</span>
          </p>
        )}
      </div>
    </main>
  )
}
