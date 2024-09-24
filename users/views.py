from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.

def login(requests):
    context = {
        "title": "StoreLinks - LogIn",
        }
    return render(requests, "users/login.html", context)

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