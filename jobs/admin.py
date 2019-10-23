from django.contrib import admin

# Register your models here.
from .models import JobType, Category, Post, ApplicationSource, Application

# Register the Admin classes for JobType using the decorator
# Reference: https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Admin_site
@admin.register(JobType) # admin.site.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(ApplicationSource)
class ApplicationSourceAdmin(admin.ModelAdmin):
    pass

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass