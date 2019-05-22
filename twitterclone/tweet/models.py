from django.db import models

from django.contrib.auth.models import User
from twitterclone.twitteruser.models import TwitterUser


class Tweet(models.Model):
    username = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.CharField(max_length=140)
