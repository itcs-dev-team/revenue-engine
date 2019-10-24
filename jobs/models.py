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
class JobType(models.Model):
    job_type        = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)
    # created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='users')
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    status          = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=2)

    def __str__(self):
        return self.job_type

class Category(models.Model):
    job_category    = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    status          = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=2)

    def __str__(self):
        return self.job_category
    
class Post(models.Model):
    job_id          = models.CharField(max_length=200)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    created_at      = models.DateTimeField(auto_now_add=True)
    # update_at  =
    # update_by  =
    location        = models.ForeignKey(Location, on_delete=models.SET_DEFAULT, default=1)
    job_type        = models.ForeignKey(JobType, on_delete=models.CASCADE)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    title           = models.CharField(max_length=200)
    description     = models.TextField(max_length=1000)
    job_id          = models.CharField(max_length=200)
    # responsibilities =    # TODO: unknown relationship since no model Services
    # equirements =         # TODO: relationship since no model Services
    featured_job    = models.CharField(max_length=200)
    status          = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=2)

    def __str__(self):
        return self.title
    
class ApplicationSource(models.Model):
    source          = models.CharField(max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    status          = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=2)

    def __str__(self):
        return self.source
    
class Application(models.Model):
    source          = models.ForeignKey(ApplicationSource, on_delete=models.SET_DEFAULT, default=1)
    location        = models.ForeignKey(Location, on_delete=models.SET_DEFAULT, default=1)
    created_at      = models.DateTimeField(auto_now_add=True)
    job_id          = models.CharField(max_length=200)

    def __str__(self):
        return self.id