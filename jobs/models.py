from django.db import models
from django.conf import settings # https://docs.djangoproject.com/en/2.2/topics/settings/
from django.urls import reverse

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
    # featured_job    = models.CharField(max_length=200)
    is_featured_job    = models.BooleanField(default=False)
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
    LOCATION_CHOICES = [ # This location is not the location defined in mysite.Location
        ('HK', 'Hong Kong'),
        ('SG', 'Singapore'),
        ('JP', 'Japan'),
        ('AU', 'Australia'),
        ('IN', 'India'),
        ('CN', 'China'),
        ('OT', 'Others'),
    ]
    
    AVAILABILITY_CHOICES = [
        ('IM', 'Immediately'),
        ('2W', '2 Weeks'),
        ('1M', '1 Month'),
        ('2M', '2 Months'),
    ]
    source          = models.ForeignKey(ApplicationSource, on_delete=models.SET_DEFAULT, default=1)
    # location        = models.ForeignKey(Location, on_delete=models.SET_DEFAULT, default=1)
    location        = models.CharField(max_length=2, choices=LOCATION_CHOICES, default='HK') # This 'location' is not the location defined in mysite.Location.
    created_at      = models.DateTimeField(auto_now_add=True)
    job_id          = models.CharField(max_length=200)
    first_name      = models.CharField(max_length=200)
    last_name       = models.CharField(max_length=200)
    email           = models.EmailField(max_length=254)
    telephone       = models.CharField(max_length=30)
    availability    = models.CharField(max_length=2, choices=AVAILABILITY_CHOICES, default='IM')

    def __str__(self):
        return self.id
    
    def get_absolute_url(self): # Google:django CreateView example -> https://www.agiliq.com/blog/2019/01/django-createview/
        # return reverse('jobs:job_detail', args=[str(self.job_id)])
        return reverse('jobs:career')