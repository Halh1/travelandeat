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
    

class Food(models.Model):
    RATINGS = (
        ('N/A', 'N/A'),
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1')
    )
    name = models.CharField(max_length=50)
    rating = models.CharField(max_length=3, choices=RATINGS, default='N/A')
    comment = models.TextField(max_length=300)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_rating_display()} from {self.name} and {self.comment}'
    