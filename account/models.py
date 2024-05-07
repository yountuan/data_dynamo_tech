from django.db import models
from django.contrib.auth.models import AbstractUser

#add image
class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', null=True, blank=True)