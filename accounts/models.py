from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    You can add additional fields here if needed.
    """
    # Example of adding a custom field
    age = models.PositiveBigIntegerField(
        null=True,
        blank=True # Optional field for user age 
    )