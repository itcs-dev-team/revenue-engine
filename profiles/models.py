from django.db import models
from django.contrib.auth.models import AbstractUser # 2019-10-22: https://wsvincent.com/django-custom-user-model-tutorial/status
from django.conf import settings # https://docs.djangoproject.com/en/2.2/topics/settings/

from mysite.models import Location, Status

User = settings.AUTH_USER_MODEL
# Create your models here.
class AccountType(models.Model):
    account_type = models.CharField(unique=True, max_length=50, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, default='1', on_delete=models.SET_DEFAULT)
    # STATUS = [
    #     ('01', 'active'),
    #     ('02', 'inactive'),
    #     ('03', 'deleted'),
    # ]
    # status = models.CharField(max_length=2, choices=STATUS, default='01')
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=2)
    
class CustomUser(AbstractUser):
    # user_id = models.IntegerField(primary_key=True)
    # password # defined in `django.contrib.auth.models.User` already
    # first_name # defined in `django.contrib.auth.models.User` already
    # last_name # defined in `django.contrib.auth.models.User` already
    
    # add additional fields in here
    account_type = models.ForeignKey('AccountType', default=1, on_delete=models.SET_NULL, null=True)
    jp_first_name = models.CharField(max_length=50, blank=True)
    jp_last_name = models.CharField(max_length=50, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=20, blank=True)
    reg_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField(null=True, blank=True)
    remark = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.username
