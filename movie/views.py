from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from unicodedata import category

from .models import Movie


def movie_catalog(request, genre_slug):

    # Get the current page number from the request
    page_number = int(request.GET.get('page', 1))

    # Use get_list_or_404 to get the list of movies with status=1
    if genre_slug == 'all':
        movies_list = get_list_or_404(Movie.objects.filter(status=1))
    else:
        movies_list = get_list_or_404(Movie.objects.filter(genres__slug=genre_slug))

    # movies_list = get_list_or_404(Movie.objects.filter(status=1).order_by('?'))

    # Set up pagination, with 24 items per page and 3 orphans
    paginator = Paginator(movies_list, 24, orphans=3)


    # Get the movies for the current page
    page_obj = paginator.get_page(page_number)

    # Pass the movies and page object to the template
    return render(request, 'movie/index.html', {'page_obj': page_obj, 'slug_url': genre_slug})

def movie_detail(request, movie_slug):


    movie = get_object_or_404(Movie, slug=movie_slug)

    context = {'movie': movie}

    return render(
        request,
        "movie/poster.html",
        context=context,
        )
