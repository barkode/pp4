from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path("", views.catalog, name="index"),
    path("movies/movie/", views.movie, name="item"),
]
