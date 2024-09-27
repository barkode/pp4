from django import forms

from movie.models import MovieComment


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('body',)
