from django.urls import path
from django.contrib import admin

from twitterclone.twitteruser.views import profile, index, toggle_following
from twitterclone.twitteruser.models import TwitterUser

admin.site.register(TwitterUser)

urlpatterns = [
    path('<str:username>/', profile, name='profile'),
    path('', index, name='homepage'),
    path("follow/<str:username>", toggle_following),
]
