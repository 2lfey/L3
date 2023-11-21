from django.db import models

from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True)
    summary = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.username
