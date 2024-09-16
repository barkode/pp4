from django.contrib import admin

from .models import MovieComment

# Register your models here.

# @admin.register(MovieComment)
class MovieCommentAdmin(admin.ModelAdmin):
    """Allows admin to manage comments on insights via the admin panel"""
    list_display = ['author', 'content', 'created_on']
    list_filter = ('created_on', 'author')
    search_fields = ['author', 'content']

admin.site.register(MovieComment, MovieCommentAdmin)