from django.contrib import admin
from django.urls import path
from twitterclone.tweet.views import composetweet
from twitterclone.tweet.models import Tweet

admin.site.register(Tweet)

urlpatterns = [
    path("compose/", composetweet),
]
