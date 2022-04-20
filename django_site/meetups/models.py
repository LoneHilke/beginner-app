from django.db import models
from django.forms import CharField

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images')
