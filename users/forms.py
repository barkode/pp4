from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    """
    This class represents a user login form used for authentication.

    Attributes:
        username: A character field for the username input.
        password: A character field for the password input.

    Meta:
        model: The User model which is associated with this form.
        fields: Specifies the fields included in the form, which are 'username' and 'password'.

    Classes:
        Meta: An inner class to specify the meta-data for the UserLoginForm.
    """
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    """
    User registration form class extending UserCreationForm.

    class UserRegisterForm(UserCreationForm):

    Meta class configuration to define model and fields for the form.

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    Form field for first name.
    first_name = forms.CharField()

    Form field for last name.
    last_name = forms.CharField()

    Form field for username.
    username = forms.CharField()

    Form field for email.
    email = forms.EmailField()

    Form field for password.
    password1 = forms.CharField()

    Form field for password confirmation.
    password2 = forms.CharField()
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserProfileForm(UserChangeForm):
    """

         class UserProfileForm(UserChangeForm):

             A form for updating user profiles, inheriting from UserChangeForm.
             This form includes the fields for the user's profile image, first name, last name, email, and username.

             class Meta:
                 model = User
                 fields = ('image', 'first_name', 'last_name', 'email', 'username')

    image = forms.ImageField(required=False)
        An optional field for the user's profile image.

    first_name = forms.CharField()
        A required field for the user's first name.

    last_name = forms.CharField()
        A required field for the user's last name.

    email = forms.EmailField()
        A required field for the user's email address.

    username = forms.CharField()
        A required field for the user's username.
    """
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'email', 'username' )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()


