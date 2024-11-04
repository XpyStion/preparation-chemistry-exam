from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

ROLES = [
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
]


class AuthUser(AbstractUser):
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    gender = models.CharField(max_length=6, choices=GENDER, default='other')
    role = models.CharField(max_length=15, choices=ROLES, default='student')
    birth_date = models.DateField(default=None, null=True)
    country = models.CharField(max_length=15, default=None, null=True)
    phone = models.CharField(max_length=11, default=None, null=True)
    telegram = models.CharField(max_length=50, default=None, null=True)
