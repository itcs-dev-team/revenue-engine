from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView

from .models import Post, Application
# Create your views here.
# def career(request):
#     """The Career home page."""
#     return render(request, 'jobs/career.html')
#
# def apply_now(request):
#     """The apply_now page."""
#     return render(request, 'jobs/apply_now.html')

## CBV
class JobListView(ListView):
    """Show a list of jobs.
    
    The Career home page.
    """
    model = Post
    template_name = "jobs/career_.html"
    context_object_name = 'posts'

# level 2 pages
class JobDetailView(DetailView):
    """A job with its detail. Take an id and give a job."""
    model = Post
    template_name = "jobs/jobs_details_.html"
    context_object_name = 'post'

class JobApplyView(CreateView):
    """Submit to apply for a job."""
    model = Application
    template_name = "jobs/apply_.html"
    fields = ["first_name", "last_name", "email", "telephone", "location", "availability"]
