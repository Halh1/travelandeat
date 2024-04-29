from django.db import models
from django.urls import reverse
# Create your models here.
class Destination(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'destination_id': self.id })
    