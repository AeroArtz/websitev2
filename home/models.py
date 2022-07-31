from django.db import models
from django.contrib.auth.models import User

class Artwork(models.Model):
    Painting_Title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    Available = models.BooleanField(default=True)
    size = models.CharField(max_length=100)
    price = models.CharField(max_length=100)



