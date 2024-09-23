from django.db.models import Q

from .models import Movie


def q_search(query):
    if query.isdigit() and len(query) <= 4:
        return Movie.objects.filter(year=int(query))

    keywords = [ word for word in query.split() if len(word) > 3 ]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(title__icontains=token)
        q_objects |= Q(plot__icontains=token)
        q_objects |= Q(actors__name__icontains=token)
        q_objects |= Q(genres__name__icontains=token)

    return Movie.objects.filter(q_objects).distinct()