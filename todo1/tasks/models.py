from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class Task(models.Model):
    title = models.TextField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, null=False)

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    img = models.ImageField(upload_to='photo', blank=True, null=True)


class Title(models.Model):
    title = models.TextField(blank=True, null=True)
