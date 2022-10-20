from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('notifications_list/<int:user_id>/', views.notifications, name='notifications'),
    path('notifications/<int:user_id>/',views.process_notifications, name='process-notifications'),
]


