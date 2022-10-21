from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True, null=True)
    email = models.CharField(max_length=50, unique=True, null=True)
    followings = models.ManyToManyField('self', symmetrical=False, blank=True, related_name= 'followers')