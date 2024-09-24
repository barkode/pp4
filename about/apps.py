from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    An application configuration class used to configure the 'about' app.

    Attributes:
        default_auto_field (str): Specifies the type of auto-created primary key field to use for models in the app.
        name (str): The name of the app this configuration applies to.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "about"
