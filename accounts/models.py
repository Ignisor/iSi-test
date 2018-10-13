from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager

from utils.types import ChoicesEnum


class UserTypes(ChoicesEnum):
    ADMIN = 'admin'
    DRIVER = 'driver'


class CustomUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('user_type', UserTypes.ADMIN.value)
        return super(CustomUserManager, self).create_superuser(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=16, choices=UserTypes.as_choices(), validators=[UserTypes.validator])
    jwt_token = models.CharField(max_length=256)

    objects = CustomUserManager()
