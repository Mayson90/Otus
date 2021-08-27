from django.contrib.auth.models import AbstractUser
from django.db import models

from main.models import Order


class NewUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=22)
    user_order = models.ManyToManyField(Order)
