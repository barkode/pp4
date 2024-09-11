from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Movies

# Register your models here.

admin.site.register(Movies)
