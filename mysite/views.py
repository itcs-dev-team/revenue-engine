from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from datetime import datetime
# Create your views here.
def index(request):
    """The home page of mysite."""
    # now = datetime.now()
    # current_time = {'current_time': str(now)}
    # return render(request, 'mysite/index.html', current_time)
    return render(request, 'mysite/index.html')

# def home(request):
#     """A simple home page, with django-bootstrap4, for debug of static files."""
#     return render(request, 'mysite/home.html')
class HomeView(TemplateView): # https://docs.djangoproject.com/en/2.2/topics/class-based-views/intro/
    template_name = 'mysite/home.html'
        
# level 1 pages
def services(request):
    """The service page."""
    return render(request, 'mysite/services.html')

def case_studies(request):
    """The Case Studies page."""
    return render(request, 'mysite/case_studies.html')

# def news_and_events(request):
#     """The News and Events page."""
#     return render(request, 'mysite/news_and_events.html')

def career(request):
    """The Career page."""
    return render(request, 'mysite/career.html')

def about(request):
    """The About Us page."""
    return render(request, 'mysite/about.html')

def contact(request):
    """The Contact Us page."""
    return render(request, 'mysite/contact.html')

def privacy(request):
    """The privacy page."""
    return render(request, 'mysite/privacy.html')

def terms_and_conditions(request):
    """The Terms and Conditions page."""
    return render(request, 'mysite/terms_and_conditions.html')

# level 2 pages

# career section
def apply_now(request):
    """The apply_now page."""
    return render(request, 'mysite/apply_now.html')

# about section
def company_profile(request):
    """The company_profile page."""
    return render(request, 'mysite/company_profile.html')

def management_team(request):
    """The management_team page."""
    return render(request, 'mysite/management_team.html')

def investor_relations(request):
    """The investor_relations page."""
    return render(request, 'mysite/investor_relations.html')

def corprate_social_responsibility(request):
    """The corprate_social_responsibility page."""
    return render(request, 'mysite/corprate_social_responsibility.html')