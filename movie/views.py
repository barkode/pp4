from django.shortcuts import render

from movie.models import Movies


# Create your views here.
def catalog(request):

    all_movies = Movies.objects.all()

    context = {
        "title": "Home Page",
        "content": "This is a page with movies",
        "movies": all_movies,
    }

    return render(request, "movie/content.html", context)


def movie(request):
    context = {"title": "Poster Page", "content": "This is a poster page"}

    return render(request, "movie/poster.html", context)
