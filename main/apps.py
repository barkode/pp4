from django.apps import AppConfig


class MainConfig(AppConfig):
    """
    Class MainConfig

    Configures the Django application named 'main'.

    Attributes:
        default_auto_field: A string representing the default type of primary key to use for models that don’t specify one.
        name: The name of the Django application.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
