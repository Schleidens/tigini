from django.db import models

from django.contrib.auth.models import AbstractUser

from PIL import Image
import io
# Create your models here.


class User(AbstractUser):
    profile_photo = models.ImageField(blank=True)
    bio = models.TextField(max_length=200)
    
    