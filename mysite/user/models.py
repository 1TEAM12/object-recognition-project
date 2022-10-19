from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True, null=True)
    email = models.CharField(max_length=50, unique=True, null=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')