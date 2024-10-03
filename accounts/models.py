# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass  # Qo'shimcha maydonlar kerak bo'lsa, bu yerda qo'shish mumkin
