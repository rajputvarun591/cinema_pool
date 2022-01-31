import requests as http

# We are using The Movie DatabaseTMDB for fetching and show movies on our web page
from cinema_pool.models import convert

base_path = "https://api.themoviedb.org/3"
images_base_path = "https://image.tmdb.org/t/p/w500"
# The Movie Database API key
api_key = "978eec01765e57ca76a06d2042e53b25"
# Path for trending movies for a week
trending_path = base_path + "/trending/movie/week"
# Ptah for get all available genres of the movies so that we can fetch movies by the genres.
genre_path = base_path + '/genre/movie/list'


def getTrendingMovies():
    response = http.get(trending_path, params={"api_key": api_key})
    print(response.url)
    print(response.text)
    data = response.json()
    movies = data["results"]
    converted = list()
    for item in movies:
        movie = convert(item)
        movie.save()
        converted.append(movie)
    return converted


def getMovieGenres():
    response = http.get(genre_path, params={"api_key": api_key})
    print(response.url)
    print(response.text)
    data = response.json()
    genres = data["genres"]
    return genres
