from twitterclone.twitteruser.models import TwitterUser
from django.shortcuts import redirect, render
from twitterclone.notification.models import Notification
import re


def notification(request):
    html = "notifications.html"
    # _set so I can get_queryset
    notifications = request.user.twitteruser.notification_set.get_queryset().all()
    tweets = []
    for check in notifications:
        if not check.noticed:
            tweets += [check.tweet]
            Notification.objects.filter(pk=check.pk).update(noticed=True)
    return render(request, html, {'tweets': tweets})


def tweet_notif_checker(tweet):
    notifications = re.findall(r"(@\w+)", tweet.message)
    if notifications:
        for user in notifications:
            notify_user = TwitterUser.objects.filter(
                username=user[1:]).first()
            if notify_user:
                Notification.objects.create(
                    tweet=tweet,
                    notify_user=notify_user
                )
        return redirect('/')
