from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path("", views.Catalog.as_view(), name="movies_catalog"),
    path("movies/movie/", views.movie, name="movie"),
]
