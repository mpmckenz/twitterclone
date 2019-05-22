from django.shortcuts import render

from twitterclone.twitteruser.models import TwitterUser


def profile(request, username):
    user = TwitterUser.objects.filter(username=username)
    return render(request, 'index.html', {'data': user})
