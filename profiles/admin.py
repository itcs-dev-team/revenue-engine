from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm # https://wsvincent.com/django-custom-user-model-tutorial/

# Register your models here.
from .models import CustomUser, AccountType

# Register the Admin classes for JobType using the decorator
# Reference: https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Admin_site
@admin.register(CustomUser) #admin.site.register(CustomUser, CustomUserAdmin)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = ['email', 'username', 'first_name', 'last_name','created_at', 'last_login']
    # fields = ['email', 'username','first_name', 'last_name', ('created_at', 'last_login')] # DEBUG: fieldsets in profile's admin.

@admin.register(AccountType) # admin.site.register(JobType)
class AccountTypeAdmin(admin.ModelAdmin):
    pass

