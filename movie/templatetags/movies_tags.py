from django import template
from django.shortcuts import get_list_or_404
from django.utils.http import urlencode

from movie.models import Genre, Movie

register = template.Library()


@register.simple_tag()
def movie_categories():
    return Genre.objects.all().order_by("name")


@register.simple_tag()
def movie_categories_random():
    return get_list_or_404(Movie.objects.filter(status=1).order_by("?"))


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)


@register.filter
def url_contains_genre(path, genres):
    return any(genre.get_absolute_url() in path for genre in genres)
