from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
from django.db.models import Q
from urllib3 import request

from .models import Movie


def q_search(query):
    if query.isdigit() and len(query) <= 4:
        return Movie.objects.filter(year=int(query))

    vector = SearchVector("title", "plot")
    query = SearchQuery(query)
    result = (
        Movie.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
        .distinct("rank")
    )

    return result
