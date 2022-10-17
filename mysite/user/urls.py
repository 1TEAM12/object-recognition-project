from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('',views.index, name='index'),
    path('account/signup/', views.signup, name='signup'),
    path('account/signin/', views.signin, name='signin'),
    path('account/logout/', views.logout, name='logout'), 
]