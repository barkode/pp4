from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from .models import Movie, Genre, Actor, Production
from comment.models import MovieComment

# Register your models here.

# @admin.action(description="Mark selected as published")
# def make_published(modeladmin, request, queryset):
#     queryset.update(status=1)
@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    """
    Allows administrator to manage movies
    """
    # STATUS = ((0, "Draft"), (1, "Published"))

    list_display = ['title', "status"]
    search_fields = ['title', "status", "plot"]
    list_filter = ['status', 'updated_on']
    prepopulated_fields = {'slug': ('title',)}

    actions = ["make_published", "make_draft"]

    @admin.action(description="Mark selected as published")
    def make_published(self, request, queryset):
        updated = queryset.update(status=1)
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as published.",
                "%d stories were successfully marked as published.",
                updated,
                )
            % updated,
            messages.SUCCESS,
            )

    @admin.action(description="Mark selected as draft")
    def make_draft(self, request, queryset):
        updated = queryset.update(status=0)
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as draft.",
                "%d stories were successfully marked as draft.",
                updated,
                )
            % updated,
            messages.WARNING,
            )

@admin.register(Genre)
class MovieGenre(admin.ModelAdmin):
    pass

@admin.register(Actor)
class MovieActor(admin.ModelAdmin):
    pass

@admin.register(Production)
class MovieProduction(admin.ModelAdmin):
    pass