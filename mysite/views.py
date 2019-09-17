from django.shortcuts import render


from datetime import datetime
# Create your views here.
def index(request):
    """The home page of mysite."""
    # now = datetime.now()
    # current_time = {'current_time': str(now)}
    # return render(request, 'mysite/index.html', current_time)
    return render(request, 'mysite/index.html')

def services(request):
    """The service page."""
    return render(request, 'mysite/services.html')

def case_studies(request):
    """The Case Studies page."""
    return render(request, 'mysite/case_studies.html')
