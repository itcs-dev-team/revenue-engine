from django.db import models
from django.conf import settings # https://docs.djangoproject.com/en/2.2/topics/settings/

from mysite.models import Location, Status

User = settings.AUTH_USER_MODEL
# Create your models here.
# class Question(models.Model):
#     question_text   = models.CharField(max_length=200)
#     pub_date        = models.DateTimeField('date published')


# class Choice(models.Model):
#     question        = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text     = models.CharField(max_length=200)
#     votes           = models.IntegerField(default=0)

# ----
class CaseStudy(models.Model):
    title           = models.CharField(max_length=255)
    client_overview = models.CharField(max_length=255)
    details         = models.TextField(max_length=255)
    picture         = models.ImageField(max_length=100, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    # created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='case_study_users')
    updated_at      = models.DateTimeField(auto_now=True)
    updated_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    status          = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=2)