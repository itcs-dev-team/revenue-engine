from django.db import models
from django.contrib.auth.models import AbstractUser # 2019-10-22: https://wsvincent.com/django-custom-user-model-tutorial/status

# Create your models here.
class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.email