from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    )
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

# Default user creation form
class SignUpForm(UserCreationForm):
    """
        SignUpForm class extending UserCreationForm for user registration.

        Fields:
            password1: Password field with 'Password' label, using PasswordInput widget with form-control class.
            password2: Password confirmation field with 'Confirm Password (again)' label, using PasswordInput widget with form-control class.

        Meta:
            model: Specifies the User model.
            fields: List of fields to be included in the form - username, first_name, last_name, email.
            labels: Custom labels for first_name, last_name, and email fields.
            widgets: Custom widgets for username, first_name, last_name, and email fields to include form-control class.
    """
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
        )
    password2 = forms.CharField(
        label="Confirm Password (again)",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        )
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            }

# Default authentication form
class LoginForm(AuthenticationForm):
    """
    LoginForm class extends the AuthenticationForm to provide custom styling and widget attributes for the username and password fields.

    Attributes:
        username: A UsernameField instance using a TextInput widget with autofocus and CSS class "form-control".
        password: A CharField instance for the password, with a PasswordInput widget that has the attributes for autocomplete set to "current-password" and CSS class "form-control".
    """
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
        )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control"}
            ),
        )