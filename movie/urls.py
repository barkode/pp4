from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path("", views.content, name="index"),
    path("movie/poster/", views.poster, name="poster"),
]
