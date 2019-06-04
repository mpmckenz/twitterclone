from django.shortcuts import render, redirect
from .models import Tweet
from twitterclone.tweet.forms import AddTweetForm
from twitterclone.tweet.models import Tweet
from twitterclone.notification.views import tweet_notif_checker

from django.views import View


class ComposeTweet(View):
    def get(self, request):
        html = 'compose.html'
        form = AddTweetForm()
        return render(request, html, {'form': form})

    def post(self, request):
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                username=request.user.twitteruser,
                message=data["message"],
            )
            tweet_notif_checker(tweet)
            return redirect('/')


class SpecificTweetView(View):
    def get(self, request, id):
        html = 'tweet.html'
        tweets = Tweet.objects.filter(pk=id)
        return render(request, html, {'tweets': tweets})
