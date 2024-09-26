from .models import MovieComment
from django import forms


class CommentForm(forms.ModelForm):
    """

    CommentForm is a Django ModelForm intended for creating or updating MovieComment instances.

    class Meta:
        Meta class to specify the model and fields to be used in the form.

    model: Specifies the model associated with the form, in this case, MovieComment.

    fields: Specifies the fields to be included in the form, in this case the 'body' field of the MovieComment model.
    """
    class Meta:
        model = MovieComment
        fields = ('body',)