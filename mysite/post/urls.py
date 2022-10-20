from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    #post
    path('', views.index, name='index'),
    path('post/detail/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/mylist/<int:user_id>/', views.my_list, name='my-list'),
    path('post/create/', views.post_create, name='post-create'),
    path('post/update/<int:post_id>/', views.post_update, name='post-update'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post-delete'),
    
    #comment
    path('comment/create/<int:comment_id>/', views.comment_create, name='comment-create'),
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment-update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment-delete'),
    
    #like
    path('post/likes/<int:post_id>/', views.likes, name='post-likes'),
    path('post/likes/list/<int:post_id>/', views.likes_list, name='like-list'),

    #search
    path('search/', views.search, name='search'),

    #follow
    path('post/followlist/<int:post_id>/', views.follow_list, name='follow-list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media루트 경로를 설정
