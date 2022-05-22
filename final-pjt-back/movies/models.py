from django.db import models
from django.conf import settings


class Genre(models.Model):
    genre_ids = models.CharField(max_length=50)

class Movie(models.Model):
    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=200)
    genre_ids = models.ManyToManyField(Genre, related_name='genre_ids')
    original_language = models.CharField(max_length=100)
    original_title = models.CharField(max_length=200)
    overview = models.CharField(max_length=400)
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    video = models.BooleanField(default=False)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def __str__(self):
        return self.original_title