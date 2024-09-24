from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm


# Create your views here.

def login(request):
    """
    Handles user login functionality.

    The function processes POST requests containing user credentials, validates them,
    authenticates the user, and upon successful authentication, logs in the user and
    redirects to a specified URL.

    Parameters:
        request: The HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse: Redirects to the 'movie_catalog' page upon successful login.
        render: Renders the login page with the login form for GET requests or invalid POST requests.
    """
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('movies:movie_catalog'))
    else:
        form = UserLoginForm()

    context = {
        "title": "StoreLinks - LogIn",
        "form": form,
        }

    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('movies:movie_catalog'))
    else:
        form = UserRegisterForm()

    context = {
        "title": "StoreLinks - Registration",
        "form": form,
        }
    return render(request, "users/registration.html", context)


def profile(request):
    context = {
        "title": "StoreLinks - Profile",
        }
    return render(request, "users/profile.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('movies:movie_catalog'))
