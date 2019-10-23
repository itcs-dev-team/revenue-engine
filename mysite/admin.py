from django.contrib import admin

# Register your models here.
from .models import Status, Location

# Register the Admin classes for JobType using the decorator
# Reference: https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Admin_site
@admin.register(Status) # admin.site.register(JobType)
class StatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass