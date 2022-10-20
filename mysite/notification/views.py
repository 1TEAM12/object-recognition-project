from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Notification
from post.models import Post

@login_required(login_url='user:signin')
def notifications(request, user_id):
    context =dict()
    context['notifications'] = Notification.objects.all()
    return render(request, 'notification/notification/notifications.html',context=context)

def process_notifications(request, user_id):
    if request.method == 'POST':
        notification = get_object_or_404(Notification, id=user_id)
        notification.delete()
        return redirect(request.META['HTTP_REFERER']) 
    