from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=20)

    @property
    def full_name(self):
        return self.get_full_name()
