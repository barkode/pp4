from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Movies

# Register your models here.


@admin.register(Movies)
class MovieList(SummernoteModelAdmin):
    list_display = ("title", "slug", "status")
    search_fields = ["title", "slug"]
    summernote_fields = ("status",)
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}
