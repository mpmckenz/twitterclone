from django.db import models
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    notify_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    noticed = models.BooleanField(default=False)
