from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations_index, name='destinations_index')
]
