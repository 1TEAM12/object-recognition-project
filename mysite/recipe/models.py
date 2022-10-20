from django.db import models
from user.models import User
from post.models import Post, Dessert

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=30, blank=True)
    youtube_url = models.URLField(max_length=100)
    ingred = models.CharField(max_length=20, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
      
    like_authors = models.ManyToManyField(User, related_name='like_recipes')
    
    def __str__(self):
        return self.title
