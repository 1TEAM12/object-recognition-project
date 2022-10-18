from django.db import models
from user.models import User
from post.models import Post

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to="post_pics", blank=True)
    youtube_url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    like_authors = models.ManyToManyField(User, related_name='like_recipes')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='recipes')
    
    def __str__(self):
        return self.title
