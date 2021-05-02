from django.shortcuts import render
from .models import IPAddress


# Create your views here.
def home(request):
    ip_count = IPAddress.objects.all().count()
    return render(request, 'home.html', {'ip_count': ip_count})
