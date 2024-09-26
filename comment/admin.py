from django.contrib import admin

from .models import MovieComment


# Register your models here.

@admin.register(MovieComment)
class MovieCommentAdmin(admin.ModelAdmin):
    """

    MovieCommentAdmin defines the admin interface settings for the MovieComment model.

    Attributes:
        list_display (list): Specifies the fields to be displayed in the list view.
        list_filter (tuple): Defines the fields to filter the list view by.
        search_fields (list): Specifies the fields to include in the search functionality.
    """
    list_display = ['body', 'author', 'created_on']
    list_filter = ('created_on', 'author')
    search_fields = ['author', 'body', ]

