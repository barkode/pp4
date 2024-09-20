from django import template

from movie.models import Genre

register = template.Library()

@register.simple_tag()
def movie_categories():
    return Genre.objects.all()