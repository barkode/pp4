from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.MovieCatalog.as_view(), name="movie_catalog"),
    path("<slug:slug>/", views.movie_detail, name="movie_detail"),
]
