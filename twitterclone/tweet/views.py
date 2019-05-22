from django.shortcuts import render, redirect
from .models import Tweet
from twitterclone.tweet.forms import AddTweetForm
# from twitterclone.tweet.models import Tweet


def composetweet(request):
    html = 'compose.html'
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                message=data["message"],
            )
            tweet.save()
            render(request, html)
            return redirect('/')
    else:
        form = AddTweetForm()
    return render(request, html, {'form': form})
