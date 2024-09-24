from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    """
    Handles the HTTP GET request for the index page.

    Args:
        request: A HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse object that renders the "main/main.html" template.
    """
    return render(request, "main/main.html")

# Home page
@login_required
def home(request):
    """

    @login_required
    def home(request):
        """
    return render(request, "home.html")

# Dashboard
def dashboard(request):
    """
    Handles the user dashboard view.

    If the user is authenticated, retrieve the user's full name and render the 'dashboard.html' template with the full name passed as context.

    If the user is not authenticated, redirect to the login page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered 'dashboard.html' template with user's full name if authenticated.
        HttpResponseRedirect: Redirects to the login page if the user is not authenticated.
    """
    if request.user.is_authenticated:
        user = request.user
        full_name = user.get_full_name()
        return render(
            request,
            "dashboard.html",
            {"full_name": full_name},
            )
    else:
        return HttpResponseRedirect("/login/")

# Sigup
def user_signup(request):
    """

    Handles user signup process. If the user is authenticated, they are redirected to the dashboard.
    Otherwise, if the request method is POST and the form is valid, the user is registered and redirected
    to the login page with a success message. If the request method is not POST, an empty signup form is
    rendered.

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse object for the signup page or redirection response.

    """
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Congratulations!! You have become an Author."
                    )
                HttpResponseRedirect("/login/")
        else:
            form = SignUpForm()
        return render(request, "signup.html", {"form": form})
    else:
        return HttpResponseRedirect("/dashboard/")

# Login
def user_login(request):
    """
    Handles the user login functionality.

    If the user is not authenticated, processes the login form
    submitted via a POST request and attempts to authenticate
    the user using the provided credentials. If authentication
    is successful, the user is logged in and redirected to the
    dashboard. If the request method is GET, an empty login
    form is rendered.

    If the user is already authenticated, redirects to the
    dashboard page.

    Args:
        request: The HTTP request object.

    Returns:
        An HTTP response object. If the user is already
        authenticated or login is successful, redirects to the
        dashboard. Otherwise, renders the login page with the login form.
    """
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data["username"]
                upass = form.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully !!")
                    return HttpResponseRedirect("/dashboard/")
        else:
            form = LoginForm()
        return render(request, "login.html", {"form": form})
    else:
        return HttpResponseRedirect("/dashboard/")

# Logout
def user_logout(request):
    """
    Logs out the user and redirects to the login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: A redirect response to the login page.
    """
    logout(request)
    return HttpResponseRedirect("/login/")