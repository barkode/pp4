from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import MovieCommentForm

from .models import Movie, MovieComment
from .utils import q_search


def movie_catalog(request, genre_slug=None):
    """
    Handles the movie catalog view, filtering movies by genre, search query, and pagination.

    Parameters:
      request: The HTTP request object.
      genre_slug: The slug of the genre to filter movies by, defaults to None.

    Returns:
      HttpResponse: Renders the movie catalog page with filtered and paginated movies.

    Functionality:
      1. Retrieves the current page number from the query parameters.
      2. Retrieves the search query parameter from the query parameters.
      3. Filters the movies based on the provided genre slug or search query.
         - If genre_slug is 'all', retrieves all movies with status=1.
         - If a search query is provided, retrieves movies matching the search query.
         - Otherwise, retrieves movies that belong to the specified genre.
      4. Sets up pagination with 24 movies per page and 3 orphans.
      5. Gets the movies for the current page.
      6. Passes the filtered and paginated movies along with the genre slug to the template.
      7. Renders the 'movie/index.html' template with the context containing the movies and pagination details.
    """

    # Get the current page number from the request
    page_number = int(request.GET.get('page', 1))

    # Get the search parameter from query
    query = request.GET.get('q', None)

    # Use get_list_or_404 to get the list of movies with status=1
    if genre_slug == 'all':
        movies_list = get_list_or_404(Movie.objects.filter(status=1))
    elif query:
        movies_list = get_list_or_404(q_search(query))
    else:
        movies_list = get_list_or_404(Movie.objects.filter(genres__slug=genre_slug))

    # movies_list = get_list_or_404(Movie.objects.filter(status=1).order_by('?'))

    # Set up pagination, with 24 items per page and 3 orphans
    paginator = Paginator(movies_list, 24, orphans=3)

    # Get the movies for the current page
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'slug_url': genre_slug}

    # Pass the movies and page object to the template
    return render(request, 'movie/index.html', context)

def movie_detail(request, movie_slug):
    """
    Handles the display of movie details including comments.

    Args:
        request: The HTTP request object.
        movie_slug: The slug for the movie.

    Functionality:
        - Retrieves the movie object by its slug or returns a 404 error if not found.
        - Fetches all approved comments related to the movie sorted by creation date in descending order.
        - Counts the number of approved comments.
        - If a POST request is made, the function attempts to create a new comment using the MovieCommentForm.
        - Sets the author of the comment as the current authenticated user and associates the comment with the movie.
        - Upon successful form submission, adds a success message indicating that the comment is submitted and awaiting approval.
        - Initializes a new MovieCommentForm in case of a GET request or if the form is invalid.
        - Prepares the context for rendering the movie detail page with movie details, comments, comment count, and the comment form.
        - Renders the 'movie/movie_detail.html' template with the context.
    """

    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=movie_slug)
    comments = movie.movie_comments.all().order_by('-created_on')
    comment_count = movie.movie_comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = MovieCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.movie = movie
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval')

    comment_form = MovieCommentForm()

    context = {'movie': movie,
               "comments": comments,
               "comment_count": comment_count,
               "comment_form": comment_form,}


    return render(
        request,
        "movie/movie_detail.html",
        context=context,
        )

def comment_edit(request, slug, comment_id):
    """
    Handles the editing of an existing comment on a movie post.

    Args:
        request: The HTTP request object containing metadata about the request.
        slug: The unique slug identifying the movie post.
        comment_id: The unique identifier of the comment to be edited.

    When a POST request is made, this function retrieves the movie post and the comment
    to be edited. It then binds the form data to a CommentForm instance.
    If the form is valid and the current user is the author of the comment, the comment
    is updated and saved but marked as not approved until further moderation.
    Appropriate success or error messages are then added to the request context.
    Finally, the function redirects to the post detail page.
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
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
                )

    return HttpResponseRedirect(reverse('movies:movie_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    Deletes a comment from a movie post if the request user is the author of the comment.

    Args:
        request: The HTTP request object.
        slug: The slug of the movie post.
        comment_id: The ID of the comment to be deleted.

    Queryset:
        Filters movie posts with a status of 1.

    Raises:
        Http404: If the movie post or comment does not exist.

    Deletes:
        The comment if the request user is the author, else adds an error message.

    Messages:
        If successful, adds a success message.
        If unsuccessful, adds an error message.

    Redirects:
        To the movie post detail page.
    """
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(MovieComment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
            )

    return HttpResponseRedirect(reverse('movies:movie_detail', args=[slug]))

@login_required
def user_comments(request, slug, comment_id, action=None):
    comments = MovieComment.objects.filter(user=request.user)
    context = {
        'comments': comments,
        }
    return render(request, 'movie/user_comments.html', context)
