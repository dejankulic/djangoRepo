from django.forms import ModelForm
from .models import Movie, Comment

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['movieName', 'rating']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

