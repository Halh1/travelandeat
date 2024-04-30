from django.contrib import admin

# Register your models here.
from .models import Destination, Food

admin.site.register([Destination, Food])