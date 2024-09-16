from cloudinary import CloudinaryImage
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    """
    The model representing the user's profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = CloudinaryField('profile_picture', default="images/profile_picture.jpg")
    location = models.CharField(max_length=255, blank=True)
    total_likes = models.IntegerField(default=0)
    total_favourites = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)