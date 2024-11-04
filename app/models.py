from django.contrib.auth.models import AbstractUser
from django.db import models

from app.base.util import wrap_db_choice, StringEnum


class Genders(StringEnum):
    MALE: str = 'male'
    FEMALE: str = 'female'
    OTHER: str = 'other'


class Roles(StringEnum):
    ADMIN: str = 'admin'
    TEACHER: str = 'teacher'
    STUDENT: str = 'student'


class AuthUser(AbstractUser):
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    gender = models.CharField(max_length=6, choices=wrap_db_choice(tuple(Genders)), default='other')
    role = models.CharField(max_length=15, choices=wrap_db_choice(tuple(Roles)), default='student')
    birth_date = models.DateField(default=None, null=True)
    country = models.CharField(max_length=15, default=None, null=True)
    phone = models.CharField(max_length=11, default=None, null=True)
    telegram = models.CharField(max_length=50, default=None, null=True)
