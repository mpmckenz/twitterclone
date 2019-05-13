from django import forms
from authentication.models import UserProfile

class SignupForm(forms.Form):
    # name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())