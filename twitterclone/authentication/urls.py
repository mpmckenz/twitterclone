from django.contrib import admin
from django.urls import path
from twitterclone.authentication.views import signup, login_view, logout_view


urlpatterns = [
    path("login/", login_view),
    path('signup/', signup),
    path("logout/", logout_view),
    # path('', index, name="homepage"),
]
