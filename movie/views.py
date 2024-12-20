from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import MovieCommentForm

from .models import Genre, Movie, MovieComment
from .utils import q_search


def movie_catalog(request, genre_slug=None):
    """
   Handles the movie catalog view, filtering movies by genre, search query, and
pagination.
    """

    # Get the current page number from the request
    page_number = int(request.GET.get("page", 1))

    # Get the search parameter from query
    query = request.GET.get("q", None)

    # Use get_list_or_404 to get the list of movies with status=1
    if genre_slug == "all":
        movies_list = get_list_or_404(Movie.objects.filter(status=1))
    elif query:
        movies_list = get_list_or_404(q_search(query))
    else:
        movies_list = get_list_or_404(
            Movie.objects.filter(genres__slug=genre_slug))

    # Set up pagination, with 24 items per page and 3 orphans
    paginator = Paginator(movies_list, 24, orphans=3)

    # Get the movies for the current page
    page_obj = paginator.get_page(page_number)
    genre_name = get_object_or_404(Genre.objects.filter(slug=genre_slug))
    genre_title = genre_name.name if genre_name else "Movie Catalog"

    context = {
        "page_obj": page_obj,
        "slug_url": genre_slug,
        "title": genre_title.capitalize(),
        }

    # Pass the movies and page object to the template
    return render(request, "movie/index.html", context)


def movie_detail(request, movie_slug):
    """
    Handles the display of movie details including comments.
    """

    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=movie_slug)
    comments = movie.movie_comments.all().order_by("-created_on")
    comment_count = movie.movie_comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = MovieCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.movie = movie
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Comment submitted and need approval"
                )

    comment_form = MovieCommentForm()

    context = {
        "movie": movie,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "title": movie.title,
        }

    return render(
        request,
        "movie/movie_detail.html",
        context=context,
        )


def comment_edit(request, slug, comment_id):
    """
    Handles the editing of an existing comment on a movie post.
    """
    if request.method == "POST":

        queryset = Movie.objects.filter(status=1)
        movie = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(MovieComment, pk=comment_id)
        comment_form = MovieCommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(
                request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("movies:movie_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Deletes a comment from a movie post if the request user is the author
    """
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(MovieComment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
            )

    return HttpResponseRedirect(reverse("movies:movie_detail", args=[slug]))


@login_required
def user_comments(request, slug, comment_id, action=None):
    comments = MovieComment.objects.filter(user=request.user)
    context = {
        "comments": comments,
        }
    return render(request, "movie/user_comments.html", context)
