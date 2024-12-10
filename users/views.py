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

    If a POST request is received with user login details, it validates the form and authenticates the user.
    If authentication is successful, the user is logged in and redirected to the movie catalog page.
    Otherwise, an empty login form is provided for GET requests.

    Arguments:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponseRedirect if the user is successfully authenticated and logged in.
        Rendered HTML template with login form for GET requests or failed logins.
    """
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username} you logged in Successfully !!")
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get['next'])

                return HttpResponseRedirect(reverse('main:index'))
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
    Upon successful form validation and user account creation, logs the user in
    and redirects them to the movie catalog page. If the request is not a POST,
    initializes an empty registration form and displays it on the registration page.

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse object that renders the registration page with context,
        or redirects to the movie catalog upon successful registration.
    """
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"Account created for {user.username} !!")
            return HttpResponseRedirect(reverse('main:index'))
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

    Args:
        request (HttpRequest): The HTTP request object. It can be either GET or POST.

    POST:
        Processes the updated user profile form. If the form is valid, it saves the changes and shows a success message. Redirects to the profile page after successful update.

    GET:
        Displays the user profile form with the current user information prefilled.

    Context:
        title (str): The title of the web page.
        form (UserProfileForm): The form for updating the user profile.

    Returns:
        HttpResponse: Renders the `profile.html` template with the given context.
    """
    comments = MovieComment.objects.filter(author_id=request.user)
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Profile updated for {request.user.username} !!")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        "title": "StoreLinks - Profile",
        "form": form,
        "comments":comments,
        }
    return render(request, "users/profile.html", context)

@login_required
def logout(request):
    """
    Logs out the current authenticated user and redirects to the movie catalog.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponseRedirect: A redirect to the movie catalog page.
    """
    messages.success(
        request,
        f"You have been logged out successfully !!")
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

@login_required
def user_comments(request, slug, comment_id, action=None):
    pass