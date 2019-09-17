from django.urls import path
from . import views

app_name = "mysite"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('services/', views.services, name='service'),
    path('case-studies/', views.case_studies, name='case_studies'),
    path('news-and-events/', views.news_and_events, name='news_and_events'),
    path('career/', views.career, name='career'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('privacy/', views.privacy, name='privacy'),
    
]
"""
URLs:
/
services
    it-consulting-and-project-management
    managed-services
    it-recruitment
    it-support
    windows-10-migration
    application-development-and-off-shoring-advisory
    it-regulatory-advisory-services
    secure-data-destruction-and-hardware-disposal
    itcs-group-unified-communication-solutions
case-studies
news-and-events
    news-and-event-details
career
    job-details
    apply-now
    send-cv
about-us
    company-profile
    management-team
    investor-relations
    corprate-social-responsibility
contact-us
privacy-policy
terms-and-conditions
"""