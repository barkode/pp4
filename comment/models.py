from datetime import timezone

from django.db import models
from django.contrib.auth.models import User

from movie.models import Movies

# Create your models here.


class MovieComment(models.Model):
    """
    Stores a simple comment entry related to :model:`auth.User`
    and :model:`Movie`.
    """

    movie = models.ForeignKey(
        Movies, on_delete=models.CASCADE, related_name="movie_comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_author"
    )
    content = models.TextField()
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
        return f"Comment {self.content} | written by {self.author}"
