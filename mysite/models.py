from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings # https://docs.djangoproject.com/en/2.2/topics/settings/
from django.utils import timezone

User = settings.AUTH_USER_MODEL
# Create your models here.

## Ref: https://docs.djangoproject.com/zh-hans/2.2/topics/db/queries/
# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     def __str__(self):
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()

#     def __str__(self):
#         return self.headline

class Status(models.Model):
    # STATUS = [
    #     ('1', 'active'),
    #     ('2', 'inactive'),
    #     ('3', 'deleted'),
    # ]
    # Status = models.IntegerField(choices=STATUS, default=2) # DEBUG: False design.
    status          = models.CharField(max_length=11, default=2) # 2019-10-24: correct design.
    
    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name_plural = 'status'
        ordering = ['status']

class Location(models.Model):
    location        = models.CharField(max_length=255, blank=True)
    company_name    = models.CharField(max_length=255, blank=True)
    jp_company_name = models.CharField(max_length=255, blank=True)
    address         = models.CharField(max_length=255, blank=True)
    jp_address      = models.CharField(max_length=255, blank=True)
    telephone       = models.CharField(max_length=30, blank=True)
    fax             = models.CharField(max_length=30, blank=True)
    email           = models.EmailField(max_length=254, blank=True)
    picture         = models.ImageField(max_length=100, blank=True)
    ea_licence      = models.CharField(max_length=255, null=True, blank=True)
    labor_dept_url  = models.URLField(max_length=200, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='users')
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default='1', on_delete=models.SET_DEFAULT)
    status          = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=2)
    
    def __str__(self):
        return self.location