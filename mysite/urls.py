from django.urls import path
from . import views

app_name = "mysite"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('services/', views.services, name='service'),
]