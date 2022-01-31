from django.db import models
from django.db.models import Model


class TrendingMovies(Model):
    release_date = models.CharField(max_length=200),
    adult = models.BooleanField(),
    backdrop_path = models.CharField(max_length=200),
    vote_count = models.IntegerField(),
    original_language = models.CharField(max_length=2),
    id = models.IntegerField(),
    poster_path = models.CharField(max_length=200),
    vote_average = models.FloatField(),
    video = models.BooleanField(),
    title = models.CharField(max_length=50),
    original_title = models.CharField(max_length=50),
    overview = models.CharField(max_length=1000),
    popularity = models.FloatField(),
    media_type = models.CharField(max_length=20)


def convert(json_object):
    model_object = TrendingMovies()
    for key in json_object:
        if hasattr(model_object, key):
            setattr(model_object, key, json_object[key])

    return model_object
