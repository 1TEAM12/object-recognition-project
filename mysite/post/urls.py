from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/detail/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/mylist/<int:user_id>/', views.my_list, name='my-list'),
    path('post/create/', views.create, name='create'),
    path('post/update/<int:post_id>/', views.update, name='update'),

    path('comment/create/<int:comment_id>/', views.comment_create, name='comment-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media루트 경로를 설정
