from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Movies

# Register your models here.


@admin.register(Movies)
class MovieList(SummernoteModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    search_fields = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}
