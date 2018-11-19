from django.db import models

class Cheese(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='media/photos/')

# Create your models here.
