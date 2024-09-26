from django.db import models
from django.contrib.auth.models import User

from app import settings
from movie.models import Movie

# Create your models here.

class MovieComment(models.Model):
    """
        A model representing a comment made on a movie.

        Attributes:
        movie: ForeignKey to the Movie model.
        author: ForeignKey to the user model defined in settings.AUTH_USER_MODEL.
        body: Text content of the comment.
        approved: Boolean indicating whether the comment has been approved.
        created_on: DateTime indicating when the comment was created.

        Meta:
        db_table: Name of the database table.
        verbose_name: Singular name for the model.
        verbose_name_plural: Plural name for the model.
        ordering: Default ordering for querying objects.

        Methods:
        __str__: Returns a string representation of the comment.
    """
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_author"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "movie_comment"
        verbose_name = "Movie comment"
        verbose_name_plural = "Movie comments"
        ordering = [
            "-created_on",
            "author",
            "approved",
        ]

    def __str__(self):
        return f"Comment {self.body} | written by {self.author}"
