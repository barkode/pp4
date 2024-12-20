from django.contrib import admin
from .models import About, CollaborateRequest

# Register your models here.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Django admin configuration for the CollaborateRequest model.
    """
    list_display = (
        "message",
        "read",
        )


admin.site.register(About)
