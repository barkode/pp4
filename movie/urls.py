from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.movie_catalog, name="movie_catalog"),
    path("<slug:genre_slug>/", views.movie_catalog, name="movie_catalog"),
    path("movie/<slug:movie_slug>/", views.movie_detail, name="movie_detail"),
]
