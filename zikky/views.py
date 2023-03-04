from django.shortcuts import render
from .models import Destination
# Create your views here.


def Homepage(request):

    dests = Destination.objects.all()
    
    return render(request, 'Homepage.html', {'dests': dests})
