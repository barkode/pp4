from django import forms

from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    CollaborateForm is a ModelForm for handling collaboration requests.

    Meta:
        - model: Associates this form with the CollaborateRequest model.
        - fields: Specifies which fields from CollaborateRequest model to include in the form ('name', 'email', 'message').
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')