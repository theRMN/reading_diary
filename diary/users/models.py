from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER = 'user'
    MANAGER = 'manager'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (USER, 'User'),
        (MANAGER, 'Manager'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)


class UserSettings(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    expected_pages_per_day = models.PositiveIntegerField(default=0)
