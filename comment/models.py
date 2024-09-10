from django.db import models
from django.contrib.auth.models import User

from movie.models import Movies

# Create your models here.


class MovieComment(models.Model):
    """
    Stores a simple comment entry related to :model:`auth.User`
    and :model:`Movie`.
    """

    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
    )
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment_movie"
        verbose_name = "Movie comment"
        verbose_name_plural = "Movie comments"

    def __str__(self):
        return f"Comment {self.content} | written by {self.user}"
