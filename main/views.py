from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from movie.models import Movie


def index(request):

    movies_list = get_list_or_404(Movie.objects.filter(status=1).order_by('?'))

    paginator = Paginator(movies_list, 24, orphans=3)
    page_obj = paginator.get_page(1)

    context = {"title": "StoreLinks - Home page", "page_obj": page_obj}

    return render(request, "main/main.html", context)