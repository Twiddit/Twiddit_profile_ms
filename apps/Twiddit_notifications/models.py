from django.db import models
from apps.Twiddit_profile.models import User


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    followerId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followedId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
    created_at = models.DateTimeField(blank=True, null=True)