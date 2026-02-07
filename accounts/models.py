from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Optional: Paste a direct image URL (e.g. from Imgur or Google)"
    )

    def __str__(self):
        return self.username
    

