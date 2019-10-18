from django.urls import path
from . import views

app_name = "mysite"

urlpatterns = [
    # TODO: services, news, career will be moved to a django app.
    path('home/', views.home, name='home'), # TODO: remove this path when production
    # level 1 pages
    path('', views.index, name='index'),
    path('services/', views.services, name='service'),
    path('case-studies/', views.case_studies, name='case_studies'),
    path('news-and-events/', views.news_and_events, name='news_and_events'),
    path('career/', views.career, name='career'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    
    # level 2 pages
    path('career/apply-now/', views.apply_now, name='apply_now'),
    path('about/company-profile/', views.company_profile, name='company_profile'),
    path('about/management-team/', views.management_team, name='management_team'),
    path('about/investor-relations/', views.investor_relations, name='investor_relations'),
    path('about/corprate-social-responsibility/', views.corprate_social_responsibility, name='corprate_social_responsibility'),
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
about
    company-profile
    management-team
    investor-relations
    corprate-social-responsibility
contact
privacy-policy
terms-and-conditions
"""