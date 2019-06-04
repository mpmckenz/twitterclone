from django.contrib import admin
from django.urls import path
from twitterclone.tweet.views import ComposeTweet, SpecificTweetView
from twitterclone.tweet.models import Tweet

admin.site.register(Tweet)

urlpatterns = [
    path("compose/", ComposeTweet.as_view(), name="composetweet"),
    path('<int:id>/', SpecificTweetView.as_view(), name="viewspecifictweet"),
]
