from django.db import models
from django.urls import reverse

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    body_of_works = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'musician_id': self.id})