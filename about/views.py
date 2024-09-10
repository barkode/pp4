from django.shortcuts import render


def about(request):
    context = {"title": "About", "movie": "Page about US"}

    return render(request, "about/about.html", context)
