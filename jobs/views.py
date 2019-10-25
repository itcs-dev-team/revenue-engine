from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView

from .models import Post
# Create your views here.
# def career(request):
#     """The Career home page."""
#     return render(request, 'jobs/career.html')

# level 2 pages

# career section
def apply_now(request):
    """The apply_now page."""
    return render(request, 'jobs/apply_now.html')

## CBV
class CareerListView(ListView):
    """The Career home page.
    
    It shows list of jobs."""
    model = Post
    template_name = "jobs/career_.html"
    context_object_name = 'all_jobs'
    
# class ApplyUpdateView(UpdateView):
#     model = Post
#     template_name = "jobs/apply_now.html"