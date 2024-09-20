from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic

from .models import Movie


def movie_catalog(request):
    # Use get_list_or_404 to get the list of movies with status=1
    movies_list = get_list_or_404(Movie.objects.filter(status=1).order_by('?'))

    # Set up pagination, with 24 items per page and 3 orphans
    paginator = Paginator(movies_list, 24, orphans=3)

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the movies for the current page
    page_obj = paginator.get_page(page_number)

    # Pass the movies and page object to the template
    return render(request, 'movie/index.html', {'movies_list': page_obj})

def movie_detail(request, movie_slug):


    movie = get_object_or_404(Movie, slug=movie_slug)

    context = {'movie': movie}

    return render(
        request,
        "movie/poster.html",
        context=context,
        )
