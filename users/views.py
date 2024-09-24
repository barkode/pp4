from django.shortcuts import render
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.forms import UserLoginForm


# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username= request.POST['username']
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

def registration(requests):
    context = {
        "title": "StoreLinks - Registration",
        }
    return render(requests, "users/registration.html", context)

def profile(requests):
    context = {
        "title": "StoreLinks - Profile",
        }
    return render(requests, "users/profile.html", context)

def logout(requests):
  pass