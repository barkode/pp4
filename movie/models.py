from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
from django.utils.text import slugify

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10, blank=True, null=True)
    rated = models.CharField(max_length=10, blank=True, null=True)
    released = models.CharField(max_length=50, blank=True, null=True)
    runtime = models.CharField(max_length=20, blank=True, null=True)
    genres = models.ManyToManyField('Genre', related_name='movies', blank=True)  # ManyToMany for Genres
    director = models.CharField(max_length=255, blank=True, null=True)
    writer = models.CharField(max_length=255, blank=True, null=True)
    actors = models.ManyToManyField('Actor', related_name='movies', blank=True)  # ManyToMany for actors
    plot = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    poster = models.URLField(blank=True, null=True)
    metascore = models.CharField(max_length=10, blank=True, null=True)
    imdb_rating = models.CharField(max_length=10, blank=True, null=True)
    imdb_votes = models.CharField(max_length=20, blank=True, null=True)
    imdb_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    dvd = models.CharField(max_length=50, blank=True, null=True)
    box_office = models.CharField(max_length=50, blank=True, null=True)
    production = models.ForeignKey('Production', related_name='movies', on_delete=models.SET_NULL, null=True, blank=True)  # ForeignKey для студии
    website = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name="URL")
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'movie'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ('id',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.slug_to_title(self.slug):
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def slug_to_title(self, slug):
        # Returns the original title из slug
        return slug.replace('-', ' ').title()  # Example, "the-shawshank-redemption" -> "The Shawshank Redemption"

    def generate_unique_slug(self):
        original_slug = slugify(self.title)
        unique_slug = original_slug
        counter = 1

        # Check whether such a slug already exists in the database
        while Movie.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{original_slug}-{counter}"  # Если есть, добавляем счетчик
            counter += 1

        return unique_slug


class Rating(models.Model):
    movie = models.ForeignKey('Movie', related_name='ratings', on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    value = models.CharField(max_length=20)

    class Meta:
        db_table = 'rating'

    def __str__(self):
        return f"{self.source}: {self.value}"


class Actor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=270, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'actor'

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a slug from the name
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name



class Genre(models.Model):
    name = models.CharField(max_length=100, default='without_genre')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'genre'

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a slug from the name
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Production(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=270, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'production'

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a slug from the name
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

