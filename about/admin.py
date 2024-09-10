from django.contrib import admin
from .models import About, CollaborateRequest

# Register your models here.


@admin.register(About)
class AboutSite(admin.ModelAdmin):
    pass


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = (
        "message",
        "read",
    )
