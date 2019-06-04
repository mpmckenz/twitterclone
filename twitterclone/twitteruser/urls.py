from django.urls import path
from django.contrib import admin

from twitterclone.twitteruser.views import Profile, Index, ToggleFollowing
from twitterclone.twitteruser.models import TwitterUser

admin.site.register(TwitterUser)

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path("follow/<str:username>", ToggleFollowing.as_view()),
    path('<str:username>/', Profile.as_view(), name='profile'),
]
