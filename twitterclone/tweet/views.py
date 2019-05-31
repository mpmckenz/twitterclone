from django.shortcuts import render, redirect
from .models import Tweet
from twitterclone.tweet.forms import AddTweetForm
from twitterclone.tweet.models import Tweet
from twitterclone.notification.views import tweet_notif_checker


def composetweet(request):
    html = 'compose.html'
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                username=request.user.twitteruser,
                message=data["message"],
            )
            # look in message and see if @ username is used and that's when a notification counts gets added
            tweet_notif_checker(tweet)
            return redirect('/')
    else:
        form = AddTweetForm()
    return render(request, html, {'form': form})


def specifictweetview(request, id):
    html = 'tweet.html'
    tweets = Tweet.objects.filter(pk=id)
    return render(request, html, {'tweets': tweets})
