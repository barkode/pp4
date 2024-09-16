from django.contrib import admin

from .models import Movies
from comment.models import MovieComment

# Register your models here.

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    """
    Allows administrator to manage movies
    """
    list_display = ['title', "created_on", "status"]
    search_fields = ['title', "status", "created_on"]
    list_filter = ['status', 'created_on']