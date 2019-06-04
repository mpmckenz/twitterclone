from django.shortcuts import render, redirect

from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator


class Profile(View):
    def get(self, request, username):
        other_user = TwitterUser.objects.filter(username=username).first()
        tweets = Tweet.objects.filter(username_id=other_user)
        active_user = TwitterUser.objects.filter(
            username=request.user.twitteruser).first()
        follow_count = other_user.following.count()
        other_user_followers = other_user.following.all()
        followers_tweets = Tweet.objects.filter(
            username__in=other_user_followers)
        all_tweets = tweets | followers_tweets
        all_tweets = all_tweets.order_by('-time')
        items = {'other_user': other_user, "active_user": active_user, "tweets": all_tweets, "tweet_count": len(
            tweets), "follow_count": follow_count}
        return render(request, 'profile.html', items)


@method_decorator(login_required, name='dispatch')
class Index(View):
    def get(self, request):
        html = 'index.html'
        users = request.user.twitteruser.following.all()
        active_user = request.user.twitteruser
        active_user_tweets = Tweet.objects.filter(
            username=active_user)
        followers_tweets = Tweet.objects.filter(
            username__in=users)
        all_tweets = followers_tweets | active_user_tweets
        all_tweets = all_tweets.order_by('-time')
        follow_count = active_user.following.count()
        notification_count = 0
        for check in request.user.twitteruser.notification_set.get_queryset().all():
            if not check.noticed:
                notification_count += 1
        items = {"active_user": active_user, 'followers_tweets': all_tweets,
                 "tweet_count": active_user_tweets.count(), "follow_count": follow_count, "notification_count": notification_count}
        return render(request, html, items)


class ToggleFollowing(View):
    def get(self, request, username):
        is_following = False
        other_user = TwitterUser.objects.filter(username=username).first()
        active_user = TwitterUser.objects.filter(
            username=request.user.twitteruser).first()
        if other_user not in active_user.following.get_queryset():
            active_user.following.add(other_user)
            is_following = True
        else:
            active_user.following.remove(other_user)
            is_following = False
        active_user.save()
        return redirect("/{}/".format(other_user.username))
