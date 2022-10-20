from .models import Notification
#class로 여유가 된다면 변경하기!
def create_notification(request, to_user, notification_type, post_like):
    notification = Notification.objects.create(to_user=to_user, notification_type=notification_type, created_by=request.user, post_like=post_like)