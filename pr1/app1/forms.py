from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Movie,Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movieName', 'rating']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','movie']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

