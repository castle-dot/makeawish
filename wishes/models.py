from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import CustomUser
# Create your models here.


class Wish(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_granted = models.BooleanField(default=False, verbose_name="Granted")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='wishes')

    def __str__(self):
        return self.title