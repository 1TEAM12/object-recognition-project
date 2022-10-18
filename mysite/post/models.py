from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to="post_pics", blank=True)
    content = models.TextField(max_length=100,null=True,blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    
    def __str__(self):
        return self.title