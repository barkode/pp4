from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Movie


class MovieCatalog(generic.ListView):
    queryset = Movie.objects.filter(status=1).order_by('?')
    template_name = "movie/index.html"
    context_object_name = "movies_list"
    paginate_by = 24
    paginate_orphans = 3

def movie_catalog(request, category_slug):
    pass

def movie_detail(request, slug):
    """
    Display an individual :model:`movie.Poster`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(Movie, slug=slug)

    return render(
        request,
        "movie/poster.html",
        context={"movie": movie},
        )
