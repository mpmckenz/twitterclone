from django import forms
from twitterclone.tweet.models import Tweet


class AddTweetForm(forms.Form):
    message = forms.CharField(max_length=200)
