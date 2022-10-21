from django.db import models
from user.models import User
from post.models import Post
class Notification(models.Model):
    FOLLOWER = 'followers'
    POSTLIKE = 'post_like'
    COMMENT = 'comment'

    CHOICES = (
        (FOLLOWER, 'followers'),
        (POSTLIKE, 'post_like'),
        (COMMENT, 'comment'),
    )
    #나 자신
    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    
    post_like = models.ForeignKey(Post, related_name='notifications', on_delete=models.CASCADE, null=True, blank=True)
    #하는 사람
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_notifications', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']

