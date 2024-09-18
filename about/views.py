from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about(request):
    """
    Renders the About page
    """
    about_field = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    return render(
        request,
        "about/about.html",
        {
            "about": about_field,
            "collaborate_form": collaborate_form
            },
        )

def contact(request):
    """
    Renders the Contact page
    """
    collaborate_form = CollaborateForm()
    return render(
        request,
        "about/contact.html",
        {
            "collaborate_form": collaborate_form
            },
        )