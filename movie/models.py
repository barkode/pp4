from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    release_date = models.DateField()
    poster = CloudinaryField("image")
    sypnosis = models.TextField(max_length=400)
    trailer = models.URLField(max_length=100)
    info_link = models.URLField(max_length=100)
    color_class = models.CharField(max_length=20, blank=True)
    # first_icon = CloudinaryField("icon", default="placeholder")
    # second_icon = CloudinaryField("icon", default="placeholder")

    class Meta:
        db_table = "movie"
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.title} - {self.release_date}"
