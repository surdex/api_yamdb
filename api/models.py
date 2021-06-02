from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_ROLES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]
    username = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
    )
    confirmation_code = models.CharField(
        max_length=40,
        blank=True,
    )
    bio = models.TextField(
        blank=True,
    )
    role = models.CharField(
        max_length=10,
        choices=USER_ROLES,
        default='user'
    )
    password = models.CharField(
        max_length=128,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'password',
    ]

    def __str__(self):
        return self.email
