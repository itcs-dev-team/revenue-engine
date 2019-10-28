from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post
# Create your views here.
# def career(request):
#     """The Career home page."""
#     return render(request, 'jobs/career.html')

# level 2 pages
def apply_now(request):
    """The apply_now page."""
    return render(request, 'jobs/apply_now.html')

## CBV
class CareerListView(ListView): # TODO: Rename to JobListView.
    """Show a list of jobs.
    
    The Career home page.
    """
    model = Post
    template_name = "jobs/career_.html"
    context_object_name = 'posts'

class JobDetailView(DetailView):
    """A job with its detail. Take an id and give a job."""
    model = Post
    template_name = "jobs/jobs_details_.html"
    context_object_name = 'post'

# class ApplyUpdateView(UpdateView):
#     model = Post
#     template_name = "jobs/apply_now.html"