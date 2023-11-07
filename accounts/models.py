from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    phone_number = models.CharField(default=0, max_length=15)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    biography = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)

