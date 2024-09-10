from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"title": "Home - Main", "movie": " HOME - Furniture and carpets store"}

    return render(
        request,
        "main/index.html",
        context,
    )
