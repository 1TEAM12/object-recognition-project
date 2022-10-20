from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
    path('recipe/like/list/<int:recipe_id>/', views.recipe_like_list, name='recipe-like-list'),
    path('recipe/likes/<int:recipe_id>/', views.likes, name='recipe-likes'),
    ]