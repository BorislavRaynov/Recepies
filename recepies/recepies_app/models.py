from django.db import models

# Create your models here.

class Recepie(models.Model):
    title = models.CharField(max_length=30)
    image = models.URLField()
    description = models.TextField()
    ingridients = models.CharField(max_length=250)
    time = models.IntegerField()
