from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from .forms import MovieCommentForm

from .models import Movie
from .utils import q_search


def movie_catalog(request, genre_slug=None):

    # Get the current page number from the request
    page_number = int(request.GET.get('page', 1))

    # Get the search parameter from query
    query = request.GET.get('q', None)

    # Use get_list_or_404 to get the list of movies with status=1
    if genre_slug == 'all':
        movies_list = get_list_or_404(Movie.objects.filter(status=1))
    elif query:
        movies_list = q_search(query)
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

    comments = movie.movie_comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = MovieCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = movie
            comment.save()
    else:
        comment_form = MovieCommentForm()

    context = {'movie': movie,
               "comments": comments,
               "comment_count": comment_count,
               "comment_form": comment_form,}

    messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
        )

    return render(
        request,
        "movie/poster.html",
        context=context,
        )
