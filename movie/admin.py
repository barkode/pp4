from django.contrib import admin

from .models import Movie, Genre
from comment.models import MovieComment

# Register your models here.



@admin.register(Genre)
class MovieGenre(admin.ModelAdmin):
    pass

@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    """
    Allows administrator to manage movies
    """
    list_display = ['title', "status"]
    search_fields = ['title', "status", "plot"]
    list_filter = ['status', 'updated_on']
    prepopulated_fields = {'slug': ('title',)}