import { useMutation, useQueryClient } from '@tanstack/react-query'
import { markNotificationsRead } from '../api/notifications'
import { NotificationItem, useNotifications, useOpenNotification } from '../components/NotificationBell'
import { Button, ButtonLink, Card, ErrorMessage, PageHeader, Spinner } from '../components/ui'

export function NotificationsPage() {
  const notifications = useNotifications()
  const open = useOpenNotification()
  const queryClient = useQueryClient()
  const unread = (notifications.data ?? []).filter((n) => !n.read_at)

  const markAll = useMutation({
    mutationFn: () => markNotificationsRead(unread.map((n) => n.id)),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['notifications'] }),
  })

  return (
    <div className="mx-auto max-w-xl">
      <PageHeader eyebrow="Notifications" title="Reminders and feedback">
        Study reminders and feedback on your progress. Change when you get reminded on your profile.
      </PageHeader>

      {notifications.isPending && <Spinner />}
      {notifications.isError && <ErrorMessage error={notifications.error} />}

      {notifications.data && (
        <Card className="p-2">
          <div className="flex items-center justify-between px-3 py-2">
            <p className="text-sm text-slate-600">{unread.length} unread</p>
            <div className="flex gap-2">
              {unread.length > 0 && (
                <Button variant="ghost" className="px-3 py-1.5" onClick={() => markAll.mutate()} disabled={markAll.isPending}>
                  Mark all read
                </Button>
              )}
              <ButtonLink to="/profile" variant="secondary" className="px-3 py-1.5">
                Reminder settings
              </ButtonLink>
            </div>
          </div>
          {notifications.data.length === 0 ? (
            <p className="px-3 py-10 text-center text-sm text-slate-500">
              No notifications yet. Take a quiz or log a study session and reminders will start here.
            </p>
          ) : (
            <div className="grid gap-0.5">
              {notifications.data.map((n) => (
                <NotificationItem key={n.id} n={n} onOpen={open} />
              ))}
            </div>
          )}
        </Card>
      )}
    </div>
  )
}
