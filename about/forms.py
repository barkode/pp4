from django import forms

from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    CollaborateForm is a ModelForm for handling collaboration requests.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'phone', 'subject', 'message')
