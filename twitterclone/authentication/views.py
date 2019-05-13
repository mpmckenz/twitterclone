from django.shortcuts import render

from .models import Author, Recipe
from authentication.forms import SignupForm, LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import reverse
from django.http import HttpResponseRedirect

def signup(request):
    html = 'form.html'
    form = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                # Will go to the user model
                username=data["username"],
                email=data["email"],
                password=data["password"],
            )
            login(request, user)
            # Author model
            Author.objects.create(name=data["name"], user=user)
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = SignupForm()
    return render(request, html, {"form": form})