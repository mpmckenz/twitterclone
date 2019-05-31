from django.contrib import admin
from django.urls import path
from twitterclone.notification.models import Notification
from twitterclone.notification.views import notification

admin.site.register(Notification)

urlpatterns = [
    path("notifications/", notification)
]
