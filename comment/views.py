from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse

from .forms import CommentForm
from .models import MovieComment, Movie

def comment(request, slug):

    movie = get_object_or_404(Movie, slug=slug)

    comments = MovieComment.objects.filter(movie=movie, approved=True).order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.movie = movie
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    context = {
        "movie": movie,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,}
    return render(request, "comment/comment.html", context)


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
        comment_form = CommentForm(data=request.POST, instance=comment)

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

    return HttpResponseRedirect(reverse('comment', args=[slug]))


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

    return HttpResponseRedirect(reverse('comment', args=[slug]))
