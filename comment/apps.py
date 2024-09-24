from django.apps import AppConfig


class CommentConfig(AppConfig):
    """
        Django application configuration class for the 'comment' app.

        Attributes:
            default_auto_field (str): Specifies the default type for primary keys.
            name (str): Name of the application.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "comment"
