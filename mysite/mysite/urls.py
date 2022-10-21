from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls')), 
    path('',include('post.urls')),
    path('',include('recipe.urls')),
    path('',include('notification.urls')),
    path('summernote/', include('django_summernote.urls')),
]
