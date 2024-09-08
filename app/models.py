from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50)


class AuthUser(AbstractUser):
    roles = models.ManyToManyField(Role, related_name='users')

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
