import { useEffect, useRef, useState } from 'react'
import { Button } from './ui'

function clock(seconds: number): string {
  const h = Math.floor(seconds / 3600)
  const m = Math.floor((seconds % 3600) / 60)
  const s = seconds % 60
  const mm = String(m).padStart(2, '0')
  const ss = String(s).padStart(2, '0')
  return h ? `${h}:${mm}:${ss}` : `${mm}:${ss}`
}

/** Optional stopwatch: start, pause, then stop to fill in the duration (whole minutes, at least 1). */
export function StudyTimer({ onStop }: { onStop: (minutes: number) => void }) {
  const [elapsed, setElapsed] = useState(0) // seconds counted before the current run
  const [runningSince, setRunningSince] = useState<number | null>(null)
  const [, tick] = useState(0)
  const timer = useRef<number | null>(null)

  useEffect(() => {
    if (runningSince === null) return
    timer.current = window.setInterval(() => tick((n) => n + 1), 1000)
    return () => {
      if (timer.current) window.clearInterval(timer.current)
    }
  }, [runningSince])

  const seconds = elapsed + (runningSince === null ? 0 : Math.floor((Date.now() - runningSince) / 1000))
  const started = runningSince !== null || elapsed > 0

  function pause() {
    setElapsed(seconds)
    setRunningSince(null)
  }

  function stop() {
    onStop(Math.min(300, Math.max(1, Math.round(seconds / 60))))
    setElapsed(0)
    setRunningSince(null)
  }

  return (
    <div className="flex flex-wrap items-center gap-3 rounded-xl bg-slate-50 p-3" data-testid="study-timer">
      <span className="font-mono text-2xl font-semibold tabular-nums text-slate-800" aria-live="off">
        {clock(seconds)}
      </span>
      <div className="flex gap-2">
        {runningSince === null ? (
          <Button type="button" variant="secondary" className="px-3 py-1.5" onClick={() => setRunningSince(Date.now())}>
            {started ? 'Resume' : 'Start timer'}
          </Button>
        ) : (
          <Button type="button" variant="secondary" className="px-3 py-1.5" onClick={pause}>
            Pause
          </Button>
        )}
        {started && (
          <Button type="button" className="px-3 py-1.5" onClick={stop}>
            Stop and use time
          </Button>
        )}
      </div>
      <p className="w-full text-xs text-slate-500">Optional. Stopping fills in the duration below.</p>
    </div>
  )
}
