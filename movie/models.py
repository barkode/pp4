from django.db import models

# from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Movies(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Movie Title")
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        blank=True,
        verbose_name="URL",
    )
    release_date = models.DateField()
    # poster = CloudinaryField("image")
    sypnosis = models.TextField(max_length=400)
    trailer = models.URLField(max_length=100)
    info_link = models.URLField(max_length=100)
    color_class = models.CharField(max_length=20, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # first_icon = CloudinaryField("icon", default="placeholder")
    # second_icon = CloudinaryField("icon", default="placeholder")
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "movie"
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} - {self.release_date} - {self.status}"
