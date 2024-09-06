from django.shortcuts import render


def about(request):
    context = {"title": "About", "content": "Page about US"}

    return render(request, "about/about.html", context)
