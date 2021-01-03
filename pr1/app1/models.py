from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):

    movieName = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.movieName

class Comment(models.Model):
    content = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content