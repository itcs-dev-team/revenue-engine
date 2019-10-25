from django.shortcuts import render

# Create your views here.
def career(request):
    """The Career page."""
    return render(request, 'jobs/career.html')

# level 2 pages

# career section
def apply_now(request):
    """The apply_now page."""
    return render(request, 'jobs/apply_now.html')