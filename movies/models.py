from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Score(models.Model):
    content = models.CharField(max_length=100)
    value = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)