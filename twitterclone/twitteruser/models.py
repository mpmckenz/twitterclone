from django.db import models

from django.contrib.auth.models import User


class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    following = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False, blank=True, null=True)

    def __str__(self):
        return self.username
