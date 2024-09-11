from django.db import models
from django.contrib.auth.models import User

# from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Movies(models.Model):
    """
    title, year,rated,released,runtime,genre,director,writer,actors,plot,language,country,awards,poster,ratings,metascore,imdbraiting,imdbvotes,imdbid,type,dvd,boxoffice,production, website, response
    """

    title = models.CharField(max_length=200, unique=True, verbose_name="Movie Title")
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        blank=True,
        verbose_name="URL",
    )
    plot = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        db_table = "movie"
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"
