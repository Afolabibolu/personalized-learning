import { supabase } from './supabase'

export type HealthcheckRow = { id: number; message: string; created_at: string }

export async function fetchHealthcheckRow(): Promise<HealthcheckRow> {
  const { data, error } = await supabase
    .from('healthcheck')
    .select('id, message, created_at')
    .limit(1)
    .single()
  if (error) throw error
  return data
}
