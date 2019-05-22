from django.shortcuts import render

from twitterclone.twitteruser.models import TwitterUser
from twitterclone.authentication.forms import SignupForm, LoginForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import reverse
from django.http import HttpResponseRedirect

from twitterclone.tweet.models import Tweet


@login_required()
def index(request):
    html = 'index.html'
    items = {"data": TwitterUser.objects.all(), 'tweet': Tweet.objects.all()}
    return render(request, html, items)


def signup(request):
    html = 'signupform.html'
    form = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
            )
            user.save()
            TwitterUser.objects.create(
                user=user,
                username=data['username']
            )
            login(request, user)
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = SignupForm()
    return render(request, html, {"form": form})


def login_view(request):
    html = "loginform.html"
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
