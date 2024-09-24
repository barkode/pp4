from comment.models import MovieComment
from django import forms


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('body',)