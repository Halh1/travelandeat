from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Destination

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def destinations_index(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/index.html', {
        'destinations': destinations
    })

def destinations_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    return render(request, 'destinations/detail.html', {
        'destination': destination
    })

class DestinationCreate(CreateView):
    model = Destination
    fields = ('city', 'country')