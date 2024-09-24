from django.contrib import admin
from .models import About, CollaborateRequest

# Register your models here.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Django admin configuration for the CollaborateRequest model.

    Registers the CollaborateRequest model with Django's admin interface
    and customizes the admin view to display specific fields.

    Attributes:
        list_display: Specifies the fields to be displayed in the list view
                      of the admin interface for the CollaborateRequest model.
    """
    list_display = (
        "message",
        "read",
    )

admin.site.register(About)