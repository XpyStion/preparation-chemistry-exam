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

    full_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=6, choices=GENDER, default='other')
    role = models.CharField(max_length=15, choices=ROLES, default='student')
    birth_date = models.DateField()
    country = models.CharField(max_length=15)
    phone = models.CharField(max_length=11,)
    telegram = models.CharField(max_length=50)
