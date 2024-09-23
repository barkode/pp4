from django import template
from django.utils.http import urlencode

from movie.models import Genre

register = template.Library()

@register.simple_tag()
def movie_categories():
    return Genre.objects.all().order_by('name')

@register.simple_tag()
def movie_categories_random():
    return Genre.objects.all().order_by('?')

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)