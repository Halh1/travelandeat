from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from .models import Destination
from .forms import FoodForm
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

    food_form = FoodForm()
    return render(request, 'destinations/detail.html', {
        'destination': destination,
        'food_form': food_form
    })

class DestinationCreate(CreateView):
    model = Destination
    fields = ('city', 'country')

class DestinationUpdate(UpdateView):
    model = Destination
    fields = ('city', 'country')


def add_food(request, destination_id):
    form = FoodForm(request.POST)

    if form.is_valid():
        new_food = form.save(commit=False)
        new_food.destination_id = destination_id
        new_food.save()
    return redirect('detail', destination_id=destination_id)
