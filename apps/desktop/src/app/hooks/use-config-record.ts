import { useQuery } from '@tanstack/react-query'

import { getKovaConfigRecord } from '@/kova'
import { queryClient, writeCache } from '@/lib/query-client'
import type { KovaConfigRecord } from '@/types/kova'

// One shared cache for the whole profile config record (`GET /api/config`).
// Every settings surface (MCP, model, config) reads and writes through this key
// so a save in one shows in the others, and revisiting a tab paints the cache
// instead of blanking on a fresh fetch.
//
// Distinct from session/hooks/use-kova-config.ts, which is side-effecting —
// it pushes personality/cwd/voice/… into the session stores for live chat.
export const KOVA_CONFIG_KEY = ['kova-config-record'] as const

// staleTime 0 → serve cache instantly, background-revalidate on every mount.
export const useKovaConfigRecord = () =>
  useQuery({ queryKey: KOVA_CONFIG_KEY, queryFn: getKovaConfigRecord, staleTime: 0 })

export const setKovaConfigCache = writeCache<KovaConfigRecord>(KOVA_CONFIG_KEY)

export const invalidateKovaConfig = () => queryClient.invalidateQueries({ queryKey: KOVA_CONFIG_KEY })
