from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('account/signup/', views.signup, name='signup'),
    path('account/signin/', views.signin, name='signin'),
    path('account/logout/', views.logout, name='logout'), 
    path('account/login/kakao/', views.kakao_social_login, name='kakao-login'),
    path('account/login/kakao/callback/', views.kakao_social_login_callback, name='kakao-login-callback'),

    #follow
    path('user/userlist/', views.userlist, name='userlist'),
    path('user/follow/<int:id>/', views.follow, name='follow'),
]