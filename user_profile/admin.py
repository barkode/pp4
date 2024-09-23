from django.contrib import admin
from .models import Profile, Favorite, Comment

admin.site.register(Profile)
admin.site.register(Favorite)
admin.site.register(Comment)