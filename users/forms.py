from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    )

from users.models import User


class UserLoginForm(AuthenticationForm):
    """
    This class represents a user login form used for authentication.
    """

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegisterForm(UserCreationForm):
    """
    User registration form class extending UserCreationForm.
    """

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            )

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserProfileForm(UserChangeForm):
    """
             A form for updating user profiles, inheriting from UserChangeForm.
             This form includes the fields for the user's profile image, first
             name, last name, email, and username.

    """

    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "email",
            "username",
            )

    image = forms.ImageField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()
    username = forms.CharField()
