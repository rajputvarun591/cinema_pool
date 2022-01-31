from django.http import HttpResponse
from django.shortcuts import render

from cinema_pool.services import getTrendingMovies
from cinema_pool.services import getMovieGenres
from cinema_pool.services import images_base_path
from cinema_pool.services import api_key


def index(request):
    movies = getTrendingMovies()
    genres = getMovieGenres()
    return render(request, "exp.html", {
        'movies': movies,
        'image_path': images_base_path,
        'api_key': api_key,
        'genres': genres,
    })


def individual_post(request):
    return HttpResponse('Hi, this is where an individual post will be.')
