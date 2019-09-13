from django.shortcuts import render


from datetime import datetime
# Create your views here.
def index(request):
    """The home page of mysite."""
    now = datetime.now()
    current_time = {'current_time': str(now)}
    return render(request, 'mysite/index.html', current_time)