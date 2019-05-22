from django.urls import path
from django.contrib import admin

from twitterclone.twitteruser.views import profile
from twitterclone.twitteruser.models import TwitterUser

admin.site.register(TwitterUser)

urlpatterns = [
    path('<str:username>/', profile, name='profile')
]
