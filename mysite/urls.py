from django.urls import path
from . import views
app_name = 'mysite'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # services
    path('case_studies', views.case_studies, name='case_studies'),
]