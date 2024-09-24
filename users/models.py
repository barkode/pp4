
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="profile_images", null=True, blank=True, verbose_name="Avatar")
    
    class Meta:
        db_table="user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username