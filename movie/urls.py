from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.movie_catalog, name="movie_catalog"),
    path("search/", views.movie_catalog, name="movie_search"),
    path("<slug:genre_slug>/", views.movie_catalog, name="movie_genre"),
    path("movie/<slug:movie_slug>/", views.movie_detail, name="movie_detail"),
]
