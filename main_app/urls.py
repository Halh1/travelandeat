from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations_index, name='destinations_index'),
    path('destinations/<int:destination_id>/', views.destinations_detail, name='detail'),
    path('destinations/create/', views.DestinationCreate.as_view(), name='destinations_create'),
    path('destinations/<int:pk>/update/', views.DestinationUpdate.as_view(), name='destinations_update'),
    path('destinations/<int:destination_id>/add_food/', views.add_food, name='add_food'),
    path('cats/<int:pk>/update/', views.FoodUpdate.as_view(), name='food_update'),
    path('destinations/<int:pk>/delete/', views.FoodDelete.as_view(), name='food_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('destinations/<int:destination_id>/add_photo/', views.add_photo, name='add_photo'),
]
