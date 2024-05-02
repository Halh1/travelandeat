from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Destination, Food
from .forms import FoodForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
@login_required
def destinations_index(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/index.html', {
        'destinations': destinations
    })
@login_required
def destinations_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)

    food_form = FoodForm()
    return render(request, 'destinations/detail.html', {
        'destination': destination, 
        'food_form': food_form
    })

class DestinationCreate(LoginRequiredMixin, CreateView):
    model = Destination
    fields = ('city', 'country')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


class DestinationUpdate(LoginRequiredMixin, UpdateView):
    model = Destination
    fields = ('city', 'country')

@login_required
def add_food(request, destination_id):
    form = FoodForm(request.POST)

    if form.is_valid():
        new_food = form.save(commit=False)
        new_food.destination_id = destination_id
        new_food.save()
    return redirect('detail', destination_id=destination_id)

class FoodUpdate(LoginRequiredMixin, UpdateView):
  model = Food
  fields = ('name', 'rating', 'comment')

class FoodDelete(LoginRequiredMixin, DeleteView):
  model = Food
  success_url = '/destinations'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # saving user to db
      user = form.save()
      # automatically login the new user
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
