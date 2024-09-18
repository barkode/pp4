from django.urls import path

from . import views

app_name = "about"

urlpatterns = [
    path("", views.about, name="about"),
    path("contact/", views.contact, name="contact_us"),
]
