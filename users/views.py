from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from movie.models import MovieComment
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm


# Create your views here.


def login(request):
    """
    Handles the login functionality for users.
    """
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(
                    request, f"{username} you logged in Successfully !!")
                if request.POST.get("next", None):
                    return HttpResponseRedirect(request.POST.get["next"])

                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "StoreLinks - LogIn",
        "form": form,
        }

    return render(request, "users/login.html", context)


def registration(request):
    """
    Handles user registration by processing a POST request with user data.
    """
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(
                request, f"Account created for {user.username} !!")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegisterForm()

    context = {
        "title": "StoreLinks - Registration",
        "form": form,
        }
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    """
    Handles the profile view for updating user profile information.
    """
    comments = MovieComment.objects.filter(author_id=request.user)
    if request.method == "POST":
        form = UserProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
            )
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Profile updated for {request.user.username} !!")
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        "title": "StoreLinks - Profile",
        "form": form,
        "comments": comments,
        }
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    """
    Logs out the current authenticated user and redirects to the movie catalog.
    """
    messages.success(request, f"You have been logged out successfully !!")
    auth.logout(request)
    return HttpResponseRedirect(reverse("main:index"))


@login_required
def user_comments(request, slug, comment_id, action=None):
    pass
