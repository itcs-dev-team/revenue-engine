from django.contrib import admin

# Register your models here.
from .models import CaseStudy

# Register the Admin classes for JobType using the decorator
# Reference: https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Admin_site
@admin.register(CaseStudy) # admin.site.register(JobType)
class CaseStudyAdmin(admin.ModelAdmin):
    pass