from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # Add any additional fields you want for your custom user model
    age = models.PositiveIntegerField(null=True, blank=True)
